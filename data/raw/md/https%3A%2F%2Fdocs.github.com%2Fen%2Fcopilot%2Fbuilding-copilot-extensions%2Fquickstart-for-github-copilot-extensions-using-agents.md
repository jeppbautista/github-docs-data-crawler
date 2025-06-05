  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Build Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions "Build Copilot Extensions")/
  * [Extensions quickstart](https://docs.github.com/en/copilot/building-copilot-extensions/quickstart-for-github-copilot-extensions-using-agents "Extensions quickstart")


# Quickstart for GitHub Copilot Extensions using agents
Build and try out GitHub's Blackbeard extension to learn about the development process for GitHub Copilot Extensions.
## Tool navigation
  * [Bash](https://docs.github.com/en/copilot/building-copilot-extensions/quickstart-for-github-copilot-extensions-using-agents?tool=bash)
  * [Codespaces](https://docs.github.com/en/copilot/building-copilot-extensions/quickstart-for-github-copilot-extensions-using-agents?tool=codespaces)
  * [Visual Studio Code](https://docs.github.com/en/copilot/building-copilot-extensions/quickstart-for-github-copilot-extensions-using-agents?tool=vscode)


## In this article
  * [1. Create and install a GitHub App](https://docs.github.com/en/copilot/building-copilot-extensions/quickstart-for-github-copilot-extensions-using-agents#1-create-and-install-a-github-app)
  * [2. Clone and host the Blackbeard agent locally](https://docs.github.com/en/copilot/building-copilot-extensions/quickstart-for-github-copilot-extensions-using-agents#2-clone-and-host-the-blackbeard-agent-locally)
  * [3. Integrate and test the Blackbeard extension](https://docs.github.com/en/copilot/building-copilot-extensions/quickstart-for-github-copilot-extensions-using-agents#3-integrate-and-test-the-blackbeard-extension)
  * [2. Clone and host the Blackbeard agent in a codespace](https://docs.github.com/en/copilot/building-copilot-extensions/quickstart-for-github-copilot-extensions-using-agents#2-clone-and-host-the-blackbeard-agent-in-a-codespace)
  * [3. Integrate and test the Blackbeard extension](https://docs.github.com/en/copilot/building-copilot-extensions/quickstart-for-github-copilot-extensions-using-agents#3-integrate-and-test-the-blackbeard-extension-1)
  * [2. Clone and start the Blackbeard agent locally](https://docs.github.com/en/copilot/building-copilot-extensions/quickstart-for-github-copilot-extensions-using-agents#2-clone-and-start-the-blackbeard-agent-locally)
  * [3. Expose your local server](https://docs.github.com/en/copilot/building-copilot-extensions/quickstart-for-github-copilot-extensions-using-agents#3-expose-your-local-server)
  * [4. Integrate and test the Blackbeard extension](https://docs.github.com/en/copilot/building-copilot-extensions/quickstart-for-github-copilot-extensions-using-agents#4-integrate-and-test-the-blackbeard-extension)
  * [Next steps](https://docs.github.com/en/copilot/building-copilot-extensions/quickstart-for-github-copilot-extensions-using-agents#next-steps)


The [Blackbeard extension](https://github.com/copilot-extensions/blackbeard-extension) is a GitHub Copilot Extension that comprises a GitHub App and a Copilot agent. The agent responds to chat requests in the style of a pirate, using Copilot's large language model (LLM) API and special system prompts. See [About Copilot agents](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/about-copilot-agents).
This guide uses a simple agent implementation, but the process is similar for skillsets. For information about the difference between agents and skillsets, see [About building Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions#about-skillsets-and-agents).
This quickstart is designed to help you build and chat with the Blackbeard extension as quickly as possible, so you can develop and test your extension without deploying infrastructure. For production, you'll need to host the application for your agent or skillset's endpoints on a publicly accessible server. To instead learn how to create a new GitHub Copilot Extension, see [Setting up Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions/setting-up-copilot-extensions).
## [1. Create and install a GitHub App](https://docs.github.com/en/copilot/building-copilot-extensions/quickstart-for-github-copilot-extensions-using-agents#1-create-and-install-a-github-app)
In the developer settings for your GitHub account, create a GitHub App. Your GitHub App must have:
  * A name
  * A homepage URL
  * Webhooks deselected


After you create your app, click **Install App** in the sidebar, then install your app on your account.
For detailed instructions, see [Creating a GitHub App for your Copilot Extension](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/creating-a-github-app-for-your-copilot-extension#creating-a-github-app).
## [2. Clone and host the Blackbeard agent locally](https://docs.github.com/en/copilot/building-copilot-extensions/quickstart-for-github-copilot-extensions-using-agents#2-clone-and-host-the-blackbeard-agent-locally)
Rather than deploying the Blackbeard agent as a web app, you can host your agent locally for a significantly faster build process.
  1. Using the Terminal built into VS Code, clone the [`copilot-extensions/blackbeard-extension`](https://github.com/copilot-extensions/blackbeard-extension) repository.
  2. In the same Terminal, run `npm install` to install the necessary dependencies, then run `npm start` to start the Blackbeard agent on port 3000.
  3. In the "Ports" tab of the VS Code panel, click **Forward a port** or **Add port** , then add port 3000.
  4. Right-click the port and set the visibility to "Public," then copy the local address.


## [3. Integrate and test the Blackbeard extension](https://docs.github.com/en/copilot/building-copilot-extensions/quickstart-for-github-copilot-extensions-using-agents#3-integrate-and-test-the-blackbeard-extension)
After you set up your GitHub App and Blackbeard agent, you can integrate the agent with your app and test the Blackbeard extension. You need to make the following changes to your GitHub App settings:
  * In the "General" settings, in the "Callback URL" field, paste the local address for your agent.
  * In the "Permissions & events" settings, grant read-only permissions to Copilot Chat.
  * In the "Copilot" settings, set your app type to "Agent," then fill out the remaining fields.


After you update your GitHub App settings, you can start chatting with your extension by typing `@YOUR-EXTENSION-NAME` in the Copilot Chat window, then sending a prompt as normal.
For more detailed instructions, see [Configuring your GitHub App for your Copilot extension](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/configuring-your-github-app-for-your-copilot-agent#configuring-your-github-app).
## [2. Clone and host the Blackbeard agent in a codespace](https://docs.github.com/en/copilot/building-copilot-extensions/quickstart-for-github-copilot-extensions-using-agents#2-clone-and-host-the-blackbeard-agent-in-a-codespace)
Rather than deploying the Blackbeard agent as a web app, you can host your agent in a codespace for a significantly faster build process.
  1. Navigate to the [`copilot-extensions/blackbeard-extension`](https://github.com/copilot-extensions/blackbeard-extension) repository. Select the **Create codespace on main**.
  2. To find your new codespace, select the 
  3. In the integrated Terminal, run `npm start` to start the Blackbeard agent on port 3000.
  4. In the "Ports" tab of the VS Code panel, click **Forward a port** , then add port 3000.
  5. Right-click the port and set the visibility to "Public," then copy the local address.


## [3. Integrate and test the Blackbeard extension](https://docs.github.com/en/copilot/building-copilot-extensions/quickstart-for-github-copilot-extensions-using-agents#3-integrate-and-test-the-blackbeard-extension-1)
After you set up your GitHub App and Blackbeard agent, you can integrate the agent with your app and test the Blackbeard extension. You need to make the following changes to your GitHub App settings:
  * In the "General" settings, in the "Callback URL" field, paste the forwarded address for your agent.
  * In the "Permissions & events" settings, grant read-only permissions to Copilot Chat.
  * In the "Copilot" settings, set your app type to "Agent," then fill out the remaining fields.


After you update your GitHub App settings, you can start chatting with your extension by typing `@YOUR-EXTENSION-NAME` in the Copilot Chat window of a supported client or IDE, then sending a prompt as normal. For a list of supported clients and IDEs, see [About building Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions#supported-clients-and-ides).
Chatting with GitHub Copilot Extensions in GitHub Codespaces is not supported.
For more detailed instructions, see [Configuring your GitHub App for your Copilot extension](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/configuring-your-github-app-for-your-copilot-agent#configuring-your-github-app).
## [2. Clone and start the Blackbeard agent locally](https://docs.github.com/en/copilot/building-copilot-extensions/quickstart-for-github-copilot-extensions-using-agents#2-clone-and-start-the-blackbeard-agent-locally)
Rather than deploying the Blackbeard agent as a web app, you can host your agent locally for a significantly faster build process.
  1. Using your command line application, clone the [`copilot-extensions/blackbeard-extension`](https://github.com/copilot-extensions/blackbeard-extension) repository.
  2. Run `npm install` to install the necessary dependencies, then run `npm start` to start the Blackbeard agent on port 3000.


## [3. Expose your local server](https://docs.github.com/en/copilot/building-copilot-extensions/quickstart-for-github-copilot-extensions-using-agents#3-expose-your-local-server)
To make the Blackbeard agent accessible to the Copilot platform and GitHub, you need to expose your local server so it's reachable by HTTP requests. You can use any port forwarding or tunneling service to achieve this. For the following steps, we'll use ngrok.
  1. Navigate to [ngrok's download page](https://ngrok.com/downloads/), then install the appropriate version of ngrok for your operating system.
  2. Navigate to the [ngrok setup and installation page](https://dashboard.ngrok.com/get-started/setup/), then log in or sign up for an ngrok account.
  3. To expose your local server, in a new window of your command line application, run the following command:
Shell```
ngrok http http://localhost:3000

```
```
ngrok http http://localhost:3000

```

  4. In your command line application, next to "Forwarding," copy the URL that ngrok assigned to your server.


## [4. Integrate and test the Blackbeard extension](https://docs.github.com/en/copilot/building-copilot-extensions/quickstart-for-github-copilot-extensions-using-agents#4-integrate-and-test-the-blackbeard-extension)
To integrate your GitHub App with the Blackbeard agent, you need to make the following changes to your app settings:
  * In the "General" settings, in the "Callback URL" field, paste the URL for your exposed server.
  * In the "Permissions & events" settings, grant read-only permissions to Copilot Chat.
  * In the "Copilot" settings, set your app type to "Agent," then fill out the remaining fields.


After you update your GitHub App settings, you can start chatting with your extension by typing `@YOUR-EXTENSION-NAME` in the Copilot Chat window, then sending a prompt as normal.
For more detailed instructions, see [Configuring your GitHub App for your Copilot extension](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/configuring-your-github-app-for-your-copilot-agent#configuring-your-github-app).
## [Next steps](https://docs.github.com/en/copilot/building-copilot-extensions/quickstart-for-github-copilot-extensions-using-agents#next-steps)
Now that you have a working GitHub Copilot Extension, you can try building on the Blackbeard agent to experiment with agent development.
To learn about more complex agent implementations, you can also review the following example agents and software development kit (SDK), all of which are available in the [`copilot-extensions`](https://github.com/copilot-extensions) organization:
  * [GitHub Models](https://github.com/copilot-extensions/github-models-extension): A more complex agent that lets you ask about and interact with various LLMs listed on the GitHub Marketplace through Copilot Chat. The GitHub Models agent makes use of function calling.
  * [Function Calling](https://github.com/copilot-extensions/function-calling-extension): An example agent written in Go that demonstrates function calling and confirmation dialogs.
  * [RAG Extension](https://github.com/copilot-extensions/rag-extension): An example agent written in Go that demonstrates a simple implementation of retrieval augmented generation.
  * [Preview SDK](https://github.com/copilot-extensions/preview-sdk.js/tree/main): An SDK that streamlines the development of Copilot Extensions by handling request verification, payload parsing, and response formatting automatically. This SDK allows extension builders to focus more on creating core functionality and less on boilerplate code.


