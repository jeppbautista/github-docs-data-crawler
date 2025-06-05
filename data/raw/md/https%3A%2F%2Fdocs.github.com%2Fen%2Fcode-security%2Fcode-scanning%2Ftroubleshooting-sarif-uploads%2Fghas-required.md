  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Troubleshooting SARIF uploads](https://docs.github.com/en/code-security/code-scanning/troubleshooting-sarif-uploads "Troubleshooting SARIF uploads")/
  * [GitHub Code Security disabled](https://docs.github.com/en/code-security/code-scanning/troubleshooting-sarif-uploads/ghas-required "GitHub Code Security disabled")


# Upload fails because GitHub Code Security is disabled
You can only upload SARIF results to private or internal repositories where GitHub Code Security is enabled.
## [About this error](https://docs.github.com/en/code-security/code-scanning/troubleshooting-sarif-uploads/ghas-required#about-this-error)
```
GitHub Code Security or GitHub Advanced Security not enabled
GitHub Code Security or GitHub Advanced Security blocked by a policy
403: GitHub Code Security or GitHub Advanced Security is not enabled

```

This error is reported if a process attempts to upload a SARIF file to a repository where GitHub Code Security is not enabled or where use of this feature is blocked by a policy.
You will only see this error for SARIF files that contain results created using CodeQL and for uploads to repositories with private or internal visibility. GitHub Code Security is enabled by default for all public repositories.
For information on how to confirm this error and fix the problem, see [Error: "GitHub Code Security or GitHub Advanced Security must be enabled for this repository to use code scanning"](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/advanced-security-must-be-enabled).
