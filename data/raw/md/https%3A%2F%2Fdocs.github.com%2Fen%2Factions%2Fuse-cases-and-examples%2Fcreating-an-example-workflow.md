  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Use cases and examples](https://docs.github.com/en/actions/use-cases-and-examples "Use cases and examples")/
  * [Create an example workflow](https://docs.github.com/en/actions/use-cases-and-examples/creating-an-example-workflow "Create an example workflow")


# Creating an example workflow
Learn how to create a basic workflow that is triggered by a push event.
## In this article
  * [Introduction](https://docs.github.com/en/actions/use-cases-and-examples/creating-an-example-workflow#introduction)
  * [Creating an example workflow](https://docs.github.com/en/actions/use-cases-and-examples/creating-an-example-workflow#creating-an-example-workflow)
  * [Understanding the workflow file](https://docs.github.com/en/actions/use-cases-and-examples/creating-an-example-workflow#understanding-the-workflow-file)
  * [Viewing the activity for a workflow run](https://docs.github.com/en/actions/use-cases-and-examples/creating-an-example-workflow#viewing-the-activity-for-a-workflow-run)


## [Introduction](https://docs.github.com/en/actions/use-cases-and-examples/creating-an-example-workflow#introduction)
This guide shows you how to create a basic workflow that is triggered when code is pushed to your repository.
To get started with preconfigured workflows, browse through the list of templates in the [actions/starter-workflows](https://github.com/actions/starter-workflows) repository. For more information, see [Using workflow templates](https://docs.github.com/en/actions/writing-workflows/using-starter-workflows).
## [Creating an example workflow](https://docs.github.com/en/actions/use-cases-and-examples/creating-an-example-workflow#creating-an-example-workflow)
GitHub Actions uses YAML syntax to define the workflow. Each workflow is stored as a separate YAML file in your code repository, in a directory named `.github/workflows`.
You can create an example workflow in your repository that automatically triggers a series of commands whenever code is pushed. In this workflow, GitHub Actions checks out the pushed code, installs the [bats](https://www.npmjs.com/package/bats) testing framework, and runs a basic command to output the bats version: `bats -v`.
  1. In your repository, create the `.github/workflows/` directory to store your workflow files.
  2. In the `.github/workflows/` directory, create a new file called `learn-github-actions.yml` and add the following code.
YAML```
name: learn-github-actions
run-name: ${{ github.actor }} is learning GitHub Actions
on: [push]
jobs:
  check-bats-version:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm install -g bats
      - run: bats -v

```
```
name: learn-github-actions
run-name: ${{ github.actor }} is learning GitHub Actions
on: [push]
jobs:
  check-bats-version:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm install -g bats
      - run: bats -v

```

  3. Commit these changes and push them to your GitHub repository.


Your new GitHub Actions workflow file is now installed in your repository and will run automatically each time someone pushes a change to the repository. To see the details about a workflow's execution history, see [Viewing the activity for a workflow run](https://docs.github.com/en/actions/use-cases-and-examples/creating-an-example-workflow#viewing-the-activity-for-a-workflow-run).
## [Understanding the workflow file](https://docs.github.com/en/actions/use-cases-and-examples/creating-an-example-workflow#understanding-the-workflow-file)
To help you understand how YAML syntax is used to create a workflow file, this section explains each line of the introduction's example:
YAML
BesideInline
```
# Optional - The name of the workflow as it will appear in the "Actions" tab of the GitHub repository. If this field is omitted, the name of the workflow file will be used instead.
name: learn-github-actions

# Optional - The name for workflow runs generated from the workflow, which will appear in the list of workflow runs on your repository's "Actions" tab. This example uses an expression with the `github` context to display the username of the actor that triggered the workflow run. For more information, see [AUTOTITLE](/actions/using-workflows/workflow-syntax-for-github-actions#run-name).
run-name: ${{ github.actor }} is learning GitHub Actions

# Specifies the trigger for this workflow. This example uses the `push` event, so a workflow run is triggered every time someone pushes a change to the repository or merges a pull request. This is triggered by a push to every branch; for examples of syntax that runs only on pushes to specific branches, paths, or tags, see [AUTOTITLE](/actions/reference/workflow-syntax-for-github-actions#onpushpull_requestpull_request_targetpathspaths-ignore).
on: [push]

# Groups together all the jobs that run in the `learn-github-actions` workflow.
jobs:

# Defines a job named `check-bats-version`. The child keys will define properties of the job.
  check-bats-version:

# Configures the job to run on the latest version of an Ubuntu Linux runner. This means that the job will execute on a fresh virtual machine hosted by GitHub. For syntax examples using other runners, see [AUTOTITLE](/actions/reference/workflow-syntax-for-github-actions#jobsjob_idruns-on)
    runs-on: ubuntu-latest

# Groups together all the steps that run in the `check-bats-version` job. Each item nested under this section is a separate action or shell script.
    steps:

# The `uses` keyword specifies that this step will run `v4` of the `actions/checkout` action. This is an action that checks out your repository onto the runner, allowing you to run scripts or other actions against your code (such as build and test tools). You should use the checkout action any time your workflow will use the repository's code.
      - uses: actions/checkout@v4

# This step uses the `actions/setup-node@v4` action to install the specified version of the Node.js. (This example uses version 20.) This puts both the `node` and `npm` commands in your `PATH`.
      - uses: actions/setup-node@v4
        with:
          node-version: '20'

# The `run` keyword tells the job to execute a command on the runner. In this case, you are using `npm` to install the `bats` software testing package.
      - run: npm install -g bats

# Finally, you'll run the `bats` command with a parameter that outputs the software version.
      - run: bats -v

```

```
name: learn-github-actions
```

Optional - The name of the workflow as it will appear in the "Actions" tab of the GitHub repository. If this field is omitted, the name of the workflow file will be used instead.
```
run-name: ${{ github.actor }} is learning GitHub Actions
```

Optional - The name for workflow runs generated from the workflow, which will appear in the list of workflow runs on your repository's "Actions" tab. This example uses an expression with the `github` context to display the username of the actor that triggered the workflow run. For more information, see [AUTOTITLE](https://docs.github.com/actions/using-workflows/workflow-syntax-for-github-actions#run-name).
```
on: [push]
```

Specifies the trigger for this workflow. This example uses the `push` event, so a workflow run is triggered every time someone pushes a change to the repository or merges a pull request. This is triggered by a push to every branch; for examples of syntax that runs only on pushes to specific branches, paths, or tags, see [AUTOTITLE](https://docs.github.com/actions/reference/workflow-syntax-for-github-actions#onpushpull_requestpull_request_targetpathspaths-ignore).
```
jobs:
```

Groups together all the jobs that run in the `learn-github-actions` workflow.
```
  check-bats-version:
```

Defines a job named `check-bats-version`. The child keys will define properties of the job.
```
    runs-on: ubuntu-latest
```

Configures the job to run on the latest version of an Ubuntu Linux runner. This means that the job will execute on a fresh virtual machine hosted by GitHub. For syntax examples using other runners, see [AUTOTITLE](https://docs.github.com/actions/reference/workflow-syntax-for-github-actions#jobsjob_idruns-on)
```
    steps:
```

Groups together all the steps that run in the `check-bats-version` job. Each item nested under this section is a separate action or shell script.
```
      - uses: actions/checkout@v4
```

The `uses` keyword specifies that this step will run `v4` of the `actions/checkout` action. This is an action that checks out your repository onto the runner, allowing you to run scripts or other actions against your code (such as build and test tools). You should use the checkout action any time your workflow will use the repository's code.
```
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
```

This step uses the `actions/setup-node@v4` action to install the specified version of the Node.js. (This example uses version 20.) This puts both the `node` and `npm` commands in your `PATH`.
```
      - run: npm install -g bats
```

The `run` keyword tells the job to execute a command on the runner. In this case, you are using `npm` to install the `bats` software testing package.
```
      - run: bats -v
```

Finally, you'll run the `bats` command with a parameter that outputs the software version.
```
# Optional - The name of the workflow as it will appear in the "Actions" tab of the GitHub repository. If this field is omitted, the name of the workflow file will be used instead.
name: learn-github-actions

# Optional - The name for workflow runs generated from the workflow, which will appear in the list of workflow runs on your repository's "Actions" tab. This example uses an expression with the `github` context to display the username of the actor that triggered the workflow run. For more information, see [AUTOTITLE](/actions/using-workflows/workflow-syntax-for-github-actions#run-name).
run-name: ${{ github.actor }} is learning GitHub Actions

# Specifies the trigger for this workflow. This example uses the `push` event, so a workflow run is triggered every time someone pushes a change to the repository or merges a pull request. This is triggered by a push to every branch; for examples of syntax that runs only on pushes to specific branches, paths, or tags, see [AUTOTITLE](/actions/reference/workflow-syntax-for-github-actions#onpushpull_requestpull_request_targetpathspaths-ignore).
on: [push]

# Groups together all the jobs that run in the `learn-github-actions` workflow.
jobs:

# Defines a job named `check-bats-version`. The child keys will define properties of the job.
  check-bats-version:

# Configures the job to run on the latest version of an Ubuntu Linux runner. This means that the job will execute on a fresh virtual machine hosted by GitHub. For syntax examples using other runners, see [AUTOTITLE](/actions/reference/workflow-syntax-for-github-actions#jobsjob_idruns-on)
    runs-on: ubuntu-latest

# Groups together all the steps that run in the `check-bats-version` job. Each item nested under this section is a separate action or shell script.
    steps:

# The `uses` keyword specifies that this step will run `v4` of the `actions/checkout` action. This is an action that checks out your repository onto the runner, allowing you to run scripts or other actions against your code (such as build and test tools). You should use the checkout action any time your workflow will use the repository's code.
      - uses: actions/checkout@v4

# This step uses the `actions/setup-node@v4` action to install the specified version of the Node.js. (This example uses version 20.) This puts both the `node` and `npm` commands in your `PATH`.
      - uses: actions/setup-node@v4
        with:
          node-version: '20'

# The `run` keyword tells the job to execute a command on the runner. In this case, you are using `npm` to install the `bats` software testing package.
      - run: npm install -g bats

# Finally, you'll run the `bats` command with a parameter that outputs the software version.
      - run: bats -v

```

### [Visualizing the workflow file](https://docs.github.com/en/actions/use-cases-and-examples/creating-an-example-workflow#visualizing-the-workflow-file)
In this diagram, you can see the workflow file you just created and how the GitHub Actions components are organized in a hierarchy. Each step executes a single action or shell script. Steps 1 and 2 run actions, while steps 3 and 4 run shell scripts. To find more prebuilt actions for your workflows, see [Using pre-written building blocks in your workflow](https://docs.github.com/en/actions/learn-github-actions/finding-and-customizing-actions).
![Diagram showing the trigger, runner, and job of a workflow. The job is broken into 4 steps.](https://docs.github.com/assets/cb-34473/images/help/actions/overview-actions-event.png)
## [Viewing the activity for a workflow run](https://docs.github.com/en/actions/use-cases-and-examples/creating-an-example-workflow#viewing-the-activity-for-a-workflow-run)
When your workflow is triggered, a _workflow run_ is created that executes the workflow. After a workflow run has started, you can see a visualization graph of the run's progress and view each step's activity on GitHub.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the tabs for the "github/docs" repository. The "Actions" tab is highlighted with an orange outline.](https://docs.github.com/assets/cb-12958/images/help/repository/actions-tab-global-nav-update.png)
  3. In the left sidebar, click the workflow you want to see.
![Screenshot of the left sidebar of the "Actions" tab. A workflow, "CodeQL," is outlined in dark orange.](https://docs.github.com/assets/cb-40551/images/help/actions/superlinter-workflow-sidebar.png)
  4. From the list of workflow runs, click the name of the run to see the workflow run summary.
  5. In the left sidebar or in the visualization graph, click the job you want to see.
  6. To view the results of a step, click the step.


