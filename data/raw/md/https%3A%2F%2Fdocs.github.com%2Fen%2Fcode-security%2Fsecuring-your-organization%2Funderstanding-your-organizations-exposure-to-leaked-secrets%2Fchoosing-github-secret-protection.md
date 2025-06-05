  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secure your organization](https://docs.github.com/en/code-security/securing-your-organization "Secure your organization")/
  * [Exposure to leaked secrets](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets "Exposure to leaked secrets")/
  * [Secret protection](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/choosing-github-secret-protection "Secret protection")


# Choosing GitHub Secret Protection
Learn how GitHub Secret Protection can help you detect secrets in your codebases and prevent leaks before they happen using continuous monitoring and prevention tools.
## Who can use this feature?
GitHub Secret Protection is a set of features within GitHub Advanced Security that is available to the following users:
  * GitHub Team plan users
  * Enterprise organizations on GitHub Enterprise Cloud and GitHub Enterprise Server


## In this article
  * [About GitHub Secret Protection](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/choosing-github-secret-protection#about-github-secret-protection)
  * [Why you should enable Secret Protection for 100% of your organization's repositories](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/choosing-github-secret-protection#why-you-should-enable-secret-protection-for-100-of-your-organizations-repositories)
  * [Enabling Secret Protection](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/choosing-github-secret-protection#enabling-secret-protection)
  * [Enabling Secret Protection from the secret risk assessment](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/choosing-github-secret-protection#enabling-secret-protection-from-the-secret-risk-assessment)


## [About GitHub Secret Protection](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/choosing-github-secret-protection#about-github-secret-protection)
Secret Protection includes the following features to help you detect and prevent secret leaks, allowing continuous monitoring and detection. For details about the features and their availability, see [GitHub Secret Protection](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security#github-secret-protection).
  * **Secret scanning** : Detect secrets, for example keys and tokens, that have been checked into a repository and receive alerts.
  * **Push protection** : Prevent secret leaks before they happen by blocking commits containing secrets.
  * **Copilot secret scanning** : Leverage AI to detect unstructured credentials, such as passwords, that have been checked into a repository.
  * **Custom patterns** : Detect and prevent leaks for organization-specific secrets.
  * **Delegated bypass for push protection** and **Delegated alert dismissal** : Implement an approval process for better control over who in your enterprise can perform sensitive actions, supporting governance at scale.
  * **Security overview** : Understand the distribution of risk across your organization.


In addition, Secret Protection includes a free scanning feature, the **risk assessment** report, to help organizations understand their secret leak footprint across their GitHub perimeter. See [About the secret risk assessment](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/about-secret-risk-assessment).
Secret Protection is billed per active committer to the repositories where it is enabled. It is available to users with a GitHub Team or GitHub Enterprise plan, see [About billing for GitHub Advanced Security](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-advanced-security/about-billing-for-github-advanced-security).
## [Why you should enable Secret Protection for 100% of your organization's repositories](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/choosing-github-secret-protection#why-you-should-enable-secret-protection-for-100-of-your-organizations-repositories)
GitHub recommends enabling GitHub Secret Protection products for all repositories, in order to protect your organization from the risk of secret leaks and exposures. GitHub Secret Protection is free to enable for public repositories, and available as a purchasable add-on for private and internal repositories.
  * The free secret risk assessment scans _only the code_ in your organization, including the code in archived repositories. You can extend the surface being scanned to cover content in pull requests, issues, wikis, and GitHub Discussions with **GitHub Secret Protection**.. See [About secret scanning](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning)
  * The secret risk assessment and secret scanning _scan code that has already been committed_ into your repositories. With **push protection** , your code is scanned for secrets _before_ commits are saved on GitHub, during the push process, and the push is blocked if any secrets are detected. See [About push protection](https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection).
  * If you have one or more secret patterns that are internal to your organization, these will not be detected by the default patterns supported by secret scanning. You can define **custom patterns** that are only valid in your organization, and extend the secret scanning capabilities to detect these patterns. See [Defining custom patterns for secret scanning](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/defining-custom-patterns-for-secret-scanning).
  * Knowing which secrets could be exploited makes it easy to prioritize remediation of leaked secrets found by secret scanning. **Validity checks** tell you if an active secret is one that could still be exploited, so these alerts should be reviewed and remediated as a priority. See [Enabling validity checks for your repository](https://docs.github.com/en/code-security/secret-scanning/enabling-secret-scanning-features/enabling-validity-checks-for-your-repository).
  * You may also want to detect leaks of unstructured secrets such as passwords. This is possible with our AI-powered **Copilot secret scanning**. See [Responsible detection of generic secrets with Copilot secret scanning](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-generic-secrets).
  * Visualizing the prevention, detection, and remediation of security data is critical to understanding where to direct effort and where security initiatives are having an impact. **Security overview** has dedicated views that allow you to dig deep into the current state of your codebases at the organization and enterprise level. See [About security overview](https://docs.github.com/en/code-security/security-overview/about-security-overview).


In addition to detecting and preventing secret leaks, you should consider building code security into all of your organization workflows to secure your software supply chain. See [About supply chain security](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-supply-chain-security).
If you require help evaluating your security needs or options, contact [GitHub's Sales team](https://github.com/security/contact-sales).
Alternatively, you can trial GitHub Advanced Security for free to assess your needs. See [Planning a trial of GitHub Advanced Security](https://docs.github.com/en/code-security/trialing-github-advanced-security/planning-a-trial-of-ghas).
## [Enabling Secret Protection](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/choosing-github-secret-protection#enabling-secret-protection)
You can quickly enable security features at scale with the GitHub-recommended security configuration, a collection of security enablement settings you can apply to repositories in an organization. You can then further customize Advanced Security features at the organization level with global settings. See [About enabling security features at scale](https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/about-enabling-security-features-at-scale).
Security configurations can be applied at enterprise and organization level. You can also configure additional security settings for your organization. These settings, called global settings, are then inherited by all repositories in the organization. With global settings, you can customize how security features analyze your organization. See [Configuring global security settings for your organization](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization).
In addition, repository administrators can enable security features at the repository level.
## [Enabling Secret Protection from the secret risk assessment](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/choosing-github-secret-protection#enabling-secret-protection-from-the-secret-risk-assessment)
The secret risk assessment report is currently in public preview and subject to change. If you have feedback or questions, please join the [discussion in GitHub Community](https://github.com/orgs/community/discussions/153016) – we’re listening.
  1. On GitHub, navigate to the main page of the organization.
  2. Under your organization name, click 
![Screenshot of the horizontal navigation bar for an organization. A tab, labeled with a shield icon and "Security," is outlined in dark orange.](https://docs.github.com/assets/cb-22170/images/help/organizations/organization-security-tab.png)
  3. In the sidebar, under "Security", click **Assessments**.
  4. Click the **Enable Secret Protection** dropdown in the banner display, and then select one of the options for enabling the feature in your organization's repositories.
     * **For public repositories for free** : Click to enable for _only_ public repositories in your organization.
     * **For all repositories** : Click **Enable Secret Protection** to enable both secret scanning and push protection for all repositories in your organization, at the estimated cost displayed. You will incur usage costs or need to purchase GitHub Secret Protection licenses.
Alternatively, click **Configure in settings** to customize which repositories you want to enable Secret Protection for. See [Applying the GitHub-recommended security configuration in your organization](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/applying-the-github-recommended-security-configuration-in-your-organization) and [Creating a custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/creating-a-custom-security-configuration).


