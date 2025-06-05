  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secure your organization](https://docs.github.com/en/code-security/securing-your-organization "Secure your organization")/
  * [Exposure to leaked secrets](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets "Exposure to leaked secrets")/
  * [View secret risk assessment](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/viewing-the-secret-risk-assessment-report-for-your-organization "View secret risk assessment")


# Viewing the secret risk assessment report for your organization
You can generate and view the secret risk assessment report for your organization from the "Security" tab.
## Who can use this feature?
Organization owners and security managers
## In this article
  * [Generating an initial secret risk assessment](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/viewing-the-secret-risk-assessment-report-for-your-organization#generating-an-initial-secret-risk-assessment)
  * [Rerunning the secret risk assessment](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/viewing-the-secret-risk-assessment-report-for-your-organization#rerunning-the-secret-risk-assessment)
  * [Viewing the secret risk assessment](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/viewing-the-secret-risk-assessment-report-for-your-organization#viewing-the-secret-risk-assessment)
  * [Exporting the secret risk assessment to CSV](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/viewing-the-secret-risk-assessment-report-for-your-organization#exporting-the-secret-risk-assessment-to-csv)
  * [Next steps](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/viewing-the-secret-risk-assessment-report-for-your-organization#next-steps)


GitHub provides a **secret risk assessment** report that organization owners and security managers can generate to evaluate the exposure of an organization to leaked secrets. The secret risk assessment is an **on-demand, point-in-time scan** of the code within an organization that:
  * Shows any leaked secrets within the organization
  * Shows the kinds of secrets that are leaked outside the organization
  * Provides actionable insights for remediation For more information about the report, see [About the secret risk assessment](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/about-secret-risk-assessment).


You can generate the secret risk assessment report for your organization, review it, and export the results to CSV.
The secret risk assessment report is currently in public preview and subject to change. If you have feedback or questions, please join the [discussion in GitHub Community](https://github.com/orgs/community/discussions/153016) – we’re listening.
## [Generating an initial secret risk assessment](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/viewing-the-secret-risk-assessment-report-for-your-organization#generating-an-initial-secret-risk-assessment)
  1. On GitHub, navigate to the main page of the organization.
  2. Under your organization name, click 
![Screenshot of the horizontal navigation bar for an organization. A tab, labeled with a shield icon and "Security," is outlined in dark orange.](https://docs.github.com/assets/cb-22170/images/help/organizations/organization-security-tab.png)
  3. In the sidebar, under "Security", click **Assessments**.
  4. To generate the secret risk assessment, click **Scan your organization**.


If you're an organization owner and you've opted in for email notifications, GitHub will send you an email to let you know when the report is ready to view.
Did you successfully generate the secret risk assessment report for your organization?
[Yes](https://docs.github.io/success-test/yes.html) [No](https://docs.github.io/success-test/no.html)
## [Rerunning the secret risk assessment](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/viewing-the-secret-risk-assessment-report-for-your-organization#rerunning-the-secret-risk-assessment)
You can only generate the report once every 90 days. We recommend that you implement GitHub Secret Protection for continuous secret monitoring and prevention. See [Choosing GitHub Secret Protection](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/choosing-github-secret-protection).
  1. On GitHub, navigate to the main page of the organization.
  2. Under your organization name, click 
![Screenshot of the horizontal navigation bar for an organization. A tab, labeled with a shield icon and "Security," is outlined in dark orange.](https://docs.github.com/assets/cb-22170/images/help/organizations/organization-security-tab.png)
  3. In the sidebar, under "Security", click **Assessments**.
  4. Towards the top right side of the existing report, click 
  5. Select **Rerun scan**.
If you're an organization owner and you've opted in for email notifications, GitHub will send you an email to let you know when the report is ready to view.


## [Viewing the secret risk assessment](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/viewing-the-secret-risk-assessment-report-for-your-organization#viewing-the-secret-risk-assessment)
  1. On GitHub, navigate to the main page of the organization.
  2. Under your organization name, click 
![Screenshot of the horizontal navigation bar for an organization. A tab, labeled with a shield icon and "Security," is outlined in dark orange.](https://docs.github.com/assets/cb-22170/images/help/organizations/organization-security-tab.png)
  3. In the sidebar, under "Security", click **Assessments**. You can see the most recent report on this page.


## [Exporting the secret risk assessment to CSV](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/viewing-the-secret-risk-assessment-report-for-your-organization#exporting-the-secret-risk-assessment-to-csv)
  1. On GitHub, navigate to the main page of the organization.
  2. Under your organization name, click 
![Screenshot of the horizontal navigation bar for an organization. A tab, labeled with a shield icon and "Security," is outlined in dark orange.](https://docs.github.com/assets/cb-22170/images/help/organizations/organization-security-tab.png)
  3. In the sidebar, under "Security", click **Assessments**.
  4. Towards the top right side of the report, click 
  5. Select **Download CSV**.


The secret risk assessment CSV file includes the following information.
CSV column | Name | Description  
---|---|---  
A | `Organization Name` | The name of the organization the secret was detected in  
B | `Name` | The token name for the type of secret  
C | `Slug` | The normalized string for the token. This corresponds to `Token` in the table of supported secrets. See [Supported secret scanning patterns](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#supported-secrets).  
D | `Push Protected` | A `boolean` to indicate whether the secret would be detected and blocked by push protection if it were enabled  
E | `Non-Provider Pattern` | A `boolean` to indicate whether the secret matched a non-provider pattern and would generate an alert if secret scanning with non-provider patterns were enabled  
F | `Secret Count` | An aggregate count of the active and inactive secrets found for the token type  
G | `Repository Count` | An aggregate count of distinct repositories in which the secret type was found, including public, private,, and archived repositories  
## [Next steps](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/viewing-the-secret-risk-assessment-report-for-your-organization#next-steps)
Now that you've generated secret risk assessment for your organization, learn how to interpret the results. See [Interpreting secret risk assessment results](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/interpreting-secret-risk-assessment-results).
