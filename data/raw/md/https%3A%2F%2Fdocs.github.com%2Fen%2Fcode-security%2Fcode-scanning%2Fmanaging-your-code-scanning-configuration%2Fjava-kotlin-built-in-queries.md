  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Manage code scanning](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration "Manage code scanning")/
  * [Java and Kotlin CodeQL queries](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/java-kotlin-built-in-queries "Java and Kotlin CodeQL queries")


# Java and Kotlin queries for CodeQL analysis
Explore the queries that CodeQL uses to analyze code written in Java or Kotlin when you select the `default` or the `security-extended` query suite.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


CodeQL includes many queries for analyzing Java and Kotlin code. All queries in the `default` query suite are run by default. If you choose to use the `security-extended` query suite, additional queries are run. For more information, see [CodeQL query suites](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/built-in-codeql-query-suites).
## [Built-in queries for Java and Kotlin analysis](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/java-kotlin-built-in-queries#built-in-queries-for-java-and-kotlin-analysis)
This table lists the queries available with the latest release of the CodeQL action and CodeQL CLI. For more information, see [CodeQL change logs](https://codeql.github.com/docs/codeql-overview/codeql-changelog/) in the CodeQL documentation site.
Query name | Related CWEs | Default | Extended | Copilot Autofix  
---|---|---|---|---  
[`TrustManager` that accepts all certificates](https://codeql.github.com/codeql-query-help/java/java-insecure-trustmanager/) | 295 |  |  |   
[Android `WebView` that accepts all certificates](https://codeql.github.com/codeql-query-help/java/java-improper-webview-certificate-validation/) | 295 |  |  |   
[Android debuggable attribute enabled](https://codeql.github.com/codeql-query-help/java/java-android-debuggable-attribute-enabled/) | 489 |  |  |   
[Android fragment injection](https://codeql.github.com/codeql-query-help/java/java-android-fragment-injection/) | 470 |  |  |   
[Android fragment injection in PreferenceActivity](https://codeql.github.com/codeql-query-help/java/java-android-fragment-injection-preference-activity/) | 470 |  |  |   
[Android Intent redirection](https://codeql.github.com/codeql-query-help/java/java-android-intent-redirection/) | 926, 940 |  |  |   
[Android Webview debugging enabled](https://codeql.github.com/codeql-query-help/java/java-android-webview-debugging-enabled/) | 489 |  |  |   
[Arbitrary file access during archive extraction ("Zip Slip")](https://codeql.github.com/codeql-query-help/java/java-zipslip/) | 022 |  |  |   
[Building a command line with string concatenation](https://codeql.github.com/codeql-query-help/java/java-concatenated-command-line/) | 078, 088 |  |  |   
[Cleartext storage of sensitive information in cookie](https://codeql.github.com/codeql-query-help/java/java-cleartext-storage-in-cookie/) | 315 |  |  |   
[Cross-site scripting](https://codeql.github.com/codeql-query-help/java/java-xss/) | 079 |  |  |   
[Depending upon JCenter/Bintray as an artifact repository](https://codeql.github.com/codeql-query-help/java/java-maven-dependency-upon-bintray/) | 1104 |  |  |   
[Deserialization of user-controlled data](https://codeql.github.com/codeql-query-help/java/java-unsafe-deserialization/) | 502 |  |  |   
[Detect JHipster Generator Vulnerability CVE-2019-16303](https://codeql.github.com/codeql-query-help/java/java-jhipster-prng/) | 338 |  |  |   
[Disabled Netty HTTP header validation](https://codeql.github.com/codeql-query-help/java/java-netty-http-request-or-response-splitting/) | 093, 113 |  |  |   
[Disabled Spring CSRF protection](https://codeql.github.com/codeql-query-help/java/java-spring-disabled-csrf-protection/) | 352 |  |  |   
[Exposed Spring Boot actuators](https://codeql.github.com/codeql-query-help/java/java-spring-boot-exposed-actuators/) | 200 |  |  |   
[Expression language injection (JEXL)](https://codeql.github.com/codeql-query-help/java/java-jexl-expression-injection/) | 094 |  |  |   
[Expression language injection (MVEL)](https://codeql.github.com/codeql-query-help/java/java-mvel-expression-injection/) | 094 |  |  |   
[Expression language injection (Spring)](https://codeql.github.com/codeql-query-help/java/java-spel-expression-injection/) | 094 |  |  |   
[Failure to use HTTPS or SFTP URL in Maven artifact upload/download](https://codeql.github.com/codeql-query-help/java/java-maven-non-https-url/) | 300, 319, 494, 829 |  |  |   
[Failure to use secure cookies](https://codeql.github.com/codeql-query-help/java/java-insecure-cookie/) | 614 |  |  |   
[Groovy Language injection](https://codeql.github.com/codeql-query-help/java/java-groovy-injection/) | 094 |  |  |   
[HTTP response splitting](https://codeql.github.com/codeql-query-help/java/java-http-response-splitting/) | 113 |  |  |   
[Implicit narrowing conversion in compound assignment](https://codeql.github.com/codeql-query-help/java/java-implicit-cast-in-compound-assignment/) | 190, 192, 197, 681 |  |  |   
[Implicitly exported Android component](https://codeql.github.com/codeql-query-help/java/java-android-implicitly-exported-component/) | 926 |  |  |   
[Improper verification of intent by broadcast receiver](https://codeql.github.com/codeql-query-help/java/java-improper-intent-verification/) | 925 |  |  |   
[Inefficient regular expression](https://codeql.github.com/codeql-query-help/java/java-redos/) | 1333, 730, 400 |  |  |   
[Information exposure through a stack trace](https://codeql.github.com/codeql-query-help/java/java-stack-trace-exposure/) | 209, 497 |  |  |   
[Information exposure through an error message](https://codeql.github.com/codeql-query-help/java/java-error-message-exposure/) | 209 |  |  |   
[Insecure Bean Validation](https://codeql.github.com/codeql-query-help/java/java-insecure-bean-validation/) | 094 |  |  |   
[Insecure LDAP authentication](https://codeql.github.com/codeql-query-help/java/java-insecure-ldap-auth/) | 522, 319 |  |  |   
[Insecure local authentication](https://codeql.github.com/codeql-query-help/java/java-android-insecure-local-authentication/) | 287 |  |  |   
[Insecure randomness](https://codeql.github.com/codeql-query-help/java/java-insecure-randomness/) | 330, 338 |  |  |   
[Intent URI permission manipulation](https://codeql.github.com/codeql-query-help/java/java-android-intent-uri-permission-manipulation/) | 266, 926 |  |  |   
[JNDI lookup with user-controlled name](https://codeql.github.com/codeql-query-help/java/java-jndi-injection/) | 074 |  |  |   
[LDAP query built from user-controlled sources](https://codeql.github.com/codeql-query-help/java/java-ldap-injection/) | 090 |  |  |   
[Missing JWT signature check](https://codeql.github.com/codeql-query-help/java/java-missing-jwt-signature-check/) | 347 |  |  |   
[OGNL Expression Language statement with user-controlled input](https://codeql.github.com/codeql-query-help/java/java-ognl-injection/) | 917 |  |  |   
[Overly permissive regular expression range](https://codeql.github.com/codeql-query-help/java/java-overly-large-range/) | 020 |  |  |   
[Partial path traversal vulnerability from remote](https://codeql.github.com/codeql-query-help/java/java-partial-path-traversal-from-remote/) | 023 |  |  |   
[Polynomial regular expression used on uncontrolled data](https://codeql.github.com/codeql-query-help/java/java-polynomial-redos/) | 1333, 730, 400 |  |  |   
[Query built from user-controlled sources](https://codeql.github.com/codeql-query-help/java/java-sql-injection/) | 089, 564 |  |  |   
[Reading from a world writable file](https://codeql.github.com/codeql-query-help/java/java-world-writable-file-read/) | 732 |  |  |   
[Regular expression injection](https://codeql.github.com/codeql-query-help/java/java-regex-injection/) | 730, 400 |  |  |   
[Resolving XML external entity in user-controlled data](https://codeql.github.com/codeql-query-help/java/java-xxe/) | 611, 776, 827 |  |  |   
[Server-side request forgery](https://codeql.github.com/codeql-query-help/java/java-ssrf/) | 918 |  |  |   
[Server-side template injection](https://codeql.github.com/codeql-query-help/java/java-server-side-template-injection/) | 1336, 094 |  |  |   
[Uncontrolled command line](https://codeql.github.com/codeql-query-help/java/java-command-line-injection/) | 078, 088 |  |  |   
[Uncontrolled data used in content resolution](https://codeql.github.com/codeql-query-help/java/java-android-unsafe-content-uri-resolution/) | 441, 610 |  |  |   
[Uncontrolled data used in path expression](https://codeql.github.com/codeql-query-help/java/java-path-injection/) | 022, 023, 036, 073 |  |  |   
[Unsafe hostname verification](https://codeql.github.com/codeql-query-help/java/java-unsafe-hostname-verification/) | 297 |  |  |   
[URL forward from a remote source](https://codeql.github.com/codeql-query-help/java/java-unvalidated-url-forward/) | 552 |  |  |   
[URL redirection from remote source](https://codeql.github.com/codeql-query-help/java/java-unvalidated-url-redirection/) | 601 |  |  |   
[Use of a broken or risky cryptographic algorithm](https://codeql.github.com/codeql-query-help/java/java-weak-cryptographic-algorithm/) | 327, 328 |  |  |   
[Use of a cryptographic algorithm with insufficient key size](https://codeql.github.com/codeql-query-help/java/java-insufficient-key-size/) | 326 |  |  |   
[Use of a predictable seed in a secure random number generator](https://codeql.github.com/codeql-query-help/java/java-predictable-seed/) | 335, 337 |  |  |   
[Use of externally-controlled format string](https://codeql.github.com/codeql-query-help/java/java-tainted-format-string/) | 134 |  |  |   
[Use of implicit PendingIntents](https://codeql.github.com/codeql-query-help/java/java-android-implicit-pendingintents/) | 927 |  |  |   
[Use of RSA algorithm without OAEP](https://codeql.github.com/codeql-query-help/java/java-rsa-without-oaep/) | 780 |  |  |   
[User-controlled data in numeric cast](https://codeql.github.com/codeql-query-help/java/java-tainted-numeric-cast/) | 197, 681 |  |  |   
[User-controlled data used in permissions check](https://codeql.github.com/codeql-query-help/java/java-tainted-permissions-check/) | 807, 290 |  |  |   
[Using a static initialization vector for encryption](https://codeql.github.com/codeql-query-help/java/java-static-initialization-vector/) | 329, 1204 |  |  |   
[XPath injection](https://codeql.github.com/codeql-query-help/java/java-xml-xpath-injection/) | 643 |  |  |   
[XSLT transformation with user-controlled stylesheet](https://codeql.github.com/codeql-query-help/java/java-xslt-injection/) | 074 |  |  |   
[Access Java object methods through JavaScript exposure](https://codeql.github.com/codeql-query-help/java/java-android-webview-addjavascriptinterface/) | 079 |  |  |   
[Android APK installation](https://codeql.github.com/codeql-query-help/java/java-android-arbitrary-apk-installation/) | 094 |  |  |   
[Android missing certificate pinning](https://codeql.github.com/codeql-query-help/java/java-android-missing-certificate-pinning/) | 295 |  |  |   
[Android sensitive keyboard cache](https://codeql.github.com/codeql-query-help/java/java-android-sensitive-keyboard-cache/) | 524 |  |  |   
[Android WebSettings file access](https://codeql.github.com/codeql-query-help/java/java-android-websettings-file-access/) | 200 |  |  |   
[Android WebView JavaScript settings](https://codeql.github.com/codeql-query-help/java/java-android-websettings-javascript-enabled/) | 079 |  |  |   
[Android WebView settings allows access to content links](https://codeql.github.com/codeql-query-help/java/java-android-websettings-allow-content-access/) | 200 |  |  |   
[Application backup allowed](https://codeql.github.com/codeql-query-help/java/java-android-backup-enabled/) | 312 |  |  |   
[Building a command with an injected environment variable](https://codeql.github.com/codeql-query-help/java/java-exec-tainted-environment/) | 078, 088, 454 |  |  |   
[Cleartext storage of sensitive information in the Android filesystem](https://codeql.github.com/codeql-query-help/java/java-android-cleartext-storage-filesystem/) | 312 |  |  |   
[Cleartext storage of sensitive information using 'Properties' class](https://codeql.github.com/codeql-query-help/java/java-cleartext-storage-in-properties/) | 313 |  |  |   
[Cleartext storage of sensitive information using `SharedPreferences` on Android](https://codeql.github.com/codeql-query-help/java/java-android-cleartext-storage-shared-prefs/) | 312 |  |  |   
[Cleartext storage of sensitive information using a local database on Android](https://codeql.github.com/codeql-query-help/java/java-android-cleartext-storage-database/) | 312 |  |  |   
[Comparison of narrow type with wide type in loop condition](https://codeql.github.com/codeql-query-help/java/java-comparison-with-wider-type/) | 190, 197 |  |  |   
[Executing a command with a relative path](https://codeql.github.com/codeql-query-help/java/java-relative-path-command/) | 078, 088 |  |  |   
[Exposure of sensitive information to notifications](https://codeql.github.com/codeql-query-help/java/java-android-sensitive-notification/) | 200 |  |  |   
[Exposure of sensitive information to UI text views](https://codeql.github.com/codeql-query-help/java/java-android-sensitive-text/) | 200 |  |  |   
[HTTP request type unprotected from CSRF](https://codeql.github.com/codeql-query-help/java/java-csrf-unprotected-request-type/) | 352 |  |  |   
[Improper validation of user-provided array index](https://codeql.github.com/codeql-query-help/java/java-improper-validation-of-array-index/) | 129 |  |  |   
[Improper validation of user-provided size used for array construction](https://codeql.github.com/codeql-query-help/java/java-improper-validation-of-array-construction/) | 129 |  |  |   
[Insecure basic authentication](https://codeql.github.com/codeql-query-help/java/java-insecure-basic-auth/) | 522, 319 |  |  |   
[Insecure JavaMail SSL Configuration](https://codeql.github.com/codeql-query-help/java/java-insecure-smtp-ssl/) | 297 |  |  |   
[Insecurely generated keys for local authentication](https://codeql.github.com/codeql-query-help/java/java-android-insecure-local-key-gen/) | 287 |  |  |   
[Insertion of sensitive information into log files](https://codeql.github.com/codeql-query-help/java/java-sensitive-log/) | 532 |  |  |   
[Leaking sensitive information through a ResultReceiver](https://codeql.github.com/codeql-query-help/java/java-android-sensitive-result-receiver/) | 927 |  |  |   
[Leaking sensitive information through an implicit Intent](https://codeql.github.com/codeql-query-help/java/java-android-sensitive-communication/) | 927 |  |  |   
[Local information disclosure in a temporary directory](https://codeql.github.com/codeql-query-help/java/java-local-temp-file-or-directory-information-disclosure/) | 200, 732 |  |  |   
[Log Injection](https://codeql.github.com/codeql-query-help/java/java-log-injection/) | 117 |  |  |   
[Loop with unreachable exit condition](https://codeql.github.com/codeql-query-help/java/java-unreachable-exit-in-loop/) | 835 |  |  |   
[Missing read or write permission in a content provider](https://codeql.github.com/codeql-query-help/java/java-android-incomplete-provider-permissions/) | 926 |  |  |   
[Partial path traversal vulnerability](https://codeql.github.com/codeql-query-help/java/java-partial-path-traversal/) | 023 |  |  |   
[Query built by concatenation with a possibly-untrusted string](https://codeql.github.com/codeql-query-help/java/java-concatenated-sql-query/) | 089, 564 |  |  |   
[Race condition in socket authentication](https://codeql.github.com/codeql-query-help/java/java-socket-auth-race-condition/) | 421 |  |  |   
[Time-of-check time-of-use race condition](https://codeql.github.com/codeql-query-help/java/java-toctou-race-condition/) | 367 |  |  |   
[Trust boundary violation](https://codeql.github.com/codeql-query-help/java/java-trust-boundary-violation/) | 501 |  |  |   
[Uncontrolled data in arithmetic expression](https://codeql.github.com/codeql-query-help/java/java-uncontrolled-arithmetic/) | 190, 191 |  |  |   
[Unreleased lock](https://codeql.github.com/codeql-query-help/java/java-unreleased-lock/) | 764, 833 |  |  |   
[Unsafe certificate trust](https://codeql.github.com/codeql-query-help/java/java-unsafe-cert-trust/) | 273 |  |  |   
[Unsafe resource fetching in Android WebView](https://codeql.github.com/codeql-query-help/java/java-android-unsafe-android-webview-fetch/) | 749, 079 |  |  |   
[Use of a potentially broken or risky cryptographic algorithm](https://codeql.github.com/codeql-query-help/java/java-potentially-weak-cryptographic-algorithm/) | 327, 328 |  |  |   
[Use of a potentially dangerous function](https://codeql.github.com/codeql-query-help/java/java-potentially-dangerous-function/) | 676 |  |  |   
[User-controlled bypass of sensitive method](https://codeql.github.com/codeql-query-help/java/java-user-controlled-bypass/) | 807, 290 |  |  |   
[User-controlled data in arithmetic expression](https://codeql.github.com/codeql-query-help/java/java-tainted-arithmetic/) | 190, 191 |  |  | 
