  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Use GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot "Use GitHub Copilot")/
  * [AI models](https://docs.github.com/en/copilot/using-github-copilot/ai-models "AI models")/
  * [Change the chat model](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat "Change the chat model")


# Changing the AI model for Copilot Chat
Learn how to change the default LLM for Copilot Chat to a different model.
## Tool navigation
  * [Eclipse](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat?tool=eclipse)
  * [JetBrains IDEs](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat?tool=jetbrains)
  * [Visual Studio](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat?tool=visualstudio)
  * [Visual Studio Code](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat?tool=vscode)
  * [Web browser](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat?tool=webui)
  * [Xcode](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat?tool=xcode)


## In this article
  * [AI models for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat#ai-models-for-copilot-chat)
  * [Changing your AI model](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat#changing-your-ai-model)
  * [AI models for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat#ai-models-for-copilot-chat-1)
  * [Changing your AI model](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat#changing-your-ai-model-1)
  * [AI models for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat#ai-models-for-copilot-chat-2)
  * [Changing the AI model for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat#changing-the-ai-model-for-copilot-chat)
  * [AI models for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat#ai-models-for-copilot-chat-3)
  * [Changing the AI model for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat#changing-the-ai-model-for-copilot-chat-1)
  * [AI models for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat#ai-models-for-copilot-chat-4)
  * [Changing the AI model for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat#changing-the-ai-model-for-copilot-chat-2)
  * [AI models for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat#ai-models-for-copilot-chat-5)
  * [Changing the AI model for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat#changing-the-ai-model-for-copilot-chat-3)
  * [Further reading](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat#further-reading)


By default, Copilot Chat uses a base model to provide fast, capable responses for a wide range of tasks, such as summarization, knowledge-based questions, reasoning, math, and coding.
However, you are not limited to using this model. You can choose from a selection of other models, each with its own particular strengths. You may have a favorite model that you like to use, or you might prefer to use a particular model for inquiring about a specific subject.
Different models have different premium request multipliers, which can affect how much of your monthly usage allowance is consumed. For details, see [About premium requests](https://docs.github.com/en/copilot/managing-copilot/monitoring-usage-and-entitlements/about-premium-requests).
Copilot allows you to change the model during a chat and have the alternative model used to generate responses to your prompts.
Changing the model that's used by Copilot Chat does not affect the model that's used for Copilot code completion. See [Changing the AI model for Copilot code completion](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-code-completion).
  * Multiple model support in Copilot Chat is in public preview and is subject to change.
  * Support for GPT-4.5 is only available on Copilot Pro+.
  * You can only use an alternative AI model in the immersive view of Copilot Chat. This is the full-page version of Copilot Chat that's displayed at <https://github.com/copilot>. The Copilot Chat panel always uses the default model.


## [AI models for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat#ai-models-for-copilot-chat)
The following models are currently available in the immersive mode of Copilot Chat:
  * GPT-4o
  * GPT-4.1
  * GPT-4.5 (preview)
  * Claude 3.5 Sonnet
  * Claude 3.7 Sonnet
  * Claude 3.7 Sonnet Thinking
  * Claude Sonnet 4
  * Claude Opus 4
  * Gemini 2.0 Flash
  * Gemini 2.5 Pro (preview)
  * o1
  * o3
  * o3-mini
  * o4-mini


For more information about these models, see [Choosing the right AI model for your task](https://docs.github.com/en/copilot/using-github-copilot/ai-models/choosing-the-right-ai-model-for-your-task).
### [Limitations of AI models for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat#limitations-of-ai-models-for-copilot-chat)
Experimental pre-release versions of the models may not interact with all filters correctly, including the duplication detection filter.
## [Changing your AI model](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat#changing-your-ai-model)
These instructions are for Copilot on the GitHub website. For instructions on different clients, click the appropriate tab at the top of this page.
If you access Copilot Chat through a Copilot Business subscription, your organization must grant members the ability to switch to a different model. See [Managing policies for Copilot in your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/setting-policies-for-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization).
If you use Copilot Extensions, they may override the model you select.
  1. In the top right of any page on GitHub, click **Immersive** in the dropdown menu.
![Screenshot of the 'Immersive' button, highlighted with a dark orange outline.](https://docs.github.com/assets/cb-21908/images/help/copilot/copilot-immersive-button.png)
  2. At the top of the immersive view, select the **CURRENT-MODEL**
  3. Optionally, after submitting a prompt, you can regenerate the same prompt using a different model by clicking the retry icon (


  * Multiple model support in Copilot Chat is in public preview and is subject to change.
  * Support for GPT-4.5 is only available on Copilot Pro+.


## [AI models for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat#ai-models-for-copilot-chat-1)
The following models are currently available through multi-model Copilot Chat:
  * GPT-4o
  * GPT-4.1
  * GPT-4.5 (preview)
  * Claude 3.5 Sonnet
  * Claude 3.7 Sonnet
  * Claude 3.7 Sonnet Thinking
  * Claude Sonnet 4
  * Claude Opus 4
  * Gemini 2.0 Flash
  * o1
  * o3
  * o3-mini
  * o4-mini


For more information about these models, see [Choosing the right AI model for your task](https://docs.github.com/en/copilot/using-github-copilot/ai-models/choosing-the-right-ai-model-for-your-task).
## [Changing your AI model](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat#changing-your-ai-model-1)
These instructions are for VS Code. For instructions on different clients, click the appropriate tab at the top of this page.
If you access Copilot Chat through a Copilot Business subscription, your organization must grant members the ability to switch to a different model. See [Managing policies for Copilot in your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/setting-policies-for-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization).
  * If you use Copilot Extensions, they may override the model you select.
  * Experimental pre-release versions of the models may not interact with all filters correctly, including the duplication detection filter.


  1. To open the chat view, click the chat icon in the activity bar or press `Control`+`Command`+`i` (Mac) / `Ctrl`+`Alt`+`i` (Windows/Linux).
  2. In the bottom right of the chat view, select the **CURRENT-MODEL**


Multiple model support in Copilot Chat is in public preview and is subject to change.
## [AI models for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat#ai-models-for-copilot-chat-2)
The following models are currently available through multi-model Copilot Chat:
  * GPT-4o
  * Claude 3.5 Sonnet
  * Claude 3.7 Sonnet
  * o1
  * o3-mini


For more information about these models, see [Choosing the right AI model for your task](https://docs.github.com/en/copilot/using-github-copilot/ai-models/choosing-the-right-ai-model-for-your-task).
## [Changing the AI model for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat#changing-the-ai-model-for-copilot-chat)
These instructions are for Visual Studio. For instructions on different clients, click the appropriate tab at the top of this page.
To use multi-model Copilot Chat, you must use Visual Studio 2022 version 17.12 or later. See the [Visual Studio downloads page](https://visualstudio.microsoft.com/downloads/).
If you access Copilot Chat through a Copilot Business subscription, your organization must grant members the ability to switch to a different model. See [Managing policies for Copilot in your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/setting-policies-for-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization).
  * If you use Copilot Extensions, they may override the model you select.
  * Experimental pre-release versions of the models may not interact with all filters correctly, including the duplication detection filter.


  1. In the Visual Studio menu bar, click **View** , then click **GitHub Copilot Chat**.
  2. In the bottom right of the chat view, select the **CURRENT-MODEL**


  * Multiple model support in Copilot Chat is in public preview and is subject to change.
  * Support for GPT-4.5 is only available on Copilot Pro+.


## [AI models for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat#ai-models-for-copilot-chat-3)
The following models are currently available through multi-model Copilot Chat:
  * GPT-4o
  * GPT-4.1
  * GPT-4.5 (preview)
  * Claude 3.5 Sonnet
  * Claude 3.7 Sonnet
  * Claude 3.7 Sonnet Thinking
  * Gemini 2.0 Flash
  * Gemini 2.5 Pro (preview)
  * o1 (preview)
  * o3 (preview)
  * o3-mini
  * o4-mini (preview)


For more information about these models, see [Choosing the right AI model for your task](https://docs.github.com/en/copilot/using-github-copilot/ai-models/choosing-the-right-ai-model-for-your-task).
## [Changing the AI model for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat#changing-the-ai-model-for-copilot-chat-1)
These instructions are for the JetBrains IDEs. For instructions on different clients, click the appropriate tab at the top of this page.
If you access Copilot Chat through a Copilot Business subscription, your organization must grant members the ability to switch to a different model. See [Managing policies for Copilot in your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/setting-policies-for-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization).
  * If you use Copilot Extensions, they may override the model you select.
  * Experimental pre-release versions of the models may not interact with all filters correctly, including the duplication detection filter.


  1. Click the 
  2. In the popup menu, click **Open GitHub Copilot Chat**.
  3. In the bottom right of the chat view, select an AI model of your choice from the 


  * Multiple model support in Copilot Chat is in public preview and is subject to change.
  * Support for GPT-4.5 is only available on Copilot Pro+.


## [AI models for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat#ai-models-for-copilot-chat-4)
The following models are currently available through multi-model Copilot Chat:
  * GPT-4o
  * GPT-4.5 (preview)
  * Claude 3.5 Sonnet
  * Claude 3.7 Sonnet
  * Claude 3.7 Sonnet Thinking
  * Gemini 2.0 Flash
  * o1 (preview)
  * o3-mini


For more information about these models, see [Choosing the right AI model for your task](https://docs.github.com/en/copilot/using-github-copilot/ai-models/choosing-the-right-ai-model-for-your-task).
## [Changing the AI model for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat#changing-the-ai-model-for-copilot-chat-2)
These instructions are for the Eclipse IDE. For instructions on different clients, click the appropriate tab at the top of this page.
If you access Copilot Chat through a Copilot Business subscription, your organization must grant members the ability to switch to a different model. See [Managing policies for Copilot in your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/setting-policies-for-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization).
  * If you use Copilot Extensions, they may override the model you select.
  * Experimental pre-release versions of the models may not interact with all filters correctly, including the duplication detection filter.


  1. Click the 
  2. In the popup menu, click **Open Chat**.
  3. In the bottom right of the chat panel, click the currently selected AI model, then select an alternative model from the popup menu.


  * Multiple model support in Copilot Chat is in public preview and is subject to change.
  * Support for GPT-4.5 is only available on Copilot Pro+.


## [AI models for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat#ai-models-for-copilot-chat-5)
The following models are currently available through multi-model Copilot Chat:
  * GPT-4o
  * GPT-4.1
  * GPT-4.5 (preview)
  * Claude 3.5 Sonnet
  * Claude 3.7 Sonnet
  * Claude 3.7 Sonnet Thinking
  * Gemini 2.0 Flash
  * Gemini 2.5 Pro (preview)
  * o1 (preview)
  * o3 (preview)
  * o3-mini
  * o4-mini (preview)


For more information about these models, see [Choosing the right AI model for your task](https://docs.github.com/en/copilot/using-github-copilot/ai-models/choosing-the-right-ai-model-for-your-task).
## [Changing the AI model for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat#changing-the-ai-model-for-copilot-chat-3)
These instructions are for Xcode. For instructions on different clients, click the appropriate tab at the top of this page.
To use multi-model Copilot Chat, you must install the GitHub Copilot for Xcode extension. See [Installing the GitHub Copilot extension in your environment](https://docs.github.com/en/copilot/configuring-github-copilot/installing-the-github-copilot-extension-in-your-environment).
If you access Copilot Chat through a Copilot Business subscription, your organization must grant members the ability to switch to a different model. See [Managing policies for Copilot in your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/setting-policies-for-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization).
  * If you use Copilot Extensions, they may override the model you select.
  * Experimental pre-release versions of the models may not interact with all filters correctly, including the duplication detection filter.


  1. To open the chat view, click **Editor** in the menu bar, then click **Open Chat**. Copilot Chat opens in a new window.
  2. In the bottom right of the chat view, select the **CURRENT-MODEL**


## [Further reading](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat#further-reading)
  * [Changing the AI model for Copilot code completion](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-code-completion)
  * [Using Claude in Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-claude-in-github-copilot)
  * [Using Gemini in Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-gemini-in-github-copilot)
  * [Choosing the right AI model for your task](https://docs.github.com/en/copilot/using-github-copilot/ai-models/choosing-the-right-ai-model-for-your-task)


