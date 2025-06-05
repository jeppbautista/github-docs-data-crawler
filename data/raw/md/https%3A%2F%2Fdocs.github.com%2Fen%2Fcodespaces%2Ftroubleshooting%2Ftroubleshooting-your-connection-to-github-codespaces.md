  * [Codespaces](https://docs.github.com/en/codespaces "Codespaces")/
  * [Troubleshooting](https://docs.github.com/en/codespaces/troubleshooting "Troubleshooting")/
  * [Connection](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-your-connection-to-github-codespaces "Connection")


# Troubleshooting your connection to GitHub Codespaces
Troubleshooting help for connecting to GitHub Codespaces.
## In this article
  * [503 codespace service unavailable](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-your-connection-to-github-codespaces#503-codespace-service-unavailable)
  * [Browser cannot connect](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-your-connection-to-github-codespaces#browser-cannot-connect)
  * [Unable to connect to your codespace in JupyterLab](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-your-connection-to-github-codespaces#unable-to-connect-to-your-codespace-in-jupyterlab)
  * [GitHub Codespaces extension for Visual Studio Code cannot connect](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-your-connection-to-github-codespaces#github-codespaces-extension-for-visual-studio-code-cannot-connect)


## [503 codespace service unavailable](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-your-connection-to-github-codespaces#503-codespace-service-unavailable)
Codespaces are set to stop after 30 minutes without any activity. If you try to interact with a codespace after it has stopped, you may see a `503 service unavailable` error.
  * If a **Start** button is shown in Visual Studio Code or in your browser window, click **Start** to reconnect to the codespace.
  * Reset your codespace by reloading the window. From the [Command Palette](https://docs.github.com/en/codespaces/reference/using-the-vs-code-command-palette-in-codespaces#accessing-the-command-palette) in Visual Studio Code, click **Developer: Reload Window**.


## [Browser cannot connect](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-your-connection-to-github-codespaces#browser-cannot-connect)
Sometimes you may not be able to access a codespace from your browser. If this happens, go to <https://github.com/codespaces> and try connecting to the codespace from that page.
  * If the codespace is not listed on that page, check that you are the owner of the codespace you are trying to connect to. You can only open a codespace that you created.
  * If the codespace is listed but you cannot connect from that page, check whether you can connect using a different browser.


### [Diagnose by error message](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-your-connection-to-github-codespaces#diagnose-by-error-message)
#### ["Oh no, it looks like you are offline"](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-your-connection-to-github-codespaces#oh-no-it-looks-like-you-are-offline)
Check that you have a stable internet connection and that your company network is not blocking the connection. If possible, check logging for rejected connections on your device.
If you see rejected connections, make sure the domains documented by the `/meta` REST API endpoint are not blocked by your firewall. For more information, see [REST API endpoints for meta data](https://docs.github.com/en/rest/meta/meta#get-github-meta-information).
To get the list of domains required by GitHub Codespaces, execute the following command using GitHub CLI:
`gh api meta --jq .domains.codespaces`
### ["We are having trouble fetching your codespace information"](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-your-connection-to-github-codespaces#we-are-having-trouble-fetching-your-codespace-information)
This is a transitional error. Wait for a few minutes and try again.
### ["We were unable to authenticate your connection"](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-your-connection-to-github-codespaces#we-were-unable-to-authenticate-your-connection)
This indicates that something went wrong with authentication. Try clearing up your local storage and cookies and try again.
If you still can't connect and the message you're seeing isn't in this list, check the service availability of Codespaces at [githubstatus.com](https://www.githubstatus.com/). If the Codespaces service is available, you may need to contact support. For more information, see [Working with support for GitHub Codespaces](https://docs.github.com/en/codespaces/troubleshooting/working-with-support-for-github-codespaces).
## [Unable to connect to your codespace in JupyterLab](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-your-connection-to-github-codespaces#unable-to-connect-to-your-codespace-in-jupyterlab)
To be able to use a codespace in JupyterLab, you must ensure that your codespace has it installed. The default dev container image that's used by GitHub Codespaces includes JupyterLab, but if you have customized your dev container configuration you will have to manually install JupyterLab.
If your codespace uses a Debian-based image, you can install JupyterLab in the dev container by adding the `python` feature to your `devcontainer.json` file, with the `installJupyterlab` option set to `true`. Otherwise, install it directly in your Dockerfile. For installation instructions, see [Installation](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html) in the JupyterLab documentation.
For more information about the `python` feature, see the README page in the [`devcontainers/features` repository](https://github.com/devcontainers/features/tree/main/src/python). For more information about the `devcontainer.json` file and the Dockerfile, see [Introduction to dev containers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers#devcontainerjson).
If you still cannot connect, you may need to contact support. For more information, see [Working with support for GitHub Codespaces](https://docs.github.com/en/codespaces/troubleshooting/working-with-support-for-github-codespaces).
## [GitHub Codespaces extension for Visual Studio Code cannot connect](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-your-connection-to-github-codespaces#github-codespaces-extension-for-visual-studio-code-cannot-connect)
If you cannot connect to a codespace from Visual Studio Code desktop, use the following troubleshooting steps.
  1. Check that you have the latest version of the GitHub Codespaces extension installed. The extension is a preview release and frequent updates are released. 
    1. In Visual Studio Code, display the "Extensions" tab.
    2. Select the GitHub Codespaces extension to display the extension's overview page.
    3. If an update is available, a button is shown, click **Update to X.X.X** to upgrade to the latest version.
  2. Check whether you are using the stable build of Visual Studio Code or the [Visual Studio Code Insiders](https://code.visualstudio.com/insiders/) release (nightly updates). If you are using the insiders release, try installing the [stable build](https://code.visualstudio.com/).
  3. Make sure your company network is not blocking the connection. 
    1. If you receive errors like `connect EACCES`, `connect ECONNREFUSED`, `getaddrinfo ENOTFOUND`, or other similar errors, your firewall is likely blocking connections to our connection service. To verify this, please visit [this URL](https://global.rel.tunnels.api.visualstudio.com/api/version). If the request fails or you see no data, you likely need to work with your system administrator add `*.visualstudio.com` to your firewall's IP allow list.
    2. If you see the error `Tunnel service HTTPS certificate is invalid. This may be caused by the use of a self-signed certificate or a firewall intercepting the connection` it's likely that your firewall is doing TLS inspection and injecting a self-signed certificate which GitHub is not able to verify. To resolve this, your system administrator will either need to allow `*.visualstudio.com` to bypass the inspection or install the root CA that the firewall is injecting on your local machine.


If you still cannot connect, you may need to contact support. For more information, see [Working with support for GitHub Codespaces](https://docs.github.com/en/codespaces/troubleshooting/working-with-support-for-github-codespaces).
### [The codespace has latency issues](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-your-connection-to-github-codespaces#the-codespace-has-latency-issues)
If the codespace seems particularly slow or has latency issues, it is possible that it has been created in a region that is far from you. To resolve this, you can [manually set your GitHub Codespaces region](https://docs.github.com/en/codespaces/setting-your-user-preferences/setting-your-default-region-for-github-codespaces).
