  * [Codespaces](https://docs.github.com/en/codespaces "Codespaces")/
  * [Setting up your project](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces "Setting up your project")/
  * [Adding a dev container configuration](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration "Adding a dev container configuration")/
  * [Setting up a PHP project](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-php-project-for-codespaces "Setting up a PHP project")


# Setting up a PHP project for GitHub Codespaces
Get started with a PHP project in GitHub Codespaces by creating a custom dev container configuration.
## In this article
  * [Introduction](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-php-project-for-codespaces#introduction)
  * [Step 1: Open the project in a codespace](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-php-project-for-codespaces#step-1-open-the-project-in-a-codespace)
  * [Step 2: Add a dev container configuration](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-php-project-for-codespaces#step-2-add-a-dev-container-configuration)
  * [Step 3: Modify your devcontainer.json file](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-php-project-for-codespaces#step-3-modify-your-devcontainerjson-file)
  * [Step 4: Run your application](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-php-project-for-codespaces#step-4-run-your-application)
  * [Step 5: Commit your changes](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-php-project-for-codespaces#step-5-commit-your-changes)
  * [Next steps](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-php-project-for-codespaces#next-steps)


## [Introduction](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-php-project-for-codespaces#introduction)
This guide shows you how to set up an example PHP project in GitHub Codespaces using the Visual Studio Code web client. It will step you through the process of opening the project in a codespace, and adding and modifying a predefined dev container configuration.
After you complete this tutorial, you'll be able to add a dev container configuration to your own repository, using either the VS Code web client or the VS Code desktop application.
For more information about dev containers, see [Introduction to dev containers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers).
## [Step 1: Open the project in a codespace](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-php-project-for-codespaces#step-1-open-the-project-in-a-codespace)
  1. Sign in to GitHub.com, if you haven't already done so.
  2. Go to <https://github.com/microsoft/vscode-remote-try-php>.
  3. Click **Use this template** , then click **Open in a codespace**.
![Screenshot of the "Use this template" button and the dropdown menu expanded to show the "Open in a codespace" option.](https://docs.github.com/assets/cb-76823/images/help/repository/use-this-template-button.png)


When you create a codespace, your project is created on a remote virtual machine that is dedicated to you. By default, the container for your codespace has many languages and runtimes including PHP. It also includes a common set of tools, such as Composer, XDebug, Apache, pecl, nvm, git, lynx, and curl.
You can customize your codespace by adjusting the amount of vCPUs and RAM, adding dotfiles to personalize your environment, or by modifying the tools and scripts installed. For more information, see [Customizing your codespace](https://docs.github.com/en/codespaces/customizing-your-codespace).
GitHub Codespaces uses a file called `devcontainer.json` to configure the development container that you use when you work in a codespace. Each repository can contain one or more `devcontainer.json` files, to give you exactly the development environment you need to work on your code in a codespace.
On launch, GitHub Codespaces uses a `devcontainer.json` file, and any dependent files that make up the dev container configuration, to install tools and runtimes, and perform other setup tasks that the project requires. For more information, see [Introduction to dev containers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers).
## [Step 2: Add a dev container configuration](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-php-project-for-codespaces#step-2-add-a-dev-container-configuration)
The default development container, or "dev container," for GitHub Codespaces will allow you to work successfully on a PHP project like [vscode-remote-try-php](https://github.com/microsoft/vscode-remote-try-php). However, we recommend that you configure your own dev container to include all of the tools and scripts your project needs. This will ensure a fully reproducible environment for all GitHub Codespaces users in your repository.
To set up your repository to use a custom dev container, you will need to create one or more `devcontainer.json` files. You can either add these from a predefined configuration template, in Visual Studio Code, or you can write your own. For more information on dev container configurations, see [Introduction to dev containers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers).
  1. Access the Visual Studio Code Command Palette (`Shift`+`Command`+`P` / `Ctrl`+`Shift`+`P`), then start typing "add dev". Click **Codespaces: Add Dev Container Configuration Files**.
![Screenshot of the Command Palette, with "add dev" entered and "Codespaces: Add Dev Container Configuration Files" listed.](https://docs.github.com/assets/cb-12613/images/help/codespaces/add-prebuilt-container-command.png)
  2. Click **Create a new configuration**.
  3. In this example, the template repository from which you created the codespace already contains a dev container configuration, so a message is displayed telling you that the configuration file already exists. We're going to overwrite the existing configuration file, so click **Continue**.
  4. Click **Show All Definitions**.
![Screenshot of the "Add Dev Container Configuration Files" dropdown, showing various options, including "Show All Definitions."](https://docs.github.com/assets/cb-38549/images/help/codespaces/show-all-definitions.png)
  5. Type `php` and click **PHP**. Other options are available if your project uses particular tools. For example, **PHP & MariaDB**.
  6. Choose the version of PHP you want to use for your project. In this case, select the version marked "(default)."
  7. A list of additional features you can install is displayed. We'll install GitHub CLI, a tool for interacting with GitHub from the command line. To install this tool, type `github`, select `GitHub CLI`, then click **OK** , then select **Keep defaults**.
  8. A message is displayed telling you that the dev container configuration file already exists. Click **Overwrite**.
A `devcontainer.json` file is created and is opened in the editor.


### [Details of your custom dev container configuration](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-php-project-for-codespaces#details-of-your-custom-dev-container-configuration)
If you look in the Visual Studio Code Explorer you'll see that a `.devcontainer` directory has been added to the root of your project's repository containing the `devcontainer.json` file. This is the main configuration file for codespaces created from this repository.
#### [devcontainer.json](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-php-project-for-codespaces#devcontainerjson)
The `devcontainer.json` file that you have added will contain values for the `name`, `image`, and `features` properties. Some additional properties that you may find useful are included but are commented out.
The file will look similar to this, depending on which image you chose:
```
// For format details, see https://aka.ms/devcontainer.json. For config options, see the
// README at: https://github.com/devcontainers/templates/tree/main/src/php
{
  "name": "PHP",
  // Or use a Dockerfile or Docker Compose file. More info: https://containers.dev/guide/dockerfile
  "image": "mcr.microsoft.com/devcontainers/php:1-8.2-bullseye",

  // Features to add to the dev container. More info: https://containers.dev/features.
  // "features": {},

  // Configure tool-specific properties.
  // "customizations": {},

  // Use 'forwardPorts' to make a list of ports inside the container available locally.
  "forwardPorts": [
    8080
  ],
  "features": {
    "ghcr.io/devcontainers/features/github-cli:1": {}
  }

  // Use 'postCreateCommand' to run commands after the container is created.
  // "postCreateCommand": "sudo chmod a+x \"$(pwd)\" && sudo rm -rf /var/www/html && sudo ln -s \"$(pwd)\" /var/www/html"

  // Uncomment to connect as root instead. More info: https://aka.ms/dev-containers-non-root.
  // "remoteUser": "root"
}

```

  * **name:** You can name your dev container anything you want. A default value is supplied.
  * **image:** The name of an image in a container registry ([DockerHub](https://hub.docker.com/), [GitHub Container registry](https://docs.github.com/en/packages/learn-github-packages/introduction-to-github-packages), or [Azure Container Registry](https://azure.microsoft.com/services/container-registry/)) that will be used to create the dev container for the codespace.
  * **features:** A list of one or more objects, each of which references one of the available dev container features. Features are self-contained, shareable units of installation code and development container configuration. They provide an easy way to add more tooling, runtime, or library features to your development container. You can add features either within VS Code or in the `devcontainer.json` editor on GitHub. For more information, click either the **Visual Studio Code** or **Web browser** tab in [Adding features to a devcontainer.json file](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/configuring-dev-containers/adding-features-to-a-devcontainer-file?tool=webui).
  * **forwardPorts:** Any ports listed here will be forwarded automatically. For more information, see [Forwarding ports in your codespace](https://docs.github.com/en/codespaces/developing-in-codespaces/forwarding-ports-in-your-codespace).
  * **postCreateCommand:** Use this property to run commands after your codespace is created. This can be formatted as a string (as above), an array, or an object. For more information, see the [dev containers specification](https://containers.dev/implementors/json_reference/#lifecycle-scripts) on the Development Containers website.
  * **customizations:** This property allows you to customize a specific tool or service when it is used for working in a codespace. For example, you can configure specific settings and extensions for VS Code. For more information, see [Supporting tools and services](https://containers.dev/supporting) on the Development Containers website.
  * **remoteUser:** By default, you’re running as the vscode user, but you can optionally set this to root. For a complete list of available properties, see the [dev containers specification](https://containers.dev/implementors/json_reference/) on the Development Containers website.


#### [Additional dev container configuration files](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-php-project-for-codespaces#additional-dev-container-configuration-files)
If you are familiar with Docker, you may want to use a Dockerfile, or Docker Compose, to configure your codespace environment, in addition to the `devcontainer.json` file. You can do this by adding your `Dockerfile` or `docker-compose.yml` files alongside the `devcontainer.json` file. For more information, see [Using Images, Dockerfiles, and Docker Compose](https://containers.dev/guide/dockerfile) on the Development Containers website.
## [Step 3: Modify your devcontainer.json file](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-php-project-for-codespaces#step-3-modify-your-devcontainerjson-file)
With your dev container configuration added and a basic understanding of what everything does, you can now make changes to customize your environment further. In this example, you'll add properties that will:
  * Run `composer install`, after the dev container is created, to install the dependencies listed in a `composer.json` file.
  * Automatically install a VS Code extension in this codespace.


  1. In the `devcontainer.json` file, delete the two commented-out lines about features:
```
// Features to add to the dev container. More info: https://containers.dev/features.
// "features": {},

```

  2. Edit the `customizations` property as follows to install the "Composer" extension.
JSONC```
// Configure tool-specific properties.
"customizations": {
  // Configure properties specific to VS Code.
  "vscode": {
    "extensions": [
      "ikappas.composer"
    ]
  }
},

```
```
// Configure tool-specific properties.
"customizations": {
  // Configure properties specific to VS Code.
  "vscode": {
    "extensions": [
      "ikappas.composer"
    ]
  }
},

```

  3. Add a comma after the `features` property.
```
"features": {
  "ghcr.io/devcontainers/features/github-cli:1": {}
},

```

  4. Uncomment the `postCreateCommand` property and add some text to the end to run the command `composer install` if a `composer.json` file exists. (The existing commands are just some setup procedures that allow Apache to access the files in the workspace.)
JSONC```
// Use 'postCreateCommand' to run commands after the container is created.
"postCreateCommand": "sudo chmod a+x \"$(pwd)\" && sudo rm -rf /var/www/html && sudo ln -s \"$(pwd)\" /var/www/html; if [ -f composer.json ];then composer install;fi"

```
```
// Use 'postCreateCommand' to run commands after the container is created.
"postCreateCommand": "sudo chmod a+x \"$(pwd)\" && sudo rm -rf /var/www/html && sudo ln -s \"$(pwd)\" /var/www/html; if [ -f composer.json ];then composer install;fi"

```



The `devcontainer.json` file should now look similar to this, depending on which image you chose:
```
// For format details, see https://aka.ms/devcontainer.json. For config options, see the
// README at: https://github.com/devcontainers/templates/tree/main/src/php
{
  "name": "PHP",
  // Or use a Dockerfile or Docker Compose file. More info: https://containers.dev/guide/dockerfile
  "image": "mcr.microsoft.com/devcontainers/php:1-8.2-bullseye",

  // Configure tool-specific properties.
  "customizations": {
    // Configure properties specific to VS Code.
    "vscode": {
      "extensions": [
        "ikappas.composer"
      ]
    }
  },

  // Use 'forwardPorts' to make a list of ports inside the container available locally.
  "forwardPorts": [
    8080
  ],
  "features": {
    "ghcr.io/devcontainers/features/github-cli:1": {}
  },

  // Use 'postCreateCommand' to run commands after the container is created.
  "postCreateCommand": "sudo chmod a+x \"$(pwd)\" && sudo rm -rf /var/www/html && sudo ln -s \"$(pwd)\" /var/www/html; if [ -f composer.json ];then composer install;fi"

  // Uncomment to connect as root instead. More info: https://aka.ms/dev-containers-non-root.
  // "remoteUser": "root"
}

```

  1. Save your changes.
  2. Access the VS Code Command Palette (`Shift`+`Command`+`P` / `Ctrl`+`Shift`+`P`), then start typing "rebuild". Click **Codespaces: Rebuild Container**.
![Screenshot of the Command Palette with a search for "rebuild container" and the "Codespace: Rebuild Container" option highlighted in the dropdown.](https://docs.github.com/assets/cb-22518/images/help/codespaces/codespaces-rebuild.png)
You may occasionally want to perform a full rebuild to clear your cache and rebuild your container with fresh images. For more information, see [Rebuilding the container in a codespace](https://docs.github.com/en/codespaces/developing-in-codespaces/rebuilding-the-container-in-a-codespace#about-rebuilding-a-container). Rebuilding inside your codespace ensures your changes work as expected before you commit the changes to the repository. If something does result in a failure, you’ll be placed in a codespace with a recovery container that you can rebuild from to keep adjusting your container.
After the dev container is rebuilt, and your codespace becomes available again, the `postCreateCommand` will have been run, installing any Composer dependencies, and the "Composer" extension will be available for use.


## [Step 4: Run your application](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-php-project-for-codespaces#step-4-run-your-application)
In the previous section, you modified the `postCreateCommand` to install a set of packages via the `composer install` command. With the dependencies now installed, you can run the application. However, in this scenario we first need to change the ports that Apache will listen on. We're forwarding port 8080, so we'll instruct Apache to use this port rather than the default port 80.
  1. In the Terminal of your codespace, enter:
Shell```
sudo sed -i 's/Listen 80$//' /etc/apache2/ports.conf

```
```
sudo sed -i 's/Listen 80$//' /etc/apache2/ports.conf

```

  2. Then, enter:
Shell```
sudo sed -i 's/<VirtualHost \*:80>/ServerName 127.0.0.1\n<VirtualHost \*:8080>/' /etc/apache2/sites-enabled/000-default.conf

```
```
sudo sed -i 's/<VirtualHost \*:80>/ServerName 127.0.0.1\n<VirtualHost \*:8080>/' /etc/apache2/sites-enabled/000-default.conf

```

  3. Then start Apache using its control tool:
Shell```
apache2ctl start

```
```
apache2ctl start

```

  4. When your project starts, you should see a "toast" notification message at the bottom right corner of VS Code, telling you that your application is available on a forwarded port. To view the running application, click **Open in Browser**.


## [Step 5: Commit your changes](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-php-project-for-codespaces#step-5-commit-your-changes)
When you've made changes to your codespace, either new code or configuration changes, you'll want to commit your changes. Committing configuration changes to your repository ensures that anyone else who creates a codespace from this repository has the same configuration. Any customization you do, such as adding VS Code extensions, will be available to all users.
For this tutorial, you created a codespace from a template repository, so the code in your codespace is not yet stored in a repository. You can create a repository by publishing the current branch to GitHub.
For information, see [Using source control in your codespace](https://docs.github.com/en/codespaces/developing-in-codespaces/using-source-control-in-your-codespace?tool=webui#publishing-a-codespace-created-from-a-template).
## [Next steps](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-php-project-for-codespaces#next-steps)
You should now be able to add a custom dev container configuration to your own PHP project.
Here are some additional resources for more advanced scenarios.
  * [Adding features to a devcontainer.json file](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/configuring-dev-containers/adding-features-to-a-devcontainer-file?tool=webui)
  * [Managing your account-specific secrets for GitHub Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces)
  * [Managing GPG verification for GitHub Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-gpg-verification-for-github-codespaces)
  * [Forwarding ports in your codespace](https://docs.github.com/en/codespaces/developing-in-codespaces/forwarding-ports-in-your-codespace)


