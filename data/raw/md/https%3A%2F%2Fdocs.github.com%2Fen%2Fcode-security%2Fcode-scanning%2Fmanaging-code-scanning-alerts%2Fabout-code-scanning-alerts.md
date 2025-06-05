  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Manage alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts "Manage alerts")/
  * [About code scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts "About code scanning alerts")


# About code scanning alerts
Learn about the different types of code scanning alerts and the information that helps you understand the problem each alert highlights.
## Who can use this feature?
Users with **write** access
Code scanning is available for the following repository types:
  * Public repositories on GitHub.com
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [About alerts from code scanning](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts#about-alerts-from-code-scanning)
  * [About alert details](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts#about-alert-details)
  * [About alert severity and security severity levels](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts#about-alert-severity-and-security-severity-levels)


## [About alerts from code scanning](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts#about-alerts-from-code-scanning)
You can configure code scanning to check the code in a repository using the default CodeQL analysis, a third-party analysis, or multiple types of analysis. When the analysis is complete, the resulting alerts are displayed alongside each other in the security view of the repository. Results from third-party tools or from custom queries may not include all of the properties that you see for alerts detected by GitHub's default CodeQL analysis. For more information, see [Configuring default setup for code scanning](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning) and [Configuring advanced setup for code scanning](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning).
By default, code scanning analyzes your code periodically on the default branch and during pull requests. For information about managing alerts on a pull request, see [Triaging code scanning alerts in pull requests](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/triaging-code-scanning-alerts-in-pull-requests).
You can use GitHub Copilot Autofix to generate fixes automatically for code scanning alerts, including CodeQL alerts. For more information, see [Resolving code scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/resolving-code-scanning-alerts#generating-suggested-fixes-for-code-scanning-alerts).
For code scanning alerts from CodeQL analysis, you can use security overview to see how CodeQL is performing in pull requests in repositories across your organization, and to identify repositories where you may need to take action. For more information, see [Viewing metrics for pull request alerts](https://docs.github.com/en/code-security/security-overview/viewing-metrics-for-pull-request-alerts).
You can audit the actions taken in response to code scanning alerts using GitHub tools. For more information, see [Auditing security alerts](https://docs.github.com/en/code-security/getting-started/auditing-security-alerts).
## [About alert details](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts#about-alert-details)
Each alert highlights a problem with the code and the name of the tool that identified it. You can see the line of code that triggered the alert, as well as properties of the alert, such as the alert severity, security severity, and the nature of the problem. Alerts also tell you when the issue was first introduced. For alerts identified by CodeQL analysis, you will also see information on how to fix the problem.
The status and details on the alert page only reflect the state of the alert on the default branch of the repository, even if the alert exists in other branches. You can see the status of the alert on non-default branches in the **Affected branches** section on the right-hand side of the alert page. If an alert doesn't exist in the default branch, the status of the alert will display as "in pull request" or "in branch" and will be colored grey. The **Development** section shows linked branches and pull requests that will fix the alert.
![Screenshot of a code scanning alert, includes the alert title, relevant lines of code at the left, metadata at the right.](https://docs.github.com/assets/cb-235019/images/help/repository/code-scanning-alert.png)
You can also view affected branches, as well as fixes and associated pull requests for an alert. This helps you and your team stay informed about the progress of fixing alerts.
![Screenshot of the "Development" section of a code scanning alert, includes a title of a pull request that could fix the alert.](https://docs.github.com/assets/cb-63041/images/help/repository/code-scanning-alert-development-section.png)
If you configure code scanning using CodeQL, you can also find data-flow problems in your code. Data-flow analysis finds potential security issues in code, such as: using data insecurely, passing dangerous arguments to functions, and leaking sensitive information.
When code scanning reports data-flow alerts, GitHub shows you how data moves through the code. Code scanning allows you to identify the areas of your code that leak sensitive information, and that could be the entry point for attacks by malicious users.
### [About alerts from multiple configurations](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts#about-alerts-from-multiple-configurations)
You can run multiple configurations of code analysis on a repository, using different tools and targeting different languages or areas of the code. Each configuration of code scanning generates a unique set of alerts. For example, an alert generated using the default CodeQL analysis with GitHub Actions comes from a different configuration than an alert generated externally and uploaded via the code scanning API.
If you use multiple configurations to analyze a file, any problems detected by the same query are reported as alerts generated by multiple configurations. If an alert exists in more than one configuration, the number of configurations appears next to the branch name in the "Affected branches" section on the right-hand side of the alert page. To view the configurations for an alert, in the "Affected branches" section, click a branch. A "Configurations analyzing" modal appears with the names of each configuration generating the alert for that branch. Below each configuration, you can see when that configuration's alert was last updated.
An alert may display different statuses from different configurations. To update the alert statuses, re-run each out-of-date configuration. Alternatively, you can delete stale configurations from a branch to remove outdated alerts. For more information on deleting stale configurations and alerts, see [Resolving code scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/resolving-code-scanning-alerts#removing-stale-configurations-and-alerts-from-a-branch).
### [About labels for alerts that are not found in application code](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts#about-labels-for-alerts-that-are-not-found-in-application-code)
GitHub assigns a category label to alerts that are not found in application code. The label relates to the location of the alert.
  * Generated: Code generated by the build process
  * Test: Test code
  * Library: Library or third-party code
  * Documentation: Documentation


Code scanning categorizes files by file path. You cannot manually categorize source files.
In this example, an alert is marked as in "Test" code in the code scanning alert list.
![Screenshot of an alert in the code scanning list. To the right of the title, a "Test" label is highlighted with a dark orange outline.](https://docs.github.com/assets/cb-20594/images/help/repository/code-scanning-library-alert-index.png)
When you click through to see details for the alert, you can see that the file path is marked as "Test" code.
![Screenshot showing the details of an alert. The file path and "Test" label are highlighted with a dark orange outline.](https://docs.github.com/assets/cb-61482/images/help/repository/code-scanning-library-alert-show.png)
Experimental alerts for code scanning were available a public preview release for JavaScript using experimental technology in the CodeQL action. This feature was retired. For more information, see [CodeQL code scanning deprecates ML-powered alerts](https://github.blog/changelog/2023-09-29-codeql-code-scanning-deprecates-ml-powered-alerts/).
## [About alert severity and security severity levels](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts#about-alert-severity-and-security-severity-levels)
The severity level for a code scanning alert indicates how much risk the problem adds to your codebase.
  * **Severity.** All code scanning alerts have a level of `Error`, `Warning`, or `Note`.
  * **Security severity.** Each security alert found using CodeQL also has a security severity level of `Critical`, `High`, `Medium`, or `Low`.


When an alert has a security severity level, code scanning displays and uses this level in preference to the `severity`. Security severity levels follow the industry-standard Common Vulnerability Scoring System (CVSS) that is also used for advisories in the GitHub Advisory Database. For more information, see [CVSS: Qualitative Severity Rating Scale](https://www.first.org/cvss/v3.1/specification-document#Qualitative-Severity-Rating-Scale).
### [Pull request check failures for code scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts#pull-request-check-failures-for-code-scanning-alerts)
You can use rulesets to prevent pull requests from being merged when one of the following conditions is met:
  * A required tool found a code scanning alert of a severity that is defined in a ruleset.
  * A required code scanning tool's analysis is still in progress.
  * A required code scanning tool is not configured for the repository.


For more information, see [Set code scanning merge protection](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/set-code-scanning-merge-protection). For more general information about rulesets, see [About rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets).
### [Calculation of security severity levels](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts#calculation-of-security-severity-levels)
When a security query is added to the CodeQL Default or Extended query suite, the CodeQL engineering team calculates the security severity as follows.
  1. Search for all CVEs that are assigned one or more of the CWE tags associated with the new security query.
  2. Calculate the 75th percentile of the CVSS score for those CVEs.
  3. Define that score as the security severity for the query.
  4. When displaying alerts found by the query, translate the numerical scores to `Critical`, `High`, `Medium`, or `Low` using the CVSS definitions.


For more information, see [CodeQL CWE coverage](https://codeql.github.com/codeql-query-help/codeql-cwe-coverage/) on the CodeQL documentation site.
