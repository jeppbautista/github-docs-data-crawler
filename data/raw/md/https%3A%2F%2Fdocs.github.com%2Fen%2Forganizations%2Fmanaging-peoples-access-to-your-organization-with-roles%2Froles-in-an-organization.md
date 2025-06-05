  * [Organizations](https://docs.github.com/en/organizations "Organizations")/
  * [Manage organization roles](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles "Manage organization roles")/
  * [Roles in an organization](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization "Roles in an organization")


# Roles in an organization
Organization owners can assign roles to individuals and teams giving them different sets of permissions in the organization.
## In this article
  * [About roles](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#about-roles)
  * [About pre-defined organization roles](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#about-pre-defined-organization-roles)
  * [About organization roles](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#about-organization-roles)
  * [Permissions for organization roles](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#permissions-for-organization-roles)
  * [Further reading](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#further-reading)


## [About roles](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#about-roles)
To perform any actions on GitHub, such as creating a pull request in a repository or changing an organization's billing settings, a person must have sufficient access to the relevant account or resource. This access is controlled by permissions. A permission is the ability to perform a specific action. For example, the ability to delete an issue is a permission. A role is a set of permissions you can assign to individuals or teams.
Repository-level roles give organization members, outside collaborators and teams of people varying levels of access to repositories. For more information, see [Repository roles for an organization](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization).
Team-level roles are roles that give permissions to manage a team. You can give any individual member of a team the team maintainer role, which gives the member a number of administrative permissions over a team. For more information, see [Assigning the team maintainer role to a team member](https://docs.github.com/en/organizations/organizing-members-into-teams/assigning-the-team-maintainer-role-to-a-team-member).
Organization-level roles are sets of permissions that can be assigned to individuals or teams to manage an organization and the organization's repositories, teams, and settings. For more information about all the roles available at the organization level, see [About organization roles](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#about-organization-roles).
## [About pre-defined organization roles](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#about-pre-defined-organization-roles)
Pre-defined organization roles are roles that are available by default in every organization. You don't need to create them yourself. They can include both organization permissions that let the recipient manage the organization, as well as repository permissions that apply to all of the repositories in the organization. The following pre-defined roles are built into every organization based on common patterns of permissions organizations usually need.
The current set of pre-defined roles are:
  * **All-repository read:** Grants read access to all repositories in the organization.
  * **All-repository write:** Grants write access to all repositories in the organization.
  * **All-repository triage:** Grants triage access to all repositories in the organization.
  * **All-repository maintain:** Grants maintenance access to all repositories in the organization.
  * **All-repository admin:** Grants admin access to all repositories in the organization.
  * **CI/CD admin:** Grants admin access to manage Actions policies, runners, runner groups, hosted compute network configurations, secrets, variables, and usage metrics for an organization.
  * **Security manager** : Grants the ability to manage security policies, security alerts, and security configurations for an organization and all its repositories.


For more information, see [Using organization roles](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/using-organization-roles).
## [About organization roles](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#about-organization-roles)
You can assign people to a variety of organization-level roles to control your members' access to your organization and its resources. For more details about the individual permissions included in each role, see [Permissions for organization roles](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#permissions-for-organization-roles).
### [Organization owners](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#organization-owners)
Organization owners have complete administrative access to your organization. This role should be limited, but to no less than two people, in your organization. For more information, see [Maintaining ownership continuity for your organization](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/maintaining-ownership-continuity-for-your-organization).
### [Organization members](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#organization-members)
The default, non-administrative role for people in an organization is the organization member. By default, organization members have a number of permissions, including the ability to create repositories and projects.
### [Organization moderators](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#organization-moderators)
Moderators are organization members who, in addition to their permissions as members, are allowed to block and unblock non-member contributors, set interaction limits, and hide comments in public repositories owned by the organization. For more information, see [Managing moderators in your organization](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-moderators-in-your-organization).
### [Billing managers](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#billing-managers)
Billing managers are users who can manage the billing settings for your organization, such as payment information. This is a useful option if members of your organization don't usually have access to billing resources. For more information, see [Adding a billing manager to your organization](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/adding-a-billing-manager-to-your-organization).
### [Security managers](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#security-managers)
The security manager role is an organization-level role that organization owners can assign to any member or team in the organization. When applied, it gives permission to view security alerts and manage settings for security features across your organization, as well as read permission for all repositories in the organization.
If your organization has a security team, you can use the security manager role to give members of the team the least access they need to the organization. For more information, see [Managing security managers in your organization](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization).
### [GitHub App managers](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#github-app-managers)
By default, only organization owners can manage the settings of GitHub App registrations owned by an organization. To allow additional users to manage GitHub App registrations owned by an organization, an owner can grant them GitHub App manager permissions.
When you designate a user as a GitHub App manager in your organization, you can grant them access to manage the settings of some or all GitHub App registrations owned by the organization. The GitHub App manager role does not grant users access to install and uninstall GitHub Apps on an organization. For more information, see [Adding and removing GitHub App managers in your organization](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/adding-and-removing-github-app-managers-in-your-organization).
### [Outside collaborators](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#outside-collaborators)
To keep your organization's data secure while allowing access to repositories, you can add outside collaborators. An outside collaborator is a person who has access to one or more organization repositories but is not explicitly a member of the organization, such as a consultant or temporary employee.
#### [Managing outside collaborators](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#managing-outside-collaborators)
To manage access to repositories for outside collaborators, see:
  * [Adding outside collaborators to repositories in your organization](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/adding-outside-collaborators-to-repositories-in-your-organization)
  * [Converting an organization member to an outside collaborator](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/converting-an-organization-member-to-an-outside-collaborator)
  * [Removing an outside collaborator from an organization repository](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/removing-an-outside-collaborator-from-an-organization-repository)


## [Permissions for organization roles](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#permissions-for-organization-roles)
Some of the features listed below are limited to organizations using GitHub Enterprise Cloud. For more information about how you can try GitHub Enterprise Cloud for free, see [Setting up a trial of GitHub Enterprise Cloud](https://docs.github.com/en/enterprise-cloud@latest/admin/overview/setting-up-a-trial-of-github-enterprise-cloud).
Organization permission | Owners | Members | Moderators | Billing managers | Security managers  
---|---|---|---|---|---  
Create repositories (see [Restricting repository creation in your organization](https://docs.github.com/en/organizations/managing-organization-settings/restricting-repository-creation-in-your-organization)) |  |  |  |  |   
View and edit billing information |  |  |  |  |   
Invite people to join the organization |  |  |  |  |   
Edit and cancel invitations to join the organization |  |  |  |  |   
Remove members from the organization |  |  |  |  |   
Reinstate former members to the organization |  |  |  |  |   
Add and remove people from **all teams** |  |  |  |  |   
Promote organization members to _team maintainer_ |  |  |  |  |   
Configure code review assignments (see [Managing code review settings for your team](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-code-review-settings-for-your-team)) |  |  |  |  |   
Set scheduled reminders (see [Managing scheduled reminders for your team](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-scheduled-reminders-for-your-team)) |  |  |  |  |   
Add collaborators to **all repositories** |  |  |  |  |   
Access the organization audit log |  |  |  |  |   
Edit the organization's profile page (see [About your organization's profile](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/about-your-organizations-profile)) |  |  |  |  |   
Delete **all teams** |  |  |  |  |   
Delete the organization account, including all repositories |  |  |  |  |   
Create teams (see [Setting team creation permissions in your organization](https://docs.github.com/en/organizations/managing-organization-settings/setting-team-creation-permissions-in-your-organization)) |  |  |  |  |   
[Move teams in an organization's hierarchy](https://docs.github.com/en/organizations/organizing-members-into-teams/moving-a-team-in-your-organizations-hierarchy) |  |  |  |  |   
See all organization members and teams |  |  |  |  |   
@mention any visible team |  |  |  |  |   
Can be made a _team maintainer_ |  |  |  |  |   
Hide comments on writable commits, pull requests, and issues (see [Managing disruptive comments](https://docs.github.com/en/communities/moderating-comments-and-conversations/managing-disruptive-comments#hiding-a-comment)) |  |  |  |  |   
Hide comments on _all_ commits, pull requests, and issues (see [Managing disruptive comments](https://docs.github.com/en/communities/moderating-comments-and-conversations/managing-disruptive-comments#hiding-a-comment)) |  |  |  |  |   
Block and unblock non-member contributors (see [Blocking a user from your organization](https://docs.github.com/en/communities/maintaining-your-safety-on-github/blocking-a-user-from-your-organization)) |  |  |  |  |   
Limit interactions for certain users in public repositories (see [Limiting interactions in your organization](https://docs.github.com/en/communities/moderating-comments-and-conversations/limiting-interactions-in-your-organization)) |  |  |  |  |   
Set a team profile picture in **all teams** (see [Setting your team's profile picture](https://docs.github.com/en/organizations/organizing-members-into-teams/setting-your-teams-profile-picture)) |  |  |  |  |   
Sponsor accounts and manage the organization's sponsorships (see [Sponsoring open source contributors](https://docs.github.com/en/sponsors/sponsoring-open-source-contributors)) |  |  |  |  |   
Manage email updates from sponsored accounts (see [Managing updates from accounts your organization sponsors](https://docs.github.com/en/organizations/managing-organization-settings/managing-updates-from-accounts-your-organization-sponsors)) |  |  |  |  |   
Attribute your sponsorships to another organization (see [Attributing sponsorships to your organization](https://docs.github.com/en/sponsors/sponsoring-open-source-contributors/attributing-sponsorships-to-your-organization) for details ) |  |  |  |  |   
Manage the publication of GitHub Pages sites from repositories in the organization (see [Managing the publication of GitHub Pages sites for your organization](https://docs.github.com/en/organizations/managing-organization-settings/managing-the-publication-of-github-pages-sites-for-your-organization)) |  |  |  |  |   
Manage security and analysis settings (see [Managing security and analysis settings for your organization](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-security-and-analysis-settings-for-your-organization)) |  |  |  |  |   
View security overview for the organization (see [About security overview](https://docs.github.com/en/code-security/security-overview/about-security-overview)) |  |  |  |  |   
Transfer repositories |  |  |  |  |   
Purchase, install, manage billing for, and cancel GitHub Marketplace apps |  |  |  |  |   
List apps in GitHub Marketplace |  |  |  |  |   
Receive [Dependabot alerts about insecure dependencies](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts) for all of an organization's repositories |  |  |  |  |   
Manage Dependabot security updates (see [About Dependabot security updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)) |  |  |  |  |   
[Manage the forking policy](https://docs.github.com/en/organizations/managing-organization-settings/managing-the-forking-policy-for-your-organization) |  |  |  |  |   
[Limit activity in public repositories in an organization](https://docs.github.com/en/communities/moderating-comments-and-conversations/limiting-interactions-in-your-organization) |  |  |  |  |   
Pull (read) _all repositories_ in the organization |  |  |  |  |   
Push (write) and clone (copy) _all repositories_ in the organization |  |  |  |  |   
Convert organization members to [outside collaborators](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#outside-collaborators) |  |  |  |  |   
[View people with access to an organization repository](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/viewing-people-with-access-to-your-repository) |  |  |  |  |   
Manage the default branch name (see [Managing the default branch name for repositories in your organization](https://docs.github.com/en/organizations/managing-organization-settings/managing-the-default-branch-name-for-repositories-in-your-organization)) |  |  |  |  |   
Manage default labels (see [Managing default labels for repositories in your organization](https://docs.github.com/en/organizations/managing-organization-settings/managing-default-labels-for-repositories-in-your-organization)) |  |  |  |  |   
Manage pull request reviews in the organization (see [Managing pull request reviews in your organization](https://docs.github.com/en/organizations/managing-organization-settings/managing-pull-request-reviews-in-your-organization)) |  |  |  |  |   
Review and manage secret scanning bypass requests (see [Delegated bypass for push protection](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection)) |  |  |  |  |   
Review and manage secret scanning dismissal requests |  |  |  |  |   
Review and manage code scanning dismissal requests |  |  |  |  |   
## [Further reading](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#further-reading)
  * [Repository roles for an organization](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization)


