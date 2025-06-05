  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Use GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot "Use GitHub Copilot")/
  * [AI models](https://docs.github.com/en/copilot/using-github-copilot/ai-models "AI models")/
  * [Use OpenAI o4-mini](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-openai-o4-mini-in-github-copilot "Use OpenAI o4-mini")


# Using OpenAI o4-mini in Copilot Chat
Learn how to enable OpenAI o4-mini in GitHub Copilot Chat, for yourself or your organization.
## In this article
  * [About OpenAI o4-mini in GitHub Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-openai-o4-mini-in-github-copilot#about-openai-o4-mini-in-github-copilot-chat)
  * [Configuring access](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-openai-o4-mini-in-github-copilot#configuring-access)
  * [Using o4-mini](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-openai-o4-mini-in-github-copilot#using-o4-mini)


## [About OpenAI o4-mini in GitHub Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-openai-o4-mini-in-github-copilot#about-openai-o4-mini-in-github-copilot-chat)
o4-mini in Copilot Chat is currently in public preview and subject to change.
OpenAI has a family of large language models that you can use as an alternative to the default model used by Copilot Chat. o4-mini is one of those models and excels at coding tasks across the entire software development lifecycle, from initial design to bug fixes, maintenance to optimizations. For information about the capabilities of o4-mini, see the [OpenAI documentation](https://platform.openai.com/docs/models).
o4-mini is currently available in:
  * Copilot Chat in Visual Studio Code
  * Immersive mode in Copilot Chat in GitHub


o4-mini is hosted by OpenAI and GitHub's Azure tenant when used in GitHub Copilot. OpenAI makes the [following data commitment](https://openai.com/enterprise-privacy/): _We [OpenAI] do not train our models on your business data by default_. GitHub maintains a [zero data retention agreement](https://platform.openai.com/docs/guides/your-data) with OpenAI.
When using o4-mini, input prompts and output completions continue to run through GitHub Copilot's content filters for public code matching, when applied, along with those for harmful, offensive, or off-topic content.
## [Configuring access](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-openai-o4-mini-in-github-copilot#configuring-access)
You must enable access to OpenAI o4-mini individually before you can use the model.
### [Setup for individual use](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-openai-o4-mini-in-github-copilot#setup-for-individual-use)
If you have a Copilot Pro or Copilot Pro+ subscription, you can enable OpenAI o4-mini in two ways:
  * The first time you choose to use o4-mini with Copilot Chat in Visual Studio Code, or in the immersive view of Copilot Chat, you will be prompted to allow access to the model.
Clicking **Allow** enables you to use o4-mini and updates the policy in your personal settings on GitHub.
  * You can enable the model directly in your personal settings on the GitHub website. See [Managing Copilot policies as an individual subscriber](https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/managing-copilot-policies-as-an-individual-subscriber#enabling-or-disabling-alternative-ai-models).


### [Setup for organization use](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-openai-o4-mini-in-github-copilot#setup-for-organization--use)
As an organization owner, you can enable or disable o4-mini for everyone who has been assigned a Copilot Business seat through your organization. See [Managing policies for Copilot in your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/setting-policies-for-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization).
## [Using o4-mini](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-openai-o4-mini-in-github-copilot#using-o4-mini)
For details of how to change the model that Copilot Chat uses, see [Changing the AI model for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat).
