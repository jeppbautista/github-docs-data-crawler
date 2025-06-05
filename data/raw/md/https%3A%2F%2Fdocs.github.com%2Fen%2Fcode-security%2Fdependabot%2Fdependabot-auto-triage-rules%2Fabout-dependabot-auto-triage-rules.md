  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Dependabot](https://docs.github.com/en/code-security/dependabot "Dependabot")/
  * [Dependabot auto-triage rules](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules "Dependabot auto-triage rules")/
  * [About auto-triage rules](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/about-dependabot-auto-triage-rules "About auto-triage rules")


# About Dependabot auto-triage rules
Dependabot auto-triage rules are a powerful tool to help you better manage your security alerts at scale. GitHub presets are rules curated by GitHub that you can use to filter out a substantial amount of false positives. Custom auto-triage rules provide control over which alerts are ignored, snoozed, or trigger a Dependabot security update to resolve the alert.
## Who can use this feature?
**GitHub presets** are available for all repository types.
**Custom auto-triage rules** are available for the following repository types:
  * Public repositories on GitHub.com
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [About Dependabot auto-triage rules](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/about-dependabot-auto-triage-rules#about-dependabot-auto-triage-rules)
  * [Further reading](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/about-dependabot-auto-triage-rules#further-reading)


## [About Dependabot auto-triage rules](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/about-dependabot-auto-triage-rules#about-dependabot-auto-triage-rules)
Dependabot auto-triage rules allow you to instruct Dependabot to automatically triage Dependabot alerts. You can use auto-triage rules to automatically dismiss or snooze certain alerts, or specify the alerts you want Dependabot to open pull requests for. Rules are applied before alert notifications are sent, so enabling rules that auto-dismiss low-risk alerts will prevent notification noise from future matching alerts.
There are two types of Dependabot auto-triage rules:
  * GitHub presets
  * Custom auto-triage rules


### [About GitHub presets](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/about-dependabot-auto-triage-rules#about-github-presets)
GitHub presets for Dependabot alerts are rules that are available for all repositories.
GitHub presets are rules curated by GitHub. The `Dismiss low impact issues for development-scoped dependencies` is a GitHub preset rule. This rule auto-dismisses certain types of vulnerabilities that are found in npm dependencies used in development. The rule has been curated to reduce false positives and reduce alert fatigue. You cannot modify GitHub presets. For more information about GitHub presets, see [Using GitHub preset rules to prioritize Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/using-github-preset-rules-to-prioritize-dependabot-alerts).
The rule is enabled by default for public repositories and can be opted into for private repositories. You can enable the rule for a private repository via the **Settings** tab for the repository. For more information, see [Enabling the `Dismiss low impact issues for development-scoped dependencies` rule for your private repository](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/using-github-preset-rules-to-prioritize-dependabot-alerts#enabling-the-dismiss-low-impact-issues-for-development-scoped-dependencies-rule-for-your-private-repository).
### [About custom auto-triage rules](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/about-dependabot-auto-triage-rules#about-custom-auto-triage-rules)
Custom auto-triage rules for Dependabot alerts are available on public repositories and on any organization-owned repositories in GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled.
With custom auto-triage rules, you can create your own rules to automatically dismiss or reopen alerts based on targeted metadata, such as severity, package name, CWE, and more. You can also specify which alerts you want Dependabot to open pull requests for. For more information, see [Customizing auto-triage rules to prioritize Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/customizing-auto-triage-rules-to-prioritize-dependabot-alerts).
You can create custom rules from the **Settings** tab of the repository, provided the repository belongs to an organization that has a license for GitHub Code Security or GitHub Advanced Security. For more information, see [Adding custom auto-triage rules to your repository](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/customizing-auto-triage-rules-to-prioritize-dependabot-alerts#adding-custom-auto-triage-rules-to-your-repository).
### [About auto-dismissing alerts](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/about-dependabot-auto-triage-rules#about-auto-dismissing-alerts)
Whilst you may find it useful to use auto-triage rules to auto-dismiss alerts, you can still reopen auto-dismissed alerts and filter to see which alerts have been auto-dismissed. For more information, see [Managing alerts that have been automatically dismissed by a Dependabot auto-triage rule](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/managing-automatically-dismissed-alerts).
Additionally, auto-dismissed alerts are still available for reporting and reviewing, and can be auto-reopened if the alert metadata changes, for example:
  * If you change the scope of a dependency from development to production.
  * If GitHub modifies certain metadata for the related advisory.


Auto-dismissed alerts are defined by the `resolution:auto-dismiss` close reason. Automatic dismissal activity is included in alert webhooks, REST and GraphQL APIs, and the audit log. For more information, see [REST API endpoints for Dependabot alerts](https://docs.github.com/en/rest/dependabot/alerts), and the "`repository_vulnerability_alert`" section in [Reviewing the audit log for your organization](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/reviewing-the-audit-log-for-your-organization#repository_vulnerability_alert-category-actions).
## [Further reading](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/about-dependabot-auto-triage-rules#further-reading)
  * [Using GitHub preset rules to prioritize Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/using-github-preset-rules-to-prioritize-dependabot-alerts)
  * [Customizing auto-triage rules to prioritize Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/customizing-auto-triage-rules-to-prioritize-dependabot-alerts)


