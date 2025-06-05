  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Manage alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts "Manage alerts")/
  * [Disable Copilot Autofix](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/disabling-autofix-for-code-scanning "Disable Copilot Autofix")


# Disabling Copilot Autofix for code scanning
You can choose to disallow GitHub Copilot Autofix for an enterprise or disable GitHub Copilot Autofix at the organization and repository level.
## Who can use this feature?
GitHub Copilot Autofix for code scanning is available for the following repository types:
  * Public repositories on GitHub.com
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [About disabling Copilot Autofix for code scanning](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/disabling-autofix-for-code-scanning#about-disabling-copilot-autofix-for-code-scanning)
  * [Blocking use of Copilot Autofix for an enterprise](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/disabling-autofix-for-code-scanning#blocking-use-of-copilot-autofix-for-an-enterprise)
  * [Disabling Copilot Autofix for an organization](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/disabling-autofix-for-code-scanning#disabling-copilot-autofix-for-an-organization)
  * [Disabling Copilot Autofix for a repository](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/disabling-autofix-for-code-scanning#disabling-copilot-autofix-for-a-repository)


## [About disabling Copilot Autofix for code scanning](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/disabling-autofix-for-code-scanning#about-disabling-copilot-autofix-for-code-scanning)
GitHub Copilot Autofix is a GitHub Copilot-powered expansion of code scanning. It provides users with targeted recommendations to help them fix code scanning alerts (including CodeQL alerts) so they can avoid introducing new security vulnerabilities. To learn more about Copilot Autofix for code scanning, see [Responsible use of Copilot Autofix for code scanning](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/responsible-use-autofix-code-scanning).
You do not need a subscription to GitHub Copilot to use GitHub Copilot Autofix. Copilot Autofix is available to all public repositories on GitHub.com, as well as internal or private repositories owned by organizations and enterprises that have a license for GitHub Code Security.
Copilot Autofix is allowed by default and enabled for every repository that uses CodeQL, regardless of whether it uses default or advanced setup for code scanning. Administrators at the enterprise, organization and repository levels can choose to opt out and disable Copilot Autofix.
Note that disabling Copilot Autofix at any level will close all open Copilot Autofix comments. If Copilot Autofix is disabled and then subsequently enabled, Copilot Autofix won't automatically suggest fixes for any pull requests that are already open. The suggestions will only be generated for any pull requests that are opened after Copilot Autofix is enabled, or after re-running code scanning analysis on existing pull requests.
## [Blocking use of Copilot Autofix for an enterprise](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/disabling-autofix-for-code-scanning#blocking-use-of-copilot-autofix-for-an-enterprise)
Enterprise administrators can disallow Copilot Autofix for their enterprise. If you disallow Copilot Autofix for an enterprise, Copilot Autofix cannot be enabled for any organizations or repositories within the enterprise.
Note that allowing Copilot Autofix for an enterprise does not enforce enablement of Copilot Autofix, but means that organization and repository administrators will have the option to enable or disable Copilot Autofix.
Disallowing Copilot Autofix at the enterprise level will remove all open Copilot Autofix comments across all repositories of all organizations within the enterprise.
  1. On the left side of the page, in the enterprise account sidebar, click 
  2. Under **Advanced Security**.
  3. Under "Copilot Autofix", use the dropdown menu to choose "Not allowed."


## [Disabling Copilot Autofix for an organization](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/disabling-autofix-for-code-scanning#disabling-copilot-autofix-for-an-organization)
If Copilot Autofix is allowed at the enterprise level, organization administrators have the option to disable Copilot Autofix for an organization. If you disable Copilot Autofix for an organization, Copilot Autofix cannot be enabled for any repositories within the organization.
Note that disabling Copilot Autofix at the organization level will remove all open Copilot Autofix comments across all repositories in the organization.
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the "Security" section of the sidebar, click **Global settings**.
  4. Under the "Code scanning" section, deselect **Copilot Autofix** or **Copilot Autofix for third-party tools**.


For more information about configuring global code scanning settings, see [Configuring global security settings for your organization](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#configuring-global-code-scanning-settings).
## [Disabling Copilot Autofix for a repository](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/disabling-autofix-for-code-scanning#disabling-copilot-autofix-for-a-repository)
If Copilot Autofix is allowed at the enterprise level and enabled at the organization level, repository administrators have the option to disable Copilot Autofix for a repository. Disabling Copilot Autofix at the repository level will remove all open Copilot Autofix comments across the repository.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Security" section of the sidebar, click 
  4. In the "Code Security" section, deselect **Copilot Autofix** or **Copilot Autofix for third-party tools**.


