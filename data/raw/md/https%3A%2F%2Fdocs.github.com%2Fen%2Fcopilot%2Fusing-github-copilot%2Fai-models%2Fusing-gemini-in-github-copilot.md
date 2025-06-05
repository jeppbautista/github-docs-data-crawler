  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Use GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot "Use GitHub Copilot")/
  * [AI models](https://docs.github.com/en/copilot/using-github-copilot/ai-models "AI models")/
  * [Use Gemini](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-gemini-in-github-copilot "Use Gemini")


# Using Gemini in Copilot Chat
Learn how to enable Gemini in GitHub Copilot Chat, for yourself or your organization.
## In this article
  * [About Gemini in GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-gemini-in-github-copilot#about-gemini-in-github-copilot)
  * [Configuring access](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-gemini-in-github-copilot#configuring-access)
  * [Using Gemini](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-gemini-in-github-copilot#using-gemini)


## [About Gemini in GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-gemini-in-github-copilot#about-gemini-in-github-copilot)
Gemini models are large language models (LLMs) that you can use as an alternative to the default model used by Copilot Chat. Gemini models are responsive LLMs that can empower you to build apps faster and more easily, so you can focus on great experiences for your users. For information about the capabilities of Gemini, see the [Google for developers blog](https://developers.googleblog.com/en/gemini-2-5-flash-pro-live-api-veo-2-gemini-api/) and the [Google Cloud documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/models). For details of Google's data handling policy, see [Generative AI and data governance](https://cloud.google.com/vertex-ai/generative-ai/docs/data-governance#prediction) on the Google website.
Gemini is currently available in:
  * Copilot Chat in Visual Studio Code
  * Immersive mode in Copilot Chat in GitHub


GitHub Copilot uses Gemini 2.0 Flash and Gemini 2.5 Pro hosted on Google Cloud Platform (GCP). When using Gemini models, prompts and metadata are sent to GCP, which makes the [following data commitment](https://cloud.google.com/gemini/docs/discover/data-governance): _Gemini doesn't use your prompts, or its responses, as data to train its models._
When using Gemini models, input prompts and output completions continue to run through GitHub Copilot's content filters for public code matching, when applied, along with those for harmful, offensive, or off-topic content.
## [Configuring access](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-gemini-in-github-copilot#configuring-access)
You must enable access to Gemini 2.0 Flash and Gemini 2.5 Pro before you can use the model.
### [Setup for individual use](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-gemini-in-github-copilot#setup-for-individual-use)
Gemini 2.5 Pro is not currently available for Copilot Free.
If you have a Copilot Free, Copilot Pro, or Copilot Pro+ subscription, you can enable Gemini in two ways:
  * The first time you choose to use Gemini models with Copilot Chat in Visual Studio Code, or in the immersive view of Copilot Chat, you will be prompted to allow access to the model.
Clicking **Allow** enables you to use Gemini and updates the policy in your personal settings on GitHub.
  * You can enable the model directly in your personal settings on the GitHub website. See [Managing Copilot policies as an individual subscriber](https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/managing-copilot-policies-as-an-individual-subscriber#enabling-or-disabling-alternative-ai-models).


### [Setup for organization use](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-gemini-in-github-copilot#setup-for-organization--use)
As an organization owner, you can enable or disable both Gemini 2.0 Flash and Gemini 2.5 Pro for everyone who has been assigned a Copilot Business seat through your organization. See [Managing policies for Copilot in your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/setting-policies-for-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization).
## [Using Gemini](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-gemini-in-github-copilot#using-gemini)
For details of how to change the model that Copilot Chat uses, see [Changing the AI model for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat).
