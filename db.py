from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import sessionmaker
from pgvector.sqlalchemy import Vector

import os

class Base(DeclarativeBase):
    ...

class VectorModel(Base):
    __tablename__ = 'vectors'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    url: Mapped[str] = mapped_column(Text)
    text: Mapped[str] = mapped_column(Text)
    vector = mapped_column(Vector(1024))
    metadata_: Mapped[dict | None] = mapped_column('metadata', JSONB)

    def __repr__(self):
        return f'Vector(id={self.id}, text={self.text[:50]}..., metadata={self.metadata_})'
    
from sqlalchemy import create_engine

user = os.getenv('USER')
password = os.getenv('PASSWORD')
rag_db = os.getenv('RAG_DB')

DB_URL = f"postgresql://{user}:{password}@localhost:5432/{rag_db}"

engine = create_engine(DB_URL)


Session = sessionmaker(bind=engine)
session = Session()

def db_create():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    db_create()
    print("Table created successfully.")