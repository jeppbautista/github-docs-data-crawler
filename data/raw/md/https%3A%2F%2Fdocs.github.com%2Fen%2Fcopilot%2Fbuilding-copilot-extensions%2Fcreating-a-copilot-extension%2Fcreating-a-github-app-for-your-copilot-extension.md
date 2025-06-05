  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Build Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions "Build Copilot Extensions")/
  * [Create a Copilot Extension](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension "Create a Copilot Extension")/
  * [Create GitHub App](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/creating-a-github-app-for-your-copilot-extension "Create GitHub App")


# Creating a GitHub App for your Copilot Extension
Learn how to create a GitHub App for your Copilot Extension.
## In this article
  * [Prerequisites](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/creating-a-github-app-for-your-copilot-extension#prerequisites)
  * [Creating a GitHub App](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/creating-a-github-app-for-your-copilot-extension#creating-a-github-app)
  * [Next steps](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/creating-a-github-app-for-your-copilot-extension#next-steps)


A Copilot Extension is a GitHub App that is associated with a Copilot agent. The GitHub App you associate your Copilot agent with is used to authenticate the Copilot agent with GitHub and to authorize the Copilot agent to access the Copilot Chat API. Each Copilot agent must be associated with a unique GitHub App.
## [Prerequisites](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/creating-a-github-app-for-your-copilot-extension#prerequisites)
  * You have created a Copilot agent. For more information, see [Building a Copilot agent for your Copilot Extension](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension).
  * You have configured your server to deploy your Copilot agent, and you have your hostname (aka forwarding endpoint). For more information, see [Configuring your server to host your Copilot extension](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/configuring-your-server-to-deploy-your-copilot-agent).


## [Creating a GitHub App](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/creating-a-github-app-for-your-copilot-extension#creating-a-github-app)
  1. In the upper-right corner of any page on GitHub, click your profile photo.
  2. Navigate to your account settings.
     * For an app owned by a personal account, click **Settings**.
     * For an app owned by an organization: 
       1. Click **Your organizations**.
       2. To the right of the organization, click **Settings**.
  3. In the left sidebar, click 
  4. In the left sidebar, click **GitHub Apps**.
  5. Click **New GitHub App**.
  6. Under "GitHub App name," enter a name for your app.
The name cannot be longer than 34 characters.
Your app's name will be shown in the user interface when your app takes an action. Uppercase letters will be converted to lowercase, with spaces replaced by `-`, and accents ignored. For example, `My APp Näme` would display as `my-app-name`.
The name must be unique across GitHub. You cannot use the same name as an existing GitHub account, unless it is your own user or organization name.
  7. Optionally, under "Description," type a description of your app. Users and organizations will see this description when they install your app.
  8. Under "Homepage URL," enter a URL for your app. You can use:
     * Your app's website URL.
     * The URL of the organization or user that owns the app.
     * The URL of the repository where your app's code is stored, if it is a public repository.
  9. Under "Webhook," deselect **Active**.
  10. Click **Create GitHub App**.


## [Next steps](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/creating-a-github-app-for-your-copilot-extension#next-steps)
  * [Configuring your GitHub App for your Copilot extension](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/configuring-your-github-app-for-your-copilot-agent)


