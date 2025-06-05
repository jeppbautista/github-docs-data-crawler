  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Monitor & troubleshoot](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows "Monitor & troubleshoot")/
  * [Monitor](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows "Monitor")/
  * [About monitoring](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/about-monitoring-workflows "About monitoring")


# About monitoring workflows
You can use the tools in GitHub Actions to monitor your workflows, metrics, and self-hosted runners.
## In this article
  * [Monitoring your workflows](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/about-monitoring-workflows#monitoring-your-workflows)
  * [Monitoring GitHub Actions metrics](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/about-monitoring-workflows#monitoring-github-actions-metrics)
  * [Monitoring self-hosted runners](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/about-monitoring-workflows#monitoring-self-hosted-runners)


## [Monitoring your workflows](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/about-monitoring-workflows#monitoring-your-workflows)
### [Monitoring your current jobs in your organization or enterprise](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/about-monitoring-workflows#monitoring-your-current-jobs-in-your-organization-or-enterprise)
To identify any constraints with concurrency or queuing, you can check how many jobs are currently being processed on the GitHub-hosted runners in your organization or enterprise. For more information, see [Monitoring your current jobs](https://docs.github.com/en/actions/using-github-hosted-runners/monitoring-your-current-jobs).
### [Using the visualization graph](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/about-monitoring-workflows#using-the-visualization-graph)
Every workflow run generates a real-time graph that illustrates the run progress. You can use this graph to monitor and debug workflows. For example:
![Screenshot of the visualization graph of a workflow run.](https://docs.github.com/assets/cb-63715/images/help/actions/workflow-graph.png)
For more information, see [Using the visualization graph](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/using-the-visualization-graph).
### [Adding a workflow status badge](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/about-monitoring-workflows#adding-a-workflow-status-badge)
A status badge shows whether a workflow is currently failing or passing. A common place to add a status badge is in the `README.md` file of your repository, but you can add it to any web page you'd like. By default, badges display the status of your default branch. If there are no workflow runs on your default branch, it will display the status of the most recent run across all branches. You can display the status of a workflow run for a specific branch or event using the `branch` and `event` query parameters in the URL.
![Screenshot of a workflow status badge. From right to left it shows: the GitHub logo, workflow name \("GitHub Actions Demo"\), and status \("passing"\).](https://docs.github.com/assets/cb-16218/images/help/repository/actions-workflow-status-badge.png)
For more information, see [Adding a workflow status badge](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge).
### [Viewing job execution time](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/about-monitoring-workflows#viewing-job-execution-time)
To identify how long a job took to run, you can view its execution time. For more information, see [Viewing job execution time](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/viewing-job-execution-time).
### [Viewing workflow run history](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/about-monitoring-workflows#viewing-workflow-run-history)
You can view the status of each job and step in a workflow. For more information, see [Viewing workflow run history](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/viewing-workflow-run-history).
## [Monitoring GitHub Actions metrics](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/about-monitoring-workflows#monitoring-github-actions-metrics)
To analyze the efficiency and reliability of your workflows using metrics, see [Viewing GitHub Actions metrics](https://docs.github.com/en/actions/administering-github-actions/viewing-github-actions-metrics).
## [Monitoring self-hosted runners](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/about-monitoring-workflows#monitoring-self-hosted-runners)
If you use self-hosted runners, you can view their activity and diagnose common issues.
For more information, see [Monitoring and troubleshooting self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/monitoring-and-troubleshooting-self-hosted-runners).
