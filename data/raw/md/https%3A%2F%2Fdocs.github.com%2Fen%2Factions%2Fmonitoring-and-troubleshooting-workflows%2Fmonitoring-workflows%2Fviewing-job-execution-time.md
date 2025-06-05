  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Monitor & troubleshoot](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows "Monitor & troubleshoot")/
  * [Monitor](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows "Monitor")/
  * [View job execution time](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/viewing-job-execution-time "View job execution time")


# Viewing job execution time
You can view the execution time of a job, including the billable minutes that a job accrued.
Billable job execution minutes are only shown for jobs run on private repositories that use GitHub-hosted runners and are rounded up to the next minute. There are no billable minutes when using GitHub Actions in public repositories or for jobs run on self-hosted runners.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the tabs for the "github/docs" repository. The "Actions" tab is highlighted with an orange outline.](https://docs.github.com/assets/cb-12958/images/help/repository/actions-tab-global-nav-update.png)
  3. In the left sidebar, click the workflow you want to see.
![Screenshot of the left sidebar of the "Actions" tab. A workflow, "CodeQL," is outlined in dark orange.](https://docs.github.com/assets/cb-40551/images/help/actions/superlinter-workflow-sidebar.png)
  4. From the list of workflow runs, click the name of the run to see the workflow run summary.
  5. Under the job summary, you can view the job's execution time.
  6. To view details about the billable job execution time, in the left sidebar under "Run details", click 
The billable time shown does not include any minute multipliers. To view your total GitHub Actions usage, including minute multipliers, see [Viewing your GitHub Actions usage](https://docs.github.com/en/billing/managing-billing-for-github-actions/viewing-your-github-actions-usage).


