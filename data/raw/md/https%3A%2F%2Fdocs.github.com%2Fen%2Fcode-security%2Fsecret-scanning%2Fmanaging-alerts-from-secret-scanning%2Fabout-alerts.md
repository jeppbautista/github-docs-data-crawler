  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secret scanning](https://docs.github.com/en/code-security/secret-scanning "Secret scanning")/
  * [Manage alerts](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning "Manage alerts")/
  * [About alerts](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/about-alerts "About alerts")


# About secret scanning alerts
Learn about the different types of secret scanning alerts.
## Who can use this feature?
Repository owners, organization owners, security managers, and users with the **admin** role
Secret scanning is available for the following repository types:
  * Public repositories on GitHub.com
  * Organization-owned repositories on GitHub Team with [GitHub Secret Protection](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [About types of alerts](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/about-alerts#about-types-of-alerts)
  * [About user alerts](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/about-alerts#about-user-alerts)
  * [About push protection alerts](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/about-alerts#about-push-protection-alerts)
  * [About partner alerts](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/about-alerts#about-partner-alerts)
  * [Next steps](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/about-alerts#next-steps)
  * [Further reading](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/about-alerts#further-reading)


## [About types of alerts](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/about-alerts#about-types-of-alerts)
There are three types of secret scanning alerts:
  * **User alerts:** Reported to users in the **Security** tab of the repository, when a supported secret is detected in the repository.
  * **Push protection alerts:** Reported to users in the **Security** tab of the repository, when a contributor bypasses push protection.
  * **Partner alerts:** Reported directly to secret providers that are part of secret scanning's partner program. These alerts are not reported in the **Security** tab of the repository.


## [About user alerts](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/about-alerts#about-user-alerts)
When GitHub detects a supported secret in a repository that has secret scanning enabled, a user alert is generated and displayed in the **Security** tab of the repository.
User alerts can be of the following types:
  * Default alerts, which relate to supported patterns and specified custom patterns.
  * Generic alerts, which can have a higher ratio of false positives or secrets used in tests.


GitHub displays generic alerts in a different list to default alerts, making triaging a better experience for users. For more information, see [Viewing and filtering alerts from secret scanning](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/viewing-alerts).
If access to a resource requires paired credentials, then secret scanning will create an alert only when both parts of the pair are detected in the same file. This ensures that the most critical leaks are not hidden behind information about partial leaks. Pair matching also helps reduce false positives since both elements of a pair must be used together to access the provider's resource.
## [About push protection alerts](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/about-alerts#about-push-protection-alerts)
Push protection scans pushes for supported secrets. If push protection detects a supported secret, it will block the push. When a contributor bypasses push protection to push a secret to the repository, a push protection alert is generated and displayed in the **Security** tab of the repository. To see all push protection alerts for a repository, you must filter by `bypassed: true` on the alerts page. For more information, see [Viewing and filtering alerts from secret scanning](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/viewing-alerts#filtering-alerts).
If access to a resource requires paired credentials, then secret scanning will create an alert only when both parts of the pair are detected in the same file. This ensures that the most critical leaks are not hidden behind information about partial leaks. Pair matching also helps reduce false positives since both elements of a pair must be used together to access the provider's resource.
You can also enable push protection for your personal account, called "push protection for users", which prevents you from accidentally pushing supported secrets to _any_ public repository. Alerts are _not_ created if you choose to bypass your user-based push protection only. Alerts are only created if the repository itself has push protection enabled. For more information, see [Push protection for users](https://docs.github.com/en/code-security/secret-scanning/working-with-secret-scanning-and-push-protection/push-protection-for-users).
Older versions of certain tokens may not be supported by push protection as these tokens may generate a higher number of false positives than their most recent version. Push protection may also not apply to legacy tokens. For tokens such as Azure Storage Keys, GitHub only supports _recently created_ tokens, not tokens that match the legacy patterns. For more information about push protection limitations, see [Troubleshooting secret scanning](https://docs.github.com/en/code-security/secret-scanning/troubleshooting-secret-scanning-and-push-protection/troubleshooting-secret-scanning#push-protection-and-pattern-versions).
## [About partner alerts](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/about-alerts#about-partner-alerts)
When GitHub detects a leaked secret in a public repository or npm package, an alert is sent directly to the secret provider, if they are part of GitHub's secret scanning partner program. For more information about secret scanning alerts for partners, see [Secret scanning partner program](https://docs.github.com/en/code-security/secret-scanning/secret-scanning-partnership-program/secret-scanning-partner-program) and [Supported secret scanning patterns](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns).
Partner alerts are not sent to repository administrators, so you do not need to take any action for this type of alert.
## [Next steps](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/about-alerts#next-steps)
  * [Viewing and filtering alerts from secret scanning](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/viewing-alerts)


## [Further reading](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/about-alerts#further-reading)
  * [Supported secret scanning patterns](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns)
  * [Defining custom patterns for secret scanning](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/defining-custom-patterns-for-secret-scanning)
  * [Enabling secret scanning for non-provider patterns](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/non-provider-patterns/enabling-secret-scanning-for-non-provider-patterns)
  * [Responsible detection of generic secrets with Copilot secret scanning](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-generic-secrets)


