  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Use cases and examples](https://docs.github.com/en/actions/use-cases-and-examples "Use cases and examples")/
  * [Deployment](https://docs.github.com/en/actions/use-cases-and-examples/deploying "Deployment")/
  * [Deploy with GitHub Actions](https://docs.github.com/en/actions/use-cases-and-examples/deploying/deploying-with-github-actions "Deploy with GitHub Actions")


# Deploying with GitHub Actions
Learn how to control deployments with features like environments and concurrency.
## In this article
  * [Introduction](https://docs.github.com/en/actions/use-cases-and-examples/deploying/deploying-with-github-actions#introduction)
  * [Prerequisites](https://docs.github.com/en/actions/use-cases-and-examples/deploying/deploying-with-github-actions#prerequisites)
  * [Triggering your deployment](https://docs.github.com/en/actions/use-cases-and-examples/deploying/deploying-with-github-actions#triggering-your-deployment)
  * [Using environments](https://docs.github.com/en/actions/use-cases-and-examples/deploying/deploying-with-github-actions#using-environments)
  * [Using concurrency](https://docs.github.com/en/actions/use-cases-and-examples/deploying/deploying-with-github-actions#using-concurrency)
  * [Viewing deployment history](https://docs.github.com/en/actions/use-cases-and-examples/deploying/deploying-with-github-actions#viewing-deployment-history)
  * [Monitoring workflow runs](https://docs.github.com/en/actions/use-cases-and-examples/deploying/deploying-with-github-actions#monitoring-workflow-runs)
  * [Tracking deployments through apps](https://docs.github.com/en/actions/use-cases-and-examples/deploying/deploying-with-github-actions#tracking-deployments-through-apps)
  * [Choosing a runner](https://docs.github.com/en/actions/use-cases-and-examples/deploying/deploying-with-github-actions#choosing-a-runner)
  * [Displaying a status badge](https://docs.github.com/en/actions/use-cases-and-examples/deploying/deploying-with-github-actions#displaying-a-status-badge)
  * [Finding deployment examples](https://docs.github.com/en/actions/use-cases-and-examples/deploying/deploying-with-github-actions#finding-deployment-examples)


## [Introduction](https://docs.github.com/en/actions/use-cases-and-examples/deploying/deploying-with-github-actions#introduction)
GitHub Actions offers features that let you control deployments. You can:
  * Trigger workflows with a variety of events.
  * Configure environments to set rules before a job can proceed and to limit access to secrets.
  * Use concurrency to control the number of deployments running at a time.


For more information about continuous deployment, see [About continuous deployment with GitHub Actions](https://docs.github.com/en/actions/deployment/about-deployments/about-continuous-deployment).
## [Prerequisites](https://docs.github.com/en/actions/use-cases-and-examples/deploying/deploying-with-github-actions#prerequisites)
You should be familiar with the syntax for GitHub Actions. For more information, see [Writing workflows](https://docs.github.com/en/actions/learn-github-actions).
## [Triggering your deployment](https://docs.github.com/en/actions/use-cases-and-examples/deploying/deploying-with-github-actions#triggering-your-deployment)
You can use a variety of events to trigger your deployment workflow. Some of the most common are: `pull_request`, `push`, and `workflow_dispatch`.
For example, a workflow with the following triggers runs whenever:
  * There is a push to the `main` branch.
  * A pull request targeting the `main` branch is opened, synchronized, or reopened.
  * Someone manually triggers it.

```
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
  workflow_dispatch:

```

For more information, see [Events that trigger workflows](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows).
## [Using environments](https://docs.github.com/en/actions/use-cases-and-examples/deploying/deploying-with-github-actions#using-environments)
Environments are used to describe a general deployment target like `production`, `staging`, or `development`. When a GitHub Actions workflow deploys to an environment, the environment is displayed on the main page of the repository. You can use environments to require approval for a job to proceed, restrict which branches can trigger a workflow, gate deployments with custom deployment protection rules, or limit access to secrets. For more information about creating environments, see [Managing environments for deployment](https://docs.github.com/en/actions/deployment/targeting-different-environments/managing-environments-for-deployment).
## [Using concurrency](https://docs.github.com/en/actions/use-cases-and-examples/deploying/deploying-with-github-actions#using-concurrency)
Concurrency ensures that only a single job or workflow using the same concurrency group will run at a time. You can use concurrency so that an environment has a maximum of one deployment in progress and one deployment pending at a time. For more information about concurrency, see [Control the concurrency of workflows and jobs](https://docs.github.com/en/actions/using-jobs/using-concurrency).
`concurrency` and `environment` are not connected. The concurrency value can be any string; it does not need to be an environment name. Additionally, if another workflow uses the same environment but does not specify concurrency, that workflow will not be subject to any concurrency rules.
For example, when the following workflow runs, it will be paused with the status `pending` if any job or workflow that uses the `production` concurrency group is in progress. It will also cancel any job or workflow that uses the `production` concurrency group and has the status `pending`. This means that there will be a maximum of one running and one pending job or workflow in that uses the `production` concurrency group.
```
name: Deployment

concurrency: production

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

You can also specify concurrency at the job level. This will allow other jobs in the workflow to proceed even if the concurrent job is `pending`.
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
    concurrency: production
    steps:
      - name: deploy
        # ...deployment-specific steps

```

You can also use `cancel-in-progress` to cancel any currently running job or workflow in the same concurrency group.
```
name: Deployment

concurrency:
  group: production
  cancel-in-progress: true

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

For guidance on writing deployment-specific steps, see [Finding deployment examples](https://docs.github.com/en/actions/use-cases-and-examples/deploying/deploying-with-github-actions#finding-deployment-examples).
## [Viewing deployment history](https://docs.github.com/en/actions/use-cases-and-examples/deploying/deploying-with-github-actions#viewing-deployment-history)
When a GitHub Actions workflow deploys to an environment, the environment is displayed on the main page of the repository. For more information about viewing deployments to environments, see [Viewing deployment history](https://docs.github.com/en/actions/deployment/managing-your-deployments/viewing-deployment-history).
## [Monitoring workflow runs](https://docs.github.com/en/actions/use-cases-and-examples/deploying/deploying-with-github-actions#monitoring-workflow-runs)
Every workflow run generates a real-time graph that illustrates the run progress. You can use this graph to monitor and debug deployments. For more information see, [Using the visualization graph](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/using-the-visualization-graph).
You can also view the logs of each workflow run and the history of workflow runs. For more information, see [Viewing workflow run history](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/viewing-workflow-run-history).
## [Tracking deployments through apps](https://docs.github.com/en/actions/use-cases-and-examples/deploying/deploying-with-github-actions#tracking-deployments-through-apps)
If your personal account or organization on GitHub is integrated with Microsoft Teams or Slack, you can track deployments that use environments through Microsoft Teams or Slack. For example, you can receive notifications through the app when a deployment is pending approval, when a deployment is approved, or when the deployment status changes. For more information about integrating Microsoft Teams or Slack, see [Featured GitHub integrations](https://docs.github.com/en/get-started/exploring-integrations/github-extensions-and-integrations#team-communication-tools).
You can also build an app that uses deployment and deployment status webhooks to track deployments. When a workflow job that references an environment runs, it creates a deployment object with the `environment` property set to the name of your environment. As the workflow progresses, it also creates deployment status objects with the `environment` property set to the name of your environment, the `environment_url` property set to the URL for environment (if specified in the workflow), and the `state` property set to the status of the job. For more information, see [GitHub Apps documentation](https://docs.github.com/en/apps) and [Webhook events and payloads](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#deployment).
## [Choosing a runner](https://docs.github.com/en/actions/use-cases-and-examples/deploying/deploying-with-github-actions#choosing-a-runner)
You can run your deployment workflow on GitHub-hosted runners or on self-hosted runners. Traffic from GitHub-hosted runners can come from a [wide range of network addresses](https://docs.github.com/en/rest/meta/meta#get-github-meta-information). If you are deploying to an internal environment and your company restricts external traffic into private networks, GitHub Actions workflows running on GitHub-hosted runners may not be able to communicate with your internal services or resources. To overcome this, you can host your own runners. For more information, see [About self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners) and [Using GitHub-hosted runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners).
## [Displaying a status badge](https://docs.github.com/en/actions/use-cases-and-examples/deploying/deploying-with-github-actions#displaying-a-status-badge)
You can use a status badge to display the status of your deployment workflow. A status badge shows whether a workflow is currently failing or passing. A common place to add a status badge is in the `README.md` file of your repository, but you can add it to any web page you'd like. By default, badges display the status of your default branch. If there are no workflow runs on your default branch, it will display the status of the most recent run across all branches. You can display the status of a workflow run for a specific branch or event using the `branch` and `event` query parameters in the URL.
![Screenshot of a workflow status badge. From right to left it shows: the GitHub logo, workflow name \("GitHub Actions Demo"\), and status \("passing"\).](https://docs.github.com/assets/cb-16218/images/help/repository/actions-workflow-status-badge.png)
For more information, see [Adding a workflow status badge](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge).
## [Finding deployment examples](https://docs.github.com/en/actions/use-cases-and-examples/deploying/deploying-with-github-actions#finding-deployment-examples)
This article demonstrated features of GitHub Actions that you can add to your deployment workflows.
GitHub offers deployment workflow templates for several popular services, such as Azure Web App. To learn how to get started using a workflow template, see [Using workflow templates](https://docs.github.com/en/actions/learn-github-actions/using-starter-workflows) or [browse the full list of deployment workflow templates](https://github.com/actions/starter-workflows/tree/main/deployments). You can also check out our more detailed guides for specific deployment workflows, such as [Deploying Node.js to Azure App Service](https://docs.github.com/en/actions/deployment/deploying-to-your-cloud-provider/deploying-to-azure/deploying-nodejs-to-azure-app-service).
Many service providers also offer actions on GitHub Marketplace for deploying to their service. For the full list, see [GitHub Marketplace](https://github.com/marketplace?category=deployment&type=actions).
