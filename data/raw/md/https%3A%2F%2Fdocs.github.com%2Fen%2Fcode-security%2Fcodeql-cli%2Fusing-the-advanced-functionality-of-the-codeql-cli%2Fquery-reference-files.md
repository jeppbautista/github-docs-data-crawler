  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [Advanced functionality](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli "Advanced functionality")/
  * [Query reference files](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/query-reference-files "Query reference files")


# Query reference files
You can use query reference files to define the location of a query you want to run in tests.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [About query reference files](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/query-reference-files#about-query-reference-files)
  * [Defining a query reference file](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/query-reference-files#defining-a-query-reference-file)


## [About query reference files](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/query-reference-files#about-query-reference-files)
A query reference file is text file that defines the location of one query to test.
You use a query reference file when you want to tell the `test run` subcommand to run a query that’s not part of a test directory. There are two ways to specify queries that you want to run as tests:
  1. Use a query reference file to specify the location of a query to test. This is useful when you create tests for alert and path queries that are intended to identify problems in real codebases. You might create several directories of test code, each focusing on different aspects of the query. Then you would add a query reference file to each directory of test code, to specify the query to test.
  2. Add the query directly to a directory of tests. These is typically useful when you’re writing queries explicitly to test the behavior of QL libraries. Often these queries contain just a few calls to library predicates, wrapping them in a `select` statement so their output can be tested.


## [Defining a query reference file](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/query-reference-files#defining-a-query-reference-file)
Each query reference file, `.qlref`, contains a single line that defines where to find one query. The location must be defined relative to the root of the CodeQL pack that contains the query. Usually, this is either the CodeQL pack that contains the `.qlref`, a CodeQL pack specified in the `dependencies` block for the test pack, or a transitive dependency of the CodeQL pack.
You should use forward slashes in the path on all operating systems to ensure compatibility between systems.
### [Example](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/query-reference-files#example)
A query reference file to test a JavaScript alert query: [DeadAngularJSEventListener.qlref](https://github.com/github/codeql/blob/main/javascript/ql/test/query-tests/AngularJS/DeadAngularJSEventListener/DeadAngularJSEventListener.qlref)
The `qlpack.yml` file, <https://github.com/github/codeql/blob/main/javascript/ql/test/qlpack.yml>, for the CodeQL pack at `javascript/ql/test` defines `codeql/javascript-queries` as a dependency. So the query reference file defines the location of the query relative to the `codeql/javascript-queries` CodeQL pack:
```
AngularJS/DeadAngularJSEventListener.ql

```

For another example, see [Testing custom queries](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/testing-custom-queries).
