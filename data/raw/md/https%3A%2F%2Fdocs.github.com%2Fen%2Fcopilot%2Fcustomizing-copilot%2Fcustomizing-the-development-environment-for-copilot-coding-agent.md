  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Customize Copilot](https://docs.github.com/en/copilot/customizing-copilot "Customize Copilot")/
  * [Customize the agent environment](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent "Customize the agent environment")


# Customizing the development environment for Copilot coding agent
Learn how to customize GitHub Copilot's development environment with additional tools.
## In this article
  * [About customizing Copilot coding agent's development environment](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent#about-customizing-copilot-coding-agents-development-environment)
  * [Preinstalling tools or dependencies in Copilot's environment](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent#preinstalling-tools-or-dependencies-in-copilots-environment)
  * [Upgrading to larger GitHub-hosted GitHub Actions runners](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent#upgrading-to-larger-github-hosted-github-actions-runners)
  * [Further reading](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent#further-reading)


Copilot coding agent is in public preview and subject to change.
For more information about Copilot coding agent, see [About assigning tasks to Copilot](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/about-assigning-tasks-to-copilot).
## [About customizing Copilot coding agent's development environment](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent#about-customizing-copilot-coding-agents-development-environment)
While working on a task, Copilot has access to its own ephemeral development environment, powered by GitHub Actions, where it can explore your code, make changes, execute automated tests and linters and more.
You can customize Copilot's environment by:
  * [Preinstalling tools or dependencies in Copilot's environment](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent#preinstalling-tools-or-dependencies-in-copilots-environment).
  * [Upgrading from standard GitHub-hosted GitHub Actions runners to larger runners](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent#upgrading-to-larger-github-hosted-github-actions-runners).
  * [Disabling or customizing the agent's firewall](https://docs.github.com/en/copilot/customizing-copilot/customizing-or-disabling-the-firewall-for-copilot-coding-agent).


## [Preinstalling tools or dependencies in Copilot's environment](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent#preinstalling-tools-or-dependencies-in-copilots-environment)
In its ephemeral development environment, Copilot can build or compile your project and run automated tests, linters and other tools. To do this, it will need to install your project's dependencies.
Copilot can discover and install these dependencies itself via a process of trial and error, but this can be slow and unreliable, given the non-deterministic nature of large language models (LLMs), and in some cases, it may be completely unable to download these dependencies—for example, if they are private.
Instead, you can preconfigure Copilot's environment before the agent starts by creating a special GitHub Actions workflow file, located at `.github/workflows/copilot-setup-steps.yml` within your repository.
A `copilot-setup-steps.yml` file looks like a normal GitHub Actions workflow file, but must contain a single `copilot-setup-steps` job. This job will be executed in GitHub Actions before Copilot starts working. For more information on GitHub Actions workflow files, see [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions).
Here is a simple example of a `copilot-setup-steps.yml` file for a TypeScript project that clones the project, installs Node.js and downloads and caches the project's dependencies. You should customize this to fit your own project's language(s) and dependencies:
YAML```
name: "Copilot Setup Steps"

# Allow testing of the setup steps from your repository's "Actions" tab.
on: workflow_dispatch

jobs:
  # The job MUST be called `copilot-setup-steps` or it will not be picked up by Copilot.
  copilot-setup-steps:
    runs-on: ubuntu-latest

    # Set the permissions to the lowest permissions possible needed for your steps.
    # Copilot will be given its own token for its operations.
    permissions:
      # If you want to clone the repository as part of your setup steps, for example to install dependencies, you'll need the `contents: read` permission. If you don't clone the repository in your setup steps, Copilot will do this for you automatically after the steps complete.
      contents: read

    # You can define any steps you want, and they will run before the agent starts.
    # If you do not check out your code, Copilot will do this for you.
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: "20"
          cache: "npm"

      - name: Install JavaScript dependencies
        run: npm ci

```
```
name: "Copilot Setup Steps"

# Allow testing of the setup steps from your repository's "Actions" tab.
on: workflow_dispatch

jobs:
  # The job MUST be called `copilot-setup-steps` or it will not be picked up by Copilot.
  copilot-setup-steps:
    runs-on: ubuntu-latest

    # Set the permissions to the lowest permissions possible needed for your steps.
    # Copilot will be given its own token for its operations.
    permissions:
      # If you want to clone the repository as part of your setup steps, for example to install dependencies, you'll need the `contents: read` permission. If you don't clone the repository in your setup steps, Copilot will do this for you automatically after the steps complete.
      contents: read

    # You can define any steps you want, and they will run before the agent starts.
    # If you do not check out your code, Copilot will do this for you.
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: "20"
          cache: "npm"

      - name: Install JavaScript dependencies
        run: npm ci

```

In your `copilot-setup-steps.yml` file, you can only customize the following settings of the `copilot-setup-steps` job. If you try to customize other settings, your changes will be ignored.
  * `steps` (see above)
  * `permissions` (see above)
  * `runs-on` (see below)
  * `container `
  * `services`
  * `snapshot`
  * `timeout-minutes` (maximum value: `59`)


For more information on these options, see [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#jobs).
Once you have created a `copilot-setup-steps.yml` file and merged it into your default branch, you can manually run the workflow from the repository's **Actions** tab to check that it works. For more information, see [Manually running a workflow](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/manually-running-a-workflow).
## [Upgrading to larger GitHub-hosted GitHub Actions runners](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent#upgrading-to-larger-github-hosted-github-actions-runners)
By default, Copilot works in a standard GitHub Actions runner with limited resources.
You can choose instead to use larger runners with more advanced features—for example more RAM, CPU and disk space and advanced networking controls. You may want to upgrade to a larger runner if you see poor performance—for example when downloading dependencies or running tests. For more information, see [About larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners).
Before Copilot can use larger runners, you must first add one or more larger runners and then configure your repository to use them. See [Managing larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/managing-larger-runners). Once you have done this, you can use the `copilot-setup-steps.yml` file to tell Copilot to use the larger runners.
To use larger runners, set the `runs-on` step of the `copilot-setup-steps` job to the label and/or group for the larger runners you want Copilot to use. For more information on specifying larger runners with `runs-on`, see [Running jobs on larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/running-jobs-on-larger-runners).
```
# ...

jobs:
  copilot-setup-steps:
    runs-on: ubuntu-4-core
    # ...

```

  * Copilot coding agent is only compatible with Ubuntu x86 Linux runners. Runners with Windows, macOS or other operating systems are not supported.
  * Self-hosted GitHub Actions runners are not supported.


## [Further reading](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent#further-reading)
  * [Customizing or disabling the firewall for Copilot coding agent](https://docs.github.com/en/copilot/customizing-copilot/customizing-or-disabling-the-firewall-for-copilot-coding-agent)


