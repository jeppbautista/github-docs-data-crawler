  * [GitHub Issues](https://docs.github.com/en/issues "GitHub Issues")/
  * [Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects "Projects")/
  * [Managing your project](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project "Managing your project")/
  * [Managing project access](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/managing-access-to-your-projects "Managing project access")


# Managing access to your projects
Learn how to manage team and individual access to your project.
## In this article
  * [About project access](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/managing-access-to-your-projects#about-project-access)
  * [Managing access for organization-level projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/managing-access-to-your-projects#managing-access-for-organization-level-projects)
  * [Managing access for user-level projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/managing-access-to-your-projects#managing-access-for-user-level-projects)


## [About project access](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/managing-access-to-your-projects#about-project-access)
Admins of organization-level projects can manage access for the entire organization, for teams, for individual organization members, and for outside collaborators.
Admins of user-level projects can invite individual collaborators and manage their access.
Project admins can also control the visibility of their project for everyone on the internet. For more information, see [Managing visibility of your projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/managing-visibility-of-your-projects).
## [Managing access for organization-level projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/managing-access-to-your-projects#managing-access-for-organization-level-projects)
You can control access to your project by setting permissions for particular individuals and teams or you can set a base permission that applies to everyone in your organization.
### [Managing access for everyone in your organization](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/managing-access-to-your-projects#managing-access-for-everyone-in-your-organization)
You can manage access for everyone in your organization to a particular project by changing the project's base permission. Changes to the base permission only affect organization members who are not organization owners and who are not granted individual access.
You can also configure the default base permission at the organization-level for new projects and projects that haven't yet had a base permission configured. For more information about setting your organization's base permission for projects, see [Managing base permissions for projects](https://docs.github.com/en/organizations/managing-organization-settings/managing-base-permissions-for-projects).
  1. Navigate to your project.
  2. In the top-right, click 
![Screenshot showing a project's menu bar. The menu icon is highlighted with an orange outline.](https://docs.github.com/assets/cb-789/images/help/projects-v2/open-menu.png)
  3. In the menu, click 
  4. Click **Manage access**.
  5. Under **Base role** , select the default role.
![Screenshot showing the "Who has access" settings. The dropdown for setting the base role is highlighted with an orange outline.](https://docs.github.com/assets/cb-29323/images/help/projects-v2/base-role.png)
     * **No access:** Only organization owners and users granted individual access can see the project. Organization owners are also admins for the project.
     * **Read:** Everyone in the organization can see the project. Organization owners are also admins for the project.
     * **Write:** Everyone in the organization can see and edit the project. Organization owners are also admins for the project.
     * **Admin:** Everyone in the organization is an admin for the project.


### [Managing access for teams and individual members of your organization](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/managing-access-to-your-projects#managing-access-for-teams-and-individual-members-of-your-organization)
You can also add teams, external collaborators, and individual organization members as collaborators for an organization-level project. For more information, see [About teams](https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams).
If you grant a team read permissions or greater for a project, the project is also displayed on the team's projects page. You can also add projects to a team on the team's projects page. For more information, see [Adding your project to a team](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/adding-your-project-to-a-team).
You can only invite an individual user to collaborate on your organization-level project if they are already a member of the organization or an outside collaborator on at least one repository in the organization.
  1. Navigate to your project.
  2. In the top-right, click 
![Screenshot showing a project's menu bar. The menu icon is highlighted with an orange outline.](https://docs.github.com/assets/cb-789/images/help/projects-v2/open-menu.png)
  3. In the menu, click 
  4. Click **Manage access**.
  5. Under **Invite collaborators** , search for the team or individual user that you want to invite.
![Screenshot showing searching for a collaborator.](https://docs.github.com/assets/cb-23608/images/help/projects-v2/access-search.png)
  6. Select the role for the collaborator.
     * **Read:** The team or individual can view the project.
     * **Write:** The team or individual can view and edit the project.
     * **Admin:** The team or individual can view, edit, and add new collaborators to the project.
  7. Click **Invite**.


### [Managing access of an existing collaborator on your project](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/managing-access-to-your-projects#managing-access-of-an-existing-collaborator-on-your-project)
  1. Navigate to your project.
  2. In the top-right, click 
![Screenshot showing a project's menu bar. The menu icon is highlighted with an orange outline.](https://docs.github.com/assets/cb-789/images/help/projects-v2/open-menu.png)
  3. In the menu, click 
  4. Click **Manage access**.
  5. Under **Manage access** , find the collaborator(s) whose permissions you want to modify.
You can use the **Type** and **Role** drop-down menus to filter the access list.
![Screenshot of the "Manage access" section. The octocat is listed as a collaborator.](https://docs.github.com/assets/cb-28165/images/help/projects-v2/access-find-member.png)
  6. Edit the role for the collaborator(s).
  7. Optionally, click **Remove** to remove the collaborator(s).


## [Managing access for user-level projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/managing-access-to-your-projects#managing-access-for-user-level-projects)
### [Granting a collaborator access to your project](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/managing-access-to-your-projects#granting-a-collaborator-access-to-your-project)
This only affects collaborators for your project, not for repositories in your project. To view an item on the project, someone must have the required permissions for the repository that the item belongs to. Only people with access to a private repository will be able to view project items from that private repository. For more information, see [Setting repository visibility](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility) and [Managing teams and people with access to your repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-teams-and-people-with-access-to-your-repository).
  1. Navigate to your project.
  2. In the top-right, click 
![Screenshot showing a project's menu bar. The menu icon is highlighted with an orange outline.](https://docs.github.com/assets/cb-789/images/help/projects-v2/open-menu.png)
  3. In the menu, click 
  4. Click **Manage access**.
  5. Under **Invite collaborators** , search for the user that you want to invite.
![Screenshot showing searching for a collaborator.](https://docs.github.com/assets/cb-23608/images/help/projects-v2/access-search.png)
  6. Select the role for the collaborator.
     * **Read:** The individual can view the project.
     * **Write:** The individual can view and edit the project.
     * **Admin:** The individual can view, edit, and add new collaborators to the project.
  7. Click **Invite**.


### [Managing access of an existing collaborator on your project](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/managing-access-to-your-projects#managing-access-of-an-existing-collaborator-on-your-project-1)
  1. Navigate to your project.
  2. In the top-right, click 
![Screenshot showing a project's menu bar. The menu icon is highlighted with an orange outline.](https://docs.github.com/assets/cb-789/images/help/projects-v2/open-menu.png)
  3. In the menu, click 
  4. Click **Manage access**.
  5. Under **Manage access** , find the collaborator(s) whose permissions you want to modify.
You can use the **Type** and **Role** drop-down menus to filter the access list.
![Screenshot of the "Manage access" section. The octocat is listed as a collaborator.](https://docs.github.com/assets/cb-28165/images/help/projects-v2/access-find-member.png)
  6. Edit the role for the collaborator(s).
  7. Optionally, click **Remove** to remove the collaborator(s).


