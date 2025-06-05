  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [GitHub-hosted runners](https://docs.github.com/en/actions/using-github-hosted-runners "GitHub-hosted runners")/
  * [Using larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners "Using larger runners")/
  * [Run jobs on larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/running-jobs-on-larger-runners "Run jobs on larger runners")


# Running jobs on larger runners
You can speed up your workflows by configuring them to run on larger runners.
## Who can use this feature?
Larger runners are only available for organizations and enterprises using the GitHub Team or GitHub Enterprise Cloud plans.
## Platform navigation
  * [Mac](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/running-jobs-on-larger-runners?platform=mac)
  * [Windows](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/running-jobs-on-larger-runners?platform=windows)
  * [Linux](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/running-jobs-on-larger-runners?platform=linux)


## In this article
  * [Running jobs on your runner](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/running-jobs-on-larger-runners#running-jobs-on-your-runner)
  * [Available macOS larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/running-jobs-on-larger-runners#available-macos-larger-runners)
  * [Viewing available runners for a repository](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/running-jobs-on-larger-runners#viewing-available-runners-for-a-repository)
  * [Using groups to control where jobs are run](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/running-jobs-on-larger-runners#using-groups-to-control-where-jobs-are-run)
  * [Using groups to control where jobs are run](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/running-jobs-on-larger-runners#using-groups-to-control-where-jobs-are-run-1)
  * [Using labels to control where jobs are run](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/running-jobs-on-larger-runners#using-labels-to-control-where-jobs-are-run)
  * [Using labels to control where jobs are run](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/running-jobs-on-larger-runners#using-labels-to-control-where-jobs-are-run-1)
  * [Targeting macOS larger runners in a workflow](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/running-jobs-on-larger-runners#targeting-macos-larger-runners-in-a-workflow)
  * [Using labels and groups to control where jobs are run](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/running-jobs-on-larger-runners#using-labels-and-groups-to-control-where-jobs-are-run)
  * [Using labels and groups to control where jobs are run](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/running-jobs-on-larger-runners#using-labels-and-groups-to-control-where-jobs-are-run-1)
  * [Troubleshooting larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/running-jobs-on-larger-runners#troubleshooting-larger-runners)


## [Running jobs on your runner](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/running-jobs-on-larger-runners#running-jobs-on-your-runner)
Once your runner type has been defined, you can update your workflow YAML files to send jobs to your newly created runner instances for processing. You can use runner groups or labels to define where your jobs run.
Larger runners are automatically assigned a default label that corresponds to the runner name. You cannot add custom labels to larger runners, but you can use the default labels or the runner's group to send jobs to specific types of runners.
Only owner or administrator accounts can see the runner settings. Non-administrative users can contact the organization owner to find out which runners are enabled. Your organization owner can create new runners and runner groups, as well as configure permissions to specify which repositories can access a runner group. For more information, see [Managing larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/managing-larger-runners#allowing-repositories-to-access-a-runner-group).
Once your runner type has been defined, you can update your workflow YAML files to send jobs to your newly created runner instances for processing. You can use runner groups or labels to define where your jobs run.
Larger runners are automatically assigned a default label that corresponds to the runner name. You cannot add custom labels to larger runners, but you can use the default labels or the runner's group to send jobs to specific types of runners.
Only owner or administrator accounts can see the runner settings. Non-administrative users can contact the organization owner to find out which runners are enabled. Your organization owner can create new runners and runner groups, as well as configure permissions to specify which repositories can access a runner group. For more information, see [Managing larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/managing-larger-runners#allowing-repositories-to-access-a-runner-group).
Once your runner type has been defined, you can update your workflow YAML files to send jobs to runner instances for processing. To run jobs on macOS larger runners, update the `runs-on` key in your workflow YAML files to use one of the GitHub-defined labels for macOS runners. For more information, see [Available macOS larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/running-jobs-on-larger-runners#available-macos-larger-runners).
## [Available macOS larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/running-jobs-on-larger-runners#available-macos-larger-runners)
Use the labels in the table below to run your workflows on the corresponding macOS larger runner.
Runner Size | Architecture | Processor (CPU) | Memory (RAM) | Storage (SSD) | Workflow label  
---|---|---|---|---|---  
Large | Intel | 12 | 30 GB | 14 GB |  `macos-latest-large`, `macos-13-large`, `macos-14-large` [latest], `macos-15-large`  
XLarge | arm64 (M1) | 6 (+ 8 GPU hardware acceleration) | 14 GB | 14 GB |  `macos-latest-xlarge`, `macos-13-xlarge` , `macos-14-xlarge` [latest], `macos-15-xlarge`  
For macOS larger runners, the `-latest` runner label uses the macOS 12 runner image. For macOS Xlarge, the `-latest` runner label uses the macOS 13 runner image
## [Viewing available runners for a repository](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/running-jobs-on-larger-runners#viewing-available-runners-for-a-repository)
If you have `repo: write` access to a repository, you can view a list of the runners available to the repository.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the tabs for the "github/docs" repository. The "Actions" tab is highlighted with an orange outline.](https://docs.github.com/assets/cb-12958/images/help/repository/actions-tab-global-nav-update.png)
  3. In the left sidebar, under the "Management" section, click 
  4. Review the list of available runners for the repository.
  5. Optionally, to copy a runner's label to use it in a workflow, click **Copy label**.


Enterprise and organization owners can create runners from this page. To create a new runner, click **New runner** at the top right of the list of runners to add runners to the repository.
For more information, see [Managing larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/managing-larger-runners) and [Adding self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/adding-self-hosted-runners).
## [Using groups to control where jobs are run](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/running-jobs-on-larger-runners#using-groups-to-control-where-jobs-are-run)
In this example, Ubuntu runners have been added to a group called `ubuntu-runners`. The `runs-on` key sends the job to any available runner in the `ubuntu-runners` group:
```
name: learn-github-actions
on: [push]
jobs:
  check-bats-version:
    runs-on: 
      group: ubuntu-runners
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '14'
      - run: npm install -g bats
      - run: bats -v

```

## [Using groups to control where jobs are run](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/running-jobs-on-larger-runners#using-groups-to-control-where-jobs-are-run-1)
In this example, Ubuntu runners have been added to a group called `ubuntu-runners`. The `runs-on` key sends the job to any available runner in the `ubuntu-runners` group:
```
name: learn-github-actions
on: [push]
jobs:
  check-bats-version:
    runs-on: 
      group: ubuntu-runners
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '14'
      - run: npm install -g bats
      - run: bats -v

```

## [Using labels to control where jobs are run](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/running-jobs-on-larger-runners#using-labels-to-control-where-jobs-are-run)
You can implicitly pass a label to the `runs-on` key by using the syntax `runs-on: LABEL`. Alternatively, you can use the `labels` key, as shown in the example below.
In this example, the `runs-on` key sends the job to any available runner that has been assigned the `ubuntu-20.04-16core` label:
```
name: learn-github-actions
on: [push]
jobs:
  check-bats-version:
    runs-on:
      labels: ubuntu-20.04-16core
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '14'
      - run: npm install -g bats
      - run: bats -v

```

Anyone with write access to an Actions-enabled repository can find out the labels for the runners that are available in that repository. See [Running jobs on larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-larger-runners/running-jobs-on-larger-runners#viewing-available-runners-for-a-repository).
## [Using labels to control where jobs are run](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/running-jobs-on-larger-runners#using-labels-to-control-where-jobs-are-run-1)
You can implicitly pass a label to the `runs-on` key by using the syntax `runs-on: LABEL`. Alternatively, you can use the `labels` key, as shown in the example below.
In this example, the `runs-on` key sends the job to any available runner that has been assigned the `windows-2022-16core` label:
```
name: learn-github-actions
on: [push]
jobs:
  check-bats-version:
    runs-on:
      labels: windows-2022-16core
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '14'
      - run: npm install -g bats
      - run: bats -v

```

Anyone with write access to an Actions-enabled repository can find out the labels for the runners that are available in that repository. See [Running jobs on larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-larger-runners/running-jobs-on-larger-runners#viewing-available-runners-for-a-repository).
## [Targeting macOS larger runners in a workflow](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/running-jobs-on-larger-runners#targeting-macos-larger-runners-in-a-workflow)
To run your workflows on macOS larger runners, set the value of the `runs-on` key to a label associated with a macOS larger runner. For a list of macOS larger runner labels, see [Available macOS larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/running-jobs-on-larger-runners#available-macos-larger-runners).
In this example, the workflow uses a label that is associated with macOS XL runners. The `runs-on` key sends the job to any available runner with a matching label:
```
name: learn-github-actions-testing
on: [push]
jobs:
  build:
    runs-on: macos-13-xlarge
    steps:
      - uses: actions/checkout@v4
      - name: Build
        run: swift build
      - name: Run tests
        run: swift test

```

## [Using labels and groups to control where jobs are run](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/running-jobs-on-larger-runners#using-labels-and-groups-to-control-where-jobs-are-run)
When you combine groups and labels, the runner must meet both requirements to be eligible to run the job.
In this example, a runner group called `ubuntu-runners` is populated with Ubuntu runners, which have also been assigned the label `ubuntu-20.04-16core`. The `runs-on` key combines `group` and `labels` so that the job is routed to any available runner within the group that also has a matching label:
```
name: learn-github-actions
on: [push]
jobs:
  check-bats-version:
    runs-on:
      group: ubuntu-runners
      labels: ubuntu-20.04-16core
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '14'
      - run: npm install -g bats
      - run: bats -v

```

## [Using labels and groups to control where jobs are run](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/running-jobs-on-larger-runners#using-labels-and-groups-to-control-where-jobs-are-run-1)
When you combine groups and labels, the runner must meet both requirements to be eligible to run the job.
In this example, a runner group called `ubuntu-runners` is populated with Ubuntu runners, which have also been assigned the label `ubuntu-20.04-16core`. The `runs-on` key combines `group` and `labels` so that the job is routed to any available runner within the group that also has a matching label:
```
name: learn-github-actions
on: [push]
jobs:
  check-bats-version:
    runs-on:
      group: ubuntu-runners
      labels: ubuntu-20.04-16core
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '14'
      - run: npm install -g bats
      - run: bats -v

```

## [Troubleshooting larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/running-jobs-on-larger-runners#troubleshooting-larger-runners)
If you notice the jobs that target your larger runners are delayed or not running, there are several factors that may be causing this.
  * **Concurrency settings:** You may have reached your maximum concurrency limit. If you would like to enable more jobs to run in parallel, you can update your autoscaling settings to a larger number. For more information, see [Managing larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/managing-larger-runners#configuring-autoscaling-for-larger-runners).
  * **Repository permissions:** Ensure you have the appropriate repository permissions enabled for your larger runners. By default, enterprise runners are not available at the repository level and must be manually enabled by an organization administrator. For more information, see [Managing larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/managing-larger-runners#allowing-repositories-to-access-larger-runners).
  * **Billing information:** You must have a valid credit card on file in order to use larger runners. After adding a credit card to your account, it can take up to 10 minutes to enable the use of your larger runners. For more information, see [Managing your payment and billing information](https://docs.github.com/en/billing/managing-your-billing/managing-your-payment-and-billing-information).
  * **Spending limit:** Your GitHub Actions spending limit must be set to a value greater than zero. For more information, see [Managing your spending limit for GitHub Actions](https://docs.github.com/en/billing/managing-billing-for-github-actions/managing-your-spending-limit-for-github-actions).
  * **Fair use policy:** GitHub has a fair use policy that begins to throttle jobs based on several factors, such as how many jobs you are running or how many jobs are running across the entirety of GitHub Actions.
  * **Job queue to assign time:** Job queue to assign time refers to the time between a job request and GitHub assigning a VM to execute the job. Standard GitHub-hosted runners utilizing prescribed YAML workflow labels (such as `ubuntu-latest`) are always in a "warm" state. With larger runners, a warm machine may not be ready to pick up a job on first request as the pools for these machines are smaller. As a result, GitHub may need to create a new VM, which increases the queue to assign time. Once a runner is in use, VMs are readily for subsequent workflow runs, reducing the queue to assign time for future workflow runs over the next 24 hours.


If you notice the jobs that target your larger runners are delayed or not running, there are several factors that may be causing this.
  * **Concurrency settings:** You may have reached your maximum concurrency limit. If you would like to enable more jobs to run in parallel, you can update your autoscaling settings to a larger number. For more information, see [Managing larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/managing-larger-runners#configuring-autoscaling-for-larger-runners).
  * **Repository permissions:** Ensure you have the appropriate repository permissions enabled for your larger runners. By default, enterprise runners are not available at the repository level and must be manually enabled by an organization administrator. For more information, see [Managing larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/managing-larger-runners#allowing-repositories-to-access-larger-runners).
  * **Billing information:** You must have a valid credit card on file in order to use larger runners. After adding a credit card to your account, it can take up to 10 minutes to enable the use of your larger runners. For more information, see [Managing your payment and billing information](https://docs.github.com/en/billing/managing-your-billing/managing-your-payment-and-billing-information).
  * **Spending limit:** Your GitHub Actions spending limit must be set to a value greater than zero. For more information, see [Managing your spending limit for GitHub Actions](https://docs.github.com/en/billing/managing-billing-for-github-actions/managing-your-spending-limit-for-github-actions).
  * **Fair use policy:** GitHub has a fair use policy that begins to throttle jobs based on several factors, such as how many jobs you are running or how many jobs are running across the entirety of GitHub Actions.
  * **Job queue to assign time:** Job queue to assign time refers to the time between a job request and GitHub assigning a VM to execute the job. Standard GitHub-hosted runners utilizing prescribed YAML workflow labels (such as `ubuntu-latest`) are always in a "warm" state. With larger runners, a warm machine may not be ready to pick up a job on first request as the pools for these machines are smaller. As a result, GitHub may need to create a new VM, which increases the queue to assign time. Once a runner is in use, VMs are readily for subsequent workflow runs, reducing the queue to assign time for future workflow runs over the next 24 hours.


Because macOS arm64 does not support Node 12, macOS larger runners automatically use Node 16 to execute any JavaScript action written for Node 12. Some community actions may not be compatible with Node 16. If you use an action that requires a different Node version, you may need to manually install a specific version at runtime.
ARM-powered runners are currently in public preview and are subject to change.
