  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Use GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot "Use GitHub Copilot")/
  * [Use Copilot Extensions](https://docs.github.com/en/copilot/using-github-copilot/using-extensions-to-integrate-external-tools-with-copilot-chat "Use Copilot Extensions")


# Using extensions to integrate external tools with Copilot Chat
You can use Copilot Extensions to interact with external tools in GitHub Copilot Chat.
## Who can use this feature?
Anyone with a Copilot Pro, Copilot Pro+, or Copilot Free plan can use Copilot Extensions.
For organizations or enterprises with a Copilot Business or Copilot Enterprise plan, organization owners and enterprise administrators can grant access to Copilot Extensions.
Copilot Extensions is not available for GitHub Enterprise Server.
## In this article
  * [About GitHub Copilot Extensions](https://docs.github.com/en/copilot/using-github-copilot/using-extensions-to-integrate-external-tools-with-copilot-chat#about-github-copilot-extensions)
  * [Prerequisites](https://docs.github.com/en/copilot/using-github-copilot/using-extensions-to-integrate-external-tools-with-copilot-chat#prerequisites)
  * [Using GitHub Copilot Extensions](https://docs.github.com/en/copilot/using-github-copilot/using-extensions-to-integrate-external-tools-with-copilot-chat#using-github-copilot-extensions)
  * [Tips for using GitHub Copilot Extensions](https://docs.github.com/en/copilot/using-github-copilot/using-extensions-to-integrate-external-tools-with-copilot-chat#tips-for-using-github-copilot-extensions)
  * [Additional resources](https://docs.github.com/en/copilot/using-github-copilot/using-extensions-to-integrate-external-tools-with-copilot-chat#additional-resources)
  * [Further reading](https://docs.github.com/en/copilot/using-github-copilot/using-extensions-to-integrate-external-tools-with-copilot-chat#further-reading)


## [About GitHub Copilot Extensions](https://docs.github.com/en/copilot/using-github-copilot/using-extensions-to-integrate-external-tools-with-copilot-chat#about-github-copilot-extensions)
GitHub Copilot Extensions are **a type of GitHub App that integrates the power of external tools into GitHub Copilot Chat**. Copilot Extensions can be developed by anyone, for private or public use, and can be shared with others through the GitHub Marketplace.
GitHub Copilot Extensions are not the same as _the GitHub Copilot extension_ , which you install in your IDE to use default Copilot functionality like code completion and GitHub Copilot Chat. For more information on _the GitHub Copilot extension_ , see [Installing the GitHub Copilot extension in your environment](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/installing-the-github-copilot-extension-in-your-environment).
You can get started with Copilot Extensions in one of two ways:
  * Build your own Copilot Extension. See [About building Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions).
  * Install a Copilot Extension from GitHub Marketplace.


You can interact with your custom-built or installed extension in a Copilot Chat conversation, asking questions and performing actions that combine the capabilities of the external tool and GitHub. For example, if you install the Sentry extension for GitHub Copilot, you can use the extension to get information about Sentry issues, then create and assign related tracking issues on GitHub.
Copilot Extensions provide several benefits, including:
  * Interaction with external tools using natural language
  * Reduced context switching
  * Customization of your Copilot Chat experience for your developer flow


Copilot Extensions are included in all Copilot subscriptions.
### [Supported clients and IDEs](https://docs.github.com/en/copilot/using-github-copilot/using-extensions-to-integrate-external-tools-with-copilot-chat#supported-clients-and-ides)
Clients and IDEs | GitHub Copilot Extensions support  
---|---  
Visual Studio Code |   
Visual Studio |   
GitHub.com |   
GitHub Mobile |   
JetBrains IDEs |   
GitHub Codespaces |   
Vim/Neovim |   
Copilot in the CLI |   
Xcode |   
## [Prerequisites](https://docs.github.com/en/copilot/using-github-copilot/using-extensions-to-integrate-external-tools-with-copilot-chat#prerequisites)
**If you have a Copilot Pro subscription** , you need to install a Copilot Extension before you can use the extension in Copilot Chat. See [Extending the capabilities of GitHub Copilot in your personal account](https://docs.github.com/en/copilot/github-copilot-chat/github-copilot-extensions/installing-github-copilot-extensions-for-your-personal-account).
**If you have access to Copilot through a Copilot Business or Copilot Enterprise subscription:**
  1. An organization owner or enterprise owner needs to enable the Copilot Extensions policy for your organization or enterprise. See [Managing policies for Copilot in your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/setting-policies-for-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization#setting-a-policy-for-github-copilot-extensions-in-your-organization) and [Managing policies and features for Copilot in your enterprise](https://docs.github.com/en/enterprise-cloud@latest/copilot/managing-copilot/managing-copilot-for-your-enterprise/managing-policies-and-features-for-copilot-in-your-enterprise#configuring-policies-for-github-copilot) in the GitHub Enterprise Cloud documentation.
  2. An organization owner needs to install Copilot Extensions for your organization. See [Extending the capabilities of GitHub Copilot in your organization](https://docs.github.com/en/copilot/github-copilot-chat/github-copilot-extensions/installing-github-copilot-extensions-for-your-organization).


## [Using GitHub Copilot Extensions](https://docs.github.com/en/copilot/using-github-copilot/using-extensions-to-integrate-external-tools-with-copilot-chat#using-github-copilot-extensions)
  1. To start using a Copilot Extension, open a supported Copilot Chat interface. See [Supported clients and IDEs](https://docs.github.com/en/copilot/using-github-copilot/using-extensions-to-integrate-external-tools-with-copilot-chat#supported-clients-and-ides).
  2. To see a list of all Copilot Extensions available in your Copilot Chat conversation, in the Copilot Chat text box, type `@`.
If you are using Copilot Chat in an IDE, and you or your organization owner install a Copilot Extension while your IDE is open, you need to restart your IDE to begin using the Copilot Extension.
  3. In the list of available Copilot Extensions, click the one you want to use.
  4. To begin interacting with the Copilot Extension, in the Copilot Chat text box, ask the extension to answer a question or perform an action, then press `Enter`. For each new request, be sure to include `@EXTENSION-NAME` at the beginning of your sentence.
     * If you did not install the Copilot Extension yourself, and it is your first time using the Copilot Extension, you will be asked to authorize the extension. See [Authorizing GitHub Apps](https://docs.github.com/en/apps/using-github-apps/authorizing-github-apps).
     * If you ask a Copilot Extension to perform an action, you need to confirm the extension has your permission to act on your behalf before it will complete the task. After carefully reviewing the proposed action, in the confirmation dialog, click **Allow** or **Dismiss**.


## [Tips for using GitHub Copilot Extensions](https://docs.github.com/en/copilot/using-github-copilot/using-extensions-to-integrate-external-tools-with-copilot-chat#tips-for-using-github-copilot-extensions)
  * When you are using a Copilot Extension, consider how you would interact with the tool outside of Copilot Chat, then use natural language to ask questions and assign tasks that integrate the capabilities of the tool with GitHub. For example, [Sentry](https://sentry.io/welcome/) is an application monitoring software with a Copilot Extension. The following are some example prompts for the Sentry extension for GitHub Copilot:
    * `@sentry list my most recent issues`
    * `@sentry tell me more about issue ISSUE-ID-OR-ISSUE-LINK`
    * `@sentry create a GitHub issue for the most recent Sentry issue and assign it to @DEVELOPER`
For information on the best ways to use a specific Copilot Extension, read the description of the extension on [GitHub Marketplace](https://github.com/marketplace?type=apps&copilot_app=true).
  * Interactions with one Copilot Extension will never be shared with another Copilot Extension. To interact with different Copilot Extensions in an IDE, change the `@EXTENSION-NAME` at the beginning of each sentence. Interactions with different extensions will appear in the same Copilot Chat window, but the conversations themselves are automatically separated.


## [Additional resources](https://docs.github.com/en/copilot/using-github-copilot/using-extensions-to-integrate-external-tools-with-copilot-chat#additional-resources)
For questions and issues related to GitHub Copilot Extensions, please use the following resources:
  * **General issues for users and builders:** Visit the [GitHub Support Portal](https://support.github.com/).
  * **Requests or feedback for GitHub:** Use the [GitHub Community Discussion Thread](https://gh.io/community-feedback).
  * **Requests or feedback for third-party extension publishers:** File an issue in the [User Feedback Repo](https://github.com/copilot-extensions/user-feedback) and add a label with the extension's slug name.
  * **GitHub Technology Partners:** Email the partnerships team directly for assistance.
  * **Copilot-enabled Visual Studio Code extensions:** For more information on this type of Copilot Extension, see [Chat extensions](https://code.visualstudio.com/api/extension-guides/chat) in the Visual Studio Code documentation.


GitHub Support is not able to answer questions regarding Copilot-enabled Visual Studio Code extensions, as this implementation path is owned and maintained by the VS Code team.
## [Further reading](https://docs.github.com/en/copilot/using-github-copilot/using-extensions-to-integrate-external-tools-with-copilot-chat#further-reading)
  * [About building Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions)


