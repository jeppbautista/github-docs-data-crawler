  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Manage workflows and deployments](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments "Manage workflows and deployments")/
  * [Manage workflow runs](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs "Manage workflow runs")/
  * [Cancel a workflow](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/canceling-a-workflow "Cancel a workflow")


# Canceling a workflow
You can cancel a workflow run that is in progress. When you cancel a workflow run, GitHub cancels all jobs and steps that are a part of that workflow.
## In this article
  * [Canceling a workflow run](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/canceling-a-workflow#canceling-a-workflow-run)
  * [Steps GitHub takes to cancel a workflow run](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/canceling-a-workflow#steps-github-takes-to-cancel-a-workflow-run)


Write access to the repository is required to perform these steps.
## [Canceling a workflow run](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/canceling-a-workflow#canceling-a-workflow-run)
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the tabs for the "github/docs" repository. The "Actions" tab is highlighted with an orange outline.](https://docs.github.com/assets/cb-12958/images/help/repository/actions-tab-global-nav-update.png)
  3. In the left sidebar, click the workflow you want to see.
![Screenshot of the left sidebar of the "Actions" tab. A workflow, "CodeQL," is outlined in dark orange.](https://docs.github.com/assets/cb-40551/images/help/actions/superlinter-workflow-sidebar.png)
  4. From the list of workflow runs, click the name of the `queued` or `in progress` run that you want to cancel.
  5. In the upper-right corner of the workflow, click **Cancel workflow**. 
![Screenshot showing the summary for a workflow that is currently running. The "Cancel workflow" button is highlighted with a dark orange outline.](https://docs.github.com/assets/cb-35999/images/help/repository/cancel-check-suite-updated.png)


## [Steps GitHub takes to cancel a workflow run](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/canceling-a-workflow#steps-github-takes-to-cancel-a-workflow-run)
When canceling workflow run, you may be running other software that uses resources that are related to the workflow run. To help you free up resources related to the workflow run, it may help to understand the steps GitHub performs to cancel a workflow run.
  1. To cancel the workflow run, the server re-evaluates `if` conditions for all currently running jobs. If the condition evaluates to `true`, the job will not get canceled. For example, the condition `if: always()` would evaluate to true and the job continues to run. When there is no condition, that is the equivalent of the condition `if: success()`, which only runs if the previous step finished successfully.
  2. For jobs that need to be canceled, the server sends a cancellation message to all the runner machines with jobs that need to be canceled.
  3. For jobs that continue to run, the server re-evaluates `if` conditions for the unfinished steps. If the condition evaluates to `true`, the step continues to run. You can use the `cancelled` expression to apply a status check of `cancelled()`. For more information see [Evaluate expressions in workflows and actions](https://docs.github.com/en/actions/learn-github-actions/expressions#cancelled).
  4. For steps that need to be canceled, the runner machine sends `SIGINT/Ctrl-C` to the step's entry process (`node` for javascript action, `docker` for container action, and `bash/cmd/pwd` when using `run` in a step). If the process doesn't exit within 7500 ms, the runner will send `SIGTERM/Ctrl-Break` to the process, then wait for 2500 ms for the process to exit. If the process is still running, the runner kills the process tree.
  5. After the 5 minutes cancellation timeout period, the server will force terminate all jobs and steps that don't finish running or fail to complete the cancellation process.


