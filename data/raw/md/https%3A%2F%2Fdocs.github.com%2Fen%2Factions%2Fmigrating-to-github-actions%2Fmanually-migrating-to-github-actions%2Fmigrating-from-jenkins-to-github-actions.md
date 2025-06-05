  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Migrate to GitHub Actions](https://docs.github.com/en/actions/migrating-to-github-actions "Migrate to GitHub Actions")/
  * [Manual migrations](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions "Manual migrations")/
  * [Migrate from Jenkins](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-jenkins-to-github-actions "Migrate from Jenkins")


# Migrating from Jenkins to GitHub Actions
GitHub Actions and Jenkins share multiple similarities, which makes migration to GitHub Actions relatively straightforward.
## In this article
  * [Introduction](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-jenkins-to-github-actions#introduction)
  * [Key differences](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-jenkins-to-github-actions#key-differences)
  * [Comparing capabilities](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-jenkins-to-github-actions#comparing-capabilities)
  * [Using directives](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-jenkins-to-github-actions#using-directives)
  * [Using sequential stages](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-jenkins-to-github-actions#using-sequential-stages)
  * [Examples of common tasks](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-jenkins-to-github-actions#examples-of-common-tasks)


## [Introduction](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-jenkins-to-github-actions#introduction)
Jenkins and GitHub Actions both allow you to create workflows that automatically build, test, publish, release, and deploy code. Jenkins and GitHub Actions share some similarities in workflow configuration:
  * Jenkins creates workflows using _Declarative Pipelines_ , which are similar to GitHub Actions workflow files.
  * Jenkins uses _stages_ to run a collection of steps, while GitHub Actions uses jobs to group one or more steps or individual commands.
  * Jenkins and GitHub Actions support container-based builds. For more information, see [Creating a Docker container action](https://docs.github.com/en/actions/creating-actions/creating-a-docker-container-action).
  * Steps or tasks can be reused and shared with the community.


For more information, see [Understanding GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions).
## [Key differences](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-jenkins-to-github-actions#key-differences)
  * Jenkins has two types of syntax for creating pipelines: Declarative Pipeline and Scripted Pipeline. GitHub Actions uses YAML to create workflows and configuration files. For more information, see [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions).
  * Jenkins deployments are typically self-hosted, with users maintaining the servers in their own data centers. GitHub Actions offers a hybrid cloud approach by hosting its own runners that you can use to run jobs, while also supporting self-hosted runners. For more information, see [About self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners).


## [Comparing capabilities](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-jenkins-to-github-actions#comparing-capabilities)
### [Distributing your builds](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-jenkins-to-github-actions#distributing-your-builds)
Jenkins lets you send builds to a single build agent, or you can distribute them across multiple agents. You can also classify these agents according to various attributes, such as operating system types.
Similarly, GitHub Actions can send jobs to GitHub-hosted or self-hosted runners, and you can use labels to classify runners according to various attributes. For more information, see [Understanding GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions#runners) and [About self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners).
### [Using sections to organize pipelines](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-jenkins-to-github-actions#using-sections-to-organize-pipelines)
Jenkins splits its Declarative Pipelines into multiple sections. Similarly, GitHub Actions organizes its workflows into separate sections. The table below compares Jenkins sections with the GitHub Actions workflow.
Jenkins Directives | GitHub Actions  
---|---  
[`agent`](https://jenkins.io/doc/book/pipeline/syntax/#agent) |  [`jobs.<job_id>.runs-on`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idruns-on)   
[`jobs.<job_id>.container`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idcontainer)  
[`post`](https://jenkins.io/doc/book/pipeline/syntax/#post) | None  
[`stages`](https://jenkins.io/doc/book/pipeline/syntax/#stages) | [`jobs`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobs)  
[`steps`](https://jenkins.io/doc/book/pipeline/syntax/#steps) | [`jobs.<job_id>.steps`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idsteps)  
## [Using directives](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-jenkins-to-github-actions#using-directives)
Jenkins uses directives to manage _Declarative Pipelines_. These directives define the characteristics of your workflow and how it will execute. The table below demonstrates how these directives map to concepts within GitHub Actions.
Jenkins Directives | GitHub Actions  
---|---  
[`environment`](https://jenkins.io/doc/book/pipeline/syntax/#environment) |  [`jobs.<job_id>.env`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#env)   
[`jobs.<job_id>.steps[*].env`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstepsenv)  
[`options`](https://jenkins.io/doc/book/pipeline/syntax/#parameters) |  [`jobs.<job_id>.strategy`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstrategy)   
[`jobs.<job_id>.strategy.fail-fast`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstrategyfail-fast)   
[`jobs.<job_id>.timeout-minutes`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idtimeout-minutes)  
[`parameters`](https://jenkins.io/doc/book/pipeline/syntax/#parameters) |  [`inputs`](https://docs.github.com/en/actions/creating-actions/metadata-syntax-for-github-actions#inputs)   
[`outputs`](https://docs.github.com/en/actions/creating-actions/metadata-syntax-for-github-actions#outputs-for-docker-container-and-javascript-actions)  
[`triggers`](https://jenkins.io/doc/book/pipeline/syntax/#triggers) |  [`on`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#on)   
[`on.<event_name>.types`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onevent_nametypes)   
[`on.<push>.<branches|tags>`](https://docs.github.com/en/actions/automating-your-workflow-with-github-actions/workflow-syntax-for-github-actions#onpushbranchestagsbranches-ignoretags-ignore)   
[`on.<pull_request>.<branches>`](https://docs.github.com/en/actions/automating-your-workflow-with-github-actions/workflow-syntax-for-github-actions#onpull_requestpull_request_targetbranchesbranches-ignore)   
[`on.<push|pull_request>.paths`](https://docs.github.com/en/actions/automating-your-workflow-with-github-actions/workflow-syntax-for-github-actions#onpushpull_requestpull_request_targetpathspaths-ignore)  
[`triggers { upstreamprojects() }`](https://jenkins.io/doc/book/pipeline/syntax/#triggers) | [`jobs.<job_id>.needs`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idneeds)  
[Jenkins cron syntax](https://jenkins.io/doc/book/pipeline/syntax/#cron-syntax) | [`on.schedule`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onschedule)  
[`stage`](https://jenkins.io/doc/book/pipeline/syntax/#stage) |  [`jobs.<job_id>`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_id)   
[`jobs.<job_id>.name`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idname)  
[`tools`](https://jenkins.io/doc/book/pipeline/syntax/#tools) | [Specifications for GitHub-hosted runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners#supported-software)  
[`input`](https://jenkins.io/doc/book/pipeline/syntax/#input) | [`inputs`](https://docs.github.com/en/actions/creating-actions/metadata-syntax-for-github-actions#inputs)  
[`when`](https://jenkins.io/doc/book/pipeline/syntax/#when) | [`jobs.<job_id>.if`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idif)  
## [Using sequential stages](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-jenkins-to-github-actions#using-sequential-stages)
### [Parallel job processing](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-jenkins-to-github-actions#parallel-job-processing)
Jenkins can run the `stages` and `steps` in parallel, while GitHub Actions currently only runs jobs in parallel.
Jenkins Parallel | GitHub Actions  
---|---  
[`parallel`](https://jenkins.io/doc/book/pipeline/syntax/#parallel) | [`jobs.<job_id>.strategy.max-parallel`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstrategymax-parallel)  
### [Matrix](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-jenkins-to-github-actions#matrix)
Both GitHub Actions and Jenkins let you use a matrix to define various system combinations.
Jenkins | GitHub Actions  
---|---  
[`axis`](https://jenkins.io/doc/book/pipeline/syntax/#matrix-axes) |  [`strategy/matrix`](https://docs.github.com/en/actions/using-workflows/about-workflows#using-a-build-matrix)   
[`context`](https://docs.github.com/en/actions/learn-github-actions/contexts)  
[`stages`](https://jenkins.io/doc/book/pipeline/syntax/#matrix-stages) | [`steps-context`](https://docs.github.com/en/actions/learn-github-actions/contexts#steps-context)  
[`excludes`](https://jenkins.io/doc/book/pipeline/syntax/#matrix-stages) | None  
### [Using steps to execute tasks](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-jenkins-to-github-actions#using-steps-to-execute-tasks)
Jenkins groups `steps` together in `stages`. Each of these steps can be a script, function, or command, among others. Similarly, GitHub Actions uses `jobs` to execute specific groups of `steps`.
Jenkins | GitHub Actions  
---|---  
[`steps`](https://jenkins.io/doc/book/pipeline/syntax/#steps) | [`jobs.<job_id>.steps`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idsteps)  
## [Examples of common tasks](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-jenkins-to-github-actions#examples-of-common-tasks)
### [Scheduling a pipeline to run with `cron`](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-jenkins-to-github-actions#scheduling-a-pipeline-to-run-with-cron)
#### [Jenkins pipeline with `cron`](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-jenkins-to-github-actions#jenkins-pipeline-with-cron)
```
pipeline {
  agent any
  triggers {
    cron('H/15 * * * 1-5')
  }
}

```

#### [GitHub Actions workflow with `cron`](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-jenkins-to-github-actions#github-actions-workflow-with-cron)
```
on:
  schedule:
    - cron: '*/15 * * * 1-5'

```

### [Configuring environment variables in a pipeline](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-jenkins-to-github-actions#configuring-environment-variables-in-a-pipeline)
#### [Jenkins pipeline with an environment variable](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-jenkins-to-github-actions#jenkins-pipeline-with-an-environment-variable)
```
pipeline {
  agent any
  environment {
    MAVEN_PATH = '/usr/local/maven'
  }
}

```

#### [GitHub Actions workflow with an environment variable](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-jenkins-to-github-actions#github-actions-workflow-with-an-environment-variable)
```
jobs:
  maven-build:
    env:
      MAVEN_PATH: '/usr/local/maven'

```

### [Building from upstream projects](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-jenkins-to-github-actions#building-from-upstream-projects)
#### [Jenkins pipeline that builds from an upstream project](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-jenkins-to-github-actions#jenkins-pipeline-that-builds-from-an-upstream-project)
```
pipeline {
  triggers {
    upstream(
      upstreamProjects: 'job1,job2',
      threshold: hudson.model.Result.SUCCESS
    )
  }
}

```

#### [GitHub Actions workflow that builds from an upstream project](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-jenkins-to-github-actions#github-actions-workflow-that-builds-from-an-upstream-project)
```
jobs:
  job1:
  job2:
    needs: job1
  job3:
    needs: [job1, job2]

```

### [Building with multiple operating systems](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-jenkins-to-github-actions#building-with-multiple-operating-systems)
#### [Jenkins pipeline that builds with multiple operating systems](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-jenkins-to-github-actions#jenkins-pipeline-that-builds-with-multiple-operating-systems)
```
pipeline {
  agent none
  stages {
    stage('Run Tests') {
      matrix {
        axes {
          axis {
            name: 'PLATFORM'
            values: 'macos', 'linux'
          }
        }
        agent { label "${PLATFORM}" }
        stages {
          stage('test') {
            tools { nodejs "node-20" }
            steps {
              dir("scripts/myapp") {
                sh(script: "npm install -g bats")
                sh(script: "bats tests")
              }
            }
          }
        }
      }
    }
  }
}

```

#### [GitHub Actions workflow that builds with multiple operating systems](https://docs.github.com/en/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-jenkins-to-github-actions#github-actions-workflow-that-builds-with-multiple-operating-systems)
```
name: demo-workflow
on:
  push:
jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false
      matrix:
        os: [macos-latest, ubuntu-latest]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm install -g bats
      - run: bats tests
        working-directory: ./scripts/myapp

```

