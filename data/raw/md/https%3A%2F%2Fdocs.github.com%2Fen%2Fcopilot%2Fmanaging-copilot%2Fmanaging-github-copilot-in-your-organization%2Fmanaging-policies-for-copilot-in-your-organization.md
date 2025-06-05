  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Manage Copilot](https://docs.github.com/en/copilot/managing-copilot "Manage Copilot")/
  * [Manage for organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization "Manage for organization")/
  * [Manage policies](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization "Manage policies")


# Managing policies for Copilot in your organization
Learn how to manage policies for GitHub Copilot in your organization.
## Who can use this feature?
Organization owners
Organizations with a GitHub Copilot Business or GitHub Copilot Enterprise plan
## In this article
  * [About policies for GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization#about-policies-for-github-copilot)
  * [Enabling Copilot features in your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization#enabling-copilot-features-in-your-organization)
  * [Setting a policy for GitHub Copilot Extensions in your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization#setting-a-policy-for-github-copilot-extensions-in-your-organization)
  * [Further reading](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization#further-reading)


## [About policies for GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization#about-policies-for-github-copilot)
Organization owners can set policies to govern how GitHub Copilot can be used within the organization. For example, an organization owner can enable or disable the following Copilot features:
  * Copilot in GitHub.com
  * Copilot Chat in the IDE
  * Editor preview Copilot features, such as: 
    * Image support in Copilot Chat (available in VS Code and Visual Studio) 
This setting only applies to preview features within Copilot and does not control all preview-related settings in VS Code.
  * Copilot coding agent (public preview)
  * Copilot Spaces (public preview)
  * MCP servers on GitHub.com (public preview)
  * Copilot Chat in GitHub Mobile
  * Copilot in the CLI and Windows Terminal
  * Copilot in GitHub Desktop (public preview)
  * Suggestions matching public code
  * Access to alternative models for Copilot 
    * Anthropic Claude in Copilot
    * Google Gemini in Copilot
    * OpenAI models in Copilot


The policy settings selected by an organization owner determine the behavior of Copilot for all organization members that have been granted access to Copilot through the organization.
### [Policies for suggestion matching](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization#policies-for-suggestion-matching)
Organization settings include an option to either allow or block code suggestions that match publicly available code. If you choose to block suggestions matching public code, Copilot will check potential code suggestions and the surrounding code of about 150 characters against public code on GitHub. If there is a match, or a near match, the suggestion is not shown.
## [Enabling Copilot features in your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization#enabling-copilot-features-in-your-organization)
Copilot policies are also managed at the enterprise level. If your organization is part of an enterprise, and explicit settings have been selected at the enterprise level, you cannot override those settings at the organization level. For more information on managing policies at the enterprise level, see [Managing policies and features for Copilot in your enterprise](https://docs.github.com/en/enterprise-cloud@latest/copilot/managing-copilot/managing-copilot-for-your-enterprise/managing-policies-and-features-for-copilot-in-your-enterprise).
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the sidebar, under "Code, planning, and automation", click **Policies**.
  4. Use the dropdown options to the right of each feature to enable or disable that feature for your organization.
For example, to enable or disable suggestion matching, in the "Suggestions matching public code" dropdown, select **Allowed** or **Blocked**.
  5. If your organization has a Copilot Business plan and you enable "Copilot in GitHub.com", two additional options are displayed:
     * **Opt in to user feedback collection:** If enabled, users can provide feedback on Copilot pull request summaries. For more information, see [Creating a pull request summary with GitHub Copilot](https://docs.github.com/en/enterprise-cloud@latest/copilot/github-copilot-enterprise/copilot-pull-request-summaries/creating-a-pull-request-summary-with-github-copilot).
     * **Opt in to preview features:** If enabled, users can test new Copilot features that are not yet generally available. Be aware that previews of features may have flaws, and the features may be changed or discontinued at any time. Current previews of Copilot features include:
       * Experimental languages in Copilot code review. See [Using GitHub Copilot code review](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review).
       * Copilot Spaces. See [About organizing and sharing context with Copilot Spaces](https://docs.github.com/en/copilot/using-github-copilot/copilot-spaces/about-organizing-and-sharing-context-with-copilot-spaces).


If you choose to enable Copilot coding agent for users, you also need to define which repositories the agent is available in, see [Adding Copilot coding agent to your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/adding-copilot-coding-agent-to-organization).
## [Setting a policy for GitHub Copilot Extensions in your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization#setting-a-policy-for-github-copilot-extensions-in-your-organization)
GitHub Copilot Extensions integrate external tools with GitHub Copilot Chat. See [Using extensions to integrate external tools with Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/using-extensions-to-integrate-external-tools-with-copilot-chat).
Before you install Copilot Extensions in your organization, you should set a usage policy for your organization. Setting a usage policy allows you to enable or disable Copilot Extensions for all members of your organization, limiting your security risk.
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the sidebar, under "Code, planning, and automation", click **Policies**.
  4. In the "Copilot Extensions" section, select the dropdown menu, then enable or disable Copilot Extensions for your organization.


### [Managing permissions for a GitHub Copilot Extension in your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization#managing-permissions-for-a-github-copilot-extension-in-your-organization)
After you have installed a Copilot Extension in your organization, you can view the permissions the extension has in your organization, and why those permissions are necessary. If you do not want the Copilot Extension to have the listed permissions, you can suspend or uninstall the extension.
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the sidebar, under "Third-party Access," click **GitHub Apps**. A list of the GitHub Apps installed on your organization will be displayed.
  4. Optionally, to filter your installed GitHub Apps for Copilot Extensions, select the **Filter:** dropdown menu, then click **Copilot Extensions**.
  5. Next to the Copilot Extension you want to review or modify, click **Configure**.
  6. In the "Permissions" section, review the permissions listed for the Copilot Extension. Optionally, you can block the Copilot Extension's access to your organization in one of two ways: 
     * To indefinitely suspend the Copilot Extension's access to resources in your organization while keeping the extension installed, in the "Danger zone" section, click **Suspend**.
     * To uninstall a Copilot Extension completely, in the "Danger zone" section, click **Uninstall**.


## [Further reading](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization#further-reading)
  * [GitHub Copilot Trust Center](https://copilot.github.trust.page)
  * [Finding public code that matches GitHub Copilot suggestions](https://docs.github.com/en/copilot/using-github-copilot/finding-public-code-that-matches-github-copilot-suggestions)
  * [Adding Copilot coding agent to your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/adding-copilot-coding-agent-to-organization)


