  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secure your organization](https://docs.github.com/en/code-security/securing-your-organization "Secure your organization")/
  * [Fix alerts at scale](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale "Fix alerts at scale")/
  * [Best practices](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/best-practice-fix-alerts-at-scale "Best practices")


# Best practices for fixing security alerts at scale
Guidance on how to create successful security campaigns that engage developers and help them grow their understanding of secure coding.
## Who can use this feature?
Organizations on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled
## In this article
  * [Elements of a successful security campaign](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/best-practice-fix-alerts-at-scale#elements-of-a-successful-security-campaign)
  * [Selecting security alerts for remediation](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/best-practice-fix-alerts-at-scale#selecting-security-alerts-for-remediation)
  * [Specifying campaign managers and contact links](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/best-practice-fix-alerts-at-scale#specifying-campaign-managers-and-contact-links)
  * [Creating issues for a campaign](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/best-practice-fix-alerts-at-scale#creating-issues-for-a-campaign)
  * [Combining security training with a security campaign](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/best-practice-fix-alerts-at-scale#combining-security-training-with-a-security-campaign)
  * [Providing AI support for learning about security vulnerabilities](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/best-practice-fix-alerts-at-scale#providing-ai-support-for-learning-about-security-vulnerabilities)
  * [Considerations in starting a security campaign and defining a deadline](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/best-practice-fix-alerts-at-scale#considerations-in-starting-a-security-campaign-and-defining-a-deadline)
  * [Next steps](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/best-practice-fix-alerts-at-scale#next-steps)


## [Elements of a successful security campaign](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/best-practice-fix-alerts-at-scale#elements-of-a-successful-security-campaign)
Successful security campaigns to fix alerts at scale have many features in common, including:
  * Selecting a related group of security alerts for remediation.
  * Using Copilot Autofix suggestions where possible to help developers remediate alerts faster and more effectively.
  * Making sure that the campaign managers are available for collaboration, reviews, and questions about fixes.
  * Providing access to educational information about the type of alerts included in the campaign.
  * Defining a realistic deadline for campaign, bearing in mind the number of alerts you aim to fix.
  * Publicizing the collaboration to developer teams and identifying the best way to engage them for your organization.


For information about the developer experience, see [Fixing alerts in a security campaign](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/fixing-alerts-in-security-campaign).
## [Selecting security alerts for remediation](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/best-practice-fix-alerts-at-scale#selecting-security-alerts-for-remediation)
Your first thought may be to identify all the most urgent alerts and create a security campaign to fix them. If your developers already have a good understanding of secure coding and are keen to remediate potential vulnerabilities, this could be a successful approach for your company. However, if you need to build up knowledge of secure coding and common vulnerabilities, you will benefit from a more stategic approach.
For example, if you have many alerts for cross-site scripting vulnerabilities, you could:
  * Create educational content for developers in a repository using resources from the OWASP Foundation, see [Cross Site Scripting (XSS)](https://owasp.org/www-community/attacks/xss/).
  * Create a campaign to remediate all alerts for this vulnerability, including a link to the educational content in the campaign description.
  * Hold a training session or other event to highlight this opportunity to gain confidence in secure coding while fixing real bugs.
  * Make sure that the security team members assigned to manage the campaign are available to review the pull requests created to fix the campaign alerts, collaborating as needed.


### [Using Copilot Autofix to help remediate security alerts](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/best-practice-fix-alerts-at-scale#using-copilot-autofix-to-help-remediate-security-alerts)
GitHub Copilot Autofix is an expansion of code scanning that provides users with targeted recommendations to help fix code scanning alerts. When you select alerts to include in a security campaign, you can preferentially include alerts that are eligible to be fixed with the help of GitHub Copilot Autofix using the `autofix:supported` filter.
### [Campaign filter templates](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/best-practice-fix-alerts-at-scale#campaign-filter-templates)
When you select alerts to include in a security campaign, you can use any of the filters on the security alerts page to define a subset of alerts. Alternatively, you can choose a campaign template to use one of the pre-defined filters for common needs, for example: "Cross-site scripting (CWE-79)."
### [Draft campaigns](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/best-practice-fix-alerts-at-scale#draft-campaigns)
It can be useful to create a draft campaign first, which lists the alerts that are set to be included in the campaign and the campaign details, so that you can collaborate on the scope of the campaign prior to publishing it. For guidance on creating a draft campaign, see [Creating and managing security campaigns](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/creating-managing-security-campaigns#create-a-campaign).
### [Limitations on security campaigns](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/best-practice-fix-alerts-at-scale#limitations-on-security-campaigns)
The following limitations are intended to encourage you to take a balanced and measured approach to remediating alerts in your code. An iterative approach, addressing a few targeted sets of alerts at a time, is likely to lead to a sustainable and long-term change in security posture.
  * A maximum of 10 active security campaigns at a time (no limits on closed campaigns).
  * Each campaign can contain up to 1000 alerts.


If you choose to create a campaign that exceeds these limits, alerts will be omitted to bring the campaign into line with the limits. Alerts in repositories with recent pushes are prioritized for inclusion in the campaign.
## [Specifying campaign managers and contact links](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/best-practice-fix-alerts-at-scale#specifying-campaign-managers-and-contact-links)
When you create a security campaign, you must select one or more "Campaign managers." A campaign manager must be either:
  * A user with the organization owner role, or the security manager role.
  * A member of a team with either the organization owner role, or the security manager role.


The names of the campaign managers are visible to developers when they take part in the campaign. To support communication between developers and the campaigns managers, you can also provide a contact link, such as a link to a GitHub Discussions or another communication channel, when you create a campaign.
If you want to increase the remediation rate for alerts and scale the knowledge of the security team, this is a key opportunity to build collaborative relationships with developers. Ideally, the campaign managers are available to answer questions and collaborate on difficult fixes via the contact link. Campaign managers should also be available to review pull requests for fixes over the whole course of the campaign.
## [Creating issues for a campaign](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/best-practice-fix-alerts-at-scale#creating-issues-for-a-campaign)
When you create a campaign, you can choose to automatically open a GitHub Issue in every repository involved in the campaign. This means that the work can be much more easily tracked, assigned, and managed on team project boards. What's more, when you update the details of the campaign, such as the contact link or due date, the issue body gets automatically updated with the latest information. When a campaign reaches its due date, or gets deleted or closed, a comment is automatically posted on the issue.
This can aid developer engagement by providing clear, up-to-date context directly within developers' existing workflows. For information on how to automate issue creation for campaigns, see [Creating and managing security campaigns](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/creating-managing-security-campaigns#create-a-campaign).
## [Combining security training with a security campaign](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/best-practice-fix-alerts-at-scale#combining-security-training-with-a-security-campaign)
If your security team already provides training for developers on secure coding, creating a campaign with alerts chosen to allow developers to use the skills from the training session is a great way to reinforce their learning. Even if you don't have a formal training program, it makes sense to provide information on the types of security vulnerabilities included in the campaign, examples of how to fix them, and how to test the fixes. This will simplify the role of the campaign manager as they will be able to direct developers to these resources for answers to basic questions.
The OWASP Foundation provides many resources for learning about the most common vulnerabilities and MITRE Corporation maintain a detailed list of common weaknesses, see [About the OWASP Foundation](https://owasp.org/about/) and [About CWE](https://cwe.mitre.org/about/index.html).
## [Providing AI support for learning about security vulnerabilities](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/best-practice-fix-alerts-at-scale#providing-ai-support-for-learning-about-security-vulnerabilities)
GitHub Copilot Autofix is automatically triggered to suggest a resolution for each security alert. However, developers will often want more information about why the original code is insecure and how to test that the fix is correct and doesn't break other components.
GitHub Copilot is an important tool for developers who have questions about secure coding, how to fix security alerts, and test their fix. Check that all developers in your organization have access to Copilot in both their IDE and GitHub, see [Granting access to Copilot for members of your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-access-to-github-copilot-in-your-organization/granting-access-to-copilot-for-members-of-your-organization).
## [Considerations in starting a security campaign and defining a deadline](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/best-practice-fix-alerts-at-scale#considerations-in-starting-a-security-campaign-and-defining-a-deadline)
As with any other project, it's important to define realistic timescales to avoid discouraging developers from participating in the security campaign. Unless your company is fixing security alerts as part of a larger campaign to reduce technical debt, most developers will not have time allocated to fixing alerts. You need to estimate remediation rates based on the time developers can find between scheduled tasks. It's also always worth checking on key company deadlines that developers may be working towards and checking national holidays.
## [Next steps](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/best-practice-fix-alerts-at-scale#next-steps)
  * [Creating and managing security campaigns](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/creating-managing-security-campaigns)


