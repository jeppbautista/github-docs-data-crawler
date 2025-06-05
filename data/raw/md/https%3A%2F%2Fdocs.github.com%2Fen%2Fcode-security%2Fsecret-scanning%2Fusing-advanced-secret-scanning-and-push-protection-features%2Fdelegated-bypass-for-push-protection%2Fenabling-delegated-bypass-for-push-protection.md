  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secret scanning](https://docs.github.com/en/code-security/secret-scanning "Secret scanning")/
  * [Advanced features](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features "Advanced features")/
  * [Delegated bypass](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection "Delegated bypass")/
  * [Enable delegated bypass](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/enabling-delegated-bypass-for-push-protection "Enable delegated bypass")


# Enabling delegated bypass for push protection
You can use delegated bypass for your organization or repository to control who can push commits that contain secrets identified by secret scanning.
## Who can use this feature?
Repository owners, organization owners, security managers, and users with the **admin** role
## In this article
  * [About enabling delegated bypass for push protection](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/enabling-delegated-bypass-for-push-protection#about-enabling-delegated-bypass-for-push-protection)
  * [Configuring delegated bypass for a repository](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/enabling-delegated-bypass-for-push-protection#configuring-delegated-bypass-for-a-repository)
  * [Configuring delegated bypass for an organization](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/enabling-delegated-bypass-for-push-protection#configuring-delegated-bypass-for-an-organization)
  * [Using fine-grained permissions to control who can review and manage bypass requests](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/enabling-delegated-bypass-for-push-protection#using-fine-grained-permissions-to-control-who-can-review-and-manage-bypass-requests)


## [About enabling delegated bypass for push protection](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/enabling-delegated-bypass-for-push-protection#about-enabling-delegated-bypass-for-push-protection)
Delegated bypass for push protection lets you:
  * Define contributors who can bypass push protection.
  * Adds an approval process for other contributors.


Delegated bypass applies to files created, edited, and uploaded on GitHub.
For more information, see [About delegated bypass for push protection](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/about-delegated-bypass-for-push-protection).
When you enable this feature, you will create a bypass list of roles and teams who can manage requests to bypass push protection. If you don't already have appropriate teams or roles to use, you should create additional teams before you start.
Alternatively, you can grant specific organization members the ability to review and manage bypass requests using fine-grained permissions, which give you more refined control over which individuals and teams can approve and deny bypass requests. For more information, see [Using fine-grained permissions to control who can review and manage bypass requests](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/enabling-delegated-bypass-for-push-protection#using-fine-grained-permissions-to-control-who-can-review-and-manage-bypass-requests).
## [Configuring delegated bypass for a repository](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/enabling-delegated-bypass-for-push-protection#configuring-delegated-bypass-for-a-repository)
If an organization owner configures delegated bypass at the organization-level, the repository-level settings are disabled.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Security" section of the sidebar, click 
  4. Under "Secret Protection", ensure that push protection is enabled for the repository.
  5. Under "Push protection", to the right of "Who can bypass push protection for secret scanning", select the dropdown menu, then click **Specific roles or teams**.
  6. Under "Bypass list", click **Add role or team**.
When you add roles or teams to the "bypass list", these users will be granted the ability to bypass push protection, and they can also review and manage the requests from all other contributors to bypass push protection.
You can't add secret teams to the bypass list.
  7. In the dialog box, select the roles and teams that you want to add to the bypass list, then click **Add selected**.


## [Configuring delegated bypass for an organization](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/enabling-delegated-bypass-for-push-protection#configuring-delegated-bypass-for-an-organization)
You must configure delegated bypass for your organization using a custom security configuration. You can then apply the security configuration to all (or selected) repositories in your organization.
  1. Create a new custom security configuration, or edit an existing one. See [Creating a custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/creating-a-custom-security-configuration#creating-a-custom-security-configuration).
  2. When defining the custom security configuration, under "Secret scanning", ensure that "Push protection" is set to **Enabled**.
  3. Under "Push protection", to the right of "Bypass privileges", select the dropdown menu, then click **Specific actors**.
When you assign bypass privileges to selected actors, these organization members are granted the ability to bypass push protection, and they also review and manage the requests from all other contributors to bypass push protection.
You can't add secret teams to the bypass list.
  4. Click the "Select actors" dropdown menu, then select the roles and teams you want to assign bypass privileges to.
In addition to assigning bypass privileges to roles and teams, you can also grant _individual_ organization members the ability to review and manage bypass requests using fine-grained permissions. See [Using fine-grained permissions to control who can review and manage bypass requests](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/enabling-delegated-bypass-for-push-protection#using-fine-grained-permissions-to-control-who-can-review-and-manage-bypass-requests).
  5. Click **Save configuration**.
  6. Apply the security configuration to all (or selected) repositories in your organization. See [Applying a custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/applying-a-custom-security-configuration).


To learn more about security configurations, see [About enabling security features at scale](https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/about-enabling-security-features-at-scale).
## [Using fine-grained permissions to control who can review and manage bypass requests](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/enabling-delegated-bypass-for-push-protection#using-fine-grained-permissions-to-control-who-can-review-and-manage-bypass-requests)
You can grant specific individuals or teams in your organization the ability to review and manage bypass requests using fine-grained permissions.
  1. Ensure that delegated bypass is enabled for the organization. For more information, follow steps 1-3 in [Configuring delegated bypass for your organization](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/enabling-delegated-bypass-for-push-protection#configuring-delegated-bypass-for-an-organization) and ensure you have saved and applied the security configuration to your selected repositories.
  2. Create (or edit) a custom organization role. For information on creating and editing custom roles, see [Managing custom organization roles](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-custom-organization-roles#creating-a-custom-role).
  3. When choosing which permissions to add to the custom role, select the "Review and manage secret scanning bypass requests" permission.
  4. Assign the custom role to individual members or teams in your organization. For more information on assigning custom roles, see [Using organization roles](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/using-organization-roles#assigning-an-organization-role).


