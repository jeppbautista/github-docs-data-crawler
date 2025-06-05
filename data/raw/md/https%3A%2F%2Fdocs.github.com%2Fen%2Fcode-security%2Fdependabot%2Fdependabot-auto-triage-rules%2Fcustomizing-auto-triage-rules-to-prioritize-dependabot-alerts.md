  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Dependabot](https://docs.github.com/en/code-security/dependabot "Dependabot")/
  * [Dependabot auto-triage rules](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules "Dependabot auto-triage rules")/
  * [Custom auto-triage rules](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/customizing-auto-triage-rules-to-prioritize-dependabot-alerts "Custom auto-triage rules")


# Customizing auto-triage rules to prioritize Dependabot alerts
You can create your own auto-triage rules to control which alerts are dismissed or snoozed, and which alerts you want Dependabot to open pull requests for.
## Who can use this feature?
  * Organization owners
  * Security managers
  * Users with **admin** access (can enable, disable, and view auto-triage rules for the repository, as well as create custom auto-triage rules)


**GitHub presets** are available for all repository types.
**Custom auto-triage rules** are available for the following repository types:
  * Public repositories on GitHub.com
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [About custom auto-triage rules](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/customizing-auto-triage-rules-to-prioritize-dependabot-alerts#about-custom-auto-triage-rules)
  * [Adding custom auto-triage rules to your repository](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/customizing-auto-triage-rules-to-prioritize-dependabot-alerts#adding-custom-auto-triage-rules-to-your-repository)
  * [Adding custom auto-triage rules to your organization](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/customizing-auto-triage-rules-to-prioritize-dependabot-alerts#adding-custom-auto-triage-rules-to-your-organization)
  * [Editing or deleting custom auto-triage rules for your repository](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/customizing-auto-triage-rules-to-prioritize-dependabot-alerts#editing-or-deleting-custom-auto-triage-rules-for-your-repository)
  * [Editing or deleting custom auto-triage rules for your organization](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/customizing-auto-triage-rules-to-prioritize-dependabot-alerts#editing-or-deleting-custom-auto-triage-rules-for-your-organization)


## [About custom auto-triage rules](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/customizing-auto-triage-rules-to-prioritize-dependabot-alerts#about-custom-auto-triage-rules)
You can create your own Dependabot auto-triage rules based on alert metadata. You can choose to auto-dismiss alerts indefinitely, or snooze alerts until a patch becomes available, and you can specify which alerts you want Dependabot to open pull requests for. Rules are applied before alert notifications are sent, so creating custom rules that auto-dismiss low-risk alerts will reduce notification noise from future matching alerts.
Since any rules that you create apply to both future and current alerts, you can also use auto-triage rules to manage your Dependabot alerts in bulk.
Repository administrators can create custom auto-triage rules for their repositories. For private or internal repositories, this requires GitHub Code Security.
Organization owners and security managers can set custom auto-triage rules at the organization-level, and then choose if a rule is enforced or enabled across all public and private repositories in the organization.
  * **Enforced:** If an organization-level rule is "enforced", repository administrators cannot edit, disable, or delete the rule.
  * **Enabled:** If an organization-level rule is "enabled", repository administrators can still disable the rule for their repository.


In the event that an organization-level rule and a repository-level rule specify conflicting behaviors, the action set out by the organization-level rule takes precedence. Dismissal rules always act before rules which trigger Dependabot pull requests.
You can create rules to target alerts using the following metadata:
  * CVE ID
  * CWE
  * Dependency scope (`devDependency` or `runtime`)
  * Ecosystem
  * GHSA ID
  * Manifest path (for repository-level rules only)
  * Package name
  * Patch availability
  * Severity
  * EPSS Score


### [Understanding how custom auto-triage rules and Dependabot security updates interact](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/customizing-auto-triage-rules-to-prioritize-dependabot-alerts#understanding-how-custom-auto-triage-rules-and-dependabot-security-updates-interact)
You can use custom auto-triage rules to tailor which alerts you want Dependabot to open pull requests for. However, for an "open a pull request" rule to take effect, you must ensure that Dependabot security updates are **disabled** for the repository (or repositories) that the rule should apply to.
When Dependabot security updates are enabled for a repository, Dependabot will automatically try to open pull requests to resolve **every** open Dependabot alert that has an available patch. If you prefer to customize this behavior using a rule, you must leave Dependabot security updates disabled.
For more information about enabling or disabling Dependabot security updates for a repository, see [Configuring Dependabot security updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates#managing-dependabot-security-updates-for-your-repositories).
## [Adding custom auto-triage rules to your repository](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/customizing-auto-triage-rules-to-prioritize-dependabot-alerts#adding-custom-auto-triage-rules-to-your-repository)
During the public preview, you can create up to 10 custom auto-triage rules for a repository.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Security" section of the sidebar, click 
  4. Under "Dependabot alerts", click 
  5. Click **New rule**.
  6. Under "Rule name", describe what this rule will do.
  7. Under "State", use the dropdown menu to select whether the rule should be enabled or disabled for the repository.
  8. Under "Target alerts", select the metadata you want to use to filter alerts.
  9. Under "Rules", select the action you want to take on alerts that match the metadata:
     * Select **Dismiss alerts** to auto-dismiss alerts that match the metadata. You can choose to dismiss alerts indefinitely or until a patch is available.
     * Select **Open a pull request to resolve this alert** if you want Dependabot to suggest changes to resolve alerts that match the targeted metadata. Note that this option is unavailable if you have already selected the option to dismiss alerts indefinitely, or if Dependabot security updates are enabled in your repository settings.
  10. Click **Create rule**.


## [Adding custom auto-triage rules to your organization](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/customizing-auto-triage-rules-to-prioritize-dependabot-alerts#adding-custom-auto-triage-rules-to-your-organization)
You can add custom auto-triage rules for all eligible repositories in your organization. For more information, see [Configuring global security settings for your organization](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#creating-and-managing-dependabot-auto-triage-rules).
## [Editing or deleting custom auto-triage rules for your repository](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/customizing-auto-triage-rules-to-prioritize-dependabot-alerts#editing-or-deleting-custom-auto-triage-rules-for-your-repository)
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Security" section of the sidebar, click 
  4. Under "Dependabot alerts", click 
  5. Under "Repository rules", to the right of the rule that you want to edit or delete, click 
  6. To edit the rule, make any changes to the applicable fields, then click **Save rule**.
  7. To delete the rule, under "Danger Zone", click **Delete rule**.
  8. In the "Are you sure you want to delete this rule?" dialog box, review the information, then click **Delete rule**.


## [Editing or deleting custom auto-triage rules for your organization](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/customizing-auto-triage-rules-to-prioritize-dependabot-alerts#editing-or-deleting-custom-auto-triage-rules-for-your-organization)
You can edit or delete custom auto-triage rules for all eligible repositories in your organization. For more information, see [Configuring global security settings for your organization](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#creating-and-managing-dependabot-auto-triage-rules).
