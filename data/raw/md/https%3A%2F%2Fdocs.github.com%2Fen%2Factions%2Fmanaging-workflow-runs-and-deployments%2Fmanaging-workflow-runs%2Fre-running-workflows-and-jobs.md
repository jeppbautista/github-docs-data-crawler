  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Manage workflows and deployments](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments "Manage workflows and deployments")/
  * [Manage workflow runs](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs "Manage workflow runs")/
  * [Re-run workflows and jobs](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/re-running-workflows-and-jobs "Re-run workflows and jobs")


# Re-running workflows and jobs
You can re-run a workflow run, all failed jobs in a workflow run, or specific jobs in a workflow run up to 30 days after its initial run.
## Who can use this feature?
People with write permissions to a repository can re-run workflows in the repository.
## Tool navigation
  * [GitHub CLI](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/re-running-workflows-and-jobs?tool=cli)
  * [Web browser](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/re-running-workflows-and-jobs?tool=webui)


## In this article
  * [About re-running workflows and jobs](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/re-running-workflows-and-jobs#about-re-running-workflows-and-jobs)
  * [Re-running all the jobs in a workflow](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/re-running-workflows-and-jobs#re-running-all-the-jobs-in-a-workflow)
  * [Re-running failed jobs in a workflow](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/re-running-workflows-and-jobs#re-running-failed-jobs-in-a-workflow)
  * [Re-running a specific job in a workflow](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/re-running-workflows-and-jobs#re-running-a-specific-job-in-a-workflow)
  * [Re-running workflows and jobs with reusable workflows](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/re-running-workflows-and-jobs#re-running-workflows-and-jobs-with-reusable-workflows)
  * [Reviewing previous workflow runs](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/re-running-workflows-and-jobs#reviewing-previous-workflow-runs)


## [About re-running workflows and jobs](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/re-running-workflows-and-jobs#about-re-running-workflows-and-jobs)
Re-running a workflow or jobs in a workflow uses the same `GITHUB_SHA` (commit SHA) and `GITHUB_REF` (Git ref) of the original event that triggered the workflow run. The workflow will use the privileges of the actor who initially triggered the workflow, not the privileges of the actor who initiated the re-run. You can re-run a workflow or jobs in a workflow for up to 30 days after the initial run. You cannot re-run jobs in a workflow once its logs have passed their retention limits. For more information, see [Usage limits, billing, and administration](https://docs.github.com/en/actions/learn-github-actions/usage-limits-billing-and-administration#artifact-and-log-retention-policy). When you re-run a workflow or jobs in a workflow, you can enable debug logging for the re-run. This will enable runner diagnostic logging and step debug logging for the re-run. For more information about debug logging, see [Enabling debug logging](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/enabling-debug-logging)
## [Re-running all the jobs in a workflow](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/re-running-workflows-and-jobs#re-running-all-the-jobs-in-a-workflow)
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the tabs for the "github/docs" repository. The "Actions" tab is highlighted with an orange outline.](https://docs.github.com/assets/cb-12958/images/help/repository/actions-tab-global-nav-update.png)
  3. In the left sidebar, click the workflow you want to see.
![Screenshot of the left sidebar of the "Actions" tab. A workflow, "CodeQL," is outlined in dark orange.](https://docs.github.com/assets/cb-40551/images/help/actions/superlinter-workflow-sidebar.png)
  4. From the list of workflow runs, click the name of the run to see the workflow run summary.
  5. In the upper-right corner of the workflow, re-run jobs.
     * If any jobs failed, select the **Re-run all jobs**.
     * If no jobs failed, click **Re-run all jobs**.
  6. Optionally, to enable runner diagnostic logging and step debug logging for the re-run, select **Enable debug logging**.
  7. Click **Re-run jobs**.


To learn more about GitHub CLI, see [About GitHub CLI](https://docs.github.com/en/github-cli/github-cli/about-github-cli).
To re-run a failed workflow run, use the `run rerun` subcommand. Replace `run-id` with the ID of the failed run that you want to re-run. If you don't specify a `run-id`, GitHub CLI returns an interactive menu for you to choose a recent failed run.
```
gh run rerun RUN_ID

```

To enable runner diagnostic logging and step debug logging for the re-run, use the `--debug` flag.
```
gh run rerun RUN_ID --debug

```

To view the progress of the workflow run, use the `run watch` subcommand and select the run from the interactive list.
```
gh run watch

```

## [Re-running failed jobs in a workflow](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/re-running-workflows-and-jobs#re-running-failed-jobs-in-a-workflow)
If any jobs in a workflow run failed, you can re-run just the jobs that failed. When you re-run failed jobs in a workflow, a new workflow run will start for all failed jobs and their dependents. Any outputs for any successful jobs in the previous workflow run will be used for the re-run. Any artifacts that were created in the initial run will be available in the re-run. Any deployment protection rules that passed in the previous run will automatically pass in the re-run.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the tabs for the "github/docs" repository. The "Actions" tab is highlighted with an orange outline.](https://docs.github.com/assets/cb-12958/images/help/repository/actions-tab-global-nav-update.png)
  3. In the left sidebar, click the workflow you want to see.
![Screenshot of the left sidebar of the "Actions" tab. A workflow, "CodeQL," is outlined in dark orange.](https://docs.github.com/assets/cb-40551/images/help/actions/superlinter-workflow-sidebar.png)
  4. From the list of workflow runs, click the name of the run to see the workflow run summary.
  5. In the upper-right corner of the workflow, select the **Re-run failed jobs**.
  6. Optionally, to enable runner diagnostic logging and step debug logging for the re-run, select **Enable debug logging**.
  7. Click **Re-run jobs**.


To re-run failed jobs in a workflow run, use the `run rerun` subcommand with the `--failed` flag. Replace `run-id` with the ID of the run for which you want to re-run failed jobs. If you don't specify a `run-id`, GitHub CLI returns an interactive menu for you to choose a recent failed run.
```
gh run rerun RUN_ID --failed

```

To enable runner diagnostic logging and step debug logging for the re-run, use the `--debug` flag.
```
gh run rerun RUN_ID --failed --debug

```

## [Re-running a specific job in a workflow](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/re-running-workflows-and-jobs#re-running-a-specific-job-in-a-workflow)
When you re-run a specific job in a workflow, a new workflow run will start for the job and any dependents. Any outputs for any other jobs in the previous workflow run will be used for the re-run. Any artifacts that were created in the initial run will be available in the re-run. Any deployment protection rules that passed in the previous run will automatically pass in the re-run.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the tabs for the "github/docs" repository. The "Actions" tab is highlighted with an orange outline.](https://docs.github.com/assets/cb-12958/images/help/repository/actions-tab-global-nav-update.png)
  3. In the left sidebar, click the workflow you want to see.
![Screenshot of the left sidebar of the "Actions" tab. A workflow, "CodeQL," is outlined in dark orange.](https://docs.github.com/assets/cb-40551/images/help/actions/superlinter-workflow-sidebar.png)
  4. From the list of workflow runs, click the name of the run to see the workflow run summary.
  5. Under the "Jobs" section of the left sidebar, next to the job that you want to re-run, click 
  6. Optionally, to enable runner diagnostic logging and step debug logging for the re-run, select **Enable debug logging**.
  7. Click **Re-run jobs**.


To re-run a specific job in a workflow run, use the `run rerun` subcommand with the `--job` flag. Replace `job-id` with the ID of the job that you want to re-run.
```
gh run rerun --job JOB_ID

```

To enable runner diagnostic logging and step debug logging for the re-run, use the `--debug` flag.
```
gh run rerun --job JOB_ID --debug

```

## [Re-running workflows and jobs with reusable workflows](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/re-running-workflows-and-jobs#re-running-workflows-and-jobs-with-reusable-workflows)
Reusable workflows from public repositories can be referenced using a SHA, a release tag, or a branch name. For more information, see [Reusing workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows#calling-a-reusable-workflow).
When you re-run a workflow that uses a reusable workflow and the reference is not a SHA, there are some behaviors to be aware of:
  * Re-running all jobs in a workflow will use the reusable workflow from the specified reference. For more information about re-running all jobs in a workflow, see [Re-running workflows and jobs](https://docs.github.com/en/actions/managing-workflow-runs/re-running-workflows-and-jobs#re-running-all-the-jobs-in-a-workflow).
  * Re-running failed jobs or a specific job in a workflow will use the reusable workflow from the same commit SHA of the first attempt. For more information about re-running failed jobs in a workflow, see [Re-running workflows and jobs](https://docs.github.com/en/actions/managing-workflow-runs/re-running-workflows-and-jobs#re-running-failed-jobs-in-a-workflow). For more information about re-running a specific job in a workflow, see [Re-running workflows and jobs](https://docs.github.com/en/actions/managing-workflow-runs/re-running-workflows-and-jobs#re-running-a-specific-job-in-a-workflow).


## [Reviewing previous workflow runs](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/re-running-workflows-and-jobs#reviewing-previous-workflow-runs)
You can view the results from your previous attempts at running a workflow. You can also view previous workflow runs using the API. For more information, see [REST API endpoints for workflow runs](https://docs.github.com/en/rest/actions/workflow-runs#get-a-workflow-run).
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the tabs for the "github/docs" repository. The "Actions" tab is highlighted with an orange outline.](https://docs.github.com/assets/cb-12958/images/help/repository/actions-tab-global-nav-update.png)
  3. In the left sidebar, click the workflow you want to see.
![Screenshot of the left sidebar of the "Actions" tab. A workflow, "CodeQL," is outlined in dark orange.](https://docs.github.com/assets/cb-40551/images/help/actions/superlinter-workflow-sidebar.png)
  4. From the list of workflow runs, click the name of the run to see the workflow run summary.
  5. To the right of the run name, select the **Latest** dropdown menu and click a previous run attempt.


