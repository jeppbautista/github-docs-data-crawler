  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Introduction](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning "Introduction")/
  * [About CodeQL code scanning](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql "About CodeQL code scanning")


# About code scanning with CodeQL
You can use CodeQL to identify vulnerabilities and errors in your code. The results are shown as code scanning alerts in GitHub.
## Who can use this feature?
Code scanning is available for the following repository types:
  * Public repositories on GitHub.com
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [About CodeQL](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql#about-codeql)
  * [Modeling custom or niche frameworks](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql#modeling-custom-or-niche-frameworks)
  * [CodeQL queries](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql#codeql-queries)


CodeQL is the code analysis engine developed by GitHub to automate security checks. You can analyze your code using CodeQL and display the results as code scanning alerts.
There are three main ways to use CodeQL analysis for code scanning:
  * Use default setup to quickly configure CodeQL analysis for code scanning on your repository. Default setup automatically chooses the languages to analyze, query suite to run, and events that trigger scans. If you prefer, you can manually select the query suite to run and languages to analyze. After you enable CodeQL, GitHub Actions will execute workflow runs to scan your code. For more information, see [Configuring default setup for code scanning](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning).
  * Use advanced setup to add the CodeQL workflow to your repository. This generates a customizable workflow file which uses the [github/codeql-action](https://github.com/github/codeql-action/) to run the CodeQL CLI. For more information, see [Configuring advanced setup for code scanning](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning#configuring-advanced-setup-for-code-scanning-with-codeql).
  * Run the CodeQL CLI directly in an external CI system and upload the results to GitHub. For more information, see [Using code scanning with your existing CI system](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/using-code-scanning-with-your-existing-ci-system).


For information about code scanning alerts, see [About code scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts).
## [About CodeQL](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql#about-codeql)
CodeQL is a programming language and associated tools that treat code like data. It was created explicitly to make it easier to analyze code and find potential vulnerabilities in your code with greater confidence than traditional static analyzers.
  1. You generate a CodeQL database to represent your codebase.
  2. Then you run CodeQL queries on that database to identify problems in the codebase.
  3. The query results are shown as code scanning alerts in GitHub when you use CodeQL with code scanning.


CodeQL supports both compiled and interpreted languages, and can find vulnerabilities and errors in code that's written in the supported languages.
CodeQL supports the following languages:
  * C/C++
  * C#
  * Go
  * Java/Kotlin
  * JavaScript/TypeScript
  * Python
  * Ruby
  * Swift
  * GitHub Actions workflows


  * Use `java-kotlin` to analyze code written in Java, Kotlin or both.
  * Use `javascript-typescript` to analyze code written in JavaScript, TypeScript or both.


For more information, see the documentation on the CodeQL website: [Supported languages and frameworks](https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/).
CodeQL does **not** support languages that are not listed above. This includes, but is not limited to, **Rust** , **PHP** , **Scala** , and others. Attempting to use CodeQL with unsupported languages may result in no alerts being generated and incomplete analysis.
## [Modeling custom or niche frameworks](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql#modeling-custom-or-niche-frameworks)
GitHub experts, security researchers, and community contributors write libraries to model the flow of data in popular frameworks and libraries. If you use custom dependencies that aren't modeled, then you can use the CodeQL extension for Visual Studio Code to create models for these dependencies and use them to extend your analysis. For more information, see [Using the CodeQL model editor](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/using-the-codeql-model-editor).
## [CodeQL queries](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql#codeql-queries)
GitHub experts, security researchers, and community contributors write and maintain the default CodeQL queries used for code scanning. The queries are regularly updated to improve analysis and reduce any false positive results.
### [Writing your own queries](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql#writing-your-own-queries)
The queries are open source, so you can view and contribute to the queries in the [github/codeql](https://github.com/github/codeql) repository. For more information, see [About CodeQL queries](https://codeql.github.com/docs/writing-codeql-queries/about-codeql-queries/) in the CodeQL documentation.
### [Running additional queries](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql#running-additional-queries)
If you are scanning your code with advanced setup or an external CI system, you can run additional queries as part of your analysis.
These queries must belong to a published CodeQL query pack or a CodeQL pack in a repository.
  * When a CodeQL query pack is published to the GitHub Container registry, all the transitive dependencies required by the queries and a compilation cache are included in the package. This improves performance and ensures that running the queries in the pack gives identical results every time until you upgrade to a new version of the pack or the CLI.
  * CodeQL query packs can be downloaded from multiple GitHub container registries. For more information, see [Customizing your advanced setup for code scanning](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/customizing-your-advanced-setup-for-code-scanning#downloading-codeql-packs-from-github-enterprise-server).


For more information, see [Customizing analysis with CodeQL packs](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/customizing-analysis-with-codeql-packs).
