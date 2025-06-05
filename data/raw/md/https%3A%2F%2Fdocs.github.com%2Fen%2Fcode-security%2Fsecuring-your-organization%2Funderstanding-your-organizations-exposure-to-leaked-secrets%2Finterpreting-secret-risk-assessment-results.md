  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secure your organization](https://docs.github.com/en/code-security/securing-your-organization "Secure your organization")/
  * [Exposure to leaked secrets](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets "Exposure to leaked secrets")/
  * [Interpret results](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/interpreting-secret-risk-assessment-results "Interpret results")


# Interpreting secret risk assessment results
Use the results from your secret risk assessment report to improve your organization's security.
## In this article
  * [Prerequisites](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/interpreting-secret-risk-assessment-results#prerequisites)
  * [Prioritizing high-risk leaks for remediation](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/interpreting-secret-risk-assessment-results#prioritizing-high-risk-leaks-for-remediation)
  * [Identifying areas of exposure](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/interpreting-secret-risk-assessment-results#identifying-areas-of-exposure)
  * [Adopt GitHub Secret Protection to prevent leaks](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/interpreting-secret-risk-assessment-results#adopt-github-secret-protection-to-prevent-leaks)


The secret risk assessment dashboard displays point-in-time insights into the secrets detected in your organization. For more information about the report, see [About the secret risk assessment](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/about-secret-risk-assessment).
The secret risk assessment report is currently in public preview and subject to change. If you have feedback or questions, please join the [discussion in GitHub Community](https://github.com/orgs/community/discussions/153016) – we’re listening.
## [Prerequisites](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/interpreting-secret-risk-assessment-results#prerequisites)
You need to generate a secret risk assessment report and wait for the scan to complete before being able to view and export the results. See [Viewing the secret risk assessment report for your organization](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/viewing-the-secret-risk-assessment-report-for-your-organization#generating-an-initial-secret-risk-assessment) and [Exporting the secret risk assessment to CSV](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/viewing-the-secret-risk-assessment-report-for-your-organization#exporting-the-secret-risk-assessment-to-csv).
## [Prioritizing high-risk leaks for remediation](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/interpreting-secret-risk-assessment-results#prioritizing-high-risk-leaks-for-remediation)
To understand your secrets' footprint and exposure to secrets leaks, review the **Total secrets** ,**Public leaks** and **Secret locations** metrics.
Next, identify the areas in your organization where leaked secrets pose the highest threat to security.
  * **Leaked secrets that are still active** usually present the greatest risk to security. Prioritize any active secrets for remediation ahead of inactive secrets. For more information about checking the validity of a detected credential, see [Enabling validity checks for your repository](https://docs.github.com/en/code-security/secret-scanning/enabling-secret-scanning-features/enabling-validity-checks-for-your-repository).
  * Similarly, **secrets leaked in public repositories** are usually considered a higher risk and priority, than those secrets leaked in private repositories.
  * The **Repositories with leaks** metric can indicate how frequent, or the extent of, secret leaks across your organization. A large proportion of repositories with secret leaks may suggest that developer education and increased security awareness around secrets is important for your organization.


## [Identifying areas of exposure](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/interpreting-secret-risk-assessment-results#identifying-areas-of-exposure)
Review the **Preventable leaks** and **Secret categories** metrics to understand your current secret detection coverage, in addition to learning how GitHub can help prevent future secret leaks.
  * Secret leaks that could have been prevented using GitHub Secret Protection features such as secret scanning and push protection are shown by the **Preventable leaks** metric.
  * Using the **Secret categories** metric and the **Token type** table, search for patterns in the type of secrets leaked across your organization. 
    * Common areas and repeated occurrences of leaked secrets may suggest particular CI/CD workflows or development processes in your organization that are contributing to the results.
    * You may also be able to identify specific teams, repositories, or networks that are more prone to secret leaks, and therefore require additional security measures or management to be put in place.


## [Adopt GitHub Secret Protection to prevent leaks](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/interpreting-secret-risk-assessment-results#adopt-github-secret-protection-to-prevent-leaks)
We recommend purchasing GitHub Secret Protection products to improve your organization's exposure to secret leaks and optimize your secret detection rates. GitHub Secret Protection is a continuous monitoring and detection solution that is the most effective path for secure development. See [Choosing GitHub Secret Protection](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/choosing-github-secret-protection).
