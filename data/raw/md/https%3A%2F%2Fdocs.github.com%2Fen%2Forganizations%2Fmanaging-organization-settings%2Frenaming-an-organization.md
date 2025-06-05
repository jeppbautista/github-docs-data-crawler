  * [Organizations](https://docs.github.com/en/organizations "Organizations")/
  * [Manage organization settings](https://docs.github.com/en/organizations/managing-organization-settings "Manage organization settings")/
  * [Renaming an organization](https://docs.github.com/en/organizations/managing-organization-settings/renaming-an-organization "Renaming an organization")


# Renaming an organization
If your project or company has changed names, you can update the name of your organization to match.
## In this article
  * [What happens when I change my organization's name?](https://docs.github.com/en/organizations/managing-organization-settings/renaming-an-organization#what-happens-when-i-change-my-organizations-name)
  * [Changing your organization's name](https://docs.github.com/en/organizations/managing-organization-settings/renaming-an-organization#changing-your-organizations-name)
  * [Further reading](https://docs.github.com/en/organizations/managing-organization-settings/renaming-an-organization#further-reading)


Only organization owners can rename an organization. For more information, see [Roles in an organization](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization).
## [What happens when I change my organization's name?](https://docs.github.com/en/organizations/managing-organization-settings/renaming-an-organization#what-happens-when-i-change-my-organizations-name)
After changing your organization's name, your old organization name becomes available for someone else to claim. When you change your organization's name, most references to your repositories under the old organization name automatically change to the new name. However, some links to your profile won't automatically redirect.
### [Changes that occur automatically](https://docs.github.com/en/organizations/managing-organization-settings/renaming-an-organization#changes-that-occur-automatically)
  * GitHub automatically redirects references to your repositories. Web links to your organization's existing **repositories** will continue to work. This can take a few minutes to complete after you initiate the change.
  * You can continue pushing your local repositories to the old remote tracking URL without updating it. However, we recommend you update all existing remote repository URLs after changing your organization name. Because your old organization name is available for use by anyone else after you change it, the new organization owner can create repositories that override the redirect entries to your repository. For more information, see [Managing remote repositories](https://docs.github.com/en/get-started/git-basics/managing-remote-repositories).
  * Previous Git commits will also be correctly attributed to users within your organization.
  * If the account namespace includes any public repositories that contain an action listed on GitHub Marketplace, or that had more than 100 clones or more than 100 uses of GitHub Actions in the week prior to you renaming your account, GitHub permanently retires the old owner name and repository name combination (`OLD-OWNER/REPOSITORY-NAME`) when you rename your account.
  * If the account namespace includes any packages or container images stored in a GitHub Packages registry, GitHub transfers the packages and container images to the new namespace. By renaming your account, you may break projects that depend on these packages. If the namespace includes any container images that are public and have more than 5,000 downloads, the full former name of these container images (`OLD-NAMESPACE/IMAGE-NAME`) is permanently retired when you rename the account to ensure the container image name cannot be reused in the future.


### [Changes that aren't automatic](https://docs.github.com/en/organizations/managing-organization-settings/renaming-an-organization#changes-that-arent-automatic)
After changing your organization's name:
  * Links to your previous organization profile page, such as `https://github.com/previousorgname`, will return a 404 error. We recommend you update links to your organization from other sites, such as your LinkedIn or Twitter profiles.
  * API requests that use the old organization's name will return a 404 error. We recommend you update the old organization name in your API requests.
  * There are no automatic [@mention](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#mentioning-people-and-teams) redirects for teams that use the old organization's name.


## [Changing your organization's name](https://docs.github.com/en/organizations/managing-organization-settings/renaming-an-organization#changing-your-organizations-name)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. Near the bottom of the settings page, under "Danger zone", click **Rename organization**.
  4. Read the warning messages, then, if you want to go ahead, click **I understand, let's rename my organization**.
  5. Type a new name for your organization, then click **Change organization's name**.


## [Further reading](https://docs.github.com/en/organizations/managing-organization-settings/renaming-an-organization#further-reading)
  * [Why are my commits linked to the wrong user?](https://docs.github.com/en/pull-requests/committing-changes-to-your-project/troubleshooting-commits/why-are-my-commits-linked-to-the-wrong-user)


