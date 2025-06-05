  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Use GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot "Use GitHub Copilot")/
  * [Coding agent](https://docs.github.com/en/copilot/using-github-copilot/coding-agent "Coding agent")/
  * [Create a PR from chat](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/asking-copilot-to-create-a-pull-request "Create a PR from chat")


# Asking Copilot to create a pull request
You can use a Copilot Chat prompt to ask Copilot to create a pull request.
## Who can use this feature?
Copilot coding agent is available with the GitHub Copilot Pro+ and GitHub Copilot Enterprise plans in repositories where it is enabled.  
[Sign up for Copilot ](https://github.com/features/copilot/plans?ref_cta=Copilot+plans+signup&ref_loc=asking+copilot+to+create+a+pull+request&ref_page=docs)
## In this article
  * [Introduction](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/asking-copilot-to-create-a-pull-request#introduction)
  * [Creating a pull request from Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/asking-copilot-to-create-a-pull-request#creating-a-pull-request-from-copilot-chat)
  * [Monitoring progress](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/asking-copilot-to-create-a-pull-request#monitoring-progress)
  * [Further reading](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/asking-copilot-to-create-a-pull-request#further-reading)


  * If you have access to Copilot coding agent, you can create a pull request from Copilot Chat in Visual Studio Code, Visual Studio, JetBrains IDEs, and on GitHub.com.
  * Copilot coding agent is in public preview and subject to change.


## [Introduction](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/asking-copilot-to-create-a-pull-request#introduction)
Often, when you are working on a project, you might notice a change you want to make, but the change doesn't directly relate to your current task. You might raise a GitHub issue to record that a change needs to be made—or perhaps, forget the change and move on.
Instead—if Copilot coding agent is available—you can ask Copilot to make the change for you. Copilot will start working on the change in the background and, when it's done, request you to review the pull request it raises.
For information on making Copilot coding agent available, see [Enabling Copilot coding agent](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/enabling-copilot-coding-agent).
## [Creating a pull request from Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/asking-copilot-to-create-a-pull-request#creating-a-pull-request-from-copilot-chat)
  1. Open GitHub Copilot Chat, in your IDE, or while viewing a file on GitHub.com.
  2. Type a prompt asking Copilot to create a pull request, and giving details of what you want Copilot to change.
For example, `@github Create a PR to put backticks around file names and variables in output.`
In VS Code, Visual Studio, and JetBrains IDEs, you must mention the `@github` chat participant in your prompt. You can omit this in Copilot Chat on GitHub.com.
To help Copilot, you can select the relevant line(s) of code before submitting your prompt.
  3. Submit your prompt.
Copilot will respond with a link to the pull request it creates. It will work on the task and push changes to the pull request, and then add you as a reviewer when it has finished, triggering a notification.


## [Monitoring progress](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/asking-copilot-to-create-a-pull-request#monitoring-progress)
You can see what Copilot is doing while it is working on a task by viewing the session logs. See [Using the Copilot coding agent logs](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/using-the-copilot-coding-agent-logs).
You can also stop Copilot from working on a task by clicking **Stop session** in the session logs.
## [Further reading](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/asking-copilot-to-create-a-pull-request#further-reading)
  * [About assigning tasks to Copilot](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/about-assigning-tasks-to-copilot)
  * [Best practices for using Copilot to work on tasks](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/best-practices-for-using-copilot-to-work-on-tasks)
  * [Troubleshooting Copilot coding agent](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/troubleshooting-copilot-coding-agent#copilot-cant-create-a-pull-request-from-copilot-chat)


