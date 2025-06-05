  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL for VS Code](https://docs.github.com/en/code-security/codeql-for-vs-code "CodeQL for VS Code")/
  * [Getting started](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code "Getting started")/
  * [Manage CodeQL databases](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/managing-codeql-databases "Manage CodeQL databases")


# Managing CodeQL databases
You can work with CodeQL databases using the extension.
## In this article
  * [About CodeQL databases](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/managing-codeql-databases#about-codeql-databases)
  * [Choosing a database to analyze](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/managing-codeql-databases#choosing-a-database-to-analyze)
  * [Filtering databases and queries by language](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/managing-codeql-databases#filtering-databases-and-queries-by-language)
  * [Next steps](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/managing-codeql-databases#next-steps)


## [About CodeQL databases](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/managing-codeql-databases#about-codeql-databases)
To analyze a project, you need to select a CodeQL database for that project. You can select a database locally (from a ZIP archive or an unarchived folder), from a public URL, or from a project's URL on GitHub. Alternatively, you can create a database using the CodeQL CLI, see [Preparing your code for CodeQL analysis](https://docs.github.com/en/code-security/codeql-cli/using-the-codeql-cli/creating-codeql-databases).
### [Downloading a database from GitHub](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/managing-codeql-databases#downloading-a-database-from-github)
GitHub.com stores CodeQL databases for over 200,000 open source repositories that you can use to test your analysis on.
You can check if a repository has any CodeQL databases available for download, and if so download it, using the REST API. For more information, see [List CodeQL databases for a repository](https://docs.github.com/en/rest/code-scanning/code-scanning#list-codeql-databases-for-a-repository) and [Get a CodeQL database for a repository](https://docs.github.com/en/rest/code-scanning/code-scanning#get-a-codeql-database-for-a-repository) in the GitHub REST API documentation.
## [Choosing a database to analyze](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/managing-codeql-databases#choosing-a-database-to-analyze)
  1. Hover over the title bar of the "Databases" view and choose the appropriate icon to select your database. You can select a local database (from a ZIP archive or an unarchived folder), from a public URL, or from a project's URL on GitHub.
  2. Once you've chosen a database, it will be displayed in the "Databases" view. To see the menu options for interacting with a database, right-click an entry in the list. You can select multiple databases at once.


You can also analyze test databases. Test databases (folders with a `.testproj` extension) are generated when you run regression tests on custom queries using the CodeQL CLI. If a query fails a regression test, you may want to import the test database into Visual Studio Code to debug the failure. For more information about running query tests, see [Testing custom queries](https://docs.github.com/en/code-security/codeql-cli/using-the-codeql-cli/testing-custom-queries).
## [Filtering databases and queries by language](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/managing-codeql-databases#filtering-databases-and-queries-by-language)
Optionally, to see databases containing a specific language and queries written for that language, you can apply a language filter using the language selector.
  1. To see available language filters, in the sidebar, open the "Language" view.
  2. Hover over the language filter you would like to apply, then click **Select**.


## [Next steps](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/managing-codeql-databases#next-steps)
To learn how to use the extension to analyze your projects by running queries on CodeQL databases, see [Running CodeQL queries](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/running-codeql-queries).
