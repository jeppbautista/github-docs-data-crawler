  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Introduction](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning "Introduction")/
  * [About code scanning](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning "About code scanning")


# About code scanning
You can use code scanning to find security vulnerabilities and errors in the code for your project on GitHub.
## Who can use this feature?
Code scanning is available for the following repository types:
  * Public repositories on GitHub.com
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [About billing for code scanning](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning#about-billing-for-code-scanning)
  * [About tools for code scanning](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning#about-tools-for-code-scanning)
  * [About the tool status page](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning#about-the-tool-status-page)


Code scanning is a feature that you use to analyze the code in a GitHub repository to find security vulnerabilities and coding errors. Any problems identified by the analysis are shown in your repository.
You can use code scanning to find, triage, and prioritize fixes for existing problems in your code. Code scanning also prevents developers from introducing new problems. You can schedule scans for specific days and times, or trigger scans when a specific event occurs in the repository, such as a push.
If code scanning finds a potential vulnerability or error in your code, GitHub displays an alert in the repository. After you fix the code that triggered the alert, GitHub closes the alert. For more information, see [Resolving code scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/resolving-code-scanning-alerts).
GitHub Copilot Autofix will suggest fixes for alerts from code scanning analysis in private repositories, allowing developers to prevent and reduce vulnerabilities with less effort. For more information, see [Responsible use of Copilot Autofix for code scanning](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/responsible-use-autofix-code-scanning).
To monitor results from code scanning across your repositories or your organization, you can use webhooks and the code scanning API. For information about the webhooks for code scanning, see [Webhook events and payloads](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#code_scanning_alert). For information about API endpoints, see [REST API endpoints for code scanning](https://docs.github.com/en/rest/code-scanning).
To get started with code scanning, see [Configuring default setup for code scanning](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning).
## [About billing for code scanning](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning#about-billing-for-code-scanning)
Code scanning uses GitHub Actions, and each run of a code scanning workflow consumes minutes for GitHub Actions. For more information, see [About billing for GitHub Actions](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions).
To use code scanning on a private repository, you will also need a license for GitHub Code Security. For information about how you can try GitHub Enterprise with GitHub Advanced Security for free, see [Setting up a trial of GitHub Enterprise Cloud](https://docs.github.com/en/enterprise-cloud@latest/admin/overview/setting-up-a-trial-of-github-enterprise-cloud) and [Setting up a trial of GitHub Advanced Security](https://docs.github.com/en/enterprise-cloud@latest/billing/managing-billing-for-your-products/managing-billing-for-github-advanced-security/setting-up-a-trial-of-github-advanced-security#setting-up-your-trial-of-github-advanced-security) in the GitHub Enterprise Cloud documentation.
## [About tools for code scanning](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning#about-tools-for-code-scanning)
You can configure code scanning to use the CodeQL product maintained by GitHub or a third-party code scanning tool.
### [About CodeQL analysis](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning#about-codeql-analysis)
CodeQL is the code analysis engine developed by GitHub to automate security checks. You can analyze your code using CodeQL and display the results as code scanning alerts. For more information about CodeQL, see [About code scanning with CodeQL](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql).
### [About third-party code scanning tools](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning#about-third-party-code-scanning-tools)
Code scanning is interoperable with third-party code scanning tools that output Static Analysis Results Interchange Format (SARIF) data. SARIF is an open standard. For more information, see [SARIF support for code scanning](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/sarif-support-for-code-scanning).
You can run third-party analysis tools within GitHub using actions or within an external CI system. For more information, see [Configuring advanced setup for code scanning](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning#configuring-code-scanning-using-third-party-actions) or [Uploading a SARIF file to GitHub](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/uploading-a-sarif-file-to-github).
## [About the tool status page](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning#about-the-tool-status-page)
The tool status page shows useful information about all of your code scanning tools. If code scanning is not working as you'd expect, the tool status page is a good starting point for debugging problems. For more information, see [About the tool status page for code scanning](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/about-the-tool-status-page).
