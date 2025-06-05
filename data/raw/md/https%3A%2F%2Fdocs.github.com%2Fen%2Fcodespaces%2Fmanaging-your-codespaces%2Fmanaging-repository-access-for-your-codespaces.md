  * [Codespaces](https://docs.github.com/en/codespaces "Codespaces")/
  * [Managing your codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces "Managing your codespaces")/
  * [Repository access](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-repository-access-for-your-codespaces "Repository access")


# Managing access to other repositories within your codespace
You can manage the repositories that GitHub Codespaces can access.
## In this article
  * [Overview](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-repository-access-for-your-codespaces#overview)
  * [Creating codespaces with custom permissions](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-repository-access-for-your-codespaces#creating-codespaces-with-custom-permissions)
  * [Setting additional repository permissions](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-repository-access-for-your-codespaces#setting-additional-repository-permissions)
  * [Authorizing requested permissions](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-repository-access-for-your-codespaces#authorizing-requested-permissions)
  * [Further reading](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-repository-access-for-your-codespaces#further-reading)


## [Overview](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-repository-access-for-your-codespaces#overview)
By default, your codespace is assigned a token scoped with `read` permission or `read` and `write` permission to the repository from which it was created. The scope of this token changes automatically in the following circumstances.
  * If you create a codespace for a repository to which you only have read access, then make a commit in the codespace or push a new branch, GitHub Codespaces automatically links your codespace to a new or existing fork of the repository and updates the token to have `read` and `write` permission to the fork. For more information, see [Using source control in your codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-source-control-in-your-codespace#about-automatic-forking).
  * If you create a codespace from a template, then publish the codespace to a new repository, GitHub Codespaces updates the token to have `read` and `write` permission to the new repository. For more information, see [Creating a codespace from a template](https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-from-a-template#publishing-to-a-repository-on-github).


For more information, see [Security in GitHub Codespaces](https://docs.github.com/en/codespaces/reference/security-in-github-codespaces#authentication).
If your project needs additional permissions for other repositories, you can configure this in the `devcontainer.json` file, as described in [Setting additional repository permissions](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-repository-access-for-your-codespaces#setting-additional-repository-permissions) later in this article. When permissions are listed in the `devcontainer.json` file, you will be prompted to review and authorize the additional permissions as part of codespace creation for that repository. Once you've authorized the listed permissions, GitHub Codespaces will remember your choice and will not prompt you for authorization unless the permissions in the `devcontainer.json` file change.
Updating the permissions in the `devcontainer.json` file does not change the permissions of existing codespaces. If you need additional permissions in an existing codespace, see [Troubleshooting authentication to a repository](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-authentication-to-a-repository#authenticating-to-repositories-that-you-didnt-create-the-codespace-from).
## [Creating codespaces with custom permissions](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-repository-access-for-your-codespaces#creating-codespaces-with-custom-permissions)
To create a codespace with custom permissions, you must use one of the following:
  * The GitHub web UI
  * [GitHub CLI](https://github.com/cli/cli/releases/latest) 2.5.2 or later
  * [GitHub Codespaces Visual Studio Code extension](https://marketplace.visualstudio.com/items?itemName=GitHub.codespaces) 1.5.3 or later


## [Setting additional repository permissions](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-repository-access-for-your-codespaces#setting-additional-repository-permissions)
You configure repository permissions for GitHub Codespaces in a `devcontainer.json` file. Any custom permissions you add or change will only apply to new codespaces created after your changes have been committed to the repository. If you add or change permissions from within a codespace those permissions will not apply to the current codespace, even if you rebuild the codespace.
  1. If your repository does not already contain a `devcontainer.json` file, add one now. For more information, see [Adding a dev container configuration to your repository](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration).
  2. Edit the `devcontainer.json` file, adding the repository name and permissions needed to the `repositories` object:
JSON```
{
  "customizations": {
    "codespaces": {
      "repositories": {
        "my_org/my_repo": {
          "permissions": {
            "issues": "write"
          }
        }
      }
    }
  }
}

```
```
{
  "customizations": {
    "codespaces": {
      "repositories": {
        "my_org/my_repo": {
          "permissions": {
            "issues": "write"
          }
        }
      }
    }
  }
}

```

     * You can only reference repositories that belong to the same personal account or organization as the repository you are currently working in.
     * You can use the `*` wildcard to grant permissions to multiple repositories in an organization. For example, to grant permissions to all repositories in the `my_org` organization use `my_org/*`. This syntax is only valid for codespaces. In any `devcontainer.json` files that are used for prebuilds, you must define permissions for each repository separately. For more information, see [Allowing a prebuild to access other repositories](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/allowing-a-prebuild-to-access-other-repositories).
You can grant as many or as few of the following permissions for each repository listed:
     * `actions` - read / write
     * `checks` - read / write
     * `contents` - read / write
     * `deployments` - read / write
     * `discussions` - read / write
     * `issues` - read / write
     * `packages` - read
     * `pages` - read / write
     * `pull_requests` - read / write
     * `repository_projects` - read / write
     * `statuses` - read / write
     * `workflows` - write
To set a permission for a repository in an organization, you must explicitly add that repository name in the `repositories` object.
```
{
  "customizations": {
    "codespaces": {
      "repositories": {
        "my_org/my_repo": {
          "permissions": {
            "issues": "write"
          }
        }
      }
    }
  }
}

```

To set all permissions for a given repository, use `"permissions": "read-all"` or `"permissions": "write-all"` in the repository object.
```
{
  "customizations": {
    "codespaces": {
      "repositories": {
        "my_org/my_repo": {
          "permissions": "write-all"
        }
      }
    }
  }
}

```



## [Authorizing requested permissions](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-repository-access-for-your-codespaces#authorizing-requested-permissions)
If additional repository permissions are defined in the `devcontainer.json` file, you will be prompted to review and optionally authorize the permissions when you create a codespace or a prebuild configuration for this repository. When you authorize permissions for a repository, GitHub Codespaces will not re-prompt you unless the set of requested permissions has changed for the repository.
![Screenshot of the requested permissions page. Two permissions are shown as requested: read permission for metadata and write permission for issues.](https://docs.github.com/assets/cb-154099/images/help/codespaces/codespaces-accept-permissions.png)
You should only authorize permissions for repositories you know and trust. If you don't trust the set of requested permissions, click **Continue without authorizing** to create the codespace with the base set of permissions. Rejecting additional permissions may impact the functionality of your project within the codespace as the codespace will only have access to the repository from which it was created.
You can only authorize permissions that your personal account already possesses. If a codespace requests permissions for repositories that you don't currently have access to, contact an owner or admin of the repository to obtain sufficient access and then try to create a codespace again.
## [Further reading](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-repository-access-for-your-codespaces#further-reading)
  * [Setting your user preferences](https://docs.github.com/en/codespaces/setting-your-user-preferences)
  * [Customizing your codespace](https://docs.github.com/en/codespaces/customizing-your-codespace)


