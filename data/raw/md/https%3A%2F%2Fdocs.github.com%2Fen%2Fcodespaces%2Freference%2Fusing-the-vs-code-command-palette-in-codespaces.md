  * [Codespaces](https://docs.github.com/en/codespaces "Codespaces")/
  * [Reference](https://docs.github.com/en/codespaces/reference "Reference")/
  * [VS Code Command Palette](https://docs.github.com/en/codespaces/reference/using-the-vs-code-command-palette-in-codespaces "VS Code Command Palette")


# Using the Visual Studio Code Command Palette in GitHub Codespaces
You can use the Command Palette feature of Visual Studio Code to access many commands in GitHub Codespaces.
## In this article
  * [About the Visual Studio Code Command Palette](https://docs.github.com/en/codespaces/reference/using-the-vs-code-command-palette-in-codespaces#about-the-visual-studio-code-command-palette)
  * [Accessing the VS Code Command Palette](https://docs.github.com/en/codespaces/reference/using-the-vs-code-command-palette-in-codespaces#accessing-the-vs-code-command-palette)
  * [Commands for Codespaces](https://docs.github.com/en/codespaces/reference/using-the-vs-code-command-palette-in-codespaces#commands-for-codespaces)
  * [Further reading](https://docs.github.com/en/codespaces/reference/using-the-vs-code-command-palette-in-codespaces#further-reading)


## [About the Visual Studio Code Command Palette](https://docs.github.com/en/codespaces/reference/using-the-vs-code-command-palette-in-codespaces#about-the-visual-studio-code-command-palette)
The VS Code Command Palette is one of the focal features of Visual Studio Code and is available for you to use in GitHub Codespaces. The Command Palette allows you to access many commands for GitHub Codespaces and VS Code. For more information on using the VS Code Command Palette, see [User Interface](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) in the VS Code documentation.
## [Accessing the VS Code Command Palette](https://docs.github.com/en/codespaces/reference/using-the-vs-code-command-palette-in-codespaces#accessing-the-vs-code-command-palette)
You can access the VS Code Command Palette in a number of ways.
  * `Shift`+`Command`+`P` (Mac) / `Ctrl`+`Shift`+`P` (Windows/Linux).
Note that this command is a reserved keyboard shortcut in Firefox.
  * `F1`
  * From the Application Menu, click **View > Command Palette**.


## [Commands for Codespaces](https://docs.github.com/en/codespaces/reference/using-the-vs-code-command-palette-in-codespaces#commands-for-codespaces)
To see all commands related to GitHub Codespaces, [access the VS Code Command Palette](https://docs.github.com/en/codespaces/reference/using-the-vs-code-command-palette-in-codespaces#accessing-the-vs-code-command-palette), then start typing "Codespaces".
![Screenshot of the Command Palette with "codespaces" entered. The dropdown lists all commands that relate to GitHub Codespaces.](https://docs.github.com/assets/cb-187285/images/help/codespaces/codespaces-command-palette.png)
### [Suspending or stopping a codespace](https://docs.github.com/en/codespaces/reference/using-the-vs-code-command-palette-in-codespaces#suspending-or-stopping-a-codespace)
If you add a new secret or change the machine type, you'll have to stop and restart the codespace for it to apply your changes.
To suspend or stop your codespace's container, [access the VS Code Command Palette](https://docs.github.com/en/codespaces/reference/using-the-vs-code-command-palette-in-codespaces#accessing-the-vs-code-command-palette), then start typing "stop". Select **Codespaces: Stop Current Codespace**.
![Screenshot of the Command Palette with the search text "stop" and the option "Codespaces: Stop Current Codespace."](https://docs.github.com/assets/cb-9151/images/help/codespaces/codespaces-stop.png)
### [Adding a predefined dev container configuration](https://docs.github.com/en/codespaces/reference/using-the-vs-code-command-palette-in-codespaces#adding-a-predefined-dev-container-configuration)
To add a predefined dev container configuration, [access the VS Code Command Palette](https://docs.github.com/en/codespaces/reference/using-the-vs-code-command-palette-in-codespaces#accessing-the-vs-code-command-palette), then start typing "add dev". Click **Codespaces: Add Dev Container Configuration Files**.
![Screenshot of the Command Palette, with "add dev" entered and "Codespaces: Add Dev Container Configuration Files" listed.](https://docs.github.com/assets/cb-12613/images/help/codespaces/add-prebuilt-container-command.png)
### [Rebuilding a codespace](https://docs.github.com/en/codespaces/reference/using-the-vs-code-command-palette-in-codespaces#rebuilding-a-codespace)
If you add a dev container or edit any of the configuration files (`devcontainer.json` and `Dockerfile`), you'll have to rebuild your codespace for it to apply your changes.
To rebuild your container, [access the VS Code Command Palette](https://docs.github.com/en/codespaces/reference/using-the-vs-code-command-palette-in-codespaces#accessing-the-vs-code-command-palette), then start typing "rebuild". Select **Codespaces: Rebuild Container**.
![Screenshot of the Command Palette with the search text "rebuild" and the option "Codespaces: Rebuild Container."](https://docs.github.com/assets/cb-22518/images/help/codespaces/codespaces-rebuild.png)
You may occasionally want to perform a full rebuild to clear your cache and rebuild your container with fresh images. For more information, see [Rebuilding the container in a codespace](https://docs.github.com/en/codespaces/developing-in-codespaces/rebuilding-the-container-in-a-codespace#about-rebuilding-a-container).
### [Codespaces logs](https://docs.github.com/en/codespaces/reference/using-the-vs-code-command-palette-in-codespaces#codespaces-logs)
You can use the VS Code Command Palette to access the codespace creation logs, or you can use it export all logs.
To retrieve the logs for GitHub Codespaces, [access the VS Code Command Palette](https://docs.github.com/en/codespaces/reference/using-the-vs-code-command-palette-in-codespaces#accessing-the-vs-code-command-palette), then start typing "export". Select **Codespaces: Export Logs** to export all logs related to GitHub Codespaces or select **Codespaces: View Creation Logs** to view logs related to the setup.
![Screenshot of the Command Palette with the search text "export" and the option "Codespaces: Export Logs."](https://docs.github.com/assets/cb-7269/images/help/codespaces/codespaces-logs.png)
## [Further reading](https://docs.github.com/en/codespaces/reference/using-the-vs-code-command-palette-in-codespaces#further-reading)
  * [Using GitHub Codespaces in Visual Studio Code](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-github-codespaces-in-visual-studio-code)


