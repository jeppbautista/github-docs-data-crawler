  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Trial GitHub Advanced Security](https://docs.github.com/en/code-security/trialing-github-advanced-security "Trial GitHub Advanced Security")/
  * [Trial Secret Protection](https://docs.github.com/en/code-security/trialing-github-advanced-security/explore-trial-secret-scanning "Trial Secret Protection")


# Exploring your enterprise trial of GitHub Secret Protection
Introduction to the features available with GitHub Secret Protection in GitHub Enterprise Cloud so you can assess their fit to your business needs.
## In this article
  * [Introduction](https://docs.github.com/en/code-security/trialing-github-advanced-security/explore-trial-secret-scanning#introduction)
  * [Identify additional access tokens](https://docs.github.com/en/code-security/trialing-github-advanced-security/explore-trial-secret-scanning#identify-additional-access-tokens)
  * [Use AI to detect potential passwords](https://docs.github.com/en/code-security/trialing-github-advanced-security/explore-trial-secret-scanning#use-ai-to-detect-potential-passwords)
  * [Control and audit the bypass process](https://docs.github.com/en/code-security/trialing-github-advanced-security/explore-trial-secret-scanning#control-and-audit-the-bypass-process)
  * [Enable validity checks](https://docs.github.com/en/code-security/trialing-github-advanced-security/explore-trial-secret-scanning#enable-validity-checks)
  * [Next steps](https://docs.github.com/en/code-security/trialing-github-advanced-security/explore-trial-secret-scanning#next-steps)


This guide assumes that you have planned and started a trial of GitHub Advanced Security for an existing or trial GitHub enterprise account. See [Planning a trial of GitHub Advanced Security](https://docs.github.com/en/code-security/trialing-github-advanced-security/planning-a-trial-of-ghas).
## [Introduction](https://docs.github.com/en/code-security/trialing-github-advanced-security/explore-trial-secret-scanning#introduction)
GitHub Secret Protection features work the same way in private and internal repositories as they do in all public repositories. This article focuses on the additional functionality that you can use to protect your business from security leaks when you use GitHub Secret Protection, that is:
  * Identify additional access tokens you use by defining custom patterns.
  * Detect potential passwords using AI.
  * Control and audit the bypass process for push protection and secret scanning alerts.
  * Enable validity checks for exposed tokens.


If you have already scanned the code in your organization for leaked secrets using the free secret risk assessment, you will also want to explore that data more completely using the additional views on the 
For full details of the features available, see [GitHub Secret Protection](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security#github-secret-protection).
### [Security configuration for Secret Protection](https://docs.github.com/en/code-security/trialing-github-advanced-security/explore-trial-secret-scanning#security-configuration-for-secret-protection)
Most enterprises choose to enable Secret Protection with push protection across all their repositories by applying security configurations with these features enabled. This ensures that repositories are checked for access tokens that have already been added to GitHub, in addition to flagging when users are about to leak tokens in GitHub. For information about creating an enterprise-level security configuration and applying it to your test repositories, see [Enabling security features in your trial enterprise](https://docs.github.com/en/code-security/trialing-github-advanced-security/enable-security-features-trial).
### [Provide access to view the results of secret scanning](https://docs.github.com/en/code-security/trialing-github-advanced-security/explore-trial-secret-scanning#provide-access-to-view-the-results-of-secret-scanning)
By default, only the repository administrator and the organization owner can view all secret scanning alerts in their area. You should assign the predefined security manager role to all organization teams and users who you want to access the alerts found during the trial. You may also want to give the enterprise account owner this role for each organization in the trial. For more information, see [Managing security managers in your organization](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization).
You can see a summary of any results found in the organizations in your trial enterprise in the [Viewing security insights](https://docs.github.com/en/code-security/security-overview/viewing-security-insights).
## [Identify additional access tokens](https://docs.github.com/en/code-security/trialing-github-advanced-security/explore-trial-secret-scanning#identify-additional-access-tokens)
You can create custom patterns to identify additional access tokens at the repository, organization, and enterprise level. In most cases, you should define custom patterns at the enterprise level because this will ensure that the patterns are used across the whole enterprise. It will also make them easy to maintain if you need to update a pattern when the format for a token changes.
Once you have created and published custom patterns, both secret scanning and push protection automatically include the new patterns in all scans. For detailed information about creating custom patterns, see [Defining custom patterns for secret scanning](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/defining-custom-patterns-for-secret-scanning).
## [Use AI to detect potential passwords](https://docs.github.com/en/code-security/trialing-github-advanced-security/explore-trial-secret-scanning#use-ai-to-detect-potential-passwords)
At the enterprise level you have full control over whether or not to allow the use of AI to detect secrets that cannot be identified using regular expressions (also known as generic secrets or as non-provider patterns).
  * Turn the feature on or off for the whole enterprise.
  * Set a policy to block control of the feature at the organization and repository level.
  * Set a policy to allow organization owners or repository administrators to control the feature.


Similar to custom patterns, if you enable AI detection both secret scanning and push protection automatically start using AI detection in all scans. For information about enterprise-level control, see [Configuring additional secret scanning settings for your enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-code-security/securing-your-enterprise/configuring-additional-secret-scanning-settings-for-your-enterprise) and [Enforcing policies for code security and analysis for your enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-code-security-and-analysis-for-your-enterprise).
## [Control and audit the bypass process](https://docs.github.com/en/code-security/trialing-github-advanced-security/explore-trial-secret-scanning#control-and-audit-the-bypass-process)
When push protection blocks a push to GitHub in a public repository without GitHub Secret Protection, the user has two simple options: bypass the control, or remove the highlighted content from the branch and its history. If they chose to bypass push protection, a secret scanning alert is automatically created. This allows developers to rapidly unblock their work while still providing an audit trail for the content identified by secret scanning.
Larger teams usually want to maintain tighter control over the potential publication of access tokens and other secrets. With GitHub Secret Protection, you can define a reviewers group to approve requests to bypass push protection, reducing the risk of a developer accidentally leaking a token that is still active. You can also define a reviewers group to approve requests to dismiss secret scanning alerts.
Reviewers are defined in an organization-level security configuration or in the settings for a repository. For more information, see [About delegated bypass for push protection](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/about-delegated-bypass-for-push-protection).
## [Enable validity checks](https://docs.github.com/en/code-security/trialing-github-advanced-security/explore-trial-secret-scanning#enable-validity-checks)
You can enable validity checks to check whether detected tokens are still active at the repository, organization, and enterprise level. Generally, it is worth enabling this feature across the whole enterprise using enterprise or organization-level security configurations. For more information, see [Enabling validity checks for your repository](https://docs.github.com/en/code-security/secret-scanning/enabling-secret-scanning-features/enabling-validity-checks-for-your-repository).
## [Next steps](https://docs.github.com/en/code-security/trialing-github-advanced-security/explore-trial-secret-scanning#next-steps)
When you have enabled the additional controls for Secret Protection, you're ready to test them against your business needs, and explore further. You may also be ready to look into exploring the options available with GitHub Code Security.
  * [Exploring your enterprise trial of GitHub Code Security](https://docs.github.com/en/code-security/trialing-github-advanced-security/explore-trial-code-scanning)
  * [Enforce GitHub Advanced Security at Scale](https://wellarchitected.github.com/library/application-security/recommendations/enforce-ghas-at-scale/)


