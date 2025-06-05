  * [Organizations](https://docs.github.com/en/organizations "Organizations")/
  * [Manage repository access](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories "Manage repository access")/
  * [Manage repository roles](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles "Manage repository roles")/
  * [Manage team access](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/managing-team-access-to-an-organization-repository "Manage team access")


# Managing team access to an organization repository
You can give a team access to a repository, remove a team's access to a repository, or change a team's permission level for a repository.
## In this article
  * [Giving a team access to a repository](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/managing-team-access-to-an-organization-repository#giving-a-team-access-to-a-repository)
  * [Removing a team's access to a repository](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/managing-team-access-to-an-organization-repository#removing-a-teams-access-to-a-repository)
  * [Further reading](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/managing-team-access-to-an-organization-repository#further-reading)


People with admin access to a repository can manage team access to the repository. Team maintainers can remove a team's access to a repository if the team has direct access to it. If the team's access to the repository is inherited from a parent team, maintainers can choose to reset the current permission to match the parent team's permission.
  * You can change a team's permission level if the team has direct access to a repository. If the team's access to the repository is inherited from a parent team, you must change the parent team's access to the repository.
  * If you add or remove repository access for a parent team, each of that parent's child teams will also receive or lose access to the repository. For more information, see [About teams](https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams).


## [Giving a team access to a repository](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/managing-team-access-to-an-organization-repository#giving-a-team-access-to-a-repository)
You can give a team access to a repository or change a team's level of access to a repository in your repository settings. For more information, see [Managing teams and people with access to your repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-teams-and-people-with-access-to-your-repository#inviting-a-team-or-person).
## [Removing a team's access to a repository](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/managing-team-access-to-an-organization-repository#removing-a-teams-access-to-a-repository)
You can remove a team's access to an organization repository in your repository settings. For more information, see [Managing teams and people with access to your repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-teams-and-people-with-access-to-your-repository#removing-access-for-a-team-or-person).
If a team has direct access to a repository, you can remove that team's access to the repository. If a team's access to the repository is inherited from a parent team, you must remove the repository from the parent team in order to remove the repository from child teams.
  * If you remove a person’s access to a private repository, any of their forks of that private repository are deleted. Local clones of the private repository are retained. If a team's access to a private repository is revoked or a team with access to a private repository is deleted, and team members do not have access to the repository through another team, private forks of the repository will be deleted.
  * You are responsible for ensuring that people who have lost access to a repository delete any confidential information or intellectual property.
  * People with admin permissions to a private repository can disallow forking of that repository, and organization owners can disallow forking of any private repository in an organization. For more information, see [Managing the forking policy for your organization](https://docs.github.com/en/organizations/managing-organization-settings/managing-the-forking-policy-for-your-organization) and [Managing the forking policy for your repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-the-forking-policy-for-your-repository).


## [Further reading](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/managing-team-access-to-an-organization-repository#further-reading)
  * [Repository roles for an organization](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization)


