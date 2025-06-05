  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Build Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions "Build Copilot Extensions")/
  * [Create a Copilot Extension](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension "Create a Copilot Extension")/
  * [Configure App for extension](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/configuring-your-github-app-for-your-copilot-extension "Configure App for extension")


# Configuring your GitHub App for your Copilot extension
Learn how to configure your GitHub App so that it is associated with your Copilot Extension.
## Tool navigation
  * [Agents](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/configuring-your-github-app-for-your-copilot-extension?tool=agents)
  * [Skillsets](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/configuring-your-github-app-for-your-copilot-extension?tool=skillsets)


## In this article
  * [Prerequisites](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/configuring-your-github-app-for-your-copilot-extension#prerequisites)
  * [Configuring your GitHub App](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/configuring-your-github-app-for-your-copilot-extension#configuring-your-github-app)


Once you have configured your server and created your GitHub App, you need to configure your GitHub App for use with your Copilot extension.
## [Prerequisites](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/configuring-your-github-app-for-your-copilot-extension#prerequisites)
  * You have configured your server to deploy your Copilot Extension, and you have your hostname (aka forwarding endpoint). For more information, see [Configuring your server to host your Copilot extension](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/configuring-your-server-to-deploy-your-copilot-agent).
  * You have created a GitHub App for your Copilot extension. For more information, see [Creating a GitHub App for your Copilot Extension](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/creating-a-github-app-for-your-copilot-extension).


## [Configuring your GitHub App](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/configuring-your-github-app-for-your-copilot-extension#configuring-your-github-app)
  1. In the upper-right corner of any page on GitHub, click your profile photo.
  2. Navigate to your account settings.
     * For an app owned by a personal account, click **Settings**.
     * For an app owned by an organization: 
       1. Click **Your organizations**.
       2. To the right of the organization, click **Settings**.
  3. In the left sidebar, click 
  4. In the left sidebar, click **GitHub Apps**.
  5. To the right of the GitHub App you want to configure for your Copilot Extension, click **Edit**.
  6. In the "Identifying and authorizing users" section, under "Callback URL", enter your callback endpoint URL, then click **Save changes**.
Your server's hostname is the forwarding endpoint that you copied from your terminal when you configured your server. See [Configuring your server to host your Copilot extension](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/configuring-your-server-to-deploy-your-copilot-agent).
If you are using an ephemeral domain in ngrok, you will need to update this URL every time you restart your ngrok server.
  7. In the left sidebar, click **Permissions & events**.
  8. To expand the "Account permissions" section, click anywhere in the section.
  9. In the "GitHub Copilot Chat" row, select the **Access:** dropdown menu, then click **Read-only**.
  10. To enable context passing, in the "Copilot Editor Context" row, select the **Access:** dropdown menu, then click **Read-only**. For more information about context passing, see [Context passing for your agent](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/context-passing-for-your-agent).
  11. Click **Save changes**.
  12. In the left sidebar, click **Copilot**.
  13. Read the GitHub Marketplace Developer Agreement and the GitHub Pre-release License Terms, then accept the terms for creating a Copilot Extension.
  14. In the "App type" section, select the dropdown menu, then click **Agent**.
  15. Under "URL," enter your server's hostname (aka forwarding endpoint) that you copied from your terminal.
If you are using an ephemeral domain in ngrok, you will need to update this URL every time you restart your ngrok server.
  16. Under "Inference description", type a brief description of your agent, then click **Save**. This will be the description users see when they hover over your extension's slug in the chat window.
  17. Your pre-authorization URL is a link on your website that starts the authorization process for your extension. Users will be redirected to this URL when they decide to authorize your extension. If you are using a pre-authorization URL, under "Pre-authorization URL," enter the URL, then click **Save**.
  18. In your GitHub App settings, in the left sidebar, click **Install App** , then, next to the account you want to install your app on, click **Install**.
  19. In the top right of any page on GitHub, click the 
The GitHub Copilot Chat panel is displayed. To resize the panel, click and drag the top or left edge.
  20. If the panel contains a previous conversation you had with Copilot, click the "New conversation" icon (a plus sign) at the top right of the panel.
![Screenshot of the new conversation button, highlighted with a dark orange outline.](https://docs.github.com/assets/cb-8475/images/help/copilot/chat-new-conversation-button.png)
  21. Invoke your extension by typing `@EXTENSION-NAME`, replacing any spaces in the extension name with `-`, then press `Enter`.
  22. If this is your first time using the extension, you will be prompted to authenticate. Follow the steps on screen to authenticate your extension.
  23. Ask your extension a question in the chat window. For example, `What is the software development lifecycle?`.


  1. In the upper-right corner of any page on GitHub, click your profile photo.
  2. Navigate to your account settings.
     * For an app owned by a personal account, click **Settings**.
     * For an app owned by an organization: 
       1. Click **Your organizations**.
       2. To the right of the organization, click **Settings**.
  3. In the left sidebar, click 
  4. In the left sidebar, click **GitHub Apps**.
  5. To the right of the GitHub App you want to configure for your Copilot Extension, click **Edit**.
  6. In the "Identifying and authorizing users" section, under "Callback URL", enter your callback endpoint URL, then click **Save changes**.
Your server's hostname is the forwarding endpoint that you copied from your terminal when you configured your server. See [Configuring your server to host your Copilot extension](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/configuring-your-server-to-deploy-your-copilot-agent).
If you are using an ephemeral domain in ngrok, you will need to update this URL every time you restart your ngrok server.
  7. In the left sidebar, click **Permissions & events**.
  8. To expand the "Account permissions" section, click anywhere in the section.
  9. In the "GitHub Copilot Chat" row, select the **Access:** dropdown menu, then click **Read-only**.
  10. To enable context passing, in the "Copilot Editor Context" row, select the **Access:** dropdown menu, then click **Read-only**. For more information about context passing, see [Context passing for your agent](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/context-passing-for-your-agent).
  11. Click **Save changes**.
  12. In the left sidebar, click **Copilot**.
  13. Read the GitHub Marketplace Developer Agreement and the GitHub Pre-release License Terms, then accept the terms for creating a Copilot Extension.
  14. In the "App type" section, select the dropdown menu, then click **Skillset**.
  15. Your pre-authorization URL is a link on your website that starts the authorization process for your extension. Users will be redirected to this URL when they decide to authorize your extension. If you are using a pre-authorization URL, under "Pre-authorization URL," enter the URL, then click **Save**.
  16. For each skill you want to add (maximum 5):
    1. Click **Add new skill**.
    2. Enter a clear **Name** for the skill (e.g., "Generate Lorem Ipsum Data").
    3. Write a detailed **Inference description** to help Copilot understand when to use this skill.
    4. Add your **API endpoint URL** that will receive the POST requests.
    5. In the **Parameter** field, add the JSON schema defining the expected request format.
    6. Click **Add Definition** to save your skill.
  17. Click **Save** to save your skillset.
  18. In your GitHub App settings, in the left sidebar, click **Install App** , then, next to the account you want to install your app on, click **Install**.
  19. In the top right of any page on GitHub, click the 
The GitHub Copilot Chat panel is displayed. To resize the panel, click and drag the top or left edge.
  20. If the panel contains a previous conversation you had with Copilot, click the "New conversation" icon (a plus sign) at the top right of the panel.
![Screenshot of the new conversation button, highlighted with a dark orange outline.](https://docs.github.com/assets/cb-8475/images/help/copilot/chat-new-conversation-button.png)
  21. Invoke your extension by typing `@EXTENSION-NAME`, replacing any spaces in the extension name with `-`, then press `Enter`.
  22. If this is your first time using the extension, you will be prompted to authenticate. Follow the steps on screen to authenticate your extension.
  23. Ask your extension a question in the chat window. For example, `What is the software development lifecycle?`.


