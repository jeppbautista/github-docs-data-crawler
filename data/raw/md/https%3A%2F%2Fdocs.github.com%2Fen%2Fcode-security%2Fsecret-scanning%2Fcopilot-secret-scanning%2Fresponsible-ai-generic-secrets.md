  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secret scanning](https://docs.github.com/en/code-security/secret-scanning "Secret scanning")/
  * [Copilot secret scanning](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning "Copilot secret scanning")/
  * [Generic secret detection](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-generic-secrets "Generic secret detection")


# Responsible detection of generic secrets with Copilot secret scanning
Learn how Copilot secret scanning uses AI responsibly to scan and create alerts for unstructured secrets, such as passwords.
## Who can use this feature?
Copilot secret scanning is available for the following repository types:
  * Organization-owned repositories on GitHub Team with [GitHub Secret Protection](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [About generic secret detection with Copilot secret scanning](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-generic-secrets#about-generic-secret-detection-with-copilot-secret-scanning)
  * [Improving the performance of generic secret detection](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-generic-secrets#improving-the-performance-of-generic-secret-detection)
  * [Limitations of generic secret detection](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-generic-secrets#limitations-of-generic-secret-detection)
  * [Evaluation of generic secret detection](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-generic-secrets#evaluation-of-generic-secret-detection)
  * [Next steps](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-generic-secrets#next-steps)
  * [Further reading](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-generic-secrets#further-reading)


## [About generic secret detection with Copilot secret scanning](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-generic-secrets#about-generic-secret-detection-with-copilot-secret-scanning)
Copilot secret scanning's generic secret detection is an AI-powered expansion of secret scanning that identifies unstructured secrets (passwords) in your source code and then generates an alert.
You do not need a subscription to GitHub Copilot to use Copilot secret scanning's generic secret detection. Copilot secret scanning features are available to repositories owned by organizations and enterprises that have a license for GitHub Secret Protection.
GitHub Secret Protection users can already receive secret scanning alerts for partner or custom patterns found in their source code, but unstructured secrets are not easily discoverable. Copilot secret scanning uses large language models (LLMs) to identify this type of secret.
When a password is detected, an alert is displayed in the "Generic" list of secret scanning alerts (under the **Security** tab of the repository, organization, or enterprise), so that maintainers and security managers can review the alert and, where necessary, remove the credential or implement a fix.
For users with GitHub Enterprise Cloud, an enterprise owner must first set a policy at the enterprise level that controls whether generic secret detection can be enabled and disabled for repositories in an organization. This policy is set to "allowed" by default. The feature must then be enabled for repositories and organizations.
### [Input processing](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-generic-secrets#input-processing)
Input is limited to text (typically code) that a user has checked into a repository. The system provides this text to the LLM along with a meta prompt asking the LLM to find passwords within the scope of the input. The user does not interact with the LLM directly.
The system scans for passwords using the LLM. No additional data is collected by the system, other than what is already collected by the existing secret scanning feature.
### [Output and display](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-generic-secrets#output-and-display)
The LLM scans for strings that resemble passwords and verifies that the identified strings included in the response actually exist in the input.
These detected strings are surfaced as alerts on the secret scanning alerts page, but they are displayed in an additional list that is separate from regular secret scanning alerts. The intent is that this separate list is triaged with more scrutiny to verify the validity of the findings. Each alert notes that it was detected using AI. For information on how to view alerts for generic secrets, see [Viewing and filtering alerts from secret scanning](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/viewing-alerts).
## [Improving the performance of generic secret detection](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-generic-secrets#improving-the-performance-of-generic-secret-detection)
To improve the performance of generic secret detection, we recommend closing false positive alerts appropriately.
### [Verify the accuracy of alerts and close as appropriate](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-generic-secrets#verify-the-accuracy-of-alerts-and-close-as-appropriate)
Since Copilot secret scanning's generic secret detection may generate more false positives than the existing secret scanning feature for partner patterns, it's important that you review the accuracy of these alerts. When you verify an alert to be a false positive, be sure to close the alert and mark the reason as "False positive" in the GitHub UI. The GitHub development team will use information on false positive volume and detection locations to improve the model. GitHub does not have access to the secret literals themselves.
## [Limitations of generic secret detection](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-generic-secrets#limitations-of-generic-secret-detection)
When using Copilot secret scanning's generic secret detection, you should consider the following limitations.
### [Limited scope](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-generic-secrets#limited-scope)
Generic secret detection currently only looks for instances of passwords in git content. The feature does not look for other types of generic secrets, and it does not look for secrets in non-git content, such as GitHub Issues.
### [Potential for false positive alerts](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-generic-secrets#potential-for-false-positive-alerts)
Generic secret detection may generate more false positive alerts when compared to the existing secret scanning feature (which detects partner patterns, and which has a very low false positive rate). To mitigate this excess noise, alerts are grouped in a separate list from partner pattern alerts, and security managers and maintainers should triage each alert to verify its accuracy.
### [Potential for incomplete reporting](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-generic-secrets#potential-for-incomplete-reporting)
Generic secret detection may miss instances of credentials checked into a repository. The LLM will improve over time. You retain ultimate responsibility for ensuring the security of your code.
### [Limitations by design](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-generic-secrets#limitations-by-design)
Generic secret detection has the following limitations by design:
  * Copilot secret scanning will not detect secrets that are obviously fake or test passwords, or passwords with low entropy.
  * Copilot secret scanning will only detect a maximum of 100 passwords per push.
  * If five or more detected secrets within a single file are marked as false positive, Copilot secret scanning will stop generating new alerts for that file.
  * Copilot secret scanning does not detect secrets in generated or vendored files.
  * Copilot secret scanning does not detect secrets in encrypted files.
  * Copilot secret scanning does not detect secrets in file types: SVG, PNG, JPEG, CSV, TXT, SQL, or ITEM.
  * Copilot secret scanning does not detect secrets in test code. Copilot secret scanning skips detections when both conditions are met: 
    * The file path contains "test", "mock", or "spec", AND
    * The file extension is `.cs`, `.go`, `.java`, `.js`, `.kt`, `.php`, `.py`, `.rb`, `.scala`, `.swift`, or `.ts`.


## [Evaluation of generic secret detection](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-generic-secrets#evaluation-of-generic-secret-detection)
Generic secret detection has been subject to Responsible AI Red Teaming and GitHub will continue to monitor the efficacy and safety of the feature over time.
## [Next steps](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-generic-secrets#next-steps)
  * [Enabling Copilot secret scanning's generic secret detection](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/enabling-ai-powered-generic-secret-detection)
  * [Managing alerts from secret scanning](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning)


## [Further reading](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-generic-secrets#further-reading)
  * [About secret scanning](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning)


