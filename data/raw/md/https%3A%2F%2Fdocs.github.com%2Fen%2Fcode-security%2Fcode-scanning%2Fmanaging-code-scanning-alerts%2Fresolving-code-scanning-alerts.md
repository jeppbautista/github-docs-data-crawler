  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Manage alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts "Manage alerts")/
  * [Resolve alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/resolving-code-scanning-alerts "Resolve alerts")


# Resolving code scanning alerts
From the security view, you can view, fix, or dismiss alerts for potential vulnerabilities or errors in your project's code.
## Who can use this feature?
Users with **write** access
## In this article
  * [Generating suggested fixes for code scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/resolving-code-scanning-alerts#generating-suggested-fixes-for-code-scanning-alerts)
  * [Fixing an alert manually](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/resolving-code-scanning-alerts#fixing-an-alert-manually)
  * [Dismissing alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/resolving-code-scanning-alerts#dismissing-alerts)
  * [Re-opening dismissed alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/resolving-code-scanning-alerts#re-opening-dismissed-alerts)
  * [Removing stale configurations and alerts from a branch](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/resolving-code-scanning-alerts#removing-stale-configurations-and-alerts-from-a-branch)
  * [Further reading](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/resolving-code-scanning-alerts#further-reading)


## [Generating suggested fixes for code scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/resolving-code-scanning-alerts#generating-suggested-fixes-for-code-scanning-alerts)
GitHub Copilot Autofix can generate fixes for alerts identified by code scanning analysis. Most CodeQL alert types are supported and also some alerts from third-party tools. For more information, see [Responsible use of Copilot Autofix for code scanning](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/responsible-use-autofix-code-scanning).
You do not need a subscription to GitHub Copilot to use GitHub Copilot Autofix. Copilot Autofix is available to all public repositories on GitHub.com, as well as internal or private repositories owned by organizations and enterprises that have a license for GitHub Code Security.
  1. On GitHub, navigate to the main page of the repository.
  2. Under the repository name, click **Security**. 
![Screenshot of a repository header showing the tabs. The "Security" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-17801/images/help/repository/security-tab.png)
  3. In the left sidebar, click 
  4. Click the name of an alert.
  5. If Copilot Autofix can suggest a fix, at the top of the page, click 
  6. Once the suggested fix has been generated, at the bottom of the page, you can click **Create PR with fix** to automatically generate a pull request with the suggested fix. A new branch is created from the default branch, the generated fix is committed and a draft pull request is created. You can test and edit the suggested fix as you would with any other fix.


You can also use the Autofix API for historical alerts endpoints to generate, get, and commit suggested fixes.
  * [Create an autofix for a code scanning alert](https://docs.github.com/en/rest/code-scanning/code-scanning#create-an-autofix-for-a-code-scanning-alert)
  * [Get the status of an autofix for a code scanning alert](https://docs.github.com/en/rest/code-scanning/code-scanning#get-the-status-of-an-autofix-for-a-code-scanning-alert)
  * [Commit an autofix for a code scanning alert](https://docs.github.com/en/rest/code-scanning/code-scanning#commit-an-autofix-for-a-code-scanning-alert)


For information about the limitations of automatically generated fixes, see [Limitations of suggestions](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-autofix-for-codeql-code-scanning#limitations-of-suggestions).
## [Fixing an alert manually](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/resolving-code-scanning-alerts#fixing-an-alert-manually)
Anyone with write permission for a repository can fix an alert by committing a correction to the code. If the repository has code scanning scheduled to run on pull requests, it's best to raise a pull request with your correction. This will trigger code scanning analysis of the changes and test that your fix doesn't introduce any new problems. For more information, see [Triaging code scanning alerts in pull requests](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/triaging-code-scanning-alerts-in-pull-requests).
You can use the free text search or the filters to display a subset of alerts and then in turn mark all matching alerts as closed.
Alerts may be fixed in one branch but not in another. You can use the "Branch" filter, on the summary of alerts, to check whether an alert is fixed in a particular branch.
![Screenshot of alerts view with the "Branch" dropdown menu expanded. The "Branch" button is outlined in dark orange.](https://docs.github.com/assets/cb-86395/images/help/repository/code-scanning-branch-filter.png)
Please note that if you have filtered for alerts on a non-default branch, but the same alerts exist on the default branch, the alert page for any given alert will still only reflect the alert's status on the default branch, even if that status conflicts with the status on a non-default branch. For example, an alert that appears in the "Open" list in the summary of alerts for `branch-x` could show a status of "Fixed" on the alert page, if the alert is already fixed on the default branch. You can view the status of the alert for the branch you filtered on in the **Affected branches** section on the right side of the alert page.
If you run code scanning using multiple configurations, the same alert will sometimes be generated by more than one configuration. Unless you run all configurations regularly, you may see alerts that are fixed in one configuration but not in another. These stale configurations and alerts can be removed from a branch. For more information, see [Removing stale configurations and alerts from a branch](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/resolving-code-scanning-alerts#removing-stale-configurations-and-alerts-from-a-branch).
## [Dismissing alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/resolving-code-scanning-alerts#dismissing-alerts)
There are two ways of closing an alert. You can fix the problem in the code, or you can dismiss the alert.
Dismissing an alert is a way of closing an alert that you don't think needs to be fixed. For example, an error in code that's used only for testing, or when the effort of fixing the error is greater than the potential benefit of improving the code. You can dismiss alerts from code scanning annotations in code, or from the summary list within the **Security** tab.
When you dismiss an alert:
  * It's dismissed in all branches.
  * The alert is removed from the number of current alerts for your project.
  * The alert is moved to the "Closed" list in the summary of alerts, from where you can reopen it, if required.
  * The reason why you closed the alert is recorded.
  * Optionally, you can comment on a dismissal to record the context of an alert dismissal.
  * Next time code scanning runs, the same code won't generate an alert.


To dismiss alerts:
  1. On GitHub, navigate to the main page of the repository.
  2. Under the repository name, click **Security**. 
![Screenshot of a repository header showing the tabs. The "Security" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-17801/images/help/repository/security-tab.png)
  3. In the left sidebar, click 
  4. If you want to dismiss an alert, it's important to explore the alert first, so that you can choose the correct dismissal reason. Click the alert you'd like to explore.
  5. Review the alert, then click **Dismiss alert** and choose, or type, a reason for closing the alert. 
![Screenshot of an alert check failure. The "Dismiss alert" button is highlighted in dark orange and the dismiss drop-down displayed. ](https://docs.github.com/assets/cb-126828/images/help/repository/code-scanning-alert-dropdown-reason.png)
It's important to choose the appropriate reason from the drop-down menu as this may affect whether a query continues to be included in future analysis. Optionally, you can comment on a dismissal to record the context of an alert dismissal. The dismissal comment is added to the alert timeline and can be used as justification during auditing and reporting. You can retrieve or set a comment by using the code scanning REST API. The comment is contained in `dismissed_comment` for the `alerts/{alert_number}` endpoint. For more information, see [REST API endpoints for code scanning](https://docs.github.com/en/rest/code-scanning#update-a-code-scanning-alert).
If you dismiss a CodeQL alert as a false positive result, for example because the code uses a sanitization library that isn't supported, consider contributing to the CodeQL repository and improving the analysis. For more information about CodeQL, see [Contributing to CodeQL](https://github.com/github/codeql/blob/main/CONTRIBUTING.md).


### [Dismissing multiple alerts at once](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/resolving-code-scanning-alerts#dismissing-multiple-alerts-at-once)
If a project has multiple alerts that you want to dismiss for the same reason, you can bulk dismiss them from the summary of alerts. Typically, you'll want to filter the list and then dismiss all of the matching alerts. For example, you might want to dismiss all of the current alerts in the project that have been tagged for a particular Common Weakness Enumeration (CWE) vulnerability.
## [Re-opening dismissed alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/resolving-code-scanning-alerts#re-opening-dismissed-alerts)
If you dismiss an alert but later realize that you need to fix the alert, you can re-open it and fix the problem with the code. Display the list of closed alerts, find the alert, display it, and reopen it. You can then fix the alert in the same way as any other alert.
## [Removing stale configurations and alerts from a branch](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/resolving-code-scanning-alerts#removing-stale-configurations-and-alerts-from-a-branch)
You may have multiple code scanning configurations on a single repository. When run, multiple configurations can generate the same alert. Additionally, if the configurations are run on different schedules, the alert statuses may become out-of-date for infrequent or stale configurations. For more information on alerts from multiple configurations, see [About code scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts#about-alerts-from-multiple-configurations).
  1. On GitHub, navigate to the main page of the repository.
  2. Under the repository name, click **Security**. 
![Screenshot of a repository header showing the tabs. The "Security" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-17801/images/help/repository/security-tab.png)
  3. In the left sidebar, click 
  4. Under "Code scanning", click a code scanning alert.
  5. In the "Affected branches" section of the sidebar, click the desired branch.
  6. In the "Configurations analyzing" dialog, review details of the configurations that reported this alert on the selected branch. To delete an unwanted configuration for the desired branch, click 
If you delete a configuration by mistake, click **Cancel** to avoid applying your changes.
![Screenshot of the "Configurations analyzing" modal. The "Delete configuration" icon is outlined in dark orange.](https://docs.github.com/assets/cb-44092/images/help/repository/code-scanning-remove-configuration.png)
  7. Once you have removed any unwanted configurations and confirmed the expected configurations are displayed, click **Save changes**.
If you save your changes after accidentally deleting a configuration, re-run the configuration to update the alert. For more information on re-running configurations that use GitHub Actions, see [Re-running workflows and jobs](https://docs.github.com/en/actions/managing-workflow-runs/re-running-workflows-and-jobs#re-running-all-the-jobs-in-a-workflow).


  * If you remove all code scanning configurations for the default branch of your repository, the default branch will remain in the "Affected branches" sidebar, but it will not be analyzed by any configurations.
  * If you remove all code scanning configurations for any branch other than the default branch of your repository, that branch will be removed from the "Affected branches" sidebar.


## [Further reading](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/resolving-code-scanning-alerts#further-reading)
  * [Triaging code scanning alerts in pull requests](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/triaging-code-scanning-alerts-in-pull-requests)
  * [Configuring default setup for code scanning](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning)
  * [About integration with code scanning](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/about-integration-with-code-scanning)
  * [Using Copilot to help you work on a pull request](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-for-pull-requests/using-copilot-to-help-you-work-on-a-pull-request)


