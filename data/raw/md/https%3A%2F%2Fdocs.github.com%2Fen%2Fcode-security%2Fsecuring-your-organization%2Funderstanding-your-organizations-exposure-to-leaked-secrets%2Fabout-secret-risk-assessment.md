  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secure your organization](https://docs.github.com/en/code-security/securing-your-organization "Secure your organization")/
  * [Exposure to leaked secrets](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets "Exposure to leaked secrets")/
  * [Secret risk assessment](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/about-secret-risk-assessment "Secret risk assessment")


# About the secret risk assessment
Learn why it's so important to understand your organization's exposure to data leaks and how the secret risk assessment report gives an overview of your organization’s secret leak footprint.
## Who can use this feature?
Secret risk assessment is available for free for organization-owned repositories on GitHub Team and GitHub Enterprise
## In this article
  * [About exposure to leaked secrets](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/about-secret-risk-assessment#about-exposure-to-leaked-secrets)
  * [About secret risk assessment](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/about-secret-risk-assessment#about-secret-risk-assessment)
  * [Next steps](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/about-secret-risk-assessment#next-steps)


## [About exposure to leaked secrets](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/about-secret-risk-assessment#about-exposure-to-leaked-secrets)
Assessing your exposure to leaked secrets is crucial if you want to prevent:
  * **Exploitation by bad actors**. Malicious actors can use leaked secrets such as API keys, passwords, and tokens to gain unauthorized access to systems, databases, and sensitive information. Leaked secrets can lead to data breaches, compromising user data and potentially causing significant financial and reputational damage. See industry examples and in-depth discussion in [Understanding your organization's exposure to secret leaks](https://resources.github.com/enterprise/understanding-secret-leak-exposure) in GitHub Executive Insights.
  * **Regulatory problems**. Many industries have strict regulatory requirements for data protection, and leaked secrets can result in non-compliance with regulations, leading to legal penalties and fines.
  * **Service disruptions**. Unauthorized access to systems can lead to service disruptions, impacting the availability and reliability of services provided to users.
  * **Loss of trust**. Customers expect robust security measures to protect their data, and exposure to leaked secrets can erode trust and confidence in your organization's ability to safeguard information.
  * **Costly fallout**. Addressing the fallout from leaked secrets can be costly, involving incident response efforts, security audits, and potential compensation for affected parties.


Regularly assessing your exposure to leaked secrets is good practice to help identify vulnerabilities, implement necessary security measures, and ensure that any compromised secrets are promptly rotated and invalidated.
## [About secret risk assessment](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/about-secret-risk-assessment#about-secret-risk-assessment)
The secret risk assessment report is currently in public preview and subject to change. If you have feedback or questions, please join the [discussion in GitHub Community](https://github.com/orgs/community/discussions/153016) – we’re listening.
This report is only available if you are on the GitHub Team plan. For information about the plan and how to upgrade, see [GitHub Team](https://docs.github.com/en/get-started/learning-about-github/githubs-plans#github-team) and [Upgrading your organization's plan](https://docs.github.com/en/billing/managing-the-plan-for-your-github-account/upgrading-your-accounts-plan#upgrading-your-organizations-plan).
GitHub provides a **secret risk assessment** report that organization owners and security managers can generate to evaluate the exposure of an organization to leaked secrets. The secret risk assessment is an **on-demand, point-in-time scan** of the code within an organization that:
  * Shows any leaked secrets within the organization
  * Shows the kinds of secrets that are leaked outside the organization
  * Provides actionable insights for remediation


The secret risk assessment report provides the following insights:
  * **Total secrets** —Aggregate count of exposed secrets detected within the organization.
  * **Public leaks** —Distinct secrets found in your organization's public repositories.
  * **Preventable leaks** —Secrets that could have been protected, using GitHub Secret Protection features such as secret scanning and push protection.
  * **Secret locations** —Locations that are scanned for the report. The free secret risk assessment scans _only the code_ in your organization, including the code in archived repositories. You can extend the surface being scanned to cover content in pull requests, issues, wikis, and GitHub Discussions with **GitHub Secret Protection**.
  * **Secret categories** —Distribution of the types of secrets that are leaked. Secrets can be partner secrets, which are strings that match secrets issued by service providers in our partner program, or generic secrets, which are non-provider patterns such as SSH keys, database connection strings, and JSON web tokens.
  * **Repositories with leaks** —Repositories where leaked secrets were detected, out of all the repositories scanned.


You can only generate the report once every 90 days. We recommend that you implement GitHub Secret Protection for continuous secret monitoring and prevention. See [Choosing GitHub Secret Protection](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/choosing-github-secret-protection).
Because the secret risk assessment report is based on **your repositories** , regardless of the enablement status of GitHub Secret Protection features, you can see your current exposure to leaked secrets, and understand better how GitHub can help you prevent future secret leaks.
## [Next steps](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/about-secret-risk-assessment#next-steps)
Now that you know about the secret risk assessment report, you may want to learn how to:
  * Generate the report to see your organization risk. See [Viewing the secret risk assessment report for your organization](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/viewing-the-secret-risk-assessment-report-for-your-organization).
  * Interpret the results of the report. See [Interpreting secret risk assessment results](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/interpreting-secret-risk-assessment-results).
  * Enable GitHub Secret Protection to improve your secret leak footprint. See [Choosing GitHub Secret Protection](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/choosing-github-secret-protection#enabling-secret-protection).


