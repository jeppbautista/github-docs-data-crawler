  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Build Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions "Build Copilot Extensions")/
  * [Extensions Glossary](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-glossary "Extensions Glossary")


# Copilot Extensions Glossary
Understand the terminology used in Copilot Extensions.
The following terms are used in the context of Copilot Extensions, and are defined here for clarity.
#### [Agent](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-glossary#agent)
A type of Copilot Extension implementation that gives developers full control over handling user queries and response generation. This approach is ideal for builders who want complete customization and management of AI interactions.
#### [Context Passing](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-glossary#context-passing)
A capability in Copilot Extensions that enables user context from editors to be sent to agents, allowing for more tailored responses.
#### [Copilot Chat](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-glossary#copilot-chat)
The conversational interface within GitHub Copilot where users can interact with the AI assistant and extensions.
#### [Copilot Extension](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-glossary#copilot-extension)
A GitHub App with additional access to the Copilot Chat window and Copilot API, allowing for extended functionality in GitHub's Copilot Chat. This is how we will refer to extensions from the perspective of an extension user.
#### [Copilot Extensibility Platform](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-glossary#copilot-extensibility-platform)
The system that handles authentication and proxies requests between clients and agent plugins.
#### [Copilot-enabled Visual Studio Code extension](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-glossary#copilot-enabled-visual-studio-code-extension)
Also known as Visual Studio Code Chat extensions, Copilot-enabled Visual Studio Code extensions are built as a Visual Studio Code extension rather than a GitHub App. These extensions are exclusive to VS Code and can be downloaded from the VS Code Marketplace.
#### [GitHub App](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-glossary#github-app)
The foundation for a Copilot Extension that provides the necessary infrastructure, permissions, and context from GitHub, such as user, repo and organization metadata.
#### [GitHub Marketplace](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-glossary#github-marketplace)
The platform where GitHub approved GitHub Copilot Extensions can be listed publicly and discovered by users.
#### [Listed/Published Extension](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-glossary#listedpublished-extension)
An extension that appears on the GitHub Marketplace. These extensions must be reviewed and approved by GitHub.
#### [Private Extension](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-glossary#private-extension)
An extension that is only visible and usable by the enterprise, organization, or individual user that created it. Enterprise-created extensions can be installed by organizations that are within the enterprise.
#### [Public Extension](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-glossary#public-extension)
An extension that is visible and installable by any GitHub user or organization.
#### [Skill](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-glossary#skill)
A piece of code that retrieves context or executes an action in response to a user’s prompt (for example, "findIssueByID(id: number)"). For a list of a skills, see [Currently available skills](https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide#currently-available-skills).
#### [Skillset](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-glossary#skillset)
A type of Copilot Extension implementation that gives developers the ability to connect external services and custom API endpoints to Copilot with minimal complexity. The Copilot Extensibility Platform handles prompt crafting, function evaluation, and response generation. The builder only needs to handle API skill definitions. This approach is ideal for builders who want minimal complexity.
#### [Tool/Function Calling](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-glossary#toolfunction-calling)
A capability of Copilot's LLM (as well as Open AI’s) that allows them to invoke specific tools or functions. Extension builders can define available tools with parameters, enabling the LLM to select and call appropriate tools to fulfill a user’s request. “Functions” are a subset of “tools” and the “function calling” term will be closing down.
#### [Unlisted Extension](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-glossary#unlisted-extension)
An extension that is not published on the GitHub Marketplace. Builders may develop and distribute public unlisted extensions without requiring review or approval from GitHub. GitHub does not guarantee the security or quality of unlisted extensions.
#### [Verified Creator](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-glossary#verified-creator)
A status required for organizations to publish extensions on the GitHub Marketplace.
