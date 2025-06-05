  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Build Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions "Build Copilot Extensions")/
  * [Set up Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions/setting-up-copilot-extensions "Set up Copilot Extensions")


# Setting up Copilot Extensions
Follow these steps to start building Copilot Extensions.
## Tool navigation
  * [Agents](https://docs.github.com/en/copilot/building-copilot-extensions/setting-up-copilot-extensions?tool=agents)
  * [Skillsets](https://docs.github.com/en/copilot/building-copilot-extensions/setting-up-copilot-extensions?tool=skillsets)


## In this article
  * [1. Learn about Copilot agents](https://docs.github.com/en/copilot/building-copilot-extensions/setting-up-copilot-extensions#1-learn-about-copilot-agents)
  * [2. Review example Copilot agents and the Copilot Extensions SDK](https://docs.github.com/en/copilot/building-copilot-extensions/setting-up-copilot-extensions#2-review-example-copilot-agents-and-the-copilot-extensions-sdk)
  * [3. Build a Copilot agent](https://docs.github.com/en/copilot/building-copilot-extensions/setting-up-copilot-extensions#3-build-a-copilot-agent)
  * [4. Deploy your Copilot agent](https://docs.github.com/en/copilot/building-copilot-extensions/setting-up-copilot-extensions#4-deploy-your-copilot-agent)
  * [5. Create a GitHub App and integrate it with your Copilot agent](https://docs.github.com/en/copilot/building-copilot-extensions/setting-up-copilot-extensions#5-create-a-github-app-and-integrate-it-with-your-copilot-agent)
  * [6. Choose the availability of your Copilot Extension](https://docs.github.com/en/copilot/building-copilot-extensions/setting-up-copilot-extensions#6-choose-the-availability-of-your-copilot-extension)
  * [Next steps](https://docs.github.com/en/copilot/building-copilot-extensions/setting-up-copilot-extensions#next-steps)
  * [1. Learn about Github Copilot skillsets](https://docs.github.com/en/copilot/building-copilot-extensions/setting-up-copilot-extensions#1-learn-about-github-copilot-skillsets)
  * [2. Build a Copilot skillset](https://docs.github.com/en/copilot/building-copilot-extensions/setting-up-copilot-extensions#2-build-a-copilot-skillset)
  * [3. Deploy your Copilot skillset](https://docs.github.com/en/copilot/building-copilot-extensions/setting-up-copilot-extensions#3-deploy-your-copilot-skillset)
  * [4. Create a GitHub App and integrate it with your Copilot skillset](https://docs.github.com/en/copilot/building-copilot-extensions/setting-up-copilot-extensions#4-create-a-github-app-and-integrate-it-with-your-copilot-skillset)
  * [5. Choose the availability of your Copilot skillset](https://docs.github.com/en/copilot/building-copilot-extensions/setting-up-copilot-extensions#5-choose-the-availability-of-your-copilot-skillset)
  * [Next steps](https://docs.github.com/en/copilot/building-copilot-extensions/setting-up-copilot-extensions#next-steps-1)


This article is designed to help you build an entirely new GitHub Copilot Extension. To instead learn how to quickly build and test a demo Copilot Extension created by GitHub, see [Quickstart for GitHub Copilot Extensions using agents](https://docs.github.com/en/copilot/building-copilot-extensions/quickstart-for-github-copilot-extensions).
Skillsets and agents are the two ways to extend Copilot's capabilities and context through the Copilot Extensibility Platform. They let you integrate external services and APIs into Copilot Chat, but each one serves different use cases and offers different levels of control and complexity:
  * **Skillsets** are lightweight and streamlined, designed for developers who need Copilot to perform specific tasks (e.g., data retrieval or simple operations) with minimal setup. They handle routing, prompt crafting, function evaluation, and response generation automatically, making them ideal for quick and straightforward integrations. For more information about skillsets, see [About Copilot skillsets](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-skillset-for-your-copilot-extension/about-copilot-skillsets).
  * **Agents** are for complex integrations that need full control over how requests are processed and responses are generated. They let you implement custom logic, integrate with other LLMs and/or the Copilot API, manage conversation context, and handle all aspects of the user interaction. While Agents require more engineering and maintenance, they offer maximum flexibility for sophisticated workflows. For more information about agents, see [About Copilot agents](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/about-copilot-agents).


## [1. Learn about Copilot agents](https://docs.github.com/en/copilot/building-copilot-extensions/setting-up-copilot-extensions#1-learn-about-copilot-agents)
Copilot agents contain the custom code for your Copilot Extension, and integrate with a GitHub App to form the Copilot Extension itself. For more information, see [About Copilot agents](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/about-copilot-agents).
To successfully build a Copilot agent, you need to understand how the agent communicates with:
  * The Copilot platform using server-sent events. See [Configuring your Copilot agent to communicate with the Copilot platform](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/configuring-your-copilot-agent-to-communicate-with-the-copilot-platform).
  * The GitHub API. See [Configuring your Copilot agent to communicate with GitHub](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/configuring-your-copilot-agent-to-communicate-with-github).


## [2. Review example Copilot agents and the Copilot Extensions SDK](https://docs.github.com/en/copilot/building-copilot-extensions/setting-up-copilot-extensions#2-review-example-copilot-agents-and-the-copilot-extensions-sdk)
To see the previous concepts in practice and learn about agent implementations, review the following example agents and software development kit (SDK), all of which are available in the [`copilot-extensions`](https://github.com/copilot-extensions) organization:
  * [Blackbeard](https://github.com/copilot-extensions/blackbeard-extension) (best starting point): A simple agent that responds to requests like a pirate using Copilot's large language model (LLM) API and special system prompts.
  * [GitHub Models](https://github.com/copilot-extensions/github-models-extension): A more complex agent that lets you ask about and interact with various LLMs listed on the GitHub Marketplace through Copilot Chat. The GitHub Models agent makes use of function calling.
  * [Function Calling](https://github.com/copilot-extensions/function-calling-extension): An example agent written in Go that demonstrates function calling and confirmation dialogs.
  * [RAG Extension](https://github.com/copilot-extensions/rag-extension): An example agent written in Go that demonstrates a simple implementation of retrieval augmented generation.
  * [Preview SDK](https://github.com/copilot-extensions/preview-sdk.js/tree/main): An SDK that streamlines the development of Copilot Extensions by handling request verification, payload parsing, and response formatting automatically. This SDK allows extension builders to focus more on creating core functionality and less on boilerplate code.


## [3. Build a Copilot agent](https://docs.github.com/en/copilot/building-copilot-extensions/setting-up-copilot-extensions#3-build-a-copilot-agent)
Using the reference material from the previous steps, plan and build your Copilot agent. You can choose to implement any of the following options:
  * To avoid building and managing your own LLM deployment, your agent can call the Copilot LLM deployment. See [Using Copilot's LLM for your agent](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/using-copilots-llm-for-your-agent).
  * To quickly interpret user input and choose from a variety of predefined functions to execute, you can implement function calling in your agent. To learn more, see [How to use function calling with Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/function-calling) in the Azure OpenAI documentation and [Function calling](https://platform.openai.com/docs/guides/function-calling) in the OpenAI documentation.


## [4. Deploy your Copilot agent](https://docs.github.com/en/copilot/building-copilot-extensions/setting-up-copilot-extensions#4-deploy-your-copilot-agent)
To make your Copilot agent accessible to the Copilot platform and GitHub, you need to deploy it to a server that is reachable by HTTP request. See [Configuring your server to host your Copilot extension](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/configuring-your-server-to-deploy-your-copilot-agent).
## [5. Create a GitHub App and integrate it with your Copilot agent](https://docs.github.com/en/copilot/building-copilot-extensions/setting-up-copilot-extensions#5-create-a-github-app-and-integrate-it-with-your-copilot-agent)
To create a Copilot Extension, you need to create and configure a GitHub App, then integrate it with your Copilot agent. See [Creating a GitHub App for your Copilot Extension](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/creating-a-github-app-for-your-copilot-extension) and [Configuring your GitHub App for your Copilot extension](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/configuring-your-github-app-for-your-copilot-agent).
## [6. Choose the availability of your Copilot Extension](https://docs.github.com/en/copilot/building-copilot-extensions/setting-up-copilot-extensions#6-choose-the-availability-of-your-copilot-extension)
Choose one of two visibility levels for your Copilot Extension:
  * **Public:** Any user or organization account with the installation page link for the extension can install it.
  * **Private:** Only the user or organization account that created the extension can install it.


If you make your Copilot Extension public, you can then choose to list it on the GitHub Marketplace.
To learn how to change the visibility of your Copilot Extension and list it on the GitHub Marketplace, see [Managing the availability of your Copilot Extension](https://docs.github.com/en/copilot/building-copilot-extensions/managing-the-availability-of-your-copilot-extension).
## [Next steps](https://docs.github.com/en/copilot/building-copilot-extensions/setting-up-copilot-extensions#next-steps)
To learn how to use your Copilot Extension, see [Using extensions to integrate external tools with Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/using-extensions-to-integrate-external-tools-with-copilot-chat).
## [1. Learn about Github Copilot skillsets](https://docs.github.com/en/copilot/building-copilot-extensions/setting-up-copilot-extensions#1-learn-about-github-copilot-skillsets)
Github Copilot skillsets contain the custom code for your Copilot Extension, and integrate with a GitHub App to form the Copilot Extension itself.
Unlike Copilot agents, Copilot skillsets handle the logic behind prompt crafting, function evaluation, and response generation, making them an ideal choice for developers seeking quick and effective integrations with minimal effort. For more information, see [About Copilot skillsets](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-skillset-for-your-copilot-extension/about-copilot-skillsets).
## [2. Build a Copilot skillset](https://docs.github.com/en/copilot/building-copilot-extensions/setting-up-copilot-extensions#2-build-a-copilot-skillset)
To explore an example of a skillset implementation, see the [skillset-example](https://github.com/copilot-extensions/skillset-example) repository in the [`copilot-extensions`](https://github.com/copilot-extensions) organization.
To build a skillset, see [Building Copilot skillsets](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-skillset-for-your-copilot-extension/building-copilot-skillsets).
## [3. Deploy your Copilot skillset](https://docs.github.com/en/copilot/building-copilot-extensions/setting-up-copilot-extensions#3-deploy-your-copilot-skillset)
To make your Copilot skillset accessible to the Copilot platform and GitHub, you need to deploy it to a server that is reachable by HTTP request. See [Configuring your server to host your Copilot extension](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/configuring-your-server-to-deploy-your-copilot-agent).
## [4. Create a GitHub App and integrate it with your Copilot skillset](https://docs.github.com/en/copilot/building-copilot-extensions/setting-up-copilot-extensions#4-create-a-github-app-and-integrate-it-with-your-copilot-skillset)
To create a Copilot Extension, you need to create and configure a GitHub App, then integrate it with your Copilot skillset. See [Creating a GitHub App for your Copilot Extension](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/creating-a-github-app-for-your-copilot-extension) and [Configuring your GitHub App for your Copilot extension](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/configuring-your-github-app-for-your-copilot-agent).
## [5. Choose the availability of your Copilot skillset](https://docs.github.com/en/copilot/building-copilot-extensions/setting-up-copilot-extensions#5-choose-the-availability-of-your-copilot-skillset)
Choose one of two visibility levels for your Copilot Extension:
  * **Public:** Any user or organization account with the installation page link for the extension can install it.
  * **Private:** Only the user or organization account that created the extension can install it.


If you make your Copilot Extension public, you can then choose to list it on the GitHub Marketplace.
To learn how to change the visibility of your Copilot Extension and list it on the GitHub Marketplace, see [Managing the availability of your Copilot Extension](https://docs.github.com/en/copilot/building-copilot-extensions/managing-the-availability-of-your-copilot-extension).
## [Next steps](https://docs.github.com/en/copilot/building-copilot-extensions/setting-up-copilot-extensions#next-steps-1)
To learn how to use your Copilot Extension, see [Using extensions to integrate external tools with Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/using-extensions-to-integrate-external-tools-with-copilot-chat).
