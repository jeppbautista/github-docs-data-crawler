  * [Organizations](https://docs.github.com/en/organizations "Organizations")/
  * [Organize members into teams](https://docs.github.com/en/organizations/organizing-members-into-teams "Organize members into teams")/
  * [Remove members](https://docs.github.com/en/organizations/organizing-members-into-teams/removing-organization-members-from-a-team "Remove members")


# Removing organization members from a team
People with _owner_ or _team maintainer_ permissions can remove team members from a team. This may be necessary if a person no longer needs access to a repository the team grants, or if a person is no longer focused on a team's projects.
Removing a member from a team revokes their access to all repositories and related resources granted through the team. This includes:
  * Removal from assignee fields in issues, pull requests, and project cards.
  * Loss of access to repository-specific tools such as GitHub Discussions, Projects, and Wikis.
  * Inability to contribute to any repositories the team has access to.


If the member is assigned to any ongoing tasks, you should reassign them or grant them individual repository permissions, as required.
  * If you remove a person’s access to a private repository, any of their forks of that private repository are deleted. Local clones of the private repository are retained. If a team's access to a private repository is revoked or a team with access to a private repository is deleted, and team members do not have access to the repository through another team, private forks of the repository will be deleted.
  * You are responsible for ensuring that people who have lost access to a repository delete any confidential information or intellectual property.
  * People with admin permissions to a private repository can disallow forking of that repository, and organization owners can disallow forking of any private repository in an organization. For more information, see [Managing the forking policy for your organization](https://docs.github.com/en/organizations/managing-organization-settings/managing-the-forking-policy-for-your-organization) and [Managing the forking policy for your repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-the-forking-policy-for-your-repository).


  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Click the name of your organization.
  3. Under your organization name, click 
![Screenshot of the horizontal navigation bar for an organization. A tab, labeled with the people icon and "Teams," is outlined in dark orange.](https://docs.github.com/assets/cb-22213/images/help/organizations/organization-teams-tab.png)
  4. Click the name of the team.
  5. Select the person or people you'd like to remove.
![Screenshot of the first user in a list of team members. To the left of the user, a checkbox is checked and outlined in dark orange.](https://docs.github.com/assets/cb-15208/images/help/teams/team-member-check-box.png)
  6. Above the list of team members, use the drop-down menu and click **Remove from team**.
![Screenshot of a team's "Members" page. Above the list of team members, a dropdown menu, labeled "2 members selected", is outlined in dark orange.](https://docs.github.com/assets/cb-27611/images/help/teams/team-member-bulk-management.png)


