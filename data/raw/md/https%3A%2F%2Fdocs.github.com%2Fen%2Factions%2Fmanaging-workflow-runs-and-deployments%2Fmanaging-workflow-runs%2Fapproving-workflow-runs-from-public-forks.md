  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Manage workflows and deployments](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments "Manage workflows and deployments")/
  * [Manage workflow runs](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs "Manage workflow runs")/
  * [Approve public fork runs](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/approving-workflow-runs-from-public-forks "Approve public fork runs")


# Approving workflow runs from public forks
When an outside contributor submits a pull request to a public repository, a maintainer with write access may need to approve some workflow runs.
## In this article
  * [About workflow runs from public forks](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/approving-workflow-runs-from-public-forks#about-workflow-runs-from-public-forks)
  * [Approving workflow runs on a pull request from a public fork](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/approving-workflow-runs-from-public-forks#approving-workflow-runs-on-a-pull-request-from-a-public-fork)


## [About workflow runs from public forks](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/approving-workflow-runs-from-public-forks#about-workflow-runs-from-public-forks)
Anyone can fork a public repository, and then submit a pull request that proposes changes to the repository's GitHub Actions workflows. Although workflows from forks do not have access to sensitive data such as secrets, they can be an annoyance for maintainers if they are modified for abusive purposes.
To help prevent this, workflows on pull requests to public repositories from some outside contributors will not run automatically, and might need to be approved first. Depending on the "Approval for running fork pull request workflows from contributors" setting, workflows on pull requests to public repositories will not run automatically and may need approval if:
  * The pull request is **created by** a user that requires approvals based on the selected policy.
  * The pull request event is **triggered by** a user that requires approvals based on the selected policy.


By default, all first-time contributors require approval to run workflows.
Workflows triggered by `pull_request_target` events are run in the context of the base branch. Since the base branch is considered trusted, workflows triggered by these events will always run, regardless of approval settings. For more information about the `pull_request_target` event, see [Events that trigger workflows](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#pull_request_target).
These workflow approval policies are intended to restrict the set of users that can execute workflows in GitHub Actions runners that could lead to unexpected resource and compute consumption when using GitHub-hosted runners. If you are using self-hosted runners, potentially malicious user-controlled workflow code will execute automatically if the user is allowed to bypass approval in the set approval policy or if the pull request is approved. You must consider the risk of executing this code in your infrastructure and should review and follow the self-hosted runner security recommendations regardless of the approval settings utilized. See [Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions#hardening-for-self-hosted-runners).
You can configure workflow approval requirements for a [repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#configuring-required-approval-for-workflows-from-public-forks), [organization](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#configuring-required-approval-for-workflows-from-public-forks), or [enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise#enforcing-a-policy-for-fork-pull-requests-in-your-enterprise).
Workflow runs that have been awaiting approval for more than 30 days are automatically deleted.
## [Approving workflow runs on a pull request from a public fork](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/approving-workflow-runs-from-public-forks#approving-workflow-runs-on-a-pull-request-from-a-public-fork)
Maintainers with write access to a repository can use the following procedure to review and run workflows on pull requests from contributors that require approval.
  1. Under your repository name, click 
![Screenshot of the main page of a repository. In the horizontal navigation bar, a tab, labeled "Pull requests," is outlined in dark orange.](https://docs.github.com/assets/cb-51156/images/help/repository/repo-tabs-pull-requests-global-nav-update.png)
  2. In the list of pull requests, click the pull request you'd like to review.
  3. On the pull request, click 
![Screenshot of the tabs for a pull request. The "Files changed" tab is outlined in dark orange.](https://docs.github.com/assets/cb-23571/images/help/pull_requests/pull-request-tabs-changed-files.png)
  4. Inspect the proposed changes in the pull request and ensure that you are comfortable running your workflows on the pull request branch. You should be especially alert to any proposed changes in the `.github/workflows/` directory that affect workflow files.
  5. If you are comfortable with running workflows on the pull request branch, return to the **Approve and run**.


