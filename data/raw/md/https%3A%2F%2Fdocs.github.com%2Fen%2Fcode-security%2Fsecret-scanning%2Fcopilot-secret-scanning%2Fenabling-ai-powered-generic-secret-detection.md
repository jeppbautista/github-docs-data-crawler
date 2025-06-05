  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secret scanning](https://docs.github.com/en/code-security/secret-scanning "Secret scanning")/
  * [Copilot secret scanning](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning "Copilot secret scanning")/
  * [Enable generic secret detection](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/enabling-ai-powered-generic-secret-detection "Enable generic secret detection")


# Enabling Copilot secret scanning's generic secret detection
You can enable generic secret detection for your repository or organization. Alerts for generic secrets, such as passwords, are displayed in a separate list on the secret scanning alerts page.
## Who can use this feature?
Repository owners, organization owners, security managers, and users with the **admin** role
## In this article
  * [Enabling generic secret detection](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/enabling-ai-powered-generic-secret-detection#enabling-generic-secret-detection)
  * [Further reading](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/enabling-ai-powered-generic-secret-detection#further-reading)


## [Enabling generic secret detection](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/enabling-ai-powered-generic-secret-detection#enabling-generic-secret-detection)
You can enable generic secret detection in the security settings page of your repository or organization.
You do not need a subscription to GitHub Copilot to use Copilot secret scanning's generic secret detection. Copilot secret scanning features are available to repositories owned by organizations and enterprises with GitHub Secret Protection enabled.
### [Enabling generic secret detection for your repository](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/enabling-ai-powered-generic-secret-detection#enabling-generic-secret-detection-for-your-repository)
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Security" section of the sidebar, click 
  4. Under "Secret Protection", to the right of "Scan for generic passwords", click **Enable**.


### [Enabling generic secret detection for your organization](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/enabling-ai-powered-generic-secret-detection#enabling-generic-secret-detection-for-your-organization)
You must configure generic secret detection for your organization using a custom security configuration. You can then apply the security configuration to all (or selected) repositories in your organization.
  1. Create a new custom security configuration, or edit an existing one. See [Creating a custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/creating-a-custom-security-configuration#creating-a-custom-security-configuration).
  2. When creating the custom security configuration, ensure that "Secret Protection" is set to **Enabled** , and that the dropdown menu for "Scan for generic secrets" is also set to **Enabled**.
  3. Apply the custom security configuration to one or more repositories. For more information, see [Applying a custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/meeting-your-specific-security-needs-with-custom-security-configurations/applying-a-custom-security-configuration).


For information on how to view alerts for generic secrets that have been detected using AI, see [Viewing and filtering alerts from secret scanning](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/viewing-alerts).
## [Further reading](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/enabling-ai-powered-generic-secret-detection#further-reading)
  * [Responsible detection of generic secrets with Copilot secret scanning](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-generic-secrets)
  * [About secret scanning](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning)


