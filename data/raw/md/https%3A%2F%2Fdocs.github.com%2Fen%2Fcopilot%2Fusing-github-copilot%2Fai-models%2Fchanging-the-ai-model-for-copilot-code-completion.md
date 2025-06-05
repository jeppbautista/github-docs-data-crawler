  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Use GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot "Use GitHub Copilot")/
  * [AI models](https://docs.github.com/en/copilot/using-github-copilot/ai-models "AI models")/
  * [Change the completion model](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-code-completion "Change the completion model")


# Changing the AI model for Copilot code completion
Learn how to change the default LLM for Copilot code completion to a different model.
## Tool navigation
  * [JetBrains IDEs](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-code-completion?tool=jetbrains)
  * [Visual Studio](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-code-completion?tool=visualstudio)
  * [Visual Studio Code](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-code-completion?tool=vscode)


## In this article
  * [Overview](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-code-completion#overview)
  * [Effects of switching the AI model](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-code-completion#effects-of-switching-the-ai-model)
  * [Enabling the model switcher](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-code-completion#enabling-the-model-switcher)
  * [Changing the AI model for code completion](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-code-completion#changing-the-ai-model-for-code-completion)
  * [Checking which model is being used](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-code-completion#checking-which-model-is-being-used)
  * [Changing the AI model for code completion](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-code-completion#changing-the-ai-model-for-code-completion-1)
  * [Changing the AI model for code completion](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-code-completion#changing-the-ai-model-for-code-completion-2)


## [Overview](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-code-completion#overview)
By default, Copilot code completion uses the GPT-4o Copilot, a fine-tuned GPT-4o mini based large language model (LLM). This model has been trained on a wide range of high quality public GitHub repositories, providing coverage of over 30 programming languages. Its knowledge base is more current than the default model and you may find that it generates completion suggestions more quickly.
View the list of programming languages and technologies included in the training data.
  * C
  * C#
  * C++
  * Clojure
  * CSS
  * Dart
  * Dockerfile
  * Elixir
  * Emacs Lisp
  * Go
  * Haskell
  * HTML
  * Java
  * JavaScript
  * Julia
  * Jupyter Notebook
  * Kotlin
  * Lua
  * MATLAB
  * Objective-C
  * Perl
  * PHP
  * PowerShell
  * Python
  * R
  * Ruby
  * Rust
  * Scala
  * Shell
  * Swift
  * TeX
  * TypeScript
  * Vue


The list of available models will change over time. When only one code completion model is available, the model picker will only show that model. Preview models and additional code completion models will appear in the picker when we release them.
You can switch AI models in the latest releases of VS Code with the latest version of the GitHub Copilot extension. 
You can switch AI models in Visual Studio 17.14 Preview 2 and later. 
You can switch AI models in the latest releases of JetBrains IDEs with the latest version of the GitHub Copilot extension. 
## [Effects of switching the AI model](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-code-completion#effects-of-switching-the-ai-model)
Changing the model that's used for Copilot code completion does not affect the model that's used by Copilot Chat. See [Changing the AI model for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat).
There are no changes to the data collection and usage policy if you change the AI model.
If you are on a Copilot Free subscription, all completions count against your completions quota regardless of the model used. See [Plans for GitHub Copilot](https://docs.github.com/en/copilot/about-github-copilot/subscription-plans-for-github-copilot#comparing-copilot-subscriptions).
The setting to enable or disable suggestions that match public code are applied irrespective of which model you choose. See [Finding public code that matches GitHub Copilot suggestions](https://docs.github.com/en/enterprise-cloud@latest/copilot/using-github-copilot/finding-public-code-that-matches-github-copilot-suggestions).
## [Enabling the model switcher](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-code-completion#enabling-the-model-switcher)
If you have a Copilot Free or Copilot Pro subscription, the model switcher for Copilot code completion is automatically enabled.
If you're using a Copilot Business plan, the organization that provides your plan must enable the **Editor preview features** setting. See [Managing policies for Copilot in your organization](https://docs.github.com/en/enterprise-cloud@latest/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization#enabling-copilot-features-in-your-organization).
## [Changing the AI model for code completion](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-code-completion#changing-the-ai-model-for-code-completion)
The following instructions are for VS Code. If you are using Visual Studio, or a JetBrains IDE, click the appropriate tab at the start of this article.
  1. Open the command palette by pressing `Ctrl`+`Shift`+`P` (Windows/Linux) / `Command`+`Shift`+`P` (Mac).
  2. Type `change completions model` and select the "GitHub Copilot: Change Completions Model" command.
  3. In the dropdown menu, select the model you want to use.


Alternatively, if Command Center is enabled, you can click **Configure Code Completions** in the dropdown menu. Then choose **Change Completions Model** in the dropdown menu and select the model you want to use.
## [Checking which model is being used](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-code-completion#checking-which-model-is-being-used)
  1. Open the Settings editor by pressing `Ctrl`+`,` (Linux/Windows) / `Command`+`,` (Mac).
  2. Type `copilot completion` and look for the "GitHub > Copilot: Selected Completion Model" section.
The field in this section displays the currently selected model. If the field is empty, the default model is being used.


## [Changing the AI model for code completion](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-code-completion#changing-the-ai-model-for-code-completion-1)
The following instructions are for Visual Studio. If you are using VS Code, or a JetBrains IDE, click the appropriate tab at the start of this article.
  1. Click the 
  2. Click **Settings** , then click **Options**.
  3. Under **Copilot Completions** , use the dropdown menu to select the model you want to use.


## [Changing the AI model for code completion](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-code-completion#changing-the-ai-model-for-code-completion-2)
The following instructions are for JetBrains IDEs. If you are using Visual Studio, or VS Code, click the appropriate tab at the start of this article.
  1. Click the 
  2. In the popup menu, click **Edit Model for Completion**.
  3. In the settings dialog box for "Languages & Frameworks > GitHub Copilot," click the dropdown menu for **Model for completions** and select the model you want to use.
  4. Click **OK**.


