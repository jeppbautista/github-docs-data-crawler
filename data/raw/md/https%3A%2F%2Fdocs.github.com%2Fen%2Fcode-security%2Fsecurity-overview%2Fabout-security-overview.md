  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Security overview](https://docs.github.com/en/code-security/security-overview "Security overview")/
  * [About security overview](https://docs.github.com/en/code-security/security-overview/about-security-overview "About security overview")


# About security overview
You can gain insights into the overall security landscape of your organization or enterprise and identify repositories that require intervention using security overview.
## Who can use this feature?
Secret risk assessment is available for all organizations owned by GitHub Team or GitHub Enterprise. Additional views are available for:
  * Organizations owned by a GitHub Team account with GitHub Secret Protection or GitHub Code Security
  * Organizations owned by a GitHub Enterprise account


## In this article
  * [About the views](https://docs.github.com/en/code-security/security-overview/about-security-overview#about-the-views)
  * [About security overview for organizations](https://docs.github.com/en/code-security/security-overview/about-security-overview#about-security-overview-for-organizations)
  * [About security overview for enterprises](https://docs.github.com/en/code-security/security-overview/about-security-overview#about-security-overview-for-enterprises)
  * [Permission to view data in security overview](https://docs.github.com/en/code-security/security-overview/about-security-overview#permission-to-view-data-in-security-overview)
  * [Further reading](https://docs.github.com/en/code-security/security-overview/about-security-overview#further-reading)


Security overview provides insights into the security of code stored in repositories in your organization.
  * **All organizations** on GitHub Team can use the free **secret risk assessment** to evaluate the exposure of their organization to leaked secrets, see [Viewing the secret risk assessment report for your organization](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/viewing-the-secret-risk-assessment-report-for-your-organization).
  * GitHub Team accounts that purchase **GitHub Secret Protection or GitHub Code Security** have access to views with additional insights.


The information below describes the views available to organizations with GitHub Secret Protection or GitHub Code Security that you can use to identify trends in detection, remediation, and prevention of security alerts and dig deep into the current state of your repositories.
## [About the views](https://docs.github.com/en/code-security/security-overview/about-security-overview#about-the-views)
All views show information and metrics for the **default** branches of the repositories you have permission to view in an organization or enterprise.
The views are interactive with filters that allow you to look at the aggregated data in detail and identify sources of high risk, see security trends, and see the impact of pull request analysis on blocking security vulnerabilities entering your code. As you apply multiple filters to focus on narrower areas of interest, all data and metrics across the view change to reflect your current selection. For more information, see [Filtering alerts in security overview](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview).
From security overview, you can download comma-separated values (CSV) files containing data from several pages of your organization or enterprise's security overview. These files can be used for efforts like security research and in-depth data analysis, and can integrate easily with external datasets. For more information, see [Exporting data from security overview](https://docs.github.com/en/code-security/security-overview/exporting-data-from-security-overview).
There are dedicated views for each type of security alert. You can limit your analysis to a specific type of alert, and then narrow the results further with a range of filters specific to each view. For example, in the secret scanning alert view, you can use the "Secret type" filter to view only secret scanning alerts for a specific secret, like a GitHub personal access token.
Security overview displays active alerts raised by security features. If there are no alerts shown in security overview for a repository, undetected security vulnerabilities or code errors may still exist or the feature may not be enabled for that repository.
## [About security overview for organizations](https://docs.github.com/en/code-security/security-overview/about-security-overview#about-security-overview-for-organizations)
The application security team at your company can use the different views for both broad and specific analyses of your organization's security status. For example, the team can use the "Overview" dashboard view to track your organization's security landscape and progression.
You can find security overview on the **Security** tab for any organization. Each view shows a summary of the data that you have access to. As you add filters, all data and metrics across the view change to reflect the repositories or alerts that you've selected. For information about permissions, see [Permission to view data in security overview](https://docs.github.com/en/code-security/security-overview/about-security-overview#permission-to-view-data-in-security-overview).
Security overview has multiple views that provide different ways to explore enablement and alert data.
  * **Overview:** visualize trends in **Detection** , **Remediation** , and **Prevention** of security alerts, see [Viewing security insights](https://docs.github.com/en/code-security/security-overview/viewing-security-insights).
  * **Risk and Alert views:** explore the risk from security alerts of all types or focus on a single alert type and identify your risk from specific vulnerable dependencies, code weaknesses, or leaked secrets, see [Assessing the security risk of your code](https://docs.github.com/en/code-security/security-overview/assessing-code-security-risk).
  * **Coverage:** assess the adoption of security features across repositories in the organization, see [Assessing adoption of security features](https://docs.github.com/en/code-security/security-overview/assessing-adoption-code-security).
  * **Assessments:** regardless of the enablement status of Advanced Security features, organizations on GitHub Team and GitHub Enterprise can run a free report to scan the code in the organization for leaked secrets, see [About the secret risk assessment](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/about-secret-risk-assessment).
  * **Enablement trends:** see how quickly different teams are adopting security features.
  * **CodeQL pull request alerts:** assess the impact of running CodeQL on pull requests and how development teams are resolving code scanning alerts, see [Viewing metrics for pull request alerts](https://docs.github.com/en/code-security/security-overview/viewing-metrics-for-pull-request-alerts).
  * **Secret scanning:** find out which types of secret are blocked by push protection and which teams are bypassing push protection, see [Viewing metrics for secret scanning push protection](https://docs.github.com/en/code-security/security-overview/viewing-metrics-for-secret-scanning-push-protection) and [Reviewing requests to bypass push protection](https://docs.github.com/en/code-security/security-overview/reviewing-requests-to-bypass-push-protection).


You also create and manage security campaigns to remediate alerts from security overview, see [Creating and managing security campaigns](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/creating-managing-security-campaigns) and [Best practices for fixing security alerts at scale](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/best-practice-fix-alerts-at-scale).
## [About security overview for enterprises](https://docs.github.com/en/code-security/security-overview/about-security-overview#about-security-overview-for-enterprises)
You can find security overview on the **Security** tab for your enterprise. Each page displays aggregated and repository-specific security information for your enterprise.
As with security overview for organizations, security overview for enterprises has multiple views that provide different ways to explore data.
For information about permissions, see [Permission to view data in security overview](https://docs.github.com/en/code-security/security-overview/about-security-overview#permission-to-view-data-in-security-overview).
## [Permission to view data in security overview](https://docs.github.com/en/code-security/security-overview/about-security-overview#permission-to-view-data-in-security-overview)
### [Organization-level overview](https://docs.github.com/en/code-security/security-overview/about-security-overview#organization-level-overview)
If you are an **owner or security manager** for an organization, you can see data for all the repositories in the organization in all views.
If you are an **organization or team member** , you can view security overview for the organization and see data for repositories where you have an appropriate level of access.
The Assessments view, which is not shown in the table below, is only available to organization owners and security managers.
Organization or team member with | Overview dashboard view | Risk and alerts views | Coverage view  
---|---|---|---  
`admin` access for one or more repositories | View data for those repositories | View data for those repositories | View data for those repositories  
`write` access for one or more repositories | View code scanning and Dependabot data for those repositories | View code scanning and Dependabot data for those repositories | No access  
`read` or `triage` access for one or more repositories | No access | No access | No access  
Security alert access for one or more repositories | View all security alert data for those repositories | View all security alert data for those repositories | No access  
Custom organization role with permission to view one or more types of security alert | View allowed alert data for all repositories | View allowed alert data for all repositories in all views | No access  
To ensure a consistent and responsive experience, for organization members, the organization-level security overview pages will only display results from the most recently updated 3,000 repositories. If your results have been restricted, a notification will appear at the top of the page. Organization owners and security managers will see results from all repositories.
For more information about access to security alerts and related views, see [Managing security and analysis settings for your repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-security-and-analysis-settings-for-your-repository#granting-access-to-security-alerts) and [About custom repository roles](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/about-custom-repository-roles#security).
### [Enterprise-level overview](https://docs.github.com/en/code-security/security-overview/about-security-overview#enterprise-level-overview)
If you are an **enterprise owner** , you will need to join an organization as an organization owner to view data for the organization's repositories in both the organization-level and enterprise-level overview. For more information, see [Managing your role in an organization owned by your enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/user-management/managing-organizations-in-your-enterprise/managing-your-role-in-an-organization-owned-by-your-enterprise).
In the enterprise-level security overview, you can see data for all organizations where you are an **organization owner or security manager**.
## [Further reading](https://docs.github.com/en/code-security/security-overview/about-security-overview#further-reading)
  * [Quickstart for securing your repository](https://docs.github.com/en/code-security/getting-started/securing-your-repository)
  * [Securing your organization](https://docs.github.com/en/code-security/securing-your-organization)
  * [Introduction to adopting GitHub Advanced Security at scale](https://docs.github.com/en/code-security/adopting-github-advanced-security-at-scale/introduction-to-adopting-github-advanced-security-at-scale)


