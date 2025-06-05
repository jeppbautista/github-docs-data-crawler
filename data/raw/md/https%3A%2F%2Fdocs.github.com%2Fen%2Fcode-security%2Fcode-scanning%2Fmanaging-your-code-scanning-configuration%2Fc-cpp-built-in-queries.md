  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Manage code scanning](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration "Manage code scanning")/
  * [C and C++ CodeQL queries](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/c-cpp-built-in-queries "C and C++ CodeQL queries")


# C and C++ queries for CodeQL analysis
Explore the queries that CodeQL uses to analyze code written in C or C++ when you select the `default` or the `security-extended` query suite.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


CodeQL includes many queries for analyzing C and C++ code. All queries in the `default` query suite are run by default. If you choose to use the `security-extended` query suite, additional queries are run. For more information, see [CodeQL query suites](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/built-in-codeql-query-suites).
## [Built-in queries for C and C++ analysis](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/c-cpp-built-in-queries#built-in-queries-for-c-and-c-analysis)
This table lists the queries available with the latest release of the CodeQL action and CodeQL CLI. For more information, see [CodeQL change logs](https://codeql.github.com/docs/codeql-overview/codeql-changelog/) in the CodeQL documentation site.
Query name | Related CWEs | Default | Extended | Copilot Autofix  
---|---|---|---|---  
[Bad check for overflow of integer addition](https://codeql.github.com/codeql-query-help/cpp/cpp-bad-addition-overflow-check/) | 190, 192 |  |  |   
[Badly bounded write](https://codeql.github.com/codeql-query-help/cpp/cpp-badly-bounded-write/) | 120, 787, 805 |  |  |   
[Call to `memset` may be deleted](https://codeql.github.com/codeql-query-help/cpp/cpp-memset-may-be-deleted/) | 014 |  |  |   
[Call to alloca in a loop](https://codeql.github.com/codeql-query-help/cpp/cpp-alloca-in-loop/) | 770 |  |  |   
[Call to function with fewer arguments than declared parameters](https://codeql.github.com/codeql-query-help/cpp/cpp-too-few-arguments/) | 234, 685 |  |  |   
[Cast between HRESULT and a Boolean type](https://codeql.github.com/codeql-query-help/cpp/cpp-hresult-boolean-conversion/) | 253 |  |  |   
[Cast from char* to wchar_t*](https://codeql.github.com/codeql-query-help/cpp/cpp-incorrect-string-type-conversion/) | 704 |  |  |   
[CGI script vulnerable to cross-site scripting](https://codeql.github.com/codeql-query-help/cpp/cpp-cgi-xss/) | 079 |  |  |   
[Cleartext storage of sensitive information in file](https://codeql.github.com/codeql-query-help/cpp/cpp-cleartext-storage-file/) | 260, 313 |  |  |   
[Cleartext transmission of sensitive information](https://codeql.github.com/codeql-query-help/cpp/cpp-cleartext-transmission/) | 319, 359 |  |  |   
[Comparison of narrow type with wide type in loop condition](https://codeql.github.com/codeql-query-help/cpp/cpp-comparison-with-wider-type/) | 190, 197, 835 |  |  |   
[Dangerous use of 'cin'](https://codeql.github.com/codeql-query-help/cpp/cpp-dangerous-cin/) | 676 |  |  |   
[Exposure of system data to an unauthorized control sphere](https://codeql.github.com/codeql-query-help/cpp/cpp-system-data-exposure/) | 497 |  |  |   
[Failure to use HTTPS URLs](https://codeql.github.com/codeql-query-help/cpp/cpp-non-https-url/) | 319, 345 |  |  |   
[File opened with O_CREAT flag but without mode argument](https://codeql.github.com/codeql-query-help/cpp/cpp-open-call-with-mode-argument/) | 732 |  |  |   
[Incorrect return-value check for a 'scanf'-like function](https://codeql.github.com/codeql-query-help/cpp/cpp-incorrectly-checked-scanf/) | 253 |  |  |   
[Iterator to expired container](https://codeql.github.com/codeql-query-help/cpp/cpp-iterator-to-expired-container/) | 416, 664 |  |  |   
[Likely overrunning write](https://codeql.github.com/codeql-query-help/cpp/cpp-very-likely-overrunning-write/) | 120, 787, 805 |  |  |   
[Mismatching new/free or malloc/delete](https://codeql.github.com/codeql-query-help/cpp/cpp-new-free-mismatch/) | 401 |  |  |   
[Multiplication result converted to larger type](https://codeql.github.com/codeql-query-help/cpp/cpp-integer-multiplication-cast-to-long/) | 190, 192, 197, 681 |  |  |   
[No space for zero terminator](https://codeql.github.com/codeql-query-help/cpp/cpp-no-space-for-terminator/) | 131, 120, 122 |  |  |   
[Pointer overflow check](https://codeql.github.com/codeql-query-help/cpp/cpp-pointer-overflow-check/) | 758 |  |  |   
[Potential double free](https://codeql.github.com/codeql-query-help/cpp/cpp-double-free/) | 415 |  |  |   
[Potential use after free](https://codeql.github.com/codeql-query-help/cpp/cpp-use-after-free/) | 416 |  |  |   
[Potentially overflowing call to snprintf](https://codeql.github.com/codeql-query-help/cpp/cpp-overflowing-snprintf/) | 190, 253 |  |  |   
[Potentially unsafe call to strncat](https://codeql.github.com/codeql-query-help/cpp/cpp-unsafe-strncat/) | 788, 676, 119, 251 |  |  |   
[Redundant null check due to previous dereference](https://codeql.github.com/codeql-query-help/cpp/cpp-redundant-null-check-simple/) | 476 |  |  |   
[Returning stack-allocated memory](https://codeql.github.com/codeql-query-help/cpp/cpp-return-stack-allocated-memory/) | 825 |  |  |   
[Setting a DACL to NULL in a SECURITY_DESCRIPTOR](https://codeql.github.com/codeql-query-help/cpp/cpp-unsafe-dacl-security-descriptor/) | 732 |  |  |   
[Signed overflow check](https://codeql.github.com/codeql-query-help/cpp/cpp-signed-overflow-check/) | 128, 190 |  |  |   
[Static array access may cause overflow](https://codeql.github.com/codeql-query-help/cpp/cpp-static-buffer-overflow/) | 119, 131 |  |  |   
[Suspicious add with sizeof](https://codeql.github.com/codeql-query-help/cpp/cpp-suspicious-add-sizeof/) | 468 |  |  |   
[Time-of-check time-of-use filesystem race condition](https://codeql.github.com/codeql-query-help/cpp/cpp-toctou-race-condition/) | 367 |  |  |   
[Too few arguments to formatting function](https://codeql.github.com/codeql-query-help/cpp/cpp-wrong-number-format-arguments/) | 234, 685 |  |  |   
[Uncontrolled data in arithmetic expression](https://codeql.github.com/codeql-query-help/cpp/cpp-uncontrolled-arithmetic/) | 190, 191 |  |  |   
[Uncontrolled data in SQL query](https://codeql.github.com/codeql-query-help/cpp/cpp-sql-injection/) | 089 |  |  |   
[Uncontrolled data used in OS command](https://codeql.github.com/codeql-query-help/cpp/cpp-command-line-injection/) | 078, 088 |  |  |   
[Uncontrolled format string](https://codeql.github.com/codeql-query-help/cpp/cpp-tainted-format-string/) | 134 |  |  |   
[Unsafe use of this in constructor](https://codeql.github.com/codeql-query-help/cpp/cpp-unsafe-use-of-this/) | 670 |  |  |   
[Unsigned difference expression compared to zero](https://codeql.github.com/codeql-query-help/cpp/cpp-unsigned-difference-expression-compared-zero/) | 191 |  |  |   
[Upcast array used in pointer arithmetic](https://codeql.github.com/codeql-query-help/cpp/cpp-upcast-array-pointer-arithmetic/) | 119, 843 |  |  |   
[Use of a broken or risky cryptographic algorithm](https://codeql.github.com/codeql-query-help/cpp/cpp-weak-cryptographic-algorithm/) | 327 |  |  |   
[Use of a cryptographic algorithm with insufficient key size](https://codeql.github.com/codeql-query-help/cpp/cpp-insufficient-key-size/) | 326 |  |  |   
[Use of a version of OpenSSL with Heartbleed](https://codeql.github.com/codeql-query-help/cpp/cpp-openssl-heartbleed/) | 327, 788 |  |  |   
[Use of dangerous function](https://codeql.github.com/codeql-query-help/cpp/cpp-dangerous-function-overflow/) | 242, 676 |  |  |   
[Use of expired stack-address](https://codeql.github.com/codeql-query-help/cpp/cpp-using-expired-stack-address/) | 825 |  |  |   
[Use of string after lifetime ends](https://codeql.github.com/codeql-query-help/cpp/cpp-use-of-string-after-lifetime-ends/) | 416, 664 |  |  |   
[Use of unique pointer after lifetime ends](https://codeql.github.com/codeql-query-help/cpp/cpp-use-of-unique-pointer-after-lifetime-ends/) | 416, 664 |  |  |   
[Wrong type of arguments to formatting function](https://codeql.github.com/codeql-query-help/cpp/cpp-wrong-type-format-argument/) | 686 |  |  |   
[XML external entity expansion](https://codeql.github.com/codeql-query-help/cpp/cpp-external-entity-expansion/) | 611 |  |  |   
[Array offset used before range check](https://codeql.github.com/codeql-query-help/cpp/cpp-offset-use-before-range-check/) | 120, 125 |  |  |   
[Authentication bypass by spoofing](https://codeql.github.com/codeql-query-help/cpp/cpp-user-controlled-bypass/) | 290 |  |  |   
[boost::asio TLS settings misconfiguration](https://codeql.github.com/codeql-query-help/cpp/cpp-boost-tls-settings-misconfiguration/) | 326 |  |  |   
[boost::asio use of deprecated hardcoded protocol](https://codeql.github.com/codeql-query-help/cpp/cpp-boost-use-of-deprecated-hardcoded-security-protocol/) | 327 |  |  |   
[Call to memory access function may overflow buffer](https://codeql.github.com/codeql-query-help/cpp/cpp-overflow-buffer/) | 119, 121, 122, 126 |  |  |   
[Certificate not checked](https://codeql.github.com/codeql-query-help/cpp/cpp-certificate-not-checked/) | 295 |  |  |   
[Certificate result conflation](https://codeql.github.com/codeql-query-help/cpp/cpp-certificate-result-conflation/) | 295 |  |  |   
[Cleartext storage of sensitive information in an SQLite database](https://codeql.github.com/codeql-query-help/cpp/cpp-cleartext-storage-database/) | 313 |  |  |   
[Cleartext storage of sensitive information in buffer](https://codeql.github.com/codeql-query-help/cpp/cpp-cleartext-storage-buffer/) | 312 |  |  |   
[Comma before misleading indentation](https://codeql.github.com/codeql-query-help/cpp/cpp-comma-before-misleading-indentation/) | 1078, 670 |  |  |   
[File created without restricting permissions](https://codeql.github.com/codeql-query-help/cpp/cpp-world-writable-file-creation/) | 732 |  |  |   
[Incorrect 'not' operator usage](https://codeql.github.com/codeql-query-help/cpp/cpp-incorrect-not-operator-usage/) | 480 |  |  |   
[Incorrect allocation-error handling](https://codeql.github.com/codeql-query-help/cpp/cpp-incorrect-allocation-error-handling/) | 570, 252, 755 |  |  |   
[Invalid pointer dereference](https://codeql.github.com/codeql-query-help/cpp/cpp-invalid-pointer-deref/) | 119, 125, 193, 787 |  |  |   
[Missing return-value check for a 'scanf'-like function](https://codeql.github.com/codeql-query-help/cpp/cpp-missing-check-scanf/) | 252, 253 |  |  |   
[Non-constant format string](https://codeql.github.com/codeql-query-help/cpp/cpp-non-constant-format/) | 134 |  |  |   
[Not enough memory allocated for array of pointer type](https://codeql.github.com/codeql-query-help/cpp/cpp-suspicious-allocation-size/) | 131, 122 |  |  |   
[Not enough memory allocated for pointer type](https://codeql.github.com/codeql-query-help/cpp/cpp-allocation-too-small/) | 131, 122 |  |  |   
[NULL application name with an unquoted path in call to CreateProcess](https://codeql.github.com/codeql-query-help/cpp/cpp-unsafe-create-process-call/) | 428 |  |  |   
[Overrunning write](https://codeql.github.com/codeql-query-help/cpp/cpp-overrun-write/) | 119, 131 |  |  |   
[Possibly wrong buffer size in string copy](https://codeql.github.com/codeql-query-help/cpp/cpp-bad-strncpy-size/) | 676, 119, 251 |  |  |   
[Potential exposure of sensitive system data to an unauthorized control sphere](https://codeql.github.com/codeql-query-help/cpp/cpp-potential-system-data-exposure/) | 497 |  |  |   
[Potentially overrunning write](https://codeql.github.com/codeql-query-help/cpp/cpp-overrunning-write/) | 120, 787, 805 |  |  |   
[Potentially overrunning write with float to string conversion](https://codeql.github.com/codeql-query-help/cpp/cpp-overrunning-write-with-float/) | 120, 787, 805 |  |  |   
[Potentially uninitialized local variable](https://codeql.github.com/codeql-query-help/cpp/cpp-uninitialized-local/) | 665, 457 |  |  |   
[Potentially unsafe use of strcat](https://codeql.github.com/codeql-query-help/cpp/cpp-unsafe-strcat/) | 676, 120, 251 |  |  |   
[Suspicious 'sizeof' use](https://codeql.github.com/codeql-query-help/cpp/cpp-suspicious-sizeof/) | 467 |  |  |   
[Suspicious pointer scaling](https://codeql.github.com/codeql-query-help/cpp/cpp-suspicious-pointer-scaling/) | 468 |  |  |   
[Suspicious pointer scaling to void](https://codeql.github.com/codeql-query-help/cpp/cpp-suspicious-pointer-scaling-void/) | 468 |  |  |   
[Type confusion](https://codeql.github.com/codeql-query-help/cpp/cpp-type-confusion/) | 843 |  |  |   
[Unbounded write](https://codeql.github.com/codeql-query-help/cpp/cpp-unbounded-write/) | 120, 787, 805 |  |  |   
[Uncontrolled allocation size](https://codeql.github.com/codeql-query-help/cpp/cpp-uncontrolled-allocation-size/) | 190, 789 |  |  |   
[Uncontrolled data used in path expression](https://codeql.github.com/codeql-query-help/cpp/cpp-path-injection/) | 022, 023, 036, 073 |  |  |   
[Uncontrolled process operation](https://codeql.github.com/codeql-query-help/cpp/cpp-uncontrolled-process-operation/) | 114 |  |  |   
[Unterminated variadic call](https://codeql.github.com/codeql-query-help/cpp/cpp-unterminated-variadic-call/) | 121 |  |  |   
[Untrusted input for a condition](https://codeql.github.com/codeql-query-help/cpp/cpp-tainted-permissions-check/) | 807 |  |  |   
[Use of potentially dangerous function](https://codeql.github.com/codeql-query-help/cpp/cpp-potentially-dangerous-function/) | 676 |  |  | 
