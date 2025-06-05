  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Manage Copilot](https://docs.github.com/en/copilot/managing-copilot "Manage Copilot")/
  * [Manage for organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization "Manage for organization")/
  * [Add Copilot coding agent](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/adding-copilot-coding-agent-to-organization "Add Copilot coding agent")


# Adding Copilot coding agent to your organization
Enable Copilot coding agent for your members and define repositories where it is available.
## Who can use this feature?
Organization owners
Copilot coding agent is available with the GitHub Copilot Pro+ and GitHub Copilot Enterprise plans in repositories where it is enabled.  
[Sign up for Copilot ](https://github.com/github-copilot/purchase?ref_cta=Copilot+Enterprise+trial&ref_cta=Copilot+Business+trial&ref_loc=adding-cca-to-org)
## In this article
  * [Prerequisites](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/adding-copilot-coding-agent-to-organization#prerequisites)
  * [Enabling Copilot coding agent for your members](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/adding-copilot-coding-agent-to-organization#enabling-copilot-coding-agent-for-your-members)
  * [Defining which repositories Copilot coding agent can operate in](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/adding-copilot-coding-agent-to-organization#defining-which-repositories-copilot-coding-agent-can-operate-in)
  * [Next steps](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/adding-copilot-coding-agent-to-organization#next-steps)


Copilot coding agent is in public preview and subject to change.
## [Prerequisites](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/adding-copilot-coding-agent-to-organization#prerequisites)
  * For general information, see [Using Copilot coding agent effectively in your organization](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/enabling-developers/using-copilot-coding-agent-in-org).
  * For information on premium requests and Actions minutes, see [Allowance usage for Copilot coding agent](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-copilot/about-billing-for-github-copilot#allowance-usage-for-copilot-coding-agent).
  * For information on MCP servers, see [Extending Copilot coding agent with the Model Context Protocol (MCP)](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-coding-agent-with-mcp).


## [Enabling Copilot coding agent for your members](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/adding-copilot-coding-agent-to-organization#enabling-copilot-coding-agent-for-your-members)
Copilot policies are also managed at the enterprise level. If your organization is part of an enterprise, and explicit settings have been selected at the enterprise level, you cannot override those settings at the organization level. For more information on managing policies at the enterprise level, see [Managing policies and features for Copilot in your enterprise](https://docs.github.com/en/enterprise-cloud@latest/copilot/managing-copilot/managing-copilot-for-your-enterprise/managing-policies-and-features-for-copilot-in-your-enterprise).
Copilot coding agent and use of third-party MCP servers are disabled by default for organization members. Organization owners with GitHub Copilot Enterprise can enable these features for members on the Copilot policies page for their organization. See [Enabling Copilot features in your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization#enabling-copilot-features-in-your-organization).
  * For the "Copilot coding agent" policy, select "Enabled".
  * For the "MCP servers on GitHub.com" policy, select "Enabled".


## [Defining which repositories Copilot coding agent can operate in](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/adding-copilot-coding-agent-to-organization#defining-which-repositories-copilot-coding-agent-can-operate-in)
Owners of any organization—even organizations without a Copilot plan—can define which repositories Copilot coding agent can work in.
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the sidebar, under "Code, planning, and automation", click **Copilot agent**.
  4. Use the "Repository access" control to define which repositories allow Copilot coding agent.
  5. If you choose "Selected repositories", in the "Select repositories" dialog, select the repositories that allow Copilot coding agent, then click **Select**.


Once Copilot coding agent is enabled for a repository, any user with access to Copilot coding agent and write permission for the repository can delegate work to Copilot.
## [Next steps](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/adding-copilot-coding-agent-to-organization#next-steps)
  * Tell the members of repositories where Copilot coding agent is available that they can delegate work to the coding agent.
  * Encourage members to educate themselves about setting up their repository to get the most from Copilot coding agent. Useful resources:
    * [Best practices for using Copilot to work on tasks](https://docs.github.com/en/copilot/using-github-copilot/using-copilot-coding-agent-to-work-on-issues/best-practices-for-using-copilot-to-work-on-tasks)
    * [Customizing the development environment for Copilot coding agent](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent)
    * [Security best practices](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/enabling-developers/using-copilot-coding-agent-in-org#security-best-practices)


