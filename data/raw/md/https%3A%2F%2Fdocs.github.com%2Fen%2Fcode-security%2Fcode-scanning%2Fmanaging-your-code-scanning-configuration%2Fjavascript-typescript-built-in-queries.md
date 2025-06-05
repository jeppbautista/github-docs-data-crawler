  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Manage code scanning](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration "Manage code scanning")/
  * [JavaScript and TypeScript queries](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/javascript-typescript-built-in-queries "JavaScript and TypeScript queries")


# JavaScript and TypeScript queries for CodeQL analysis
Explore the queries that CodeQL uses to analyze code written in JavaScript or TypeScript when you select the `default` or the `security-extended` query suite.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


CodeQL includes many queries for analyzing JavaScript and TypeScript code. All queries in the `default` query suite are run by default. If you choose to use the `security-extended` query suite, additional queries are run. For more information, see [CodeQL query suites](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/built-in-codeql-query-suites).
## [Built-in queries for JavaScript and TypeScript analysis](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/javascript-typescript-built-in-queries#built-in-queries-for-javascript-and-typescript-analysis)
This table lists the queries available with the latest release of the CodeQL action and CodeQL CLI. For more information, see [CodeQL change logs](https://codeql.github.com/docs/codeql-overview/codeql-changelog/) in the CodeQL documentation site.
Query name | Related CWEs | Default | Extended | Copilot Autofix  
---|---|---|---|---  
[Arbitrary file access during archive extraction ("Zip Slip")](https://codeql.github.com/codeql-query-help/javascript/js-zipslip/) | 022 |  |  |   
[Bad HTML filtering regexp](https://codeql.github.com/codeql-query-help/javascript/js-bad-tag-filter/) | 020, 080, 116, 184, 185, 186 |  |  |   
[Case-sensitive middleware path](https://codeql.github.com/codeql-query-help/javascript/js-case-sensitive-middleware-path/) | 178 |  |  |   
[Clear text storage of sensitive information](https://codeql.github.com/codeql-query-help/javascript/js-clear-text-storage-of-sensitive-data/) | 312, 315, 359 |  |  |   
[Clear text transmission of sensitive cookie](https://codeql.github.com/codeql-query-help/javascript/js-clear-text-cookie/) | 614, 311, 312, 319 |  |  |   
[Clear-text logging of sensitive information](https://codeql.github.com/codeql-query-help/javascript/js-clear-text-logging/) | 312, 359, 532 |  |  |   
[Client-side cross-site scripting](https://codeql.github.com/codeql-query-help/javascript/js-xss/) | 079, 116 |  |  |   
[Client-side URL redirect](https://codeql.github.com/codeql-query-help/javascript/js-client-side-unvalidated-url-redirection/) | 079, 116, 601 |  |  |   
[Code injection](https://codeql.github.com/codeql-query-help/javascript/js-code-injection/) | 094, 095, 079, 116 |  |  |   
[CORS misconfiguration for credentials transfer](https://codeql.github.com/codeql-query-help/javascript/js-cors-misconfiguration-for-credentials/) | 346, 639, 942 |  |  |   
[Creating biased random numbers from a cryptographically secure source](https://codeql.github.com/codeql-query-help/javascript/js-biased-cryptographic-random/) | 327 |  |  |   
[Cross-window communication with unrestricted target origin](https://codeql.github.com/codeql-query-help/javascript/js-cross-window-information-leak/) | 201, 359 |  |  |   
[Database query built from user-controlled sources](https://codeql.github.com/codeql-query-help/javascript/js-sql-injection/) | 089, 090, 943 |  |  |   
[Dependency download using unencrypted communication channel](https://codeql.github.com/codeql-query-help/javascript/js-insecure-dependency/) | 300, 319, 494, 829 |  |  |   
[Deserialization of user-controlled data](https://codeql.github.com/codeql-query-help/javascript/js-unsafe-deserialization/) | 502 |  |  |   
[Disabling certificate validation](https://codeql.github.com/codeql-query-help/javascript/js-disabling-certificate-validation/) | 295, 297 |  |  |   
[Disabling Electron webSecurity](https://codeql.github.com/codeql-query-help/javascript/js-disabling-electron-websecurity/) | 079 |  |  |   
[Disabling SCE](https://codeql.github.com/codeql-query-help/javascript/js-angular-disabling-sce/) | 116 |  |  |   
[DOM text reinterpreted as HTML](https://codeql.github.com/codeql-query-help/javascript/js-xss-through-dom/) | 079, 116 |  |  |   
[Double compilation](https://codeql.github.com/codeql-query-help/javascript/js-angular-double-compilation/) | 1176 |  |  |   
[Double escaping or unescaping](https://codeql.github.com/codeql-query-help/javascript/js-double-escaping/) | 116, 020 |  |  |   
[Download of sensitive file through insecure connection](https://codeql.github.com/codeql-query-help/javascript/js-insecure-download/) | 829 |  |  |   
[Enabling Electron allowRunningInsecureContent](https://codeql.github.com/codeql-query-help/javascript/js-enabling-electron-insecure-content/) | 494 |  |  |   
[Exception text reinterpreted as HTML](https://codeql.github.com/codeql-query-help/javascript/js-xss-through-exception/) | 079, 116 |  |  |   
[Exposure of private files](https://codeql.github.com/codeql-query-help/javascript/js-exposure-of-private-files/) | 200, 219, 548 |  |  |   
[Expression injection in Actions](https://codeql.github.com/codeql-query-help/javascript/js-actions-command-injection/) | 094 |  |  |   
[Host header poisoning in email generation](https://codeql.github.com/codeql-query-help/javascript/js-host-header-forgery-in-email-generation/) | 640 |  |  |   
[Improper code sanitization](https://codeql.github.com/codeql-query-help/javascript/js-bad-code-sanitization/) | 094, 079, 116 |  |  |   
[Inclusion of functionality from an untrusted source](https://codeql.github.com/codeql-query-help/javascript/js-functionality-from-untrusted-source/) | 830 |  |  |   
[Incomplete HTML attribute sanitization](https://codeql.github.com/codeql-query-help/javascript/js-incomplete-html-attribute-sanitization/) | 079, 116, 020 |  |  |   
[Incomplete multi-character sanitization](https://codeql.github.com/codeql-query-help/javascript/js-incomplete-multi-character-sanitization/) | 020, 080, 116 |  |  |   
[Incomplete regular expression for hostnames](https://codeql.github.com/codeql-query-help/javascript/js-incomplete-hostname-regexp/) | 020 |  |  |   
[Incomplete string escaping or encoding](https://codeql.github.com/codeql-query-help/javascript/js-incomplete-sanitization/) | 020, 080, 116 |  |  |   
[Incomplete URL scheme check](https://codeql.github.com/codeql-query-help/javascript/js-incomplete-url-scheme-check/) | 020, 184 |  |  |   
[Incomplete URL substring sanitization](https://codeql.github.com/codeql-query-help/javascript/js-incomplete-url-substring-sanitization/) | 020 |  |  |   
[Incorrect suffix check](https://codeql.github.com/codeql-query-help/javascript/js-incorrect-suffix-check/) | 020 |  |  |   
[Inefficient regular expression](https://codeql.github.com/codeql-query-help/javascript/js-redos/) | 1333, 730, 400 |  |  |   
[Information exposure through a stack trace](https://codeql.github.com/codeql-query-help/javascript/js-stack-trace-exposure/) | 209, 497 |  |  |   
[Insecure configuration of Helmet security middleware](https://codeql.github.com/codeql-query-help/javascript/js-insecure-helmet-configuration/) | 693, 1021 |  |  |   
[Insecure randomness](https://codeql.github.com/codeql-query-help/javascript/js-insecure-randomness/) | 338 |  |  |   
[Insecure URL whitelist](https://codeql.github.com/codeql-query-help/javascript/js-angular-insecure-url-whitelist/) | 183, 625 |  |  |   
[JWT missing secret or public key verification](https://codeql.github.com/codeql-query-help/javascript/js-jwt-missing-verification/) | 347 |  |  |   
[Loop bound injection](https://codeql.github.com/codeql-query-help/javascript/js-loop-bound-injection/) | 834, 730 |  |  |   
[Missing CSRF middleware](https://codeql.github.com/codeql-query-help/javascript/js-missing-token-validation/) | 352 |  |  |   
[Missing rate limiting](https://codeql.github.com/codeql-query-help/javascript/js-missing-rate-limiting/) | 770, 307, 400 |  |  |   
[Overly permissive regular expression range](https://codeql.github.com/codeql-query-help/javascript/js-overly-large-range/) | 020 |  |  |   
[Polynomial regular expression used on uncontrolled data](https://codeql.github.com/codeql-query-help/javascript/js-polynomial-redos/) | 1333, 730, 400 |  |  |   
[Prototype-polluting assignment](https://codeql.github.com/codeql-query-help/javascript/js-prototype-polluting-assignment/) | 078, 079, 094, 400, 471, 915 |  |  |   
[Prototype-polluting function](https://codeql.github.com/codeql-query-help/javascript/js-prototype-pollution-utility/) | 078, 079, 094, 400, 471, 915 |  |  |   
[Prototype-polluting merge call](https://codeql.github.com/codeql-query-help/javascript/js-prototype-pollution/) | 078, 079, 094, 400, 471, 915 |  |  |   
[Reflected cross-site scripting](https://codeql.github.com/codeql-query-help/javascript/js-reflected-xss/) | 079, 116 |  |  |   
[Regular expression injection](https://codeql.github.com/codeql-query-help/javascript/js-regex-injection/) | 730, 400 |  |  |   
[Replacement of a substring with itself](https://codeql.github.com/codeql-query-help/javascript/js-identity-replacement/) | 116 |  |  |   
[Resource exhaustion](https://codeql.github.com/codeql-query-help/javascript/js-resource-exhaustion/) | 400, 770 |  |  |   
[Resources exhaustion from deep object traversal](https://codeql.github.com/codeql-query-help/javascript/js-resource-exhaustion-from-deep-object-traversal/) | 400 |  |  |   
[Second order command injection](https://codeql.github.com/codeql-query-help/javascript/js-second-order-command-line-injection/) | 078, 088 |  |  |   
[Sensitive data read from GET request](https://codeql.github.com/codeql-query-help/javascript/js-sensitive-get-query/) | 598 |  |  |   
[Sensitive server cookie exposed to the client](https://codeql.github.com/codeql-query-help/javascript/js-client-exposed-cookie/) | 1004 |  |  |   
[Server crash](https://codeql.github.com/codeql-query-help/javascript/js-server-crash/) | 248, 730 |  |  |   
[Server-side request forgery](https://codeql.github.com/codeql-query-help/javascript/js-request-forgery/) | 918 |  |  |   
[Server-side URL redirect](https://codeql.github.com/codeql-query-help/javascript/js-server-side-unvalidated-url-redirection/) | 601 |  |  |   
[Shell command built from environment values](https://codeql.github.com/codeql-query-help/javascript/js-shell-command-injection-from-environment/) | 078, 088 |  |  |   
[Storage of sensitive information in build artifact](https://codeql.github.com/codeql-query-help/javascript/js-build-artifact-leak/) | 312, 315, 359 |  |  |   
[Storage of sensitive information in GitHub Actions artifact](https://codeql.github.com/codeql-query-help/javascript/js-actions-actions-artifact-leak/) | 312, 315, 359 |  |  |   
[Stored cross-site scripting](https://codeql.github.com/codeql-query-help/javascript/js-stored-xss/) | 079, 116 |  |  |   
[Template Object Injection](https://codeql.github.com/codeql-query-help/javascript/js-template-object-injection/) | 073, 094 |  |  |   
[Type confusion through parameter tampering](https://codeql.github.com/codeql-query-help/javascript/js-type-confusion-through-parameter-tampering/) | 843 |  |  |   
[Uncontrolled command line](https://codeql.github.com/codeql-query-help/javascript/js-command-line-injection/) | 078, 088 |  |  |   
[Uncontrolled data used in path expression](https://codeql.github.com/codeql-query-help/javascript/js-path-injection/) | 022, 023, 036, 073, 099 |  |  |   
[Unnecessary use of `cat` process](https://codeql.github.com/codeql-query-help/javascript/js-unnecessary-use-of-cat/) | 078 |  |  |   
[Unsafe dynamic method access](https://codeql.github.com/codeql-query-help/javascript/js-unsafe-dynamic-method-access/) | 094 |  |  |   
[Unsafe expansion of self-closing HTML tag](https://codeql.github.com/codeql-query-help/javascript/js-unsafe-html-expansion/) | 079, 116 |  |  |   
[Unsafe HTML constructed from library input](https://codeql.github.com/codeql-query-help/javascript/js-html-constructed-from-input/) | 079, 116 |  |  |   
[Unsafe jQuery plugin](https://codeql.github.com/codeql-query-help/javascript/js-unsafe-jquery-plugin/) | 079, 116 |  |  |   
[Unsafe shell command constructed from library input](https://codeql.github.com/codeql-query-help/javascript/js-shell-command-constructed-from-input/) | 078, 088 |  |  |   
[Untrusted domain used in script or other content](https://codeql.github.com/codeql-query-help/javascript/js-functionality-from-untrusted-domain/) | 830 |  |  |   
[Unvalidated dynamic method call](https://codeql.github.com/codeql-query-help/javascript/js-unvalidated-dynamic-method-call/) | 754 |  |  |   
[Use of a broken or weak cryptographic algorithm](https://codeql.github.com/codeql-query-help/javascript/js-weak-cryptographic-algorithm/) | 327, 328 |  |  |   
[Use of a weak cryptographic key](https://codeql.github.com/codeql-query-help/javascript/js-insufficient-key-size/) | 326 |  |  |   
[Use of externally-controlled format string](https://codeql.github.com/codeql-query-help/javascript/js-tainted-format-string/) | 134 |  |  |   
[Use of password hash with insufficient computational effort](https://codeql.github.com/codeql-query-help/javascript/js-insufficient-password-hash/) | 916 |  |  |   
[Useless regular-expression character escape](https://codeql.github.com/codeql-query-help/javascript/js-useless-regexp-character-escape/) | 020 |  |  |   
[XML external entity expansion](https://codeql.github.com/codeql-query-help/javascript/js-xxe/) | 611, 827 |  |  |   
[XML internal entity expansion](https://codeql.github.com/codeql-query-help/javascript/js-xml-bomb/) | 776, 400 |  |  |   
[XPath injection](https://codeql.github.com/codeql-query-help/javascript/js-xpath-injection/) | 643 |  |  |   
[Client-side request forgery](https://codeql.github.com/codeql-query-help/javascript/js-client-side-request-forgery/) | 918 |  |  |   
[Empty password in configuration file](https://codeql.github.com/codeql-query-help/javascript/js-empty-password-in-configuration-file/) | 258, 862 |  |  |   
[Failure to abandon session](https://codeql.github.com/codeql-query-help/javascript/js-session-fixation/) | 384 |  |  |   
[File data in outbound network request](https://codeql.github.com/codeql-query-help/javascript/js-file-access-to-http/) | 200 |  |  |   
[Hard-coded data interpreted as code](https://codeql.github.com/codeql-query-help/javascript/js-hardcoded-data-interpreted-as-code/) | 506 |  |  |   
[Indirect uncontrolled command line](https://codeql.github.com/codeql-query-help/javascript/js-indirect-command-line-injection/) | 078, 088 |  |  |   
[Insecure temporary file](https://codeql.github.com/codeql-query-help/javascript/js-insecure-temporary-file/) | 377, 378 |  |  |   
[Log injection](https://codeql.github.com/codeql-query-help/javascript/js-log-injection/) | 117 |  |  |   
[Missing origin verification in `postMessage` handler](https://codeql.github.com/codeql-query-help/javascript/js-missing-origin-check/) | 020, 940 |  |  |   
[Missing regular expression anchor](https://codeql.github.com/codeql-query-help/javascript/js-regex-missing-regexp-anchor/) | 020 |  |  |   
[Network data written to file](https://codeql.github.com/codeql-query-help/javascript/js-http-to-file-access/) | 912, 434 |  |  |   
[Potential file system race condition](https://codeql.github.com/codeql-query-help/javascript/js-file-system-race/) | 367 |  |  |   
[Remote property injection](https://codeql.github.com/codeql-query-help/javascript/js-remote-property-injection/) | 250, 400 |  |  |   
[Sensitive cookie without SameSite restrictions](https://codeql.github.com/codeql-query-help/javascript/js-samesite-none-cookie/) | 1275 |  |  |   
[Unsafe code constructed from library input](https://codeql.github.com/codeql-query-help/javascript/js-unsafe-code-construction/) | 094, 079, 116 |  |  |   
[User-controlled bypass of security check](https://codeql.github.com/codeql-query-help/javascript/js-user-controlled-bypass/) | 807, 290 |  |  | 
