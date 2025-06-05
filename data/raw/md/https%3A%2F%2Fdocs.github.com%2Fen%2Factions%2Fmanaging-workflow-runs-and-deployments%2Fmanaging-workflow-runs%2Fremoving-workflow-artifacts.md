  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Manage workflows and deployments](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments "Manage workflows and deployments")/
  * [Manage workflow runs](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs "Manage workflow runs")/
  * [Remove workflow artifacts](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/removing-workflow-artifacts "Remove workflow artifacts")


# Removing workflow artifacts
You can reclaim used GitHub Actions storage by deleting artifacts before they expire on GitHub.
## In this article
  * [Deleting an artifact](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/removing-workflow-artifacts#deleting-an-artifact)
  * [Setting the retention period for an artifact](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/removing-workflow-artifacts#setting-the-retention-period-for-an-artifact)
  * [Finding the expiration date of an artifact](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/removing-workflow-artifacts#finding-the-expiration-date-of-an-artifact)
  * [Artifacts from deleted workflow runs](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/removing-workflow-artifacts#artifacts-from-deleted-workflow-runs)


## [Deleting an artifact](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/removing-workflow-artifacts#deleting-an-artifact)
Once you delete an artifact, it cannot be restored.
Write access to the repository is required to perform these steps.
By default, GitHub stores build logs and artifacts for 90 days, and this retention period can be customized. For more information, see [Usage limits, billing, and administration](https://docs.github.com/en/actions/learn-github-actions/usage-limits-billing-and-administration#artifact-and-log-retention-policy).
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the tabs for the "github/docs" repository. The "Actions" tab is highlighted with an orange outline.](https://docs.github.com/assets/cb-12958/images/help/repository/actions-tab-global-nav-update.png)
  3. In the left sidebar, click the workflow you want to see.
![Screenshot of the left sidebar of the "Actions" tab. A workflow, "CodeQL," is outlined in dark orange.](https://docs.github.com/assets/cb-40551/images/help/actions/superlinter-workflow-sidebar.png)
  4. From the list of workflow runs, click the name of the run to see the workflow run summary.
  5. Under **Artifacts** , click 
![Screenshot showing artifacts created during a workflow run. A trash can icon, used to remove an artifact, is outlined in dark orange.](https://docs.github.com/assets/cb-14510/images/help/repository/actions-delete-artifact-updated.png)


## [Setting the retention period for an artifact](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/removing-workflow-artifacts#setting-the-retention-period-for-an-artifact)
Retention periods for artifacts and logs can be configured at the repository, organization, and enterprise level. For more information, see [Usage limits, billing, and administration](https://docs.github.com/en/actions/learn-github-actions/usage-limits-billing-and-administration#artifact-and-log-retention-policy).
You can also define a custom retention period for individual artifacts using the `actions/upload-artifact` action in a workflow. For more information, see [Storing and sharing data from a workflow](https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts#configuring-a-custom-artifact-retention-period).
## [Finding the expiration date of an artifact](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/removing-workflow-artifacts#finding-the-expiration-date-of-an-artifact)
You can use the API to confirm the date that an artifact is scheduled to be deleted. For more information, see the `expires_at` value returned by the REST API. For more information, see [REST API endpoints for GitHub Actions artifacts](https://docs.github.com/en/rest/actions/artifacts).
## [Artifacts from deleted workflow runs](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/removing-workflow-artifacts#artifacts-from-deleted-workflow-runs)
When a workflow run is deleted all artifacts associated with the run are also deleted from storage. You can delete a workflow run using the GitHub Actions UI, the REST API, or using the GitHub CLI, see: [Deleting a workflow run](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/deleting-a-workflow-run), [Delete a workflow run](https://docs.github.com/en/rest/actions/workflow-runs?apiVersion=2022-11-28#delete-a-workflow-run), or [gh run delete](https://cli.github.com/manual/gh_run_delete).
