  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Write workflows](https://docs.github.com/en/actions/writing-workflows "Write workflows")/
  * [Choose where workflows run](https://docs.github.com/en/actions/writing-workflows/choosing-where-your-workflow-runs "Choose where workflows run")/
  * [Choose the runner for a job](https://docs.github.com/en/actions/writing-workflows/choosing-where-your-workflow-runs/choosing-the-runner-for-a-job "Choose the runner for a job")


# Choosing the runner for a job
Define the type of machine that will process a job in your workflow.
## In this article
  * [Overview](https://docs.github.com/en/actions/writing-workflows/choosing-where-your-workflow-runs/choosing-the-runner-for-a-job#overview)
  * [Choosing GitHub-hosted runners](https://docs.github.com/en/actions/writing-workflows/choosing-where-your-workflow-runs/choosing-the-runner-for-a-job#choosing-github-hosted-runners)
  * [Choosing self-hosted runners](https://docs.github.com/en/actions/writing-workflows/choosing-where-your-workflow-runs/choosing-the-runner-for-a-job#choosing-self-hosted-runners)
  * [Choosing runners in a group](https://docs.github.com/en/actions/writing-workflows/choosing-where-your-workflow-runs/choosing-the-runner-for-a-job#choosing-runners-in-a-group)


## [Overview](https://docs.github.com/en/actions/writing-workflows/choosing-where-your-workflow-runs/choosing-the-runner-for-a-job#overview)
Use `jobs.<job_id>.runs-on` to define the type of machine to run the job on.
  * The destination machine can be either a [GitHub-hosted runner](https://docs.github.com/en/actions/writing-workflows/choosing-where-your-workflow-runs/choosing-the-runner-for-a-job#choosing-github-hosted-runners), [larger runner](https://docs.github.com/en/actions/writing-workflows/choosing-where-your-workflow-runs/choosing-the-runner-for-a-job#choosing-runners-in-a-group), or a [self-hosted runner](https://docs.github.com/en/actions/writing-workflows/choosing-where-your-workflow-runs/choosing-the-runner-for-a-job#choosing-self-hosted-runners).


  * You can target runners based on the labels assigned to them, or their group membership, or a combination of these.
  * You can provide `runs-on` as:
    * A single string
    * A single variable containing a string
    * An array of strings, variables containing strings, or a combination of both
    * A `key: value` pair using the `group` or `labels` keys
  * If you specify an array of strings or variables, your workflow will execute on any runner that matches all of the specified `runs-on` values. For example, here the job will only run on a self-hosted runner that has the labels `linux`, `x64`, and `gpu`:
```
runs-on: [self-hosted, linux, x64, gpu]

```

For more information, see [Choosing self-hosted runners](https://docs.github.com/en/actions/writing-workflows/choosing-where-your-workflow-runs/choosing-the-runner-for-a-job#choosing-self-hosted-runners).
  * You can mix strings and variables in an array. For example:
```
on:
  workflow_dispatch:
    inputs:
      chosen-os:
        required: true
        type: choice
        options:
        - Ubuntu
        - macOS

jobs:
  test:
    runs-on: [self-hosted, "${{ inputs.chosen-os }}"]
    steps:
    - run: echo Hello world!

```

  * If you would like to run your workflow on multiple machines, use [`jobs.<job_id>.strategy`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstrategy).


Quotation marks are not required around simple strings like `self-hosted`, but they are required for expressions like `"${{ inputs.chosen-os }}"`.
## [Choosing GitHub-hosted runners](https://docs.github.com/en/actions/writing-workflows/choosing-where-your-workflow-runs/choosing-the-runner-for-a-job#choosing-github-hosted-runners)
If you use a GitHub-hosted runner, each job runs in a fresh instance of a runner image specified by `runs-on`.
The value for runs-on, when you are using a GitHub-hosted runner, is a runner label or the name of a runner group. The labels for the standard GitHub-hosted runners are shown in the following tables.
For more information, see [About GitHub-hosted runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners/about-github-hosted-runners).
### [Standard GitHub-hosted runners for public repositories](https://docs.github.com/en/actions/writing-workflows/choosing-where-your-workflow-runs/choosing-the-runner-for-a-job#standard-github-hosted-runners-for-public-repositories)
For public repositories, jobs using the workflow labels shown in the table below will run on virtual machines with the associated specifications. The use of these runners on public repositories is free and unlimited.
**Virtual Machine** | **Processor (CPU)** | **Memory (RAM)** | **Storage (SSD)** | **Architecture** | **Workflow label**  
---|---|---|---|---|---  
Linux | 4 | 16 GB | 14 GB |  x64  |  `ubuntu-latest[](https://github.com/actions/runner-images/blob/main/images/ubuntu/Ubuntu2404-Readme.md)`, `ubuntu-24.04[](https://github.com/actions/runner-images/blob/main/images/ubuntu/Ubuntu2404-Readme.md)`, `ubuntu-22.04[](https://github.com/actions/runner-images/blob/main/images/ubuntu/Ubuntu2204-Readme.md)`  
Windows | 4 | 16 GB | 14 GB |  x64  |  `windows-latest[](https://github.com/actions/runner-images/blob/main/images/windows/Windows2022-Readme.md)`, `windows-2025[](https://github.com/actions/runner-images/blob/main/images/windows/Windows2025-Readme.md)`, `windows-2022[](https://github.com/actions/runner-images/blob/main/images/windows/Windows2022-Readme.md)`, `windows-2019[](https://github.com/actions/runner-images/blob/main/images/windows/Windows2019-Readme.md)`  
Linux [Public preview] | 4 | 16 GB | 14 GB |  arm64  |  `ubuntu-24.04-arm[](https://github.com/actions/partner-runner-images/blob/main/images/arm-ubuntu-24-image.md)`, `ubuntu-22.04-arm[](https://github.com/actions/partner-runner-images/blob/main/images/arm-ubuntu-22-image.md)`  
Windows [Public preview] | 4 | 16 GB | 14 GB | arm64 |  `windows-11-arm[](https://github.com/actions/partner-runner-images/blob/main/images/arm-windows-11-image.md)`  
macOS | 4 | 14 GB | 14 GB |  Intel  |  `macos-13[](https://github.com/actions/runner-images/blob/main/images/macos/macos-13-Readme.md)`  
macOS | 3 (M1) | 7 GB | 14 GB |  arm64  |  `macos-latest[](https://github.com/actions/runner-images/blob/main/images/macos/macos-14-Readme.md)`, `macos-14[](https://github.com/actions/runner-images/blob/main/images/macos/macos-14-Readme.md)`, `macos-15[](https://github.com/actions/runner-images/blob/main/images/macos/macos-15-Readme.md)`  
The arm64 Linux and Windows runners are in public preview and subject to change.
### [Standard GitHub-hosted runners for private repositories](https://docs.github.com/en/actions/writing-workflows/choosing-where-your-workflow-runs/choosing-the-runner-for-a-job#standard-github-hosted-runners-for--private-repositories)
For private repositories, jobs using the workflow labels shown in the table below will run on virtual machines with the associated specifications. These runners use your GitHub account's allotment of free minutes, and are then charged at the per minute rates. For more information, see [About billing for GitHub Actions](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions#per-minute-rates).
**Virtual Machine** | **Processor (CPU)** | **Memory (RAM)** | **Storage (SSD)** | **Architecture** | **Workflow label**  
---|---|---|---|---|---  
Linux | 2 | 7 GB | 14 GB |  x64  |  `ubuntu-latest[](https://github.com/actions/runner-images/blob/main/images/ubuntu/Ubuntu2404-Readme.md)`, `ubuntu-24.04[](https://github.com/actions/runner-images/blob/main/images/ubuntu/Ubuntu2404-Readme.md)`, `ubuntu-22.04[](https://github.com/actions/runner-images/blob/main/images/ubuntu/Ubuntu2204-Readme.md)`  
Windows | 2 | 7 GB | 14 GB |  x64  |  `windows-latest[](https://github.com/actions/runner-images/blob/main/images/windows/Windows2022-Readme.md)`, `windows-2025[](https://github.com/actions/runner-images/blob/main/images/windows/Windows2025-Readme.md)`, `windows-2022[](https://github.com/actions/runner-images/blob/main/images/windows/Windows2022-Readme.md)`, `windows-2019[](https://github.com/actions/runner-images/blob/main/images/windows/Windows2019-Readme.md)`  
macOS | 4 | 14 GB | 14 GB |  Intel  |  `macos-13[](https://github.com/actions/runner-images/blob/main/images/macos/macos-13-Readme.md)`  
macOS | 3 (M1) | 7 GB | 14 GB |  arm64  |  `macos-latest[](https://github.com/actions/runner-images/blob/main/images/macos/macos-14-Readme.md)`, `macos-14[](https://github.com/actions/runner-images/blob/main/images/macos/macos-14-Readme.md)`, `macos-15[](https://github.com/actions/runner-images/blob/main/images/macos/macos-15-Readme.md)`  
In addition to the standard GitHub-hosted runners, GitHub offers customers on GitHub Team and GitHub Enterprise Cloud plans a range of managed virtual machines with advanced features - for example, more cores and disk space, GPU-powered machines, and ARM-powered machines. For more information, see [About larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-larger-runners/about-larger-runners).
The `-latest` runner images are the latest stable images that GitHub provides, and might not be the most recent version of the operating system available from the operating system vendor.
Beta and Deprecated Images are provided "as-is", "with all faults" and "as available" and are excluded from the service level agreement and warranty. Beta Images may not be covered by customer support.
#### [Example: Specifying an operating system](https://docs.github.com/en/actions/writing-workflows/choosing-where-your-workflow-runs/choosing-the-runner-for-a-job#example-specifying-an-operating-system)
```
runs-on: ubuntu-latest

```

For more information, see [Using GitHub-hosted runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners).
## [Choosing self-hosted runners](https://docs.github.com/en/actions/writing-workflows/choosing-where-your-workflow-runs/choosing-the-runner-for-a-job#choosing-self-hosted-runners)
To specify a self-hosted runner for your job, configure `runs-on` in your workflow file with self-hosted runner labels.
Self-hosted runners may have the `self-hosted` label. When setting up a self-hosted runner, by default we will include the label `self-hosted`. You may pass in the `--no-default-labels` flag to prevent the self-hosted label from being applied. Labels can be used to create targeting options for runners, such as operating system or architecture, we recommend providing an array of labels that begins with `self-hosted` (this must be listed first) and then includes additional labels as needed. When you specify an array of labels, jobs will be queued on runners that have all the labels that you specify.
Note that Actions Runner Controller does not support multiple labels and does not support the `self-hosted` label.
#### [Example: Using labels for runner selection](https://docs.github.com/en/actions/writing-workflows/choosing-where-your-workflow-runs/choosing-the-runner-for-a-job#example-using-labels-for-runner-selection)
```
runs-on: [self-hosted, linux]

```

For more information, see [About self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners) and [Using self-hosted runners in a workflow](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/using-self-hosted-runners-in-a-workflow).
## [Choosing runners in a group](https://docs.github.com/en/actions/writing-workflows/choosing-where-your-workflow-runs/choosing-the-runner-for-a-job#choosing-runners-in-a-group)
You can use `runs-on` to target runner groups, so that the job will execute on any runner that is a member of that group. For more granular control, you can also combine runner groups with labels.
Runner groups can only have [larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners) or [self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners) as members.
#### [Example: Using groups to control where jobs are run](https://docs.github.com/en/actions/writing-workflows/choosing-where-your-workflow-runs/choosing-the-runner-for-a-job#example-using-groups-to-control-where-jobs-are-run)
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

#### [Example: Combining groups and labels](https://docs.github.com/en/actions/writing-workflows/choosing-where-your-workflow-runs/choosing-the-runner-for-a-job#example-combining-groups-and-labels)
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

