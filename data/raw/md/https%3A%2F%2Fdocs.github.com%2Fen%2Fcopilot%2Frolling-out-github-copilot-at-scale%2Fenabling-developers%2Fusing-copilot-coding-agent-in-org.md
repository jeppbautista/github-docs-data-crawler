  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Roll out Copilot at scale](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale "Roll out Copilot at scale")/
  * [Enabling developers](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/enabling-developers "Enabling developers")/
  * [Use Copilot coding agent](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/enabling-developers/using-copilot-coding-agent-in-org "Use Copilot coding agent")


# Using Copilot coding agent effectively in your organization
Learn about adopting Copilot coding agent in your organization.
## Who can use this feature?
Copilot coding agent is available with the GitHub Copilot Pro+ and GitHub Copilot Enterprise plans in repositories where it is enabled.
## In this article
  * [Why Copilot coding agent?](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/enabling-developers/using-copilot-coding-agent-in-org#why-copilot-coding-agent)
  * [How Copilot coding agent can contribute to your organization](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/enabling-developers/using-copilot-coding-agent-in-org#how-copilot-coding-agent-can-contribute-to-your-organization)
  * [Using MCP to enhance Copilot coding agent](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/enabling-developers/using-copilot-coding-agent-in-org#using-mcp-to-enhance-copilot-coding-agent)
  * [Using Copilot coding agent securely](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/enabling-developers/using-copilot-coding-agent-in-org#using-copilot-coding-agent-securely)
  * [Piloting Copilot coding agent](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/enabling-developers/using-copilot-coding-agent-in-org#piloting-copilot-coding-agent)


Copilot coding agent is in public preview and subject to change.
## [Why Copilot coding agent?](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/enabling-developers/using-copilot-coding-agent-in-org#why-copilot-coding-agent)
Copilot coding agent is an autonomous, AI-powered agent that completes software development tasks on GitHub. Adopting Copilot coding agent in your organization frees your engineering teams to spend more time thinking strategically and less time making routine fixes and maintenance updates in a codebase. Copilot coding agent:
  * **Joins your team** : Developers can delegate work to Copilot unlike IDE-based coding agents that require synchronous pairing sessions.
  * **Reduces context switching** : Developers working in JetBrains IDEs, VS Code, Visual Studio, or GitHub.com can ask Copilot coding agent to create a pull request to complete small tasks without stopping what they are currently doing.
  * **Works on GitHub** : Copilot operates within your existing workflows on GitHub alongside your developers.
  * **Uses pull request review workflows** : Copilot opens draft pull requests for team members to review and iterates based on feedback, as a developer would.
  * **Executes tasks in parallel** : Copilot can work on multiple issues simultaneously, handling tasks in the background while your team focuses on other priorities.
  * **Provides decision transparency** : Developers can review Copilot’s logs on GitHub to understand its reasoning and see the tools it used to complete tasks.
  * **Ensures enterprise-grade security** : Copilot coding agent's security-first design keeps a human in the loop and enables governance via enterprise policies and settings.


## [How Copilot coding agent can contribute to your organization](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/enabling-developers/using-copilot-coding-agent-in-org#how-copilot-coding-agent-can-contribute-to-your-organization)
Copilot can help your organization address well-defined and scoped issues, such as increasing test coverage, fixing bugs or flaky tests, or updating config files or documentation. For more on the kinds of issues Copilot works best on, see [Best practices for using Copilot to work on tasks](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/best-practices-for-using-copilot-to-work-on-tasks).
Developers stay in the flow when they ask Copilot to create pull requests directly from Copilot Chat instead of opening issues that may sit in a backlog.
When used effectively, Copilot coding agent offers productivity benefits over traditional AI assistants in IDEs:
  * With **AI assistants in IDEs** , coding happens **locally**. Individual developers pair in **synchronous** sessions with the AI assistant. Decisions made during the session are **untracked** and lost to time unless committed. Although the assistant helps write code, the developer still has a lot of **manual steps** to do: create the branch, write commit messages, push the changes, open the PR, write the PR description, get a review, iterate in the IDE, and repeat. These steps take time and effort that may be hard to justify for simple or routine issues.
  * With **Copilot coding agent** , all coding and iterating happens **on GitHub** as part of the pull request workflow. Copilot **automates** branch creation, commit message writing and pushing, PR opening, and PR description writing. Developers let the agent **work in the background** and then steer Copilot to a final solution using PR reviews. Working on GitHub adds **transparency** , where every step happens in a commit and is viewable in logs. Working on GitHub also opens up **collaboration** opportunities for the entire team.


Over time, your engineering teams can benefit from the increased automation, transparency, and collaboration Copilot coding agent provides. For ideas on how to run a successful pilot, see [Piloting Copilot coding agent](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/enabling-developers/using-copilot-coding-agent-in-org#piloting-copilot-coding-agent).
For an example scenario that walks through how to use Copilot coding agent alongside other AI features on GitHub, see [Integrating agentic AI into your enterprise's software development lifecycle](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/enabling-developers/integrating-agentic-ai).
## [Using MCP to enhance Copilot coding agent](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/enabling-developers/using-copilot-coding-agent-in-org#using-mcp-to-enhance-copilot-coding-agent)
The Model Context Protocol (MCP) is an open standard that defines how applications share context with large language models (LLMs). MCP provides a standardized way to provide Copilot coding agent with access to different data sources and tools.
Copilot coding agent has access to the full GitHub context of the repository it's working in, including issues and pull requests, using the built-in GitHub MCP server. By default, it's restricted from accessing external data by authentication barriers and a firewall. You can extend the information available to Copilot coding agent by giving it access to local MCP servers for the tools your organization uses. For example, you might want to provide access to local MCP servers for some of the following contexts:
  * **Web browser** : Set up the Playwright MCP server to allow Copilot to pull context directly from an external link in an issue.
  * **Project planning tools** : Allow Copilot direct access to private planning documents that are stored outside GitHub in tools like Notion or Figma.
  * **Augment training data** : Each LLM contains training data up to a specific cut-off date. If you're working with fast moving tools, Copilot may not have access to information on new features. You can fill this knowledge gap by making the tool's MCP server available. For example, adding the Terraform MCP server will give Copilot access to the most recently supported Terraform providers.


For more information, see [Extending Copilot coding agent with the Model Context Protocol (MCP)](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-coding-agent-with-mcp).
## [Using Copilot coding agent securely](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/enabling-developers/using-copilot-coding-agent-in-org#using-copilot-coding-agent-securely)
Security is a fundamental consideration when you enable Copilot coding agent, as with any other AI agent. Copilot has a strong base of built-in security protections that you can supplement by following best practice guidance.
### [Built-in protections](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/enabling-developers/using-copilot-coding-agent-in-org#built-in-protections)
  * **Subject to existing governance** : Organization settings and enterprise policies control availability. Any security policies and practices set up for the organization also apply to Copilot coding agent.
  * **Restricted development environment** : Copilot works in a sandbox development environment with internet access controlled by a firewall. It has read-only access to the repository it's assigned to work in.
  * **Limited access to branches** : Copilot can only create and push to branches beginning with `copilot/`. It is subject to any branch protections and required checks for the working repository.
  * **Responds only to users with write permissions** : Copilot will not respond to feedback from users with lower levels of access.
  * **Treated as an outside collaborator** : Draft pull requests proposed by Copilot require approval by a user with write permissions before Actions workflows can run. Copilot cannot mark its pull requests as "Ready for review" and cannot approve or merge a pull request.
  * **Tracked for compliance** : Copilot's commits are co-authored by the developer who assigned the issue or requested the change to the pull request, allowing attribution of proposed changes. The developer who asked Copilot to create a pull request cannot approve that pull request. In repositories where an approving review is required, this ensures that at least one independent developer reviews Copilot's work.


For more information, see:
  * [Responsible use of Copilot coding agent on GitHub.com](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom)
  * [GitHub Copilot Trust Center](https://copilot.github.trust.page/)


### [Security best practices](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/enabling-developers/using-copilot-coding-agent-in-org#security-best-practices)
All AI models are trained to meet a request, even if they don't have all the information needed to provide a good answer, and this can lead them to make mistakes. By following best practices, you can reduce the risks of using Copilot in your organization.
  1. Give Copilot the information it needs to work successfully in a repository using a `copilot-instructions.md` file. See [Adding repository custom instructions for GitHub Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot).
  2. Set up the Copilot development environment for a repository with access to the tools and package repositories approved by the organization using a `copilot-setup-steps.yml` file and local MCP servers. See [Customizing the development environment for Copilot coding agent](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent) and [Extending Copilot coding agent with the Model Context Protocol (MCP)](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-coding-agent-with-mcp).
  3. Follow best practices for storing secrets securely. See [Using secrets in GitHub Actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions).
  4. Enable code security features to further lower the risk of leaking secrets and introducing vulnerabilities into the code. See [Applying the GitHub-recommended security configuration in your organization](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/applying-the-github-recommended-security-configuration-in-your-organization).
  5. Configure your branch rulesets to ensure that all pull requests raised by Copilot are approved by a second user with write permissions (a sub-option of "Require a pull request before merging"). See [Creating rulesets for repositories in your organization](https://docs.github.com/en/organizations/managing-organization-settings/creating-rulesets-for-repositories-in-your-organization) and [Available rules for rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-a-pull-request-before-merging).


## [Piloting Copilot coding agent](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/enabling-developers/using-copilot-coding-agent-in-org#piloting-copilot-coding-agent)
[Sign up for Copilot ](https://github.com/github-copilot/purchase?ref_cta=Copilot+Enterprise+trial&ref_cta=Copilot+Business+trial&ref_loc=using-cca-effectively)
During the public preview, you need GitHub Copilot Pro+ or GitHub Copilot Enterprise to use Copilot coding agent.
As with any other change to working practices, it's important to run a trial to learn how to deploy Copilot coding agent effectively in your organization or enterprise.
  1. Gather a cross-functional team for the trial to bring different roles, backgrounds, and perspectives to the project. This will make it easier to ensure that you explore a broad range of ways to define issues, assign work to Copilot, and give clear review feedback.
  2. Choose an isolated or low-risk repository, for example, one that contains documentation or internal tools. You could create a fresh repository to use as a playground, but Copilot needs context to be successful, so you would need to add a lot of context, including team processes, development environment, and common dependencies.
  3. Enable Copilot coding agent in the repository and optionally enable third-party MCP servers for enhanced context sharing. See [Adding Copilot coding agent to your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/adding-copilot-coding-agent-to-organization).
  4. Create repository instructions and pre-install any tools required in the development environment Copilot uses. See [Customizing the development environment for Copilot coding agent](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent).
  5. Identify a few compelling use cases for your organization, for example: test coverage or improving accessibility. See [Choose the right type of tasks to give to Copilot](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/best-practices-for-using-copilot-to-work-on-tasks#choosing-the-right-type-of-tasks-to-give-to-copilot) in the best practice guide.
  6. Use best practice to create or refine issues for Copilot in your pilot repository.
  7. Assign issues to Copilot and prepare team members to review its work.
  8. Spend time looking at the codebase or documentation in VS Code or GitHub.com, asking Copilot to create a pull request to fix any bugs or small improvements that you identify.


Over the course of the trial, the team should iterate on the repository instructions, installed tools, access to MCP servers, and issue definition to identify how your organization can get the most from Copilot coding agent. This process will help you identify your organization's best practices for working with Copilot and plan an effective rollout strategy.
In addition to giving you insight into how to set up Copilot coding agent for success, you'll learn how Copilot uses premium requests and actions minutes. This will be valuable when you come to set and manage your budget for a broader trial or full rollout. See [Managing your company's spending on GitHub Copilot](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/assigning-licenses/managing-your-companys-spending-on-github-copilot).
