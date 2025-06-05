  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secret scanning](https://docs.github.com/en/code-security/secret-scanning "Secret scanning")/
  * [Troubleshoot](https://docs.github.com/en/code-security/secret-scanning/troubleshooting-secret-scanning-and-push-protection "Troubleshoot")/
  * [Troubleshoot secret scanning](https://docs.github.com/en/code-security/secret-scanning/troubleshooting-secret-scanning-and-push-protection/troubleshooting-secret-scanning "Troubleshoot secret scanning")


# Troubleshooting secret scanning
When using secret scanning to detect secrets in your repository, or secrets about to be committed into your repository, you may need to troubleshoot unexpected issues.
## Who can use this feature?
Secret scanning is available for the following repository types:
  * Public repositories on GitHub.com
  * Organization-owned repositories on GitHub Team with [GitHub Secret Protection](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Detection of pattern pairs](https://docs.github.com/en/code-security/secret-scanning/troubleshooting-secret-scanning-and-push-protection/troubleshooting-secret-scanning#detection-of-pattern-pairs)
  * [About legacy GitHub tokens](https://docs.github.com/en/code-security/secret-scanning/troubleshooting-secret-scanning-and-push-protection/troubleshooting-secret-scanning#about-legacy-github-tokens)
  * [Push protection limitations](https://docs.github.com/en/code-security/secret-scanning/troubleshooting-secret-scanning-and-push-protection/troubleshooting-secret-scanning#push-protection-limitations)


## [Detection of pattern pairs](https://docs.github.com/en/code-security/secret-scanning/troubleshooting-secret-scanning-and-push-protection/troubleshooting-secret-scanning#detection-of-pattern-pairs)
Secret scanning will only detect pattern pairs, such as AWS Access Keys and Secrets, if the ID and the secret are found in the same file, and both are pushed to the repository. Pair matching helps reduce false positives since both elements of a pair (the ID and the secret) must be used together to access the provider's resource.
Pairs pushed to different files, or not pushed to the same repository, will not result in alerts. For more information about the supported pattern pairs, see the table in [Supported secret scanning patterns](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns).
## [About legacy GitHub tokens](https://docs.github.com/en/code-security/secret-scanning/troubleshooting-secret-scanning-and-push-protection/troubleshooting-secret-scanning#about-legacy-github-tokens)
For GitHub tokens, we check the validity of the secret to determine whether the secret is active or inactive. This means that for legacy tokens, secret scanning won't detect a GitHub Enterprise Server personal access token on GitHub Enterprise Cloud. Similarly, a GitHub Enterprise Cloud personal access token won't be found on GitHub Enterprise Server.
## [Push protection limitations](https://docs.github.com/en/code-security/secret-scanning/troubleshooting-secret-scanning-and-push-protection/troubleshooting-secret-scanning#push-protection-limitations)
If push protection did not detect a secret that you think should have been detected, then you should first check that push protection supports the secret type in the list of supported secrets. For further information, see [Supported secret scanning patterns](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#supported-secrets).
If your secret is in the supported list, there are various reasons why push protection may not detect it.
  * Push protection only blocks leaked secrets on a subset of the most identifiable user-alerted patterns. Contributors can trust security defenses when such secrets are blocked as these are the patterns that have the lowest number of false positives.
  * The version of your secret may be old. Older versions of certain tokens may not be supported by push protection as these tokens may generate a higher number of false positives than their most recent version. Push protection may also not apply to legacy tokens. For tokens such as Azure Storage Keys, GitHub only supports _recently created_ tokens, not tokens that match the legacy patterns.
  * The push may be too large, for example, if you're trying to push thousands of large files. A push protection scan may time out and not block a user if the push is too large. GitHub will still scan and create alerts, if needed, after the push.
  * If the push results in the detection of over five new secrets, we will only show you the first five (we will always show you a maximum of five secrets at one time).
  * If a push contains over 1,000 existing secrets (that is, secrets for which alerts have already been created), push protection will not block the push.
  * If a push in a public repository is larger than 50 MB, push protection will skip it and won't scan it.


