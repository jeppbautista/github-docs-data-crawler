  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Responsible use](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features "Responsible use")/
  * [Copilot coding agent](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom "Copilot coding agent")


# Responsible use of Copilot coding agent on GitHub.com
Learn how to use Copilot coding agent on GitHub.com responsibly by understanding its purposes, capabilities, and limitations.
## In this article
  * [About Copilot coding agent on GitHub.com](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom#about-copilot-coding-agent-on-githubcom)
  * [Use cases for Copilot coding agent](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom#use-cases-for-copilot-coding-agent)
  * [Improving performance for Copilot coding agent](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom#improving-performance-for-copilot-coding-agent)
  * [Security measures for Copilot coding agent](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom#security-measures-for-copilot-coding-agent)
  * [Limitations of Copilot coding agent](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom#limitations-of-copilot-coding-agent)


## [About Copilot coding agent on GitHub.com](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom#about-copilot-coding-agent-on-githubcom)
Copilot coding agent is an autonomous and asynchronous software development agent integrated into GitHub. The agent can pick up a task from an issue or from Copilot Chat, create a pull request, and then iterate on the pull request in response to comments.
Copilot coding agent can generate tailored changes based on your description and configurations, including tasks like bug fixes, implementing incremental new features, prototyping, documentation, and codebase maintenance. After the initial pull request is created, the agent can iterate with you, based on your feedback and reviews.
While working on your task, the agent has access to its own ephemeral development environment where it can make changes to your code, execute automated tests, and run linters.
The agent has been evaluated across a variety of programming languages, with English as the primary supported language.
The agent works by using a combination of natural language processing and machine learning to understand your task and make changes in a codebase to complete your task. This process can be broken down into a number of steps.
### [Prompt processing](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom#prompt-processing)
The task provided to Copilot through an issue, pull request comment or Copilot Chat message is combined with other relevant, contextual information to form a prompt. That prompt is sent to a large language model for processing. Inputs can take the form of plain natural language, code snippets, or images.
### [Language model analysis](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom#language-model-analysis)
The prompt is then passed through a large language model, which is a neural network that has been trained on a large body of data. The language model analyzes the input prompt to help the agent reason on the task and leverage necessary tools.
### [Response generation](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom#response-generation)
The language model generates a response based on its analysis of the prompt. This response can take the form of natural language suggestions and code suggestions.
### [Output formatting](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom#output-formatting)
Once the agent completes its first run, it will update the pull request description with the changes it made. The agent may include supplemental information about resources it could not access and provide suggestions on the steps to resolve.
You may provide feedback to the agent by commenting within the pull request or explicitly mentioning the agent (`@copilot`). The agent will then resubmit that feedback to the language model for further analysis. Once the agent completes changes based on feedback, the agent will respond to your comment with updated changes.
Copilot is intended to provide you with the most relevant solution for task resolution. However, it may not always provide the answer you are looking for. You are responsible for reviewing and validating responses generated by Copilot to ensure they are accurate and appropriate.
Additionally, as part of our product development process, GitHub undertakes red teaming (testing) to understand and improve the safety of the agent.
For information on how to improve performance, see [Improving performance for Copilot coding agent](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom#improving-performance-for-copilot-coding-agent) below.
## [Use cases for Copilot coding agent](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom#use-cases-for-copilot-coding-agent)
You can delegate a task to Copilot in a variety of scenarios, including, but not limited to:
  * **Codebase maintenance:** Tackling Security related fixes, dependency upgrades, and targeted refactoring.
  * **Documentation:** Updating and creating new documentation.
  * **Feature development:** Implementing incremental feature requests.
  * **Improving test coverage:** Developing additional test suites for quality management.
  * **Prototyping new projects:** Greenfielding new concepts.


## [Improving performance for Copilot coding agent](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom#improving-performance-for-copilot-coding-agent)
Copilot coding agent can support a wide range of tasks. To enhance the performance and address some of the limitations of the agent, there are various measures that you can adopt.
For more information about limitations, see [Limitations of Copilot coding agent](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom#limitations-of-copilot-coding-agent) (below).
### [Ensure your tasks are well-scoped](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom#ensure-your-tasks-are-well-scoped)
Copilot coding agent leverages your prompt as key context when generating a pull request. The more clear and well-scoped the prompt you assign to the agent, the better the results you will get. An ideal issue includes:
  * A clear description of the problem to be solved or the work required.
  * Complete acceptance criteria on what a good solution looks like (for example, should there be unit tests?).
  * Hints or pointers on what files need to be changed.


### [Customize your experience with additional context](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom#customize-your-experience-with-additional-context)
Copilot coding agent leverages your prompt, comments and the repository’s code as context when generating suggested changes. To enhance Copilot’s performance, consider implementing custom Copilot instructions to help the agent better understand your project and how to build, test and validate its changes. For more information, see the "Add custom instructions to your repository" in [Best practices for using Copilot to work on tasks](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/best-practices-for-using-copilot-to-work-on-tasks#adding-custom-instructions-to-your-repository).
For information about other customizations for Copilot coding agent, see:
  * [Customizing the development environment for Copilot coding agent](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent)
  * [Customizing or disabling the firewall for Copilot coding agent](https://docs.github.com/en/copilot/customizing-copilot/customizing-or-disabling-the-firewall-for-copilot-coding-agent)
  * [Extending Copilot coding agent with the Model Context Protocol (MCP)](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-coding-agent-with-mcp)


### [Use Copilot coding agent as a tool, not a replacement](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom#use-copilot-coding-agent-as-a-tool-not-a-replacement)
While Copilot coding agent can be a powerful tool for generating code and documentation, it is important to use it as a tool, rather than a replacement for human programming. You should always review and test the content generated by the agent to ensure that it meets your requirements and is free of errors or security concerns prior to merging.
### [Use secure coding and code review practices](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom#use-secure-coding-and-code-review-practices)
Although Copilot coding agent can generate syntactically correct code, it may not always be secure. You should always follow best practices for secure coding, such as avoiding hard-coded passwords or SQL injection vulnerabilities, as well as following code review best practices, to address the agent’s limitations. You should always take the same precautions as you would with any code you write that uses material you did not independently originate, including precautions to ensure its suitability. These include rigorous testing, IP scanning, and checking for security vulnerabilities.
### [Provide feedback](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom#provide-feedback)
If you encounter any issues or limitations with Copilot coding agent on GitHub.com, we recommend that you provide feedback by clicking the thumbs down icon below each agent response. This can help the developers to improve the tool and address any concerns or limitations. Additionally, you can provide feedback in the community discussion forum.
### [Stay up to date](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom#stay-up-to-date)
Copilot coding agent is a new technology and is likely to evolve over time. You should stay up to date with any new security risks or best practices that may emerge.
## [Security measures for Copilot coding agent](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom#security-measures-for-copilot-coding-agent)
By design, Copilot coding agent is built with several mitigations to help ensure your data and codebase is secure. Although mitigations exist, be sure to continue implementing security best practices while understanding the agent’s limitations and how they may impact your code.
### [Avoiding privileged escalation](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom#avoiding-privileged-escalation)
Copilot coding agent will only respond to interactions (for example, assigning the agent or commenting) from users with repository write access.
GitHub Actions workflows triggered in response to pull requests raised by Copilot coding agent require approval from a user with repository write access before they will run.
The agent filters hidden characters, that are not displayed on GitHub.com, which might otherwise allow users to hide harmful instructions in comments or issue body contents. This protects against risks like jailbreaks.
### [Constraining Copilot’s permissions](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom#constraining-copilots-permissions)
Copilot only has access to the repository where it is creating a pull request, and cannot access other repositories.
Its permissions are limited, allowing it to push code and read other resources. Built-in protections mean that Copilot can only push to branches with names beginning with `copilot/`. This means that Copilot cannot push to your default branch (for example, `main`).
Copilot coding agent does not have access to Actions organization or repository secrets or variables during runtime. Only secrets and variables specifically added to the `copilot` environment are passed to the agent.
### [Preventing data exfiltration](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom#preventing-data-exfiltration)
By default, Copilot coding agent has a firewall enabled to prevent exfiltration of code or other sensitive data, either accidentally or due to malicious user input.
For more information, see [Customizing or disabling the firewall for Copilot coding agent](https://docs.github.com/en/copilot/customizing-copilot/customizing-or-disabling-the-firewall-for-copilot-coding-agent).
## [Limitations of Copilot coding agent](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom#limitations-of-copilot-coding-agent)
Depending on factors such as your codebase and input data, you may experience different levels of performance when using Copilot coding agent. The following information is designed to help you understand system limitations and key concepts about performance as they apply to Copilot coding agent.
### [Limited scope](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom#limited-scope)
The language model used by Copilot coding agent has been trained on a large body of code but still has a limited scope and may not be able to handle certain code structures or obscure programming languages. For each language, the quality of suggestions you receive may depend on the volume and diversity of training data for that language.
### [Potential biases](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom#potential-biases)
The language model used by Copilot coding agent’s training data and context gathered by the large language model may contain biases and errors that can be perpetuated by the tool. Additionally, Copilot coding agent may be biased towards certain programming languages or coding styles, which can lead to suboptimal or incomplete suggestions.
### [Security risks](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom#security-risks)
Copilot coding agent generates code and natural language based on the context of an issue or comment within a repository, which can potentially expose sensitive information or vulnerabilities if not used carefully. You should be careful to review all outputs generated by the agent thoroughly prior to merging.
### [Inaccurate code](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom#inaccurate-code)
Allowing GitHub Copilot to make suggestions that match publicly available code is not supported for Copilot coding agent at this time. For more information, see [Finding public code that matches GitHub Copilot suggestions](https://docs.github.com/en/copilot/using-github-copilot/finding-public-code-that-matches-github-copilot-suggestions).
Copilot coding agent may generate code that appears to be valid but may not actually be semantically or syntactically correct or may not accurately reflect the intent of the developer.
To mitigate the risk of inaccurate code, you should carefully review and test the generated code, particularly when dealing with critical or sensitive applications. You should also ensure that the generated code adheres to best practices and design patterns and fits within the overall architecture and style of the codebase.
### [Legal and regulatory considerations](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom#legal-and-regulatory-considerations)
Users need to evaluate potential specific legal and regulatory obligations when using any AI services and solutions, which may not be appropriate for use in every industry or scenario. Additionally, AI services or solutions are not designed for and may not be used in ways prohibited in applicable terms of service and relevant codes of conduct.
