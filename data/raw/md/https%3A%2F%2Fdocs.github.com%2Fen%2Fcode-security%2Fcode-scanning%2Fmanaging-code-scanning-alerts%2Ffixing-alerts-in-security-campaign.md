  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Manage alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts "Manage alerts")/
  * [Fix alerts in campaign](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/fixing-alerts-in-security-campaign "Fix alerts in campaign")


# Fixing alerts in a security campaign
Learn how to find and fix alerts in a security campaign.
## Who can use this feature?
Users with **write** access
Organizations on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled
## In this article
  * [Viewing alerts in a security campaign](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/fixing-alerts-in-security-campaign#viewing-alerts-in-a-security-campaign)
  * [Fixing alerts in a security campaign](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/fixing-alerts-in-security-campaign#fixing-alerts-in-a-security-campaign)
  * [Using GitHub Copilot Chat for secure coding](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/fixing-alerts-in-security-campaign#using-github-copilot-chat-for-secure-coding)


## [Viewing alerts in a security campaign](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/fixing-alerts-in-security-campaign#viewing-alerts-in-a-security-campaign)
When a campaign targets security alerts in a repository that you have write access to, you can navigate to the list of repository alerts in the campaign.
  * Display the **Security** tab for the repository and click one of the campaigns under "Campaigns" in the sidebar.
  * If you have enabled email notifications for "All activity" or "Security alerts" in the repository, click **View security campaign** in the campaign email.
  * If you have write access to more than one repository in the organization, display the **Security** tab for the organization and click one of the campaigns under "Campaigns" in the sidebar.


This view shows the alerts in the current repository for a campaign called "SQL injection (CWE-89)" (highlighted gray) that is managed by "octocat" (outlined in dark orange).
![Screenshot of repository campaign view with "SQL injection \(CWE-89\)" campaign displayed and the "Campaign manager" outlined in dark orange.](https://docs.github.com/assets/cb-176856/images/help/security/builder-sec-campaign.png)
## [Fixing alerts in a security campaign](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/fixing-alerts-in-security-campaign#fixing-alerts-in-a-security-campaign)
If you want to see the code that triggered the security alert and the suggested fix, click on the alert name to show the alert view.
  1. When you are ready to work on one or more security alerts, check that no one else is working on those alerts already. In the campaign view, git icons are displayed on alerts where a fix may already be in progress. Click an icon to display the linked work:
  2. In the campaign view for the repository, select the alerts that you want to fix.
  3. Connect the security alerts to a working branch:
     * If at least one "Autofix" suggestion is available for the selected alerts, click **Commit autofix** and commit the changes either to a new branch or to an existing branch.
     * If no autofix suggestions are available for the selected alerts, click **Create new branch** to create a new branch where you will work on fixing the alerts.
  4. When you have finished fixing the alerts and testing your solutions, create a pull request for your changes and request a review from the campaign manager.


If you have write permission for more than one repository in the campaign, click the link in the "Campaign progress" box in your repository to show the organization-level view of the campaign. When you open a repository from this view, the campaign alerts view is displayed.
## [Using GitHub Copilot Chat for secure coding](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/fixing-alerts-in-security-campaign#using-github-copilot-chat-for-secure-coding)
If you have access to Copilot Chat then you can ask the AI questions about the vulnerability, the suggested fix, and how to test that the fix is comprehensive.
Copilot's ability to answer natural language questions like these in a repository context is optimized when the semantic code search index for the repository is up to date. For more information, see [Indexing repositories for Copilot Chat](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-github-copilot-features-in-your-organization/indexing-repositories-for-copilot-chat).
