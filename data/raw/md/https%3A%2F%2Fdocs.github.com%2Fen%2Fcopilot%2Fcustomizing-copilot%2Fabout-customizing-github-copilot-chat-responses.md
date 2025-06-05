  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Customize Copilot](https://docs.github.com/en/copilot/customizing-copilot "Customize Copilot")/
  * [About customizing Copilot responses](https://docs.github.com/en/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses "About customizing Copilot responses")


# About customizing GitHub Copilot Chat responses
Learn about customizing GitHub Copilot Chat responses to fit with your preferences and requirements.
## Tool navigation
  * [Visual Studio](https://docs.github.com/en/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses?tool=visualstudio)
  * [Visual Studio Code](https://docs.github.com/en/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses?tool=vscode)
  * [Web browser](https://docs.github.com/en/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses?tool=webui)


## In this article
  * [About customizing GitHub Copilot Chat responses](https://docs.github.com/en/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses#about-customizing-github-copilot-chat-responses)
  * [Using custom instructions](https://docs.github.com/en/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses#using-custom-instructions)
  * [About repository custom instructions](https://docs.github.com/en/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses#about-repository-custom-instructions)
  * [About prompt files](https://docs.github.com/en/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses#about-prompt-files)
  * [About repository custom instructions](https://docs.github.com/en/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses#about-repository-custom-instructions-1)
  * [Next steps](https://docs.github.com/en/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses#next-steps)


This version of this article is about custom instructions on the GitHub website. Click the tabs above for other environments. 
This version of this article is about custom instructions and prompt files in VS Code. Click the tabs above for other environments. 
This version of this article is about custom instructions in Visual Studio. Click the tabs above for other environments. 
## [About customizing GitHub Copilot Chat responses](https://docs.github.com/en/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses#about-customizing-github-copilot-chat-responses)
GitHub Copilot can provide chat responses that are tailored to your personal preferences, the way your team works, the tools you use, or the specifics of your project, if you provide it with enough context to do so. Instead of repeatedly adding this contextual detail to your chat questions, you can create custom instructions that automatically add this information for you. The additional information is not displayed in the chat, but is available to Copilot to allow it to generate higher quality responses.
### [Types of custom instructions](https://docs.github.com/en/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses#types-of-custom-instructions)
  * **Personal custom instructions** apply to all conversations you have with Copilot Chat across the GitHub website. They allow you to specify your individual preferences, such as preferred language or response style, ensuring that the responses are tailored to your personal needs.
  * **Repository custom instructions** apply to conversations within the context of a specific repository. They are useful for defining project-specific coding standards, frameworks, or tools. For example, you can specify that a repository uses TypeScript and a particular library, ensuring consistent responses for all contributors.
  * **Organization custom instructions (public preview)** apply to conversations within the context of an organization on the GitHub website. They are ideal for enforcing organization-wide preferences, such as a common language or security guidelines. Organization custom instructions can only be set by organization owners for organizations with a Copilot Enterprise subscription.


GitHub Copilot can provide chat responses that are tailored to the way your team works, the tools you use, or the specifics of your project, if you provide it with enough context to do so. Instead of repeatedly adding this contextual detail to your chat questions, you can create files in your repository that automatically add this information for you.
There are two types of files you can use to provide context and instructions to GitHub Copilot Chat in VS Code:
  * **Repository custom instructions** allow you to specify repository-wide instructions and preferences, in a single file, that apply to any conversation held in the context of the repository.
  * **Prompt files** (public preview) allow you to save common prompt instructions and relevant context in Markdown files (`*.prompt.md`) that you can then reuse in your chat prompts. Prompt files are only available in VS Code.


While custom instructions help to add codebase-wide context to each AI workflow, prompt files let you add instructions to a specific chat interaction.
GitHub Copilot can provide chat responses that are tailored to the way your team works, the tools you use, or the specifics of your project, if you provide it with enough context to do so. Instead of repeatedly adding this contextual detail to your chat questions, you can create a custom instructions file in your repository that automatically adds this information for you. The additional information is not displayed in the chat, but is available to Copilot to allow it to generate higher quality responses.
## [Using custom instructions](https://docs.github.com/en/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses#using-custom-instructions)
Custom instructions consist of natural language instructions and are most effective when they are short, self-contained statements. Consider the scope over which you want the instruction to apply when choosing whether to add an instruction on the personal, repository, or (if available) organization level.
  * It is possible for multiple types of custom instructions to apply to a conversation. Personal instructions take the highest priority, followed by repository instructions, with organization instructions prioritized last. However, all sets of relevant instructions are still combined and provided to Copilot Chat.
  * Whenever possible, you should avoid providing conflicting sets of instructions. If you are concerned about response quality, you can also choose to temporarily disable repository instructions. See [Adding repository custom instructions for GitHub Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot?tool=webui#enabling-or-disabling-repository-custom-instructions).


Here are some common use cases and examples for each type of custom instructions:
  * **Personal custom instructions:**
    * Preferred individual language: `Always respond in Portuguese.`
    * Individual response preferences: `Explain a single concept per line. Be clear and concise.`
  * **Repository custom instructions:**
    * Coding standards: `Use early returns whenever possible.`
    * Frameworks: `Use Vue with the PrimeVue library.` or `Use Typescript rather than Javascript.`
    * Code style preferences: `Use camel case for variable names.`
  * **Organization custom instructions:**
    * Describe how to answer certain questions: `For questions related to security, use the Security Docs Knowledge Base or advise people to consult with #security on Slack.`
    * Preferred language for a company which exclusively speaks a single language: `Always respond in Portuguese.`
    * Organization-wide preferences: `Do not generate code blocks in responses.`


## [About repository custom instructions](https://docs.github.com/en/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses#about-repository-custom-instructions)
Repository custom instructions consist of a single file, `.github/copilot-instructions.md`, that you create in a repository. The instructions you add to the file should be short, self-contained statements that add context or relevant information to supplement chat questions.
Common use cases include:
  * **Test generation.** Create instructions for test generation, such as specifying the use of a certain test framework.
  * **Code review.** Specify instructions for reviewing code, such as telling a reviewer to look for a specific error in the code.
  * **Commit message generation.** Write instructions for generating commit messages, such as format or the type of information to include.


### [Example](https://docs.github.com/en/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses#example)
This example of a `.github/copilot-instructions.md` file contains three instructions that will be added to all chat questions.
```
We use Bazel for managing our Java dependencies, not Maven, so when talking about Java packages, always give me instructions and code samples that use Bazel.

We always write JavaScript with double quotes and tabs for indentation, so when your responses include JavaScript code, please follow those conventions.

Our team uses Jira for tracking items of work.

```

## [About prompt files](https://docs.github.com/en/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses#about-prompt-files)
Prompt files are public preview and subject to change.
Prompt files let you build and share reusable prompt instructions with additional context. A prompt file is a Markdown file, stored in your workspace, that mimics the existing format of writing prompts in Copilot Chat (for example, `Rewrite #file:x.ts`). This allows blending natural language instructions, additional context, and even linking to other prompt files as dependencies.
Common use cases include:
  * **Code generation**. Create reusable prompts for components, tests, or migrations (for example, React forms, or API mocks).
  * **Domain expertise**. Share specialized knowledge through prompts, such as security practices, or compliance checks.
  * **Team collaboration**. Document patterns and guidelines with references to specs and documentation.
  * **Onboarding**. Create step-by-step guides for complex processes or project-specific patterns.


You can have multiple prompt files in your workspace, each of which defines a prompt for a different purpose.
### [Examples](https://docs.github.com/en/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses#examples)
The following examples demonstrate how to use prompt files.
  * `New React form.prompt.md` - contains instructions for a reusable task to generate a form using React.
```
Your goal is to generate a new React form component.

Ask for the form name and fields if not provided.

Requirements for the form:
- Use form design system components: [design-system/Form.md](../docs/design-system/Form.md)
- Use `react-hook-form` for form state management:
  - Always define TypeScript types for your form data
  - Prefer *uncontrolled* components using register
  - Use `defaultValues` to prevent unnecessary rerenders
- Use `yup` for validation:
  - Create reusable validation schemas in separate files
  - Use TypeScript types to ensure type safety
  - Customize UX-friendly validation rules

```

  * `API security review.prompt.md` - contains reusable information about security practices for REST APIs, which can be used to do security reviews of REST APIs.
```
Secure REST API review:
- Ensure all endpoints are protected by authentication and authorization
- Validate all user inputs and sanitize data
- Implement rate limiting and throttling
- Implement logging and monitoring for security events
…

```



## [About repository custom instructions](https://docs.github.com/en/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses#about-repository-custom-instructions-1)
Repository custom instructions consist of a single file, `.github/copilot-instructions.md`, that you create in a repository. The instructions you add to the file should be short, self-contained statements that add context or relevant information to supplement chat questions.
Common use cases include:
  * **Test generation.** Create instructions for test generation, such as specifying the use of a certain test framework.
  * **Code review.** Specify instructions for reviewing code, such as telling a reviewer to look for a specific error in the code.
  * **Commit message generation.** Write instructions for generating commit messages, such as format or the type of information to include.


### [Example](https://docs.github.com/en/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses#example-1)
This example of a `.github/copilot-instructions.md` file contains three instructions that will be added to all chat questions.
```
We use Bazel for managing our Java dependencies, not Maven, so when talking about Java packages, always give me instructions and code samples that use Bazel.

We always write JavaScript with double quotes and tabs for indentation, so when your responses include JavaScript code, please follow those conventions.

Our team uses Jira for tracking items of work.

```

## [Next steps](https://docs.github.com/en/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses#next-steps)
  * [Adding personal custom instructions for GitHub Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-personal-custom-instructions-for-github-copilot)
  * [Adding repository custom instructions for GitHub Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot)
  * [Adding organization custom instructions for GitHub Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-organization-custom-instructions-for-github-copilot) in the GitHub Enterprise Cloud documentation


  * [Adding repository custom instructions for GitHub Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot)


  * [Adding repository custom instructions for GitHub Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot)


