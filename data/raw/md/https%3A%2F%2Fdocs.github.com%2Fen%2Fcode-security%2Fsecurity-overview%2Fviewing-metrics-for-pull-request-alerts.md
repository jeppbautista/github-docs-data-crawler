  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Security overview](https://docs.github.com/en/code-security/security-overview "Security overview")/
  * [View PR alert metrics](https://docs.github.com/en/code-security/security-overview/viewing-metrics-for-pull-request-alerts "View PR alert metrics")


# Viewing metrics for pull request alerts
You can use security overview to see how CodeQL is performing in pull requests for repositories across your organizations, and to identify repositories where you may need to take action.
## Who can use this feature?
Access requires:
  * Organization views: **write** access to repositories in the organization
  * Enterprise views: organization owners and security managers


Organizations owned by a GitHub Team account with GitHub Code Security, or owned by a GitHub Enterprise account
## In this article
  * [About CodeQL pull request alerts metrics](https://docs.github.com/en/code-security/security-overview/viewing-metrics-for-pull-request-alerts#about-codeql-pull-request-alerts-metrics)
  * [Viewing CodeQL pull request alerts metrics for an organization](https://docs.github.com/en/code-security/security-overview/viewing-metrics-for-pull-request-alerts#viewing-codeql-pull-request-alerts-metrics-for-an-organization)
  * [Viewing CodeQL pull request alerts metrics for your enterprise](https://docs.github.com/en/code-security/security-overview/viewing-metrics-for-pull-request-alerts#viewing-codeql-pull-request-alerts-metrics-for-your-enterprise)


## [About CodeQL pull request alerts metrics](https://docs.github.com/en/code-security/security-overview/viewing-metrics-for-pull-request-alerts#about-codeql-pull-request-alerts-metrics)
The metrics overview for CodeQL pull request alerts helps you to understand how well CodeQL is preventing vulnerabilities in your organizations. You can use the metrics to assess how CodeQL is performing in pull requests, and to easily identify the repositories where you may need to take action in order to identify and reduce security risks.
The overview shows you a summary of how many vulnerabilities prevented by CodeQL have been caught in pull requests. The metrics are only tracked for pull requests that have been merged into the default branches of repositories in your organizations.
You can also find more granular metrics, such as how many alerts were fixed with and without Copilot Autofix suggestions, how many were unresolved and merged, and how many were dismissed as false positive or as risk accepted.
You can also view:
  * The rules that are causing the most alerts, and how many alerts each rule is associated with.
  * The number of alerts that were merged into the default branch without resolution, and the number of alerts dismissed as an acceptable risk.
  * The number of alerts that were fixed with an accepted Copilot Autofix suggestion, displayed as a fraction of how many total Copilot Autofix suggestions were available.
  * Remediation rates, in a graph showing the percentage of alerts that were remediated with an available Copilot Autofix suggestion, and the percentage of alerts that were remediated without a Copilot Autofix suggestion.


You can apply filters to the data. The metrics are based on activity from the default period or your selected period.
Metrics for Copilot Autofix will be shown only for repositories where Copilot Autofix is enabled.
## [Viewing CodeQL pull request alerts metrics for an organization](https://docs.github.com/en/code-security/security-overview/viewing-metrics-for-pull-request-alerts#viewing-codeql-pull-request-alerts-metrics-for-an-organization)
  1. On GitHub, navigate to the main page of the organization.
  2. Under your organization name, click 
![Screenshot of the horizontal navigation bar for an organization. A tab, labeled with a shield icon and "Security," is outlined in dark orange.](https://docs.github.com/assets/cb-22170/images/help/organizations/organization-security-tab.png)
  3. In the sidebar, under "Metrics", click 
  4. Optionally, use the date picker to set the time range. The date picker will show data based on the pull request alerts' creation dates.
  5. Optionally, apply filters in the search box at the top of the page.
  6. Alternatively, you can open the advanced filter dialog:
     * At the top of the page, next to the search box, click 
     * Click 
     * To search for repositories matching the selected filter, fill out the available fields for that filter, then click **Apply**. You can repeat this process to add as many filters as you would like to your search.
     * Optionally, to remove a filter from your search, click **Apply**.
  7. You can use the [Exporting data from security overview](https://docs.github.com/en/code-security/security-overview/exporting-data-from-security-overview).


## [Viewing CodeQL pull request alerts metrics for your enterprise](https://docs.github.com/en/code-security/security-overview/viewing-metrics-for-pull-request-alerts#viewing-codeql-pull-request-alerts-metrics-for-your-enterprise)
You can also view metrics for CodeQL alerts in pull requests across organizations in your enterprise.
  1. Navigate to GitHub Enterprise Cloud.
  2. In the top-right corner of GitHub, click your profile photo, then click **Your enterprises**.
  3. In the list of enterprises, click the enterprise you want to view.
  4. On the left side of the page, in the enterprise account sidebar, click 
  5. In the sidebar, under "Metrics", click 


You can use the `owner` filter in the search field to filter the data by organization. For more information, see [Filtering alerts in security overview](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview#repository-owner-name-and-type-filters).
