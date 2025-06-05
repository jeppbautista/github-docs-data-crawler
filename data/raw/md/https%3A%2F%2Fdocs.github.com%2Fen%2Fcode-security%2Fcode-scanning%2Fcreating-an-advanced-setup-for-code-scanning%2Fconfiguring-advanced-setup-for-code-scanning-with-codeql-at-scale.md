  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Create advanced setup](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning "Create advanced setup")/
  * [CodeQL advanced setup at scale](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning-with-codeql-at-scale "CodeQL advanced setup at scale")


# Configuring advanced setup for code scanning with CodeQL at scale
You can use a script to configure advanced setup for code scanning for a specific group of repositories in your organization.
## Who can use this feature?
Organization owners, security managers, and organization members with the **admin** role
Code scanning is available for the following repository types:
  * Public repositories on GitHub.com
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [About enabling advanced setup for code scanning with CodeQL at scale](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning-with-codeql-at-scale#about-enabling-advanced-setup-for-code-scanning-with-codeql-at-scale)
  * [Using a script to enable advanced setup](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning-with-codeql-at-scale#using-a-script-to-enable-advanced-setup)


## [About enabling advanced setup for code scanning with CodeQL at scale](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning-with-codeql-at-scale#about-enabling-advanced-setup-for-code-scanning-with-codeql-at-scale)
If you need to configure a highly customizable code scanning setup for many repositories in your organization, or if repositories in your organization are ineligible for default setup, you can enable code scanning at scale with advanced setup.
To enable advanced setup across multiple repositories, you can write a bulk configuration script. To successfully execute the script, GitHub Actions must be enabled for the organization.
Alternatively, if you do not need granular control over the code scanning configuration for many repositories in your organization, you can quickly and easily configure code scanning at scale with default setup. For more information, see [Configuring default setup for code scanning at scale](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning-at-scale).
## [Using a script to enable advanced setup](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning-with-codeql-at-scale#using-a-script-to-enable-advanced-setup)
For repositories that are not eligible for default setup, you can use a bulk configuration script to enable advanced setup across multiple repositories.
  1. Identify a group of repositories that can be analyzed using the same code scanning configuration. For example, all repositories that build Java artifacts using the production environment.
  2. Create and test a GitHub Actions workflow to call the CodeQL action with the appropriate configuration. For more information, see [Configuring advanced setup for code scanning](https://docs.github.com/en/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/configuring-advanced-setup-for-code-scanning#configuring-advanced-setup-for-code-scanning-with-codeql).
  3. Use one of the example scripts or create a custom script to add the workflow to each repository in the group. 
     * GitHub CLI extension: [`advanced-security/gh-add-files`](https://github.com/advanced-security/gh-add-files)
     * Python example: [`Malwarebytes/ghas-cli`](https://github.com/Malwarebytes/ghas-cli) repository
     * NodeJS example: [`nickliffen/ghas-enablement`](https://github.com/NickLiffen/ghas-enablement) repository
     * PowerShell example: [`jhutchings1/Create-ActionsPRs`](https://github.com/jhutchings1/Create-ActionsPRs) repository


### [Extending CodeQL coverage with model packs](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning-with-codeql-at-scale#extending-codeql-coverage-with-model-packs)
CodeQL model packs are currently in public preview and subject to change. Model packs are supported for C/C++, C#, Java/Kotlin, Python, and Ruby analysis.
The CodeQL model editor in the CodeQL extension for Visual Studio Code supports modeling dependencies for C#, Java/Kotlin, Python, and Ruby.
If your codebase depends on a library or framework that is not recognized by the standard queries in CodeQL, you can extend the CodeQL coverage in your bulk configuration script by specifying published CodeQL model packs. For more information, see [Customizing your advanced setup for code scanning](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/customizing-your-advanced-setup-for-code-scanning#extending-codeql-coverage-with-codeql-model-packs).
Alternatively, if you do not need granular control over the code scanning configuration for many repositories in your organization, you can quickly and easily configure model packs with code scanning at scale with default setup. For more information, see [Editing your configuration of default setup](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/editing-your-configuration-of-default-setup#extending-codeql-coverage-with-codeql-model-packs-in-default-setup).
