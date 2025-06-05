  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Manage code scanning](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration "Manage code scanning")/
  * [Swift CodeQL queries](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/swift-built-in-queries "Swift CodeQL queries")


# Swift queries for CodeQL analysis
Explore the queries that CodeQL uses to analyze code written in Swift when you select the `default` or the `security-extended` query suite.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


CodeQL includes many queries for analyzing Swift code. All queries in the `default` query suite are run by default. If you choose to use the `security-extended` query suite, additional queries are run. For more information, see [CodeQL query suites](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/built-in-codeql-query-suites).
## [Built-in queries for Swift analysis](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/swift-built-in-queries#built-in-queries-for-swift-analysis)
This table lists the queries available with the latest release of the CodeQL action and CodeQL CLI. For more information, see [CodeQL change logs](https://codeql.github.com/docs/codeql-overview/codeql-changelog/) in the CodeQL documentation site.
Query name | Related CWEs | Default | Extended | Copilot Autofix  
---|---|---|---|---  
[Bad HTML filtering regexp](https://codeql.github.com/codeql-query-help/swift/swift-bad-tag-filter/) | 116, 020, 185, 186 |  |  |   
[Cleartext logging of sensitive information](https://codeql.github.com/codeql-query-help/swift/swift-cleartext-logging/) | 312, 359, 532 |  |  |   
[Cleartext storage of sensitive information in a local database](https://codeql.github.com/codeql-query-help/swift/swift-cleartext-storage-database/) | 312 |  |  |   
[Cleartext storage of sensitive information in an application preference store](https://codeql.github.com/codeql-query-help/swift/swift-cleartext-storage-preferences/) | 312 |  |  |   
[Cleartext transmission of sensitive information](https://codeql.github.com/codeql-query-help/swift/swift-cleartext-transmission/) | 319 |  |  |   
[Database query built from user-controlled sources](https://codeql.github.com/codeql-query-help/swift/swift-sql-injection/) | 089 |  |  |   
[Encryption using ECB](https://codeql.github.com/codeql-query-help/swift/swift-ecb-encryption/) | 327 |  |  |   
[Incomplete regular expression for hostnames](https://codeql.github.com/codeql-query-help/swift/swift-incomplete-hostname-regexp/) | 020 |  |  |   
[Inefficient regular expression](https://codeql.github.com/codeql-query-help/swift/swift-redos/) | 1333, 730, 400 |  |  |   
[Insecure TLS configuration](https://codeql.github.com/codeql-query-help/swift/swift-insecure-tls/) | 757 |  |  |   
[Insufficient hash iterations](https://codeql.github.com/codeql-query-help/swift/swift-insufficient-hash-iterations/) | 916 |  |  |   
[Missing regular expression anchor](https://codeql.github.com/codeql-query-help/swift/swift-missing-regexp-anchor/) | 020 |  |  |   
[Predicate built from user-controlled sources](https://codeql.github.com/codeql-query-help/swift/swift-predicate-injection/) | 943 |  |  |   
[Regular expression injection](https://codeql.github.com/codeql-query-help/swift/swift-regex-injection/) | 730, 400 |  |  |   
[Resolving XML external entity in user-controlled data](https://codeql.github.com/codeql-query-help/swift/swift-xxe/) | 611, 776, 827 |  |  |   
[Static initialization vector for encryption](https://codeql.github.com/codeql-query-help/swift/swift-static-initialization-vector/) | 329, 1204 |  |  |   
[String length conflation](https://codeql.github.com/codeql-query-help/swift/swift-string-length-conflation/) | 135 |  |  |   
[System command built from user-controlled sources](https://codeql.github.com/codeql-query-help/swift/swift-command-line-injection/) | 078, 088 |  |  |   
[Uncontrolled data used in path expression](https://codeql.github.com/codeql-query-help/swift/swift-path-injection/) | 022, 023, 036, 073, 099 |  |  |   
[Uncontrolled format string](https://codeql.github.com/codeql-query-help/swift/swift-uncontrolled-format-string/) | 134 |  |  |   
[Unsafe WebView fetch](https://codeql.github.com/codeql-query-help/swift/swift-unsafe-webview-fetch/) | 079, 095, 749 |  |  |   
[Use of a broken or weak cryptographic hashing algorithm on sensitive data](https://codeql.github.com/codeql-query-help/swift/swift-weak-sensitive-data-hashing/) | 327, 328 |  |  |   
[Use of an inappropriate cryptographic hashing algorithm on passwords](https://codeql.github.com/codeql-query-help/swift/swift-weak-password-hashing/) | 327, 328, 916 |  |  |   
[Use of constant salts](https://codeql.github.com/codeql-query-help/swift/swift-constant-salt/) | 760 |  |  |   
[JavaScript Injection](https://codeql.github.com/codeql-query-help/swift/swift-unsafe-js-eval/) | 094, 095, 749 |  |  | 
