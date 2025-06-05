  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Monitor & troubleshoot](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows "Monitor & troubleshoot")/
  * [Troubleshoot](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows "Troubleshoot")/
  * [About troubleshooting](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/about-troubleshooting-workflows "About troubleshooting")


# About troubleshooting workflows
You can use the tools in GitHub Actions to debug your workflows.
## In this article
  * [Troubleshooting your workflows](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/about-troubleshooting-workflows#troubleshooting-your-workflows)
  * [Troubleshooting GitHub Actions inefficiencies](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/about-troubleshooting-workflows#troubleshooting-github-actions-inefficiencies)
  * [Troubleshooting self-hosted runners](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/about-troubleshooting-workflows#troubleshooting-self-hosted-runners)


## [Troubleshooting your workflows](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/about-troubleshooting-workflows#troubleshooting-your-workflows)
There are several ways you can troubleshoot failed workflow runs.
### [Using GitHub Copilot](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/about-troubleshooting-workflows#using-github-copilot)
If a workflow run fails, you can open a chat with GitHub Copilot for assistance resolving the error. See [Using Copilot to troubleshoot workflows](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/using-copilot-to-troubleshoot-workflows).
### [Using workflow run logs](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/about-troubleshooting-workflows#using-workflow-run-logs)
Each workflow run generates activity logs that you can view, search, and download. For more information, see [Using workflow run logs](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/using-workflow-run-logs).
### [Enabling debug logging](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/about-troubleshooting-workflows#enabling-debug-logging)
If the workflow logs do not provide enough detail to diagnose why a workflow, job, or step is not working as expected, you can enable additional debug logging. For more information, see [Enabling debug logging](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/enabling-debug-logging).
### [Canceling a workflow](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/about-troubleshooting-workflows#canceling-a-workflow)
If you attempt to cancel a workflow and the cancellation doesn't succeed, make sure you aren't using the `always` expression. The `always` expression causes a workflow step to run even when the workflow is canceled, which results in a hanging cancellation. For more information, see [Evaluate expressions in workflows and actions](https://docs.github.com/en/actions/learn-github-actions/expressions#always).
## [Troubleshooting GitHub Actions inefficiencies](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/about-troubleshooting-workflows#troubleshooting-github-actions-inefficiencies)
To analyze the inefficiencies and reliability of your workflows using metrics, see [Viewing GitHub Actions metrics](https://docs.github.com/en/actions/administering-github-actions/viewing-github-actions-metrics).
## [Troubleshooting self-hosted runners](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/about-troubleshooting-workflows#troubleshooting-self-hosted-runners)
If you use self-hosted runners, you can view their activity and diagnose common issues.
For more information, see [Monitoring and troubleshooting self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/monitoring-and-troubleshooting-self-hosted-runners).
