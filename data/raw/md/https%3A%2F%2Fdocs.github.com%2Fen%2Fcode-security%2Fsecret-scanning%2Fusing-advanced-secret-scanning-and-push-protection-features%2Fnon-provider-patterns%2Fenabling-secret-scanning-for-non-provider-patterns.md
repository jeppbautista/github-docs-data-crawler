  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secret scanning](https://docs.github.com/en/code-security/secret-scanning "Secret scanning")/
  * [Advanced features](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features "Advanced features")/
  * [Non-provider patterns](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/non-provider-patterns "Non-provider patterns")/
  * [Enable for non-provider patterns](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/non-provider-patterns/enabling-secret-scanning-for-non-provider-patterns "Enable for non-provider patterns")


# Enabling secret scanning for non-provider patterns
You can enable secret scanning to detect additional potential secrets at the repository and organization levels.
## Who can use this feature?
Repository owners, organization owners, security managers, and users with the **admin** role
Scanning for non-provider patterns is available for the following repository types:
  * Organization-owned repositories on GitHub Team with [GitHub Secret Protection](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Enabling scanning for non-provider patterns](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/non-provider-patterns/enabling-secret-scanning-for-non-provider-patterns#enabling-scanning-for-non-provider-patterns)
  * [Further reading](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/non-provider-patterns/enabling-secret-scanning-for-non-provider-patterns#further-reading)


## [Enabling scanning for non-provider patterns](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/non-provider-patterns/enabling-secret-scanning-for-non-provider-patterns#enabling-scanning-for-non-provider-patterns)
You can enable scanning for non-provider patterns. Non-provider patterns correspond to secrets such as private keys.
For more information about non-provider patterns, see "[Supported secret scanning patterns](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#about-user--alerts)."
### [Enabling detection of non-provider patterns for a repository](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/non-provider-patterns/enabling-secret-scanning-for-non-provider-patterns#enabling-detection-of-non-provider-patterns-for-a-repository)
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Security" section of the sidebar, click 
  4. Under "Secret Protection", to the right of "Non-provider patterns", click **Enable**.


### [Enabling detection of non-provider patterns for an organization](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/non-provider-patterns/enabling-secret-scanning-for-non-provider-patterns#enabling-detection-of-non-provider-patterns-for-an-organization)
You can enable scanning for non-provider patterns at the organization level using the GitHub-recommended security configuration or by applying a custom security configuration. For more information, see [Applying the GitHub-recommended security configuration in your organization](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/applying-the-github-recommended-security-configuration-in-your-organization) and [Creating a custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/creating-a-custom-security-configuration).
## [Further reading](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/non-provider-patterns/enabling-secret-scanning-for-non-provider-patterns#further-reading)
  * [Managing alerts from secret scanning](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning)


