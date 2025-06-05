  * [Organizations](https://docs.github.com/en/organizations "Organizations")/
  * [Manage organization settings](https://docs.github.com/en/organizations/managing-organization-settings "Manage organization settings")/
  * [Custom properties](https://docs.github.com/en/organizations/managing-organization-settings/managing-custom-properties-for-repositories-in-your-organization "Custom properties")


# Managing custom properties for repositories in your organization
With custom properties, you can add metadata to repositories in your organization. You can use those properties to target repositories with rulesets.
## Who can use this feature?
Organization owners can add and set a custom property schema at the organization level.
## In this article
  * [About custom properties](https://docs.github.com/en/organizations/managing-organization-settings/managing-custom-properties-for-repositories-in-your-organization#about-custom-properties)
  * [Allowed characters](https://docs.github.com/en/organizations/managing-organization-settings/managing-custom-properties-for-repositories-in-your-organization#allowed-characters)
  * [Adding custom properties](https://docs.github.com/en/organizations/managing-organization-settings/managing-custom-properties-for-repositories-in-your-organization#adding-custom-properties)
  * [Setting values for repositories in your organization](https://docs.github.com/en/organizations/managing-organization-settings/managing-custom-properties-for-repositories-in-your-organization#setting-values-for-repositories-in-your-organization)
  * [Viewing values for repositories in your organization](https://docs.github.com/en/organizations/managing-organization-settings/managing-custom-properties-for-repositories-in-your-organization#viewing-values-for-repositories-in-your-organization)
  * [Searching and filtering repositories by custom properties values](https://docs.github.com/en/organizations/managing-organization-settings/managing-custom-properties-for-repositories-in-your-organization#searching-and-filtering-repositories-by-custom-properties-values)


## [About custom properties](https://docs.github.com/en/organizations/managing-organization-settings/managing-custom-properties-for-repositories-in-your-organization#about-custom-properties)
Custom properties allow you to decorate your repositories with information such as compliance frameworks, data sensitivity, or project details. Custom properties visibility follows the visibility of the repository. Custom properties on public repositories can be viewed by anyone, while custom properties on internal or private repositories can be viewed by accounts with read permissions to the repository. An organization can have up to 100 property definitions. An allowed value list can have up to 200 items.
## [Allowed characters](https://docs.github.com/en/organizations/managing-organization-settings/managing-custom-properties-for-repositories-in-your-organization#allowed-characters)
Custom property names and values may only contain certain characters:
  * Names: `a-z`, `A-Z`, `0-9`, `_`, `-`, `$`, `#`.
  * Values: All printable ASCII characters except `"`.


## [Adding custom properties](https://docs.github.com/en/organizations/managing-organization-settings/managing-custom-properties-for-repositories-in-your-organization#adding-custom-properties)
You can add custom properties to your organization and set values for those properties for repositories in your organization.
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the left sidebar, in the "Code, planning, and automation" section, click **Custom properties**.
![Screenshot of an organization's settings page. In the sidebar, a link labeled "Custom properties" is outlined in orange.](https://docs.github.com/assets/cb-40889/images/help/organizations/custom-properties.png)
  4. To add a new custom property, click **New property** in the upper right corner.
  5. In the "Name" field, type the name you'd like to use for your custom property. The name can't contain spaces, and cannot exceed 75 characters in length.
  6. Optionally, in the "Description" field, fill in a description of your custom property.
  7. Under "Type", select the type of property you'd like to add. This can either be a text string, a single select field, a multi select field, or a true/false boolean.
  8. Optionally, you can select **Allow repository actors to set this property**. When enabled, repository users and apps with the repository-level "custom properties" fine-grained permission will be able to set and update the property value for their repository.
  9. Optionally, you can select **Require this property for all repositories** and add a default value. This means that you require that all repositories in your organization have a value for this property. Repositories that don’t have an explicit value for this property will inherit the default value.
  10. Click **Save property**.


## [Setting values for repositories in your organization](https://docs.github.com/en/organizations/managing-organization-settings/managing-custom-properties-for-repositories-in-your-organization#setting-values-for-repositories-in-your-organization)
You can set values for custom properties for repositories in your organization.
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the left sidebar, in the "Code, planning, and automation" section, click **Custom properties**.
![Screenshot of an organization's settings page. In the sidebar, a link labeled "Custom properties" is outlined in orange.](https://docs.github.com/assets/cb-40889/images/help/organizations/custom-properties.png)
  4. Click the "Set values" tab.
  5. Select one or more repositories from the list and click 
![Screenshot the page to set values for repositories. A button, labeled with a pencil icon and "Edit properties", is highlighted with an orange outline.](https://docs.github.com/assets/cb-13183/images/help/repository/edit-properties.png)
  6. In the modal dialog that appears, select a value for each property you'd like to set for the selected repositories.
  7. Click **Save changes**.


## [Viewing values for repositories in your organization](https://docs.github.com/en/organizations/managing-organization-settings/managing-custom-properties-for-repositories-in-your-organization#viewing-values-for-repositories-in-your-organization)
People with read permissions to a repository can view the values of custom properties for that repository, but they can't edit those values.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Code and automation" section of the sidebar, click 


## [Searching and filtering repositories by custom properties values](https://docs.github.com/en/organizations/managing-organization-settings/managing-custom-properties-for-repositories-in-your-organization#searching-and-filtering-repositories-by-custom-properties-values)
You can search for repositories in your organization by custom properties values.
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Click the name of your organization.
  3. Under your organization name, click 
  4. In the search bar, type `prop` to see a list of all custom properties in your organization, and select the property you'd like to search by.


