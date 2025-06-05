  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secure your organization](https://docs.github.com/en/code-security/securing-your-organization "Secure your organization")/
  * [Enable security features](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization "Enable security features")/
  * [Configure global settings](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization "Configure global settings")


# Configuring global security settings for your organization
Customize Advanced Security features to strengthen the security of your organization.
## Who can use this feature?
Organization owners, security managers, and organization members with the **admin** role
## In this article
  * [About global settings](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#about-global-settings)
  * [Accessing the global settings page for your organization](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#accessing-the-global-settings-page-for-your-organization)
  * [Configuring global Dependabot settings](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#configuring-global-dependabot-settings)
  * [Configuring global code scanning settings](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#configuring-global-code-scanning-settings)
  * [Configuring global secret scanning settings](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#configuring-global-secret-scanning-settings)
  * [Creating security managers for your organization](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#creating-security-managers-for-your-organization)


## [About global settings](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#about-global-settings)
Alongside security configurations, which determine repository-level security settings, you should also configure global settings for your organization. Global settings apply to your entire organization, and can customize Advanced Security features based on your needs.
## [Accessing the global settings page for your organization](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#accessing-the-global-settings-page-for-your-organization)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Under your organization name, click **Settings**.
![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](https://docs.github.com/assets/cb-49309/images/help/discussions/org-settings-global-nav-update.png)
  3. In the "Security" section of the sidebar, select the **Advanced Security** dropdown menu, then click **Global settings**.


## [Configuring global Dependabot settings](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#configuring-global-dependabot-settings)
Dependabot consists of three different features that help you manage your dependencies:
  * Dependabot alerts: Inform you about vulnerabilities in the dependencies that you use in your repository.
  * Dependabot security updates: Automatically raise pull requests to update the dependencies you use that have known security vulnerabilities.
  * Dependabot version updates: Automatically raise pull requests to keep your dependencies up-to-date.


You can customize several global settings for Dependabot:
  * [Creating and managing Dependabot auto-triage rules](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#creating-and-managing-dependabot-auto-triage-rules)
  * [Grouping Dependabot security updates](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#grouping-dependabot-security-updates)
  * [Enabling dependency updates on GitHub Actions runners](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#enabling-dependency-updates-on-github-actions-runners)
  * [Granting Dependabot access to private repositories](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#granting-dependabot-access-to-private-repositories)


### [Creating and managing Dependabot auto-triage rules](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#creating-and-managing-dependabot-auto-triage-rules)
You can create and manage Dependabot auto-triage rules to instruct Dependabot to automatically dismiss or snooze Dependabot alerts, and even open pull requests to attempt to resolve them. To configure Dependabot auto-triage rules, click 
  * You can create a new rule by clicking **New rule** , then entering the details for your rule and clicking **Create rule**.
  * You can edit an existing rule by clicking **Save rule**.


For more information on Dependabot auto-triage rules, see [About Dependabot auto-triage rules](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/about-dependabot-auto-triage-rules) and [Customizing auto-triage rules to prioritize Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/customizing-auto-triage-rules-to-prioritize-dependabot-alerts#adding-custom-auto-triage-rules-to-your-organization).
### [Grouping Dependabot security updates](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#grouping-dependabot-security-updates)
Dependabot can group all automatically suggested security updates into a single pull request. To enable grouped security updates, select **Grouped security updates**. For more information about grouped updates and customization options, see [Configuring Dependabot security updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates#grouping-dependabot-security-updates-into-a-single-pull-request).
### [Enabling dependency updates on GitHub Actions runners](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#enabling-dependency-updates-on-github-actions-runners)
If both Dependabot and GitHub Actions are enabled for existing repositories in your organization, GitHub will automatically use GitHub-hosted runners to run dependency updates for those repositories.
Otherwise, to allow Dependabot to use GitHub Actions runners to perform dependency updates for all existing repositories in the organization, select "Dependabot on Actions runners".
For more information, see [About Dependabot on GitHub Actions runners](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/about-dependabot-on-github-actions-runners).
To have greater control over Dependabot's access to your private registries and internal network resources, you can configure Dependabot to run on GitHub Actions self-hosted runners. For more information, see [About Dependabot on GitHub Actions runners](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/about-dependabot-on-github-actions-runners) and [Managing Dependabot on self-hosted runners](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/managing-dependabot-on-self-hosted-runners).
### [Granting Dependabot access to private repositories](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#granting-dependabot-access-to-private-repositories)
To update private dependencies of repositories in your organization, Dependabot needs access to those repositories. To grant Dependabot access to the desired private repository, scroll down to the "Grant Dependabot access to private repositories" section, then use the search bar to find and select the desired repository. Be aware that granting Dependabot access to a repository means all users in your organization will have access to the contents of that repository through Dependabot updates. For more information about the supported ecosystems for private repositories, see [Dependabot supported ecosystems and repositories](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories).
## [Configuring global code scanning settings](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#configuring-global-code-scanning-settings)
Code scanning is a feature that you use to analyze the code in a GitHub repository to find security vulnerabilities and coding errors. Any problems identified by the analysis are shown in your repository.
You can customize several global settings for code scanning:
  * [Enabling Copilot Autofix for CodeQL](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#enabling-copilot-autofix-for-codeql)
  * [Enabling Copilot Autofix for third-party code scanning tools](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#enabling-copilot-autofix-for-third-party-code-scanning-tools)
  * [Recommending the extended query suite for default setup](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#recommending-the-extended-query-suite-for-default-setup)


### [Recommending the extended query suite for default setup](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#recommending-the-extended-query-suite-for-default-setup)
Code scanning offers specific groups of CodeQL queries, called CodeQL query suites, to run against your code. By default, the "Default" query suite is run. GitHub also offers the "Extended" query suite, which contains all the queries in the "Default" query suite, plus additional queries with lower precision and severity. To suggest the "Extended" query suite across your organization, select **Recommend the extended query suite for repositories enabling default setup**. For more information on built-in query suites for CodeQL default setup, see [CodeQL query suites](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/codeql-query-suites).
### [Enabling Copilot Autofix for CodeQL](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#enabling-copilot-autofix-for-codeql)
You can select **Copilot Autofix** to enable Copilot Autofix for all the repositories in your organization that use CodeQL default setup or CodeQL advanced setup. Copilot Autofix is an expansion of code scanning that suggests fixes for code scanning alerts. For more information, see [Responsible use of Copilot Autofix for code scanning](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/responsible-use-autofix-code-scanning).
### [Enabling Copilot Autofix for third-party code scanning tools](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#enabling-copilot-autofix-for-third-party-code-scanning-tools)
Third-party code scanning tool support is in public preview, and subject to change. Currently, the third-party tool ESLint is supported. For more information, see [Responsible use of Copilot Autofix for code scanning](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/responsible-use-autofix-code-scanning).
You can select **Copilot Autofix for third-party tools** to enable Copilot Autofix for all the repositories in your organization that use third-party tools. Copilot Autofix is an expansion of code scanning that suggests fixes for code scanning alerts.
## [Configuring global secret scanning settings](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#configuring-global-secret-scanning-settings)
Secret scanning is a security tool that scans the entire Git history of repositories, as well as issues, pull requests, discussions, and wikis in those repositories, for leaked secrets that have been accidentally committed, such as tokens or private keys.
You can customize several global settings for secret scanning:
  * [Adding a resource link for blocked commits](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#adding-a-resource-link-for-blocked-commits)
  * [Defining custom patterns](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#defining-custom-patterns)


### [Adding a resource link for blocked commits](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#adding-a-resource-link-for-blocked-commits)
To provide context for developers when secret scanning blocks a commit, you can display a link with more information on why the commit was blocked. To include a link, select **Add a resource link in the CLI and the web UI when a commit is blocked**. In the text box, type the link to the desired resource, then click **Save Link**.
### [Defining custom patterns](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#defining-custom-patterns)
You can define custom patterns for secret scanning with regular expressions. Custom patterns can identify secrets that are not detected by the default patterns supported by secret scanning. To create a custom pattern, click **New pattern** , then enter the details for your pattern and click **Save and dry run**. For more information on custom patterns, see [Defining custom patterns for secret scanning](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/defining-custom-patterns-for-secret-scanning).
## [Creating security managers for your organization](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#creating-security-managers-for-your-organization)
The security manager role grants members of your organization the ability to manage security settings and alerts across your organization. Security managers can view data for all repositories in your organization through security overview.
To learn more about the security manager role, see [Managing security managers in your organization](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization).
To assign the security manager role, see [Using organization roles](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/using-organization-roles#assigning-an-organization-role).
