  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Monitor & troubleshoot](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows "Monitor & troubleshoot")/
  * [Troubleshoot](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows "Troubleshoot")/
  * [Working with GitHub Support](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/working-with-support-for-github-actions "Working with GitHub Support")


# Working with Support for GitHub Actions
Learn how GitHub Support can assist with GitHub Actions
## In this article
  * [Providing diagnostic and troubleshooting information](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/working-with-support-for-github-actions#providing-diagnostic-and-troubleshooting-information)
  * [Scope of support](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/working-with-support-for-github-actions#scope-of-support)


You can [contact GitHub Support](https://docs.github.com/en/support/contacting-github-support) for assistance with GitHub Actions.
## [Providing diagnostic and troubleshooting information](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/working-with-support-for-github-actions#providing-diagnostic-and-troubleshooting-information)
The contents of private and internal repositories are not visible to GitHub Support, so GitHub Support may request additional information to understand the complete context of your inquiry and reproduce any unexpected behavior. You can accelerate the resolution of your inquiry by providing this information when you initially raise a ticket with GitHub Support.
Some information that GitHub Support will request can include, but is not limited to, the following:
  * The URL of the workflow run.
For example: `https://github.com/ORG/REPO/actions/runs/0123456789`
  * The workflow `.yml` file(s) attached to the ticket as `.txt` files. For more information about workflows, see [About workflows](https://docs.github.com/en/actions/using-workflows/about-workflows#about-workflows).
  * A copy of your workflow run logs for an example workflow run failure. For more information about workflow run logs, see [Using workflow run logs](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/using-workflow-run-logs#downloading-logs).
  * If you are running this workflow on a self-hosted runner, self-hosted runner logs which can be found under the `_diag` folder within the runner. For more information about self-hosted runners, see [Monitoring and troubleshooting self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/monitoring-and-troubleshooting-self-hosted-runners#reviewing-the-self-hosted-runner-application-log-files).
Self-hosted runner log file names are be formatted: `Runner_YYYY####-xxxxxx-utc.log` and `Worker_YYYY####-xxxxxx-utc.log`.


Attach files to your support ticket by changing the file's extension to `.txt` or `.zip`. If you include textual data such as log or workflow file snippets inline in your ticket, ensure they are formatted correctly as Markdown code blocks. For more information about proper Markdown formatting, see [Basic writing and formatting syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#quoting-code).
If the information you provide is unreadable due to the loss of formatting by improper Markdown syntax, GitHub Support may request that resubmit the information either as an attachment or with the correct Markdown formatting.
Ensure all files and text provided to GitHub Support have been properly redacted to remove sensitive information such as tokens and other secrets.
### [Ephemeral Runner Application Log Files](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/working-with-support-for-github-actions#ephemeral-runner-application-log-files)
GitHub Support may request the runner application log files from ephemeral runners. GitHub expects and recommends that you have implemented a mechanism to forward and preserve the runner application log files from self-hosted ephemeral runners. For more information about runner application log files and troubleshooting self-hosted runners, see [Monitoring and troubleshooting self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/monitoring-and-troubleshooting-self-hosted-runners#reviewing-the-self-hosted-runner-application-log-files).
### [Actions Runner Controller](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/working-with-support-for-github-actions#actions-runner-controller)
If you are using Actions Runner Controller (ARC), GitHub Support may ask you to submit the complete logs for the controller, listeners, and runner pods. For more information about collecting Actions Runner Controller's logs, see [Troubleshooting Actions Runner Controller errors](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/troubleshooting-actions-runner-controller-errors#checking-the-logs-of-the-controller-and-runner-set-listener).
For more information about the scope of support for Actions Runner Controller, see [About support for Actions Runner Controller](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/about-support-for-actions-runner-controller).
### [CodeQL and GitHub Actions](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/working-with-support-for-github-actions#codeql-and-github-actions)
If you are requesting assistance with a CodeQL analysis workflow, GitHub Support may request a copy of the CodeQL debugging artifacts. For more information about debugging artifacts for a CodeQL analysis workflow, see [Logs are not detailed enough](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/logs-not-detailed-enough#creating-codeql-debugging-artifacts).
To provide the debugging artifacts to GitHub Support, please download the CodeQL debugging artifacts from a sample workflow run and attach it to your ticket as a `.zip` file. For more information on downloading workflow artifacts, see [Downloading workflow artifacts](https://docs.github.com/en/actions/managing-workflow-runs/downloading-workflow-artifacts).
If the CodeQL debugging artifacts `.zip` file is too large to upload to the ticket, please advise GitHub Support, and we will work with you to determine the next steps.
## [Scope of support](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/working-with-support-for-github-actions#scope-of-support)
If your support request is outside of the scope of what our team can help you with, we may recommend next steps to resolve your issue outside of GitHub Support. Your support request is possibly out of GitHub Support's scope if the request is primarily about:
  * Third party integrations, such as Jira
  * CI/CD, such as Jenkins
  * Writing scripts
  * Configuration of external authentication systems, such as SAML identity providers
  * Open source projects
  * Writing or debugging new queries for CodeQL
  * Cloud provider configurations, such as virtual network setup, custom firewall, or proxy rules
  * Container orchestration, such as Kubernetes setup, or networking
  * Detailed assistance with workflows and data management
  * Preview features. Public preview, private preview, and technical preview features are out of GitHub Support's scope.


For detailed assistance with workflows and data management, consult [GitHub Expert Services](https://github.com/services/), which offer specialized support to help you optimize your use of the platform.
If you're uncertain if the issue is out of scope, open a ticket and we're happy to help you determine the best way to proceed.
