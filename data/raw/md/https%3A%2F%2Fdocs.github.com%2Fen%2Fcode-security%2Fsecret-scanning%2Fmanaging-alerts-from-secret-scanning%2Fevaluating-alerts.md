  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secret scanning](https://docs.github.com/en/code-security/secret-scanning "Secret scanning")/
  * [Manage alerts](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning "Manage alerts")/
  * [Evaluate alerts](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts "Evaluate alerts")


# Evaluating alerts from secret scanning
Learn about additional features that can help you evaluate alerts and prioritize their remediation, such as checking a secret's validity.
## Who can use this feature?
Repository owners, organization owners, security managers, and users with the **admin** role
## In this article
  * [About evaluating alerts](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts#about-evaluating-alerts)
  * [Checking a secret's validity](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts#checking-a-secrets-validity)
  * [Performing an on-demand validity check](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts#performing-an-on-demand-validity-check)
  * [Reviewing GitHub token metadata](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts#reviewing-github-token-metadata)
  * [Reviewing alert labels](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts#reviewing-alert-labels)
  * [Next steps](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts#next-steps)


## [About evaluating alerts](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts#about-evaluating-alerts)
There are some additional features that can help you to evaluate alerts in order to better prioritize and manage them. You can:
  * Check the validity of a secret, to see if the secret is still active. **Applies to GitHub tokens only**. For more information, see [Checking a secret's validity](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts#checking-a-secrets-validity).
  * Perform an "on-demand" validity check, to get the most up to date validation status. For more information, see [Performing an on-demand validity check](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts#performing-an-on-demand-validity-check).
  * Review a token's metadata. **Applies to GitHub tokens only**. For example, to see when the token was last used. For more information, see [Reviewing GitHub token metadata](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts#reviewing-github-token-metadata).
  * Review the labels assigned to the alert. For more information, see [Reviewing alert labels](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts#reviewing-alert-labels).


## [Checking a secret's validity](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts#checking-a-secrets-validity)
Validity checks help you prioritize alerts by telling you which secrets are `active` or `inactive`. An `active` secret is one that could still be exploited, so these alerts should be reviewed and remediated as a priority.
By default, GitHub checks the validity of GitHub tokens and displays the validation status of the token in the alert view.
Organizations using GitHub Team or GitHub Enterprise Cloud with a license for GitHub Secret Protection can also enable validity checks for partner patterns. For more information, see [Checking a secret's validity](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts#checking-a-secrets-validity).
Validity | Status | Result  
---|---|---  
Active secret | `active` | GitHub checked with this secret's provider and found that the secret is active  
Possibly active secret | `unknown` | GitHub does not support validation checks for this token type yet  
Possibly active secret | `unknown` | GitHub could not verify this secret  
Secret inactive | `inactive` | You should make sure no unauthorized access has already occurred  
Validity checks for partner patterns are available for the following repository types:
  * Organization-owned repositories on GitHub Team with [GitHub Secret Protection](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


For information on how to enable validity checks for partner patterns, see [Enabling validity checks for your repository](https://docs.github.com/en/code-security/secret-scanning/enabling-secret-scanning-features/enabling-validity-checks-for-your-repository), and for information on which partner patterns are currently supported, see [Supported secret scanning patterns](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns).
You can use the REST API to retrieve a list of the most recent validation status for each of your tokens. For more information, see [REST API endpoints for secret scanning](https://docs.github.com/en/rest/secret-scanning) in the REST API documentation. You can also use webhooks to be notified of activity relating to a secret scanning alert. For more information, see the `secret_scanning_alert` event in [Webhook events and payloads](https://docs.github.com/en/webhooks/webhook-events-and-payloads?actionType=created#secret_scanning_alert).
## [Performing an on-demand validity check](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts#performing-an-on-demand-validity-check)
Once you have enabled validity checks for partner patterns for your repository, you can perform an "on-demand" validity check for any supported secret by clicking 
![Screenshot of the UI showing a secret scanning alert. A button, labeled "Verify secret" is highlighted with an orange outline.](https://docs.github.com/assets/cb-45069/images/help/security/secret-scanning-verify-secret.png)
## [Reviewing GitHub token metadata](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts#reviewing-github-token-metadata)
Metadata for GitHub tokens is currently in public preview and subject to change.
In the view for an active GitHub token alert, you can review certain metadata about the token. This metadata may help you identify the token and decide what remediation steps to take.
Tokens, like personal access token and other credentials, are considered personal information. For more information about using GitHub tokens, see [GitHub's Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement) and [Acceptable Use Policies](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies).
![Screenshot of the UI for a GitHub token, showing the token metadata.](https://docs.github.com/assets/cb-57664/images/help/repository/secret-scanning-github-token-metadata.png)
Metadata for GitHub tokens is available for active tokens in any repository with secret scanning enabled. If a token has been revoked or its status cannot be validated, metadata will not be available. GitHub auto-revokes GitHub tokens in public repositories, so metadata for GitHub tokens in public repositories is unlikely to be available. The following metadata is available for active GitHub tokens:
Metadata | Description  
---|---  
Secret name | The name given to the GitHub token by its creator  
Secret owner | The GitHub handle of the token's owner  
Created on | Date the token was created  
Expired on | Date the token expired  
Last used on | Date the token was last used  
Access | Whether the token has organization access  
## [Reviewing alert labels](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts#reviewing-alert-labels)
In the alert view, you can review any labels assigned to the alert. The labels provide additional details about the alert, which can inform the approach you take for remediation.
Secret scanning alerts can have the following labels assigned to them. Depending on the labels assigned, you'll see additional information in the alert view.
Label | Description | Alert view information  
---|---|---  
`public leak` | The secret detected in your repository has also been found as publicly leaked by at least one of GitHub's scans of code, discussions, gists, issues, pull requests, and wikis. This may require you to address the alert with greater urgency, or remediate the alert differently compared to a privately exposed token. | You'll see links to any specific public locations where the leaked secret has been detected.  
`multi-repo` | The secret detected in your repository has been found across multiple repositories in your organization or enterprise. This information may help you more easily dedupe the alert across your organization or enterprise. | If you have appropriate permissions, you'll see links to any specific alerts for the same secret in your organization or enterprise.  
## [Next steps](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts#next-steps)
  * [Resolving alerts from secret scanning](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/resolving-alerts)


