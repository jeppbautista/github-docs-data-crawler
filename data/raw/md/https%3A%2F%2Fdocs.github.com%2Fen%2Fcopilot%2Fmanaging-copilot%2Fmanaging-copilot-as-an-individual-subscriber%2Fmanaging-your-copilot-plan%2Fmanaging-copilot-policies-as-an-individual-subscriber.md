  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Manage Copilot](https://docs.github.com/en/copilot/managing-copilot "Manage Copilot")/
  * [Manage for individual](https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber "Manage for individual")/
  * [Manage your Copilot plan](https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/managing-your-copilot-plan "Manage your Copilot plan")/
  * [Manage policies](https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/managing-your-copilot-plan/managing-copilot-policies-as-an-individual-subscriber "Manage policies")


# Managing Copilot policies as an individual subscriber
Find out how to change your personal settings on GitHub to configure GitHub Copilot's behavior.
## Who can use this feature?
Copilot Pro, Copilot Pro+, and Copilot Free
## In this article
  * [About GitHub Copilot settings on GitHub](https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/managing-your-copilot-plan/managing-copilot-policies-as-an-individual-subscriber#about-github-copilot-settings-on-github)
  * [Enabling or disabling suggestions matching public code](https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/managing-your-copilot-plan/managing-copilot-policies-as-an-individual-subscriber#enabling-or-disabling-suggestions-matching-public-code)
  * [Enabling or disabling Copilot coding agent](https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/managing-your-copilot-plan/managing-copilot-policies-as-an-individual-subscriber#enabling-or-disabling-copilot-coding-agent)
  * [Enabling or disabling prompt and suggestion collection](https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/managing-your-copilot-plan/managing-copilot-policies-as-an-individual-subscriber#enabling-or-disabling-prompt-and-suggestion-collection)
  * [Enabling or disabling alternative AI models](https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/managing-your-copilot-plan/managing-copilot-policies-as-an-individual-subscriber#enabling-or-disabling-alternative-ai-models)
  * [Enabling or disabling web search for GitHub Copilot Chat](https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/managing-your-copilot-plan/managing-copilot-policies-as-an-individual-subscriber#enabling-or-disabling-web-search-for-github-copilot-chat)
  * [Model training and improvements](https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/managing-your-copilot-plan/managing-copilot-policies-as-an-individual-subscriber#model-training-and-improvements)


## [About GitHub Copilot settings on GitHub](https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/managing-your-copilot-plan/managing-copilot-policies-as-an-individual-subscriber#about-github-copilot-settings-on-github)
In addition to the configuration for the GitHub Copilot plugin in your supported IDE, you can configure settings for GitHub Copilot on GitHub. The settings apply wherever you use GitHub Copilot.
## [Enabling or disabling suggestions matching public code](https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/managing-your-copilot-plan/managing-copilot-policies-as-an-individual-subscriber#enabling-or-disabling-suggestions-matching-public-code)
If you are a member of an organization on GitHub Enterprise Cloud who has been assigned a GitHub Copilot seat through your organization, you will not be able to configure suggestions matching public code in your personal account settings. Your setting for suggestions matching public code will be inherited from your organization or enterprise.
Your personal settings for GitHub Copilot include an option to either allow or block code suggestions that match publicly available code. If you choose to block suggestions matching public code, GitHub Copilot checks code suggestions with their surrounding code of about 150 characters against public code on GitHub. If there is a match, or a near match, the suggestion is not shown to you.
If you choose to allow suggestions matching public code, when Copilot suggests matching code you can display details of the matches and click through to the relevant repositories on GitHub. For more information, see [Finding public code that matches GitHub Copilot suggestions](https://docs.github.com/en/copilot/using-github-copilot/finding-public-code-that-matches-github-copilot-suggestions).
  1. In the upper-right corner of any page on GitHub, click your profile photo, then click 
  2. To the right of **Suggestions matching public code** , select the dropdown menu, then click **Allow** to allow suggestions matching public code, or **Block** to block suggestions matching public code.


## [Enabling or disabling Copilot coding agent](https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/managing-your-copilot-plan/managing-copilot-policies-as-an-individual-subscriber#enabling-or-disabling-copilot-coding-agent)
Copilot coding agent allows you to assign Copilot to GitHub issues, or ask Copilot to raise a pull request from a prompt in Copilot Chat.
  * Copilot coding agent is available with the GitHub Copilot Pro+ and GitHub Copilot Enterprise plans in repositories where it is enabled.
  * Copilot coding agent is in public preview and subject to change.


To use Copilot coding agent in repositories owned by your own personal account, you must enable it for those repositories in your account settings.
  1. In the upper-right corner of any page on GitHub, click your profile photo, then click 
  2. In the sidebar, under **Coding agent**.
  3. On the Copilot coding agent page, under "Policies," click the dropdown button for "Repository access," then choose either **No repositories** , **All repositories** , or **Only selected repositories**.
  4. If you choose **Only selected repositories** , click **Select repositories** and choose the repositories where you want to enable Copilot coding agent.


For organizations, the ability to use Copilot coding agent is controlled by policy settings for the organization. See [Adding Copilot coding agent to your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/adding-copilot-coding-agent-to-organization).
If the organization is owned by an enterprise, enablement may be controlled at the enterprise level. See [Making Copilot coding agent available to enterprise members](https://docs.github.com/en/enterprise-cloud@latest/copilot/managing-copilot/managing-copilot-for-your-enterprise/adding-copilot-coding-agent-to-enterprise).
## [Enabling or disabling prompt and suggestion collection](https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/managing-your-copilot-plan/managing-copilot-policies-as-an-individual-subscriber#enabling-or-disabling-prompt-and-suggestion-collection)
You can choose whether your prompts and Copilot's suggestions are collected and retained by GitHub, and further processed and shared with Microsoft. For more information about data that GitHub Copilot may collect depending on your settings, see [GitHub Terms for Additional Products and Features](https://docs.github.com/en/site-policy/github-terms/github-terms-for-additional-products-and-features#github-copilot) and the [GitHub Copilot privacy FAQ](https://github.com/features/copilot/#faq).
  1. In the upper-right corner of any page on GitHub, click your profile photo, then click 
  2. To allow or prevent GitHub using your data, select or deselect **Allow GitHub to use my code snippets from the code editor for product improvements**.


## [Enabling or disabling alternative AI models](https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/managing-your-copilot-plan/managing-copilot-policies-as-an-individual-subscriber#enabling-or-disabling-alternative-ai-models)
You can choose whether to allow the following AI models to be used as an alternative to Copilot's default model.
  * Claude - see [Using Claude in Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-claude-in-github-copilot)
  * Gemini - see [Using Gemini in Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-gemini-in-github-copilot)


  1. In the upper-right corner of any page on GitHub, click your profile photo, then click 
  2. To the right of the model name, select the dropdown menu, then click **Enabled** or **Disabled**.


## [Enabling or disabling web search for GitHub Copilot Chat](https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/managing-your-copilot-plan/managing-copilot-policies-as-an-individual-subscriber#enabling-or-disabling-web-search-for-github-copilot-chat)
You can enable web search for GitHub Copilot Chat. This setting is disabled by default. If you enable this setting, Copilot Chat will use Bing to search the internet for information related to a question. Bing search is particularly helpful when discussing new technologies or highly specific subjects.
  1. In the upper-right corner of any page on GitHub, click your profile photo, then click 
  2. To the right of **Copilot access to Bing** , select the dropdown menu, and then click **Enabled** or **Disabled**.


## [Model training and improvements](https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/managing-your-copilot-plan/managing-copilot-policies-as-an-individual-subscriber#model-training-and-improvements)
By default, GitHub, its affiliates, and third parties will **not** use your data, including prompts, suggestions, and code snippets, for AI model training. This is reflected in your personal settings for GitHub Copilot and cannot be enabled.
