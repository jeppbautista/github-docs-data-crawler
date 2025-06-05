  * [Codespaces](https://docs.github.com/en/codespaces "Codespaces")/
  * [Setting up your project](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces "Setting up your project")/
  * [Configuring dev containers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/configuring-dev-containers "Configuring dev containers")/
  * [Adding features](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/configuring-dev-containers/adding-features-to-a-devcontainer-file "Adding features")


# Adding features to a devcontainer.json file
With features, you can quickly add tools, runtimes, or libraries to your dev container configuration.
## Tool navigation
  * [Visual Studio Code](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/configuring-dev-containers/adding-features-to-a-devcontainer-file?tool=vscode)
  * [Web browser](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/configuring-dev-containers/adding-features-to-a-devcontainer-file?tool=webui)


Features are self-contained units of installation code and dev container configuration, designed to work across a wide range of base container images. You can use features to quickly add tools, runtimes, or libraries to your codespace image. For more information, see the [available features](https://containers.dev/features) and [features specification](https://containers.dev/implementors/features/) on the Development Containers website.
You can add features to a `devcontainer.json` file from VS Code or from your repository on GitHub. Use the tabs in this article to display instructions for each of these ways of adding features.
## [Adding features to a `devcontainer.json` file](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/configuring-dev-containers/adding-features-to-a-devcontainer-file#adding-features-to-a-devcontainerjson-file)
  1. Navigate to your repository on GitHub, find your `devcontainer.json` file, and click 
If you don't already have a `devcontainer.json` file, you can create one now. For more information, see [Introduction to dev containers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers#creating-a-custom-dev-container-configuration).
  2. To the right of the file editor, in the **Marketplace** tab, browse or search for the feature you want to add, then click the name of the feature.
![Screenshot of the "Marketplace" tab with "Terra" in the search box and the Terraform feature listed in the search results.](https://docs.github.com/assets/cb-80759/images/help/codespaces/feature-marketplace.png)
  3. Under "Installation," click the code snippet to copy it to your clipboard, then paste the snippet into the `features` object in your `devcontainer.json` file.
![Screenshot of the "Marketplace" tab showing the installation code snippet for Terraform.](https://docs.github.com/assets/cb-159859/images/help/codespaces/feature-installation-code.png)
```
"features": {
     // ...
     "ghcr.io/devcontainers/features/terraform:1": {},
     // ...
 }

```

  4. By default, the latest version of the feature will be used. To choose a different version, or configure other options for the feature, expand the properties listed under "Options" to view the available values, then add the options by manually editing the object in your `devcontainer.json` file.
![Screenshot of the "Options" section of the "Marketplace" tab, with the "version" and "tflint" properties expanded.](https://docs.github.com/assets/cb-44765/images/help/codespaces/feature-options.png)
```
"features": {
     // ...
     "ghcr.io/devcontainers/features/terraform:1": {
         "version": "1.1",
         "tflint": "latest"
     },
     // ...
 }

```

  5. Commit the changes to your `devcontainer.json` file.


The configuration changes will take effect in new codespaces created from the repository. To make the changes take effect in existing codespaces, you will need to pull the updates to the `devcontainer.json` file into your codespace, then rebuild the container for the codespace. For more information, see [Introduction to dev containers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers#applying-configuration-changes-to-a-codespace).
To add features in VS Code while you are working locally, and not connected to a codespace, you must have the "Dev Containers" extension installed and enabled. For more information about this extension, see the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).
  1. Access the VS Code Command Palette with `Shift`+`Command`+`P` (Mac) or `Ctrl`+`Shift`+`P` (Windows/Linux).
  2. Start typing "add dev" then click **Codespaces: Add Dev Container Configuration Files**.
![Screenshot of the Command Palette, with "add dev" entered and "Codespaces: Add Dev Container Configuration Files" listed.](https://docs.github.com/assets/cb-12613/images/help/codespaces/add-prebuilt-container-command.png)
  3. Click **Modify your active configuration**.
  4. Update your feature selections, then click **OK**.
  5. If you're working in a codespace, a prompt will appear in the lower-right corner. To rebuild the container and apply the changes to the codespace you're working in, click **Rebuild Now**.
![Screenshot of the message: "We've noticed a change to the dev container configuration." Below this is the "Rebuild Now" button.](https://docs.github.com/assets/cb-21360/images/help/codespaces/rebuild-prompt.png)


