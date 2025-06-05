  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secure your organization](https://docs.github.com/en/code-security/securing-your-organization "Secure your organization")/
  * [Enable security features](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization "Enable security features")/
  * [Create custom configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/creating-a-custom-security-configuration "Create custom configuration")


# Creating a custom security configuration
Build a custom security configuration to meet the specific security needs of repositories in your organization.
## Who can use this feature?
Organization owners, security managers, and organization members with the **admin** role
## In this article
  * [About custom security configurations](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/creating-a-custom-security-configuration#about-custom-security-configurations)
  * [Creating a Secret Protection and Code Security configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/creating-a-custom-security-configuration#creating-a-secret-protection-and-code-security-configuration)
  * [Creating a GitHub Advanced Security configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/creating-a-custom-security-configuration#creating-a-github-advanced-security-configuration)
  * [Next steps](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/creating-a-custom-security-configuration#next-steps)


## [About custom security configurations](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/creating-a-custom-security-configuration#about-custom-security-configurations)
We recommend securing your organization with the GitHub-recommended security configuration, then evaluating the security findings on your repositories before configuring custom security configurations. For more information, see [Applying the GitHub-recommended security configuration in your organization](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/applying-the-github-recommended-security-configuration-in-your-organization).
With custom security configurations, you can create collections of enablement settings for GitHub's security products to meet the specific security needs of your organization. For example, you can create a different custom security configuration for each group of repositories to reflect their different levels of visibility, risk tolerance, and impact.
You can also choose whether or not you want to include GitHub Code Security or GitHub Secret Protection features in a configuration. If you do, keep in mind that these features incur usage costs (or require GitHub Advanced Security licenses) when applied to private and internal repositories. For more information, see [About GitHub Advanced Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security).
The order and names of some settings will differ depending on whether you are using licenses for the original GitHub Advanced Security product, or for the two new products: GitHub Code Security and GitHub Secret Protection. See [Creating a GitHub Advanced Security configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/creating-a-custom-security-configuration#creating-a-github-advanced-security-configuration) or [Creating a Secret Protection and Code Security configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/creating-a-custom-security-configuration#creating-a-secret-protection-and-code-security-configuration).
## [Creating a Secret Protection and Code Security configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/creating-a-custom-security-configuration#creating-a-secret-protection-and-code-security-configuration)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Under your organization name, click **Settings**.
![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](https://docs.github.com/assets/cb-49309/images/help/discussions/org-settings-global-nav-update.png)
  3. In the "Security" section of the sidebar, select the **Configurations**.
  4. In the "Security configurations" section, click **New configuration**.
  5. To help identify your custom security configuration and clarify its purpose on the "Security configurations" page, name your configuration and create a description.
  6. Optionally, enable "Secret Protection", a paid feature for private repositories. Enabling Secret Protection enables alerts for secret scanning. In addition, you can choose whether to enable, disable, or keep the existing settings for the following secret scanning features:
     * **Validity checks**. To learn more about validity checks for partner patterns, see [Evaluating alerts from secret scanning](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts#checking-a-secrets-validity).
     * **Non-provider patterns**. To learn more about scanning for non-provider patterns, see [Supported secret scanning patterns](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#non-provider-patterns) and [Viewing and filtering alerts from secret scanning](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/viewing-alerts).
     * **Scan for generic passwords**. To learn more, see [Responsible detection of generic secrets with Copilot secret scanning](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-generic-secrets).
     * **Push protection**. To learn about push protection, see [About push protection](https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection).
     * **Bypass privileges**. By assigning bypass privileges, selected organization members can bypass push protection, and there is a review and approval process for all other contributors. See [About delegated bypass for push protection](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/about-delegated-bypass-for-push-protection).
     * **Prevent direct alert dismissals**. To learn more, see [Enabling delegated alert dismissal for secret scanning](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/enabling-delegated-alert-dismissal-for-secret-scanning).
  7. Optionally, enable "Code Security", a paid feature for private repositories. You can choose whether to enable, disable, or keep the existing settings for the following code scanning features:
     * **Default setup**. To learn more, see [Configuring default setup for code scanning](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning#about-default-setup).
     * **Runner type**. If you want to target specific runners for code scanning, you can choose to use custom-labeled runners at this step. See [Configuring default setup for code scanning](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning#assigning-labels-to-runners).
     * **Prevent direct alert dismissals**. To learn more, see [Enabling delegated alert dismissal for code scanning](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/enabling-delegated-alert-dismissal-for-code-scanning).
  8. Still under "Code Security", in the "Dependency scanning" table, choose whether you want to enable, disable, or keep the existing settings for the following dependency scanning features:
     * **Dependency graph**. To learn about dependency graph, see [About the dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph). 
When both "Code Security" and Dependency graph are enabled, this enables dependency review, see [About dependency review](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review).
     * **Automatic dependency submission**. To learn about automatic dependency submission, see [Configuring automatic dependency submission for your repository](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-automatic-dependency-submission-for-your-repository).
     * **Dependabot alerts**. To learn about Dependabot, see [About Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts).
     * **Security updates**. To learn about security updates, see [About Dependabot security updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates).
  9. For "Private vulnerability reporting", choose whether you want to enable, disable, or keep the existing settings. To learn about private vulnerability reporting, see [Configuring private vulnerability reporting for a repository](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/configuring-private-vulnerability-reporting-for-a-repository).
  10. Optionally, in the "Policy" section, you can use additional options to control how the configuration is applied:
     * **Use as default for newly created repositories**. Select the **None** **Public** , **Private and internal** , or **All repositories**. 
The default security configuration for an organization is only automatically applied to new repositories created in your organization. If a repository is transferred into your organization, you will still need to apply an appropriate security configuration to the repository manually.
     * **Enforce configuration**. Block repository owners from changing features that are enabled or disabled by the configuration (features that are not set aren't enforced). Select **Enforce** from the dropdown menu.
  11. To finish creating your custom security configuration, click **Save configuration**.


If a user in your enterprise attempts to change the enablement status of a feature in an enforced configuration using the REST API, the API call will appear to succeed, but no enablement statuses will change.
Some situations can break the enforcement of security configurations for a repository. For example, the enablement of code scanning will not apply to a repository if:
  * GitHub Actions is initially enabled on the repository, but is then disabled in the repository.
  * GitHub Actions required by code scanning configurations are not available in the repository.
  * The definition for which languages should not be analyzed using code scanning default setup is changed.


## [Creating a GitHub Advanced Security configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/creating-a-custom-security-configuration#creating-a-github-advanced-security-configuration)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Under your organization name, click **Settings**.
![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](https://docs.github.com/assets/cb-49309/images/help/discussions/org-settings-global-nav-update.png)
  3. In the "Security" section of the sidebar, select the **Configurations**.
  4. In the "Security configurations" section, click **New configuration**.
  5. To help identify your custom security configuration and clarify its purpose on the "New configuration" page, name your configuration and create a description.
  6. In the "GitHub Advanced Security features" row, choose whether to include or exclude GitHub Advanced Security (GHAS) features.
  7. In the "Secret scanning" table, choose whether you want to enable, disable, or keep the existing settings for the following security features:
     * **Validity checks**. To learn more about validity checks for partner patterns, see [Evaluating alerts from secret scanning](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts#checking-a-secrets-validity).
     * **Non-provider patterns**. To learn more about scanning for non-provider patterns, see [Supported secret scanning patterns](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#non-provider-patterns) and [Viewing and filtering alerts from secret scanning](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/viewing-alerts).
     * **Scan for generic passwords**. To learn more, see [Responsible detection of generic secrets with Copilot secret scanning](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-generic-secrets).
     * **Push protection**. To learn about push protection, see [About push protection](https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection).
     * **Bypass privileges**. By assigning bypass privileges, selected organization members can bypass push protection, and there is a review and approval process for all other contributors. See [About delegated bypass for push protection](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/about-delegated-bypass-for-push-protection).
     * **Prevent direct alert dismissals**. To learn more, see [Enabling delegated alert dismissal for secret scanning](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/enabling-delegated-alert-dismissal-for-secret-scanning).
  8. In the "Code scanning" table, choose whether you want to enable, disable, or keep the existing settings for code scanning default setup.
     * **Default setup**. To learn more, see [Configuring default setup for code scanning](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning#about-default-setup).
     * **Runner type**. If you want to target specific runners for code scanning, you can choose to use custom-labeled runners at this step. See [Configuring default setup for code scanning](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning#assigning-labels-to-runners).
     * **Prevent direct alert dismissals**. To learn more, see [Enabling delegated alert dismissal for code scanning](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/enabling-delegated-alert-dismissal-for-code-scanning).
  9. In the "Dependency scanning" table, choose whether you want to enable, disable, or keep the existing settings for the following dependency scanning features:
     * **Dependency graph**. To learn about dependency graph, see [About the dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph). 
When both "GitHub Advanced Security" and Dependency graph are enabled, this enables dependency review, see [About dependency review](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review).
     * **Automatic dependency submission**. To learn about automatic dependency submission, see [Configuring automatic dependency submission for your repository](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-automatic-dependency-submission-for-your-repository).
     * **Dependabot alerts**. To learn about Dependabot, see [About Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts).
     * **Security updates**. To learn about security updates, see [About Dependabot security updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates).
  10. For "Private vulnerability reporting", choose whether you want to enable, disable, or keep the existing settings. To learn about private vulnerability reporting, see [Configuring private vulnerability reporting for a repository](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/configuring-private-vulnerability-reporting-for-a-repository).
  11. Optionally, in the "Policy" section, you can use additional options to control how the configuration is applied:
     * **Use as default for newly created repositories**. Select the **None** **Public** , **Private and internal** , or **All repositories**. 
The default security configuration for an organization is only automatically applied to new repositories created in your organization. If a repository is transferred into your organization, you will still need to apply an appropriate security configuration to the repository manually.
     * **Enforce configuration**. Block repository owners from changing features that are enabled or disabled by the configuration (features that are not set aren't enforced). Select **Enforce** from the dropdown menu.
  12. To finish creating your custom security configuration, click **Save configuration**.


## [Next steps](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/creating-a-custom-security-configuration#next-steps)
To apply your custom security configuration to repositories in your organization, see [Applying a custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/applying-a-custom-security-configuration).
To learn how to edit your custom security configuration, see [Editing a custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/editing-a-custom-security-configuration).
