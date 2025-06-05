  * [Organizations](https://docs.github.com/en/organizations "Organizations")/
  * [Manage organization settings](https://docs.github.com/en/organizations/managing-organization-settings "Manage organization settings")/
  * [Set visibility changes policy](https://docs.github.com/en/organizations/managing-organization-settings/restricting-repository-visibility-changes-in-your-organization "Set visibility changes policy")


# Restricting repository visibility changes in your organization
To protect your organization's data, you can configure permissions for changing repository visibility in your organization.
## Who can use this feature?
Organization owners can restrict repository visibility changes for an organization.
You can restrict who has the ability to change the visibility of repositories in your organization, such as changing a repository from private to public. For more information about repository visibility, see [About repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories#about-repository-visibility).
Restricting who has the ability to change the visibility of repositories in your organization helps prevent sensitive information from being exposed. For more information, see [Best practices for preventing data leaks in your organization](https://docs.github.com/en/code-security/getting-started/best-practices-for-preventing-data-leaks-in-your-organization).
You can restrict the ability to change repository visibility to organization owners only, or you can allow anyone with admin access to a repository to change visibility.
If this setting is enabled, individuals or GitHub Apps with admin access can _modify_ the visibility of an existing repository even if the ability to _create_ a repository with that specific visibility has been disabled. For more information about restricting the visibility of repositories during creation, see [Restricting repository creation in your organization](https://docs.github.com/en/organizations/managing-organization-settings/restricting-repository-creation-in-your-organization).
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the "Access" section of the sidebar, click 
  4. Under "Repository visibility change", deselect **Allow members to change repository visibilities for this organization**.
  5. Click **Save**.


