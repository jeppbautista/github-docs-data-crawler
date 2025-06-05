  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Troubleshooting code scanning](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning "Troubleshooting code scanning")/
  * [Code Security must be enabled](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/advanced-security-must-be-enabled "Code Security must be enabled")


# Error: "GitHub Code Security or GitHub Advanced Security must be enabled for this repository to use code scanning"
If you see this error, make sure that GitHub Code Security is enabled.
## In this article
  * [About this error](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/advanced-security-must-be-enabled#about-this-error)
  * [Confirming the cause of the error](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/advanced-security-must-be-enabled#confirming-the-cause-of-the-error)
  * [Fixing the problem](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/advanced-security-must-be-enabled#fixing-the-problem)


## [About this error](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/advanced-security-must-be-enabled#about-this-error)
```
GitHub Code Security or GitHub Advanced Security must be enabled for this repository to use code scanning
403: GitHub Code Security or GitHub Advanced Security is not enabled

```

This error is reported if you try to run code scanning in a repository where GitHub Code Security is not enabled or where use of this feature is blocked by a policy.
You will only see this error for repositories with private or internal visibility. GitHub Code Security is enabled by default for all public repositories.
If you are on a **GitHub Free** or **GitHub Pro** plan, you can only use code scanning on repositories that are publicly available. To enable code scanning for private or internal repositories, you must upgrade to GitHub Team or GitHub Enterprise with GitHub Code Security and enable Code Security for the repository. For more information, see [GitHub’s plans](https://docs.github.com/en/get-started/learning-about-github/githubs-products#github-team) and [About GitHub Advanced Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security).
## [Confirming the cause of the error](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/advanced-security-must-be-enabled#confirming-the-cause-of-the-error)
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Security" section of the sidebar, click 
  4. On the settings page, scroll down to "Code Security."
  5. If there is an associated and active **Enable** button, GitHub Code Security is available for this repository but not yet enabled.
  6. If use of GitHub Code Security is blocked by a policy, "**Enable** button.
!["Screenshot of the Advanced Security" setting. The disabled option is highlighted in dark orange.](https://docs.github.com/assets/cb-81713/images/help/repository/ghas-enterprise-policy-block.png)


## [Fixing the problem](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/advanced-security-must-be-enabled#fixing-the-problem)
If GitHub Code Security is available to your repository, you can enable it on the settings page.
If GitHub Code Security is blocked by a policy, you first need to request access.
### [Requesting access to GitHub Code Security](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/advanced-security-must-be-enabled#requesting-access-to-github-code-security)
  1. In the "Advanced Security" settings, click the enterprise name to display a list of users with access to edit the policy that controls access to Code Security products. For more information, see [Enforcing policies for code security and analysis for your enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-code-security-and-analysis-for-your-enterprise#enforcing-a-policy-for-the-use-of-github-advanced-security-in-your-enterprises-organizations).
  2. Follow your company's policy for requesting access to additional features.


### [Enabling GitHub Code Security](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/advanced-security-must-be-enabled#enabling-github-code-security)
  1. Open the "Code security" settings page.
  2. Next to the "Code Security" feature, click **Enable**.
  3. Rerun code scanning.


