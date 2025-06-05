  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Security overview](https://docs.github.com/en/code-security/security-overview "Security overview")/
  * [Assess adoption of features](https://docs.github.com/en/code-security/security-overview/assessing-adoption-code-security "Assess adoption of features")


# Assessing adoption of security features
You can use security overview to see which teams and repositories have already enabled features for secure coding, and identify any that are not yet protected.
## Who can use this feature?
Access requires:
  * Organization views: **write** access to repositories in the organization
  * Enterprise views: organization owners and security managers


Organizations owned by a GitHub Team account with GitHub Secret Protection or GitHub Code Security, or owned by a GitHub Enterprise account
## In this article
  * [About adoption of features for secure coding](https://docs.github.com/en/code-security/security-overview/assessing-adoption-code-security#about-adoption-of-features-for-secure-coding)
  * [Viewing the enablement of security features for an organization](https://docs.github.com/en/code-security/security-overview/assessing-adoption-code-security#viewing-the-enablement-of-security-features-for-an-organization)
  * [Viewing the enablement of features for secure coding in an enterprise](https://docs.github.com/en/code-security/security-overview/assessing-adoption-code-security#viewing-the-enablement-of-features-for-secure-coding-in-an-enterprise)
  * [Viewing enablement trends for an organization](https://docs.github.com/en/code-security/security-overview/assessing-adoption-code-security#viewing-enablement-trends-for-an-organization)
  * [Viewing enablement trends for an enterprise](https://docs.github.com/en/code-security/security-overview/assessing-adoption-code-security#viewing-enablement-trends-for-an-enterprise)
  * [Interpreting and acting on the enablement data](https://docs.github.com/en/code-security/security-overview/assessing-adoption-code-security#interpreting-and-acting-on-the-enablement-data)


## [About adoption of features for secure coding](https://docs.github.com/en/code-security/security-overview/assessing-adoption-code-security#about-adoption-of-features-for-secure-coding)
You can use security overview to see which repositories and teams have already enabled each security feature, and where people need more encouragement to adopt these features. The "Security coverage" view shows a summary and detailed information on feature enablement for an organization. You can filter the view to show a subset of repositories using the "enabled" and "not enabled" links, the "Teams" dropdown menu, and a search field in the page header.
![Screenshot of the header section of the "Security coverage" view on the "Security" tab for an organization.](https://docs.github.com/assets/cb-114980/images/help/security-overview/security-coverage-view-summary.png)
"Pull request alerts" are reported as enabled only when code scanning has analyzed at least one pull request since alerts were enabled for the repository.
You can download a CSV file of the data displayed on the "Security coverage" page. This data file can be used for efforts like security research and in-depth data analysis, and can integrate easily with external datasets. For more information, see [Exporting data from security overview](https://docs.github.com/en/code-security/security-overview/exporting-data-from-security-overview).
You can use the "Enablement trends" view to see enablement status and enablement status trends over time for Dependabot, code scanning, or secret scanning for repositories in an organization, or across organizations in an enterprise. For each of these features, you can view a graph visualizing the percentage of repositories that have the feature enabled, as well as a detailed table with enablement percentages for different points in time. For more information, see [Viewing enablement trends for an organization](https://docs.github.com/en/code-security/security-overview/assessing-adoption-code-security#viewing-enablement-trends-for-an-organization) and [Viewing enablement trends for an enterprise](https://docs.github.com/en/code-security/security-overview/assessing-adoption-code-security#viewing-enablement-trends-for-an-enterprise).
## [Viewing the enablement of security features for an organization](https://docs.github.com/en/code-security/security-overview/assessing-adoption-code-security#viewing-the-enablement-of-security-features-for-an-organization)
You can view data to assess the enablement of features for secure coding across repositories in an organization.
  1. On GitHub, navigate to the main page of the organization.
  2. Under your organization name, click 
![Screenshot of the horizontal navigation bar for an organization. A tab, labeled with a shield icon and "Security," is outlined in dark orange.](https://docs.github.com/assets/cb-22170/images/help/organizations/organization-security-tab.png)
  3. To display the "Security coverage" view, in the sidebar, click 
  4. Use options in the page summary to filter results to show the repositories you want to assess. The list of repositories and metrics displayed on the page automatically update to match your current selection. For more information on filtering, see [Filtering alerts in security overview](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview).
     * Use the **Teams** dropdown to show information only for the repositories owned by one or more teams. For more information, see [Managing team access to an organization repository](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-team-access-to-an-organization-repository).
     * Click **NUMBER enabled** or **NUMBER not enabled** in the header for any feature to show only the repositories with that feature enabled or not enabled.
     * At the top of the list of repositories, click **NUMBER Archived** to show only repositories that are archived.
     * Click in the search box to add further filters to the repositories displayed.


## [Viewing the enablement of features for secure coding in an enterprise](https://docs.github.com/en/code-security/security-overview/assessing-adoption-code-security#viewing-the-enablement-of-features-for-secure-coding-in-an-enterprise)
You can view data to assess the enablement of security features across organizations in an enterprise.
  1. Navigate to GitHub Enterprise Cloud.
  2. In the top-right corner of GitHub, click your profile photo, then click **Your enterprises**.
  3. In the list of enterprises, click the enterprise you want to view.
  4. On the left side of the page, in the enterprise account sidebar, click 
  5. To display the "Security coverage" view, in the sidebar, click **Coverage**.
  6. Use options in the page summary to filter results to show the repositories you want to assess. The list of repositories and metrics displayed on the page automatically update to match your current selection. For more information on filtering, see [Filtering alerts in security overview](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview).
     * Use the **Teams** dropdown to show information only for the repositories owned by one or more teams. For more information, see [Managing team access to an organization repository](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-team-access-to-an-organization-repository).
     * Click **NUMBER enabled** or **NUMBER not enabled** in the header for any feature to show only the repositories with that feature enabled or not enabled.
     * At the top of the list of repositories, click **NUMBER Archived** to show only repositories that are archived.
     * Click in the search box to add further filters to the repositories displayed.
You can use the `owner` filter in the search field to filter the data by organization. For more information, see [Filtering alerts in security overview](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview#repository-owner-name-and-type-filters).


## [Viewing enablement trends for an organization](https://docs.github.com/en/code-security/security-overview/assessing-adoption-code-security#viewing-enablement-trends-for-an-organization)
You can view data to assess the enablement status and enablement status trends of security features for an organization.
  1. On GitHub, navigate to the main page of the organization.
  2. Under your organization name, click 
![Screenshot of the horizontal navigation bar for an organization. A tab, labeled with a shield icon and "Security," is outlined in dark orange.](https://docs.github.com/assets/cb-22170/images/help/organizations/organization-security-tab.png)
  3. In the sidebar, under "Metrics", click 
  4. Click on one of the tabs for "Dependabot", "Code scanning", or "Secret scanning" to view enablement trends and the percentage of repositories in your organization with that feature enabled. This data is displayed as a graph and a detailed table.
  5. Optionally, use the options at the top of the "Enablement trends" view page to filter the group of repositories you want to see enablement trends for.
     * Use the date picker to set the time range that you want to view enablement trends for.
     * Click in the search box to add further filters on the enablement trends displayed. The filters you can apply are the same as those for the "Overview" dashboard view. For more information, see [Filtering alerts in security overview](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview).
![Screenshot of the "Enablement trends" view for an organization, showing Dependabot status and trends over 30 days, with a filter applied.](https://docs.github.com/assets/cb-101335/images/help/security-overview/security-overview-enablement-trends.png)


## [Viewing enablement trends for an enterprise](https://docs.github.com/en/code-security/security-overview/assessing-adoption-code-security#viewing-enablement-trends-for-an-enterprise)
You can view data to assess the enablement status and enablement status trends of security features across organizations in an enterprise.
  1. Navigate to GitHub Enterprise Cloud.
  2. In the top-right corner of GitHub, click your profile photo, then click **Your enterprises**.
  3. In the list of enterprises, click the enterprise you want to view.
  4. On the left side of the page, in the enterprise account sidebar, click 
  5. To display the "Enablement trends" view, in the sidebar, click **Enablement trends**.
  6. Click on one of the tabs for "Dependabot", "Code scanning", or "Secret scanning" to view enablement trends and the percentage of repositories across organizations in your enterprise with that feature enabled. This data is displayed as a graph and a detailed table.
  7. Optionally, use the options at the top of the "Enablement trends" view page to filter the group of repositories you want to see enablement trends for.
     * Use the date picker to set the time range that you want to view enablement trends for.
     * Click in the search box to add further filters on the enablement trends displayed. For more information, see [Filtering alerts in security overview](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview).


You can use the `owner:` filter in the search field to filter the data by organization. For more information, see [Filtering alerts in security overview](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview).
## [Interpreting and acting on the enablement data](https://docs.github.com/en/code-security/security-overview/assessing-adoption-code-security#interpreting-and-acting-on-the-enablement-data)
Some security features can and should be enabled on all repositories. For example, secret scanning alerts and push protection reduce the risk of a security leak no matter what information is stored in the repository. If you see repositories that don't already use these features, you should either enable them or discuss an enablement plan with the team who owns the repository. For information on enabling features for a whole organization, see [Enabling security features in your organization](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization).
Other features are not suitable for use in all repositories. For example, there would be no point in enabling Dependabot for repositories that only use ecosystems or languages that are unsupported. As such, it's normal to have some repositories where these features are not enabled.
Your enterprise may also have configured policies to limit the use of some security features. For more information, see [Enforcing policies for code security and analysis for your enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-code-security-and-analysis-for-your-enterprise).
