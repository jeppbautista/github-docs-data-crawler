  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [GitHub-hosted runners](https://docs.github.com/en/actions/using-github-hosted-runners "GitHub-hosted runners")/
  * [About GitHub-hosted runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-github-hosted-runners "About GitHub-hosted runners")/
  * [Monitor current jobs](https://docs.github.com/en/actions/using-github-hosted-runners/using-github-hosted-runners/monitoring-your-current-jobs "Monitor current jobs")


# Monitoring your current jobs
Monitor how GitHub-hosted runners are processing jobs in your organization or enterprise, and identify any related constraints.
## In this article
  * [Viewing active jobs in your organization or enterprise](https://docs.github.com/en/actions/using-github-hosted-runners/using-github-hosted-runners/monitoring-your-current-jobs#viewing-active-jobs-in-your-organization-or-enterprise)
  * [Viewing queued jobs in your organization or enterprise](https://docs.github.com/en/actions/using-github-hosted-runners/using-github-hosted-runners/monitoring-your-current-jobs#viewing-queued-jobs-in-your-organization-or-enterprise)


## [Viewing active jobs in your organization or enterprise](https://docs.github.com/en/actions/using-github-hosted-runners/using-github-hosted-runners/monitoring-your-current-jobs#viewing-active-jobs-in-your-organization-or-enterprise)
You can get a list of all jobs currently running on GitHub-hosted runners in your organization or enterprise.
  1. Navigate to the main page of the organization or repository.
  2. Click 
  3. In the left sidebar, click **Actions** , then click **Runners**.
  4. In the "Runners" table, click the entry for **GitHub-hosted runners**. This entry will only be present if you're using GitHub-hosted runners.
  5. Review the "Active jobs" section, which contains a list of all jobs currently running on GitHub-hosted runners.


## [Viewing queued jobs in your organization or enterprise](https://docs.github.com/en/actions/using-github-hosted-runners/using-github-hosted-runners/monitoring-your-current-jobs#viewing-queued-jobs-in-your-organization-or-enterprise)
GitHub-hosted runners allow you to run jobs concurrently, and the maximum number of concurrent jobs will vary depending on your plan. If you reach the maximum number of concurrent jobs, any new jobs will start to enter a queue. To find out more about the number of concurrent jobs available to your plan, see [Usage limits, billing, and administration](https://docs.github.com/en/actions/learn-github-actions/usage-limits-billing-and-administration).
The following procedure demonstrates how to check the maximum number of concurrent jobs you can run.
  1. Navigate to the main page of the organization or repository.
  2. Click 
  3. In the left sidebar, click **Actions** , then click **Runners**.
  4. In the "Runners" table, click the entry for **GitHub-hosted runners**. This entry will only be present if you're using GitHub-hosted runners.
  5. Review the "All jobs usage" section, which lists the number of active jobs and the maximum number of jobs you can run.


