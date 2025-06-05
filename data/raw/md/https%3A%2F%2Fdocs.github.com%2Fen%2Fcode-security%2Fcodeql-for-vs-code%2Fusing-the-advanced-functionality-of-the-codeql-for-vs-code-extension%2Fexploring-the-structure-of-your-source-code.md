  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL for VS Code](https://docs.github.com/en/code-security/codeql-for-vs-code "CodeQL for VS Code")/
  * [Advanced functionality](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension "Advanced functionality")/
  * [Explore code structure](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/exploring-the-structure-of-your-source-code "Explore code structure")


# Exploring the structure of your source code
You can use the AST viewer to display the abstract syntax tree of a CodeQL database.
## In this article
  * [About the abstract syntax tree](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/exploring-the-structure-of-your-source-code#about-the-abstract-syntax-tree)
  * [Viewing the abstract syntax tree of a source file](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/exploring-the-structure-of-your-source-code#viewing-the-abstract-syntax-tree-of-a-source-file)


## [About the abstract syntax tree](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/exploring-the-structure-of-your-source-code#about-the-abstract-syntax-tree)
The abstract syntax tree (AST) of a program represents the program's syntactic structure. Nodes on the AST represent elements such as statements and expressions. A CodeQL database encodes these program elements and the relationships between them through a database schema. For more information about database schemas, see [CodeQL glossary](https://codeql.github.com/docs/codeql-overview/codeql-glossary/#ql-database-schema) in the CodeQL documentation.
CodeQL for Visual Studio Code contains an AST viewer. The viewer consists of a graph visualization view that lets you explore the AST of a file in a CodeQL database. This helps you see which CodeQL classes correspond to which parts of your source files.
## [Viewing the abstract syntax tree of a source file](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/exploring-the-structure-of-your-source-code#viewing-the-abstract-syntax-tree-of-a-source-file)
If you don't have an appropriate query (usually `printAST.ql`) in your workspace, the **CodeQL: View AST** command in the following steps won't work. To fix this, you can update your copy of the [`github/codeql`](https://github.com/github/codeql) repository from the `main` branch. If you do this, query caches may be discarded, so your next query runs may be slower.
  1. Open the "Databases" view in the extension, and right-click the database that you want to explore. Click **Add Database Source to Workspace**.
  2. Navigate to a CodeQL database's source file in the File Explorer.
  3. Run **CodeQL: View AST** from the VS Code Command Palette. This runs a CodeQL query (usually called `printAST.ql`) over the active file, which may take a few seconds. Once the query is complete, the AST viewer will display the structure of the source file.
  4. To see the nested structure of the source file, click the arrows and expand the nodes.


You can click a node in the AST viewer to jump to it in the source code. Conversely, if you click a section of the source code, the AST viewer displays the corresponding node.
