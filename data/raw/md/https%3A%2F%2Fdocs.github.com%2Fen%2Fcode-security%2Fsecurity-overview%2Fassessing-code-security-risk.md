  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Security overview](https://docs.github.com/en/code-security/security-overview "Security overview")/
  * [Assess security risk of code](https://docs.github.com/en/code-security/security-overview/assessing-code-security-risk "Assess security risk of code")


# Assessing the security risk of your code
You can use security overview to see which teams and repositories are affected by security alerts, and identify repositories for urgent remedial action.
## Who can use this feature?
Access requires:
  * Organization views: **write** access to repositories in the organization
  * Enterprise views: organization owners and security managers


Organizations owned by a GitHub Team account with GitHub Secret Protection or GitHub Code Security, or owned by a GitHub Enterprise account
## In this article
  * [Exploring the security risks in your code](https://docs.github.com/en/code-security/security-overview/assessing-code-security-risk#exploring-the-security-risks-in-your-code)
  * [Viewing organization-level security risks in code](https://docs.github.com/en/code-security/security-overview/assessing-code-security-risk#viewing-organization-level-security-risks-in-code)
  * [Viewing enterprise-level security risks in code](https://docs.github.com/en/code-security/security-overview/assessing-code-security-risk#viewing-enterprise-level-security-risks-in-code)
  * [Next steps](https://docs.github.com/en/code-security/security-overview/assessing-code-security-risk#next-steps)


## [Exploring the security risks in your code](https://docs.github.com/en/code-security/security-overview/assessing-code-security-risk#exploring-the-security-risks-in-your-code)
You can use the different views on your **Security** tab to explore the security risks in your code.
  * **Overview:** use to explore trends in **Detection** , **Remediation** , and **Prevention** of security alerts.
  * **Risk:** use to explore the current state of repositories, across all alert types.
  * **Assessments:** use to explore the current state of repositories, for secret leaks specifically
  * **Alerts views:** use to explore code scanning, Dependabot, or secret scanning alerts in greater detail.


These views provide you with the data and filters to:
  * Assess the landscape of security risk of code stored in all your repositories.
  * Identify the highest impact vulnerabilities to address.
  * Monitor your progress in remediating potential vulnerabilities.
  * Understand how your organization is affected by secret leaks and exposures.
  * Export your current selection of data for further analysis and reporting.


For information about the **Overview** , see [Viewing security insights](https://docs.github.com/en/code-security/security-overview/viewing-security-insights).
## [Viewing organization-level security risks in code](https://docs.github.com/en/code-security/security-overview/assessing-code-security-risk#viewing-organization-level-security-risks-in-code)
  1. On GitHub, navigate to the main page of the organization.
  2. Under your organization name, click 
![Screenshot of the horizontal navigation bar for an organization. A tab, labeled with a shield icon and "Security," is outlined in dark orange.](https://docs.github.com/assets/cb-22170/images/help/organizations/organization-security-tab.png)
  3. To display the "Security risk" view, in the sidebar, click 
  4. Use options in the page summary to filter results to show the repositories you want to assess. The list of repositories and metrics displayed on the page automatically update to match your current selection. For more information on filtering, see [Filtering alerts in security overview](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview).
     * Use the **Teams** dropdown to show information only for the repositories owned by one or more teams.
     * Click **NUMBER affected** or **NUMBER unaffected** in the header for any feature to show only the repositories with open alerts or no open alerts of that type.
     * Click any of the descriptions of "Open alerts" in the header to show only repositories with alerts of that type and category. For example, **1 critical** to show the repository with a critical alert for Dependabot.
     * At the top of the list of repositories, click **NUMBER Archived** to show only repositories that are archived.
     * Click in the search box to add further filters to the repositories displayed.
![Screenshot of the "Security risk" view for an organization. The options for filtering are outlined in dark orange.](https://docs.github.com/assets/cb-85068/images/help/security-overview/security-risk-view-highlights.png)
The set of unaffected repositories includes all repositories without open alerts and also any repositories where the security feature is not enabled.
  5. Optionally, use the sidebar on the left to explore alerts for a specific security feature in greater detail. On each page, you can use filters that are specific to that feature to refine your search. For more information about the available qualifiers, see [Filtering alerts in security overview](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview).
  6. Optionally, use the [Exporting data from security overview](https://docs.github.com/en/code-security/security-overview/exporting-data-from-security-overview).


The summary views ("Overview", "Coverage" and "Risk") show data only for default alerts. Secret scanning alerts for ignored directories and non-provider alerts are all omitted from these views. Consequently, the individual alert views may include a larger number of open and closed alerts.
## [Viewing enterprise-level security risks in code](https://docs.github.com/en/code-security/security-overview/assessing-code-security-risk#viewing-enterprise-level-security-risks-in-code)
You can view data for security alerts across organizations in an enterprise.
You can use the `owner` filter in the search field to filter the data by organization. For more information, see [Filtering alerts in security overview](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview#repository-owner-name-and-type-filters).
  1. Navigate to GitHub Enterprise Cloud.
  2. In the top-right corner of GitHub, click your profile photo, then click **Your enterprises**.
  3. In the list of enterprises, click the enterprise you want to view.
  4. On the left side of the page, in the enterprise account sidebar, click 
  5. To display the "Security risk" view, in the sidebar, click 
  6. Use options in the page summary to filter results to show the repositories you want to assess. The list of repositories and metrics displayed on the page automatically update to match your current selection. For more information on filtering, see [Filtering alerts in security overview](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview).
     * Use the **Teams** dropdown to show information only for the repositories owned by one or more teams.
     * Click **NUMBER affected** or **NUMBER unaffected** in the header for any feature to show only the repositories with open alerts or no open alerts of that type.
     * Click any of the descriptions of "Open alerts" in the header to show only repositories with alerts of that type and category. For example, **1 critical** to show the repository with a critical alert for Dependabot.
     * At the top of the list of repositories, click **NUMBER Archived** to show only repositories that are archived.
     * Click in the search box to add further filters to the repositories displayed.
![Screenshot of the "Security risk" view for an enterprise. The options for filtering are outlined in dark orange.](https://docs.github.com/assets/cb-101874/images/help/security-overview/security-risk-view-highlights-enterprise.png)
The set of unaffected repositories includes all repositories without open alerts and also any repositories where the security feature is not enabled.
  7. Optionally, use the sidebar on the left to explore alerts for a specific security feature in greater detail. On each page, you can use filters that are specific to that feature to refine your search. For more information about the available qualifiers, see [Filtering alerts in security overview](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview).
  8. Optionally, use the **Export CSV** button to download a CSV file of the data currently displayed on the page for security research and in-depth data analysis. For more information, see [Exporting data from security overview](https://docs.github.com/en/code-security/security-overview/exporting-data-from-security-overview).


The summary views ("Overview", "Coverage" and "Risk") show data only for default alerts. Secret scanning alerts for ignored directories and non-provider alerts are all omitted from these views. Consequently, the individual alert views may include a larger number of open and closed alerts.
## [Next steps](https://docs.github.com/en/code-security/security-overview/assessing-code-security-risk#next-steps)
When you have assessed your security risks, you are ready to create a security campaign to collaborate with developers to remediate alerts. For information about fixing security alerts at scale, see [Creating and managing security campaigns](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/creating-managing-security-campaigns) and [Best practices for fixing security alerts at scale](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/best-practice-fix-alerts-at-scale).
