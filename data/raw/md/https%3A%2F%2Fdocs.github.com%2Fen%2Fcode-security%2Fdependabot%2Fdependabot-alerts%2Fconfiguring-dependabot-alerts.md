  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Dependabot](https://docs.github.com/en/code-security/dependabot "Dependabot")/
  * [Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts "Dependabot alerts")/
  * [Configure Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/configuring-dependabot-alerts "Configure Dependabot alerts")


# Configuring Dependabot alerts
Enable Dependabot alerts to be generated when a new vulnerable dependency is found in one of your repositories.
## Who can use this feature?
  * Repository administrators, organization owners, and people with **write** or **maintain** access
  * Users and teams with explicit access. See [Granting access to security alert](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-security-and-analysis-settings-for-your-repository#granting-access-to-security-alerts).


## In this article
  * [About Dependabot alerts for vulnerable dependencies](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/configuring-dependabot-alerts#about-dependabot-alerts-for-vulnerable-dependencies)
  * [Managing Dependabot alerts for your personal account](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/configuring-dependabot-alerts#managing-dependabot-alerts-for-your-personal-account)
  * [Managing Dependabot alerts for your repository](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/configuring-dependabot-alerts#managing-dependabot-alerts-for-your-repository)
  * [Managing Dependabot alerts for your organization](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/configuring-dependabot-alerts#managing-dependabot-alerts-for-your-organization)


## [About Dependabot alerts for vulnerable dependencies](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/configuring-dependabot-alerts#about-dependabot-alerts-for-vulnerable-dependencies)
A vulnerability is a problem in a project's code that could be exploited to damage the confidentiality, integrity, or availability of the project or other projects that use its code. Vulnerabilities vary in type, severity, and method of attack.
Dependabot scans code when a new advisory is added to the GitHub Advisory Database or the dependency graph for a repository changes. When vulnerable dependencies are detected, Dependabot alerts are generated. For more information, see [About Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts).
If you have enabled Dependabot security updates for your repository, the alert may also contain a link to a pull request to update the manifest or lock file to the minimum version that resolves the vulnerability. For more information, see [About Dependabot security updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates).
You can enable or disable Dependabot alerts for:
  * Your personal account
  * Your repository
  * Your organization


Additionally, you can use Dependabot auto-triage rules to manage your alerts at scale, so you can auto-dismiss or snooze alerts, and specify which alerts you want Dependabot to open pull requests for. For information about the different types of auto-triage rules, and whether your repositories are eligible, see [About Dependabot auto-triage rules](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/about-dependabot-auto-triage-rules).
## [Managing Dependabot alerts for your personal account](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/configuring-dependabot-alerts#managing-dependabot-alerts-for-your-personal-account)
You can enable or disable Dependabot alerts for all repositories owned by your personal account.
### [Enabling or disabling Dependabot alerts for existing repositories](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/configuring-dependabot-alerts#enabling-or-disabling-dependabot-alerts-for-existing-repositories)
  1. In the upper-right corner of any page on GitHub, click your profile photo, then click 
  2. In the "Security" section of the sidebar, click 
  3. Under "Advanced Security", to the right of Dependabot alerts, click **Disable all** or **Enable all**.
  4. Optionally, to enable Dependabot alerts by default for new repositories that you create, in the dialog box, select "Enable by default for new repositories".
  5. Click **Disable Dependabot alerts** or **Enable Dependabot alerts** to disable or enable Dependabot alerts for all the repositories you own.


When you enable Dependabot alerts for existing repositories, you will see any results displayed on GitHub within minutes.
### [Enabling or disabling Dependabot alerts for new repositories](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/configuring-dependabot-alerts#enabling-or-disabling-dependabot-alerts-for-new-repositories)
  1. In the upper-right corner of any page on GitHub, click your profile photo, then click 
  2. In the "Security" section of the sidebar, click 
  3. Under "Advanced Security", to the right of Dependabot alerts, select **Automatically enable for new repositories**.


## [Managing Dependabot alerts for your repository](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/configuring-dependabot-alerts#managing-dependabot-alerts-for-your-repository)
You can manage Dependabot alerts for your public, private or internal repository.
By default, we notify people with write, maintain, or admin permissions in the affected repositories about new Dependabot alerts. GitHub never publicly discloses insecure dependencies for any repository. You can also make Dependabot alerts visible to additional people or teams working on repositories that you own or have admin permissions for.
If you enable security and analysis features, GitHub performs read-only analysis on your repository.
### [Enabling or disabling Dependabot alerts for a repository](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/configuring-dependabot-alerts#enabling-or-disabling-dependabot-alerts-for-a-repository)
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Security" section of the sidebar, click 
  4. Under "Advanced Security", to the right of Dependabot alerts, click **Enable** to enable alerts or **Disable** to disable alerts.


## [Managing Dependabot alerts for your organization](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/configuring-dependabot-alerts#managing-dependabot-alerts-for-your-organization)
You can enable Dependabot alerts for all eligible repositories in your organization. For more information, see [About enabling security features at scale](https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/about-enabling-security-features-at-scale).
