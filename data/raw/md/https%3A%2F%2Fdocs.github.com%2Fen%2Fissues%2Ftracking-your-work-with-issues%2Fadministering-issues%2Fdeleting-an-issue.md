  * [GitHub Issues](https://docs.github.com/en/issues "GitHub Issues")/
  * [Issues](https://docs.github.com/en/issues/tracking-your-work-with-issues "Issues")/
  * [Administering issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues "Administering issues")/
  * [Deleting an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues/deleting-an-issue "Deleting an issue")


# Deleting an issue
People with admin permissions in a repository can permanently delete an issue from a repository.
The ability to delete issues depends on whether the repository is owned by a personal account or an organization:
  * The only account that can delete issues in a repository owned by a personal account is that account.
  * Only accounts with admin or owner permissions can delete issues in a repository owned by an organization.
To delete an issue in a repository owned by an organization, an organization owner must enable deleting issues for the organization's repositories. For more information, see [Allowing people to delete issues in your organization](https://docs.github.com/en/organizations/managing-organization-settings/allowing-people-to-delete-issues-in-your-organization) and [Repository roles for an organization](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization).


Collaborators do not receive a notification when issues are deleted. When visiting the URL of a deleted issue, collaborators will see a message stating that the web page can't be found (but they can use the API to determine that it was deleted). People with admin or owner permissions in the repository will additionally see the username of the person who deleted the issue and when it was deleted.
  1. Navigate to the issue you want to delete.
  2. On the right side bar, under "Notifications", click 
![Screenshot of the issue sidebar. A trash can icon and "Delete issue" are outlined in dark orange.](https://docs.github.com/assets/cb-32984/images/help/issues/delete-issue.png)
  3. To confirm deletion, click **Delete this issue**.


## [Further reading](https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues/deleting-an-issue#further-reading)
  * [Linking a pull request to an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue)


