  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secure your organization](https://docs.github.com/en/code-security/securing-your-organization "Secure your organization")/
  * [Enable security features](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization "Enable security features")/
  * [Apply recommended configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/applying-the-github-recommended-security-configuration-in-your-organization "Apply recommended configuration")


# Applying the GitHub-recommended security configuration in your organization
Secure your code with the security enablement settings created, managed, and recommended by GitHub.
## Who can use this feature?
Organization owners, security managers, and organization members with the **admin** role
## In this article
  * [About the GitHub-recommended security configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/applying-the-github-recommended-security-configuration-in-your-organization#about-the-github-recommended-security-configuration)
  * [Applying the GitHub-recommended security configuration to all repositories in your organization](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/applying-the-github-recommended-security-configuration-in-your-organization#applying-the-github-recommended-security-configuration-to-all-repositories-in-your-organization)
  * [Applying the GitHub-recommended security configuration to specific repositories in your organization](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/applying-the-github-recommended-security-configuration-in-your-organization#applying-the-github-recommended-security-configuration-to-specific-repositories-in-your-organization)
  * [Enforcing the GitHub-recommended security configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/applying-the-github-recommended-security-configuration-in-your-organization#enforcing-the-github-recommended-security-configuration)
  * [Next steps](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/applying-the-github-recommended-security-configuration-in-your-organization#next-steps)


## [About the GitHub-recommended security configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/applying-the-github-recommended-security-configuration-in-your-organization#about-the-github-recommended-security-configuration)
The GitHub-recommended security configuration is a collection of enablement settings for GitHub's security features that is created and maintained by subject matter experts at GitHub. The GitHub-recommended security configuration is designed to successfully reduce the security risks for low- and high-impact repositories. We recommend you apply this configuration to all the repositories in your organization.
The GitHub-recommended security configuration includes GitHub Code Security and GitHub Secret Protection features. Applying the configuration to repositories in your organization will incur usage costs or require licenses.
## [Applying the GitHub-recommended security configuration to all repositories in your organization](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/applying-the-github-recommended-security-configuration-in-your-organization#applying-the-github-recommended-security-configuration-to-all-repositories-in-your-organization)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Under your organization name, click **Settings**.
![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](https://docs.github.com/assets/cb-49309/images/help/discussions/org-settings-global-nav-update.png)
  3. In the "Security" section of the sidebar, select the **Configurations**.
  4. In the "GitHub recommended" row of the configurations table for your organization, select the **Apply to** **All repositories** or **All repositories without configurations**.
The default security configuration for an organization is only automatically applied to new repositories created in your organization. If a repository is transferred into your organization, you will still need to apply an appropriate security configuration to the repository manually.
  5. Review the detailed information about how your changes will affect GitHub Secret Protection, GitHub Code Security, or GitHub Advanced Security license consumption. To apply the security configuration, click **Apply**.


The security configuration is applied to both active and archived repositories because some security features run on archived repositories, for example, secret scanning. In addition, if a repository is later unarchived you can be confident that it is protected by the chosen security configuration.
## [Applying the GitHub-recommended security configuration to specific repositories in your organization](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/applying-the-github-recommended-security-configuration-in-your-organization#applying-the-github-recommended-security-configuration-to-specific-repositories-in-your-organization)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Under your organization name, click **Settings**.
![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](https://docs.github.com/assets/cb-49309/images/help/discussions/org-settings-global-nav-update.png)
  3. In the "Security" section of the sidebar, select the **Configurations**.
  4. Optionally, in the "Apply configurations" section, filter the view to find the repositories you would like to apply the GitHub-recommended security configuration to. To learn how to filter the repository table, see [Filtering repositories in your organization using the repository table](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/filtering-repositories-in-your-organization-using-the-repository-table).
  5. In the repository table, select repositories with one of three methods:
     * Select each repository you would like to apply the security configuration to.
     * To select all repositories displayed on the current page of the repository table, select the checkbox associated with "NUMBER repositories".
     * After selecting the current page of repositories, "25 of NUMBER selected", to select _all_ repositories in your organization that match any filters you have applied, click **Select all**.
  6. Select the **Apply configuration** **GitHub recommended**.
The default security configuration for an organization is only automatically applied to new repositories created in your organization. If a repository is transferred into your organization, you will still need to apply an appropriate security configuration to the repository manually.
  7. Review the detailed information about how your changes will affect GitHub Secret Protection, GitHub Code Security, or GitHub Advanced Security license consumption. To apply the security configuration, click **Apply**.


The security configuration is applied to both active and archived repositories because some security features run on archived repositories, for example, secret scanning. In addition, if a repository is later unarchived you can be confident that it is protected by the chosen security configuration.
## [Enforcing the GitHub-recommended security configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/applying-the-github-recommended-security-configuration-in-your-organization#enforcing-the-github-recommended-security-configuration)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Under your organization name, click **Settings**.
![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](https://docs.github.com/assets/cb-49309/images/help/discussions/org-settings-global-nav-update.png)
  3. In the "Security" section of the sidebar, select the **Configurations**.
  4. In the "Security configurations" section, select "GitHub recommended".
  5. In the "Policy" section, next to "Enforce configuration", select **Enforce** from the dropdown menu.


If a user in your organization attempts to change the enablement status of a feature in an enforced configuration using the REST API, the API call will appear to succeed, but no enablement statuses will change.
Some situations can break the enforcement of security configurations for a repository. For example, the enablement of code scanning will not apply to a repository if:
  * GitHub Actions is initially enabled on the repository, but is then disabled in the repository.
  * GitHub Actions required by code scanning configurations are not available in the repository.
  * The definition for which languages should not be analyzed using code scanning default setup is changed.


## [Next steps](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/applying-the-github-recommended-security-configuration-in-your-organization#next-steps)
After you apply the GitHub-recommended security configuration, you can customize your organization-level security settings with global settings. See [Configuring global security settings for your organization](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization).
You may encounter an error when you attempt to apply a security configuration. For more information, see [Finding and fixing configuration attachment failures](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/finding-repositories-with-attachment-failures) and [Troubleshooting security configurations](https://docs.github.com/en/code-security/securing-your-organization/troubleshooting-security-configurations).
