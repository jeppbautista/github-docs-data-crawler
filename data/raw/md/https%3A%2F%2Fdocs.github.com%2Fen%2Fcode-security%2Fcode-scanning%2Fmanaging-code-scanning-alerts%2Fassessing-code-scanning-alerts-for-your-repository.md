  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Manage alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts "Manage alerts")/
  * [Assess alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository "Assess alerts")


# Assessing code scanning alerts for your repository
From the security view, you can explore and evaluate alerts for potential vulnerabilities or errors in your project's code.
## Who can use this feature?
Users with **write** access
## In this article
  * [Viewing the alerts for a repository](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository#viewing-the-alerts-for-a-repository)
  * [Viewing metrics for CodeQL pull request alerts for an organization](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository#viewing-metrics-for-codeql-pull-request-alerts-for-an-organization)
  * [Filtering code scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository#filtering-code-scanning-alerts)
  * [Searching code scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository#searching-code-scanning-alerts)
  * [Auditing responses to code scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository#auditing-responses-to-code-scanning-alerts)
  * [Further reading](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository#further-reading)


Anyone with read permission for a repository can see code scanning annotations on pull requests. For more information, see [Triaging code scanning alerts in pull requests](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/triaging-code-scanning-alerts-in-pull-requests).
## [Viewing the alerts for a repository](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository#viewing-the-alerts-for-a-repository)
You need write permission to view a summary of all the alerts for a repository on the **Security** tab.
By default, the code scanning alerts page is filtered to show alerts for the default branch of the repository only.
  1. On GitHub, navigate to the main page of the repository.
  2. Under the repository name, click **Security**. 
![Screenshot of a repository header showing the tabs. The "Security" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-17801/images/help/repository/security-tab.png)
  3. In the left sidebar, click 
  4. Optionally, use the free text search box or the dropdown menus to filter alerts. For example, you can filter by the tool that was used to identify alerts.
![Screenshot of code scanning alerts page. The search box and filter dropdown menus are outlined in dark orange.](https://docs.github.com/assets/cb-49053/images/help/repository/filter-code-scanning-alerts.png)
  5. Under "Code scanning," click the alert you'd like to explore to display the detailed alert page. The status and details on the alert page only reflect the state of the alert on the default branch of the repository, even if the alert exists in other branches. You can see the status of the alert on non-default branches in the **Affected branches** section on the right-hand side of the alert page. If an alert doesn't exist in the default branch, the status of the alert will display as "in pull request" or "in branch" and will be colored grey. The **Development** section shows linked branches and pull requests that will fix the alert.
  6. Optionally, if the alert highlights a problem with data flow, click **Show paths** to display the path from the data source to the sink where it's used.
![Screenshot of a code scanning alert. The "Show paths" and "Show more" links are outlined in dark orange.](https://docs.github.com/assets/cb-107683/images/help/repository/code-scanning-alert-details.png)
  7. Alerts from CodeQL analysis include a description of the problem. Click **Show more** for guidance on how to fix your code.


For more information, see [About code scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts).
You can see information about when code scanning analysis last ran on the tool status page. For more information, see [About the tool status page for code scanning](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/about-the-tool-status-page).
## [Viewing metrics for CodeQL pull request alerts for an organization](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository#viewing-metrics-for-codeql-pull-request-alerts-for-an-organization)
For code scanning alerts from CodeQL analysis, you can use security overview to see how CodeQL is performing in pull requests in repositories where you have write access across your organization, and to identify repositories where you may need to take action. For more information, see [Viewing metrics for pull request alerts](https://docs.github.com/en/code-security/security-overview/viewing-metrics-for-pull-request-alerts).
## [Filtering code scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository#filtering-code-scanning-alerts)
You can filter the alerts shown in the code scanning alerts view. This is useful if there are many alerts as you can focus on a particular type of alert. There are some predefined filters and a range of keywords that you can use to refine the list of alerts displayed.
When you select a keyword from either a drop-down list, or as you enter a keyword in the search field, only values with results are shown. This makes it easier to avoid setting filters that find no results.
![Screenshot of search field in alerts view. The field has "branch:dependabot" and all valid branches with a matching name are shown.](https://docs.github.com/assets/cb-82053/images/help/repository/code-scanning-filter-keywords.png)
If you enter multiple filters, the view will show alerts matching _all_ these filters. For example, `is:closed severity:high branch:main` will only display closed high-severity alerts that are present on the `main` branch. The exception is filters relating to refs (`ref`, `branch` and `pr`): `is:open branch:main branch:next` will show you open alerts from both the `main` branch and the `next` branch.
Please note that if you have filtered for alerts on a non-default branch, but the same alerts exist on the default branch, the alert page for any given alert will still only reflect the alert's status on the default branch, even if that status conflicts with the status on a non-default branch. For example, an alert that appears in the "Open" list in the summary of alerts for `branch-x` could show a status of "Fixed" on the alert page, if the alert is already fixed on the default branch. You can view the status of the alert for the branch you filtered on in the **Affected branches** section on the right side of the alert page.
You can prefix the `tag` filter with `-` to exclude results with that tag. For example, `-tag:style` only shows alerts that do not have the `style` tag.
### [Restricting results to application code only](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository#restricting-results-to-application-code-only)
You can use the "Only alerts in application code" filter or `autofilter:true` keyword and value to restrict results to alerts in application code. For more information about the types of code that are automatically labeled as not application code, see [About code scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts#about-labels-for-alerts-that-are-not-found-in-application-code).
## [Searching code scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository#searching-code-scanning-alerts)
You can search the list of alerts. This is useful if there is a large number of alerts in your repository, or if you don't know the exact name for an alert for example. GitHub performs the free text search across:
  * The name of the alert
  * The alert details (this also includes the information hidden from view by default in the **Show more** collapsible section)

Supported search | Syntax example | Results  
---|---|---  
Single word search | `injection` | Returns all the alerts containing the word `injection`  
Multiple word search | `sql injection` | Returns all the alerts containing `sql` or `injection`  
Exact match search  
(use double quotes) | `"sql injection"` | Returns all the alerts containing the exact phrase `sql injection`  
OR search | `sql OR injection` | Returns all the alerts containing `sql` or `injection`  
AND search | `sql AND injection` | Returns all the alerts containing both words `sql` and `injection`  
  * The multiple word search is equivalent to an OR search.
  * The AND search will return results where the search terms are found _anywhere_ , in any order in the alert name or details.


  1. On GitHub, navigate to the main page of the repository.
  2. Under the repository name, click **Security**. 
![Screenshot of a repository header showing the tabs. The "Security" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-17801/images/help/repository/security-tab.png)
  3. In the left sidebar, click 
  4. To the right of the **Filters** drop-down menus, type the keywords to search for in the free text search box. 
![Screenshot of search field in alerts view. The field has pre-defined filters "is: open branch:main" and free text of "sql or injection" highlighted.](https://docs.github.com/assets/cb-33017/images/help/repository/code-scanning-search-alerts.png)
  5. Press `return`. The alert listing will contain the open code scanning alerts matching your search criteria.


## [Auditing responses to code scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository#auditing-responses-to-code-scanning-alerts)
You can audit the actions taken in response to code scanning alerts using GitHub tools. For more information, see [Auditing security alerts](https://docs.github.com/en/code-security/getting-started/auditing-security-alerts).
## [Further reading](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository#further-reading)
  * [Resolving code scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/resolving-code-scanning-alerts)
  * [Triaging code scanning alerts in pull requests](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/triaging-code-scanning-alerts-in-pull-requests)
  * [Configuring default setup for code scanning](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning)
  * [About integration with code scanning](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/about-integration-with-code-scanning)


