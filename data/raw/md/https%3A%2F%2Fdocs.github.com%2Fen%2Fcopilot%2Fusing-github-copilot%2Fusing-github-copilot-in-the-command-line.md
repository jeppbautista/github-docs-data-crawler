  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Use GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot "Use GitHub Copilot")/
  * [Use Copilot in the CLI](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line "Use Copilot in the CLI")


# Using GitHub Copilot in the command line
You can use Copilot with the GitHub CLI to get suggestions and explanations for the command line.
## In this article
  * [Prerequisites](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line#prerequisites)
  * [Getting command explanations](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line#getting-command-explanations)
  * [Getting command suggestions](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line#getting-command-suggestions)
  * [Sharing feedback](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line#sharing-feedback)
  * [Further reading](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line#further-reading)


## [Prerequisites](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line#prerequisites)
  * **Access to GitHub Copilot**. See [What is GitHub Copilot?](https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot#getting-access-to-copilot).
  * **GitHub CLI installed**. For installation instructions for GitHub CLI, see the [GitHub CLI repository](https://github.com/cli/cli#installation).
  * **Copilot in the CLI extension installed**. See [Installing GitHub Copilot in the CLI](https://docs.github.com/en/copilot/github-copilot-in-the-cli/installing-github-copilot-in-the-cli).


If you have access to GitHub Copilot via your organization or enterprise, you cannot use Copilot in the CLI if your organization owner or enterprise administrator has disabled Copilot in the CLI. See [Managing policies for Copilot in your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-github-copilot-features-in-your-organization/managing-policies-for-copilot-in-your-organization).
## [Getting command explanations](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line#getting-command-explanations)
To ask Copilot in the CLI to explain a command, run `gh copilot explain` followed by the command that you want explained. For example:
Shell```
gh copilot explain "sudo apt-get"

```
```
gh copilot explain "sudo apt-get"

```

## [Getting command suggestions](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line#getting-command-suggestions)
To ask Copilot in the CLI to suggest a command, run `gh copilot suggest` followed by the command that you want. For example:
Shell```
gh copilot suggest "Undo the last commit"

```
```
gh copilot suggest "Undo the last commit"

```

Copilot in the CLI will start an interactive session to get more information about what you want.
If you choose the **Execute command** option after Copilot in the CLI suggests a command, Copilot in the CLI will copy the command to your clipboard and exit the interactive session. Then you can manually paste the command into your CLI.
If you want Copilot in the CLI to be able to execute commands on your behalf, you must set up the `ghcs` alias. See [Configuring GitHub Copilot in the CLI](https://docs.github.com/en/copilot/github-copilot-in-the-cli/configuring-github-copilot-in-the-cli#setting-up-aliases).
## [Sharing feedback](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line#sharing-feedback)
To send feedback to GitHub about the quality of a suggestion, select the **Rate response** option in Copilot in the CLI.
You can also open an issue in the [Copilot in the CLI extension repository](https://github.com/github/gh-copilot).
## [Further reading](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line#further-reading)
  * [Copilot in the CLI extension README](https://github.com/github/gh-copilot?tab=readme-ov-file)
  * [Configuring GitHub Copilot in the CLI](https://docs.github.com/en/copilot/github-copilot-in-the-cli/configuring-github-copilot-in-the-cli)


