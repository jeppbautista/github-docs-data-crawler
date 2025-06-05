  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Migrate to GitHub Actions](https://docs.github.com/en/actions/migrating-to-github-actions "Migrate to GitHub Actions")/
  * [Manual migrations](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions "Manual migrations")/
  * [Migrate from Travis CI](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions "Migrate from Travis CI")


# Migrating from Travis CI to GitHub Actions
GitHub Actions and Travis CI share multiple similarities, which helps make it relatively straightforward to migrate to GitHub Actions.
## In this article
  * [Introduction](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#introduction)
  * [Before you start](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#before-you-start)
  * [Comparing job execution](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#comparing-job-execution)
  * [Key similarities](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#key-similarities)
  * [Key features in GitHub Actions](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#key-features-in-github-actions)
  * [Executing scripts](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#executing-scripts)
  * [Error handling in GitHub Actions](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#error-handling-in-github-actions)
  * [Migrating syntax for conditionals and expressions](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#migrating-syntax-for-conditionals-and-expressions)
  * [Migrating phases to steps](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#migrating-phases-to-steps)
  * [Caching dependencies](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#caching-dependencies)
  * [Examples of common tasks](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#examples-of-common-tasks)
  * [Next steps](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#next-steps)


## [Introduction](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#introduction)
This guide helps you migrate from Travis CI to GitHub Actions. It compares their concepts and syntax, describes the similarities, and demonstrates their different approaches to common tasks.
## [Before you start](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#before-you-start)
Before starting your migration to GitHub Actions, it would be useful to become familiar with how it works:
  * For a quick example that demonstrates a GitHub Actions job, see [Quickstart for GitHub Actions](https://docs.github.com/en/actions/quickstart).
  * To learn the essential GitHub Actions concepts, see [Understanding GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions).


## [Comparing job execution](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#comparing-job-execution)
To give you control over when CI tasks are executed, a GitHub Actions _workflow_ uses _jobs_ that run in parallel by default. Each job contains _steps_ that are executed in a sequence that you define. If you need to run setup and cleanup actions for a job, you can define steps in each job to perform these.
## [Key similarities](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#key-similarities)
GitHub Actions and Travis CI share certain similarities, and understanding these ahead of time can help smooth the migration process.
### [Using YAML syntax](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#using-yaml-syntax)
Travis CI and GitHub Actions both use YAML to create jobs and workflows, and these files are stored in the code's repository. For more information on how GitHub Actions uses YAML, see [Understanding GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions#create-an-example-workflow).
### [Custom variables](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#custom-variables)
Travis CI lets you set variables and share them between stages. Similarly, GitHub Actions lets you define variables for a workflow. For more information, see [Store information in variables](https://docs.github.com/en/actions/learn-github-actions/variables).
### [Default variables](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#default-variables)
Travis CI and GitHub Actions both include default environment variables that you can use in your YAML files. For GitHub Actions, you can see these listed in [Store information in variables](https://docs.github.com/en/actions/learn-github-actions/variables#default-environment-variables).
### [Parallel job processing](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#parallel-job-processing)
Travis CI can use `stages` to run jobs in parallel. Similarly, GitHub Actions runs `jobs` in parallel. For more information, see [About workflows](https://docs.github.com/en/actions/using-workflows/about-workflows#creating-dependent-jobs).
### [Status badges](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#status-badges)
Travis CI and GitHub Actions both support status badges, which let you indicate whether a build is passing or failing. For more information, see [Adding a workflow status badge](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge).
### [Using a matrix](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#using-a-matrix)
Travis CI and GitHub Actions both support a matrix, allowing you to perform testing using combinations of operating systems and software packages. For more information, see [Running variations of jobs in a workflow](https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs).
Below is an example comparing the syntax for each system.
#### [Travis CI syntax for a matrix](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#travis-ci-syntax-for-a-matrix)
```
matrix:
  include:
    - rvm: '2.5'
    - rvm: '2.6.3'

```

#### [GitHub Actions syntax for a matrix](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#github-actions-syntax-for-a-matrix)
```
jobs:
  build:
    strategy:
      matrix:
        ruby: ['2.5', '2.6.3']

```

### [Targeting specific branches](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#targeting-specific-branches)
Travis CI and GitHub Actions both allow you to target your CI to a specific branch. For more information, see [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onpushbranchestagsbranches-ignoretags-ignore).
Below is an example of the syntax for each system.
#### [Travis CI syntax for targeting specific branches](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#travis-ci-syntax-for-targeting-specific-branches)
```
branches:
  only:
    - main
    - 'mona/octocat'

```

#### [GitHub Actions syntax for targeting specific branches](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#github-actions-syntax-for-targeting-specific-branches)
```
on:
  push:
    branches:
      - main
      - 'mona/octocat'

```

### [Checking out submodules](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#checking-out-submodules)
Travis CI and GitHub Actions both allow you to control whether submodules are included in the repository clone.
Below is an example of the syntax for each system.
#### [Travis CI syntax for checking out submodules](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#travis-ci-syntax-for-checking-out-submodules)
```
git:
  submodules: false

```

#### [GitHub Actions syntax for checking out submodules](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#github-actions-syntax-for-checking-out-submodules)
```
- uses: actions/checkout@v4
  with:
    submodules: false

```

### [Using environment variables in a matrix](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#using-environment-variables-in-a-matrix)
Travis CI and GitHub Actions can both add custom variables to a test matrix, which allows you to refer to the variable in a later step.
In GitHub Actions, you can use the `include` key to add custom environment variables to a matrix. In this example, the matrix entries for `node-version` are each configured to use different values for the `site` and `datacenter` environment variables. The `Echo site details` step then uses `env: ${{ matrix.env }}` to refer to the custom variables:
```
name: Node.js CI
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
       include:
         - node-version: '14.x'
           site: "prod"
           datacenter: "site-a"
         - node-version: '16.x'
           site: "dev"
           datacenter: "site-b"
    steps:
      - name: Echo site details
        env:
          SITE: ${{ matrix.site }}
          DATACENTER: ${{ matrix.datacenter }}
        run: echo $SITE $DATACENTER

```

## [Key features in GitHub Actions](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#key-features-in-github-actions)
When migrating from Travis CI, consider the following key features in GitHub Actions:
### [Storing secrets](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#storing-secrets)
GitHub Actions allows you to store secrets and reference them in your jobs. GitHub Actions organizations can limit which repositories can access organization secrets. Deployment protection rules can require manual approval for a workflow to access environment secrets. For more information, see [About secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/about-secrets).
### [Sharing files between jobs and workflows](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#sharing-files-between-jobs-and-workflows)
GitHub Actions includes integrated support for artifact storage, allowing you to share files between jobs in a workflow. You can also save the resulting files and share them with other workflows. For more information, see [Understanding GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/essential-features-of-github-actions#sharing-data-between-jobs).
### [Hosting your own runners](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#hosting-your-own-runners)
If your jobs require specific hardware or software, GitHub Actions allows you to host your own runners and send your jobs to them for processing. GitHub Actions also lets you use policies to control how these runners are accessed, granting access at the organization or repository level. For more information, see [Hosting your own runners](https://docs.github.com/en/actions/hosting-your-own-runners).
### [Concurrent jobs and execution time](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#concurrent-jobs-and-execution-time)
The concurrent jobs and workflow execution times in GitHub Actions can vary depending on your GitHub plan. For more information, see [Usage limits, billing, and administration](https://docs.github.com/en/actions/learn-github-actions/usage-limits-billing-and-administration).
### [Using different languages in GitHub Actions](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#using-different-languages-in-github-actions)
When working with different languages in GitHub Actions, you can create a step in your job to set up your language dependencies. For more information about working with a particular language, see [Building and testing](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing).
## [Executing scripts](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#executing-scripts)
GitHub Actions can use `run` steps to run scripts or shell commands. To use a particular shell, you can specify the `shell` type when providing the path to the script. For more information, see [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstepsrun).
For example:
```
steps:
  - name: Run build script
    run: ./.github/scripts/build.sh
    shell: bash

```

## [Error handling in GitHub Actions](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#error-handling-in-github-actions)
When migrating to GitHub Actions, there are different approaches to error handling that you might need to be aware of.
### [Script error handling](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#script-error-handling)
GitHub Actions stops a job immediately if one of the steps returns an error code. For more information, see [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#exit-codes-and-error-action-preference).
### [Job error handling](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#job-error-handling)
GitHub Actions uses `if` conditionals to execute jobs or steps in certain situations. For example, you can run a step when another step results in a `failure()`. For more information, see [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#example-using-status-check-functions). You can also use [`continue-on-error`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idcontinue-on-error) to prevent a workflow run from stopping when a job fails.
## [Migrating syntax for conditionals and expressions](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#migrating-syntax-for-conditionals-and-expressions)
To run jobs under conditional expressions, Travis CI and GitHub Actions share a similar `if` condition syntax. GitHub Actions lets you use the `if` conditional to prevent a job or step from running unless a condition is met. For more information, see [Evaluate expressions in workflows and actions](https://docs.github.com/en/actions/learn-github-actions/expressions).
This example demonstrates how an `if` conditional can control whether a step is executed:
```
jobs:
  conditional:
    runs-on: ubuntu-latest
    steps:
      - run: echo "This step runs with str equals 'ABC' and num equals 123"
        if: env.str == 'ABC' && env.num == 123

```

## [Migrating phases to steps](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#migrating-phases-to-steps)
Where Travis CI uses _phases_ to run _steps_ , GitHub Actions has _steps_ which execute _actions_. You can find prebuilt actions in the [GitHub Marketplace](https://github.com/marketplace?type=actions), or you can create your own actions. For more information, see [Sharing automations](https://docs.github.com/en/actions/creating-actions).
Below is an example of the syntax for each system.
### [Travis CI syntax for phases and steps](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#travis-ci-syntax-for-phases-and-steps)
```
language: python
python:
  - "3.7"

script:
  - python script.py

```

### [GitHub Actions syntax for steps and actions](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#github-actions-syntax-for-steps-and-actions)
```
jobs:
  run_python:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/setup-python@v5
        with:
          python-version: '3.7'
          architecture: 'x64'
      - run: python script.py

```

## [Caching dependencies](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#caching-dependencies)
Travis CI and GitHub Actions let you manually cache dependencies for later reuse.
These examples demonstrate the cache syntax for each system.
### [Travis CI syntax for caching](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#travis-ci-syntax-for-caching)
```
language: node_js
cache: npm

```

### [GitHub Actions syntax for caching](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#github-actions-syntax-for-caching)
```
- name: Cache node modules
  uses: actions/cache@v4
  with:
    path: ~/.npm
    key: v1-npm-deps-${{ hashFiles('**/package-lock.json') }}
    restore-keys: v1-npm-deps-

```

## [Examples of common tasks](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#examples-of-common-tasks)
This section compares how GitHub Actions and Travis CI perform common tasks.
### [Configuring environment variables](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#configuring-environment-variables)
You can create custom environment variables in a GitHub Actions job.
#### [Travis CI syntax for an environment variable](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#travis-ci-syntax-for-an-environment-variable)
```
env:
  - MAVEN_PATH="/usr/local/maven"

```

#### [GitHub Actions workflow with an environment variable](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#github-actions-workflow-with-an-environment-variable)
```
jobs:
  maven-build:
    env:
      MAVEN_PATH: '/usr/local/maven'

```

### [Building with Node.js](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#building-with-nodejs)
#### [Travis CI for building with Node.js](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#travis-ci-for-building-with-nodejs)
```
install:
  - npm install
script:
  - npm run build
  - npm test

```

#### [GitHub Actions workflow for building with Node.js](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#github-actions-workflow-for-building-with-nodejs)
```
name: Node.js CI
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Use Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '16.x'
      - run: npm install
      - run: npm run build
      - run: npm test

```

## [Next steps](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions#next-steps)
To continue learning about the main features of GitHub Actions, see [Writing workflows](https://docs.github.com/en/actions/learn-github-actions).
