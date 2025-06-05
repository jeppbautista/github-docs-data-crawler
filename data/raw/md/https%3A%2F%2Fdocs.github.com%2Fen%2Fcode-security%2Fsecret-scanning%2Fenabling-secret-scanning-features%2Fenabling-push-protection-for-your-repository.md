  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secret scanning](https://docs.github.com/en/code-security/secret-scanning "Secret scanning")/
  * [Enable features](https://docs.github.com/en/code-security/secret-scanning/enabling-secret-scanning-features "Enable features")/
  * [Enable push protection](https://docs.github.com/en/code-security/secret-scanning/enabling-secret-scanning-features/enabling-push-protection-for-your-repository "Enable push protection")


# Enabling push protection for your repository
With push protection, secret scanning blocks contributors from pushing secrets to a repository and generates an alert whenever a contributor bypasses the block.
## Who can use this feature?
Repository owners, organization owners, security managers, and users with the **admin** role
## In this article
  * [About enabling push protection](https://docs.github.com/en/code-security/secret-scanning/enabling-secret-scanning-features/enabling-push-protection-for-your-repository#about-enabling-push-protection)
  * [Enabling push protection for a repository](https://docs.github.com/en/code-security/secret-scanning/enabling-secret-scanning-features/enabling-push-protection-for-your-repository#enabling-push-protection-for-a-repository)
  * [Further reading](https://docs.github.com/en/code-security/secret-scanning/enabling-secret-scanning-features/enabling-push-protection-for-your-repository#further-reading)


## [About enabling push protection](https://docs.github.com/en/code-security/secret-scanning/enabling-secret-scanning-features/enabling-push-protection-for-your-repository#about-enabling-push-protection)
To enable push protection for a repository, you must first enable Secret Protection. You can then enable push protection in the repository's "Advanced Security" settings page following the steps outlined in this article.
You can additionally enable push protection for your own personal account, which prevents you from pushing secrets to _any_ public repository on GitHub. For more information, see [Push protection for users](https://docs.github.com/en/code-security/secret-scanning/working-with-secret-scanning-and-push-protection/push-protection-for-users).
If you're an organization owner, you can enable push protection for multiple repositories at a time using security configurations. For more information, see [About enabling security features at scale](https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/about-enabling-security-features-at-scale).
Organization owners, security managers, and repository administrators can also enable push protection for secret scanning via the API. For more information, see [REST API endpoints for repositories](https://docs.github.com/en/rest/repos#update-a-repository) and expand the "Properties of the `security_and_analysis` object" section.
## [Enabling push protection for a repository](https://docs.github.com/en/code-security/secret-scanning/enabling-secret-scanning-features/enabling-push-protection-for-your-repository#enabling-push-protection-for-a-repository)
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Security" section of the sidebar, click 
  4. Under "Secret Protection", to the right of "Push Protection", click **Enable**.


## [Further reading](https://docs.github.com/en/code-security/secret-scanning/enabling-secret-scanning-features/enabling-push-protection-for-your-repository#further-reading)
  * [Working with secret scanning and push protection](https://docs.github.com/en/code-security/secret-scanning/working-with-secret-scanning-and-push-protection)
  * [Excluding folders and files from secret scanning](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/excluding-folders-and-files-from-secret-scanning)
  * [About GitHub Advanced Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security)


