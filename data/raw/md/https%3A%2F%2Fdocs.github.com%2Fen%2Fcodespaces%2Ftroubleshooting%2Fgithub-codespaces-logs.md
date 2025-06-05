  * [Codespaces](https://docs.github.com/en/codespaces "Codespaces")/
  * [Troubleshooting](https://docs.github.com/en/codespaces/troubleshooting "Troubleshooting")/
  * [Codespaces logs](https://docs.github.com/en/codespaces/troubleshooting/github-codespaces-logs "Codespaces logs")


# GitHub Codespaces logs
Overview of the logs used by GitHub Codespaces.
## Tool navigation
  * [GitHub CLI](https://docs.github.com/en/codespaces/troubleshooting/github-codespaces-logs?tool=cli)
  * [Visual Studio Code](https://docs.github.com/en/codespaces/troubleshooting/github-codespaces-logs?tool=vscode)
  * [Web browser](https://docs.github.com/en/codespaces/troubleshooting/github-codespaces-logs?tool=webui)


## In this article
  * [Codespace logs](https://docs.github.com/en/codespaces/troubleshooting/github-codespaces-logs#codespace-logs)
  * [Codespace logs](https://docs.github.com/en/codespaces/troubleshooting/github-codespaces-logs#codespace-logs-1)
  * [Codespace logs](https://docs.github.com/en/codespaces/troubleshooting/github-codespaces-logs#codespace-logs-2)
  * [Creation logs](https://docs.github.com/en/codespaces/troubleshooting/github-codespaces-logs#creation-logs)
  * [Extension logs](https://docs.github.com/en/codespaces/troubleshooting/github-codespaces-logs#extension-logs)
  * [Browser console logs](https://docs.github.com/en/codespaces/troubleshooting/github-codespaces-logs#browser-console-logs)
  * [Further reading](https://docs.github.com/en/codespaces/troubleshooting/github-codespaces-logs#further-reading)


Information on GitHub Codespaces is output to various logs:
  * Codespace logs
  * Creation logs
  * Browser console logs (for the VS Code web client)


Extension logs are available if you are using GitHub Codespaces in VS Code. Click the "Visual Studio Code" tab above for details.
  * Codespace logs
  * Creation logs
  * Extension logs (for the VS Code desktop application)


Browser logs are available if you are using GitHub Codespaces in your browser. Click the "Web browser" tab above for details.
  * Codespace logs
  * Creation logs


Other logs are available if you are using GitHub Codespaces in VS Code or in your web browser. Click the tabs above for details.
## [Codespace logs](https://docs.github.com/en/codespaces/troubleshooting/github-codespaces-logs#codespace-logs)
These logs contain detailed information about the codespace, the container, the session, and the VS Code environment. They are useful for diagnosing connection issues and other unexpected behavior. For example, the codespace freezes but the "Reload Windows" option unfreezes it for a few minutes, or you are randomly disconnected from the codespace but able to reconnect immediately.
  1. If you are using GitHub Codespaces in the browser, ensure that you are connected to the codespace you want to debug.
  2. Open the VS Code Command Palette (`Shift`+`Command`+`P` (Mac) / `Ctrl`+`Shift`+`P` (Windows/Linux)) and type `export logs`. Select **Codespaces: Export Logs** from the list to download the logs.
  3. Define where to save the zip archive of logs then click **Save** (desktop) or click **OK** (web).
  4. If you are using GitHub Codespaces in the browser, right-click on the zip archive of logs from the Explorer view and select **Download…** to download them to your local machine.


## [Codespace logs](https://docs.github.com/en/codespaces/troubleshooting/github-codespaces-logs#codespace-logs-1)
These logs contain detailed information about the codespace, the container, the session, and the VS Code environment. They are useful for diagnosing connection issues and other unexpected behavior. For example, the codespace freezes but the "Reload Windows" option unfreezes it for a few minutes, or you are randomly disconnected from the codespace but able to reconnect immediately.
  1. Open the VS Code Command Palette (`Shift`+`Command`+`P` (Mac) / `Ctrl`+`Shift`+`P` (Windows/Linux)) and type `export log`. Select **Codespaces: Export Logs** from the list to download the logs.
  2. Define where to save the zip archive of logs then click **Save** (desktop) or click **OK** (web).


## [Codespace logs](https://docs.github.com/en/codespaces/troubleshooting/github-codespaces-logs#codespace-logs-2)
These logs contain detailed information about the codespace, the container, the session, and the VS Code environment. They are useful for diagnosing connection issues and other unexpected behavior. For example, the codespace freezes but the "Reload Windows" option unfreezes it for a few minutes, or you are randomly disconnected from the codespace but able to reconnect immediately.
Currently you can't use GitHub CLI to access these logs. To access them, open your codespace in VS Code or in a browser.
## [Creation logs](https://docs.github.com/en/codespaces/troubleshooting/github-codespaces-logs#creation-logs)
These logs contain information about the container, dev container, and their configuration. They are useful for debugging configuration and setup problems.
  1. Connect to the codespace you want to debug.
  2. Open the VS Code Command Palette (`Shift`+`Command`+`P` (Mac) / `Ctrl`+`Shift`+`P` (Windows/Linux)) and type `creation log`. Select **Codespaces: View Creation Log** from the list to open the `creation.log` file.


If you want to share the log with support, you can copy the text from the creation log into a text editor and save the file locally.
Open the VS Code Command Palette (`Shift`+`Command`+`P` (Mac) / `Ctrl`+`Shift`+`P` (Windows/Linux)) and type `creation log`. Select **Codespaces: View Creation Log** from the list to open the `creation.log` file.
If you want to share the log with support, you can copy the text from the creation log into a text editor and save the file locally.
To learn more about GitHub CLI, see [About GitHub CLI](https://docs.github.com/en/github-cli/github-cli/about-github-cli).
To see the creation log use the `gh codespace logs` subcommand. After entering the command choose from the list of codespaces that's displayed.
```
gh codespace logs

```

For more information about this command, see [the GitHub CLI manual](https://cli.github.com/manual/gh_codespace_logs).
If you want to share the log with support, you can save the output to a file:
```
gh codespace logs -c <CODESPACE-NAME> > /path/to/logs.txt

```

## [Extension logs](https://docs.github.com/en/codespaces/troubleshooting/github-codespaces-logs#extension-logs)
These logs are available for VS Code desktop users only. They are useful if it seems like the GitHub Codespaces extension or VS Code editor are having issues that prevent creation or connection.
  1. In VS Code, open the Command Palette.
  2. Type `logs` and select **Developer: Open Extension Logs Folder**.
  3. Your system's file explorer is displayed showing various log files and folders. Open the folder `output_logging_DATETIME`.


From this view, you can access logs generated by extensions you use in VS Code, including GitHub Codespaces.
## [Browser console logs](https://docs.github.com/en/codespaces/troubleshooting/github-codespaces-logs#browser-console-logs)
These logs are useful only if you want to debug problems with using GitHub Codespaces in the browser. They are useful for debugging problems creating and connecting to GitHub Codespaces.
The following instructions are for Chrome. The steps for other browsers are similar.
  1. In the browser window for the codespace you want to debug, open the developer tools window.
  2. Click the **Console** tab.
  3. Show the console sidebar, if it is not already displayed. For more information, see [Console features reference](https://developer.chrome.com/docs/devtools/console/reference#sidebar) in the Chrome for Developers documentation.
  4. In the sidebar, click **NUMBER errors** to show only the errors.
  5. In the log area on the right, right-click and select **Save as** to save a copy of the errors to your local machine.
![Screenshot of the developer tools panel in the Chrome browser. The right-click menu is displayed, showing the option "Save as."](https://docs.github.com/assets/cb-192184/images/help/codespaces/browser-console-log-save.png)


## [Further reading](https://docs.github.com/en/codespaces/troubleshooting/github-codespaces-logs#further-reading)
  * [Reviewing your organization's audit logs for GitHub Codespaces](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/reviewing-your-organizations-audit-logs-for-github-codespaces)
  * [Reviewing your security logs for GitHub Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/reviewing-your-security-logs-for-github-codespaces)


