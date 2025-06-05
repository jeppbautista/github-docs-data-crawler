  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Manage code scanning](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration "Manage code scanning")/
  * [GitHub Actions queries](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/github-actions-built-in-queries "GitHub Actions queries")


# GitHub Actions queries for CodeQL analysis
Explore the queries that CodeQL uses to analyze workflows used by GitHub Actions when you select the `default` or the `security-extended` query suite.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


CodeQL includes many queries for analyzing workflows used by GitHub Actions. All queries in the `default` query suite are run by default. If you choose to use the `security-extended` query suite, additional queries are run. For more information, see [CodeQL query suites](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/built-in-codeql-query-suites).
## [Built-in queries for workflow analysis](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/github-actions-built-in-queries#built-in-queries-for-workflow-analysis)
This table lists the queries available with the latest release of the CodeQL action and CodeQL CLI. For more information, see [CodeQL change logs](https://codeql.github.com/docs/codeql-overview/codeql-changelog/) in the CodeQL documentation site.
Query name | Related CWEs | Default | Extended | Copilot Autofix  
---|---|---|---|---  
[Artifact poisoning](https://codeql.github.com/codeql-query-help/actions/actions-artifact-poisoning-critical/) | 829 |  |  |   
[Cache Poisoning via caching of untrusted files](https://codeql.github.com/codeql-query-help/actions/actions-cache-poisoning-direct-cache/) | 349 |  |  |   
[Cache Poisoning via execution of untrusted code](https://codeql.github.com/codeql-query-help/actions/actions-cache-poisoning-poisonable-step/) | 349 |  |  |   
[Cache Poisoning via low-privileged code injection](https://codeql.github.com/codeql-query-help/actions/actions-cache-poisoning-code-injection/) | 349, 094 |  |  |   
[Checkout of untrusted code in a privileged context](https://codeql.github.com/codeql-query-help/actions/actions-untrusted-checkout-critical/) | 829 |  |  |   
[Checkout of untrusted code in trusted context](https://codeql.github.com/codeql-query-help/actions/actions-untrusted-checkout-high/) | 829 |  |  |   
[Code injection](https://codeql.github.com/codeql-query-help/actions/actions-code-injection-critical/) | 094, 095, 116 |  |  |   
[Environment variable built from user-controlled sources](https://codeql.github.com/codeql-query-help/actions/actions-envvar-injection-critical/) | 077, 020 |  |  |   
[Excessive Secrets Exposure](https://codeql.github.com/codeql-query-help/actions/actions-excessive-secrets-exposure/) | 312 |  |  |   
[Improper Access Control](https://codeql.github.com/codeql-query-help/actions/actions-improper-access-control/) | 285 |  |  |   
[PATH environment variable built from user-controlled sources](https://codeql.github.com/codeql-query-help/actions/actions-envpath-injection-critical/) | 077, 020 |  |  |   
[Storage of sensitive information in GitHub Actions artifact](https://codeql.github.com/codeql-query-help/actions/actions-secrets-in-artifacts/) | 312 |  |  |   
[Unmasked Secret Exposure](https://codeql.github.com/codeql-query-help/actions/actions-unmasked-secret-exposure/) | 312 |  |  |   
[Untrusted Checkout TOCTOU](https://codeql.github.com/codeql-query-help/actions/actions-untrusted-checkout-toctou-high/) | 367 |  |  |   
[Untrusted Checkout TOCTOU](https://codeql.github.com/codeql-query-help/actions/actions-untrusted-checkout-toctou-critical/) | 367 |  |  |   
[Use of a known vulnerable action](https://codeql.github.com/codeql-query-help/actions/actions-vulnerable-action/) | 1395 |  |  |   
[Workflow does not contain permissions](https://codeql.github.com/codeql-query-help/actions/actions-missing-workflow-permissions/) | 275 |  |  |   
[Artifact poisoning](https://codeql.github.com/codeql-query-help/actions/actions-artifact-poisoning-medium/) | 829 |  |  |   
[Checkout of untrusted code in trusted context](https://codeql.github.com/codeql-query-help/actions/actions-untrusted-checkout-medium/) | 829 |  |  |   
[Code injection](https://codeql.github.com/codeql-query-help/actions/actions-code-injection-medium/) | 094, 095, 116 |  |  |   
[Environment variable built from user-controlled sources](https://codeql.github.com/codeql-query-help/actions/actions-envvar-injection-medium/) | 077, 020 |  |  |   
[PATH environment variable built from user-controlled sources](https://codeql.github.com/codeql-query-help/actions/actions-envpath-injection-medium/) | 077, 020 |  |  |   
[Unpinned tag for a non-immutable Action in workflow](https://codeql.github.com/codeql-query-help/actions/actions-unpinned-tag/) | 829 |  |  | 
