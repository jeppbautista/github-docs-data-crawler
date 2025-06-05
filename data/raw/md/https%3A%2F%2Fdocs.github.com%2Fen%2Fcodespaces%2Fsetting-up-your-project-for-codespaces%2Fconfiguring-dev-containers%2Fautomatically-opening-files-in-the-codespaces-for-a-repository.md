  * [Codespaces](https://docs.github.com/en/codespaces "Codespaces")/
  * [Setting up your project](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces "Setting up your project")/
  * [Configuring dev containers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/configuring-dev-containers "Configuring dev containers")/
  * [Automatically opening files](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/configuring-dev-containers/automatically-opening-files-in-the-codespaces-for-a-repository "Automatically opening files")


# Automatically opening files in the codespaces for a repository
You can set particular files to be opened automatically whenever someone creates a codespace for your repository and opens the codespace in the Visual Studio Code web client.
## Who can use this feature?
People with write permissions to a repository can create or edit the codespace configuration.
## In this article
  * [Overview](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/configuring-dev-containers/automatically-opening-files-in-the-codespaces-for-a-repository#overview)
  * [Setting files to be opened automatically](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/configuring-dev-containers/automatically-opening-files-in-the-codespaces-for-a-repository#setting-files-to-be-opened-automatically)
  * [Further reading](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/configuring-dev-containers/automatically-opening-files-in-the-codespaces-for-a-repository#further-reading)


## [Overview](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/configuring-dev-containers/automatically-opening-files-in-the-codespaces-for-a-repository#overview)
If there's a particular file that's useful for people to see when they create a codespace for your repository, you can set this file to be opened automatically in the VS Code web client. You set this up in the dev container configuration file for your repository.
The file, or files, you specify are only opened the first time a codespace is opened in the web client. If the person closes the specified files, those files are not automatically reopened the next time that person opens or restarts the codespace.
This automation only applies to the VS Code web client, not to the VS Code desktop application, or other supported editors.
## [Setting files to be opened automatically](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/configuring-dev-containers/automatically-opening-files-in-the-codespaces-for-a-repository#setting-files-to-be-opened-automatically)
  1. You can configure the codespaces that are created for your repository by adding settings to a `devcontainer.json` file. If your repository doesn't already contain a `devcontainer.json` file, you can add one now. See [Adding a dev container configuration to your repository](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration).
  2. Edit the `devcontainer.json` file, adding a `customizations.codespaces.openFiles` property. The `customizations` property resides at the top level of the file, within the enclosing JSON object. For example:
JSON```
"customizations": {
  "codespaces": {
    "openFiles": [
      "README.md",
      "scripts/tsconfig.json",
      "docs/main/CODING_STANDARDS.md"
    ]
  }
}

```
```
"customizations": {
  "codespaces": {
    "openFiles": [
      "README.md",
      "scripts/tsconfig.json",
      "docs/main/CODING_STANDARDS.md"
    ]
  }
}

```

The value of the `openFiles` property is an array of one or more files in your repository. The paths are relative to the root of the repository (absolute paths are not supported). The files are opened in the web client in the order specified, with the first file in the array displayed in the editor.
  3. Save the file and commit your changes to the required branch of the repository.


## [Further reading](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/configuring-dev-containers/automatically-opening-files-in-the-codespaces-for-a-repository#further-reading)
  * [Introduction to dev containers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers)


