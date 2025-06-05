  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secure your organization](https://docs.github.com/en/code-security/securing-your-organization "Secure your organization")/
  * [Manage organization security](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization "Manage organization security")/
  * [Manage paid GHAS use](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/managing-your-github-advanced-security-license-usage "Manage paid GHAS use")


# Managing your paid use of Advanced Security
You can understand and control the costs of using GitHub Secret Protection and GitHub Code Security in repositories in your organization.
## Who can use this feature?
Organization owners, security managers, and organization members with the **admin** role
Requires GitHub Team or GitHub Enterprise
## In this article
  * [Requirements for enabling Advanced Security products](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/managing-your-github-advanced-security-license-usage#requirements-for-enabling-advanced-security-products)
  * [Understanding your license usage](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/managing-your-github-advanced-security-license-usage#understanding-your-license-usage)
  * [Turning off Secret Protection or Code Security](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/managing-your-github-advanced-security-license-usage#turning-off-secret-protection-or-code-security)


## [Requirements for enabling Advanced Security products](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/managing-your-github-advanced-security-license-usage#requirements-for-enabling-advanced-security-products)
To use GitHub Secret Protection, GitHub Code Security, or GitHub Advanced Security on private or internal repositories with unique active committers, you must have licenses available. The user-interface and options depend on how you pay for Advanced Security.
  * **Metered billing:** by default, there is no limit on how many licenses you can consume. See [Preventing overspending](https://docs.github.com/en/billing/managing-your-billing/preventing-overspending) .
  * **Volume/subscription billing** (GitHub Enterprise only)**:** once the licenses you have purchased are all in use, you cannot enable GitHub Secret Protection, GitHub Code Security, or GitHub Advanced Security on additional repositories until you free up or buy additional licenses.


With security configurations, you can easily understand the license usage of repositories in your organization, as well as the number of available GitHub Secret Protection, GitHub Code Security, or GitHub Advanced Security licenses in your organization. Additionally, if you need to make more licenses available to secure a high-impact repository, you can quickly disable GitHub Secret Protection, GitHub Code Security, or GitHub Advanced Security on private and internal repositories at scale.
To learn about licensing for GitHub Secret Protection, GitHub Code Security, and GitHub Advanced Security, see [About billing for GitHub Advanced Security](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-advanced-security/about-billing-for-github-advanced-security).
## [Understanding your license usage](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/managing-your-github-advanced-security-license-usage#understanding-your-license-usage)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Under your organization name, click **Settings**.
![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](https://docs.github.com/assets/cb-49309/images/help/discussions/org-settings-global-nav-update.png)
  3. In the "Security" section of the sidebar, select the **Configurations**.
  4. In the "Apply configurations" section, your current license usage will be displayed. This screenshot shows metered usage. If you have bought a volume/subscription license, then the number of licenses available is also reported.
![Screenshot of the "Apply configurations" section. The current license use for the enterprise is outlined in dark orange.](https://docs.github.com/assets/cb-20858/images/help/security-configurations/current-sp-cs-license-usage.png)
  5. Optionally, to find specific repositories in your organization, filter the repository table. To learn more, see [Filtering repositories in your organization using the repository table](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/filtering-repositories-in-your-organization-using-the-repository-table).


## [Turning off Secret Protection or Code Security](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/managing-your-github-advanced-security-license-usage#turning-off-secret-protection-or-code-security)
The simplest way to turn off all Secret Protection or Code Security features for one or more repositories is to create a security configuration where the product is disabled at the top level. You can apply this custom configuration to repositories where you want to turn off paid features.
Ensure that you give your custom configuration a very clear name, for example: "No Code Security" or "Secret Protection and Supply chain only" to avoid confusion.
For more information, see [Creating a custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/creating-a-custom-security-configuration) and [Applying a custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/applying-a-custom-security-configuration).
