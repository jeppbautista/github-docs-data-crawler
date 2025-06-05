  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Manage code scanning](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration "Manage code scanning")/
  * [Enable delegated alert dismissal](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/enabling-delegated-alert-dismissal-for-code-scanning "Enable delegated alert dismissal")


# Enabling delegated alert dismissal for code scanning
You can use delegated alert dismissal to control who can dismiss an alert found by code scanning.
## Who can use this feature?
Organization owners, security managers, and repository administrators can enable delegated alert dismissals. Once enabled, organization owners and security managers can dismiss alerts.
## In this article
  * [About enabling delegated alert dismissal](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/enabling-delegated-alert-dismissal-for-code-scanning#about-enabling-delegated-alert-dismissal)
  * [Configuring delegated dismissal for a repository](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/enabling-delegated-alert-dismissal-for-code-scanning#configuring-delegated-dismissal-for-a-repository)
  * [Configuring delegated dismissal for an organization](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/enabling-delegated-alert-dismissal-for-code-scanning#configuring-delegated-dismissal-for-an-organization)


## [About enabling delegated alert dismissal](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/enabling-delegated-alert-dismissal-for-code-scanning#about-enabling-delegated-alert-dismissal)
Delegated alert dismissal is currently in public preview and subject to change.
Delegated alert dismissal lets you restrict which users can directly dismiss an alert. When the feature is enabled, users attempting to dismiss an alert will instead create a request for dismissal.
Enabling the feature automatically assigns organization owners and security managers with the permission to approve or deny dismissal requests for alerts. This permission is:
  * "Review and manage code scanning alert dismissal requests" permission for code scanning.
  * "Review and manage secret scanning alert dismissal requests" permission for secret scanning'


For more information about these permissions, see [Roles in an organization](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#permissions-for-organization-roles).
To learn more about the security manager role, see [Managing security managers in your organization](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization).
The implementation of this approval process can potentially cause some friction, so it's important to ensure that the team of security managers has adequate coverage before proceeding.
Reviewers (security managers and organization owners):
  * Get an email notification for requests. These users need to ensure that they can review these lists periodically, so that there is no backlog and that the process is smooth.
  * Can process requests in a dedicated view in the "Security" tab of the organization. An alert will only be dismissed if the dismissal request is approved; otherwise, the alert will remain open.


Requesters will get an email notification with the decision as to whether the alert can be dismissed or not.
## [Configuring delegated dismissal for a repository](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/enabling-delegated-alert-dismissal-for-code-scanning#configuring-delegated-dismissal-for-a-repository)
If an organization owner configures delegated alert dismissal via an enforced security configuration, the settings can't be changed at the repository level.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Security" section of the sidebar, click 
  4. Under "Code Security", click **Enable** for "Prevent direct alert dismissals".


## [Configuring delegated dismissal for an organization](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/enabling-delegated-alert-dismissal-for-code-scanning#configuring-delegated-dismissal-for-an-organization)
You must configure delegated dismissal for your organization using a custom security configuration. You can then apply the security configuration to all (or selected) repositories in your organization.
  1. Create a new custom security configuration, or edit an existing one. See [Creating a custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/creating-a-custom-security-configuration#creating-a-custom-security-configuration).
  2. When creating the custom security configuration, under "Code scanning", set "Prevent direct alert dismissals" to **Enabled**.
  3. Click **Save configuration**.
  4. Apply the security configuration to all (or selected) repositories in your organization. See [Applying a custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/applying-a-custom-security-configuration).


To learn more about security configurations, see [About enabling security features at scale](https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/about-enabling-security-features-at-scale).
