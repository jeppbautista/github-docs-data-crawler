  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Manage alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts "Manage alerts")/
  * [Best practices for campaigns](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/best-practices-for-participating-in-a-security-campaign "Best practices for campaigns")


# Best practices for participating in a security campaign
Learn how you can successfully take part in a security campaign and how it can benefit your career as well as your code.
## Who can use this feature?
Users with **write** access
Organizations on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled
## In this article
  * [What is a security campaign](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/best-practices-for-participating-in-a-security-campaign#what-is-a-security-campaign)
  * [What are the benefits of participating in a campaign](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/best-practices-for-participating-in-a-security-campaign#what-are-the-benefits-of-participating-in-a-campaign)
  * [Stay informed](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/best-practices-for-participating-in-a-security-campaign#stay-informed)
  * [Seek context](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/best-practices-for-participating-in-a-security-campaign#seek-context)
  * [Group similar alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/best-practices-for-participating-in-a-security-campaign#group-similar-alerts)
  * [Leverage Copilot](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/best-practices-for-participating-in-a-security-campaign#leverage-copilot)
  * [Ask questions](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/best-practices-for-participating-in-a-security-campaign#ask-questions)
  * [Next steps](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/best-practices-for-participating-in-a-security-campaign#next-steps)


## [What is a security campaign](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/best-practices-for-participating-in-a-security-campaign#what-is-a-security-campaign)
A security campaign is a group of security alerts, detected in the default branches of repositories, chosen by an organization owner or security manager for remediation.
You can take part in a security campaign by fixing one or more of the alerts included in the campaign.
## [What are the benefits of participating in a campaign](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/best-practices-for-participating-in-a-security-campaign#what-are-the-benefits-of-participating-in-a-campaign)
In addition to the benefit of removing an important security problem from your organization's codebase, alerts in a security campaign have several other benefits compared with fixing another alert in your repository.
  * You have a campaign manager on the security team to collaborate with and a specific contact link for discussing campaign activities.
  * You know that you are fixing a security alert that is important to the company.
  * Potentially, you may have access to targeted training materials.
  * You don't need to request a GitHub Copilot Autofix suggestion, it is already available as a starting point.
  * If you have access to GitHub Copilot Chat, you can ask questions about the alert and the suggested fix.
  * You are improving and demonstrating your knowledge of secure coding.


Adopting a few key best practices can help you participate successfully in a campaign.
## [Stay informed](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/best-practices-for-participating-in-a-security-campaign#stay-informed)
### [Notification settings](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/best-practices-for-participating-in-a-security-campaign#notification-settings)
To receive email updates about security campaigns in repositories you have write access to, make sure that you:
  * **Watch** all repositories that you have write access to.
  * **Subscribe** to notifications for "All activity" or "Security alerts".


### [View campaign details](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/best-practices-for-participating-in-a-security-campaign#view-campaign-details)
When you open the **Security** tab for a repository with one or more campaign alerts, you can see the campaign name in the sidebar of the view. Click the campaign name to see the list of alerts included in the campaign and summary information on how the campaign is progressing.
### [Campaign-generated GitHub Issues](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/best-practices-for-participating-in-a-security-campaign#campaign-generated-github-issues)
Some campaigns automatically create GitHub Issues for each repository which details the campaign managers, contact URL, and due date.
You can use this issue to plan and track campaign work as part of your usual workflows, such as:
  * Adding the issue to project boards
  * Adding assignees
  * Creating sub-issues or tasklists


## [Seek context](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/best-practices-for-participating-in-a-security-campaign#seek-context)
Your security team may provide you with specific training ahead of participating in a campaign, so that you feel equipped to address the alerts included in the campaign.
If no formal training program is available, you can request that the campaign manager shares information on:
  * Types of security vulnerabilities included in the campaign
  * Examples of how to fix them
  * How to test the fixes


In addition, there are external resources for understanding common security issues:
  * The **OWASP Foundation** provides many resources for learning about the most common vulnerabilities, see [About the OWASP Foundation](https://owasp.org/about/).
  * The **MITRE Corporation** maintains a detailed list of common weaknesses, see [About CWE](https://cwe.mitre.org/about/index.html).


## [Group similar alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/best-practices-for-participating-in-a-security-campaign#group-similar-alerts)
When fixing security alerts as part of a campaign, it may be helpful to group and fix similar alerts together. By doing so, you can develop a deeper understanding of the underlying issue. As you gain confidence and efficiency in resolving a specific type of alert, it makes it easier and faster for you to resolve subsequent alerts.
## [Leverage Copilot](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/best-practices-for-participating-in-a-security-campaign#leverage-copilot)
### [Copilot Autofix](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/best-practices-for-participating-in-a-security-campaign#copilot-autofix)
Copilot Autofix is automatically triggered for alerts that are included in a campaign, meaning that where possible, fixes are automatically generated for you. You can commit the suggested fix to resolve the alert and then verify that continuous integration testing (CI) for the codebase is still passing. See [Fixing alerts in a security campaign](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/fixing-alerts-in-security-campaign).
### [Copilot Chat](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/best-practices-for-participating-in-a-security-campaign#copilot-chat)
You can ask Copilot Chat for help in understanding the vulnerability, the suggested fix, and how to test that the fix is comprehensive. To access Copilot Chat, navigate to <https://github.com/copilot>.
Alternatively, when viewing a specific alert, in the top right corner of the page, click the Copilot Chat icon (
For example:
Text```
Explain how this alert introduces a vulnerability into the code.


```
```

Explain how this alert introduces a vulnerability into the code.


```

If you don't already have access to Copilot Chat through your organization, you can sign up to GitHub Copilot Free. For more information, see [Getting started with a Copilot plan](https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/managing-copilot-free/accessing-github-copilot-free).
## [Ask questions](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/best-practices-for-participating-in-a-security-campaign#ask-questions)
A security campaign will generally include a contact URL, which might link you to the campaign manager, an open forum (such as a GitHub Discussion), or a website of resources. You should use this space to ask questions about the campaign or specific alerts, find useful resources, and share knowledge.
To find the contact URL:
  1. Open the **Security** tab for your repository.
  2. On the left sidebar, click the name of the campaign you are participating in.
  3. On the campaign tracking page, to the right of the campaign manager's name, click 


## [Next steps](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/best-practices-for-participating-in-a-security-campaign#next-steps)
  * [Fixing alerts in a security campaign](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/fixing-alerts-in-security-campaign)


