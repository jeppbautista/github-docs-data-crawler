  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Write workflows](https://docs.github.com/en/actions/writing-workflows "Write workflows")/
  * [Choose what workflows do](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does "Choose what workflows do")/
  * [Environments](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-environments-for-deployment "Environments")


# Using environments for deployment
Specify a deployment environment in your workflow.
## In this article
  * [About environments](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-environments-for-deployment#about-environments)
  * [Using an environment in a workflow](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-environments-for-deployment#using-an-environment-in-a-workflow)


## [About environments](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-environments-for-deployment#about-environments)
Environments are used to describe a general deployment target like `production`, `staging`, or `development`. When a GitHub Actions workflow deploys to an environment, the environment is displayed on the main page of the repository. You can use environments to require approval for a job to proceed, restrict which branches can trigger a workflow, gate deployments with custom deployment protection rules, or limit access to secrets. For more information about creating environments, see [Managing environments for deployment](https://docs.github.com/en/actions/deployment/targeting-different-environments/managing-environments-for-deployment).
Each job in a workflow can reference a single environment. Any protection rules configured for the environment must pass before a job referencing the environment is sent to a runner. The job can access the environment's secrets only after the job is sent to a runner.
When a workflow references an environment, the environment will appear in the repository's deployments. For more information about viewing current and previous deployments, see [Viewing deployment history](https://docs.github.com/en/actions/deployment/managing-your-deployments/viewing-deployment-history).
## [Using an environment in a workflow](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-environments-for-deployment#using-an-environment-in-a-workflow)
You can specify an environment for each job in your workflow. To do so, add a [`jobs.<job_id>.environment`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idenvironment) key followed by the name of the environment.
For example, this workflow will use an environment called `production`.
```
name: Deployment

on:
  push:
    branches:
      - main

jobs:
  deployment:
    runs-on: ubuntu-latest
    environment: production
    steps:
      - name: deploy
        # ...deployment-specific steps

```

When the above workflow runs, the `deployment` job will be subject to any rules configured for the `production` environment. For example, if the environment requires reviewers, the job will pause until one of the reviewers approves the job.
You can also specify a URL for the environment. The specified URL will appear on the deployments page for the repository (accessed by clicking **Environments** on the home page of your repository) and in the visualization graph for the workflow run. If a pull request triggered the workflow, the URL is also displayed as a **View deployment** button in the pull request timeline. When using the "Require deployments to succeed before merging" rule, only the `name` specified is being checked even if a URL has also been specified. See [About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches#require-deployments-to-succeed-before-merging).
```
name: Deployment

on:
  push:
    branches:
      - main

jobs:
  deployment:
    runs-on: ubuntu-latest
    environment: 
      name: production
      url: https://github.com
    steps:
      - name: deploy
        # ...deployment-specific steps

```

