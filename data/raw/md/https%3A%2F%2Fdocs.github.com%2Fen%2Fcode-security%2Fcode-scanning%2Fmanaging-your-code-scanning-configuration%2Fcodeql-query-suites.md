  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Manage code scanning](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration "Manage code scanning")/
  * [CodeQL query suites](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/codeql-query-suites "CodeQL query suites")


# CodeQL query suites
You can choose from different built-in CodeQL query suites to use in your CodeQL code scanning setup.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [About CodeQL query suites](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/codeql-query-suites#about-codeql-query-suites)
  * [Built-in CodeQL query suites](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/codeql-query-suites#built-in-codeql-query-suites)
  * [Query lists for the default query suites](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/codeql-query-suites#query-lists-for-the-default-query-suites)
  * [Further reading](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/codeql-query-suites#further-reading)


## [About CodeQL query suites](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/codeql-query-suites#about-codeql-query-suites)
With CodeQL code scanning, you can select a specific group of CodeQL queries, called a CodeQL query suite, to run against your code. The following built-in query suites are available through GitHub:
  * `default` query suite.
  * `security-extended` query suite. This suite is referred to as the "Extended" query suite on GitHub.


Currently, both the `default` query suite and the `security-extended` query suite are available for default setup for code scanning. Additionally, organization owners and security managers can recommend a query suite for use with default setup throughout their organization. For more information on configuring default setup for individual repositories, see [Configuring default setup for code scanning](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning). For more information on configuring default setup at scale and recommending a query suite, see [Configuring default setup for code scanning at scale](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning-at-scale).
To use a custom query suite, you must configure advanced setup for CodeQL code scanning. For more information on advanced setups and creating a query suite, see [Configuring advanced setup for code scanning](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning#configuring-advanced-setup-for-code-scanning-with-codeql) and [Creating CodeQL query suites](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/creating-codeql-query-suites).
## [Built-in CodeQL query suites](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/codeql-query-suites#built-in-codeql-query-suites)
The built-in CodeQL query suites, `default` and `security-extended`, are created and maintained by GitHub. Both of these query suites are available for every CodeQL-supported language. For more information on CodeQL-supported languages, see [About code scanning with CodeQL](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql#about-codeql).
### [`default` query suite](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/codeql-query-suites#default-query-suite)
  * The `default` query suite is the group of queries run by default in CodeQL code scanning on GitHub.
  * The queries in the `default` query suite are highly precise and return few false positive code scanning results. Relative to the `security-extended` query suite, the `default` suite returns fewer low-confidence code scanning results.
  * This query suite is available for use with default setup for code scanning.


### [`security-extended` query suite](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/codeql-query-suites#security-extended-query-suite)
  * The `security-extended` query suite consists of all the queries in the `default` query suite, plus additional queries with slightly lower precision and severity.
  * Relative to the `default` query suite, the `security-extended` suite may return a greater number of false positive code scanning results.
  * This query suite is available for use with default setup for code scanning, and is referred to as the "Extended" query suite on GitHub.


## [Query lists for the default query suites](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/codeql-query-suites#query-lists-for-the-default-query-suites)
For each language, the following article lists which queries are included in the `default` and the `security-extended` suites. Where Copilot Autofix is available for a language, details of which queries are supported are also included.
  * [Actions queries for CodeQL analysis](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/actions-built-in-queries)
  * [C and C++ queries for CodeQL analysis](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/c-cpp-built-in-queries)
  * [C# queries for CodeQL analysis](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/csharp-built-in-queries)
  * [GitHub Actions queries for CodeQL analysis](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/github-actions-built-in-queries)
  * [Go queries for CodeQL analysis](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/go-built-in-queries)
  * [Java and Kotlin queries for CodeQL analysis](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/java-kotlin-built-in-queries)
  * [JavaScript and TypeScript queries for CodeQL analysis](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/javascript-typescript-built-in-queries)
  * [Python queries for CodeQL analysis](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/python-built-in-queries)
  * [Ruby queries for CodeQL analysis](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/ruby-built-in-queries)
  * [Swift queries for CodeQL analysis](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/swift-built-in-queries)


## [Further reading](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/codeql-query-suites#further-reading)
  * [Creating CodeQL query suites](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/creating-codeql-query-suites)


