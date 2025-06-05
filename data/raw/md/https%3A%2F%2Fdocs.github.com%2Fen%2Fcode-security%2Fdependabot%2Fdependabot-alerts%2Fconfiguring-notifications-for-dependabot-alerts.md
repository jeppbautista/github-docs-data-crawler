  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Dependabot](https://docs.github.com/en/code-security/dependabot "Dependabot")/
  * [Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts "Dependabot alerts")/
  * [Configure notifications](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/configuring-notifications-for-dependabot-alerts "Configure notifications")


# Configuring notifications for Dependabot alerts
Optimize how you receive notifications about Dependabot alerts.
## In this article
  * [About notifications for Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/configuring-notifications-for-dependabot-alerts#about-notifications-for-dependabot-alerts)
  * [Configuring notifications for Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/configuring-notifications-for-dependabot-alerts#configuring-notifications-for-dependabot-alerts)
  * [How to reduce the noise from notifications for Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/configuring-notifications-for-dependabot-alerts#how-to-reduce-the-noise-from-notifications-for-dependabot-alerts)
  * [Further reading](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/configuring-notifications-for-dependabot-alerts#further-reading)


## [About notifications for Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/configuring-notifications-for-dependabot-alerts#about-notifications-for-dependabot-alerts)
When Dependabot detects vulnerable dependencies in your repositories, we generate a Dependabot alert and display it on the **Security** tab for the repository. GitHub notifies the maintainers of affected repositories about the new alert according to their notification preferences. Dependabot is enabled by default on all public repositories, and needs to be enabled on private repositories. By default, you will receive Dependabot alerts by email. You can override the default overall behavior by choosing the type of notifications you want to receive, or switching notifications off altogether in the settings page for your user notifications at <https://github.com/settings/notifications>.
Dependabot doesn't generate Dependabot alerts for malware. For more information, see [About the GitHub Advisory database](https://docs.github.com/en/code-security/security-advisories/working-with-global-security-advisories-from-the-github-advisory-database/about-the-github-advisory-database#malware-advisories).
Regardless of your notification preferences, when Dependabot is first enabled, GitHub does not send notifications for all vulnerable dependencies found in your repository. Instead, you will receive notifications for new vulnerable dependencies identified after Dependabot is enabled, if your notification preferences allow it.
If you're an organization owner, you can enable or disable Dependabot alerts for all repositories in your organization with one click. You can also set whether Dependabot alerts will be enabled or disabled for newly-created repositories. For more information, see [Managing security and analysis settings for your organization](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-security-and-analysis-settings-for-your-organization#enabling-or-disabling-a-feature-for-all-new-repositories-when-they-are-added).
## [Configuring notifications for Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/configuring-notifications-for-dependabot-alerts#configuring-notifications-for-dependabot-alerts)
When a new Dependabot alert is detected, GitHub notifies all users with access to Dependabot alerts for the repository according to their notification preferences. You will receive alerts if you are watching the repository, have enabled notifications for security alerts or for all the activity on the repository, and are not ignoring the repository. For more information, see [Configuring notifications](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications#configuring-your-watch-settings-for-an-individual-repository).
You can configure notification settings for yourself or your organization from the Manage notifications drop-down [Configuring notifications](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications#choosing-your-notification-settings).
You can choose the delivery method for notifications, as well as the frequency at which the notifications are sent to you. By default, you will receive notifications:
  * In your inbox, as web notifications. A web notification is sent when Dependabot is enabled for a repository, when a new manifest file is committed to the repository, and when a new vulnerability with a critical or high severity is found (**On GitHub** option).
  * By email. An email is sent when Dependabot is enabled for a repository, when a new manifest file is committed to the repository, and when a new vulnerability with a critical or high severity is found (**Email** option).
  * On the command line. Warnings are displayed as callbacks when you push to repositories with any insecure dependencies (**CLI** option).
  * On GitHub Mobile, as web notifications. For more information, see [Configuring notifications](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications#enabling-push-notifications-with-github-mobile).


The email and web/GitHub Mobile notifications are:
  * _Per repository_ when Dependabot is enabled on the repository, or when a new manifest file is committed to the repository.
  * _Per organization_ when a new vulnerability is discovered.
  * Sent when a new vulnerability is discovered. GitHub doesn't send notifications when vulnerabilities are updated.


You can customize the way you are notified about Dependabot alerts. For example, you can receive a daily or weekly digest email summarizing alerts for up to 10 of your repositories using the **Email weekly digest** option.
![Screenshot of the notification options for Dependabot alerts. A dropdown menu with frequency options is outlined in orange.](https://docs.github.com/assets/cb-70021/images/help/dependabot/dependabot-notification-frequency.png)
You can filter your notifications on GitHub to show Dependabot alerts. For more information, see [Managing notifications from your inbox](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/viewing-and-triaging-notifications/managing-notifications-from-your-inbox#dependabot-custom-filters).
Email notifications for Dependabot alerts that affect one or more repositories include the `X-GitHub-Severity` header field. You can use the value of the `X-GitHub-Severity` header field to filter email notifications for Dependabot alerts. For more information, see [Configuring notifications](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications#filtering-email-notifications).
## [How to reduce the noise from notifications for Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/configuring-notifications-for-dependabot-alerts#how-to-reduce-the-noise-from-notifications-for-dependabot-alerts)
If you are concerned about receiving too many notifications for Dependabot alerts, we recommend leveraging Dependabot auto-triage rules to auto-dismiss low-risk alerts. Rules are applied before alert notifications are sent, so alerts that are auto-dismissed upon creation do not send notifications. For more information, see [About Dependabot auto-triage rules](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/about-dependabot-auto-triage-rules).
Alternatively, you can opt into the weekly email digest, or even completely turn off notifications while keeping Dependabot alerts enabled. You can still navigate to see your Dependabot alerts in your repository's **Security** tab. For more information, see [Viewing and updating Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/viewing-and-updating-dependabot-alerts).
## [Further reading](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/configuring-notifications-for-dependabot-alerts#further-reading)
  * [Configuring notifications](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications)
  * [Managing notifications from your inbox](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/viewing-and-triaging-notifications/managing-notifications-from-your-inbox#supported-is-queries)


