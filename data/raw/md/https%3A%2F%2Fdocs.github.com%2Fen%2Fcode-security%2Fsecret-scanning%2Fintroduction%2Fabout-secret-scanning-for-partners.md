  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secret scanning](https://docs.github.com/en/code-security/secret-scanning "Secret scanning")/
  * [Introduction](https://docs.github.com/en/code-security/secret-scanning/introduction "Introduction")/
  * [Secret scanning for partners](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning-for-partners "Secret scanning for partners")


# About secret scanning for partners
When secret scanning detects authentication details for a service provider in a public repository on GitHub, an alert is sent directly to the provider. This allows service providers who are GitHub partners to promptly take action to secure their systems.
## Who can use this feature?
Secret scanning alerts for partners runs by default on the following repositories:
  * Public repositories and public npm packages on GitHub


## In this article
  * [About secret scanning alerts for partners](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning-for-partners#about-secret-scanning-alerts-for-partners)
  * [What are the supported secrets](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning-for-partners#what-are-the-supported-secrets)
  * [Further reading](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning-for-partners#further-reading)


## [About secret scanning alerts for partners](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning-for-partners#about-secret-scanning-alerts-for-partners)
GitHub scans public repositories and public npm packages for secrets issued by specific service providers who joined our partnership program, and alerts the relevant service provider whenever a secret is detected in a commit. The service provider validates the string and then decides whether they should revoke the secret, issue a new secret, or contact you directly. Their action will depend on the associated risks to you or them. To find out about our partner program, see [Secret scanning partner program](https://docs.github.com/en/code-security/secret-scanning/secret-scanning-partnership-program/secret-scanning-partner-program).
You cannot change the configuration of secret scanning for partner patterns on public repositories.
The reason partner alerts are directly sent to the secret providers whenever a leak is detected for one of their secrets is that this enables the provider to take immediate action to protect you and protect their resources. The notification process for regular alerts is different. Regular alerts are displayed on the repository's **Security** tab on GitHub for you to resolve.
If access to a resource requires paired credentials, then secret scanning will create an alert only when both parts of the pair are detected in the same file. This ensures that the most critical leaks are not hidden behind information about partial leaks. Pair matching also helps reduce false positives since both elements of a pair must be used together to access the provider's resource.
## [What are the supported secrets](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning-for-partners#what-are-the-supported-secrets)
For information about the secrets and service providers supported by push protection, see [Supported secret scanning patterns](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#supported-secrets).
## [Further reading](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning-for-partners#further-reading)
  * [About secret scanning](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning)
  * [Supported secret scanning patterns](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns)
  * [Secret scanning partner program](https://docs.github.com/en/code-security/secret-scanning/secret-scanning-partnership-program/secret-scanning-partner-program)


