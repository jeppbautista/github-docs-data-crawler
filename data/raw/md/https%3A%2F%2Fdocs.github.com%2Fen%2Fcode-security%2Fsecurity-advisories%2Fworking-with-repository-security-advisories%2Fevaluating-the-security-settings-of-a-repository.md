  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Security advisories](https://docs.github.com/en/code-security/security-advisories "Security advisories")/
  * [Repository security advisories](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories "Repository security advisories")/
  * [Evaluate repository security](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/evaluating-the-security-settings-of-a-repository "Evaluate repository security")


# Evaluating the security settings of a repository
Security researchers can assess the security settings of a public repository, suggest a security policy and report a vulnerability.
## Who can use this feature?
**Anyone** can:
  * View a public repository's security settings.
  * Contact the repository maintainers regarding a security issue.


## In this article
  * [About evaluating a repository's security settings](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/evaluating-the-security-settings-of-a-repository#about-evaluating-a-repositorys-security-settings)
  * [Suggesting a security policy for a repository](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/evaluating-the-security-settings-of-a-repository#suggesting-a-security-policy-for-a-repository)
  * [Reporting a vulnerability in a repository](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/evaluating-the-security-settings-of-a-repository#reporting-a-vulnerability-in-a-repository)


## [About evaluating a repository's security settings](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/evaluating-the-security-settings-of-a-repository#about-evaluating-a-repositorys-security-settings)
Evaluating a public repository's security settings can help security researchers understand the repository's security posture. This information can help you decide whether to engage with the repository maintainers, for example, by reporting a vulnerability in the repository.
If a repository is public, high level information about the repository's security settings is available to anyone. For example, you can see whether the repository has a security policy, and whether private vulnerability reporting is enabled. You can also view published and closed security advisories for the repository. If no security policy is associated with a repository, you can suggest one. If the repository has private vulnerability reporting enabled, you can privately report security vulnerabilities directly to repository maintainers.
If you have admin permissions to the repository, and the repository is owned by an organization, you can see more detailed information about the repository's security settings through the security overview. For more information on the security overview, see [About security overview](https://docs.github.com/en/code-security/security-overview/about-security-overview).
If a repository is private, you can only see the security settings if you have admin permissions to the repository or have been granted special security permissions covering the repository, for example, as an organization-wide security manager.
If you would like to evaluate the security posture of repositories at scale, you can use the API to check whether or not some security settings are enabled for repositories, such as private vulnerability reporting. For more information, see [REST API endpoints for repositories](https://docs.github.com/en/rest/repos/repos#check-if-private-vulnerability-reporting-is-enabled-for-a-repository).
## [Suggesting a security policy for a repository](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/evaluating-the-security-settings-of-a-repository#suggesting-a-security-policy-for-a-repository)
If you do not have admin or security permissions for a public repository, you can still suggest a security policy to the repository maintainers if one doesn't already exist. The repository maintainers can then choose to accept or reject your suggestion. If the repository maintainers accept your suggestion, the security policy will be associated with the repository.
  1. On GitHub, navigate to the main page of the repository.
  2. Under the repository name, click **Security**. 
![Screenshot of a repository header showing the tabs. The "Security" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-17801/images/help/repository/security-tab.png)
  3. If the repository has a security policy, it will be displayed. If no security policy is associated with the repository, click **Suggest a policy**.
  4. A SECURITY.md file will be created in the repository's default branch. The file will contain a template for a security policy. You can edit the file to add your suggested security policy.
  5. When you are done, click **Commit changes**.
  6. Fill out the **Commit changes** dialog. 
     * Under "Commit message", enter a commit message.
     * Optionally, under "Extended description", describe the changes being made.
     * Select "Create a new branch for this commit and start a pull request"
     * Click **Commit changes**.
  7. Click **Create pull request**.
  8. Optionally, leave a comment.
  9. Click **Create pull request**.


## [Reporting a vulnerability in a repository](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/evaluating-the-security-settings-of-a-repository#reporting-a-vulnerability-in-a-repository)
If you do not have admin or security permissions for a public repository, you can still privately report a security vulnerability to repository maintainers if private vulnerability reporting is enabled. The repository maintainers can then choose to accept or reject your report. If the repository maintainers accept your report, a security advisory will be created for the repository.
If the repository doesn't have private vulnerability reporting enabled, you need to initiate the reporting process by following the instructions in the security policy for the repository, or create an issue asking the maintainers for a preferred security contact. For more information, see [About coordinated disclosure of security vulnerabilities](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/about-coordinated-disclosure-of-security-vulnerabilities#about-reporting-and-disclosing-vulnerabilities-in-projects-on-github).
  1. On GitHub, navigate to the main page of the repository.
  2. Under the repository name, click **Security**. 
![Screenshot of a repository header showing the tabs. The "Security" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-17801/images/help/repository/security-tab.png)
  3. Click **Report a vulnerability** to open the advisory form.
  4. Fill in the advisory details form.
In this form, only the title and description are mandatory. (In the general draft security advisory form, which the repository maintainer initiates, specifying the ecosystem is also required.) However, we recommend security researchers provide as much information as possible on the form so that the maintainers can make an informed decision about the submitted report. You can adopt the template used by our security researchers from the GitHub Security Lab, which is available on the [`github/securitylab` repository](https://github.com/github/securitylab/blob/main/docs/report-template.md).
For more information about the fields available and guidance on filling in the form, see [Creating a repository security advisory](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/creating-a-repository-security-advisory) and [Best practices for writing repository security advisories](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/best-practices-for-writing-repository-security-advisories).
  5. At the bottom of the form, click **Submit report**. GitHub will display a message letting you know that maintainers have been notified and that you have a pending credit for this security advisory.
When the report is submitted, GitHub automatically adds the reporter of the vulnerability as a collaborator and as a credited user on the proposed advisory.
  6. Optionally, click **Start a temporary private fork** if you want to start to fix the issue. Note that only the repository maintainer can merge changes from that private fork into the parent repository.
![Screenshot of the bottom of a security advisory. A button, labeled "Start a temporary fork" is outlined in dark orange.](https://docs.github.com/assets/cb-51900/images/help/security/advisory-start-a-temporary-private-fork-button.png)


