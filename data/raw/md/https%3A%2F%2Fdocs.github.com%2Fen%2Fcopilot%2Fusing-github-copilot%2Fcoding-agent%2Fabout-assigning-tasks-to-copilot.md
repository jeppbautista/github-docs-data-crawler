  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Use GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot "Use GitHub Copilot")/
  * [Coding agent](https://docs.github.com/en/copilot/using-github-copilot/coding-agent "Coding agent")/
  * [About assigning tasks to Copilot](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/about-assigning-tasks-to-copilot "About assigning tasks to Copilot")


# About assigning tasks to Copilot
You can assign GitHub issues to Copilot, or ask Copilot to create a pull request.
## Who can use this feature?
Copilot coding agent is available with the GitHub Copilot Pro+ and GitHub Copilot Enterprise plans in repositories where it is enabled.  
[Sign up for Copilot ](https://github.com/features/copilot/plans?ref_cta=Copilot+plans+signup&ref_loc=about+assigning+issues+to+copilot&ref_page=docs)
## In this article
  * [Overview of Copilot coding agent](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/about-assigning-tasks-to-copilot#overview-of-copilot-coding-agent)
  * [Copilot coding agent usage costs](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/about-assigning-tasks-to-copilot#copilot-coding-agent-usage-costs)
  * [Risks and mitigations](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/about-assigning-tasks-to-copilot#risks-and-mitigations)
  * [Limitations of Copilot coding agent](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/about-assigning-tasks-to-copilot#limitations-of-copilot-coding-agent)
  * [Further reading](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/about-assigning-tasks-to-copilot#further-reading)


Copilot coding agent is in public preview and subject to change.
## [Overview of Copilot coding agent](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/about-assigning-tasks-to-copilot#overview-of-copilot-coding-agent)
With Copilot coding agent, GitHub Copilot can work independently in the background to complete tasks, just like a human developer.
Copilot can:
  * Fix bugs
  * Implement incremental new features
  * Improve test coverage
  * Update documentation
  * Address technical debt


To delegate development tasks to Copilot, you can:
  * Assign an issue to Copilot
  * Use GitHub Copilot Chat to ask Copilot to create a pull request


Copilot will evaluate the task it has been assigned based on the prompt you give it—whether that's from the issue description or a chat message. Then Copilot will make the required changes and open a pull request. When Copilot finishes, it will request a review from you, and you can leave pull request comments to ask Copilot to iterate.
While working on a coding task, Copilot has access to its own ephemeral development environment, powered by GitHub Actions, where it can explore your code, make changes, execute automated tests and linters and more.
### [Streamlining software development with Copilot coding agent](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/about-assigning-tasks-to-copilot#streamlining-software-development-with-copilot-coding-agent)
Assigning tasks to Copilot can enhance your software development workflow.
For example, you can assign Copilot to straightforward issues on your backlog. This allows you to spend less time on these and more time on more complex or interesting work, or work that requires a high degree of creative thinking. Copilot can work on "nice to have" issues that improve the quality of your codebase or product, but often remain on the backlog while you focus on more urgent work.
Having Copilot as an additional coding resource also allows you to start tasks that you might not have otherwise due to lack of resources. For example, you might delegate Copilot tasks to refactor code or add more logging, then immediately assign these to Copilot.
Copilot can start a task, which you then pick up and continue working on yourself. By assigning the initial work to Copilot, you free up time that you would otherwise have spent doing repetitive tasks, such as setting up the scaffolding for a new project.
### [Making Copilot coding agent available](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/about-assigning-tasks-to-copilot#making-copilot-coding-agent-available)
Before you can assign tasks to Copilot, it must be enabled. See [Enabling Copilot coding agent](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/enabling-copilot-coding-agent).
## [Copilot coding agent usage costs](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/about-assigning-tasks-to-copilot#copilot-coding-agent-usage-costs)
Starting June 4th, 2025, Copilot coding agent will use one premium request per model request the agent makes. This is a preview feature and may be changed in the future.
Copilot coding agent uses GitHub Actions minutes and Copilot premium requests.
Within your monthly usage allowance for GitHub Actions and premium requests, you can ask Copilot to work on coding tasks without incurring any additional costs.
For more information, see [About billing for GitHub Copilot](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-copilot/about-billing-for-github-copilot#allowance-usage-for-copilot-coding-agent).
## [Risks and mitigations](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/about-assigning-tasks-to-copilot#risks-and-mitigations)
Copilot coding agent is an autonomous agent that has access to your code and can push changes to your repository. This entails certain risks. Where possible, GitHub has applied appropriate mitigations.
### [Risk: Copilot can push code changes to your repository](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/about-assigning-tasks-to-copilot#risk-copilot-can-push-code-changes-to-your-repository)
To mitigate this risk, GitHub:
  * **Limits who can assign tasks to Copilot.** Only users with write access to the repository can trigger Copilot to work. Comments from users without write access are never presented to the agent.
  * **Limits the permissions in access tokens used by Copilot.** Pushes are only allowed to branches beginning with `copilot/`. Copilot cannot push to the `main` or `master` branches.
  * **Limits Copilot's credentials.** Copilot can only perform simple push operations. It cannot directly run `git push` or other Git commands.
  * **Restricts GitHub Actions workflow runs.** Workflows are not triggered until Copilot's code is reviewed and a user with write access to the repo clicks the **Approve and run workflows** button. See [Using Copilot to work on an issue](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/using-copilot-to-work-on-an-issue#allowing-github-actions-workflows-to-run-when-copilot-pushes-changes).
  * **Prevents the user who asked Copilot to create a pull request from approving it.** This maintains the expected controls in the "Required approvals" rule and branch protection. See [Available rules for rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets).


### [Risk: Copilot has access to sensitive information](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/about-assigning-tasks-to-copilot#risk-copilot-has-access-to-sensitive-information)
Copilot has access to code and other sensitive information, and could leak it, either accidentally or due to malicious user input. To mitigate this risk, GitHub:
  * **Restricts Copilot's access to the internet.** See [Customizing or disabling the firewall for Copilot coding agent](https://docs.github.com/en/copilot/customizing-copilot/customizing-or-disabling-the-firewall-for-copilot-coding-agent).


### [Risk: Prompt injection vulnerabilities](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/about-assigning-tasks-to-copilot#risk-prompt-injection-vulnerabilities)
Users can include hidden messages in issues assigned to Copilot or comments left for Copilot as a form of [prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/). To mitigate this risk, GitHub:
  * **Filters hidden characters before passing user input to Copilot** : For example, text entered as an HTML comment in an issue or pull request comment is not passed to Copilot.


## [Limitations of Copilot coding agent](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/about-assigning-tasks-to-copilot#limitations-of-copilot-coding-agent)
Copilot coding agent has certain limitations in its software development workflow and compatibility with other features.
### [Limitations in Copilot's software development workflow](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/about-assigning-tasks-to-copilot#limitations-in-copilots-software-development-workflow)
  * **Copilot can only make changes in the same repository where it is creating its pull request**. When Copilot is assigned an issue, it can only make changes in the repository where that issue is located. In addition, Copilot cannot make changes across multiple repositories in one run.
  * **Copilot can only access context in the same repository as the assigned issue**. By default, an integration with the Copilot MCP server provides Copilot access to one repository at a time. You can, however, configure broader access. See [Extending Copilot coding agent with the Model Context Protocol (MCP)](https://docs.github.com/en/enterprise-cloud@latest/copilot/customizing-copilot/extending-copilot-coding-agent-with-mcp).
  * **Copilot can only open one pull request at a time**. Copilot will open exactly one pull request to address each task it is assigned.
  * **Copilot cannot work on an existing pull request that it didn't create**. If you would like Copilot to provide feedback on an existing pull request, you can add it as a reviewer. See [Using GitHub Copilot code review](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review).
  * **Copilot will always start its changes from the repository's default branch**. Copilot cannot branch off from any other branch—for example, a feature branch or a release branch.


### [Limitations in Copilot's compatibility with other features](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/about-assigning-tasks-to-copilot#limitations-in-copilots-compatibility-with-other-features)
  * **Copilot does not sign its commits**. If you have the "Require signed commits" rule or branch protection enabled, you must rewrite the commit history in order to merge Copilot's pull requests. See [Available rules for rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-signed-commits).
  * **Copilot does not work with self-hosted GitHub Actions runners**. Copilot has access to its own development environment, running in GitHub Actions, and must use GitHub-hosted runners. See [Customizing the development environment for Copilot coding agent](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent#upgrading-to-larger-github-hosted-github-actions-runners).
  * **Copilot doesn't account for content exclusions**. Content exclusions allow administrators to configure Copilot to ignore certain files. When using Copilot coding agent, Copilot will not ignore these files, and will be able to see and update them. See [Excluding content from GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion/excluding-content-from-github-copilot).
  * **Copilot coding agent is not available in GitHub Enterprise Cloud with data residency**. The agent is only available in GitHub.com.


## [Further reading](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/about-assigning-tasks-to-copilot#further-reading)
  * [Coding agent](https://docs.github.com/en/copilot/using-github-copilot/coding-agent)
  * [Responsible use of Copilot coding agent on GitHub.com](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom)
  * [Customizing the development environment for Copilot coding agent](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent)
  * [Customizing or disabling the firewall for Copilot coding agent](https://docs.github.com/en/copilot/customizing-copilot/customizing-or-disabling-the-firewall-for-copilot-coding-agent)
  * [Extending Copilot coding agent with the Model Context Protocol (MCP)](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-coding-agent-with-mcp)


