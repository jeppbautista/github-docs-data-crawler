  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Getting started](https://docs.github.com/en/code-security/getting-started "Getting started")/
  * [Add a security policy](https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository "Add a security policy")


# Adding a security policy to your repository
You can give instructions for how to report a security vulnerability in your project by adding a security policy to your repository.
## In this article
  * [About security policies](https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository#about-security-policies)
  * [Adding a security policy to your repository](https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository#adding-a-security-policy-to-your-repository)
  * [Further reading](https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository#further-reading)


## [About security policies](https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository#about-security-policies)
To give people instructions for reporting security vulnerabilities in your project, you can add a `SECURITY.md` file to your repository's root, `docs`, or `.github` folder. Adding this file to this part(s) of your repository automatically creates a row with a description where people can review it. When someone creates an issue in your repository, they will see a link to your project's security policy.
You can create a default security policy for your organization or personal account. For more information, see [Creating a default community health file](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file).
To help people find your security policy, you can link to your `SECURITY.md` file from other places in your repository, such as your `README` file. For more information, see [About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes).
After someone reports a security vulnerability in your project, you can use GitHub Security Advisories to disclose, fix, and publish information about the vulnerability. For more information about the process of reporting and disclosing vulnerabilities in GitHub, see [About coordinated disclosure of security vulnerabilities](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/about-coordinated-disclosure-of-security-vulnerabilities#about-reporting-and-disclosing-vulnerabilities-in-projects-on-github). For more information about repository security advisories, see [About repository security advisories](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/about-repository-security-advisories).
You can also join [GitHub Security Lab](https://securitylab.github.com/) to browse security-related topics and contribute to security tools and projects.
For an example of a real `SECURITY.md` file, see <https://github.com/electron/electron/blob/main/SECURITY.md>.
## [Adding a security policy to your repository](https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository#adding-a-security-policy-to-your-repository)
  1. On GitHub, navigate to the main page of the repository.
  2. Under the repository name, click **Security**. 
![Screenshot of a repository header showing the tabs. The "Security" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-17801/images/help/repository/security-tab.png)
  3. In the left sidebar, under "Reporting", click 
  4. Click **Start setup**.
  5. In the new `SECURITY.md` file, add information about supported versions of your project and how to report a vulnerability.
  6. Click **Commit changes...**
  7. In the "Commit message" field, type a short, meaningful commit message that describes the change you made to the file. You can attribute the commit to more than one author in the commit message. For more information, see [Creating a commit with multiple authors](https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/creating-a-commit-with-multiple-authors).
  8. If you have more than one email address associated with your account on GitHub, click the email address drop-down menu and select the email address to use as the Git author email address. Only verified email addresses appear in this drop-down menu. If you enabled email address privacy, then a no-reply will be the default commit author email address. For more information about the exact form the no-reply email address can take, see [Setting your commit email address](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address).
![Screenshot of a GitHub pull request showing a dropdown menu with options to choose the commit author email address. octocat@github.com is selected.](https://docs.github.com/assets/cb-72047/images/help/repository/choose-commit-email-address.png)
  9. Below the commit message fields, decide whether to add your commit to the current branch or to a new branch. If your current branch is the default branch, you should choose to create a new branch for your commit and then create a pull request. For more information, see [Creating a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).
![Screenshot of a GitHub pull request showing a radio button to commit directly to the main branch or to create a new branch. New branch is selected.](https://docs.github.com/assets/cb-27122/images/help/repository/choose-commit-branch.png)
  10. Click **Commit changes** or **Propose changes**.


## [Further reading](https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository#further-reading)
  * [Quickstart for securing your repository](https://docs.github.com/en/code-security/getting-started/securing-your-repository)
  * [Setting up your project for healthy contributions](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions)
  * [GitHub Security Lab](https://securitylab.github.com/)


