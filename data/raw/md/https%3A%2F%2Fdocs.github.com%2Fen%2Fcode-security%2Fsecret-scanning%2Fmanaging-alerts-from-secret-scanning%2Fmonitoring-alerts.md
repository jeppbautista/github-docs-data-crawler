  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secret scanning](https://docs.github.com/en/code-security/secret-scanning "Secret scanning")/
  * [Manage alerts](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning "Manage alerts")/
  * [Monitor alerts](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/monitoring-alerts "Monitor alerts")


# Monitoring alerts from secret scanning
Learn how and when GitHub will notify you about a secret scanning alert.
## Who can use this feature?
Repository owners, organization owners, security managers, and users with the **admin** role
## In this article
  * [Configuring notifications for secret scanning alerts](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/monitoring-alerts#configuring-notifications-for-secret-scanning-alerts)
  * [Auditing responses to secret scanning alerts](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/monitoring-alerts#auditing-responses-to-secret-scanning-alerts)


## [Configuring notifications for secret scanning alerts](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/monitoring-alerts#configuring-notifications-for-secret-scanning-alerts)
In addition to displaying an alert in the **Security** tab of the repository, GitHub can also send email notifications for alerts. These notifications are different for incremental scans and historical scans.
### [Incremental scans](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/monitoring-alerts#incremental-scans)
When a new secret is detected, GitHub notifies all users with access to security alerts for the repository according to their notification preferences. These users include:
  * Repository administrators
  * Security managers
  * Users with custom roles with read/write access
  * Organization owners and enterprise owners, if they are administrators of repositories where secrets were leaked


Commit authors who've accidentally committed secrets will be notified, regardless of their notification preferences.
You will receive an email notification if:
  * You are watching the repository.
  * You have enabled notifications for "All Activity", or for custom "Security alerts" on the repository.
  * In your notification settings, under "Subscriptions", then under "Watching", you have selected to receive notifications by email.


  1. On GitHub, navigate to the main page of the repository.
  2. To start watching the repository, select 
![Screenshot of the repository's main page. A dropdown menu, titled "Watch", is highlighted with an orange outline.](https://docs.github.com/assets/cb-6045/images/help/repository/repository-watch-dropdown.png)
  3. In the dropdown menu, click **All Activity**. Alternatively, to only subscribe to security alerts, click **Custom** , then click **Security alerts**.
  4. Navigate to the notification settings for your personal account. These are available at <https://github.com/settings/notifications>.
  5. On your notification settings page, under "Subscriptions", then under "Watching", select the **Notify me** dropdown.
  6. Select "Email" as a notification option, then click **Save**.
![Screenshot of the notification settings for a user account. Under "Subscriptions" and "Watching" a checkbox, titled "Email", is outlined in orange.](https://docs.github.com/assets/cb-65804/images/help/notifications/repository-watching-notification-options.png)


For more information about setting up notification preferences, see [Managing security and analysis settings for your repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-security-and-analysis-settings-for-your-repository#granting-access-to-security-alerts) and [Configuring your watch settings for an individual repository](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications#configuring-your-watch-settings-for-an-individual-repository).
### [Historical scans](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/monitoring-alerts#historical-scans)
For historical scans, GitHub notifies the following users:
  * Organization owners, enterprise owners, and security managers—whenever a historical scan is complete, even if no secrets are found.
  * Repository administrators, security managers, and users with custom roles with read/write access—whenever a historical scan detects a secret, and according to their notification preferences.


We do _not_ notify commit authors.
For more information about setting up notification preferences, see [Managing security and analysis settings for your repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-security-and-analysis-settings-for-your-repository#granting-access-to-security-alerts) and [Configuring your watch settings for an individual repository](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications#configuring-your-watch-settings-for-an-individual-repository).
## [Auditing responses to secret scanning alerts](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/monitoring-alerts#auditing-responses-to-secret-scanning-alerts)
You can audit the actions taken in response to secret scanning alerts using GitHub tools. For more information, see [Auditing security alerts](https://docs.github.com/en/code-security/getting-started/auditing-security-alerts).
