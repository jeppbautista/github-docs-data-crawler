  * [Get started](https://docs.github.com/en/get-started "Get started")/
  * [Learn to code](https://docs.github.com/en/get-started/learning-to-code "Learn to code")/
  * [Finding example code](https://docs.github.com/en/get-started/learning-to-code/finding-and-understanding-example-code "Finding example code")


# Finding and understanding example code
Improve your coding skills by learning from example code on GitHub.
## In this article
  * [How can I learn from code on GitHub?](https://docs.github.com/en/get-started/learning-to-code/finding-and-understanding-example-code#how-can-i-learn-from-code-on-github)
  * [Finding an example project](https://docs.github.com/en/get-started/learning-to-code/finding-and-understanding-example-code#finding-an-example-project)
  * [Orienting yourself within the project](https://docs.github.com/en/get-started/learning-to-code/finding-and-understanding-example-code#orienting-yourself-within-the-project)
  * [Navigating the source code](https://docs.github.com/en/get-started/learning-to-code/finding-and-understanding-example-code#navigating-the-source-code)
  * [Understanding the source code](https://docs.github.com/en/get-started/learning-to-code/finding-and-understanding-example-code#understanding-the-source-code)
  * [Next steps](https://docs.github.com/en/get-started/learning-to-code/finding-and-understanding-example-code#next-steps)


## [How can I learn from code on GitHub?](https://docs.github.com/en/get-started/learning-to-code/finding-and-understanding-example-code#how-can-i-learn-from-code-on-github)
Learning from projects on GitHub is a great way of **learning new techniques** and **finding inspiration** for your own projects.
However, with millions of publicly available repositories on GitHub, finding code that applies to your project can be overwhelming. Even after you find the perfect repository, it can be difficult to navigate the codebase to find useful examples.
Instead of trying to understand an entire project, a better approach is to pick a single feature or function and see how it works. We can use Copilot Chat and GitHub's search functionality to locate a feature and follow it through the codebase. This is a great way to learn as we can see how the feature works all the way from the backend to the frontend.
In this guide, you'll learn how to do both by following an **example scenario** : learning how to load and display data from files on a Jekyll website. Then, you can apply the tips and techniques to other projects and programming languages.
## [Finding an example project](https://docs.github.com/en/get-started/learning-to-code/finding-and-understanding-example-code#finding-an-example-project)
The first step is to find the right project to learn from.
### [Use Copilot Chat to identify a repository](https://docs.github.com/en/get-started/learning-to-code/finding-and-understanding-example-code#use-copilot-chat-to-identify-a-repository)
The fastest way to find a project with code that you can learn from is to ask [Copilot Chat](https://github.com/copilot) to find repositories that match your criteria.
Open [Copilot Chat](https://github.com/copilot) and start a general purpose chat. Then ask:
> Can you find some popular repositories that use Jekyll to display data from files in the repository?
Copilot will return links to relevant repositories, and you can ask follow-up questions about the repositories.
Often, Copilot will end its response with a link to GitHub search with more results. Next, we'll review these results.
### [Using search to identify more options](https://docs.github.com/en/get-started/learning-to-code/finding-and-understanding-example-code#using-search-to-identify-more-options)
If Copilot included a link to search results, follow the link. If not, form your own search query by following the steps below.
  1. Navigate to [Advanced search](https://github.com/search/advanced).
  2. In the "Advanced options" section, use the "Written in this language" dropdown to select a programming language. For our Jekyll site, we'll select "HTML".
  3. Optionally, under "Repositories options", next to "With this many stars", type `>150`. This will help you find popular repositories that are likely well maintained.
  4. Back at the top of the page, click **Search**.


We can further narrow down your search results by adding topics and text to the search query. For example, `topic:jekyll "blog"` would return repositories the owner has classified as related to Jekyll and with the word "blog" in the repository name or description. For a list of popular topics, see [Topics on GitHub](https://github.com/topics).
### [Choosing a project](https://docs.github.com/en/get-started/learning-to-code/finding-and-understanding-example-code#choosing-a-project)
After reviewing the results from Copilot and search, we decide to use the [`github/choosealicense.com`](https://github.com/github/choosealicense.com) repository. This repository contains the source code for [Choose a License](https://choosealicense.com/), a Jekyll website that shares information about open source licenses.
We're particularly interested in the [Licenses](https://choosealicense.com/licenses/) page, which displays popular open source licenses from data files. 
## [Orienting yourself within the project](https://docs.github.com/en/get-started/learning-to-code/finding-and-understanding-example-code#orienting-yourself-within-the-project)
Before we dig into the code for displaying data files, let's orient ourselves in the repository in general.
It can be difficult to know where to start when you first visit a repository. While each project will organize itself in its own individual way, there are common documentation methods that we can usually rely upon to get our bearings.
### [The README.md file](https://docs.github.com/en/get-started/learning-to-code/finding-and-understanding-example-code#the-readmemd-file)
It's always a good idea to read the **README.md** file, which is the front page of a repository and is automatically rendered beneath the list of files. Different maintainers will include different information, but you can often find information about the project, how to build it on your local machine, and links to documentation.
In the [`github/choosealicense.com`](https://github.com/github/choosealicense.com) repository, the README.md file explains where the license files live (`/_licenses`), the attributes each license can have, and how to get the website running on your computer.
### [Using Copilot Chat](https://docs.github.com/en/get-started/learning-to-code/finding-and-understanding-example-code#using-copilot-chat)
If the README.md file doesn't give you all the answers, you can ask Copilot to help you navigate the repository and locate functionality.
To open Copilot Chat, click the 
> What is the main landing page for this Jekyll website?
When you ask Copilot questions about a repository, it can return the relevant files, explain the part they play in the functionality, and include links.
### [The repository's wiki](https://docs.github.com/en/get-started/learning-to-code/finding-and-understanding-example-code#the-repositorys-wiki)
Another possible source of information is the repository's **wiki** , a section of the repository specifically for hosting documentation. Every repository on GitHub comes equipped with the ability to use a wiki, but not every repository uses it. To access the wiki, click the 
### [Releases](https://docs.github.com/en/get-started/learning-to-code/finding-and-understanding-example-code#releases)
If the repository's source code builds into an executable file, some repository maintainers will use the repository's **releases** to publish binary files. You can download and run these binary files to examine how the application works while exploring the codebase, without needing to build the project yourself.
You can find a repository's releases in the sidebar, to the right of the list of files and README.md.
### [Internal documentation](https://docs.github.com/en/get-started/learning-to-code/finding-and-understanding-example-code#internal-documentation)
You can also look for internal documentation in the repository's contents. This could be a single Markdown file or a directory full of Markdown files. Common names to look for include "docs", "documentation", "wiki", "resources", "help", and "manual".
## [Navigating the source code](https://docs.github.com/en/get-started/learning-to-code/finding-and-understanding-example-code#navigating-the-source-code)
Now that we understand the overall structure of the repository, it's time to use GitHub search to find to the specific functionality we're looking for.
When you're in a repository and click into the search field at the top of the page, GitHub will automatically add the `repo` search qualifier so your search results are constrained to the repository you're viewing.
To get started, we need something to search for. This could be a string of text unique to the feature we're examining, or we could look at the HTML source of the page and find a particular `class` or `id` attribute.
In our example, we'll search for the text at the top of the [licenses page](https://choosealicense.com/licenses/), using this query: [`repo:github/choosealicense "If you’re looking for a reference table?"`](https://github.com/search?q=repo%3Agithub%2Fchoosealicense.com+%22If+you%E2%80%99re+looking+for+a+reference+table%22&type=code). This returns one result, a file named `licenses.html`.
Now we can click on the result and dig deeper! [`licenses.html`](https://github.com/github/choosealicense.com/blob/gh-pages/licenses.html) is the source of the "Licences" page we were looking for. We can see the string that we searched for and that each of the licenses is included with the code below:
```
{% include license-overview.html license-id="agpl-3.0" %}

```

## [Understanding the source code](https://docs.github.com/en/get-started/learning-to-code/finding-and-understanding-example-code#understanding-the-source-code)
Now that we've found the specific code we're interested in, we can move on to understanding it.
### [Asking Copilot Chat about the code](https://docs.github.com/en/get-started/learning-to-code/finding-and-understanding-example-code#asking-copilot-chat-about-the-code)
You can use Copilot to learn more about a file or even specific lines of code. Copilot will combine information about the programming language with the context from the repository to answer your questions in great detail.
Let's ask Copilot to explain what's happening on line 11, with the `{% include %}` tag. Click the line number. Then, to the right of the line, click 
> What's happening in this line?
Copilot will explain that the line is including the `license-overview.html` file and passing along `"agpl-3.0"` as the `license-id` to display.
If you don't understand a response from Copilot Chat, you can always ask it to simplify the answer or expand on a particular part of it.
### [Reading comments](https://docs.github.com/en/get-started/learning-to-code/finding-and-understanding-example-code#reading-comments)
Comments are human readable annotations that you can use to understand the code and are not executed. They are usually delimited with characters such as `//` or `/*`.
There are a few types of comments to look for:
  * **Line** : Single-line comments that describe what a particular line is doing
  * **Block** : Multi-line comments that might describe what an entire function or file is doing
  * **File** : A block comment at the very beginning of a file, providing an overview of that particular part of the codebase


### [Looking up functions in programming language references](https://docs.github.com/en/get-started/learning-to-code/finding-and-understanding-example-code#looking-up-functions-in-programming-language-references)
Every programming language will have a reference online, explaining every aspect of the language.
If you use a search engine to search for the programming language and the function, you should find a link to that function's reference page.
For our example, searching for `jekyll include` in a search engine should return the ["Includes" documentation](https://jekyllrb.com/docs/includes/) in the Jekyll documentation. If we read further into Jekyll's documentation, we can see that the licenses themselves are a [collection](https://jekyllrb.com/docs/collections/) in the [`_licenses`](https://github.com/github/choosealicense.com/tree/gh-pages/_licenses) directory.
If you can't find a function in a programming language reference, it's likely that the function is defined in the codebase itself. Ask [GitHub Copilot](https://github.com/copilot) to locate it.
To summarize what we've learned: the [`licenses.html`](https://github.com/github/choosealicense.com/blob/gh-pages/licenses.html) file includes [`/_includes/license-overview.html`](https://github.com/github/choosealicense.com/blob/gh-pages/_includes/license-overview.html) for each license shown. The [`/_includes/license-overview.html`](https://github.com/github/choosealicense.com/blob/gh-pages/_includes/license-overview.html) file matches the `license-id` provided to a license in the [`/_licenses`](https://github.com/github/choosealicense.com/tree/gh-pages/_licenses) collection and renders the details.
### [Experimenting with small changes](https://docs.github.com/en/get-started/learning-to-code/finding-and-understanding-example-code#experimenting-with-small-changes)
If you're able to run the project locally on your computer, a great way to learn is to make little changes to see what happens.
You can start by changing text, then move on to making bigger changes, such as experimenting with how functions and files interact with each other.
Try finding the [`license-overview.html`](https://github.com/github/choosealicense.com/blob/gh-pages/_includes/license-overview.html) file in the `_includes` directory, then making changes to how the license is displayed or experimenting with how the license is loaded from the collection.
You could change the metadata at the beginning of one of the license files, change which attributes are displayed in `license-overview.html`, or even try adding your own attribute. When you've made your change, you can test it by following the README.md instructions to view it in your browser.
### [Applying what we've learnt](https://docs.github.com/en/get-started/learning-to-code/finding-and-understanding-example-code#applying-what-weve-learnt)
The [`github/choosealicense.com`](https://github.com/github/choosealicense.com) repository is a great example of a large Jekyll project and demonstrates just how much is possible with Jekyll and GitHub Pages. Can you apply what you've learnt from the structure of the repository, how it uses collections, and the way it includes the license data to build your own project?
## [Next steps](https://docs.github.com/en/get-started/learning-to-code/finding-and-understanding-example-code#next-steps)
Now that you understand how the example code works, you may want to reuse it in your own project. Code reuse is a powerful part of software development, but there are important steps to follow to do it correctly and legally. For a full tutorial, see [Reusing other people's code in your projects](https://docs.github.com/en/get-started/learning-to-code/reusing-other-peoples-code-in-your-projects).
