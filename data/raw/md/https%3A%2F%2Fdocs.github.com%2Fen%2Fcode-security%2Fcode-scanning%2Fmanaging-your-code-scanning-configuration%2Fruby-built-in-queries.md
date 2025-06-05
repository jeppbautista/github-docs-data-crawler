  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Manage code scanning](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration "Manage code scanning")/
  * [Ruby CodeQL queries](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/ruby-built-in-queries "Ruby CodeQL queries")


# Ruby queries for CodeQL analysis
Explore the queries that CodeQL uses to analyze code written in Ruby when you select the `default` or the `security-extended` query suite.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


CodeQL includes many queries for analyzing Ruby code. All queries in the `default` query suite are run by default. If you choose to use the `security-extended` query suite, additional queries are run. For more information, see [CodeQL query suites](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/built-in-codeql-query-suites).
## [Built-in queries for Ruby analysis](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/ruby-built-in-queries#built-in-queries-for-ruby-analysis)
This table lists the queries available with the latest release of the CodeQL action and CodeQL CLI. For more information, see [CodeQL change logs](https://codeql.github.com/docs/codeql-overview/codeql-changelog/) in the CodeQL documentation site.
Query name | Related CWEs | Default | Extended | Copilot Autofix  
---|---|---|---|---  
[Bad HTML filtering regexp](https://codeql.github.com/codeql-query-help/ruby/rb-bad-tag-filter/) | 116, 020, 185, 186 |  |  |   
[Badly anchored regular expression](https://codeql.github.com/codeql-query-help/ruby/rb-regex-badly-anchored-regexp/) | 020 |  |  |   
[Clear-text logging of sensitive information](https://codeql.github.com/codeql-query-help/ruby/rb-clear-text-logging-sensitive-data/) | 312, 359, 532 |  |  |   
[Clear-text storage of sensitive information](https://codeql.github.com/codeql-query-help/ruby/rb-clear-text-storage-sensitive-data/) | 312, 359, 532 |  |  |   
[Code injection](https://codeql.github.com/codeql-query-help/ruby/rb-code-injection/) | 094, 095, 116 |  |  |   
[CSRF protection not enabled](https://codeql.github.com/codeql-query-help/ruby/rb-csrf-protection-not-enabled/) | 352 |  |  |   
[CSRF protection weakened or disabled](https://codeql.github.com/codeql-query-help/ruby/rb-csrf-protection-disabled/) | 352 |  |  |   
[Dependency download using unencrypted communication channel](https://codeql.github.com/codeql-query-help/ruby/rb-insecure-dependency/) | 300, 319, 494, 829 |  |  |   
[Deserialization of user-controlled data](https://codeql.github.com/codeql-query-help/ruby/rb-unsafe-deserialization/) | 502 |  |  |   
[Download of sensitive file through insecure connection](https://codeql.github.com/codeql-query-help/ruby/rb-insecure-download/) | 829 |  |  |   
[Incomplete multi-character sanitization](https://codeql.github.com/codeql-query-help/ruby/rb-incomplete-multi-character-sanitization/) | 020, 080, 116 |  |  |   
[Incomplete regular expression for hostnames](https://codeql.github.com/codeql-query-help/ruby/rb-incomplete-hostname-regexp/) | 020 |  |  |   
[Incomplete string escaping or encoding](https://codeql.github.com/codeql-query-help/ruby/rb-incomplete-sanitization/) | 020, 080, 116 |  |  |   
[Incomplete URL substring sanitization](https://codeql.github.com/codeql-query-help/ruby/rb-incomplete-url-substring-sanitization/) | 020 |  |  |   
[Inefficient regular expression](https://codeql.github.com/codeql-query-help/ruby/rb-redos/) | 1333, 730, 400 |  |  |   
[Information exposure through an exception](https://codeql.github.com/codeql-query-help/ruby/rb-stack-trace-exposure/) | 209, 497 |  |  |   
[Insecure Mass Assignment](https://codeql.github.com/codeql-query-help/ruby/rb-insecure-mass-assignment/) | 915 |  |  |   
[Overly permissive regular expression range](https://codeql.github.com/codeql-query-help/ruby/rb-overly-large-range/) | 020 |  |  |   
[Polynomial regular expression used on uncontrolled data](https://codeql.github.com/codeql-query-help/ruby/rb-polynomial-redos/) | 1333, 730, 400 |  |  |   
[Reflected server-side cross-site scripting](https://codeql.github.com/codeql-query-help/ruby/rb-reflected-xss/) | 079, 116 |  |  |   
[Regular expression injection](https://codeql.github.com/codeql-query-help/ruby/rb-regexp-injection/) | 1333, 730, 400 |  |  |   
[Sensitive data read from GET request](https://codeql.github.com/codeql-query-help/ruby/rb-sensitive-get-query/) | 598 |  |  |   
[Server-side request forgery](https://codeql.github.com/codeql-query-help/ruby/rb-request-forgery/) | 918 |  |  |   
[SQL query built from user-controlled sources](https://codeql.github.com/codeql-query-help/ruby/rb-sql-injection/) | 089 |  |  |   
[Stored cross-site scripting](https://codeql.github.com/codeql-query-help/ruby/rb-stored-xss/) | 079, 116 |  |  |   
[Uncontrolled command line](https://codeql.github.com/codeql-query-help/ruby/rb-command-line-injection/) | 078, 088 |  |  |   
[Uncontrolled data used in path expression](https://codeql.github.com/codeql-query-help/ruby/rb-path-injection/) | 022, 023, 036, 073, 099 |  |  |   
[Unsafe HTML constructed from library input](https://codeql.github.com/codeql-query-help/ruby/rb-html-constructed-from-input/) | 079, 116 |  |  |   
[Unsafe shell command constructed from library input](https://codeql.github.com/codeql-query-help/ruby/rb-shell-command-constructed-from-input/) | 078, 088, 073 |  |  |   
[URL redirection from remote source](https://codeql.github.com/codeql-query-help/ruby/rb-url-redirection/) | 601 |  |  |   
[Use of `Kernel.open` or `IO.read` or similar sinks with a non-constant value](https://codeql.github.com/codeql-query-help/ruby/rb-non-constant-kernel-open/) | 078, 088, 073 |  |  |   
[Use of `Kernel.open`, `IO.read` or similar sinks with user-controlled input](https://codeql.github.com/codeql-query-help/ruby/rb-kernel-open/) | 078, 088, 073 |  |  |   
[Use of a broken or weak cryptographic algorithm](https://codeql.github.com/codeql-query-help/ruby/rb-weak-cryptographic-algorithm/) | 327 |  |  |   
[Use of a broken or weak cryptographic hashing algorithm on sensitive data](https://codeql.github.com/codeql-query-help/ruby/rb-weak-sensitive-data-hashing/) | 327, 328, 916 |  |  |   
[Use of externally-controlled format string](https://codeql.github.com/codeql-query-help/ruby/rb-tainted-format-string/) | 134 |  |  |   
[Weak cookie configuration](https://codeql.github.com/codeql-query-help/ruby/rb-weak-cookie-configuration/) | 732, 1275 |  |  |   
[XML external entity expansion](https://codeql.github.com/codeql-query-help/ruby/rb-xxe/) | 611, 776, 827 |  |  |   
[Hard-coded data interpreted as code](https://codeql.github.com/codeql-query-help/ruby/rb-hardcoded-data-interpreted-as-code/) | 506 |  |  |   
[Log injection](https://codeql.github.com/codeql-query-help/ruby/rb-log-injection/) | 117 |  |  |   
[Missing regular expression anchor](https://codeql.github.com/codeql-query-help/ruby/rb-regex-missing-regexp-anchor/) | 020 |  |  |   
[Network data written to file](https://codeql.github.com/codeql-query-help/ruby/rb-http-to-file-access/) | 912, 434 |  |  |   
[Request without certificate validation](https://codeql.github.com/codeql-query-help/ruby/rb-request-without-cert-validation/) | 295 |  |  |   
[Unsafe code constructed from library input](https://codeql.github.com/codeql-query-help/ruby/rb-unsafe-code-construction/) | 094, 079, 116 |  |  | 
