  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secure your organization](https://docs.github.com/en/code-security/securing-your-organization "Secure your organization")/
  * [Manage organization security](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization "Manage organization security")/
  * [Delete custom configuration](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/deleting-a-custom-security-configuration "Delete custom configuration")


# Deleting a custom security configuration
You can delete unnecessary custom security configurations in your organization.
## Who can use this feature?
Organization owners, security managers, and organization members with the **admin** role
## In this article
  * [About deleting a custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/deleting-a-custom-security-configuration#about-deleting-a-custom-security-configuration)
  * [Deleting a custom security configuration from your organization](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/deleting-a-custom-security-configuration#deleting-a-custom-security-configuration-from-your-organization)


## [About deleting a custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/deleting-a-custom-security-configuration#about-deleting-a-custom-security-configuration)
If you no longer need a custom security configuration, you can delete that configuration to ensure it will not be applied to any repositories in the future. If you are deleting a custom security configuration because you want to change the security enablement settings in that configuration, you can instead edit the configuration. For more information, see [Editing a custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/editing-a-custom-security-configuration).
Deleting a custom security configuration will detach all repositories that are linked to that configuration. The existing security settings for those repositories will be unchanged, but you must apply a different security configuration or manage their security settings at the repository level to keep their settings up to date.
## [Deleting a custom security configuration from your organization](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/deleting-a-custom-security-configuration#deleting-a-custom-security-configuration-from-your-organization)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Under your organization name, click **Settings**.
![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](https://docs.github.com/assets/cb-49309/images/help/discussions/org-settings-global-nav-update.png)
  3. In the "Security" section of the sidebar, select the **Configurations**.
  4. In the configurations table, click the name of the custom security configuration you want to delete.
  5. Scroll to the bottom of the page, then click **Delete configuration**.
  6. In the "Delete this configuration?" window, read the warning to confirm you are comfortable deleting the custom security configuration, then click **Delete configuration**.


