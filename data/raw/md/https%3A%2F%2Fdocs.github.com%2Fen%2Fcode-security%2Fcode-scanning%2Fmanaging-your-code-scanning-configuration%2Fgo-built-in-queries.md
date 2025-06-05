  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Manage code scanning](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration "Manage code scanning")/
  * [Go CodeQL queries](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/go-built-in-queries "Go CodeQL queries")


# Go queries for CodeQL analysis
Explore the queries that CodeQL uses to analyze code written in Go (Golang) when you select the `default` or the `security-extended` query suite.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


CodeQL includes many queries for analyzing Go code. All queries in the `default` query suite are run by default. If you choose to use the `security-extended` query suite, additional queries are run. For more information, see [CodeQL query suites](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/built-in-codeql-query-suites).
## [Built-in queries for Go analysis](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/go-built-in-queries#built-in-queries-for-go-analysis)
This table lists the queries available with the latest release of the CodeQL action and CodeQL CLI. For more information, see [CodeQL change logs](https://codeql.github.com/docs/codeql-overview/codeql-changelog/) in the CodeQL documentation site.
Query name | Related CWEs | Default | Extended | Copilot Autofix  
---|---|---|---|---  
[Arbitrary file access during archive extraction ("Zip Slip")](https://codeql.github.com/codeql-query-help/go/go-zipslip/) | 022 |  |  |   
[Arbitrary file write extracting an archive containing symbolic links](https://codeql.github.com/codeql-query-help/go/go-unsafe-unzip-symlink/) | 022 |  |  |   
[Bad redirect check](https://codeql.github.com/codeql-query-help/go/go-bad-redirect-check/) | 601 |  |  |   
[Clear-text logging of sensitive information](https://codeql.github.com/codeql-query-help/go/go-clear-text-logging/) | 312, 315, 359 |  |  |   
[Command built from user-controlled sources](https://codeql.github.com/codeql-query-help/go/go-command-injection/) | 078 |  |  |   
[Database query built from user-controlled sources](https://codeql.github.com/codeql-query-help/go/go-sql-injection/) | 089 |  |  |   
[Disabled TLS certificate check](https://codeql.github.com/codeql-query-help/go/go-disabled-certificate-check/) | 295 |  |  |   
[Email content injection](https://codeql.github.com/codeql-query-help/go/go-email-injection/) | 640 |  |  |   
[Incomplete regular expression for hostnames](https://codeql.github.com/codeql-query-help/go/go-incomplete-hostname-regexp/) | 020 |  |  |   
[Incomplete URL scheme check](https://codeql.github.com/codeql-query-help/go/go-incomplete-url-scheme-check/) | 020 |  |  |   
[Incorrect conversion between integer types](https://codeql.github.com/codeql-query-help/go/go-incorrect-integer-conversion/) | 190, 681 |  |  |   
[Information exposure through a stack trace](https://codeql.github.com/codeql-query-help/go/go-stack-trace-exposure/) | 209, 497 |  |  |   
[Insecure TLS configuration](https://codeql.github.com/codeql-query-help/go/go-insecure-tls/) | 327 |  |  |   
[Missing JWT signature check](https://codeql.github.com/codeql-query-help/go/go-missing-jwt-signature-check/) | 347 |  |  |   
[Missing regular expression anchor](https://codeql.github.com/codeql-query-help/go/go-regex-missing-regexp-anchor/) | 020 |  |  |   
[Open URL redirect](https://codeql.github.com/codeql-query-help/go/go-unvalidated-url-redirection/) | 601 |  |  |   
[Potentially unsafe quoting](https://codeql.github.com/codeql-query-help/go/go-unsafe-quoting/) | 078, 089, 094 |  |  |   
[Reflected cross-site scripting](https://codeql.github.com/codeql-query-help/go/go-reflected-xss/) | 079, 116 |  |  |   
[Size computation for allocation may overflow](https://codeql.github.com/codeql-query-help/go/go-allocation-size-overflow/) | 190 |  |  |   
[Slice memory allocation with excessive size value](https://codeql.github.com/codeql-query-help/go/go-uncontrolled-allocation-size/) | 770 |  |  |   
[Suspicious characters in a regular expression](https://codeql.github.com/codeql-query-help/go/go-suspicious-character-in-regex/) | 020 |  |  |   
[Uncontrolled data used in network request](https://codeql.github.com/codeql-query-help/go/go-request-forgery/) | 918 |  |  |   
[Uncontrolled data used in path expression](https://codeql.github.com/codeql-query-help/go/go-path-injection/) | 022, 023, 036, 073, 099 |  |  |   
[Use of a weak cryptographic key](https://codeql.github.com/codeql-query-help/go/go-weak-crypto-key/) | 326 |  |  |   
[Use of constant `state` value in OAuth 2.0 URL](https://codeql.github.com/codeql-query-help/go/go-constant-oauth2-state/) | 352 |  |  |   
[Use of insecure HostKeyCallback implementation](https://codeql.github.com/codeql-query-help/go/go-insecure-hostkeycallback/) | 322 |  |  |   
[Use of insufficient randomness as the key of a cryptographic algorithm](https://codeql.github.com/codeql-query-help/go/go-insecure-randomness/) | 338 |  |  |   
[XPath injection](https://codeql.github.com/codeql-query-help/go/go-xml-xpath-injection/) | 643 |  |  |   
[Log entries created from user input](https://codeql.github.com/codeql-query-help/go/go-log-injection/) | 117 |  |  | 
