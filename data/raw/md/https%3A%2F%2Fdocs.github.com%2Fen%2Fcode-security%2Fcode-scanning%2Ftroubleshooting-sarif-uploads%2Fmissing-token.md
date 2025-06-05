  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Troubleshooting SARIF uploads](https://docs.github.com/en/code-security/code-scanning/troubleshooting-sarif-uploads "Troubleshooting SARIF uploads")/
  * [GitHub token missing](https://docs.github.com/en/code-security/code-scanning/troubleshooting-sarif-uploads/missing-token "GitHub token missing")


# GitHub token is required to upload SARIF results
You need to provide an authentication method for the upload process to use to access the repository.
## In this article
  * [About this error](https://docs.github.com/en/code-security/code-scanning/troubleshooting-sarif-uploads/missing-token#about-this-error)
  * [Fixing the problem](https://docs.github.com/en/code-security/code-scanning/troubleshooting-sarif-uploads/missing-token#fixing-the-problem)


## [About this error](https://docs.github.com/en/code-security/code-scanning/troubleshooting-sarif-uploads/missing-token#about-this-error)
```
A GitHub token is required to upload SARIF results but none was specified

```

This error is reported if the upload process does not reference an authentication method, or if that method has the wrong permission. The permissions required to upload SARIF file to a repository are the same no matter what process you use to upload the data.
  * Fine-grained personal access tokens require `write` scope for the repository.
  * Classic personal access tokens require `security_events` scope for the repository for private or internal repositories. You can use tokens with the `public_repo` scope for public repositories.
  * GitHub Apps require `security_events` scope for the repository.


You could see this error for SARIF files created using any tool and uploaded using any method.
## [Fixing the problem](https://docs.github.com/en/code-security/code-scanning/troubleshooting-sarif-uploads/missing-token#fixing-the-problem)
Create a new personal access token or GitHub App with the correct permission. For more information see, [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens), or [Authenticating as a GitHub App](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app) and [Deciding when to build a GitHub App](https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/deciding-when-to-build-a-github-app).
