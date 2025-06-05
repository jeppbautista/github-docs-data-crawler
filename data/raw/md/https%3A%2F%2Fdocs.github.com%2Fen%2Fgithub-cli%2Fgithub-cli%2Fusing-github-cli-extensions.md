  * [GitHub CLI](https://docs.github.com/en/github-cli "GitHub CLI")/
  * [GitHub CLI](https://docs.github.com/en/github-cli/github-cli "GitHub CLI")/
  * [Using GitHub CLI extensions](https://docs.github.com/en/github-cli/github-cli/using-github-cli-extensions "Using GitHub CLI extensions")


# Using GitHub CLI extensions
Learn how to use custom extensions written by other GitHub CLI users.
## In this article
  * [About GitHub CLI extensions](https://docs.github.com/en/github-cli/github-cli/using-github-cli-extensions#about-github-cli-extensions)
  * [Finding extensions](https://docs.github.com/en/github-cli/github-cli/using-github-cli-extensions#finding-extensions)
  * [Installing extensions](https://docs.github.com/en/github-cli/github-cli/using-github-cli-extensions#installing-extensions)
  * [Running an extension](https://docs.github.com/en/github-cli/github-cli/using-github-cli-extensions#running-an-extension)
  * [Viewing installed extensions](https://docs.github.com/en/github-cli/github-cli/using-github-cli-extensions#viewing-installed-extensions)
  * [Updating extensions](https://docs.github.com/en/github-cli/github-cli/using-github-cli-extensions#updating-extensions)
  * [Uninstalling extensions](https://docs.github.com/en/github-cli/github-cli/using-github-cli-extensions#uninstalling-extensions)


## [About GitHub CLI extensions](https://docs.github.com/en/github-cli/github-cli/using-github-cli-extensions#about-github-cli-extensions)
Extensions outside of GitHub and GitHub CLI are not certified by GitHub and are governed by separate terms of service, privacy policy, and support documentation. To mitigate risk when using third-party extensions, audit the source code of the extension before installing or updating the extension.
GitHub CLI extensions are custom GitHub CLI commands that anyone can create and use. For more information about how to create GitHub CLI extensions, see [Creating GitHub CLI extensions](https://docs.github.com/en/github-cli/github-cli/creating-github-cli-extensions).
Extensions are locally installed and are scoped to the user. Therefore, if you access GitHub CLI from a different machine or another user accesses GitHub CLI from the same machine, the extension will not be available.
## [Finding extensions](https://docs.github.com/en/github-cli/github-cli/using-github-cli-extensions#finding-extensions)
You can find extensions by browsing [repositories with the `gh-extension` topic](https://github.com/topics/gh-extension).
## [Installing extensions](https://docs.github.com/en/github-cli/github-cli/using-github-cli-extensions#installing-extensions)
To install an extension, use the `extensions install` subcommand. Replace the `repo` parameter with the repository of the extension. You can use the full URL, such as `https://github.com/octocat/gh-whoami`, or just the owner and repository, such as `octocat/gh-whoami`.
If the owner and repository are used, `gh` will install the extension using the hostname to which `gh` is currently authenticated. The full URL format is useful when installing extensions from a different host. For example, users on GitHub Enterprise Server should use the full repository URL to install extensions from GitHub.com or any other host.
To install an extension in development from the current directory, use `.` as the value for the `repo` parameter.
```
gh extension install REPO

```

If you already have an extension by the same name installed, the command will fail. For example, if you have installed `octocat/gh-whoami`, you must uninstall it before installing `hubot/gh-whoami`.
## [Running an extension](https://docs.github.com/en/github-cli/github-cli/using-github-cli-extensions#running-an-extension)
When you have installed an extension, you run the extension as you would run a native GitHub CLI command, using `gh EXTENSION-NAME`. The `EXTENSION-NAME` is the name of the repository that contains the extension, minus the `gh-` prefix.
For example, if you installed the extension from the `octocat/gh-whoami` repository, you would run the extension with the following command.
```
gh whoami

```

You can usually find specific information about how to use an extension in the README of the repository that contains the extension.
## [Viewing installed extensions](https://docs.github.com/en/github-cli/github-cli/using-github-cli-extensions#viewing-installed-extensions)
To view all installed extensions, use the `extensions list` subcommand. The output will also tell you which extensions have updates available.
```
gh extension list

```

## [Updating extensions](https://docs.github.com/en/github-cli/github-cli/using-github-cli-extensions#updating-extensions)
To update an extension, use the `extensions upgrade` subcommand. Replace the `extension` parameter with the name of the extension.
```
gh extension upgrade EXTENSION

```

To update all installed extensions, use the `--all` flag.
```
gh extension upgrade --all

```

## [Uninstalling extensions](https://docs.github.com/en/github-cli/github-cli/using-github-cli-extensions#uninstalling-extensions)
To uninstall an extension, use the `extensions remove` subcommand. Replace the `extension` parameter with the name of the extension.
```
gh extension remove EXTENSION

```

