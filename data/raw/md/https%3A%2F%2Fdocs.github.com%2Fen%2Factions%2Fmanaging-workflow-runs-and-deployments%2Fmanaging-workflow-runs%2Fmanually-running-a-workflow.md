  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Manage workflows and deployments](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments "Manage workflows and deployments")/
  * [Manage workflow runs](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs "Manage workflow runs")/
  * [Manually run a workflow](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/manually-running-a-workflow "Manually run a workflow")


# Manually running a workflow
When a workflow is configured to run on the `workflow_dispatch` event, you can run the workflow using the Actions tab on GitHub, GitHub CLI, or the REST API.
## Tool navigation
  * [GitHub CLI](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/manually-running-a-workflow?tool=cli)
  * [Web browser](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/manually-running-a-workflow?tool=webui)


## In this article
  * [Configuring a workflow to run manually](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/manually-running-a-workflow#configuring-a-workflow-to-run-manually)
  * [Running a workflow](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/manually-running-a-workflow#running-a-workflow)
  * [Running a workflow using the REST API](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/manually-running-a-workflow#running-a-workflow-using-the-rest-api)


## [Configuring a workflow to run manually](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/manually-running-a-workflow#configuring-a-workflow-to-run-manually)
To run a workflow manually, the workflow must be configured to run on the `workflow_dispatch` event.
To trigger the `workflow_dispatch` event, your workflow must be in the default branch. For more information about configuring the `workflow_dispatch` event, see [Events that trigger workflows](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#workflow_dispatch).
Write access to the repository is required to perform these steps.
## [Running a workflow](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/manually-running-a-workflow#running-a-workflow)
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the tabs for the "github/docs" repository. The "Actions" tab is highlighted with an orange outline.](https://docs.github.com/assets/cb-12958/images/help/repository/actions-tab-global-nav-update.png)
  3. In the left sidebar, click the name of the workflow you want to run.
![Screenshot of the "Actions" page. In the left sidebar, a workflow name is highlighted with an outline in dark orange.](https://docs.github.com/assets/cb-60473/images/help/repository/actions-select-workflow-2022.png)
  4. Above the list of workflow runs, click the **Run workflow** button.
To see the **Run workflow** button, your workflow file must use the `workflow_dispatch` event trigger. Only workflow files that use the `workflow_dispatch` event trigger will have the option to run the workflow manually using the **Run workflow** button. For more information about configuring the `workflow_dispatch` event, see [Events that trigger workflows](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#workflow_dispatch).
![Screenshot of a workflow page. Above the list of workflow runs, a button, labeled "Run workflow", is outlined in dark orange.](https://docs.github.com/assets/cb-52943/images/help/actions/actions-workflow-dispatch.png)
  5. Select the **Branch** dropdown menu and click a branch to run the workflow on.
  6. If the workflow requires input, fill in the fields.
  7. Click **Run workflow**.


To learn more about GitHub CLI, see [About GitHub CLI](https://docs.github.com/en/github-cli/github-cli/about-github-cli).
To run a workflow, use the `workflow run` subcommand. Replace the `workflow` parameter with either the name, ID, or file name of the workflow you want to run. For example, `"Link Checker"`, `1234567`, or `"link-check-test.yml"`. If you don't specify a workflow, GitHub CLI returns an interactive menu for you to choose a workflow.
```
gh workflow run WORKFLOW

```

If your workflow accepts inputs, GitHub CLI will prompt you to enter them. Alternatively, you can use `-f` or `-F` to add an input in `key=value` format. Use `-F` to read from a file.
```
gh workflow run greet.yml -f name=mona -f greeting=hello -F data=@myfile.txt

```

You can also pass inputs as JSON by using standard input.
```
echo '{"name":"mona", "greeting":"hello"}' | gh workflow run greet.yml --json

```

To run a workflow on a branch other than the repository's default branch, use the `--ref` flag.
```
gh workflow run WORKFLOW --ref BRANCH

```

To view the progress of the workflow run, use the `run watch` subcommand and select the run from the interactive list.
```
gh run watch

```

## [Running a workflow using the REST API](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/manually-running-a-workflow#running-a-workflow-using-the-rest-api)
When using the REST API, you configure the `inputs` and `ref` as request body parameters. If the inputs are omitted, the default values defined in the workflow file are used.
You can define up to 10 `inputs` for a `workflow_dispatch` event.
For more information about using the REST API, see [REST API endpoints for workflows](https://docs.github.com/en/rest/actions/workflows#create-a-workflow-dispatch-event).
