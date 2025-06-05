  * [Codespaces](https://docs.github.com/en/codespaces "Codespaces")/
  * [Setting up your project](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces "Setting up your project")/
  * [Configuring dev containers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/configuring-dev-containers "Configuring dev containers")/
  * [Specifying recommended secrets](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/configuring-dev-containers/specifying-recommended-secrets-for-a-repository "Specifying recommended secrets")


# Specifying recommended secrets for a repository
You can add a setting to your dev container configuration that will prompt people to set specific development environment secrets when they create a codespace.
## Who can use this feature?
People with write permissions to a repository can create or edit the codespace configuration.
## In this article
  * [About recommended secrets](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/configuring-dev-containers/specifying-recommended-secrets-for-a-repository#about-recommended-secrets)
  * [Specifying recommended secrets in the dev container configuration](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/configuring-dev-containers/specifying-recommended-secrets-for-a-repository#specifying-recommended-secrets-in-the-dev-container-configuration)
  * [Further reading](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/configuring-dev-containers/specifying-recommended-secrets-for-a-repository#further-reading)


## [About recommended secrets](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/configuring-dev-containers/specifying-recommended-secrets-for-a-repository#about-recommended-secrets)
If a project needs user-specific secrets to be set up, you can prompt people to do this when they create a codespace. You do this by adding a setting to a dev container configuration file for the repository.
After you specify recommended secrets, if people have not already created those secrets in their personal settings for Codespaces, they will be prompted to do so when they use the advanced options method of creating a codespace. This is done on GitHub by clicking the **Codespaces** tab, then selecting **New with options**.
![Screenshot of the options dropdown in the "Codespaces" tab, with the option "New with options" highlighted.](https://docs.github.com/assets/cb-69581/images/help/codespaces/default-machine-type.png)
Recommended secrets are listed at the bottom of the page.
![Screenshot of the "Create codespace" page with four recommended secrets highlighted with a dark orange outline.](https://docs.github.com/assets/cb-146520/images/help/codespaces/recommended-secrets.png)
The names of the recommended secrets are only listed on this page when the container configuration on the selected branch specifies these secrets.
Each recommended secret is displayed in one of three ways:
  * If the person has not set the recommended secret in their Codespaces settings, an input box is displayed, allowing them to create the secret now. A description and link to more information are displayed if you have configured them. Entering a value is optional.
  * If the person has already created the recommended secret but has not associated it with this repository, they can select a checkbox to add this association. Doing so is optional.
  * If the person has already created the recommended secret and associated it with this repository, a preselected checkbox is displayed.


### [When to specify recommended secrets for a project](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/configuring-dev-containers/specifying-recommended-secrets-for-a-repository#when-to-specify-recommended-secrets-for-a-project)
You should use recommended secrets for development environment secrets that the user who creates the codespace, rather than the owner of the repository or organization, must provide. For example, if you have a public project, and users must provide a personal API key to run the application in your project, you can specify a recommended secret so that users will be prompted to provide the key as the value of the secret when they use the advanced options page to create a codespace.
Alternatively, for development environment secrets that the owner of the repository or organization can provide, such as API keys shared across a team, you can set secrets at the level of the repository or organization. For more information, see [Managing development environment secrets for your repository or organization](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/managing-development-environment-secrets-for-your-repository-or-organization).
## [Specifying recommended secrets in the dev container configuration](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/configuring-dev-containers/specifying-recommended-secrets-for-a-repository#specifying-recommended-secrets-in-the-dev-container-configuration)
  1. You can configure the codespaces that are created for your repository by adding settings to a `devcontainer.json` file. If your repository doesn't already contain a `devcontainer.json` file, you can add one now. See [Adding a dev container configuration to your repository](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration).
  2. Edit the `devcontainer.json` file, adding the `secrets` property at the top level of the file, within the enclosing JSON object. For example:
JSON```
"secrets": {
  "NAME_OF_SECRET_1": {
    "description": "This is the description of the secret.",
    "documentationUrl": "https://example.com/link/to/info"
  },
  "NAME_OF_SECRET_2": { }
}

```
```
"secrets": {
  "NAME_OF_SECRET_1": {
    "description": "This is the description of the secret.",
    "documentationUrl": "https://example.com/link/to/info"
  },
  "NAME_OF_SECRET_2": { }
}

```

  3. Add a property within `secrets` for each secret you want to recommend. For example, change `NAME_OF_SECRET_1` and `NAME_OF_SECRET_2`, in the previous code example, to the names of the secrets that people should create in their personal settings for Codespaces.
  4. Optionally, supply a description for each secret and a URL for more information about this secret.
You can omit `description` and `documentationUrl`, as shown by `NAME_OF_SECRET_2` in the previous code example.
  5. Specify additional secrets, as required.
  6. Save the file and commit your changes to the required branch of the repository.


## [Further reading](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/configuring-dev-containers/specifying-recommended-secrets-for-a-repository#further-reading)
  * [Creating a codespace for a repository](https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-for-a-repository?tool=webui#creating-a-codespace-for-a-repository)


