  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secure your organization](https://docs.github.com/en/code-security/securing-your-organization "Secure your organization")/
  * [Manage organization security](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization "Manage organization security")/
  * [Edit custom configuration](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/editing-a-custom-security-configuration "Edit custom configuration")


# Editing a custom security configuration
Change the enablement settings in your custom security configuration to better meet the security needs of your repositories.
## Who can use this feature?
Organization owners, security managers, and organization members with the **admin** role
## In this article
  * [About editing a custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/editing-a-custom-security-configuration#about-editing-a-custom-security-configuration)
  * [Modifying your custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/editing-a-custom-security-configuration#modifying-your-custom-security-configuration)


## [About editing a custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/editing-a-custom-security-configuration#about-editing-a-custom-security-configuration)
After creating and applying a custom security configuration, you may need to edit the enablement settings for that configuration to better secure your repositories. Any changes you make to the enablement settings of a security configuration will automatically populate to all linked repositories.
To determine if your custom security configuration is meeting your security needs, see [Interpreting security findings](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/interpreting-security-findings).
The GitHub-recommended security configuration is managed by GitHub and cannot be edited. If you would like to customize your security enablement settings, you need to create a custom security configuration. For more information, see [Creating a custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/creating-a-custom-security-configuration).
## [Modifying your custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/editing-a-custom-security-configuration#modifying-your-custom-security-configuration)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Under your organization name, click **Settings**.
![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](https://docs.github.com/assets/cb-49309/images/help/discussions/org-settings-global-nav-update.png)
  3. In the "Security" section of the sidebar, select the **Configurations**.
  4. Under "Security configurations", click the name of the custom security configuration you want to edit.
The default security configuration for an organization is only automatically applied to new repositories created in your organization. If a repository is transferred into your organization, you will still need to apply an appropriate security configuration to the repository manually.
  5. Edit the name and description of your custom security configuration as desired.
  6. Edit the enablement settings of your custom security configuration as desired.
  7. In the "Policy" section, you can modify the configuration's enforcement status. Enforcing a configuration will block repository owners from changing features that are enabled or disabled by the configuration, but features that are not set aren't enforced. Next to "Enforce configuration", select **Enforce** or **Don't enforce** from the dropdown menu.
If a user in your organization attempts to change the enablement status of a feature in an enforced configuration using the REST API, the API call will appear to succeed, but no enablement statuses will change.
Some situations can break the enforcement of security configurations for a repository. For example, the enablement of code scanning will not apply to a repository if:
     * GitHub Actions is initially enabled on the repository, but is then disabled in the repository.
     * GitHub Actions required by code scanning configurations are not available in the repository.
     * The definition for which languages should not be analyzed using code scanning default setup is changed.
  8. To apply your changes, click **Update configuration**.


