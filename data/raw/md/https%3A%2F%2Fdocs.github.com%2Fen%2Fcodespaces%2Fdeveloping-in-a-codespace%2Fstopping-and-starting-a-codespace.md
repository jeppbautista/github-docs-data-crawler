  * [Codespaces](https://docs.github.com/en/codespaces "Codespaces")/
  * [Developing in a codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace "Developing in a codespace")/
  * [Stop a codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/stopping-and-starting-a-codespace "Stop a codespace")


# Stopping and starting a codespace
You can stop and start your codespace to save resources and to pause work.
## Tool navigation
  * [GitHub CLI](https://docs.github.com/en/codespaces/developing-in-a-codespace/stopping-and-starting-a-codespace?tool=cli)
  * [Visual Studio Code](https://docs.github.com/en/codespaces/developing-in-a-codespace/stopping-and-starting-a-codespace?tool=vscode)
  * [Web browser](https://docs.github.com/en/codespaces/developing-in-a-codespace/stopping-and-starting-a-codespace?tool=webui)


## In this article
  * [About stopping and starting a codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/stopping-and-starting-a-codespace#about-stopping-and-starting-a-codespace)
  * [Stopping a codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/stopping-and-starting-a-codespace#stopping-a-codespace)
  * [Restarting a codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/stopping-and-starting-a-codespace#restarting-a-codespace)
  * [Further reading](https://docs.github.com/en/codespaces/developing-in-a-codespace/stopping-and-starting-a-codespace#further-reading)


## [About stopping and starting a codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/stopping-and-starting-a-codespace#about-stopping-and-starting-a-codespace)
You can stop a codespace at any time. When you stop a codespace, any running processes are stopped. Any saved changes in your codespace will still be available when you next start it. The terminal history is preserved, but the visible contents of the terminal window are not preserved between codespace sessions.
If you do not explicitly stop a codespace, it will continue to run until it times out from inactivity. Closing a codespace does not stop the codespace. For example, if you're using a codespace in the VS Code web client and you close the browser tab, the codespace remains running on the remote machine. For information about timeouts, see [Understanding the codespace lifecycle](https://docs.github.com/en/codespaces/about-codespaces/the-codespace-lifecycle#timeouts-for-github-codespaces).
Only running codespaces incur CPU charges. A stopped codespace incurs only storage costs.
You may want to stop and restart a codespace to apply changes to it. For example, if you change the machine type used for your codespace, you will need to stop and restart it for the change to take effect. You can also stop your codespace and choose to restart or delete it if you encounter an error or something unexpected.
Regardless of where you created or access your codespaces, you can view and manage them in your browser at <https://github.com/codespaces>.
## [Stopping a codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/stopping-and-starting-a-codespace#stopping-a-codespace)
  1. Navigate to the "Your Codespaces" page at <https://github.com/codespaces>.
  2. To the right of the codespace you want to stop, click the ellipsis (**...**).
  3. Click **Stop codespace**.


![Screenshot of a list of codespaces with the dropdown menu for one of them displayed, showing the "Stop codespace" option.](https://docs.github.com/assets/cb-90117/images/help/codespaces/stop-codespace-webui.png)
To learn more about GitHub CLI, see [About GitHub CLI](https://docs.github.com/en/github-cli/github-cli/about-github-cli).
To stop a codespace use the `gh codespace stop` subcommand and then choose the codespace you want to stop from the list that's displayed.
Shell```
gh codespace stop

```
```
gh codespace stop

```

  1. Open the VS Code Command Palette (`Shift`+`Command`+`P` (Mac) / `Ctrl`+`Shift`+`P` (Windows/Linux)).
  2. Type `stop` and select **Codespaces: Stop Codespace** from the list of options.
  3. In the list of codespaces, select the codespace you want to stop.


## [Restarting a codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/stopping-and-starting-a-codespace#restarting-a-codespace)
  1. Navigate to the "Your Codespaces" page at <https://github.com/codespaces>.
  2. Click the name of the codespace you want to restart.
![Screenshot of a list of two codespaces on GitHub. The names of the codespaces are highlighted with dark orange outlines.](https://docs.github.com/assets/cb-52884/images/help/codespaces/restart-codespace-webui.png)


When you restart a codespace you can choose to open it in Visual Studio Code or in your browser.
  * To restart a codespace and open it in Visual Studio Code, use the `gh codespace code` subcommand and then choose the codespace you want to restart from the list that's displayed.
Shell```
gh codespace code

```
```
gh codespace code

```

  * To restart a codespace and open it in your browser, use the `gh codespace open --web` subcommand and then choose the codespace you want to restart from the list that's displayed.
Shell```
gh codespace open --web

```
```
gh codespace open --web

```



  1. Open the VS Code Command Palette (`Shift`+`Command`+`P` (Mac) / `Ctrl`+`Shift`+`P` (Windows/Linux)).
  2. Type `connect` and select **Codespaces: Connect to Codespace** from the list of options.
  3. In the list of codespaces, select the codespace you want to restart.


## [Further reading](https://docs.github.com/en/codespaces/developing-in-a-codespace/stopping-and-starting-a-codespace#further-reading)
  * [Understanding the codespace lifecycle](https://docs.github.com/en/codespaces/about-codespaces/understanding-the-codespace-lifecycle)


