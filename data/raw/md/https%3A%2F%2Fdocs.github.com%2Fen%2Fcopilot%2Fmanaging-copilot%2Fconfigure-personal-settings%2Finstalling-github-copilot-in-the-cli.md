  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Manage Copilot](https://docs.github.com/en/copilot/managing-copilot "Manage Copilot")/
  * [Configure personal settings](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings "Configure personal settings")/
  * [Install Copilot in the CLI](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/installing-github-copilot-in-the-cli "Install Copilot in the CLI")


# Installing GitHub Copilot in the CLI
Learn how to install Copilot in the CLI so that you can get suggestions and explanations for the command line.
## In this article
  * [Prerequisites](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/installing-github-copilot-in-the-cli#prerequisites)
  * [Installing Copilot in the CLI](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/installing-github-copilot-in-the-cli#installing-copilot-in-the-cli)
  * [Updating Copilot in the CLI](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/installing-github-copilot-in-the-cli#updating-copilot-in-the-cli)
  * [Further reading](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/installing-github-copilot-in-the-cli#further-reading)


## [Prerequisites](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/installing-github-copilot-in-the-cli#prerequisites)
  * **Access to GitHub Copilot**. See [What is GitHub Copilot?](https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot#getting-access-to-copilot).
  * **GitHub CLI installed.** For installation instructions for GitHub CLI, see the [GitHub CLI repository](https://github.com/cli/cli#installation).


If you have access to GitHub Copilot via your organization or enterprise, you cannot use Copilot in the CLI if your organization owner or enterprise administrator has disabled Copilot in the CLI. See [Managing policies for Copilot in your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-github-copilot-features-in-your-organization/managing-policies-for-copilot-in-your-organization).
## [Installing Copilot in the CLI](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/installing-github-copilot-in-the-cli#installing-copilot-in-the-cli)
  1. If you have not already authenticated to the GitHub CLI, run the following command in your terminal.
Shell```
gh auth login

```
```
gh auth login

```

  2. To install the Copilot in the CLI extension, run the following command.
Shell```
gh extension install github/gh-copilot

```
```
gh extension install github/gh-copilot

```



## [Updating Copilot in the CLI](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/installing-github-copilot-in-the-cli#updating-copilot-in-the-cli)
After installing the Copilot in the CLI extension, you can update at any time by running:
Shell```
gh extension upgrade gh-copilot

```
```
gh extension upgrade gh-copilot

```

## [Further reading](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/installing-github-copilot-in-the-cli#further-reading)
  * [Using GitHub Copilot in the command line](https://docs.github.com/en/copilot/github-copilot-in-the-cli/using-github-copilot-in-the-cli)
  * [Configuring GitHub Copilot in the CLI](https://docs.github.com/en/copilot/github-copilot-in-the-cli/configuring-github-copilot-in-the-cli)


