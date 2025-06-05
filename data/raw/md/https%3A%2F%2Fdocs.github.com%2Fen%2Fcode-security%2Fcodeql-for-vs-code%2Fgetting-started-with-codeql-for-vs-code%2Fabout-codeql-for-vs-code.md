  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL for VS Code](https://docs.github.com/en/code-security/codeql-for-vs-code "CodeQL for VS Code")/
  * [Getting started](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code "Getting started")/
  * [About the extension](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/about-codeql-for-vs-code "About the extension")


# About CodeQL for VS Code
You can write, run, and test CodeQL queries inside Visual Studio Code with the CodeQL extension.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [About CodeQL for Visual Studio Code](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/about-codeql-for-vs-code#about-codeql-for-visual-studio-code)
  * [Data and telemetry](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/about-codeql-for-vs-code#data-and-telemetry)
  * [About the GitHub CodeQL license](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/about-codeql-for-vs-code#about-the-github-codeql-license)
  * [Next steps](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/about-codeql-for-vs-code#next-steps)


## [About CodeQL for Visual Studio Code](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/about-codeql-for-vs-code#about-codeql-for-visual-studio-code)
You can run CodeQL queries on databases generated from source code, in order to find errors and security vulnerabilities in a codebase. For more information about CodeQL code scanning, see [About code scanning with CodeQL](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql).
With the CodeQL for Visual Studio Code extension, you can:
  * Write custom CodeQL queries and supporting libraries.
  * Directly view and use the CodeQL security queries from the large, open-source [`github/codeql`](https://github.com/github/codeql) repository.
  * Run queries over one or more CodeQL databases.
  * Track the flow of data through a program, highlighting areas that are potential security vulnerabilities.
  * View, create, and edit all types of CodeQL packs of queries or libraries that you can use or publish to share with others.
  * Run unit tests for CodeQL queries.
  * Use a dedicated editor for viewing, creating, and editing CodeQL model packs, which are used to extend standard CodeQL analysis.


The CodeQL for Visual Studio Code extension also adds a CodeQL sidebar view to VS Code. This contains a list of local CodeQL databases, an overview of the queries that you have run in the current session, and a variant analysis view for large-scale analysis.
### [IntelliSense](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/about-codeql-for-vs-code#intellisense)
The extension provides standard IntelliSense features for query files (extension `.ql`) and library files (extension `.qll`) that you open in the VS Code editor. These include:
  * Syntax highlighting
  * Right-click options (such as **Go To Definition**)
  * Autocomplete suggestions
  * Hover information


For more information about Intellisense in VS Code, see [IntelliSense](https://code.visualstudio.com/docs/editor/intellisense) in the Visual Studio Code documentation.
You can also use the VS Code **Format Document** command to format your code according to the [CodeQL style guide](https://github.com/github/codeql/blob/main/docs/ql-style-guide.md).
### [The VS Code Command Palette](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/about-codeql-for-vs-code#the-vs-code-command-palette)
You can run commands for the CodeQL for Visual Studio Code extension from the VS Code Command Palette. For more information about the VS Code Command Palette, see [User Interface](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) in the VS Code documentation.
## [Data and telemetry](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/about-codeql-for-vs-code#data-and-telemetry)
If you specifically opt in to permit GitHub to do so, GitHub will collect usage data and metrics for the purposes of helping the core developers to improve the CodeQL for Visual Studio Code extension. For more information, see [Telemetry in CodeQL for Visual Studio Code](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/telemetry-in-codeql-for-visual-studio-code).
## [About the GitHub CodeQL license](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/about-codeql-for-vs-code#about-the-github-codeql-license)
**License notice:** If you don’t have a license for GitHub Code Security then, by installing this product, you are agreeing to the [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md).
For information about how you can try GitHub Enterprise with GitHub Advanced Security for free, see [Setting up a trial of GitHub Enterprise Cloud](https://docs.github.com/en/enterprise-cloud@latest/admin/overview/setting-up-a-trial-of-github-enterprise-cloud) and [Setting up a trial of GitHub Advanced Security](https://docs.github.com/en/enterprise-cloud@latest/billing/managing-billing-for-your-products/managing-billing-for-github-advanced-security/setting-up-a-trial-of-github-advanced-security#setting-up-your-trial-of-github-advanced-security) in the GitHub Enterprise Cloud documentation.
## [Next steps](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/about-codeql-for-vs-code#next-steps)
To learn about how to install the CodeQL for Visual Studio Code extension, see [Installing CodeQL for Visual Studio Code](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/installing-codeql-for-vs-code).
