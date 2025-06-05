  * [Organizations](https://docs.github.com/en/organizations "Organizations")/
  * [Manage organization roles](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles "Manage organization roles")/
  * [Security manager role](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization "Security manager role")


# Managing security managers in your organization
You can give your security experts the least access they need to configure and monitor the use of security features for codebases in your organization.
## Who can use this feature?
Organization owners can assign the security manager role.
## In this article
  * [Permissions for the security manager role](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization#permissions-for-the-security-manager-role)
  * [Managing security managers in your organization](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization#managing-security-managers-in-your-organization)
  * [Creating a custom security role](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization#creating-a-custom-security-role)


The security manager role is an organization-level role that organization owners can assign to any member or team in the organization. When applied, it gives permission to view security alerts and manage settings for security features across your organization, as well as read permission for all repositories in the organization.
## [Permissions for the security manager role](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization#permissions-for-the-security-manager-role)
Organization members and members of teams assigned the security manager role have only the permissions required to effectively manage use of security features for the organization.
  * Read access on all repositories in the organization, in addition to any existing repository access
  * Write access on all security alerts in the organization
  * The ability to configure settings for security features at the organization level, including the ability to enable or disable GitHub Advanced Security features
  * The ability to configure settings for security features at the repository level, including the ability to enable or disable GitHub Advanced Security features


Additional functionality, including a security overview for the organization, is available in organizations that use GitHub Secret Protection, GitHub Code Security, or GitHub Advanced Security.
If a team has the security manager role, people with admin access to the team and a specific repository can change the team's level of access to that repository but cannot remove the access. For more information, see [Managing team access to an organization repository](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/managing-team-access-to-an-organization-repository) and [Managing teams and people with access to your repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-teams-and-people-with-access-to-your-repository).
## [Managing security managers in your organization](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization#managing-security-managers-in-your-organization)
You can assign the pre-defined security manager role to either an organization team or directly to an organization member. Larger organizations may want to create a dedicated team for security management. This approach is especially useful if you want to assign additional permissions to your security experts.
For information about assigning roles to users and teams, see [Using organization roles](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/using-organization-roles).
## [Creating a custom security role](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization#creating-a-custom-security-role)
You can create custom security roles for your organization with reduced or increased access, as needed. For example, you might create a security role limited to managing secret scanning results and bypass requests, or you might create a combined security and audit log role. For more information, see [Managing custom organization roles](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-custom-organization-roles).
