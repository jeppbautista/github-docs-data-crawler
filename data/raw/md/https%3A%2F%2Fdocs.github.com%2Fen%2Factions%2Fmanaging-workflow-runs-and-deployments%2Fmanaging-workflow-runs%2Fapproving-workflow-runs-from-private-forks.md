  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Manage workflows and deployments](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments "Manage workflows and deployments")/
  * [Manage workflow runs](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs "Manage workflow runs")/
  * [Approve private fork runs](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/approving-workflow-runs-from-private-forks "Approve private fork runs")


# Approving workflow runs from private forks
When someone without write access submits a pull request to a private repository, a maintainer may need to approve any workflow runs.
## Who can use this feature?
Maintainers with write access to a repository can approve workflow runs.
## In this article
  * [About workflow runs from private forks](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/approving-workflow-runs-from-private-forks#about-workflow-runs-from-private-forks)
  * [Approving workflow runs on a pull request from a private fork](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/approving-workflow-runs-from-private-forks#approving-workflow-runs-on-a-pull-request-from-a-private-fork)


## [About workflow runs from private forks](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/approving-workflow-runs-from-private-forks#about-workflow-runs-from-private-forks)
If you rely on using forks of your private repositories, you can configure policies that control how users can run workflows on `pull_request` events. Available to private repositories only, you can configure these policy settings for organizations or repositories. For more information, see [Enforcing policies for GitHub Actions in your enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise#enforcing-a-policy-for-fork-pull-requests-in-private-repositories).
## [Approving workflow runs on a pull request from a private fork](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/approving-workflow-runs-from-private-forks#approving-workflow-runs-on-a-pull-request-from-a-private-fork)
Maintainers with write access to a repository can use the following procedure to review and run workflows on pull requests from contributors that require approval.
  1. Under your repository name, click 
![Screenshot of the main page of a repository. In the horizontal navigation bar, a tab, labeled "Pull requests," is outlined in dark orange.](https://docs.github.com/assets/cb-51156/images/help/repository/repo-tabs-pull-requests-global-nav-update.png)
  2. In the list of pull requests, click the pull request you'd like to review.
  3. On the pull request, click 
![Screenshot of the tabs for a pull request. The "Files changed" tab is outlined in dark orange.](https://docs.github.com/assets/cb-23571/images/help/pull_requests/pull-request-tabs-changed-files.png)
  4. Inspect the proposed changes in the pull request and ensure that you are comfortable running your workflows on the pull request branch. You should be especially alert to any proposed changes in the `.github/workflows/` directory that affect workflow files.
  5. If you are comfortable with running workflows on the pull request branch, return to the **Approve and run**.


