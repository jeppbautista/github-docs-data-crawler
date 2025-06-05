  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners "Self-hosted runners")/
  * [Manage self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners "Manage self-hosted runners")/
  * [Usage limits](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/usage-limits-for-self-hosted-runners "Usage limits")


# Usage limits for self-hosted runners
There are some limits on GitHub Actions usage when using self-hosted runners. These limits are subject to change.
  * **Job execution time** - Each job in a workflow can run for up to 5 days of execution time. If a job reaches this limit, the job is terminated and fails to complete.
  * **Workflow run time** - Each workflow run is limited to 35 days. If a workflow run reaches this limit, the workflow run is cancelled. This period includes execution duration, and time spent on waiting and approval.
  * **Job queue time** - Each job for self-hosted runners that has been queued for at least 24 hours will be canceled. The actual time in queue can reach up to 48 hours before cancellation occurs. If a self-hosted runner does not start executing the job within this limit, the job is terminated and fails to complete.
  * **API requests** - You can execute up to 1,000 requests to the GitHub API in an hour across all actions within a repository. If requests are exceeded, additional API calls will fail which might cause jobs to fail.
  * **Job matrix** - A job matrix can generate a maximum of 256 jobs per workflow run. This limit applies to both GitHub-hosted and self-hosted runners.
  * **Workflow run queue** - No more than 500 workflow runs can be queued in a 10 second interval per repository. If a workflow run reaches this limit, the workflow run is terminated and fails to complete.
  * **Registering self-hosted runners** - You can have a maximum of 10,000 self-hosted runners in one runner group. If this limit is reached, adding a new runner will not be possible.


