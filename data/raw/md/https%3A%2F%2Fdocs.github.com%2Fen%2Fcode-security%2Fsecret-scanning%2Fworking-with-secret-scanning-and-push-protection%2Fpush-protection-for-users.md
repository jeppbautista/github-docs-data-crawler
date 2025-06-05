  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secret scanning](https://docs.github.com/en/code-security/secret-scanning "Secret scanning")/
  * [Work with secret scanning](https://docs.github.com/en/code-security/secret-scanning/working-with-secret-scanning-and-push-protection "Work with secret scanning")/
  * [Push protection for users](https://docs.github.com/en/code-security/secret-scanning/working-with-secret-scanning-and-push-protection/push-protection-for-users "Push protection for users")


# Push protection for users
With push protection for users, you are automatically protected on all pushes to public repositories across GitHub.
## Who can use this feature?
Push protection for users is on by default on the following repository types:
  * Public repositories


## In this article
  * [About push protection for users](https://docs.github.com/en/code-security/secret-scanning/working-with-secret-scanning-and-push-protection/push-protection-for-users#about-push-protection-for-users)
  * [Disabling push protection for users](https://docs.github.com/en/code-security/secret-scanning/working-with-secret-scanning-and-push-protection/push-protection-for-users#disabling-push-protection-for-users)


## [About push protection for users](https://docs.github.com/en/code-security/secret-scanning/working-with-secret-scanning-and-push-protection/push-protection-for-users#about-push-protection-for-users)
Push protection for users automatically protects you from accidentally committing secrets to public repositories across GitHub.
When you try to push a secret to a public repository, GitHub blocks the push. If you believe it's safe to allow the secret, you have the option to bypass the block. Otherwise, you must remove the secret from the commit before pushing again. For more information on how to resolve a blocked push, see [Working with push protection in the GitHub UI](https://docs.github.com/en/code-security/secret-scanning/working-with-secret-scanning-and-push-protection/working-with-push-protection-in-the-github-ui) or [Working with push protection from the command line](https://docs.github.com/en/code-security/secret-scanning/working-with-secret-scanning-and-push-protection/working-with-push-protection-from-the-command-line), depending on whether you use the GitHub UI or the command line.
Push protection for users is always on by default. You can disable the feature at any time through your personal account settings. This may cause secrets to be accidentally leaked. For more information, see [Disabling push protection for users](https://docs.github.com/en/code-security/secret-scanning/working-with-secret-scanning-and-push-protection/push-protection-for-users#disabling-push-protection-for-users).
Push protection for users is different from _push protection for repositories and organizations_ , which is a secret scanning feature that must be enabled by a repository administrator or organization owner. With push protection for repositories and organizations, secret scanning blocks contributors from pushing secrets to a repository and generates an alert whenever a contributor bypasses the protection. For more information, see [About push protection](https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection).
With push protection for users, GitHub won't create an alert when you bypass the protection and push a secret to a public repository, unless the repository itself has secret scanning enabled. However, if the bypassed secret is a GitHub token, the token will be revoked and you will be notified by email.
For information on the secrets and service providers supported for push protection, see [Supported secret scanning patterns](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#supported-secrets).
## [Disabling push protection for users](https://docs.github.com/en/code-security/secret-scanning/working-with-secret-scanning-and-push-protection/push-protection-for-users#disabling-push-protection-for-users)
You can disable push protection for users through your personal account settings.
  1. In the upper-right corner of any page on GitHub, click your profile photo, then click 
  2. In the "Security" section of the sidebar, click 
  3. Under "User", to the right of "Push protection for yourself", click **Disable**.
![Screenshot of the "User" section of the "Code security and analysis" settings page. A button labeled "Disable" is outlined in dark orange.](https://docs.github.com/assets/cb-30958/images/help/security/push-protection-for-yourself.png)


