  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Write workflows](https://docs.github.com/en/actions/writing-workflows "Write workflows")/
  * [Choose what workflows do](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does "Choose what workflows do")/
  * [Find and customize actions](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-pre-written-building-blocks-in-your-workflow "Find and customize actions")


# Using pre-written building blocks in your workflow
Actions are the building blocks that power your workflow. A workflow can contain actions created by the community, or you can create your own actions directly within your application's repository. This guide will show you how to discover, use, and customize actions.
## In this article
  * [Overview](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-pre-written-building-blocks-in-your-workflow#overview)
  * [Browsing Marketplace actions in the workflow editor](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-pre-written-building-blocks-in-your-workflow#browsing-marketplace-actions-in-the-workflow-editor)
  * [Adding an action to your workflow](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-pre-written-building-blocks-in-your-workflow#adding-an-action-to-your-workflow)
  * [Using release management for your custom actions](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-pre-written-building-blocks-in-your-workflow#using-release-management-for-your-custom-actions)
  * [Using inputs and outputs with an action](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-pre-written-building-blocks-in-your-workflow#using-inputs-and-outputs-with-an-action)
  * [Next steps](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-pre-written-building-blocks-in-your-workflow#next-steps)


## [Overview](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-pre-written-building-blocks-in-your-workflow#overview)
You can use pre-written building blocks, called actions, in your workflow. An action is a pre-defined, reusable set of jobs or code that perform specific tasks within a workflow.
Actions can be:
  * **Reusable:** actions can be used across different workflows and repositories, allowing you to avoid rewriting the same code.
  * **Pre-written:** many actions are available in the GitHub Marketplace, covering a wide range of tasks like checking out code, setting up environments, running tests, and deploying applications.
  * **Configurable:** you can configure actions with inputs, outputs, and environment variables to tailor them to your specific needs.
  * **Community-driven:** you can create your own actions and share them with others or use actions developed by the community.


The actions you use in your workflow can be defined in:
  * The same repository as your workflow file
  * Any public repository
  * A published Docker container image on Docker Hub


GitHub Marketplace is a central location for you to find actions created by the GitHub community. [GitHub Marketplace page](https://github.com/marketplace/actions/) enables you to filter for actions by category.
## [Browsing Marketplace actions in the workflow editor](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-pre-written-building-blocks-in-your-workflow#browsing-marketplace-actions-in-the-workflow-editor)
You can search and browse actions directly in your repository's workflow editor. From the sidebar, you can search for a specific action, view featured actions, and browse featured categories. You can also view the number of stars an action has received from the GitHub community.
  1. In your repository, browse to the workflow file you want to edit.
  2. In the upper right corner of the file view, to open the workflow editor, click 
![Screenshot of a workflow file showing the header section. The pencil icon for editing files is highlighted with a dark orange outline.](https://docs.github.com/assets/cb-26543/images/help/repository/actions-edit-workflow-file.png)
  3. To the right of the editor, use the GitHub Marketplace sidebar to browse actions. Actions with the 
![Screenshot of a workflow in the file editor. The sidebar shows Marketplace actions. A "Creator verified by GitHub" badge is outlined in orange.](https://docs.github.com/assets/cb-93797/images/help/repository/actions-marketplace-sidebar.png)


## [Adding an action to your workflow](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-pre-written-building-blocks-in-your-workflow#adding-an-action-to-your-workflow)
You can add an action to your workflow by referencing the action in your workflow file.
You can view the actions referenced in your GitHub Actions workflows as dependencies in the dependency graph of the repository containing your workflows. For more information, see “[About the dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph).”
To enhance security, GitHub Actions does not support redirects for actions or reusable workflows. This means that when the owner, name of an action's repository, or name of an action is changed, any workflows using that action with the previous name will fail.
### [Adding an action from GitHub Marketplace](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-pre-written-building-blocks-in-your-workflow#adding-an-action-from-github-marketplace)
An action's listing page includes the action's version and the workflow syntax required to use the action. To keep your workflow stable even when updates are made to an action, you can reference the version of the action to use by specifying the Git or Docker tag number in your workflow file.
  1. Navigate to the action you want to use in your workflow.
  2. Click to view the full marketplace listing for the action.
  3. Under "Installation", click 
![Screenshot of the marketplace listing for an action. The "Copy to clipboard" icon for the action is highlighted with a dark orange outline.](https://docs.github.com/assets/cb-52844/images/help/repository/actions-sidebar-detailed-view.png)
  4. Paste the syntax as a new step in your workflow. For more information, see [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idsteps).
  5. If the action requires you to provide inputs, set them in your workflow. For information on inputs an action might require, see [Using pre-written building blocks in your workflow](https://docs.github.com/en/actions/learn-github-actions/finding-and-customizing-actions#using-inputs-and-outputs-with-an-action).


You can also enable Dependabot version updates for the actions that you add to your workflow. For more information, see [Keeping your actions up to date with Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/keeping-your-actions-up-to-date-with-dependabot).
### [Adding an action from the same repository](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-pre-written-building-blocks-in-your-workflow#adding-an-action-from-the-same-repository)
If an action is defined in the same repository where your workflow file uses the action, you can reference the action with either the ‌`{owner}/{repo}@{ref}` or `./path/to/dir` syntax in your workflow file.
Example repository file structure:
```
|-- hello-world (repository)
|   |__ .github
|       └── workflows
|           └── my-first-workflow.yml
|       └── actions
|           |__ hello-world-action
|               └── action.yml

```

The path is relative (`./`) to the default working directory (`github.workspace`, `$GITHUB_WORKSPACE`). If the action checks out the repository to a location different than the workflow, the relative path used for local actions must be updated.
Example workflow file:
```
jobs:
  my_first_job:
    runs-on: ubuntu-latest
    steps:
      # This step checks out a copy of your repository.
      - name: My first step - check out repository
        uses: actions/checkout@v4
      # This step references the directory that contains the action.
      - name: Use local hello-world-action
        uses: ./.github/actions/hello-world-action

```

The `action.yml` file is used to provide metadata for the action. Learn about the content of this file in [Metadata syntax for GitHub Actions](https://docs.github.com/en/actions/creating-actions/metadata-syntax-for-github-actions).
### [Adding an action from a different repository](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-pre-written-building-blocks-in-your-workflow#adding-an-action-from-a-different-repository)
If an action is defined in a different repository than your workflow file, you can reference the action with the `{owner}/{repo}@{ref}` syntax in your workflow file.
The action must be stored in a public repository.
```
jobs:
  my_first_job:
    steps:
      - name: My first step
        uses: actions/setup-node@v4

```

### [Referencing a container on Docker Hub](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-pre-written-building-blocks-in-your-workflow#referencing-a-container-on-docker-hub)
If an action is defined in a published Docker container image on Docker Hub, you must reference the action with the `docker://{image}:{tag}` syntax in your workflow file. To protect your code and data, we strongly recommend you verify the integrity of the Docker container image from Docker Hub before using it in your workflow.
```
jobs:
  my_first_job:
    steps:
      - name: My first step
        uses: docker://alpine:3.8

```

For some examples of Docker actions, see the [Docker-image.yml workflow](https://github.com/actions/starter-workflows/blob/main/ci/docker-image.yml) and [Creating a Docker container action](https://docs.github.com/en/actions/creating-actions/creating-a-docker-container-action).
### [Security hardening for using actions in your workflows](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-pre-written-building-blocks-in-your-workflow#security-hardening-for-using-actions-in-your-workflows)
GitHub provides security features that you can use to increase the security of your workflows. You can use GitHub's built-in features to ensure you are notified about vulnerabilities in the actions you consume, or to automate the process of keeping the actions in your workflows up to date. For more information, see [Using GitHub's security features to secure your use of GitHub Actions](https://docs.github.com/en/actions/security-guides/using-githubs-security-features-to-secure-your-use-of-github-actions).
## [Using release management for your custom actions](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-pre-written-building-blocks-in-your-workflow#using-release-management-for-your-custom-actions)
The creators of a community action have the option to use tags, branches, or SHA values to manage releases of the action. Similar to any dependency, you should indicate the version of the action you'd like to use based on your comfort with automatically accepting updates to the action.
You will designate the version of the action in your workflow file. Check the action's documentation for information on their approach to release management, and to see which tag, branch, or SHA value to use.
We recommend that you use a SHA value when using third-party actions. However, it's important to note Dependabot will only create Dependabot alerts for vulnerable GitHub Actions that use semantic versioning. For more information, see [Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions#using-third-party-actions) and [About Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts).
### [Using tags](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-pre-written-building-blocks-in-your-workflow#using-tags)
Tags are useful for letting you decide when to switch between major and minor versions, but these are more ephemeral and can be moved or deleted by the maintainer. This example demonstrates how to target an action that's been tagged as `v1.0.1`:
```
steps:
  - uses: actions/javascript-action@v1.0.1

```

### [Using SHAs](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-pre-written-building-blocks-in-your-workflow#using-shas)
If you need more reliable versioning, you should use the SHA value associated with the version of the action. SHAs are immutable and therefore more reliable than tags or branches. However, this approach means you will not automatically receive updates for an action, including important bug fixes and security updates. You must use a commit's full SHA value, and not an abbreviated value. When selecting a SHA, you should verify it is from the action's repository and not a repository fork. This example targets an action's SHA:
```
steps:
  - uses: actions/javascript-action@a824008085750b8e136effc585c3cd6082bd575f

```

### [Using branches](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-pre-written-building-blocks-in-your-workflow#using-branches)
Specifying a target branch for the action means it will always run the version currently on that branch. This approach can create problems if an update to the branch includes breaking changes. This example targets a branch named `@main`:
```
steps:
  - uses: actions/javascript-action@main

```

For more information, see [About custom actions](https://docs.github.com/en/actions/creating-actions/about-custom-actions#using-release-management-for-actions).
## [Using inputs and outputs with an action](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-pre-written-building-blocks-in-your-workflow#using-inputs-and-outputs-with-an-action)
An action often accepts or requires inputs and generates outputs that you can use. For example, an action might require you to specify a path to a file, the name of a label, or other data it will use as part of the action processing.
To see the inputs and outputs of an action, check the `action.yml` in the root directory of the repository.
In this example `action.yml`, the `inputs` keyword defines a required input called `file-path`, and includes a default value that will be used if none is specified. The `outputs` keyword defines an output called `results-file`, which tells you where to locate the results.
```
name: "Example"
description: "Receives file and generates output"
inputs:
  file-path: # id of input
    description: "Path to test script"
    required: true
    default: "test-file.js"
outputs:
  results-file: # id of output
    description: "Path to results file"

```

## [Next steps](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-pre-written-building-blocks-in-your-workflow#next-steps)
To continue learning about GitHub Actions, see [Understanding GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/essential-features-of-github-actions).
