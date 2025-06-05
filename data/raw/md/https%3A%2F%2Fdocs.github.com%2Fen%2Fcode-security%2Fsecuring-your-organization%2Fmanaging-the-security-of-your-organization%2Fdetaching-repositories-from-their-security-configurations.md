  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secure your organization](https://docs.github.com/en/code-security/securing-your-organization "Secure your organization")/
  * [Manage organization security](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization "Manage organization security")/
  * [Detach security configuration](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/detaching-repositories-from-their-security-configurations "Detach security configuration")


# Detaching repositories from their security configurations
You can unlink repositories from their security configurations and instead manage their security enablement settings at the repository level.
## Who can use this feature?
Organization owners, security managers, and organization members with the **admin** role
## In this article
  * [About detaching repositories from their security configurations](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/detaching-repositories-from-their-security-configurations#about-detaching-repositories-from-their-security-configurations)
  * [Detaching repositories from linked security configurations](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/detaching-repositories-from-their-security-configurations#detaching-repositories-from-linked-security-configurations)


## [About detaching repositories from their security configurations](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/detaching-repositories-from-their-security-configurations#about-detaching-repositories-from-their-security-configurations)
If you decide that the security needs of a repository are too specific for a security configuration to be useful, you can detach that repository from the linked configuration and instead manage security enablement settings at the repository level. Detaching a repository from a security configuration will not change the existing security enablement settings for that repository. For an introduction to securing your repository at the repository level, see [Quickstart for securing your repository](https://docs.github.com/en/code-security/getting-started/securing-your-repository).
Alternatively, if you want to apply a security configuration to a repository that's already attached to a different configuration, you can apply the configuration as normal, and you do not need to detach the current configuration. For more information, see [Applying the GitHub-recommended security configuration in your organization](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/applying-the-github-recommended-security-configuration-in-your-organization) and [Applying a custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/applying-a-custom-security-configuration).
## [Detaching repositories from linked security configurations](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/detaching-repositories-from-their-security-configurations#detaching-repositories-from-linked-security-configurations)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Under your organization name, click **Settings**.
![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](https://docs.github.com/assets/cb-49309/images/help/discussions/org-settings-global-nav-update.png)
  3. In the "Security" section of the sidebar, select the **Configurations**.
  4. Optionally, in the "Apply configurations" section, filter for specific repositories you would like to detach from their configurations. To learn more, see [Filtering repositories in your organization using the repository table](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/filtering-repositories-in-your-organization-using-the-repository-table).
  5. In the repository table, select repositories with one of three methods:
     * Select each repository you would like to apply the security configuration to.
     * To select all repositories displayed on the current page of the repository table, select the checkbox associated with "NUMBER repositories".
     * After selecting the current page of repositories, "25 of NUMBER selected", to select _all_ repositories in your organization that match any filters you have applied, click **Select all**.
  6. Select the **Apply configuration** **No configuration**.
  7. To finish detaching your repositories from their linked security configurations, in the "No configuration?" window, click **No configuration**.


