  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Manage code scanning](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration "Manage code scanning")/
  * [Edit default setup](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/editing-your-configuration-of-default-setup "Edit default setup")


# Editing your configuration of default setup
You can edit your existing configuration of default setup for code scanning to better meet your needs.
## Who can use this feature?
Organization owners, security managers, and organization members with the **admin** role
## In this article
  * [About editing your configuration of default setup](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/editing-your-configuration-of-default-setup#about-editing-your-configuration-of-default-setup)
  * [Customizing your existing configuration of default setup](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/editing-your-configuration-of-default-setup#customizing-your-existing-configuration-of-default-setup)
  * [Defining the alert severities that cause a check failure for a pull request](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/editing-your-configuration-of-default-setup#defining-the-alert-severities-that-cause-a-check-failure-for-a-pull-request)
  * [Including local sources of tainted data in default setup](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/editing-your-configuration-of-default-setup#including-local-sources-of-tainted-data-in-default-setup)
  * [Extending CodeQL coverage with CodeQL model packs in default setup](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/editing-your-configuration-of-default-setup#extending-codeql-coverage-with-codeql-model-packs-in-default-setup)


## [About editing your configuration of default setup](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/editing-your-configuration-of-default-setup#about-editing-your-configuration-of-default-setup)
After running an initial analysis of your code with default setup, you may need to make changes to your configuration to better meet your needs. For existing configurations of default setup, you can edit:
  * Which languages default setup will analyze.
  * The query suite run during analysis. For more information on the available query suites, see [CodeQL query suites](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/codeql-query-suites).
  * The threat models (public preview) to use for analysis. Your choice of threat model determines which sources of tainted data are treated as a risk to your application. During the public preview, threat models are supported only for analysis of Java/Kotlin and C#. For more information about threat models, see [Including local sources of tainted data in default setup](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/editing-your-configuration-of-default-setup#including-local-sources-of-tainted-data-in-default-setup).


If your codebase depends on a library or framework that is not recognized by the standard libraries included with CodeQL, you can also extend the CodeQL coverage in default setup using CodeQL model packs. For more information, see [Extending CodeQL coverage with CodeQL model packs in default setup](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/editing-your-configuration-of-default-setup#extending-codeql-coverage-with-codeql-model-packs-in-default-setup).
If you need to change any other aspects of your code scanning configuration, consider configuring advanced setup. For more information, see [Configuring advanced setup for code scanning](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning).
## [Customizing your existing configuration of default setup](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/editing-your-configuration-of-default-setup#customizing-your-existing-configuration-of-default-setup)
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Security" section of the sidebar, click 
  4. In the "CodeQL analysis" row of the "Code Security" section, select 
  5. In the "CodeQL default configuration" window, click 
  6. Optionally, in the "Languages" section, select or deselect languages for analysis.
  7. Optionally, in the "Query suite" row of the "Scan settings" section, select a different query suite to run against your code.
  8. Optionally, to use labeled runners, in the "Runner type" section of the "CodeQL default configuration" modal dialog, select **Standard GitHub runner** **Labeled runner**. Then, next to "Runner label", enter the label of an existing self-hosted or GitHub-hosted runner. For more information, see [Configuring default setup for code scanning](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning#assigning-labels-to-runners).
  9. (Public preview) Optionally, in the "Threat model" row of the "Scan settings" section, select **Remote and local sources**. This option is only available for repositories with code in a supported language: Java/Kotlin and C#.
  10. To update your configuration, as well as run an initial analysis of your code with the new configuration, click **Save changes**. All future analyses will use your new configuration.


## [Defining the alert severities that cause a check failure for a pull request](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/editing-your-configuration-of-default-setup#defining-the-alert-severities-that-cause-a-check-failure-for-a-pull-request)
You can use rulesets to prevent pull requests from being merged when one of the following conditions is met:
  * A required tool found a code scanning alert of a severity that is defined in a ruleset.
  * A required code scanning tool's analysis is still in progress.
  * A required code scanning tool is not configured for the repository.


For more information, see [Set code scanning merge protection](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/set-code-scanning-merge-protection). For more general information about rulesets, see [About rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets).
## [Including local sources of tainted data in default setup](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/editing-your-configuration-of-default-setup#including-local-sources-of-tainted-data-in-default-setup)
Threat models are currently in public preview and subject to change. During the public preview, threat models are supported only by analysis for Java/Kotlin and C#.
If your codebase only considers remote network requests to be potential sources of tainted data, then we recommend using the default threat model. If your codebase considers sources other than network requests to potentially contain tainted data, then you can use threat models to add these additional sources to your CodeQL analysis. During the public preview, you can add local sources (for example: command-line arguments, environment variables, file systems, and databases) that your codebase may consider to be additional sources of tainted data.
You can edit the threat model used in a default setup configuration. For more information, see [Customizing your existing configuration of default setup](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/editing-your-configuration-of-default-setup#customizing-your-existing-configuration-of-default-setup).
## [Extending CodeQL coverage with CodeQL model packs in default setup](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/editing-your-configuration-of-default-setup#extending-codeql-coverage-with-codeql-model-packs-in-default-setup)
CodeQL model packs are currently in public preview and subject to change. Model packs are supported for C/C++, C#, Java/Kotlin, Python, and Ruby analysis.
The CodeQL model editor in the CodeQL extension for Visual Studio Code supports modeling dependencies for C#, Java/Kotlin, Python, and Ruby.
If you use frameworks and libraries that are not recognized by the standard libraries included with CodeQL, you can model your dependencies and extend code scanning analysis. For more information, see [Supported languages and frameworks](https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/) in the documentation for CodeQL.
For default setup, you need to define the models of your additional dependencies in CodeQL model packs. You can extend coverage in default setup with CodeQL model packs for individual repositories, or at scale for all repositories in an organization.
For more information about CodeQL model packs and writing your own, see [Using the CodeQL model editor](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/using-the-codeql-model-editor).
### [Extending coverage for a repository](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/editing-your-configuration-of-default-setup#extending-coverage-for-a-repository)
  1. In the `.github/codeql/extensions` directory of the repository, copy the model pack directory which should include a `codeql-pack.yml` file and any `.yml` files containing additional models for the libraries or frameworks you wish to include in your analysis.
  2. The model packs will be automatically detected and used in your code scanning analysis.
  3. If you later change your configuration to use advanced setup, any model packs in the `.github/codeql/extensions` directory will still be recognized and used.


### [Extending coverage for all repositories in an organization](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/editing-your-configuration-of-default-setup#extending-coverage-for-all-repositories-in-an-organization)
If you extend coverage with CodeQL model packs for all repositories in an organization, the model packs that you specify must be published to the GitHub Container registry and be accessible to the repositories that run code scanning. For more information, see [Working with the Container registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry).
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Under your organization name, click **Settings**.
![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](https://docs.github.com/assets/cb-49309/images/help/discussions/org-settings-global-nav-update.png)
  3. In the "Security" section of the sidebar, click **Global settings**.
  4. Find the "Code scanning" section.
  5. Next to "Expand CodeQL analysis", click **Configure**.
  6. Enter references to the published model packs you want to use, one per line, then click **Save**.
![Screenshot of the "Expand CodeQL analysis" view" in the settings for an organization.](https://docs.github.com/assets/cb-61123/images/help/security/enable-codeql-org-model-packs.png)
  7. The model packs will be automatically detected and used when code scanning runs on any repository in the organization with default setup enabled.


