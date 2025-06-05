  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secret scanning](https://docs.github.com/en/code-security/secret-scanning "Secret scanning")/
  * [Enable features](https://docs.github.com/en/code-security/secret-scanning/enabling-secret-scanning-features "Enable features")/
  * [Enable validity checks](https://docs.github.com/en/code-security/secret-scanning/enabling-secret-scanning-features/enabling-validity-checks-for-your-repository "Enable validity checks")


# Enabling validity checks for your repository
Enabling validity checks on your repository helps you prioritize the remediation of alerts as it tells you if a secret is active or inactive.
## Who can use this feature?
Validity checks for partner patterns are available for the following repository types:
  * Organization-owned repositories on GitHub Team with [GitHub Secret Protection](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [About validity checks](https://docs.github.com/en/code-security/secret-scanning/enabling-secret-scanning-features/enabling-validity-checks-for-your-repository#about-validity-checks)
  * [Enabling validity checks](https://docs.github.com/en/code-security/secret-scanning/enabling-secret-scanning-features/enabling-validity-checks-for-your-repository#enabling-validity-checks)
  * [Further reading](https://docs.github.com/en/code-security/secret-scanning/enabling-secret-scanning-features/enabling-validity-checks-for-your-repository#further-reading)


## [About validity checks](https://docs.github.com/en/code-security/secret-scanning/enabling-secret-scanning-features/enabling-validity-checks-for-your-repository#about-validity-checks)
You can enable validity checks for secrets identified as service provider tokens for your repository. Once enabled, GitHub will periodically check the validity of a detected credential by sending the secret directly to the provider, as part of GitHub's secret scanning partnership program. To find out about our partner program, see [Secret scanning partner program](https://docs.github.com/en/code-security/secret-scanning/secret-scanning-partnership-program/secret-scanning-partner-program).
GitHub displays the validation status of the secret in the alert view, so you can see if the secret is `active`, `inactive`, or if the validation status is `unknown`. You can optionally perform an "on-demand" validity check for the secret in the alert view.
You can additionally choose to enable validity checks for partner patterns. Once enabled, GitHub will periodically check the validity of a detected credential by sending the secret directly to the provider, as part of GitHub's formal secret scanning partnership program. GitHub typically makes GET requests to check the validity of the credential, picks the least intrusive endpoints, and selects endpoints that don't return any personal information.
GitHub displays the validation status of the secret in the alert view.
You can filter by validation status on the alerts page, to help you prioritize which alerts you need to take action on.
GitHub typically makes GET requests to check the validity of the credential, picks the least intrusive endpoints, and selects endpoints that don't return any personal information.
For more information on using validity checks, see [Evaluating alerts from secret scanning](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts#checking-a-secrets-validity).
## [Enabling validity checks](https://docs.github.com/en/code-security/secret-scanning/enabling-secret-scanning-features/enabling-validity-checks-for-your-repository#enabling-validity-checks)
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Security" section of the sidebar, click 
  4. Under "Secret Protection", to the right of "Validity checks", click **Enable**.


You can also use the REST API to enable validity checks for partner patterns for your repository. For more information, see [REST API endpoints for repositories](https://docs.github.com/en/rest/repos/repos#update-a-repository).
Alternatively, organization owners and enterprise administrators can enable the feature for all repositories in the organization or enterprise. For more information on enabling at the organization-level, see [Creating a custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/creating-a-custom-security-configuration). For more information on enabling at the enterprise-level, see [Creating a custom security configuration for your enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-code-security/securing-your-enterprise/creating-a-custom-security-configuration-for-your-enterprise).
## [Further reading](https://docs.github.com/en/code-security/secret-scanning/enabling-secret-scanning-features/enabling-validity-checks-for-your-repository#further-reading)
  * [Managing alerts from secret scanning](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning)


