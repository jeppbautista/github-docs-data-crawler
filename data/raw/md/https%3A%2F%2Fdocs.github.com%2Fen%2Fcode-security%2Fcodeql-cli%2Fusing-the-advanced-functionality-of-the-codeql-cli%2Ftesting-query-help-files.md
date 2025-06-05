  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [Advanced functionality](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli "Advanced functionality")/
  * [Testing query help files](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/testing-query-help-files "Testing query help files")


# Testing query help files
You can use the CodeQL CLI to preview your query help files as Markdown and ensure they are valid.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [About testing query help files](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/testing-query-help-files#about-testing-query-help-files)
  * [Prerequisites](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/testing-query-help-files#prerequisites)
  * [Running codeql generate query-help](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/testing-query-help-files#running-codeql-generate-query-help)
  * [Results](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/testing-query-help-files#results)
  * [Further reading](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/testing-query-help-files#further-reading)


## [About testing query help files](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/testing-query-help-files#about-testing-query-help-files)
Test query help files by rendering them as Markdown to ensure they are valid before uploading them to the CodeQL repository or using them in code scanning.
Query help is documentation that accompanies a query to explain how the query works, as well as providing information about the potential problem that the query identifies. It is good practice to write query help for all new queries. For more information, see [Contributing to CodeQL](https://github.com/github/codeql/blob/main/CONTRIBUTING.md) in the CodeQL repository.
The CodeQL CLI includes a command to test query help and render the content as markdown, so that you can easily preview the content in your IDE. Use the command to validate query help files before uploading them to the CodeQL repository or sharing them with other users. From CodeQL CLI 2.7.1 onwards, you can also include the markdown-rendered query help in SARIF files generated during CodeQL analyses so that the query help can be displayed in the code scanning UI. For more information, see [Analyzing your code with CodeQL queries](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/analyzing-your-code-with-codeql-queries).
## [Prerequisites](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/testing-query-help-files#prerequisites)
  * The query help (`.qhelp`) file must have an accompanying query (`.ql`) file with an identical base name.
  * The query help file should follow the standard structure and style for query help documentation. For more information, see the [Query help style guide](https://github.com/github/codeql/blob/main/docs/query-help-style-guide.md) in the CodeQL repository.


## [Running `codeql generate query-help`](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/testing-query-help-files#running-codeql-generate-query-help)
You can test query help files by running the following command:
```
codeql generate query-help <qhelp|query|dir|suite> --format=<format> [--output=<dir|file>]

```

For this command `<qhelp|query|dir|suite>` must be the path to a `.qhelp` file, the path to a `.ql` file, the path to a directory containing queries and query help files, or the path to a query suite.
You must specify a `--format` option, which defines how the query help is rendered. Currently, you must specify `markdown` to render the query help as markdown.
The `--output` option defines a file path where the rendered query help will be saved.
  * For directories containing `.qhelp` files or a query suites defining one or more `.qhelp` files, you must specify an `--output` directory. Filenames within the output directory will be derived from the `.qhelp` file names.
  * For single `.qhelp` or `.ql` files, you may specify an `--output` option. If you don’t specify an output path, the rendered query help is written to `stdout`.


For full details of all the options you can use when testing query help files, see [generate query-help](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-query-help).
## [Results](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/testing-query-help-files#results)
When you run the command, CodeQL attempts to render each `.qhelp` file that has an accompanying `.ql` file. For single files, the rendered content will be printed to `stdout` if you don’t specify an `--output` option. For all other use cases, the rendered content is saved to the specified output path.
By default, the CodeQL CLI will print a warning message if:
  * Any of the query help is invalid, along with a description of the invalid query help elements
  * Any `.qhelp` files specified in the command don’t have the same base name as an accompanying `.ql` file
  * Any `.ql` files specified in the command don’t have the same base name as an accompanying `.qhelp` file


You can tell the CodeQL CLI how to handle these warnings by including a `--warnings` option in your command. For more information, see [generate query-help](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-query-help#--warningsmode).
## [Further reading](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/testing-query-help-files#further-reading)
  * [Query help files](https://codeql.github.com/docs/writing-codeql-queries/query-help-files/#query-help-files)


