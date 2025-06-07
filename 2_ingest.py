import datetime
import os 
import re
import urllib.parse

from db import VectorModel, session

from llama_index.core.node_parser import SentenceSplitter
from sentence_transformers import SentenceTransformer
embedding_model = SentenceTransformer('BAAI/bge-large-en-v1.5')


def load_files(path="./data/raw/md/"):
    for file in os.listdir(path):
        yield os.path.join(path, file)

def extract_markdown_links(text):
    pattern = r'## \[(.*?)\]\((https?://[^\s)]+)\)'
    matches = re.findall(pattern, text)
    
    links = [{'title': title, 'url': url} for title, url in matches]
    return links

def _remove_markdown_links(text):
    return re.sub(r'\[([^\]]+)\]\(https?://[^\s)]+\)', r'\1', text)

def _remove_up_to_double_newline(text):
    parts = text.split('\n\n\n', 1)
    return parts[1] if len(parts) > 1 else ''

def _remove_in_this_article_section(text):
    pattern = r'## In this article.*?\n\n'
    return re.sub(pattern, '', text, flags=re.DOTALL)

def prep_doc(doc):
    if doc[0] != "#":
        doc = _remove_up_to_double_newline(doc)
        doc = _remove_in_this_article_section(doc)
        doc = _remove_markdown_links(doc)
    return doc

def split_doc(doc):

    splitter = SentenceSplitter(
        chunk_size=800,
        chunk_overlap=100,
        paragraph_separator="\n\n"
    )
    return splitter.split_text(doc)

def run():
    chunks = []
    for file in load_files():
        filename = os.path.splitext(file.split("/")[-1])[0]
        print(filename)
        with open(file, 'r') as f:
            raw_doc = f.read()
        refs = extract_markdown_links(raw_doc)
        proc_doc = prep_doc(raw_doc)
        splitted_docs = split_doc(proc_doc)

        for doc_split in splitted_docs:
            doc_vector = embedding_model.encode(doc_split)
            session.add(
                VectorModel(
                    text=doc_split,
                    vector=doc_vector,
                    url=urllib.parse.unquote_plus(filename),
                    metadata_={
                        'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        'refs': refs
                    }
                )
            )
            session.commit()

            print(f"Done inserting: {filename}")

if __name__ == "__main__":

    from dotenv import load_dotenv

    load_dotenv()
    run()