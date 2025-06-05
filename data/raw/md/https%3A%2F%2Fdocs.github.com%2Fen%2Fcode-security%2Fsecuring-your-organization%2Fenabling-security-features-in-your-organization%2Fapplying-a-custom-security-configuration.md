  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secure your organization](https://docs.github.com/en/code-security/securing-your-organization "Secure your organization")/
  * [Enable security features](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization "Enable security features")/
  * [Apply custom configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/applying-a-custom-security-configuration "Apply custom configuration")


# Applying a custom security configuration
You can apply your custom security configuration to repositories in your organization to meet the specific security needs of those repositories.
## Who can use this feature?
Organization owners, security managers, and organization members with the **admin** role
## In this article
  * [About applying a custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/applying-a-custom-security-configuration#about-applying-a-custom-security-configuration)
  * [Applying your custom security configuration to repositories in your organization](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/applying-a-custom-security-configuration#applying-your-custom-security-configuration-to-repositories-in-your-organization)
  * [Next steps](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/applying-a-custom-security-configuration#next-steps)


## [About applying a custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/applying-a-custom-security-configuration#about-applying-a-custom-security-configuration)
After you create a custom security configuration, you need to apply it to repositories in your organization to enable the configuration's settings on those repositories. To learn how to create a custom security configuration, see [Creating a custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/creating-a-custom-security-configuration).
## [Applying your custom security configuration to repositories in your organization](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/applying-a-custom-security-configuration#applying-your-custom-security-configuration-to-repositories-in-your-organization)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Under your organization name, click **Settings**.
![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](https://docs.github.com/assets/cb-49309/images/help/discussions/org-settings-global-nav-update.png)
  3. In the "Security" section of the sidebar, select the **Configurations**.
  4. Optionally, in the "Apply configurations" section, filter for specific repositories you would like to apply your custom security configuration to. To learn how to filter the repository table, see [Filtering repositories in your organization using the repository table](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/filtering-repositories-in-your-organization-using-the-repository-table).
  5. In the repository table, select repositories with one of three methods:
     * Select each repository you would like to apply the security configuration to.
     * To select all repositories displayed on the current page of the repository table, select the checkbox associated with "NUMBER repositories".
     * After selecting the current page of repositories, "25 of NUMBER selected", to select _all_ repositories in your organization that match any filters you have applied, click **Select all**.
  6. Select the **Apply configuration** **YOUR-CONFIGURATION-NAME**.
The default security configuration for an organization is only automatically applied to new repositories created in your organization. If a repository is transferred into your organization, you will still need to apply an appropriate security configuration to the repository manually.
  7. Review the detailed information about how your changes will affect GitHub Secret Protection, GitHub Code Security, or GitHub Advanced Security license consumption. To apply the security configuration, click **Apply**.


The security configuration is applied to both active and archived repositories because some security features run on archived repositories, for example, secret scanning. In addition, if a repository is later unarchived you can be confident that it is protected by the chosen security configuration.
If you apply an enforced configuration, this information is reported in the list of repositories. An enforced configuration means that repository owners are blocked from changing features that have been enabled or disabled in the configuration, but features that are not set aren't enforced.
## [Next steps](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/applying-a-custom-security-configuration#next-steps)
To learn how to interpret security findings from your custom security configuration on a repository, see [Interpreting security findings](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/interpreting-security-findings).
To learn how to edit your custom security configuration, see [Editing a custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/editing-a-custom-security-configuration).
You may encounter an error when you attempt to apply a security configuration. For more information, see [Finding and fixing configuration attachment failures](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/finding-repositories-with-attachment-failures) and [Troubleshooting security configurations](https://docs.github.com/en/code-security/securing-your-organization/troubleshooting-security-configurations).
