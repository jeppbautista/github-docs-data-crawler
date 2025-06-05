  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Manage code scanning](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration "Manage code scanning")/
  * [View code scanning logs](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/viewing-code-scanning-logs "View code scanning logs")


# Viewing code scanning logs
You can view the output generated during code scanning analysis in GitHub.
## Who can use this feature?
Users with **read** access
## In this article
  * [About your code scanning configuration](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/viewing-code-scanning-logs#about-your-code-scanning-configuration)
  * [About analysis and diagnostic information](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/viewing-code-scanning-logs#about-analysis-and-diagnostic-information)
  * [Viewing the logging output from code scanning](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/viewing-code-scanning-logs#viewing-the-logging-output-from-code-scanning)


## [About your code scanning configuration](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/viewing-code-scanning-logs#about-your-code-scanning-configuration)
You can use a variety of tools to configure code scanning in your repository. For more information, see [Configuring default setup for code scanning](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning) and [Configuring advanced setup for code scanning](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning).
The log and diagnostic information available to you depends on the method you use for code scanning in your repository. You can check the type of code scanning you're using in the **Security** tab of your repository, by using the **Tool** drop-down menu in the alert list. For more information, see [Assessing code scanning alerts for your repository](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository#viewing-the-alerts-for-a-repository).
## [About analysis and diagnostic information](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/viewing-code-scanning-logs#about-analysis-and-diagnostic-information)
You can see analysis and diagnostic information for code scanning run using CodeQL analysis on GitHub.
Analysis information is shown for the most recent analysis in a header at the top of the list of alerts. For more information, see [Assessing code scanning alerts for your repository](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository#viewing-the-alerts-for-a-repository).
Diagnostic information is displayed in the Action workflow logs and consists of summary metrics and extractor diagnostics. For information about accessing code scanning logs on GitHub, see [Viewing the logging output from code scanning](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/viewing-code-scanning-logs#viewing-the-logging-output-from-code-scanning) below.
If you're using the CodeQL CLI outside GitHub, you'll see diagnostic information in the output generated during database analysis. This information is also included in the SARIF results file you upload to GitHub with the code scanning results.
For information about the CodeQL CLI, see [Analyzing your code with CodeQL queries](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/analyzing-your-code-with-codeql-queries#viewing-log-and-diagnostic-information).
### [About summary metrics](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/viewing-code-scanning-logs#about-summary-metrics)
Summary metrics include:
  * Lines of code in the codebase (used as a baseline), before creation and extraction of the CodeQL database
  * Lines of code in the CodeQL database extracted from the code, including external libraries and auto-generated files
  * Lines of code in the CodeQL database excluding auto-generated files and external libraries


### [About CodeQL source code extraction diagnostics](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/viewing-code-scanning-logs#about-codeql-source-code-extraction-diagnostics)
Extractor diagnostics only cover files that were seen during the analysis, metrics include:
  * Number of files successfully analyzed
  * Number of files that generated extractor errors during database creation
  * Number of files that generated extractor warnings during database creation


You can see more detailed information about CodeQL extractor errors and warnings that occurred during database creation by enabling debug logging. For more information, see [Logs are not detailed enough](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/logs-are-not-detailed-enough#creating-codeql-debugging-artifacts-by-re-running-jobs-with-debug-logging-enabled).
## [Viewing the logging output from code scanning](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/viewing-code-scanning-logs#viewing-the-logging-output-from-code-scanning)
This section applies to code scanning run using GitHub Actions (CodeQL or third-party).
After configuring code scanning for your repository, you can watch the output of the actions as they run.
  1. Under your repository name, click 
![Screenshot of the tabs for the "github/docs" repository. The "Actions" tab is highlighted with an orange outline.](https://docs.github.com/assets/cb-12958/images/help/repository/actions-tab-global-nav-update.png)
You'll see a list that includes an entry for running the code scanning workflow. The text of the entry is the title you gave your commit message.
![Screenshot of the "All workflows" page. In the list of workflow runs is a run labeled "Create .github/workflows/codeql.yml."](https://docs.github.com/assets/cb-37609/images/help/repository/code-scanning-actions-list.png)
  2. Click the entry for the code scanning workflow.
If you are looking for the CodeQL workflow run triggered by enabling default setup, the text of the entry is "CodeQL."
  3. Click the job name on the left. For example, **Analyze (LANGUAGE)**.
![Screenshot of the log output for the "Analyze \(go\)" job. In the left sidebar, under the "Jobs" heading, "Analyze \(go\)" is listed.](https://docs.github.com/assets/cb-47516/images/help/repository/code-scanning-logging-analyze-action.png)
  4. Review the logging output from the actions in this workflow as they run.
  5. Optionally, to see more detail about the commit that triggered the workflow run, click the short commit hash. The short commit hash is 7 lowercase characters immediately following the commit author's username.
  6. Once all jobs are complete, you can view the details of any code scanning alerts that were identified. For more information, see [Assessing code scanning alerts for your repository](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository#viewing-the-alerts-for-a-repository).


### [Determining whether code scanning default setup used any private registries](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/viewing-code-scanning-logs#determining-whether-code-scanning-default-setup-used-any-private-registries)
Code scanning default setup includes a `Setup proxy or registries` step. When you are looking at a log file for default setup, you can expand this step. If the step includes:
  * `Using registries_credentials input.` At least one private registry is configured for the organization.
  * `Credentials loaded for the following registries:`
    * No further output in the step. Access was unsuccessful.
    * `Type: nuget_feed;` Default set up accessed a private Nuget feed.
    * `Type: maven_repository;` Default set up accessed a private Maven repository.


For more information, see [Giving security features access to private registries](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/giving-org-access-private-registries).
