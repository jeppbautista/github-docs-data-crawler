  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Manage code scanning](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration "Manage code scanning")/
  * [C# CodeQL queries](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/csharp-built-in-queries "C# CodeQL queries")


# C# queries for CodeQL analysis
Explore the queries that CodeQL uses to analyze code written in C# when you select the `default` or the `security-extended` query suite.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


CodeQL includes many queries for analyzing C# code. All queries in the `default` query suite are run by default. If you choose to use the `security-extended` query suite, additional queries are run. For more information, see [CodeQL query suites](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/built-in-codeql-query-suites).
## [Built-in queries for C# analysis](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/csharp-built-in-queries#built-in-queries-for-c-analysis)
This table lists the queries available with the latest release of the CodeQL action and CodeQL CLI. For more information, see [CodeQL change logs](https://codeql.github.com/docs/codeql-overview/codeql-changelog/) in the CodeQL documentation site.
Query name | Related CWEs | Default | Extended | Copilot Autofix  
---|---|---|---|---  
['requireSSL' attribute is not set to true](https://codeql.github.com/codeql-query-help/csharp/cs-web-requiressl-not-set/) | 319, 614 |  |  |   
[Arbitrary file access during archive extraction ("Zip Slip")](https://codeql.github.com/codeql-query-help/csharp/cs-zipslip/) | 022 |  |  |   
[ASP.NET config file enables directory browsing](https://codeql.github.com/codeql-query-help/csharp/cs-web-directory-browse-enabled/) | 548 |  |  |   
[Assembly path injection](https://codeql.github.com/codeql-query-help/csharp/cs-assembly-path-injection/) | 114 |  |  |   
[Clear text storage of sensitive information](https://codeql.github.com/codeql-query-help/csharp/cs-cleartext-storage-of-sensitive-information/) | 312, 315, 359 |  |  |   
[Cookie security: overly broad domain](https://codeql.github.com/codeql-query-help/csharp/cs-web-broad-cookie-domain/) | 287 |  |  |   
[Cookie security: overly broad path](https://codeql.github.com/codeql-query-help/csharp/cs-web-broad-cookie-path/) | 287 |  |  |   
[Cookie security: persistent cookie](https://codeql.github.com/codeql-query-help/csharp/cs-web-persistent-cookie/) | 539 |  |  |   
[Creating an ASP.NET debug binary may reveal sensitive information](https://codeql.github.com/codeql-query-help/csharp/cs-web-debug-binary/) | 011, 532 |  |  |   
[Cross-site scripting](https://codeql.github.com/codeql-query-help/csharp/cs-web-xss/) | 079, 116 |  |  |   
[Denial of Service from comparison of user input against expensive regex](https://codeql.github.com/codeql-query-help/csharp/cs-redos/) | 1333, 730, 400 |  |  |   
[Deserialization of untrusted data](https://codeql.github.com/codeql-query-help/csharp/cs-unsafe-deserialization-untrusted-input/) | 502 |  |  |   
[Deserialized delegate](https://codeql.github.com/codeql-query-help/csharp/cs-deserialized-delegate/) | 502 |  |  |   
[Encryption using ECB](https://codeql.github.com/codeql-query-help/csharp/cs-ecb-encryption/) | 327 |  |  |   
[Exposure of private information](https://codeql.github.com/codeql-query-help/csharp/cs-exposure-of-sensitive-information/) | 359 |  |  |   
[Failure to abandon session](https://codeql.github.com/codeql-query-help/csharp/cs-session-reuse/) | 384 |  |  |   
[Header checking disabled](https://codeql.github.com/codeql-query-help/csharp/cs-web-disabled-header-checking/) | 113 |  |  |   
[Improper control of generation of code](https://codeql.github.com/codeql-query-help/csharp/cs-code-injection/) | 094, 095, 096 |  |  |   
[Information exposure through an exception](https://codeql.github.com/codeql-query-help/csharp/cs-information-exposure-through-exception/) | 209, 497 |  |  |   
[Information exposure through transmitted data](https://codeql.github.com/codeql-query-help/csharp/cs-sensitive-data-transmission/) | 201 |  |  |   
[Insecure randomness](https://codeql.github.com/codeql-query-help/csharp/cs-insecure-randomness/) | 338 |  |  |   
[LDAP query built from user-controlled sources](https://codeql.github.com/codeql-query-help/csharp/cs-ldap-injection/) | 090 |  |  |   
[Log entries created from user input](https://codeql.github.com/codeql-query-help/csharp/cs-log-forging/) | 117 |  |  |   
[Missing cross-site request forgery token validation](https://codeql.github.com/codeql-query-help/csharp/cs-web-missing-token-validation/) | 352 |  |  |   
[Missing global error handler](https://codeql.github.com/codeql-query-help/csharp/cs-web-missing-global-error-handler/) | 012, 248 |  |  |   
[Missing X-Frame-Options HTTP header](https://codeql.github.com/codeql-query-help/csharp/cs-web-missing-x-frame-options/) | 451, 829 |  |  |   
[Page request validation is disabled](https://codeql.github.com/codeql-query-help/csharp/cs-web-request-validation-disabled/) | 016 |  |  |   
[Regular expression injection](https://codeql.github.com/codeql-query-help/csharp/cs-regex-injection/) | 730, 400 |  |  |   
[Resource injection](https://codeql.github.com/codeql-query-help/csharp/cs-resource-injection/) | 099 |  |  |   
[SQL query built from user-controlled sources](https://codeql.github.com/codeql-query-help/csharp/cs-sql-injection/) | 089 |  |  |   
[Uncontrolled command line](https://codeql.github.com/codeql-query-help/csharp/cs-command-line-injection/) | 078, 088 |  |  |   
[Uncontrolled data used in path expression](https://codeql.github.com/codeql-query-help/csharp/cs-path-injection/) | 022, 023, 036, 073, 099 |  |  |   
[Uncontrolled format string](https://codeql.github.com/codeql-query-help/csharp/cs-uncontrolled-format-string/) | 134 |  |  |   
[Untrusted XML is read insecurely](https://codeql.github.com/codeql-query-help/csharp/cs-xml-insecure-dtd-handling/) | 611, 827, 776 |  |  |   
[Unvalidated local pointer arithmetic](https://codeql.github.com/codeql-query-help/csharp/cs-unvalidated-local-pointer-arithmetic/) | 119, 120, 122, 788 |  |  |   
[URL redirection from remote source](https://codeql.github.com/codeql-query-help/csharp/cs-web-unvalidated-url-redirection/) | 601 |  |  |   
[User-controlled bypass of sensitive method](https://codeql.github.com/codeql-query-help/csharp/cs-user-controlled-bypass/) | 807, 247, 350 |  |  |   
[Weak encryption](https://codeql.github.com/codeql-query-help/csharp/cs-weak-encryption/) | 327 |  |  |   
[Weak encryption: inadequate RSA padding](https://codeql.github.com/codeql-query-help/csharp/cs-inadequate-rsa-padding/) | 327, 780 |  |  |   
[Weak encryption: Insufficient key size](https://codeql.github.com/codeql-query-help/csharp/cs-insufficient-key-size/) | 326 |  |  |   
[XML injection](https://codeql.github.com/codeql-query-help/csharp/cs-xml-injection/) | 091 |  |  |   
[XPath injection](https://codeql.github.com/codeql-query-help/csharp/cs-xml-xpath-injection/) | 643 |  |  |   
[Empty password in configuration file](https://codeql.github.com/codeql-query-help/csharp/cs-empty-password-in-configuration/) | 258, 862 |  |  |   
[Insecure Direct Object Reference](https://codeql.github.com/codeql-query-help/csharp/cs-web-insecure-direct-object-reference/) | 639 |  |  |   
[Insecure SQL connection](https://codeql.github.com/codeql-query-help/csharp/cs-insecure-sql-connection/) | 327 |  |  |   
[Missing function level access control](https://codeql.github.com/codeql-query-help/csharp/cs-web-missing-function-level-access-control/) | 285, 284, 862 |  |  |   
[Missing XML validation](https://codeql.github.com/codeql-query-help/csharp/cs-xml-missing-validation/) | 112 |  |  |   
[Serialization check bypass](https://codeql.github.com/codeql-query-help/csharp/cs-serialization-check-bypass/) | 020 |  |  |   
[Thread-unsafe capturing of an ICryptoTransform object](https://codeql.github.com/codeql-query-help/csharp/cs-thread-unsafe-icryptotransform-captured-in-lambda/) | 362 |  |  |   
[Thread-unsafe use of a static ICryptoTransform field](https://codeql.github.com/codeql-query-help/csharp/cs-thread-unsafe-icryptotransform-field-in-class/) | 362 |  |  |   
[Use of file upload](https://codeql.github.com/codeql-query-help/csharp/cs-web-file-upload/) | 434 |  |  |   
[Value shadowing](https://codeql.github.com/codeql-query-help/csharp/cs-web-ambiguous-client-variable/) | 348 |  |  |   
[Value shadowing: server variable](https://codeql.github.com/codeql-query-help/csharp/cs-web-ambiguous-server-variable/) | 348 |  |  | 
