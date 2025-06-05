  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Use GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot "Use GitHub Copilot")/
  * [AI models](https://docs.github.com/en/copilot/using-github-copilot/ai-models "AI models")/
  * [Use Claude](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-claude-in-github-copilot "Use Claude")


# Using Claude in Copilot Chat
Learn how to enable Claude in GitHub Copilot Chat for yourself or your organization.
## In this article
  * [About Claude in GitHub Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-claude-in-github-copilot#about-claude-in-github-copilot-chat)
  * [Configuring access](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-claude-in-github-copilot#configuring-access)
  * [Using Claude](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-claude-in-github-copilot#using-claude)
  * [Leaving feedback](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-claude-in-github-copilot#leaving-feedback)


## [About Claude in GitHub Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-claude-in-github-copilot#about-claude-in-github-copilot-chat)
Claude Opus 4 and Claude Sonnet 4 in Copilot Chat are currently in public preview and subject to change.
Claude is a family of large language models that you can use as an alternative to the default model used by Copilot Chat. Claude excels at coding tasks across the entire software development lifecycle, from initial design to bug fixes, maintenance to optimizations. Learn more about [Claude's capabilities](https://www.anthropic.com/claude).
  * Claude Opus 4 is available in:
    * Copilot Chat in Visual Studio Code
    * Immersive mode in Copilot Chat in GitHub
  * Claude Sonnet 4 is available in:
    * Copilot Chat in Visual Studio Code
    * Immersive mode in Copilot Chat in GitHub
  * Claude 3.5 Sonnet and Claude 3.7 Sonnet are available in:
    * Copilot Chat in Visual Studio Code
    * Copilot Chat in Visual Studio 2022 
      * **3.5** : Version 17.12 or later
      * **3.7** : Version 17.13 or later
    * Copilot Chat in Xcode
    * Copilot Chat in Eclipse
    * Copilot Chat in JetBrains
    * Immersive mode in Copilot Chat in GitHub


Claude Opus 4 and Claude Sonnet 4 are hosted by Anthropic PBC and Google Cloud Platform. Claude 3.7 Sonnet is hosted by Amazon Web Services, Anthropic PBC, and Google Cloud Platform. Claude 3.5 Sonnet is hosted exclusively by Amazon Web Services. GitHub has provider agreements in place to ensure data is not used for training. Additional details for each provider are included below:
  * Amazon Bedrock: Amazon makes the [following data commitments](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html): _Amazon Bedrock doesn't store or log your prompts and completions. Amazon Bedrock doesn't use your prompts and completions to train any AWS models and doesn't distribute them to third parties_.
  * Anthropic PBC: GitHub maintains a [zero data retention agreement](https://privacy.anthropic.com/en/articles/8956058-i-have-a-zero-retention-agreement-with-anthropic-what-products-does-it-apply-to) with Anthropic.
  * Google Cloud: [Google commits to not training on GitHub data as part of their service terms](https://cloud.google.com/vertex-ai/generative-ai/docs/data-governance). GitHub is additionally not subject to prompt logging for abuse monitoring.


In order to provide better service quality and reduce latency, GitHub uses [prompt caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching). You can read more about prompt caching on [Anthropic PBC](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching), [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html), and [Google Cloud](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/claude-prompt-caching).
When using Claude, input prompts and output completions continue to run through GitHub Copilot's content filters for public code matching, when applied, along with those for harmful, offensive, or off-topic content.
## [Configuring access](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-claude-in-github-copilot#configuring-access)
You must enable access to each Claude individually before you can use the model.
### [Setup for individual use](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-claude-in-github-copilot#setup-for-individual-use)
  * Claude Opus 4 is not currently available for Copilot Free and Copilot Pro.
  * Claude Sonnet 4 and Claude 3.7 Sonnet are not currently available for Copilot Free.
  * Claude 3.7 Sonnet is not currently available for Copilot Free.


If you have a Copilot Free or Copilot Pro subscription, you can enable Claude in two ways:
  * The first time you choose to use Claude models with Copilot Chat in Visual Studio Code, or in the immersive view of Copilot Chat, you will be prompted to allow access to the model.
Clicking **Allow** enables you to use Claude and updates the policy in your personal settings on GitHub.
  * You can enable the model directly in your personal settings on the GitHub website. See [Managing Copilot policies as an individual subscriber](https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/managing-copilot-policies-as-an-individual-subscriber#enabling-or-disabling-alternative-ai-models).


### [Setup for organization use](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-claude-in-github-copilot#setup-for-organization--use)
Claude Opus 4 is not currently available for Copilot Business.
As an organization owner, you can enable or disable Claude models for everyone who has been assigned a Copilot Business seat through your organization. See [Managing policies for Copilot in your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/setting-policies-for-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization).
## [Using Claude](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-claude-in-github-copilot#using-claude)
For details on how to change the model that Copilot Chat uses, see [Changing the AI model for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat).
## [Leaving feedback](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-claude-in-github-copilot#leaving-feedback)
To leave feedback about Claude in Copilot, or to ask a question, see the GitHub Community discussion [Claude 3.5 Sonnet is now available to all Copilot users in Public Preview](https://github.com/orgs/community/discussions/143337).
