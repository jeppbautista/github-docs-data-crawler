  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Use GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot "Use GitHub Copilot")/
  * [Coding agent](https://docs.github.com/en/copilot/using-github-copilot/coding-agent "Coding agent")/
  * [Troubleshooting](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/troubleshooting-copilot-coding-agent "Troubleshooting")


# Troubleshooting Copilot coding agent
Learn how to resolve problems that may occur when you assign tasks to Copilot.
## Who can use this feature?
Copilot coding agent is available with the GitHub Copilot Pro+ and GitHub Copilot Enterprise plans in repositories where it is enabled.  
[Sign up for Copilot ](https://github.com/features/copilot/plans?ref_cta=Copilot+plans+signup&ref_loc=troubleshooting+copilot+coding+agent&ref_page=docs)
## In this article
  * [Copilot is not available in the "Assignees" list on my issue](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/troubleshooting-copilot-coding-agent#copilot-is-not-available-in-the-assignees-list-on-my-issue)
  * [Copilot can't create a pull request from Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/troubleshooting-copilot-coding-agent#copilot-cant-create-a-pull-request-from-copilot-chat)
  * [I assigned an issue to Copilot, but nothing is happening](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/troubleshooting-copilot-coding-agent#i-assigned-an-issue-to-copilot-but-nothing-is-happening)
  * [Copilot has opened a pull request, but nothing is happening](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/troubleshooting-copilot-coding-agent#copilot-has-opened-a-pull-request-but-nothing-is-happening)
  * [Copilot won't respond to my pull request comments](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/troubleshooting-copilot-coding-agent#copilot-wont-respond-to-my-pull-request-comments)
  * [Based on the agent session logs, Copilot appears to be stuck](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/troubleshooting-copilot-coding-agent#based-on-the-agent-session-logs-copilot-appears-to-be-stuck)
  * [My GitHub Actions workflows are not running when Copilot pushes](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/troubleshooting-copilot-coding-agent#my-github-actions-workflows-are-not-running-when-copilot-pushes)
  * [Copilot is pushing changes which don't pass my CI checks](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/troubleshooting-copilot-coding-agent#copilot-is-pushing-changes-which-dont-pass-my-ci-checks)
  * [There is a warning from GitHub Copilot about the firewall](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/troubleshooting-copilot-coding-agent#there-is-a-warning-from-github-copilot-about-the-firewall)
  * [Further reading](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/troubleshooting-copilot-coding-agent#further-reading)


Copilot coding agent is in public preview and subject to change.
## [Copilot is not available in the "Assignees" list on my issue](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/troubleshooting-copilot-coding-agent#copilot-is-not-available-in-the-assignees-list-on-my-issue)
You can only assign issues to Copilot if you have access to Copilot through either the **GitHub Copilot Pro+** plan or the **GitHub Copilot Enterprise** plan.
If you do not already have a subscription for one of these plans, click this button for more information:  
[Sign up for Copilot ](https://github.com/features/copilot/plans?ref_cta=Copilot+plans+signup&ref_loc=troubleshooting+copilot+coding+agent&ref_page=docs)
If you _do_ have either GitHub Copilot Pro+ or GitHub Copilot Enterprise, check that Copilot coding agent has been made available for the repository:
  * For organization-owned repositories, the availability of Copilot coding agent in the repository is configured in the settings for the organization. See [Adding Copilot coding agent to your organization](https://docs.github.com/en/enterprise-cloud@latest/copilot/managing-copilot/managing-github-copilot-in-your-organization/adding-copilot-coding-agent-to-organization).
  * For personal repositories, the availability of Copilot coding agent in the repository is configured in your account settings. See [Managing Copilot policies as an individual subscriber](https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/managing-your-copilot-plan/managing-copilot-policies-as-an-individual-subscriber#enabling-or-disabling-copilot-coding-agent).


You can check whether Copilot coding agent has been enabled for you in the features page of your Copilot settings: [github.com/settings/copilot/features](https://github.com/settings/copilot/features).
## [Copilot can't create a pull request from Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/troubleshooting-copilot-coding-agent#copilot-cant-create-a-pull-request-from-copilot-chat)
If you asked Copilot to create a pull request and it responds that it cannot directly create a pull request, check that Copilot coding agent is available.
In VS Code, Visual Studio, and JetBrains IDEs, you must mention the `@github` chat participant in your prompt. You can omit this in Copilot Chat on GitHub.com.
## [I assigned an issue to Copilot, but nothing is happening](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/troubleshooting-copilot-coding-agent#i-assigned-an-issue-to-copilot-but-nothing-is-happening)
Wait a while, then refresh the page. You should see Copilot leave an 👀 reaction on the issue. Shortly after this, Copilot will open a draft pull request linked to the issue, which will be shown in the issue timeline.
## [Copilot has opened a pull request, but nothing is happening](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/troubleshooting-copilot-coding-agent#copilot-has-opened-a-pull-request-but-nothing-is-happening)
If there is a "Copilot started work" event in the pull request timeline, click **View session** to see the session logs. These will stream live, and you will be able to see what Copilot is doing.
## [Copilot won't respond to my pull request comments](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/troubleshooting-copilot-coding-agent#copilot-wont-respond-to-my-pull-request-comments)
Copilot only responds to comments from people who have write access to the repository.
If you do have write access, and you add a comment on a pull request that is assigned to Copilot, the comment is passed to Copilot coding agent. An eyes emoji (👀) is added to your comment to indicate that Copilot coding agent is considering your comment. If the agent proceeds to work on making changes in response to your comment a "Copilot started work" event is added to the pull request timeline.
If this doesn't happen, Copilot may have been unassigned from the pull request, or Copilot may have decided that your comment is not actionable.
Check that Copilot is assigned to the pull request. If it is, you can force Copilot to respond to your comment by @mentioning Copilot in the comment with `@copilot`.
## [Based on the agent session logs, Copilot appears to be stuck](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/troubleshooting-copilot-coding-agent#based-on-the-agent-session-logs-copilot-appears-to-be-stuck)
Copilot can appear to be stuck for a while, and then get moving again.
If the session remains stuck, it will time out after an hour. You can retry by unassigning the issue and then reassigning it to Copilot.
If Copilot got stuck while responding to a comment, try adding the same comment to the pull request again.
## [My GitHub Actions workflows are not running when Copilot pushes](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/troubleshooting-copilot-coding-agent#my-github-actions-workflows-are-not-running-when-copilot-pushes)
GitHub Actions workflows will not run automatically when Copilot pushes changes to a pull request.
To allow GitHub Actions workflows to run, click the **Approve and run workflows** button in the pull request's merge box. See [Using Copilot to work on an issue](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/using-copilot-to-work-on-an-issue#allowing-github-actions-workflows-to-run-when-copilot-pushes-changes).
## [Copilot is pushing changes which don't pass my CI checks](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/troubleshooting-copilot-coding-agent#copilot-is-pushing-changes-which-dont-pass-my-ci-checks)
While working on an issue, Copilot has access to its own ephemeral development environment, powered by GitHub Actions, where it can execute automated tests and linters to validate its work before it pushes.
It is most likely to do this if given clear instructions on what to do. The best way to do this is with a `.github/copilot-instructions.md` file. See [Best practices for using Copilot to work on tasks](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/best-practices-for-using-copilot-to-work-on-tasks#adding-custom-instructions-to-your-repository).
## [There is a warning from GitHub Copilot about the firewall](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/troubleshooting-copilot-coding-agent#there-is-a-warning-from-github-copilot-about-the-firewall)
By default, Copilot's access to the internet is limited by a firewall.
Limiting access to the internet helps to manage data exfiltration risks, where surprising behavior from Copilot or malicious instructions given to it could lead to code or other sensitive information being leaked to remote locations.
If Copilot tries to make a request which is blocked by the firewall, a warning is added to the pull request body (if Copilot is responding to an issue assignment) or to a comment (if Copilot is responding to a comment). The warning shows the blocked address and the command that tried to make the request.
![Screenshot of a warning from Copilot about being blocked by the firewall.](https://docs.github.com/assets/cb-121588/images/help/copilot/coding-agent/firewall-warning.png)
For more information, see [Customizing or disabling the firewall for Copilot coding agent](https://docs.github.com/en/copilot/customizing-copilot/customizing-or-disabling-the-firewall-for-copilot-coding-agent).
## [Further reading](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/troubleshooting-copilot-coding-agent#further-reading)
  * [Best practices for using Copilot to work on tasks](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/best-practices-for-using-copilot-to-work-on-tasks)
  * [Customizing the development environment for Copilot coding agent](https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent)


