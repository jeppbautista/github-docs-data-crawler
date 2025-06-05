  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Security overview](https://docs.github.com/en/code-security/security-overview "Security overview")/
  * [View security insights](https://docs.github.com/en/code-security/security-overview/viewing-security-insights "View security insights")


# Viewing security insights
You can use the overview dashboard in security overview to monitor the security landscape of the repositories in your organization.
## Who can use this feature?
Access requires:
  * Organization views: **write** access to repositories in the organization
  * Enterprise views: organization owners and security managers


Organizations owned by a GitHub Team account with GitHub Secret Protection or GitHub Code Security, or owned by a GitHub Enterprise account
## In this article
  * [About organization-level security insights](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#about-organization-level-security-insights)
  * [Viewing the security overview dashboard](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#viewing-the-security-overview-dashboard)
  * [Understanding the overview dashboard](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#understanding-the-overview-dashboard)


## [About organization-level security insights](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#about-organization-level-security-insights)
The overview page in security overview is a consolidated dashboard of insights about your organization's security landscape and progress. You can use the dashboard to monitor the health of your application security program, collaborate with engineering teams, and gather data for benchmarking purposes.
You can view a variety of metrics about the security alerts in your organization. The dashboard displays trending data that tracks alert counts and activity over time, as well as snapshot data that reflects the current state.
The dashboard is divided into three tabs, each focused around a different security goal:
  * **Detection:** this tab shows metrics about the status and age of alerts in your organization, the secrets that have been blocked or bypassed, and the top repositories and vulnerabilities that pose the highest potential security risk.
  * **Remediation:** this tab shows metrics about how alerts are resolved and alert activity over time.
  * **Prevention:** this tab shows metrics about how vulnerabilities have been prevented and fixed.


Unlike the **Detection** and **Remediation** tabs which report alerts on the default branch, the **Prevention** tab gives you insights for CodeQL alerts found in merged pull requests.
You can filter the overview dashboard by selecting a specific time period, and apply additional filters to focus on narrower areas of interest. All data and metrics across the dashboard will change as you apply filters. By default, the dashboard displays all alerts from GitHub tools, but you can use the tool filter to show alerts from a specific tool (secret scanning, Dependabot, code scanning using CodeQL, a specific third-party tool) or all third-party code scanning tools. For more information, see [Filtering alerts in security overview](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview).
You can download a CSV file of the overview dashboard data for your organization or enterprise. This data file can integrate easily with external datasets, so you may find it useful for security research, data analysis, and more. For more information, see [Exporting data from security overview](https://docs.github.com/en/code-security/security-overview/exporting-data-from-security-overview).
The metrics you see will depend on your role and repository permissions. For more information, see [About security overview](https://docs.github.com/en/code-security/security-overview/about-security-overview#permission-to-view-data-in-security-overview).
If you're interested in assessing your organization's exposure to secret leaks specifically, you can run a free secret risk assessment on GitHub. The resulting report gives you aggregate insights on public leaks, private exposures, and token types, as well as provides you with actionable steps to strengthen your security and protect your code. See [About the secret risk assessment](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/about-secret-risk-assessment).
### [Limitations](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#limitations)
The data that populates the overview page can and will change over time due to various factors, such as repository deletion or modifications to a security advisory. This means that the overview metrics for the same time period could vary if viewed at two different times. For compliance reports or other scenarios where data consistency is crucial, we recommend that you source data from the audit log. For more information, see [Auditing security alerts](https://docs.github.com/en/code-security/getting-started/auditing-security-alerts).
Keep in mind that the overview page tracks changes over time for security alert data only. If you filter the page by non-alert attributes, such as repository status, the data you see will reflect the current state of those attributes, instead of the historical state. For example, consider that you archived a repository that contains open security alerts, an action which closes the alerts. If you then view the overview page for the week before you archived the repository, the alert data for the repository will only appear when you filter to show data from archived repositories, because the current state of the repository is archived. However, the alerts will appear as open, since they were open during that time period and the overview page tracks the historical state of alerts.
The summary views ("Overview", "Coverage" and "Risk") show data only for default alerts. Secret scanning alerts for ignored directories and non-provider alerts are all omitted from these views. Consequently, the individual alert views may include a larger number of open and closed alerts.
## [Viewing the security overview dashboard](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#viewing-the-security-overview-dashboard)
  1. On GitHub, navigate to the main page of the organization.
  2. Under your organization name, click 
![Screenshot of the horizontal navigation bar for an organization. A tab, labeled with a shield icon and "Security," is outlined in dark orange.](https://docs.github.com/assets/cb-22170/images/help/organizations/organization-security-tab.png)
  3. The overview page is the primary view that you will see after clicking on the "Security" tab. To get to the dashboard from another security overview page, in the sidebar, click 
  4. By default, the **Detection** tab is displayed. If you want to switch to another tab to see other metrics, click **Remediation** or **Prevention**.
  5. Use the options at the top of the overview page to filter the group of alerts you want to see metrics for. All of the data and metrics on the page will change as you adjust the filters.
     * Use the date picker to set the time range that you want to view alert activity and metrics for.
     * Click in the search box to add further filters on the alerts and metrics displayed.
![Screenshot of the overview page in security overview. Filtering options are outlined in dark orange, including the date picker and search field.](https://docs.github.com/assets/cb-155037/images/help/security-overview/security-overview-dashboard-filters-3-tab.png)


## [Understanding the overview dashboard](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#understanding-the-overview-dashboard)
  * [Detection tab](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#detection-tab)
  * [Remediation tab](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#remediation-tab)
  * [Prevention tab](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#prevention-tab)


Some metrics in the security overview dashboard include a trend indicator, which shows the percentage gain or loss for the chosen time period relative to previous period. For example, when you select a week with 10 alerts, if the previous week had 20 alerts, the trend indicator reports that the metric has dropped by 50%. If the average age of the open alerts is 15 days, and for the previous period it was 5 days, the trend indicator reports that the metric has risen by 200%.
The number of alerts shown on the security overview dashboard may not match the number of code scanning alerts. The security overview dashboard focuses on the security landscape of your organization, and only includes alerts with a security severity ("Critical", "High", "Medium", or "Low"), but CodeQL and third-party tools may separately produce non-security alerts with a level of "Error", "Warning", or "Note". For more information about alert severity and security severity levels in code scanning, see [About code scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts#about-alert-severity-and-security-severity-levels).
### [Detection tab](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#detection-tab)
  * [Open alerts over time](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#open-alerts-over-time)
  * [Age of alerts](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#age-of-alerts)
  * [Reopened alerts](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#reopened-alerts)
  * [Secrets bypassed or blocked](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#secrets-bypassed-or-blocked)
  * [Impact analysis table](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#impact-analysis-table)


#### [Open alerts over time](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#open-alerts-over-time)
The "Open alerts over time" graph shows the change in the number of open alerts in your organization or enterprise over the time period you have chosen. By default, alerts are grouped by severity. You can change the way alerts are grouped.
Open alerts include both newly created and existing open security alerts. New alerts are represented on their creation date, while alerts that existed before the chosen time period are represented at the start of the period. Once an alert is remediated or dismissed, it is not included in the graph. Instead, the alert will move to the closed alerts graph.
#### [Age of alerts](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#age-of-alerts)
The "Age of alerts" metric is the average age of all alerts that are still open at the end of the chosen time period.
The age of each open alert is calculated by subtracting the date the alert was created from the date that the chosen time period ends. For reopened alerts, the age is calculated by subtracting the original created date rather than the date the alert was reopened.
#### [Reopened alerts](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#reopened-alerts)
The "Reopened alerts" metric is the total open alerts that were reopened during the chosen time period. Only alerts that are open at the end of the reporting period are reported. This includes:
  * Alerts that were closed as of the day before the chosen time period, and that remain open at the end of the period.
  * Newly created alerts that were closed, and then reopened, during the chosen time period.
  * Alerts that were open at the start of the chosen time period, but closed and then reopened within the same period.


#### [Secrets bypassed or blocked](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#secrets-bypassed-or-blocked)
The "Secrets bypassed" metric shows the ratio of secrets bypassed to the total secrets blocked by push protection.
You can also see how many secrets were successfully blocked, which is calculated by subtracting the number of secrets bypassed from the total number of secrets blocked by push protection. A secret is considered to have been successfully blocked when it has been corrected, and not committed to the repository.
You can click **View details** to view the secret scanning report with the same filters and time period selected.
For more information on secret scanning push protection metrics, see [Viewing metrics for secret scanning push protection](https://docs.github.com/en/code-security/security-overview/viewing-metrics-for-secret-scanning-push-protection).
#### [Impact analysis table](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#impact-analysis-table)
The impact analysis table has separate tabs showing data for: "Repositories", "Advisories", and "SAST vulnerabilities".
  * The "Repositories" tab shows the top 10 repositories with the most open alerts at the end of the chosen time period, ranked by the total number of open alerts. For each repository, the total number of open alerts is shown alongside a breakdown by severity.
  * The "Advisories" tab shows the 10 CVE advisories that triggered the most Dependabot alerts at the end of the chosen time period, ranked by the total number of open alerts. For each advisory, the total number of open alerts is shown alongside a severity rating.
  * The "SAST vulnerabilities" tab shows the 10 static application security testing (SAST) vulnerabilities that triggered the most code scanning alerts, ranked by the total number of open alerts. For each vulnerability, the total number of open alerts is shown alongside a severity rating.


### [Remediation tab](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#remediation-tab)
  * [Closed alerts over time](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#closed-alerts-over-time)
  * [Mean time to remediate](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#mean-time-to-remediate)
  * [Net resolve rate](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#net-resolve-rate)
  * [Alert activity graph](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#alert-activity-graph)


#### [Closed alerts over time](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#closed-alerts-over-time)
The "Closed alerts over time" graph shows the change in the number of closed alerts in your organization or enterprise over the time period you have chosen. By default, alerts are grouped by severity. You can change the way alerts are grouped.
Closed alerts include security alerts that have been successfully remediated or dismissed prior to or during the chosen time period. Alerts closed during the time period are represented on the graph on their closed date, while alerts remediated or dismissed before the chosen time period are represented at the start of the period.
#### [Mean time to remediate](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#mean-time-to-remediate)
The "Mean time to remediate" metric is the average age of all alerts that were remediated or dismissed in the chosen time period. Alerts that were closed as "false positive" are excluded.
The age of each closed alert is calculated by subtracting the date the alert was created from the date that the alert was last closed during the chosen time period. For reopened alerts, the age is calculated by subtracting the original created date rather than the date the alert was reopened.
#### [Net resolve rate](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#net-resolve-rate)
The "Net resolve rate" metric is the rate at which alerts are being closed. This metric is similar to measuring "developer velocity", reflecting the speed and efficiency with which alerts are resolved.
The rate is calculated by dividing the number of alerts that were closed and remained closed during the chosen time period, by the number of alerts created during the time period.
The net resolve rate takes into account any new and any closed alerts during the chosen time period. This means that the set of new alerts and set of closed alerts used for the calculation do not necessarily correspond, since they may represent different populations of alerts.
Alerts that are reopened and re-closed during the chosen time period are ignored.
#### [Alert activity graph](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#alert-activity-graph)
Expanding on the alert trends graph, the alert activity graph shows you alert inflows and outflows over your chosen time period.
Green bars represent the number of new alerts created during the segmented time period. Purple bars represent the number of alerts that were closed during the segmented time period. The blue dotted line represents the net alert activity, which is the difference between new and closed alerts.
### [Prevention tab](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#prevention-tab)
Unlike the **Detection** and **Remediation** tabs which report alerts on the default branch, the **Prevention** tab gives you insights for CodeQL alerts found in merged pull requests.
  * [Introduced versus prevented](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#introduced-versus-prevented)
  * [Vulnerabilities fixed in pull requests](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#vulnerabilities-fixed-in-pull-requests)
  * [Copilot Autofix suggestions](https://docs.github.com/en/code-security/security-overview/viewing-security-insights##pull-request-alerts-fixed-with-copilot-autofix-suggestions)


#### [Introduced versus prevented](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#introduced-versus-prevented)
The "Introduced versus Prevented" graph shows the cumulative number of vulnerabilities that were caught in the developer workflow versus the vulnerabilities introduced in your organization or enterprise over the time period you have chosen. Prevented vulnerabilities are defined as the count of pull request alerts detected by CodeQL that have been fixed for merged pull requests. Introduced vulnerabilities are the count of new pull request alerts detected by CodeQL that were dismissed as "Risk accepted" or were unresolved at the time the pull request was merged.
The dates for prevented alerts are based on the date the alerts were fixed, and the dates for introduced alerts are based on the date the alerts were created.
#### [Vulnerabilities fixed in pull requests](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#vulnerabilities-fixed-in-pull-requests)
The "Vulnerabilities fixed in pull requests" metric shows the count of pull request alerts detected by CodeQL or secret scanning with a close reason of "Fixed" that are tied to a merged pull request.
#### [Pull request alerts fixed with Copilot Autofix suggestions](https://docs.github.com/en/code-security/security-overview/viewing-security-insights#pull-request-alerts-fixed-with-copilot-autofix-suggestions)
GitHub Copilot Autofix for code scanning is an expansion of code scanning that provides you with targeted recommendations to help you fix code scanning alerts. For more information, see [Responsible use of Copilot Autofix for code scanning](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/responsible-use-autofix-code-scanning).
The "Pull request alerts fixed with autofix suggestions" metric shows the ratio of accepted Copilot Autofix suggestions to the total number of Copilot Autofix suggestions on pull request alerts detected by code scanning.
