  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Build Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions "Build Copilot Extensions")/
  * [About building Extensions](https://docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions "About building Extensions")


# About building Copilot Extensions
Learn about the development process for Copilot Extensions.
## Who can use this feature?
Anyone with a Copilot Pro, Copilot Pro+, or Copilot Free plan can use Copilot Extensions.
For organizations or enterprises with a Copilot Business or Copilot Enterprise plan, organization owners and enterprise administrators can grant access to Copilot Extensions.
Copilot Extensions is not available for GitHub Enterprise Server.
## In this article
  * [About Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions#about-copilot-extensions)
  * [About building GitHub Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions#about-building-github-copilot-extensions)
  * [Resources for building GitHub Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions#resources-for-building-github-copilot-extensions)
  * [About building Copilot-enabled Visual Studio Code extensions](https://docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions#about-building-copilot-enabled-visual-studio-code-extensions)
  * [Further reading](https://docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions#further-reading)


## [About Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions#about-copilot-extensions)
Copilot Extensions are integrations that expand the functionality of Copilot Chat, allowing developers to bring external tools, services, and custom behaviors into the Chat experience. You can use Copilot Extensions to extend the capabilities of Copilot Chat in a variety of ways, including:
  * **Querying documentation:** A Copilot Extension can allow Copilot Chat to query a third-party documentation service to find information about a specific topic.
  * **AI-assisted coding:** A Copilot Extension can use a third-party AI model to provide code suggestions.
  * **Data retrieval:** A Copilot Extension can allow Copilot Chat to query a third-party data service to retrieve information about a specific topic.
  * **Action execution:** A Copilot Extension can allow Copilot Chat to execute a specific action, such as posting to a message board or updating a tracking item in an external system.


## [About building GitHub Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions#about-building-github-copilot-extensions)
GitHub Copilot Extensions are a type of Copilot Extension built with GitHub Apps. GitHub Copilot Extensions are best suited for developers who want cross-platform compatibility and app management and support from GitHub.
### [Supported clients and IDEs](https://docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions#supported-clients-and-ides)
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
### [About visibility of GitHub Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions#about-visibility-of-github-copilot-extensions)
GitHub Copilot Extensions can be private, public and shareable, or public and listed on the GitHub Marketplace. Which visibility option you choose will depend on your use case and the audience you are targeting.
  * Private extensions are often preferred by large enterprises or companies that: 
    * Want more customization and controls over data access
    * Need to integrate with a large volume of internal documents and databases
    * Have strict security policies making it difficult to authorize permissions for third-parties
  * Public extensions are suitable for: 
    * Open-source projects
    * Collaborative development and use across organizations within an enterprise
    * Sharing your tool and getting feedback before publishing to the GitHub Marketplace
  * GitHub Marketplace extensions are ideal for third-parties that want to: 
    * Offer their service to a broader audience
    * Integrate their tool into the developer workflow on GitHub and the IDE
    * Leverage the GitHub ecosystem to raise awareness for their product


### [About GitHub Copilot Extensions permissions](https://docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions#about-github-copilot-extensions-permissions)
Permissions vary by extension, depending on the level of authorization that the extension requires in order to respond to your query. You can view the required permissions on the extension’s installation page, located after the billing information step and before the install and authorize step.
**For developers** : At a minimum, the **Copilot Chat** permissions must be set to "Read-only". Additional permissions may include executing write actions on other surfaces and authorizing read access to repository and organization level data in GitHub.
**For builders** : In addition to the above, you may also request local context from a user’s editor to further tailor responses. To do so, the **Copilot Editor Context** permissions must be set to "Read-only". Users will be notified to provide the required authorization.
For more information on GitHub App permissions, see [Choosing permissions for a GitHub App](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app)
#### [Granting permissions to access organization resources](https://docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions#granting-permissions-to-access-organization-resources)
Only organization admins can grant permissions for Copilot Extensions to access organization resources. To grant organization members access:
  * The organization admin must install the extension.
  * The organization admin must grant the extension permission to access specific repositories.
  * The organization admin must authorize access for all, or specific repositories.


### [About skillsets and agents](https://docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions#about-skillsets-and-agents)
Skillsets and agents are the two ways to extend Copilot's capabilities and context through the Copilot Extensibility Platform. They let you integrate external services and APIs into Copilot Chat, but each one serves different use cases and offers different levels of control and complexity:
  * **Skillsets** are lightweight and streamlined, designed for developers who need Copilot to perform specific tasks (e.g., data retrieval or simple operations) with minimal setup. They handle routing, prompt crafting, function evaluation, and response generation automatically, making them ideal for quick and straightforward integrations. For more information about skillsets, see [About Copilot skillsets](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-skillset-for-your-copilot-extension/about-copilot-skillsets).
  * **Agents** are for complex integrations that need full control over how requests are processed and responses are generated. They let you implement custom logic, integrate with other LLMs and/or the Copilot API, manage conversation context, and handle all aspects of the user interaction. While Agents require more engineering and maintenance, they offer maximum flexibility for sophisticated workflows. For more information about agents, see [About Copilot agents](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/about-copilot-agents).


### [About context passing](https://docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions#about-context-passing)
You can allow your Copilot Extension to receive context from the editor, such as the currently opened file, by enabling the **Read-only** access level for the "Copilot Editor Context" permission in your GitHub App settings. See step 10 of [Configuring your GitHub App](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/configuring-your-github-app-for-your-copilot-extension#configuring-your-github-app).
The GitHub Copilot Extensibility Platform automatically handles messaging when implicit and explicit context is unavailable or unauthorized. To enable context passing, you are required to request permissions from users. To enable context passing, you are required to:
  * Update your APIs to handle new reference types.
  * Request permissions from users. When requesting permissions, follow these best practices: 
    * Clearly communicate what context you need and what you need it for.
    * Implement appropriate error handling for unavailable context that your own application logic and API calls.
    * If context is unavailable, provide value where possible without this data.
    * Request only the minimum required permissions for your extension.


Context passing respects content exclusions, which refers to any files listed in your context exclusion settings, including files that begin with `.`.
For more information about context passing, see [Context passing for your agent](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/context-passing-for-your-agent).
### [Using APIs in GitHub Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions#using-apis-in-github-copilot-extensions)
Building GitHub Copilot Extensions requires using the GitHub API. Optionally, the Copilot API can be used for additional capabilities. For details on request and response formatting, see the [OpenAI API documentation](https://platform.openai.com/docs/api-reference/chat).
The Copilot API is available for Copilot Extension builders, but only GitHub Apps and VS Code Chat extensions can be used to access these endpoints.
## [Resources for building GitHub Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions#resources-for-building-github-copilot-extensions)
GitHub provides a comprehensive toolkit for extension builders, with code samples, a CLI debugging tool, quickstart SDKs, and a user feedback repository. For more information, see the [copilot-extensions](https://github.com/orgs/copilot-extensions/) organization on GitHub.
Before creating your own GitHub Copilot Extension from scratch, you may want to explore an existing Copilot agent, then integrate it with a GitHub App to see how it works. GitHub provides a few example Copilot agents that you can clone and use as the basis for your own GitHub Copilot Extension:
  * **Blackbeard:** A simple Copilot agent that responds to requests like a pirate, using Copilot's LLM API and special system prompts. It is a good starting point for learning how to build a GitHub Copilot Extension. For more information, see the [Blackbeard Copilot Extension](https://github.com/copilot-extensions/blackbeard-extension).
  * **GitHub Models:** A more complex Copilot agent that lets you ask about and interact with various LLMs listed on the GitHub Marketplace from within Copilot Chat. For more information, see the [GitHub Models Copilot Extension](https://github.com/copilot-extensions/github-models-extension).
GitHub Models are in public preview and subject to change. To request access, join the [waitlist](https://github.com/marketplace/models/waitlist).
  * **Function calling:** an example agent written in Go that demonstrates function calling and confirmation dialogues. For more information, see the [Function calling extension](https://github.com/copilot-extensions/function-calling-extension).
  * **RAG extension:** an example agent written in Go that demonstrates a simple implementation of retrieval augmented generation. For more information, see the [RAG extension](https://github.com/copilot-extensions/rag-extension).
  * **Preview SDK:** An SDK that simplifies the process of building GitHub Copilot Extensions by handling request verification, response formatting, and API interactions. It allows builders to focus on their extension's core functionality rather than boilerplate, by streamlining the integration of tools, APIs, and data sources into Copilot Chat. For more information, see the [Preview SDK](https://github.com/copilot-extensions/preview-sdk.js).


## [About building Copilot-enabled Visual Studio Code extensions](https://docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions#about-building-copilot-enabled-visual-studio-code-extensions)
The GitHub documentation focuses on building GitHub Copilot Extensions, not Copilot-enabled Visual Studio Code extensions.
You can build a Copilot Extension that is exclusive and native to Visual Studio Code, called a Copilot-enabled Visual Studio Code extensions. This option is best suited for developers who want to build extensions that use VS Code-specific APIs and functionality, or extend existing VS Code extensions.
Also known as VS Code Chat extensions, Copilot-enabled Visual Studio Code extensions function similarly to GitHub Copilot Extensions by extending the capabilities of Copilot Chat, with a few notable differences:
  * VS Code Chat extensions are only usable in VS Code.
  * VS Code Chat extensions have more access to VS Code's features and APIs, allowing more editor-specific interactions like accessing local workspace data, manipulating Visual Studio Code's interface, and read/write access to local files.
  * VS Code Chat extensions are published to the VS Code Marketplace, not the GitHub Marketplace.
  * VS Code Chat extensions are local to the user's machine, and cannot be controlled by an organization's policies.


For more information on Copilot-enabled Visual Studio Code extensions, see [Chat extensions](https://code.visualstudio.com/api/extension-guides/chat) in the Visual Studio Code documentation.
## [Further reading](https://docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions#further-reading)
  * [Copilot Extensions Glossary](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-glossary)


