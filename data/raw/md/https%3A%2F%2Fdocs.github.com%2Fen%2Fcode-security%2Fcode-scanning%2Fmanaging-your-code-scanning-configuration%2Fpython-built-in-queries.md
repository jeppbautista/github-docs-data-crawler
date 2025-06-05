  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Manage code scanning](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration "Manage code scanning")/
  * [Python CodeQL queries](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/python-built-in-queries "Python CodeQL queries")


# Python queries for CodeQL analysis
Explore the queries that CodeQL uses to analyze code written in Python when you select the `default` or the `security-extended` query suite.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


CodeQL includes many queries for analyzing Python code. All queries in the `default` query suite are run by default. If you choose to use the `security-extended` query suite, additional queries are run. For more information, see [CodeQL query suites](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/built-in-codeql-query-suites).
## [Built-in queries for Python analysis](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/python-built-in-queries#built-in-queries-for-python-analysis)
This table lists the queries available with the latest release of the CodeQL action and CodeQL CLI. For more information, see [CodeQL change logs](https://codeql.github.com/docs/codeql-overview/codeql-changelog/) in the CodeQL documentation site.
Query name | Related CWEs | Default | Extended | Copilot Autofix  
---|---|---|---|---  
['input' function used in Python 2](https://codeql.github.com/codeql-query-help/python/py-use-of-input/) | 094, 095 |  |  |   
[Accepting unknown SSH host keys when using Paramiko](https://codeql.github.com/codeql-query-help/python/py-paramiko-missing-host-key-validation/) | 295 |  |  |   
[Bad HTML filtering regexp](https://codeql.github.com/codeql-query-help/python/py-bad-tag-filter/) | 116, 020, 185, 186 |  |  |   
[Binding a socket to all network interfaces](https://codeql.github.com/codeql-query-help/python/py-bind-socket-all-network-interfaces/) | 200 |  |  |   
[Clear-text logging of sensitive information](https://codeql.github.com/codeql-query-help/python/py-clear-text-logging-sensitive-data/) | 312, 359, 532 |  |  |   
[Clear-text storage of sensitive information](https://codeql.github.com/codeql-query-help/python/py-clear-text-storage-sensitive-data/) | 312, 315, 359 |  |  |   
[Code injection](https://codeql.github.com/codeql-query-help/python/py-code-injection/) | 094, 095, 116 |  |  |   
[Construction of a cookie using user-supplied input](https://codeql.github.com/codeql-query-help/python/py-cookie-injection/) | 020 |  |  |   
[CSRF protection weakened or disabled](https://codeql.github.com/codeql-query-help/python/py-csrf-protection-disabled/) | 352 |  |  |   
[Default version of SSL/TLS may be insecure](https://codeql.github.com/codeql-query-help/python/py-insecure-default-protocol/) | 327 |  |  |   
[Deserialization of user-controlled data](https://codeql.github.com/codeql-query-help/python/py-unsafe-deserialization/) | 502 |  |  |   
[Failure to use secure cookies](https://codeql.github.com/codeql-query-help/python/py-insecure-cookie/) | 614, 1004, 1275 |  |  |   
[Flask app is run in debug mode](https://codeql.github.com/codeql-query-help/python/py-flask-debug/) | 215, 489 |  |  |   
[Full server-side request forgery](https://codeql.github.com/codeql-query-help/python/py-full-ssrf/) | 918 |  |  |   
[HTTP Response Splitting](https://codeql.github.com/codeql-query-help/python/py-http-response-splitting/) | 113, 079 |  |  |   
[Incomplete regular expression for hostnames](https://codeql.github.com/codeql-query-help/python/py-incomplete-hostname-regexp/) | 020 |  |  |   
[Incomplete URL substring sanitization](https://codeql.github.com/codeql-query-help/python/py-incomplete-url-substring-sanitization/) | 020 |  |  |   
[Inefficient regular expression](https://codeql.github.com/codeql-query-help/python/py-redos/) | 1333, 730, 400 |  |  |   
[Information exposure through an exception](https://codeql.github.com/codeql-query-help/python/py-stack-trace-exposure/) | 209, 497 |  |  |   
[Insecure temporary file](https://codeql.github.com/codeql-query-help/python/py-insecure-temporary-file/) | 377 |  |  |   
[LDAP query built from user-controlled sources](https://codeql.github.com/codeql-query-help/python/py-ldap-injection/) | 090 |  |  |   
[NoSQL Injection](https://codeql.github.com/codeql-query-help/python/py-nosql-injection/) | 943 |  |  |   
[Overly permissive regular expression range](https://codeql.github.com/codeql-query-help/python/py-overly-large-range/) | 020 |  |  |   
[PAM authorization bypass due to incorrect usage](https://codeql.github.com/codeql-query-help/python/py-pam-auth-bypass/) | 285 |  |  |   
[Polynomial regular expression used on uncontrolled data](https://codeql.github.com/codeql-query-help/python/py-polynomial-redos/) | 1333, 730, 400 |  |  |   
[Reflected server-side cross-site scripting](https://codeql.github.com/codeql-query-help/python/py-reflective-xss/) | 079, 116 |  |  |   
[Regular expression injection](https://codeql.github.com/codeql-query-help/python/py-regex-injection/) | 730, 400 |  |  |   
[Server Side Template Injection](https://codeql.github.com/codeql-query-help/python/py-template-injection/) | 074 |  |  |   
[SQL query built from user-controlled sources](https://codeql.github.com/codeql-query-help/python/py-sql-injection/) | 089 |  |  |   
[Uncontrolled command line](https://codeql.github.com/codeql-query-help/python/py-command-line-injection/) | 078, 088 |  |  |   
[Uncontrolled data used in path expression](https://codeql.github.com/codeql-query-help/python/py-path-injection/) | 022, 023, 036, 073, 099 |  |  |   
[URL redirection from remote source](https://codeql.github.com/codeql-query-help/python/py-url-redirection/) | 601 |  |  |   
[Use of a broken or weak cryptographic algorithm](https://codeql.github.com/codeql-query-help/python/py-weak-cryptographic-algorithm/) | 327 |  |  |   
[Use of a broken or weak cryptographic hashing algorithm on sensitive data](https://codeql.github.com/codeql-query-help/python/py-weak-sensitive-data-hashing/) | 327, 328, 916 |  |  |   
[Use of insecure SSL/TLS version](https://codeql.github.com/codeql-query-help/python/py-insecure-protocol/) | 327 |  |  |   
[Use of weak cryptographic key](https://codeql.github.com/codeql-query-help/python/py-weak-crypto-key/) | 326 |  |  |   
[XML external entity expansion](https://codeql.github.com/codeql-query-help/python/py-xxe/) | 611, 827 |  |  |   
[XML internal entity expansion](https://codeql.github.com/codeql-query-help/python/py-xml-bomb/) | 776, 400 |  |  |   
[XPath query built from user-controlled sources](https://codeql.github.com/codeql-query-help/python/py-xpath-injection/) | 643 |  |  |   
[Arbitrary file write during tarfile extraction](https://codeql.github.com/codeql-query-help/python/py-tarslip/) | 022 |  |  |   
[Jinja2 templating with autoescape=False](https://codeql.github.com/codeql-query-help/python/py-jinja2-autoescape-false/) | 079 |  |  |   
[Log Injection](https://codeql.github.com/codeql-query-help/python/py-log-injection/) | 117 |  |  |   
[Overly permissive file permissions](https://codeql.github.com/codeql-query-help/python/py-overly-permissive-file/) | 732 |  |  |   
[Partial server-side request forgery](https://codeql.github.com/codeql-query-help/python/py-partial-ssrf/) | 918 |  |  |   
[Request without certificate validation](https://codeql.github.com/codeql-query-help/python/py-request-without-cert-validation/) | 295 |  |  |   
[Unsafe shell command constructed from library input](https://codeql.github.com/codeql-query-help/python/py-shell-command-constructed-from-input/) | 078, 088, 073 |  |  | 
