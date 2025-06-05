  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Migrate to GitHub Actions](https://docs.github.com/en/actions/migrating-to-github-actions "Migrate to GitHub Actions")/
  * [Manual migrations](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions "Manual migrations")/
  * [Migrate from GitLab CI/CD](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions "Migrate from GitLab CI/CD")


# Migrating from GitLab CI/CD to GitHub Actions
GitHub Actions and GitLab CI/CD share several configuration similarities, which makes migrating to GitHub Actions relatively straightforward.
## In this article
  * [Introduction](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#introduction)
  * [Jobs](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#jobs)
  * [Runners](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#runners)
  * [Docker images](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#docker-images)
  * [Condition and expression syntax](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#condition-and-expression-syntax)
  * [Dependencies between Jobs](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#dependencies-between-jobs)
  * [Scheduling workflows](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#scheduling-workflows)
  * [Variables and secrets](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#variables-and-secrets)
  * [Caching](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#caching)
  * [Artifacts](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#artifacts)
  * [Databases and service containers](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#databases-and-service-containers)


## [Introduction](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#introduction)
GitLab CI/CD and GitHub Actions both allow you to create workflows that automatically build, test, publish, release, and deploy code. GitLab CI/CD and GitHub Actions share some similarities in workflow configuration:
  * Workflow configuration files are written in YAML and are stored in the code's repository.
  * Workflows include one or more jobs.
  * Jobs include one or more steps or individual commands.
  * Jobs can run on either managed or self-hosted machines.


There are a few differences, and this guide will show you the important differences so that you can migrate your workflow to GitHub Actions.
## [Jobs](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#jobs)
Jobs in GitLab CI/CD are very similar to jobs in GitHub Actions. In both systems, jobs have the following characteristics:
  * Jobs contain a series of steps or scripts that run sequentially.
  * Jobs can run on separate machines or in separate containers.
  * Jobs run in parallel by default, but can be configured to run sequentially.


You can run a script or a shell command in a job. In GitLab CI/CD, script steps are specified using the `script` key. In GitHub Actions, all scripts are specified using the `run` key.
Below is an example of the syntax for each system.
### [GitLab CI/CD syntax for jobs](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#gitlab-cicd-syntax-for-jobs)
```
job1:
  variables:
    GIT_CHECKOUT: "true"
  script:
    - echo "Run your script here"

```

### [GitHub Actions syntax for jobs](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#github-actions-syntax-for-jobs)
```
jobs:
  job1:
    steps:
      - uses: actions/checkout@v4
      - run: echo "Run your script here"

```

## [Runners](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#runners)
Runners are machines on which the jobs run. Both GitLab CI/CD and GitHub Actions offer managed and self-hosted variants of runners. In GitLab CI/CD, `tags` are used to run jobs on different platforms, while in GitHub Actions it is done with the `runs-on` key.
Below is an example of the syntax for each system.
### [GitLab CI/CD syntax for runners](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#gitlab-cicd-syntax-for-runners)
```
windows_job:
  tags:
    - windows
  script:
    - echo Hello, %USERNAME%!

linux_job:
  tags:
    - linux
  script:
    - echo "Hello, $USER!"

```

### [GitHub Actions syntax for runners](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#github-actions-syntax-for-runners)
```
windows_job:
  runs-on: windows-latest
  steps:
    - run: echo Hello, %USERNAME%!

linux_job:
  runs-on: ubuntu-latest
  steps:
    - run: echo "Hello, $USER!"

```

For more information, see [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idruns-on).
## [Docker images](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#docker-images)
Both GitLab CI/CD and GitHub Actions support running jobs in a Docker image. In GitLab CI/CD, Docker images are defined with an `image` key, while in GitHub Actions it is done with the `container` key.
Below is an example of the syntax for each system.
### [GitLab CI/CD syntax for Docker images](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#gitlab-cicd-syntax-for-docker-images)
```
my_job:
  image: node:20-bookworm-slim

```

### [GitHub Actions syntax for Docker images](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#github-actions-syntax-for-docker-images)
```
jobs:
  my_job:
    container: node:20-bookworm-slim

```

For more information, see [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idcontainer).
## [Condition and expression syntax](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#condition-and-expression-syntax)
GitLab CI/CD uses `rules` to determine if a job will run for a specific condition. GitHub Actions uses the `if` keyword to prevent a job from running unless a condition is met.
Below is an example of the syntax for each system.
### [GitLab CI/CD syntax for conditions and expressions](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#gitlab-cicd-syntax-for-conditions-and-expressions)
```
deploy_prod:
  stage: deploy
  script:
    - echo "Deploy to production server"
  rules:
    - if: '$CI_COMMIT_BRANCH == "master"'

```

### [GitHub Actions syntax for conditions and expressions](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#github-actions-syntax-for-conditions-and-expressions)
```
jobs:
  deploy_prod:
    if: contains( github.ref, 'master')
    runs-on: ubuntu-latest
    steps:
      - run: echo "Deploy to production server"

```

For more information, see [Evaluate expressions in workflows and actions](https://docs.github.com/en/actions/learn-github-actions/expressions).
## [Dependencies between Jobs](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#dependencies-between-jobs)
Both GitLab CI/CD and GitHub Actions allow you to set dependencies for a job. In both systems, jobs run in parallel by default, but job dependencies in GitHub Actions can be specified explicitly with the `needs` key. GitLab CI/CD also has a concept of `stages`, where jobs in a stage run concurrently, but the next stage will start when all the jobs in the previous stage have completed. You can recreate this scenario in GitHub Actions with the `needs` key.
Below is an example of the syntax for each system. The workflows start with two jobs named `build_a` and `build_b` running in parallel, and when those jobs complete, another job called `test_ab` will run. Finally, when `test_ab` completes, the `deploy_ab` job will run.
### [GitLab CI/CD syntax for dependencies between jobs](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#gitlab-cicd-syntax-for-dependencies-between-jobs)
```
stages:
  - build
  - test
  - deploy

build_a:
  stage: build
  script:
    - echo "This job will run first."

build_b:
  stage: build
  script:
    - echo "This job will run first, in parallel with build_a."

test_ab:
  stage: test
  script:
    - echo "This job will run after build_a and build_b have finished."

deploy_ab:
  stage: deploy
  script:
    - echo "This job will run after test_ab is complete"

```

### [GitHub Actions syntax for dependencies between jobs](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#github-actions-syntax-for-dependencies-between-jobs)
```
jobs:
  build_a:
    runs-on: ubuntu-latest
    steps:
      - run: echo "This job will be run first."

  build_b:
    runs-on: ubuntu-latest
    steps:
      - run: echo "This job will be run first, in parallel with build_a"

  test_ab:
    runs-on: ubuntu-latest
    needs: [build_a,build_b]
    steps:
      - run: echo "This job will run after build_a and build_b have finished"

  deploy_ab:
    runs-on: ubuntu-latest
    needs: [test_ab]
    steps:
      - run: echo "This job will run after test_ab is complete"

```

For more information, see [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idneeds).
## [Scheduling workflows](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#scheduling-workflows)
Both GitLab CI/CD and GitHub Actions allow you to run workflows at a specific interval. In GitLab CI/CD, pipeline schedules are configured with the UI, while in GitHub Actions you can trigger a workflow on a scheduled interval with the "on" key.
For more information, see [Events that trigger workflows](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#scheduled-events).
## [Variables and secrets](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#variables-and-secrets)
GitLab CI/CD and GitHub Actions support setting variables in the pipeline or workflow configuration file, and creating secrets using the GitLab or GitHub UI.
For more information, see [Store information in variables](https://docs.github.com/en/actions/learn-github-actions/variables) and [About secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/about-secrets).
## [Caching](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#caching)
GitLab CI/CD and GitHub Actions provide a method in the configuration file to manually cache workflow files.
Below is an example of the syntax for each system.
### [GitLab CI/CD syntax for caching](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#gitlab-cicd-syntax-for-caching)
```
image: node:latest

cache:
  key: $CI_COMMIT_REF_SLUG
  paths:
    - .npm/

before_script:
  - npm ci --cache .npm --prefer-offline

test_async:
  script:
    - node ./specs/start.js ./specs/async.spec.js

```

### [GitHub Actions syntax for caching](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#github-actions-syntax-for-caching)
```
jobs:
  test_async:
    runs-on: ubuntu-latest
    steps:
    - name: Cache node modules
      uses: actions/cache@v4
      with:
        path: ~/.npm
        key: v1-npm-deps-${{ hashFiles('**/package-lock.json') }}
        restore-keys: v1-npm-deps-

```

## [Artifacts](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#artifacts)
Both GitLab CI/CD and GitHub Actions can upload files and directories created by a job as artifacts. In GitHub Actions, artifacts can be used to persist data across multiple jobs.
Below is an example of the syntax for each system.
### [GitLab CI/CD syntax for artifacts](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#gitlab-cicd-syntax-for-artifacts)
```
script:
artifacts:
  paths:
    - math-homework.txt

```

### [GitHub Actions syntax for artifacts](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#github-actions-syntax-for-artifacts)
```
- name: Upload math result for job 1
  uses: actions/upload-artifact@v4
  with:
    name: homework
    path: math-homework.txt

```

For more information, see [Storing and sharing data from a workflow](https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts).
## [Databases and service containers](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#databases-and-service-containers)
Both systems enable you to include additional containers for databases, caching, or other dependencies.
In GitLab CI/CD, a container for the job is specified with the `image` key, while GitHub Actions uses the `container` key. In both systems, additional service containers are specified with the `services` key.
Below is an example of the syntax for each system.
### [GitLab CI/CD syntax for databases and service containers](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#gitlab-cicd-syntax-for-databases-and-service-containers)
```
container-job:
  variables:
    POSTGRES_PASSWORD: postgres
    # The hostname used to communicate with the
    # PostgreSQL service container
    POSTGRES_HOST: postgres
    # The default PostgreSQL port
    POSTGRES_PORT: 5432
  image: node:20-bookworm-slim
  services:
    - postgres
  script:
    # Performs a clean installation of all dependencies
    # in the `package.json` file
    - npm ci
    # Runs a script that creates a PostgreSQL client,
    # populates the client with data, and retrieves data
    - node client.js
  tags:
    - docker

```

### [GitHub Actions syntax for databases and service containers](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-gitlab-cicd-to-github-actions#github-actions-syntax-for-databases-and-service-containers)
```
jobs:
  container-job:
    runs-on: ubuntu-latest
    container: node:20-bookworm-slim

    services:
      postgres:
        image: postgres
        env:
          POSTGRES_PASSWORD: postgres

    steps:
      - name: Check out repository code
        uses: actions/checkout@v4

      # Performs a clean installation of all dependencies
      # in the `package.json` file
      - name: Install dependencies
        run: npm ci

      - name: Connect to PostgreSQL
        # Runs a script that creates a PostgreSQL client,
        # populates the client with data, and retrieves data
        run: node client.js
        env:
          # The hostname used to communicate with the
          # PostgreSQL service container
          POSTGRES_HOST: postgres
          # The default PostgreSQL port
          POSTGRES_PORT: 5432

```

For more information, see [About service containers](https://docs.github.com/en/actions/using-containerized-services/about-service-containers).
