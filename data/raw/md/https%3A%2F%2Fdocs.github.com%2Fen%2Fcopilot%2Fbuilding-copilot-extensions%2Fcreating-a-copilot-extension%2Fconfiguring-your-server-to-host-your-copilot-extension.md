  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Build Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions "Build Copilot Extensions")/
  * [Create a Copilot Extension](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension "Create a Copilot Extension")/
  * [Host your extension](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/configuring-your-server-to-host-your-copilot-extension "Host your extension")


# Configuring your server to host your Copilot extension
Learn how to make your Copilot extension accessible to the internet.
## In this article
  * [Prerequisites](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/configuring-your-server-to-host-your-copilot-extension#prerequisites)
  * [Configuring your server](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/configuring-your-server-to-host-your-copilot-extension#configuring-your-server)
  * [Next steps](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/configuring-your-server-to-host-your-copilot-extension#next-steps)


Your Copilot Extension must be hosted on a server that is accessible to the internet. In this guide, we will use [ngrok](https://ngrok.com/) to create a tunnel to your local server, but you could also use a service like [localtunnel](https://localtunnel.github.io/www/).
Alternatively, if you are a Codespaces user, you can use the built-in Codespaces port forwarding. For more information, see [Forwarding ports in your codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace).
## [Prerequisites](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/configuring-your-server-to-host-your-copilot-extension#prerequisites)
  * You have created a Copilot Extension. For more information, see [Building a Copilot agent for your Copilot Extension](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension) or [Building a Copilot skillset for your Copilot Extension](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-skillset-for-your-copilot-extension).


## [Configuring your server](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/configuring-your-server-to-host-your-copilot-extension#configuring-your-server)
  1. Visit the [ngrok setup & installation page](https://dashboard.ngrok.com/get-started/setup/).
  2. If you do not yet have an account, follow the instructions on screen to sign up.
  3. Under "Agents," ensure the correct operating system is selected.
  4. Under "Installation," follow the instructions for your operating system to download and install ngrok.
  5. Under "Deploy your app online," select **Ephemeral domain** or **Static domain**.
  6. Run the command provided in your terminal, replacing the port number with the port your extension is configured to run on. For example:
     * For an ephemeral domain:
Shell```
ngrok http http://localhost:EXTENSION-PORT-NUMBER

```
```
ngrok http http://localhost:EXTENSION-PORT-NUMBER

```

     * For a static domain:
Shell```
ngrok http --domain=YOUR-STATIC-DOMAIN.ngrok-free.app EXTENSION-PORT-NUMBER

```
```
ngrok http --domain=YOUR-STATIC-DOMAIN.ngrok-free.app EXTENSION-PORT-NUMBER

```

  7. In your terminal, next to "Forwarding," copy the URL that ngrok has assigned to your server. You will need this forwarding endpoint when you are configuring your GitHub App.
Do not copy the `-> http://localhost:XXXX` part of the URL.
Keep the terminal window open while you are using your extension.


## [Next steps](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/configuring-your-server-to-host-your-copilot-extension#next-steps)
  * [Creating a GitHub App for your Copilot Extension](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/creating-a-github-app-for-your-copilot-extension)


