  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Write workflows](https://docs.github.com/en/actions/writing-workflows "Write workflows")/
  * [About workflows](https://docs.github.com/en/actions/writing-workflows/about-workflows "About workflows")


# About workflows
Get a high-level overview of GitHub Actions workflows, including triggers, syntax, and advanced features.
## In this article
  * [About workflows](https://docs.github.com/en/actions/writing-workflows/about-workflows#about-workflows)
  * [Workflow basics](https://docs.github.com/en/actions/writing-workflows/about-workflows#workflow-basics)
  * [Triggering a workflow](https://docs.github.com/en/actions/writing-workflows/about-workflows#triggering-a-workflow)
  * [Workflow syntax](https://docs.github.com/en/actions/writing-workflows/about-workflows#workflow-syntax)
  * [Using workflow templates](https://docs.github.com/en/actions/writing-workflows/about-workflows#using-workflow-templates)
  * [Advanced workflow features](https://docs.github.com/en/actions/writing-workflows/about-workflows#advanced-workflow-features)


## [About workflows](https://docs.github.com/en/actions/writing-workflows/about-workflows#about-workflows)
A **workflow** is a configurable automated process that will run one or more jobs. Workflows are defined by a YAML file checked in to your repository and will run when triggered by an event in your repository, or they can be triggered manually, or at a defined schedule.
Workflows are defined in the `.github/workflows` directory in a repository. A repository can have multiple workflows, each of which can perform a different set of tasks such as:
  * Building and testing pull requests
  * Deploying your application every time a release is created
  * Adding a label whenever a new issue is opened


## [Workflow basics](https://docs.github.com/en/actions/writing-workflows/about-workflows#workflow-basics)
A workflow must contain the following basic components:
  1. One or more _events_ that will trigger the workflow.
  2. One or more _jobs_ , each of which will execute on a _runner_ machine and run a series of one or more _steps_.
  3. Each step can either run a script that you define or run an action, which is a reusable extension that can simplify your workflow.


For more information on these basic components, see [Understanding GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions#the-components-of-github-actions).
![Diagram of an event triggering Runner 1 to run Job 1, which triggers Runner 2 to run Job 2. Each of the jobs is broken into multiple steps.](https://docs.github.com/assets/cb-25535/images/help/actions/overview-actions-simple.png)
## [Triggering a workflow](https://docs.github.com/en/actions/writing-workflows/about-workflows#triggering-a-workflow)
Workflow triggers are events that cause a workflow to run. These events can be:
  * Events that occur in your workflow's repository
  * Events that occur outside of GitHub and trigger a `repository_dispatch` event on GitHub
  * Scheduled times
  * Manual


For example, you can configure your workflow to run when a push is made to the default branch of your repository, when a release is created, or when an issue is opened.
For more information, see [Triggering a workflow](https://docs.github.com/en/actions/using-workflows/triggering-a-workflow), and for a full list of events, see [Events that trigger workflows](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows).
## [Workflow syntax](https://docs.github.com/en/actions/writing-workflows/about-workflows#workflow-syntax)
Workflows are defined using YAML. For the full reference of the YAML syntax for authoring workflows, see [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#about-yaml-syntax-for-workflows).
For more on managing workflow runs, such as re-running, cancelling, or deleting a workflow run, see [Managing workflow runs and deployments](https://docs.github.com/en/actions/managing-workflow-runs).
## [Using workflow templates](https://docs.github.com/en/actions/writing-workflows/about-workflows#using-workflow-templates)
GitHub provides preconfigured workflow templates that you can use as-is or customize to create your own workflow. GitHub analyzes your code and shows you workflow templates that might be useful for your repository. For example, if your repository contains Node.js code, you'll see suggestions for Node.js projects.
These workflow templates are designed to help you get up and running quickly, offering a range of configurations such as:
  * CI: [Continuous Integration workflows](https://github.com/actions/starter-workflows/tree/main/ci)
  * Deployments: [Deployment workflows](https://github.com/actions/starter-workflows/tree/main/deployments)
  * Automation: [Automating workflows](https://github.com/actions/starter-workflows/tree/main/automation)
  * Code Scanning: [Code Scanning workflows](https://github.com/actions/starter-workflows/tree/main/code-scanning)
  * Pages: [Pages workflows](https://github.com/actions/starter-workflows/tree/main/pages)


Use these workflows as a starting place to build your custom workflow or use them as-is. You can browse the full list of workflow templates in the [actions/starter-workflows](https://github.com/actions/starter-workflows) repository. For more information, see [Using workflow templates](https://docs.github.com/en/actions/writing-workflows/using-starter-workflows).
## [Advanced workflow features](https://docs.github.com/en/actions/writing-workflows/about-workflows#advanced-workflow-features)
This section briefly describes some of the advanced features of GitHub Actions that help you create more complex workflows.
### [Storing secrets](https://docs.github.com/en/actions/writing-workflows/about-workflows#storing-secrets)
If your workflows use sensitive data, such as passwords or certificates, you can save these in GitHub as _secrets_ and then use them in your workflows as environment variables. This means that you will be able to create and share workflows without having to embed sensitive values directly in the workflow's YAML source.
This example job demonstrates how to reference an existing secret as an environment variable, and send it as a parameter to an example command.
```
jobs:
  example-job:
    runs-on: ubuntu-latest
    steps:
      - name: Retrieve secret
        env:
          super_secret: ${{ secrets.SUPERSECRET }}
        run: |
          example-command "$super_secret"

```

For more information, see [Using secrets in GitHub Actions](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions).
### [Creating dependent jobs](https://docs.github.com/en/actions/writing-workflows/about-workflows#creating-dependent-jobs)
By default, the jobs in your workflow all run in parallel at the same time. If you have a job that must only run after another job has completed, you can use the `needs` keyword to create this dependency. If one of the jobs fails, all dependent jobs are skipped; however, if you need the jobs to continue, you can define this using the `if` conditional statement.
In this example, the `setup`, `build`, and `test` jobs run in series, with `build` and `test` being dependent on the successful completion of the job that precedes them:
```
jobs:
  setup:
    runs-on: ubuntu-latest
    steps:
      - run: ./setup_server.sh
  build:
    needs: setup
    runs-on: ubuntu-latest
    steps:
      - run: ./build_server.sh
  test:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - run: ./test_server.sh

```

For more information, see [Using jobs in a workflow](https://docs.github.com/en/actions/using-jobs/using-jobs-in-a-workflow#defining-prerequisite-jobs).
### [Using a matrix](https://docs.github.com/en/actions/writing-workflows/about-workflows#using-a-matrix)
A matrix strategy lets you use variables in a single job definition to automatically create multiple job runs that are based on the combinations of the variables. For example, you can use a matrix strategy to test your code in multiple versions of a language or on multiple operating systems. The matrix is created using the `strategy` keyword, which receives the build options as an array. For example, this matrix will run the job multiple times, using different versions of Node.js:
```
jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node: [14, 16]
    steps:
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}

```

For more information, see [Running variations of jobs in a workflow](https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs).
### [Caching dependencies](https://docs.github.com/en/actions/writing-workflows/about-workflows#caching-dependencies)
If your jobs regularly reuse dependencies, you can consider caching these files to help improve performance. Once the cache is created, it is available to all workflows in the same repository.
This example demonstrates how to cache the `~/.npm` directory:
```
jobs:
  example-job:
    steps:
      - name: Cache node modules
        uses: actions/cache@v4
        env:
          cache-name: cache-node-modules
        with:
          path: ~/.npm
          key: ${{ runner.os }}-build-${{ env.cache-name }}-${{ hashFiles('**/package-lock.json') }}
          restore-keys: |
            ${{ runner.os }}-build-${{ env.cache-name }}-

```

For more information, see [Caching dependencies to speed up workflows](https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows).
### [Using databases and service containers](https://docs.github.com/en/actions/writing-workflows/about-workflows#using-databases-and-service-containers)
If your job requires a database or cache service, you can use the [`services`](https://docs.github.com/en/actions/using-jobs/running-jobs-in-a-container) keyword to create an ephemeral container to host the service; the resulting container is then available to all steps in that job and is removed when the job has completed. This example demonstrates how a job can use `services` to create a `postgres` container, and then use `node` to connect to the service.
```
jobs:
  container-job:
    runs-on: ubuntu-latest
    container: node:20-bookworm-slim
    services:
      postgres:
        image: postgres
    steps:
      - name: Check out repository code
        uses: actions/checkout@v4
      - name: Install dependencies
        run: npm ci
      - name: Connect to PostgreSQL
        run: node client.js
        env:
          POSTGRES_HOST: postgres
          POSTGRES_PORT: 5432

```

For more information, see [Using containerized services](https://docs.github.com/en/actions/using-containerized-services).
### [Using labels to route workflows](https://docs.github.com/en/actions/writing-workflows/about-workflows#using-labels-to-route-workflows)
If you want to be sure that a particular type of runner will process your job, you can use labels to control where jobs are executed. You can assign labels to a self-hosted runner in addition to their default label of `self-hosted`. Then, you can refer to these labels in your YAML workflow, ensuring that the job is routed in a predictable way. GitHub-hosted runners have predefined labels assigned.
This example shows how a workflow can use labels to specify the required runner:
```
jobs:
  example-job:
    runs-on: [self-hosted, linux, x64, gpu]

```

A workflow will only run on a runner that has all the labels in the `runs-on` array. The job will preferentially go to an idle self-hosted runner with the specified labels. If none are available and a GitHub-hosted runner with the specified labels exists, the job will go to a GitHub-hosted runner.
To learn more about self-hosted runner labels, see [Using labels with self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/using-labels-with-self-hosted-runners).
To learn more about GitHub-hosted runner labels, see [Using GitHub-hosted runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners#supported-runners-and-hardware-resources).
### [Reusing workflows](https://docs.github.com/en/actions/writing-workflows/about-workflows#reusing-workflows)
You can call one workflow from within another workflow. This allows you to reuse workflows, avoiding duplication and making your workflows easier to maintain. For more information, see [Reusing workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows).
### [Security hardening for workflows](https://docs.github.com/en/actions/writing-workflows/about-workflows#security-hardening-for-workflows)
GitHub provides security features that you can use to increase the security of your workflows. You can use GitHub's built-in features to ensure you are notified about vulnerabilities in the actions you consume, or to automate the process of keeping the actions in your workflows up to date. For more information, see [Using GitHub's security features to secure your use of GitHub Actions](https://docs.github.com/en/actions/security-guides/using-githubs-security-features-to-secure-your-use-of-github-actions).
### [Using environments](https://docs.github.com/en/actions/writing-workflows/about-workflows#using-environments)
You can configure environments with protection rules and secrets to control the execution of jobs in a workflow. Each job in a workflow can reference a single environment. Any protection rules configured for the environment must pass before a job referencing the environment is sent to a runner. For more information, see [Managing environments for deployment](https://docs.github.com/en/actions/deployment/targeting-different-environments/managing-environments-for-deployment).
