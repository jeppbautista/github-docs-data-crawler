  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secret scanning](https://docs.github.com/en/code-security/secret-scanning "Secret scanning")/
  * [Manage alerts](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning "Manage alerts")/
  * [Resolve alerts](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/resolving-alerts "Resolve alerts")


# Resolving alerts from secret scanning
After reviewing the details of a secret scanning alert, you should fix and then close the alert.
## Who can use this feature?
Repository owners, organization owners, security managers, and users with the **admin** role
## In this article
  * [Fixing alerts](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/resolving-alerts#fixing-alerts)
  * [Closing alerts](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/resolving-alerts#closing-alerts)
  * [Next steps](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/resolving-alerts#next-steps)


## [Fixing alerts](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/resolving-alerts#fixing-alerts)
Once a secret has been committed to a repository, you should consider the secret compromised. GitHub recommends the following actions for compromised secrets:
  * Verify that the secret committed to GitHub is valid. **Applies to GitHub tokens only**. See [Checking a secret's validity](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts#checking-a-secrets-validity).See [Performing an on-demand validity check](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts#performing-an-on-demand-validity-check).
  * For secrets detected in private repositories, report the leaked secret to GitHub, who will treat it like any publicly leaked secret and revoke it. **Applies to GitHub personal access tokens only**. See [Reporting a leaked secret](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/resolving-alerts#reporting-a-leaked-secret).
  * Review and update any services that use the old token. For GitHub personal access tokens, delete the compromised token and create a new token. See [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).
  * Depending on the secret provider, check your security logs for any unauthorized activity.


### [Reporting a leaked secret](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/resolving-alerts#reporting-a-leaked-secret)
Reporting a privately exposed secret to GitHub is in public preview and subject to change. The feature is currently only available for GitHub personal access tokens (v1 and v2).
If a secret is detected in a **public** repository on GitHub and the secret also matches a supported partner pattern, the potential secret is **automatically reported** to the service provider. For details of all supported partner patterns, see [Supported secret scanning patterns](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#supported-secrets).
For secrets detected in **private** repositories, anyone who can view secret scanning alerts for a repository can choose to report the privately exposed secret directly to GitHub.
By reporting the secret, the token provider will treat the privately exposed secret as if it had been publicly leaked. This means the token provider may revoke the secret, so you should first consider reviewing and updating any services that use the secret. If possible, you should also consider notifying the token owner before reporting the token, so that the token owner is aware that the secret may get revoked.
You will only see the option to report a privately exposed secret to GitHub if the following conditions are met:
  * The secret is a GitHub personal access token.
  * The secret's validity has not been confirmed, or the secret's validity has been confirmed as `active`.


  1. On GitHub, navigate to the main page of the repository.
  2. Under the repository name, click **Security**. 
![Screenshot of a repository header showing the tabs. The "Security" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-17801/images/help/repository/security-tab.png)
  3. In the left sidebar, under "Vulnerability alerts", click **Secret scanning**.
  4. From the alert list, click the alert you want to view.
  5. In the alert view for the leaked secret, click **Report leak**.
In order to prevent breaking workflows, consider first rotating the secret before continuing, as disclosing it could lead to the secret being revoked. If possible, you should also reach out to the token owner to let them know about the leak and coordinate a remediation plan.
  6. Review the information in the dialog box, then click **I understand the consequence, report this secret**.


## [Closing alerts](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/resolving-alerts#closing-alerts)
Secret scanning doesn't automatically close alerts when the corresponding token has been removed from the repository. You must manually close these alerts in the alert list on GitHub.
  1. On GitHub, navigate to the main page of the repository.
  2. Under the repository name, click **Security**. 
![Screenshot of a repository header showing the tabs. The "Security" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-17801/images/help/repository/security-tab.png)
  3. In the left sidebar, under "Vulnerability alerts", click **Secret scanning**.
  4. Under "Secret scanning", click the alert you want to view.
  5. To dismiss an alert, select the "Close as" dropdown menu and click a reason for resolving an alert.
![Screenshot of a secret scanning alert. A dropdown menu, titled "Close as", is expanded and highlighted in a dark orange outline.](https://docs.github.com/assets/cb-332927/images/help/repository/secret-scanning-dismiss-alert-web-ui-link-partner-documentation.png)
  6. Optionally, in the "Comment" field, add a dismissal comment. The dismissal comment will be added to the alert timeline and can be used as justification during auditing and reporting. You can view the history of all dismissed alerts and dismissal comments in the alert timeline. You can also retrieve or set a comment by using the Secret scanning API. The comment is contained in the `resolution_comment` field. For more information, see [REST API endpoints for secret scanning](https://docs.github.com/en/rest/secret-scanning#update-a-secret-scanning-alert) in the REST API documentation.
  7. Click **Close alert**.


## [Next steps](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/resolving-alerts#next-steps)
  * [Monitoring alerts from secret scanning](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/monitoring-alerts)


