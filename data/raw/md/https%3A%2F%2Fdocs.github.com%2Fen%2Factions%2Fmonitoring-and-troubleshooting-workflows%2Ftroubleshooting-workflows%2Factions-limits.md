  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Monitor & troubleshoot](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows "Monitor & troubleshoot")/
  * [Troubleshoot](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows "Troubleshoot")/
  * [Actions limits](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/actions-limits "Actions limits")


# Actions limits
There are limits in GitHub Actions which you may hit as you scale up, some may be increased by contacting support.
## In this article
  * [Limits in GitHub Actions](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/actions-limits#limits-in-github-actions)
  * [Existing system limits](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/actions-limits#existing-system-limits)


## [Limits in GitHub Actions](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/actions-limits#limits-in-github-actions)
You may be rate limited by GitHub Actions when you scale your usage. Some limits can be increased by contacting us through the [GitHub Support portal](https://support.github.com).
Unless otherwise stated, the expected behaviour when a limit is reached is that the workflow/job will get cancelled.
These limits are subject to change.
## [Existing system limits](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/actions-limits#existing-system-limits)
Limit category | Limit | Threshold | Description | Can GitHub Support increase?  
---|---|---|---|---  
Workflow execution limit | Workflow run time | 35 days / workflow run | If a workflow run reaches this limit, the workflow run is cancelled. This period includes execution duration, and time spent on waiting and approval. |   
Workflow execution limit | Gate approval time | 30 days | A workflow may wait for up to [30 days on environment approvals](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#wait-timer). |   
Workflows queuing | Workflow trigger event rate limit | 1500 events / 10 seconds / repository | Each repository is limited to events triggering a workflow run. |   
Workflows queuing | Workflow run queued | 500 workflow runs / 10 seconds | When the limit is reached, the workflow runs that were supposed to be triggered by the webhook events will be blocked and will not be queued. Reusable workflows are viewed as a single entity. For example, a run with 30 reusable workflows counts as 1 in this instance. |   
Workflows queuing | Workflow run start | 50 workflow runs / minute | When the limit is reached, additional workflow runs will queue, causing delays in starting jobs. |   
Workflows execution | Job assignment | 100 jobs / minute / repo | When the limit is reached, additional jobs will queue, causing delays in starting jobs and updating the UI results of existing jobs. |   
Workflow execution | Job Matrix | 256 jobs / workflow run | A job matrix can generate a maximum of jobs per workflow run. This limit applies to both GitHub-hosted and self-hosted runners. |   
Self-hosted | Runner registrations | 1500 runners / 5 minutes / repository/org/enterprise | Runners can be registered per repository/organization/enterprise. |   
Self-hosted | Runners per runner group | 10,000 runners | Runners registered at the same time per runner group. |   
Hosted-runners | Job Concurrency | Varies | For more information about concurrency limits for standard and larger runners, see [Usage limits, billing, and administration](https://docs.github.com/en/actions/administering-github-actions/usage-limits-billing-and-administration#usage-limits). |   
Hosted-runners | Job execution time | 6 hours | Each job in a workflow can run for up to 6 hours of execution time. If a job reaches this limit, the job is terminated and fails. |   
Hosted-runners | Storage limits | Varies | For more information, see [About billing for GitHub Actions](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-actions/about-billing-for-github-actions#included-storage-and-minutes). |   
Larger runners | Per runner concurrency limit | Varies by runner type | You establish when setting up a runner, normally 1,000 max for Linux CPU runners but varies by type. For more information, see [Usage limits, billing, and administration](https://docs.github.com/en/actions/administering-github-actions/usage-limits-billing-and-administration#usage-limits). |   
Larger runners | Static IP limits | 10-50 IPs | 10 IPs for team plans, 50 IPs for enterprise, and the limit is configurable. |   
Larger runners | Private IP scaling for vnet injection | 30% buffer | You need to determine the appropriate subnet IP address range, for which we recommend adding a buffer to the maximum job concurrency you anticipate. For instance, if the network configuration's runners are set to a maximum job concurrency of 300, utilize a subnet IP address range that can accommodate at least 390 runners. Note that Azure reserves 5 IPs in every subnet (first 4 and last 1), which sets a minimum practical subnet size depending on runner requirements. Very small subnets (like /29 or smaller) may not provide enough usable addresses for your needs. |   
### [Commonly hit dependent service limits](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/actions-limits#commonly-hit-dependent-service-limits)
GitHub's [REST API rate limits](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api) apply to GitHub Actions users, those that are commonly hit are:
  * **Unauthenticated users** - You can make unauthenticated requests if you are only fetching public data. Unauthenticated requests are associated with the originating IP address, not with the user or application that made the request.
The primary rate limit for unauthenticated requests is 60 requests per hour.
  * **Authenticated users** - You can use a personal access token to make API requests. Additionally, you can authorize a GitHub App or OAuth app, which can then make API requests on your behalf.
All of these requests count towards your personal rate limit of 5,000 requests per hour. Requests made on your behalf by a GitHub App that is owned by a GitHub Enterprise Cloud organization have a higher rate limit of 15,000 requests per hour. Similarly, requests made on your behalf by a OAuth app that is owned or approved by a GitHub Enterprise Cloud organization have a higher rate limit of 15,000 requests per hour if you are a member of the GitHub Enterprise Cloud organization.
  * **GitHub app installations** - GitHub Apps authenticating with an installation access token use the installation's minimum rate limit of 5,000 requests per hour. If the installation is on a GitHub Enterprise Cloud organization, the installation has a rate limit of 15,000 requests per hour.
For installations that are not on a GitHub Enterprise Cloud organization, the rate limit for the installation will scale with the number of users and repositories. Installations that have more than 20 repositories receive another 50 requests per hour for each repository. Installations that are on an organization that have more than 20 users receive another 50 requests per hour for each user. The rate limit cannot increase beyond 12,500 requests per hour.
Primary rate limits for GitHub App user access tokens (as opposed to installation access tokens) are dictated by the primary rate limits for the authenticated user. This rate limit is combined with any requests that another GitHub App or OAuth app makes on that user's behalf and any requests that the user makes with a personal access token. For more information, see [Rate limits for the REST API](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api#primary-rate-limit-for-authenticated-users).
  * **OAuth apps -** For these requests, the rate limit is 5,000 requests per hour per OAuth app. If the app is owned by a GitHub Enterprise Cloud organization, the rate limit is 15,000 requests per hour.
  * **GITHUB TOKEN** - The rate limit for `GITHUB_TOKEN` is 1,000 requests per hour per repository. For requests to resources that belong to a GitHub Enterprise Cloud account, the limit is 15,000 requests per hour per repository.
  * **Secondary rate limits** - In addition to primary rate limits, GitHub enforces secondary rate limits in order to prevent abuse and keep the API available for all users, these are not configurable with GHEC. For more information, see [Rate limits for the REST API](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api?apiVersion=2022-11-28#about-secondary-rate-limits).


