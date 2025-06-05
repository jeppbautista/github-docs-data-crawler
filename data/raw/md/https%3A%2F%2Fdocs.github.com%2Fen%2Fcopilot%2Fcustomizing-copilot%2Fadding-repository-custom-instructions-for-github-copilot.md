  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Customize Copilot](https://docs.github.com/en/copilot/customizing-copilot "Customize Copilot")/
  * [Repository custom instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot "Repository custom instructions")


# Adding repository custom instructions for GitHub Copilot
Create a file in a repository that gives Copilot additional context for the work it does in that repository.
## Tool navigation
  * [Visual Studio](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot?tool=visualstudio)
  * [Visual Studio Code](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot?tool=vscode)
  * [Web browser](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot?tool=webui)


## In this article
  * [About repository custom instructions for Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#about-repository-custom-instructions-for-copilot)
  * [About repository custom instructions and prompt files for GitHub Copilot Chat](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#about-repository-custom-instructions-and-prompt-files-for-github-copilot-chat)
  * [About repository custom instructions for GitHub Copilot Chat](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#about-repository-custom-instructions-for-github-copilot-chat)
  * [Prerequisites for repository custom instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#prerequisites-for-repository-custom-instructions)
  * [Creating a repository custom instructions file](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#creating-a-repository-custom-instructions-file)
  * [Writing effective repository custom instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#writing-effective-repository-custom-instructions)
  * [Repository custom instructions in use](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#repository-custom-instructions-in-use)
  * [Enabling or disabling repository custom instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#enabling-or-disabling-repository-custom-instructions)
  * [Enabling and using prompt files](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#enabling-and-using-prompt-files)


This feature is currently in public preview and is subject to change.
Repository custom instructions are currently supported for Copilot Chat in Visual Studio, VS Code and on the GitHub website. They are also supported for Copilot coding agent.
This version of this article is for using repository custom instructions on the GitHub website. Click the tabs above for information on using custom instructions in other environments. 
For an overview of the methods you can use to customize GitHub Copilot Chat responses, see [About customizing GitHub Copilot Chat responses](https://docs.github.com/en/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses?tool=webui). For information on customizing Copilot coding agent see [Customizing the development environment for Copilot coding agent](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent).
## [About repository custom instructions for Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#about-repository-custom-instructions-for-copilot)
GitHub Copilot can provide chat responses that are tailored to the way your team works, the tools you use, or the specifics of your project, if you provide it with enough context to do so. Instead of repeatedly adding this contextual detail to your chat questions, you can create a file in your repository that automatically adds this information for you. The additional information is not displayed in the chat, but is available to Copilot to allow it to generate higher quality responses.
The custom instructions file is also used by Copilot when you assign it to an issue or ask it to create a pull request. Instructions included in this file can help Copilot to work on files in a way that matches your team's working practices and conforms to coding standards for your project. See [About assigning tasks to Copilot](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/about-assigning-tasks-to-copilot).
### [Example](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#example)
This example of a `.github/copilot-instructions.md` file contains three instructions that will be added to all chat questions.
```
We use Bazel for managing our Java dependencies, not Maven, so when talking about Java packages, always give me instructions and code samples that use Bazel.

We always write JavaScript with double quotes and tabs for indentation, so when your responses include JavaScript code, please follow those conventions.

Our team uses Jira for tracking items of work.

```

Repository custom instructions are currently supported for Copilot Chat in Visual Studio, VS Code and on the GitHub website.
This version of this article is for using repository custom instructions in VS Code. Click the tabs above for instructions on using custom instructions in other environments. 
For an overview of the methods you can use to customize GitHub Copilot Chat responses, see [About customizing GitHub Copilot Chat responses](https://docs.github.com/en/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses?tool=vscode).
## [About repository custom instructions and prompt files for GitHub Copilot Chat](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#about-repository-custom-instructions-and-prompt-files-for-github-copilot-chat)
GitHub Copilot can provide chat responses that are tailored to the way your team works, the tools you use, or the specifics of your project, if you provide it with enough context to do so. Instead of repeatedly adding this contextual detail to your chat questions, you can create files in your repository that automatically add this information for you.
There are two types of files you can use to provide context and instructions to GitHub Copilot Chat in VS Code:
  * **Repository custom instructions** allow you to specify repository-wide instructions and preferences, in a single file, that apply to any conversation held in the context of the repository.
  * **Prompt files** (public preview) allow you to save common prompt instructions and relevant context in Markdown files (`*.prompt.md`) that you can then reuse in your chat prompts. Prompt files are only available in VS Code.


While custom instructions help to add codebase-wide context to each AI workflow, prompt files let you add instructions to a specific chat interaction.
### [Repository custom instructions example](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#repository-custom-instructions-example)
This example of a `.github/copilot-instructions.md` file contains three instructions that will be added to all chat questions.
```
We use Bazel for managing our Java dependencies, not Maven, so when talking about Java packages, always give me instructions and code samples that use Bazel.

We always write JavaScript with double quotes and tabs for indentation, so when your responses include JavaScript code, please follow those conventions.

Our team uses Jira for tracking items of work.

```

### [Prompt file examples](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#prompt-file-examples)
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



This feature is currently in public preview and is subject to change.
Repository custom instructions are currently supported for Copilot Chat in Visual Studio, VS Code and on the GitHub website.
This version of this article is for using repository custom instructions in Visual Studio. Click the tabs above for instructions on using custom instructions in other environments. 
For an overview of the methods you can use to customize GitHub Copilot Chat responses, see [About customizing GitHub Copilot Chat responses](https://docs.github.com/en/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses?tool=visualstudio).
## [About repository custom instructions for GitHub Copilot Chat](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#about-repository-custom-instructions-for-github-copilot-chat)
GitHub Copilot can provide chat responses that are tailored to the way your team works, the tools you use, or the specifics of your project, if you provide it with enough context to do so. Instead of repeatedly adding this contextual detail to your chat questions, you can create a file in your repository that automatically adds this information for you. The additional information is not displayed in the chat, but is available to Copilot to allow it to generate higher quality responses.
### [Example](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#example-1)
This example of a `.github/copilot-instructions.md` file contains three instructions that will be added to all chat questions.
```
We use Bazel for managing our Java dependencies, not Maven, so when talking about Java packages, always give me instructions and code samples that use Bazel.

We always write JavaScript with double quotes and tabs for indentation, so when your responses include JavaScript code, please follow those conventions.

Our team uses Jira for tracking items of work.

```

## [Prerequisites for repository custom instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#prerequisites-for-repository-custom-instructions)
  * A custom instructions file (see the instructions below).


  * Your personal choice of whether to use custom instructions must be set to enabled. This is enabled by default. See [Enabling or disabling repository custom instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#enabling-or-disabling-repository-custom-instructions) later in this article.
  * During the public preview, if you're using a Copilot Business plan, the organization that provides your plan must have the **Opt in to preview features** setting enabled. See [Managing policies for Copilot in your organization](https://docs.github.com/en/enterprise-cloud@latest/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization#enabling-copilot-features-in-your-organization).


  * The **Use Instruction Files** option must be enabled in your settings. This is enabled by default. See [Enabling or disabling repository custom instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#enabling-or-disabling-repository-custom-instructions) later in this article.


  * The **Enable custom instructions** option must be enabled in your settings. This is disabled by default. See [Enabling or disabling repository custom instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#enabling-or-disabling-repository-custom-instructions) later in this article.


## [Creating a repository custom instructions file](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#creating-a-repository-custom-instructions-file)
  1. In the root of your repository, create a file named `.github/copilot-instructions.md`.
Create the `.github` directory if it does not already exist.
  2. Add natural language instructions to the file, in Markdown format.
Whitespace between instructions is ignored, so the instructions can be written as a single paragraph, each on a new line, or separated by blank lines for legibility.


To see your instructions in action, go to <https://github.com/copilot>, attach the repository containing the instructions file, and start a conversation.
Did you successfully add a custom instructions file to your repository?
[Yes](https://docs.github.io/success-test/yes.html) [No](https://docs.github.io/success-test/no.html)
## [Writing effective repository custom instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#writing-effective-repository-custom-instructions)
The instructions you add to the `.github/copilot-instructions.md` file should be short, self-contained statements that add context or relevant information to supplement users' chat questions.
You should also consider the size and complexity of your repository. The following types of instructions may work for a small repository with only a few contributors, but for a large and diverse repository, they may cause problems with other areas of Copilot:
  * Requests to refer to external resources when formulating a response
  * Instructions to answer in a particular style
  * Requests to always respond with a certain level of detail


For example, the following instructions may not have the intended results:
```
Always conform to the coding styles defined in styleguide.md in repo my-org/my-repo when generating code.

Use @terminal when answering questions about Git.

Answer all questions in the style of a friendly colleague, using informal language.

Answer all questions in less than 1000 characters, and words of no more than 12 characters.

```

## [Repository custom instructions in use](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#repository-custom-instructions-in-use)
The instructions in the `.github/copilot-instructions.md` file are available for use by Copilot Chat as soon as you save the file. The complete set of instructions will be automatically added to chat prompts that relate to the repository containing the instructions file.
In Copilot Chat's immersive view ([github.com/copilot](https://github.com/copilot)), you can start a conversation that uses repository custom instructions by adding, as an attachment, the repository that contains the instructions file.
Whenever repository custom instructions are used by Copilot Chat, the instructions file is added as a reference for the response that's generated. To find out whether repository custom instructions were used, expand the list of references at the top of a chat response in the Chat panel and check whether the `.github/copilot-instructions.md` file is listed.
![Screenshot of an expanded References list, showing the 'copilot-instructions.md' file highlighted with a dark orange outline.](https://docs.github.com/assets/cb-42321/images/help/copilot/custom-instructions-ref-in-github.png)
You can click the reference to open the file.
  * It is possible for multiple types of custom instructions to apply to a conversation. Personal instructions take the highest priority, followed by repository instructions, with organization instructions prioritized last. However, all sets of relevant instructions are still combined and provided to Copilot Chat.
  * Whenever possible, you should avoid providing conflicting sets of instructions. If you are concerned about response quality, you can also choose to temporarily disable repository instructions. See [Adding repository custom instructions for GitHub Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot?tool=webui#enabling-or-disabling-repository-custom-instructions).


The instructions in the `.github/copilot-instructions.md` file are available for use by Copilot Chat as soon as you save the file. The complete set of instructions will be automatically attached to requests that you submit in either the Copilot Chat view, or in inline chat.
Custom instructions are not visible in the Chat view or inline chat, but you can verify that they are being used by Copilot by looking at the References list of a response in the Chat view. If custom instructions were added to the prompt that was sent to the model, the `.github/copilot-instructions.md` file is listed as a reference. You can click the reference to open the file.
![Screenshot of an expanded References list, showing the 'copilot-instructions.md' file highlighted with a dark orange outline.](https://docs.github.com/assets/cb-28337/images/help/copilot/custom-instructions-vscode.png)
The instructions in the `.github/copilot-instructions.md` file are available for use by Copilot Chat as soon as you save the file. The complete set of instructions will be automatically attached to requests that you submit in either the Copilot Chat view, or in inline chat.
Custom instructions are not visible in the Chat view or inline chat, but you can verify that they are being used by Copilot by looking at the References list of a response in the Chat view. If custom instructions were added to the prompt that was sent to the model, the `.github/copilot-instructions.md` file is listed as a reference. You can click the reference to open the file.
![Screenshot of the References popup, showing the 'copilot-instructions.md' file highlighted with a dark orange outline.](https://docs.github.com/assets/cb-24107/images/help/copilot/custom-instruction-ref-visual-studio.png)
## [Enabling or disabling repository custom instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#enabling-or-disabling-repository-custom-instructions)
You can choose whether or not to have custom instructions added to your chat questions.
  1. Click the 
  2. Click **Disable custom instructions** or **Enable custom instructions**.
In immersive mode, you will only see these options if you have attached a repository that contains a custom instructions file.


Your choice persists until you change it.
  1. Open the Setting editor by using the keyboard shortcut `Command`+`,` (Mac) / `Ctrl`+`,` (Linux/Windows).
  2. Type `instruction file` in the search box.
  3. Select or clear the checkbox under **Code Generation: Use Instruction Files**.


  1. In the Visual Studio menu bar, under **Tools** , click **Options**.
![Screenshot of the Visual Studio menu bar. The "Tools" menu is expanded, and the "Options" item is highlighted with an orange outline.](https://docs.github.com/assets/cb-37169/images/help/copilot/vs-toolbar-options.png)
  2. In the "Options" dialog, type `custom instructions` in the search box, then click **Copilot**.
  3. Select or clear the checkbox for **(Preview) Enable custom instructions to be loaded from .github/copilot-instructions.md files and added to requests**.


## [Enabling and using prompt files](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#enabling-and-using-prompt-files)
Prompt files are public preview and subject to change.
Prompt files let you build and share reusable prompt instructions with additional context. A prompt file is a Markdown file, stored in your workspace, that mimics the existing format of writing prompts in Copilot Chat (for example, `Rewrite #file:x.ts`). You can have multiple prompt files in your workspace, each of which defines a prompt for a different purpose.
### [Enabling prompt files](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#enabling-prompt-files)
To enable prompt files, configure the workspace settings.
  1. Open the command palette by pressing `Ctrl`+`Shift`+`P` (Windows/Linux) / `Command`+`Shift`+`P` (Mac).
  2. Type "Open Workspace Settings (JSON)" and select the option that's displayed.
  3. In the `settings.json` file, add `"chat.promptFiles": true` to enable the `.github/prompts` folder as the location for prompt files. This folder will be created if it does not already exist.


### [Creating prompt files](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#creating-prompt-files)
  1. Open the command palette by pressing `Ctrl`+`Shift`+`P` (Windows/Linux) / `Command`+`Shift`+`P` (Mac).
  2. Type "prompt" and select **Chat: Create Prompt**.
  3. Enter a name for the prompt file, excluding the `.prompt.md` file name extension. The name can contain alphanumeric characters and spaces and should describe the purpose of the prompt information the file will contain.
  4. Write the prompt instructions, using Markdown formatting.
You can reference other files in the workspace by using Markdown links—for example, `[index](../../web/index.ts)`—or by using the `#file:../../web/index.ts` syntax. Paths are relative to the prompt file. Referencing other files allows you to provide additional context, such as API specifications or product documentation.


### [Using prompt files](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#using-prompt-files)
  1. At the bottom of the Copilot Chat view, click the **Attach context** icon (
  2. In the dropdown menu, click **Prompt...** and choose the prompt file you want to use.
  3. Optionally, attach additional files, including prompt files, to provide more context.
  4. Optionally, type additional information in the chat prompt box.
Whether you need to do this or not depends on the contents of the prompt you are using.
  5. Submit the chat prompt.


For more information about prompt files, see [Custom instructions for GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/copilot-customization#_reusable-prompt-files-experimental) in the Visual Studio Code documentation.
