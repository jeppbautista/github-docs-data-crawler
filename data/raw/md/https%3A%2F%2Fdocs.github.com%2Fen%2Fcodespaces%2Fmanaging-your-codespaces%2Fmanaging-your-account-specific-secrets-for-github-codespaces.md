  * [Codespaces](https://docs.github.com/en/codespaces "Codespaces")/
  * [Managing your codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces "Managing your codespaces")/
  * [Codespaces secrets](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces "Codespaces secrets")


# Managing your account-specific secrets for GitHub Codespaces
You can store sensitive information, like tokens, that you want to access in your codespaces via environment variables.
## In this article
  * [About secrets for GitHub Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces#about-secrets-for-github-codespaces)
  * [Adding a secret](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces#adding-a-secret)
  * [Editing a secret](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces#editing-a-secret)
  * [Deleting a secret](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces#deleting-a-secret)
  * [Using secrets](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces#using-secrets)
  * [Further reading](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces#further-reading)


## [About secrets for GitHub Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces#about-secrets-for-github-codespaces)
You can add development environment secrets to your personal account that you want to use in your codespaces. For example, you may want to store and access the following sensitive information as secrets:
  * Access tokens to cloud services
  * Service principals
  * Subscription identifiers
  * Credentials for a private image registry (for more information, see [Allowing your codespace to access a private registry](https://docs.github.com/en/codespaces/reference/allowing-your-codespace-to-access-a-private-registry))


You can choose which repositories should have access to each secret. Then, you can use the secret in any codespace you create for a repository that has access to the secret. To share a secret with a codespace created from a template, you will need to publish the codespace to a repository on GitHub, then give that repository access to the secret.
Once you have created a secret, it will be available when you create a new codespace or restart the codespace. If you've created a secret on GitHub and you want to use it in a currently running codespace, stop the codespace and then restart it. For information about stopping the codespace, see [Using the Visual Studio Code Command Palette in GitHub Codespaces](https://docs.github.com/en/codespaces/codespaces-reference/using-the-vs-code-command-palette-in-codespaces#suspending-or-stopping-a-codespace).
### [Naming secrets](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces#naming-secrets)
The following rules apply to secret names:
  * Secret names can only contain alphanumeric characters (`[a-z]`, `[A-Z]`, `[0-9]`) or underscores (`_`). Spaces are not allowed.
  * Secret names must not start with the `GITHUB_` prefix.
  * Secret names must not start with a number.
  * Secret names are not case-sensitive.
  * Secret names must be unique at the level they are created at. For example, a secret created at the repository level must have a unique name in that repository.


If a secret with the same name exists at multiple levels, the secret at the lowest level takes precedence. For example, if an organization-level secret has the same name as a repository-level secret, then the repository-level secret takes precedence.
### [Limits for secrets](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces#limits-for-secrets)
You can store up to 100 secrets for GitHub Codespaces.
Secrets are limited to 48 KB in size.
## [Adding a secret](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces#adding-a-secret)
  1. In the upper-right corner of any page on GitHub, click your profile photo, then click 
  2. In the "Code, planning, and automation" section of the sidebar, click 
  3. To the right of "Codespaces secrets", click **New secret**.
  4. Under "Name," type a name for your secret.
  5. Under "Value", type the value of your secret.
  6. Select the "Repository access" drop-down menu, then click a repository you want to have access to the secret. Repeat for every repository you want to have access to the secret.
![Screenshot of the "Repository access" dropdown menu. Two repositories are listed in the dropdown menu.](https://docs.github.com/assets/cb-32169/images/help/codespaces/select-repository-access.png)
  7. Click **Add secret**.


## [Editing a secret](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces#editing-a-secret)
You can update the value of an existing secret, and you can change which repositories can access a secret.
  1. In the upper-right corner of any page on GitHub, click your profile photo, then click 
  2. In the "Code, planning, and automation" section of the sidebar, click 
  3. Under "Codespaces secrets," to the right of the secret you want to edit, click **Update**.
  4. Under "Value," click the link "**enter a new value**."
![Screenshot of the "Codespaces / Update secret" page. The "enter a new value" link is highlighted with a dark orange outline.](https://docs.github.com/assets/cb-38851/images/help/codespaces/codespaces-secret-update-value-text.png)
  5. Under "Value", type the value of your secret.
  6. Select the "Repository access" drop-down menu, then click a repository you want to have access to the secret. Repeat for every repository you want to have access to the secret.
![Screenshot of the "Repository access" dropdown menu. Two repositories are listed in the dropdown menu.](https://docs.github.com/assets/cb-32169/images/help/codespaces/select-repository-access.png)
  7. Optionally, to remove the secret's access to a repository, deselect the repository.
![Screenshot showing a list of two repositories. Each has a selected checkbox.](https://docs.github.com/assets/cb-20326/images/help/codespaces/codespaces-secret-repository-checkboxes.png)
  8. Click **Save changes**.


## [Deleting a secret](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces#deleting-a-secret)
  1. In the upper-right corner of any page on GitHub, click your profile photo, then click 
  2. In the "Code, planning, and automation" section of the sidebar, click 
  3. Under "Codespaces secrets," to the right of the secret you want to delete, click **Delete**.
  4. Read the warning, then click **OK**.


## [Using secrets](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces#using-secrets)
A development environment secret is exported as an environment variable into the user's terminal session.
![Screenshot of the Terminal in VS Code. The command "echo $EXAMPLE_API_KEY" has returned "aBCdeFG1234567."](https://docs.github.com/assets/cb-28847/images/help/codespaces/exported-codespace-secret.png)
You can use development environment secrets after the codespace is built and is running. For example, a secret can be used:
  * When launching an application from the integrated terminal or ssh session.
  * Within a dev container lifecycle script that is run after the codespace is running. For more information about dev container lifecycle scripts, see the documentation on the Development Containers website: [Specification](https://containers.dev/implementors/json_reference/#lifecycle-scripts).


Development environment secrets cannot be used:
  * During codespace build time (that is, within a Dockerfile or custom entry point).
  * Within a dev container feature. For more information, see the `features` property in the [dev containers specification](https://containers.dev/implementors/json_reference/#general-properties) on the Development Containers website.


## [Further reading](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces#further-reading)
  * [Managing development environment secrets for your repository or organization](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/managing-development-environment-secrets-for-your-repository-or-organization)
  * [Creating a codespace for a repository](https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-for-a-repository#recommended-secrets)
  * [Setting your user preferences](https://docs.github.com/en/codespaces/setting-your-user-preferences)
  * [Customizing your codespace](https://docs.github.com/en/codespaces/customizing-your-codespace)


