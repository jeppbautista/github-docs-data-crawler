  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Troubleshooting code scanning](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning "Troubleshooting code scanning")/
  * [Cannot enable CodeQL in a private repository](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/cannot-enable-codeql-in-a-private-repository "Cannot enable CodeQL in a private repository")


# Cannot enable CodeQL in a private repository
GitHub Code Security must be enabled in order to use code scanning on private repositories.
If you are on a **GitHub Free** or **GitHub Pro** plan, you can only use code scanning on repositories that are publicly available. To enable code scanning for private or internal repositories, you must upgrade to GitHub Team or GitHub Enterprise with GitHub Code Security and enable Code Security for the repository. For more information, see [GitHub’s plans](https://docs.github.com/en/get-started/learning-about-github/githubs-products#github-team) and [About GitHub Advanced Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security).
## [Confirm whether GitHub Code Security is enabled](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/cannot-enable-codeql-in-a-private-repository#confirm-whether-github-code-security-is-enabled)
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Security" section of the sidebar, click 
  4. On the settings page, scroll down to "Code Security."
  5. If there is an associated and active **Enable** button, Code Security is available for this repository but not yet enabled.
  6. If use of GitHub Code Security is blocked by a policy, "**Enable** button.
!["Screenshot of the Advanced Security" setting. The disabled option is highlighted in dark orange.](https://docs.github.com/assets/cb-81713/images/help/repository/ghas-enterprise-policy-block.png)


### [Requesting access to GitHub Code Security](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/cannot-enable-codeql-in-a-private-repository#requesting-access-to-github-code-security)
  1. In the "Code Security" settings, click the enterprise or organization name to display a list of users with access to edit the policy that controls access to GitHub Code Security. For more information, see [Enforcing policies for code security and analysis for your enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-code-security-and-analysis-for-your-enterprise#enforcing-a-policy-for-the-availability-of-advanced-security-in-your-enterprises-organizations).
  2. Follow your company's policy for requesting access to additional features.


### [Enabling GitHub Code Security](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/cannot-enable-codeql-in-a-private-repository#enabling-github-code-security)
  1. Open the "Code security" settings page.
  2. Next to the "Code Security" feature, click **Enable**.
  3. Rerun code scanning.


