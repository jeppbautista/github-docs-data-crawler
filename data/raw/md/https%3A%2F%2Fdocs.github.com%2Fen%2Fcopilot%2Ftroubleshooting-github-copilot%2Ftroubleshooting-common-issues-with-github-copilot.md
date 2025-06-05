  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Troubleshooting](https://docs.github.com/en/copilot/troubleshooting-github-copilot "Troubleshooting")/
  * [Common issues with GitHub Copilot](https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-common-issues-with-github-copilot "Common issues with GitHub Copilot")


# Troubleshooting common issues with GitHub Copilot
This guide describes the most common issues with GitHub Copilot and how to resolve them.
## In this article
  * [Unable to use the GitHub Copilot extension in the IDE](https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-common-issues-with-github-copilot#unable-to-use-the-github-copilot-extension-in-the-ide)
  * [GitHub Copilot not working in some files](https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-common-issues-with-github-copilot#github-copilot-not-working-in-some-files)
  * [GitHub Copilot content exclusions are not being applied](https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-common-issues-with-github-copilot#github-copilot-content-exclusions-are-not-being-applied)
  * [Error: "GitHub Copilot could not connect to server. Extension activation failed"](https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-common-issues-with-github-copilot#error-github-copilot-could-not-connect-to-server-extension-activation-failed)
  * [Copilot not suggesting multiple lines of code](https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-common-issues-with-github-copilot#copilot-not-suggesting-multiple-lines-of-code)
  * [Error: "No valid OAuth token detected" in GitHub Copilot in the CLI](https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-common-issues-with-github-copilot#error-no-valid-oauth-token-detected-in-github-copilot-in-the-cli)
  * [Error: "Sorry, your request was rate-limited."](https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-common-issues-with-github-copilot#error-sorry-your-request-was-rate-limited)
  * [Further reading](https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-common-issues-with-github-copilot#further-reading)


For questions about the general use of GitHub Copilot, product impact, human oversight, and privacy, see the comprehensive list of [GitHub Copilot FAQs](https://github.com/features/copilot#:~:text=Frequently%20asked%C2%A0questions).
If GitHub Copilot stops working, check GitHub's [Status page](https://githubstatus.com) for any active incidents.
## [Unable to use the GitHub Copilot extension in the IDE](https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-common-issues-with-github-copilot#unable-to-use-the-github-copilot-extension-in-the-ide)
We recommend you follow the quickstart guide for GitHub Copilot while setting up GitHub Copilot on your machine. For more information, see [Quickstart for GitHub Copilot](https://docs.github.com/en/copilot/quickstart).
The GitHub Copilot extension is frequently updated to fix bugs and add new features. It's important to keep your extension up to date because older clients cannot communicate with the GitHub Copilot servers. Update your GitHub Copilot extension on all the machines you have it installed.
If you're using a Copilot plan for a managed user account on GHE.com, you'll need to update some settings before you sign in. See [Using GitHub Copilot with an account on GHE.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/using-github-copilot-with-an-account-on-ghecom).
For more information about configuring GitHub Copilot in a supported IDE, see [Configuring GitHub Copilot in your environment](https://docs.github.com/en/copilot/configuring-github-copilot/configuring-github-copilot-in-your-environment).
## [GitHub Copilot not working in some files](https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-common-issues-with-github-copilot#github-copilot-not-working-in-some-files)
If you're using GitHub Copilot with a Copilot Business or Copilot Enterprise license, you may not see code completion suggestions in your editor for some files. This happens when a file is excluded from being used by GitHub Copilot. Content exclusion can be configured by a repository administrator, or by an organization owner.
When a file is affected by a content exclusion setting, GitHub Copilot will not suggest code completion in that file, and the content of that file will not be used to inform code completion suggestions in other files.
If a file has been configured as excluded content for GitHub Copilot, the icon in the status bar will have a diagonal line through it. Hover over the icon to see a tooltip that tells you which settings have applied this restriction.
![Screenshot of the Copilot icon in VS Code with a tooltip for a content exclusion.](https://docs.github.com/assets/cb-36787/images/help/copilot/copilot-disabled-for-repo.png)
For more information, see [Excluding content from GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-github-copilot-features-in-your-organization/about-content-exclusions-for-github-copilot).
## [GitHub Copilot content exclusions are not being applied](https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-common-issues-with-github-copilot#github-copilot-content-exclusions-are-not-being-applied)
Content exclusion can be configured at the repository and organization level. The scope of the exclusion is determined by the level at which the rule is set:
  * **Repository administrators** can exclude content for their own repositories. This affects any Copilot users in the enterprise working within those specific repositories.
  * **Organization owners** can exclude content for users assigned a Copilot seat through their organization.


After you add or change content exclusions, it can take up to 30 minutes to take effect in IDEs where the settings are already loaded. You can apply changes to your own IDE, forcing it to reload the content exclusion settings. For more information, see [Excluding content from GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-github-copilot-features-in-your-organization/testing-changes-to-content-exclusions-in-your-ide#propagating-content-exclusion-changes-to-your-ide).
It's possible that Copilot may use semantic information from an excluded file if the information is provided by the IDE indirectly. Examples of such content include type information and hover-over definitions for symbols used in code, as well as general project properties such as build configuration information.
## [Error: "GitHub Copilot could not connect to server. Extension activation failed"](https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-common-issues-with-github-copilot#error-github-copilot-could-not-connect-to-server-extension-activation-failed)
This error indicates that you do not have a Copilot plan, or there was an error connecting to the GitHub API to request a token to use GitHub Copilot.
To request another token from api.github.com, try signing in and out of Copilot from your IDE. Once you've logged out, Copilot will prompt you to sign back in.
If you cannot connect to the server, you can create a discussion in our [discussion forum](https://github.com/orgs/community/discussions/categories/copilot). You can include log files from your IDE to help us troubleshoot the issue. For more information on obtaining log files from your specific IDE, see [Viewing logs for GitHub Copilot in your environment](https://docs.github.com/en/copilot/troubleshooting-github-copilot/viewing-logs-for-github-copilot-in-your-environment).
## [Copilot not suggesting multiple lines of code](https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-common-issues-with-github-copilot#copilot-not-suggesting-multiple-lines-of-code)
This is a known issue and our team is working towards a fix. For more information, see this comment on a [GitHub Community discussion](https://github.com/orgs/community/discussions/40522#discussioncomment-4701470).
## [Error: "No valid OAuth token detected" in GitHub Copilot in the CLI](https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-common-issues-with-github-copilot#error-no-valid-oauth-token-detected-in-github-copilot-in-the-cli)
This error suggests that a classic or fine-grained personal access token might be in use, either via the `GITHUB_TOKEN` or `GH_TOKEN` environment variables, or during a `gh auth login` attempt. GitHub Copilot in the CLI currently only supports using the GitHub CLI OAuth app.
For more information, see the [Copilot in the CLI extension repository](https://github.com/github/gh-copilot).
## [Error: "Sorry, your request was rate-limited."](https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-common-issues-with-github-copilot#error-sorry-your-request-was-rate-limited)
This error suggests that you have exceeded the rate limit for Copilot requests. GitHub uses rate limits to ensure everyone has fair access to the Copilot service and to protect against abuse.
Most people see rate limiting for preview models, like OpenAI’s o1 and o3-mini, which are rate-limited due to limited capacity.
Service-level request rate limits ensure high service quality for all Copilot users and should not affect typical or even deeply engaged Copilot usage. We are aware of some use cases that are affected by it. GitHub is iterating on Copilot’s rate-limiting heuristics to ensure it doesn’t block legitimate use cases.
In case you experience repeated rate-limiting in Copilot, contact [GitHub Support](https://support.github.com).
## [Further reading](https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-common-issues-with-github-copilot#further-reading)
  * [GitHub and Trade Controls](https://docs.github.com/en/site-policy/other-site-policies/github-and-trade-controls)


