  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secure your organization](https://docs.github.com/en/code-security/securing-your-organization "Secure your organization")/
  * [Introduction](https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale "Introduction")/
  * [About organization security](https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/about-enabling-security-features-at-scale "About organization security")


# About enabling security features at scale
You can quickly secure your organization at scale with security configurations and global settings.
## In this article
  * [About securing your organization](https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/about-enabling-security-features-at-scale#about-securing-your-organization)
  * [About security configurations](https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/about-enabling-security-features-at-scale#about-security-configurations)
  * [About global settings](https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/about-enabling-security-features-at-scale#about-global-settings)
  * [About enabling secure access to private registries](https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/about-enabling-security-features-at-scale#about-enabling-secure-access-to-private-registries)
  * [Next steps](https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/about-enabling-security-features-at-scale#next-steps)


## [About securing your organization](https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/about-enabling-security-features-at-scale#about-securing-your-organization)
GitHub has many features that help you improve and maintain the quality of your code. Some features are included in all GitHub plans. Additional features are available to organizations on GitHub Team and GitHub Enterprise Cloud that purchase a GitHub Advanced Security product:
  * **GitHub Secret Protection** , which includes features that help you detect and prevent secret leaks, such as secret scanning and push protection.
  * **GitHub Code Security** , which includes features that help you find and fix vulnerabilities, like code scanning, premium Dependabot features, and dependency review.


You can easily enable and manage GitHub's security features throughout your organization with security configurations, which control repository-level security features, and global settings, which control security features at the organization level. We recommend applying security configurations _and_ customizing your global settings to create a system that best meets the security needs of your organization.
For more information on purchasing GitHub Secret Protection or GitHub Code Security, see [About GitHub Advanced Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security).
## [About security configurations](https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/about-enabling-security-features-at-scale#about-security-configurations)
Security configurations are collections of enablement settings for GitHub's security features that you can apply to any repository within your organization.
There are two types of security configuration:
  * **The GitHub-recommended security configuration**. This configuration is a collection of enablement settings created and managed by subject matter experts at GitHub. The GitHub-recommended security configuration is designed to adequately secure any repository, and can easily be applied to all repositories in your organization.
  * **Custom security configurations**. These are configurations you can create and edit yourself, allowing you to choose different enablement settings for groups of repositories with specific security needs.


If a user in your organization attempts to change the enablement status of a feature in an enforced configuration using the REST API, the API call will appear to succeed, but no enablement statuses will change.
Some situations can break the enforcement of security configurations for a repository. For example, the enablement of code scanning will not apply to a repository if:
  * GitHub Actions is initially enabled on the repository, but is then disabled in the repository.
  * GitHub Actions required by code scanning configurations are not available in the repository.
  * The definition for which languages should not be analyzed using code scanning default setup is changed.


Each repository can only have one security configuration applied to it. To find out how you should get started with security configurations, see [Choosing a security configuration for your repositories](https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/choosing-a-security-configuration-for-your-repositories).
You can also create and manage security configurations using the REST API. For more information, see [Configurations](https://docs.github.com/en/rest/code-security/configurations).
## [About global settings](https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/about-enabling-security-features-at-scale#about-global-settings)
While security configurations determine repository-level security settings, global settings determine your organization-level security settings, which are then inherited by all repositories. With global settings, you can customize how security features analyze your organization.
## [About enabling secure access to private registries](https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/about-enabling-security-features-at-scale#about-enabling-secure-access-to-private-registries)
If your organization uses private registries, providing code scanning and Dependabot secure access to these registries will improve code analysis and allow Dependabot to update a wider range of dependencies. For information, see [Giving security features access to private registries](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/giving-org-access-private-registries).
## [Next steps](https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/about-enabling-security-features-at-scale#next-steps)
To determine which security configurations are right for the repositories in your organization, see [Choosing a security configuration for your repositories](https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/choosing-a-security-configuration-for-your-repositories).
