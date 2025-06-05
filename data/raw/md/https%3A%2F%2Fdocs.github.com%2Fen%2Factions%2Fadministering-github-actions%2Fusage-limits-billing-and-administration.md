  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Administer GitHub Actions](https://docs.github.com/en/actions/administering-github-actions "Administer GitHub Actions")/
  * [Workflow billing & limits](https://docs.github.com/en/actions/administering-github-actions/usage-limits-billing-and-administration "Workflow billing & limits")


# Usage limits, billing, and administration
There are usage limits for GitHub Actions workflows. Usage charges apply to repositories that go beyond the amount of free minutes and storage for a repository.
## In this article
  * [About billing for GitHub Actions](https://docs.github.com/en/actions/administering-github-actions/usage-limits-billing-and-administration#about-billing-for-github-actions)
  * [Availability](https://docs.github.com/en/actions/administering-github-actions/usage-limits-billing-and-administration#availability)
  * [Usage limits](https://docs.github.com/en/actions/administering-github-actions/usage-limits-billing-and-administration#usage-limits)
  * [Usage policy](https://docs.github.com/en/actions/administering-github-actions/usage-limits-billing-and-administration#usage-policy)
  * [GitHub Actions usage metrics](https://docs.github.com/en/actions/administering-github-actions/usage-limits-billing-and-administration#github-actions-usage-metrics)
  * [Billing for reusable workflows](https://docs.github.com/en/actions/administering-github-actions/usage-limits-billing-and-administration#billing-for-reusable-workflows)
  * [Artifact and log retention policy](https://docs.github.com/en/actions/administering-github-actions/usage-limits-billing-and-administration#artifact-and-log-retention-policy)
  * [Workflow run history retention policy](https://docs.github.com/en/actions/administering-github-actions/usage-limits-billing-and-administration#workflow-run-history-retention-policy)
  * [Disabling or limiting GitHub Actions for your repository or organization](https://docs.github.com/en/actions/administering-github-actions/usage-limits-billing-and-administration#disabling-or-limiting-github-actions-for-your-repository-or-organization)
  * [Disabling and enabling workflows](https://docs.github.com/en/actions/administering-github-actions/usage-limits-billing-and-administration#disabling-and-enabling-workflows)


## [About billing for GitHub Actions](https://docs.github.com/en/actions/administering-github-actions/usage-limits-billing-and-administration#about-billing-for-github-actions)
GitHub Actions help you automate your software development workflows in the same place you store code and collaborate on pull requests and issues. You can write individual tasks, called actions, and combine them to create a custom workflow. For more information, see [Understanding GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions).
GitHub Actions usage is free for standard GitHub-hosted runners in public repositories, and for self-hosted runners. See [Choosing the runner for a job](https://docs.github.com/en/actions/writing-workflows/choosing-where-your-workflow-runs/choosing-the-runner-for-a-job#standard-github-hosted-runners-for-public-repositories). For private repositories, each GitHub account receives a certain amount of free minutes and storage for use with GitHub-hosted runners, depending on the account's plan. Any usage beyond the included amounts is controlled by spending limits. For more information, see [About billing for GitHub Actions](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions).
## [Availability](https://docs.github.com/en/actions/administering-github-actions/usage-limits-billing-and-administration#availability)
GitHub Actions is available on all GitHub products, but GitHub Actions is not available for private repositories owned by accounts using legacy per-repository plans. For more information, see [GitHub’s plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans).
## [Usage limits](https://docs.github.com/en/actions/administering-github-actions/usage-limits-billing-and-administration#usage-limits)
There are some limits on GitHub Actions usage when using GitHub-hosted runners. These limits are subject to change.
For self-hosted runners, different usage limits apply. For more information, see [Usage limits for self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/usage-limits-for-self-hosted-runners).
For more information about service rate limits, see [Actions limits](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/actions-limits).
**Standard GitHub-hosted runners**
GitHub plan | Total concurrent jobs | Maximum concurrent macOS jobs  
---|---|---  
Free | 20 | 5  
Pro | 40 | 5  
Team | 60 | 5  
Enterprise | 500 | 50  
**GitHub-hosted larger runners**
GitHub plan | Total concurrent jobs | Maximum concurrent macOS jobs | Maximum concurrent GPU jobs  
---|---|---|---  
Team | 1000 | 5 | 100  
Enterprise | 1000 | 50 | 100  
  * If required, customers on enterprise plans can request a higher limit for concurrent jobs. For more information, contact us through the [GitHub Support portal](https://support.github.com/), or contact your sales representative.
  * The maximum concurrent macOS jobs is shared across standard GitHub-hosted runner and GitHub-hosted larger runners.


  * **Job matrix** - A job matrix can generate a maximum of 256 jobs per workflow run. This limit applies to both GitHub-hosted and self-hosted runners.
  * **Workflow run queue** - No more than 500 workflow runs can be queued in a 10 second interval per repository. If a workflow run reaches this limit, the workflow run is terminated and fails to complete.


## [Usage policy](https://docs.github.com/en/actions/administering-github-actions/usage-limits-billing-and-administration#usage-policy)
In addition to the usage limits, you must ensure that you use GitHub Actions within the [GitHub Terms of Service](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service). For more information on GitHub Actions-specific terms, see the [GitHub Additional Product Terms](https://docs.github.com/en/site-policy/github-terms/github-terms-for-additional-products-and-features#a-actions-usage).
## [GitHub Actions usage metrics](https://docs.github.com/en/actions/administering-github-actions/usage-limits-billing-and-administration#github-actions-usage-metrics)
Organization owners and users with the "View organization Actions metrics" permission can view GitHub Actions usage metrics for their organization. These metrics can help you understand how and where your Actions minutes are being used. For more information, see [Viewing GitHub Actions metrics for your organization](https://docs.github.com/en/enterprise-cloud@latest/organizations/collaborating-with-groups-in-organizations/viewing-usage-metrics-for-github-actions).
When you view usage metrics, it is important to remember that GitHub Actions usage metrics do not apply minute multipliers to the metrics displayed. While they _can_ help you understand your bill, their primary purpose is to help you understand how and where Actions minutes are being used in your organization.
For more information about minute multipliers, see [About billing for GitHub Actions](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions#minute-multipliers).
## [Billing for reusable workflows](https://docs.github.com/en/actions/administering-github-actions/usage-limits-billing-and-administration#billing-for-reusable-workflows)
If you reuse a workflow, billing is always associated with the caller workflow. Assignment of GitHub-hosted runners is always evaluated using only the caller's context. The caller cannot use GitHub-hosted runners from the called repository.
For more information see, [Reusing workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows).
## [Artifact and log retention policy](https://docs.github.com/en/actions/administering-github-actions/usage-limits-billing-and-administration#artifact-and-log-retention-policy)
You can configure the artifact and log retention period for your repository, organization, or enterprise account.
By default, the artifacts and log files generated by workflows are retained for 90 days before they are automatically deleted. You can adjust the retention period, depending on the type of repository:
  * For public repositories: you can change this retention period to anywhere between 1 day or 90 days.
  * For private repositories: you can change this retention period to anywhere between 1 day or 400 days.


When you customize the retention period, it only applies to new artifacts and log files, and does not retroactively apply to existing objects. For managed repositories and organizations, the maximum retention period cannot exceed the limit set by the managing organization or enterprise.
For more information, see:
  * [Managing GitHub Actions settings for a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#configuring-the-retention-period-for-github-actions-artifacts-and-logs-in-your-repository)
  * [Configuring the retention period for GitHub Actions artifacts and logs in your organization](https://docs.github.com/en/organizations/managing-organization-settings/configuring-the-retention-period-for-github-actions-artifacts-and-logs-in-your-organization)
  * [Enforcing policies for GitHub Actions in your enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise#enforcing-a-policy-for-artifact-and-log-retention-in-your-enterprise)


## [Workflow run history retention policy](https://docs.github.com/en/actions/administering-github-actions/usage-limits-billing-and-administration#workflow-run-history-retention-policy)
The workflow runs in a repository's workflow run history are retained for 400 days. After 400 days, workflow runs are archived. 10 days after archival, they are permanently deleted. The retention period for workflow runs cannot be modified. For more information, see [Viewing workflow run history](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/viewing-workflow-run-history).
## [Disabling or limiting GitHub Actions for your repository or organization](https://docs.github.com/en/actions/administering-github-actions/usage-limits-billing-and-administration#disabling-or-limiting-github-actions-for-your-repository-or-organization)
By default, GitHub Actions is enabled on all repositories and organizations. You can choose to disable GitHub Actions or limit it to actions and reusable workflows in your organization.
For more information, see:
  * [Managing GitHub Actions settings for a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository)
  * [Disabling or limiting GitHub Actions for your organization](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization)
  * [Enforcing policies for GitHub Actions in your enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise)


## [Disabling and enabling workflows](https://docs.github.com/en/actions/administering-github-actions/usage-limits-billing-and-administration#disabling-and-enabling-workflows)
You can enable and disable individual workflows in your repository on GitHub.
To prevent unnecessary workflow runs, scheduled workflows may be disabled automatically. When a public repository is forked, scheduled workflows are disabled by default. In a public repository, scheduled workflows are automatically disabled when no repository activity has occurred in 60 days.
For more information, see [Disabling and enabling a workflow](https://docs.github.com/en/actions/managing-workflow-runs/disabling-and-enabling-a-workflow).
