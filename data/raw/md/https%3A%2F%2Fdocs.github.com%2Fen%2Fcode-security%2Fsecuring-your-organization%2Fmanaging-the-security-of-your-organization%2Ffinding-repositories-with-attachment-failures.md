  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secure your organization](https://docs.github.com/en/code-security/securing-your-organization "Secure your organization")/
  * [Manage organization security](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization "Manage organization security")/
  * [Find attachment failures](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/finding-repositories-with-attachment-failures "Find attachment failures")


# Finding and fixing configuration attachment failures
You can identify any repositories where the security configuration could not be attached, and follow guidance to remediate the problem.
## Who can use this feature?
Organization owners, security managers, and organization members with the **admin** role
## In this article
  * [Finding and remediating attachment failures](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/finding-repositories-with-attachment-failures#finding-and-remediating-attachment-failures)
  * [Further reading](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/finding-repositories-with-attachment-failures#further-reading)


## [Finding and remediating attachment failures](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/finding-repositories-with-attachment-failures#finding-and-remediating-attachment-failures)
When you apply a configuration to a group of repositories, you may see a banner reporting that there was an attachment failure for some repositories. This happens when there is a conflict between the existing repository settings and the configuration that you applied.
When an attachment failure happens:
  * Only some of the settings in the security configuration are applied to affected repositories.
  * Any changes you later make to the security configuration will not be inherited by the affected repositories.


On the security configuration settings page, under "Apply configurations", you will see a banner advising how many repositories in your organization have an attachment failure, and an overview of the reason(s) for the failure.
Click the link in the banner display, or alternatively, filter the list of repositories by `config-status:failed`, to see the list of affected repositories and to source additional guidance on how to remediate the attachment failure for a specific repository.
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Under your organization name, click **Settings**.
![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](https://docs.github.com/assets/cb-49309/images/help/discussions/org-settings-global-nav-update.png)
  3. In the "Security" section of the sidebar, select the **Configurations**.
  4. In the "Apply configurations" section, filter by `config-status:failed`.
  5. From the results list, for the repository you're interested in, click 
  6. In the dialog box, review the information and follow the remediation guidance.


## [Further reading](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/finding-repositories-with-attachment-failures#further-reading)
  * [A repository is using advanced setup for code scanning](https://docs.github.com/en/code-security/securing-your-organization/troubleshooting-security-configurations/a-repository-is-using-advanced-setup-for-code-scanning)
  * [Not enough GitHub Advanced Security licenses](https://docs.github.com/en/code-security/securing-your-organization/troubleshooting-security-configurations/not-enough-github-advanced-security-licenses)


