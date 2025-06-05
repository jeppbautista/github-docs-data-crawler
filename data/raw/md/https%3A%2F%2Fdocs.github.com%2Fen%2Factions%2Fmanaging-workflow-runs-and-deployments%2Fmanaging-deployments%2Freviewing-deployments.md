  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Manage workflows and deployments](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments "Manage workflows and deployments")/
  * [Manage deployments](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments "Manage deployments")/
  * [Review deployments](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/reviewing-deployments "Review deployments")


# Reviewing deployments
You can approve or reject jobs awaiting review.
## Who can use this feature?
Environments, environment secrets, and deployment protection rules are available in public repositories for all current GitHub plans. They are not available on legacy plans, such as Bronze, Silver, or Gold. For access to environments, environment secrets, and deployment branches in private or internal repositories, you must use GitHub Pro, GitHub Team, or GitHub Enterprise. If you are on a GitHub Free, GitHub Pro, or GitHub Team plan, other deployment protection rules, such as a wait timer or required reviewers, are only available for public repositories.
## In this article
  * [About required reviews in workflows](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/reviewing-deployments#about-required-reviews-in-workflows)
  * [Approving or rejecting a job](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/reviewing-deployments#approving-or-rejecting-a-job)
  * [Bypassing deployment protection rules](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/reviewing-deployments#bypassing-deployment-protection-rules)


## [About required reviews in workflows](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/reviewing-deployments#about-required-reviews-in-workflows)
Jobs that reference an environment configured with required reviewers will wait for an approval before starting. While a job is awaiting approval, it has a status of "Waiting". If a job is not approved within 30 days, it will automatically fail.
For more information about environments and required approvals, see [Managing environments for deployment](https://docs.github.com/en/actions/deployment/targeting-different-environments/managing-environments-for-deployment). For information about how to review deployments with the REST API, see [REST API endpoints for workflow runs](https://docs.github.com/en/rest/actions/workflow-runs).
## [Approving or rejecting a job](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/reviewing-deployments#approving-or-rejecting-a-job)
  1. Navigate to the workflow run that requires review. For more information about navigating to a workflow run, see [Viewing workflow run history](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/viewing-workflow-run-history).
  2. If the run requires review, you will see a notification for the review request. On the notification, click **Review deployments**.
  3. Select the job environment(s) to approve or reject. Optionally, leave a comment.
  4. Approve or reject: 
     * To approve the job, click **Approve and deploy**. Once a job is approved (and any other deployment protection rules have passed), the job will proceed. At this point, the job can access any secrets stored in the environment.
     * To reject the job, click **Reject**. If a job is rejected, the workflow will fail.


If the targeted environment is configured to prevent self-approvals for deployments, you will not be able to approve a deployment from a workflow run you initiated. For more information, see [Managing environments for deployment](https://docs.github.com/en/actions/deployment/targeting-different-environments/managing-environments-for-deployment#required-reviewers).
## [Bypassing deployment protection rules](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/reviewing-deployments#bypassing-deployment-protection-rules)
If you have configured deployment protection rules that control whether software can be deployed to an environment, you can bypass these rules and force all pending jobs referencing the environment to proceed.
  * You cannot bypass deployment protection rules if the environment has been configured to prevent admins from bypassing configured protection rules. For more information, see [Managing environments for deployment](https://docs.github.com/en/actions/deployment/targeting-different-environments/managing-environments-for-deployment#creating-an-environment).
  * You can only bypass deployment protection rules during workflow execution when a job referencing the environment is in a "Pending" state.


  1. Navigate to the workflow run. For more information about navigating to a workflow run, see [Viewing workflow run history](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/viewing-workflow-run-history).
  2. To the right of **Deployment protection rules** , click **Start all waiting jobs**. 
![Screenshot of the "Deployment protection rules" section with the "Start all waiting jobs" button outlined in orange.](https://docs.github.com/assets/cb-50220/images/actions-bypass-env-protection-rules.png)
  3. In the pop-up window, select the environments for which you want to bypass deployment protection rules.
  4. Under **Leave a comment** , enter a description for bypassing the deployment protection rules.
  5. Click **I understand the consequences, start deploying**.


