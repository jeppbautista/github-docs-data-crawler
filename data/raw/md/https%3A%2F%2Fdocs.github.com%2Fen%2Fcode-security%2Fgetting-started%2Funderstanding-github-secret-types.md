  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Getting started](https://docs.github.com/en/code-security/getting-started "Getting started")/
  * [GitHub secret types](https://docs.github.com/en/code-security/getting-started/understanding-github-secret-types "GitHub secret types")


# Understanding GitHub secret types
Learn about the usage, scope, and access permissions for GitHub secrets.
## In this article
  * [About GitHub's secret types](https://docs.github.com/en/code-security/getting-started/understanding-github-secret-types#about-githubs-secret-types)
  * [Dependabot secrets](https://docs.github.com/en/code-security/getting-started/understanding-github-secret-types#dependabot-secrets)
  * [Actions secrets](https://docs.github.com/en/code-security/getting-started/understanding-github-secret-types#actions-secrets)
  * [Codespaces secrets](https://docs.github.com/en/code-security/getting-started/understanding-github-secret-types#codespaces-secrets)
  * [Further reading](https://docs.github.com/en/code-security/getting-started/understanding-github-secret-types#further-reading)


## [About GitHub's secret types](https://docs.github.com/en/code-security/getting-started/understanding-github-secret-types#about-githubs-secret-types)
GitHub secrets are used to securely store sensitive information like API keys, tokens, and passwords in repositories.
When you store the sensitive information as a GitHub secret, you remove the need to hardcode the credential or key, and prevent exposure of it in your code or logs. The secret can then be used to authenticate services, manage credentials, and securely pass sensitive data in workflows.
There are three types of secrets used by GitHub:
  * [Dependabot secrets](https://docs.github.com/en/code-security/getting-started/understanding-github-secret-types#dependabot-secrets)
  * [Actions secrets](https://docs.github.com/en/code-security/getting-started/understanding-github-secret-types#actions-secrets)
  * [Codespaces secrets](https://docs.github.com/en/code-security/getting-started/understanding-github-secret-types#codespaces-secrets)


Depending on the GitHub secret type, you can create and manage secrets under your repository, organization, or personal account security settings page.
### [Understanding how GitHub stores secrets](https://docs.github.com/en/code-security/getting-started/understanding-github-secret-types#understanding-how-github-stores-secrets)
GitHub uses [Libsodium sealed boxes](https://libsodium.gitbook.io/doc/public-key_cryptography/sealed_boxes) to encrypt secrets. A secret is encrypted before reaching GitHub and remains encrypted until it's used by the relevant service (Dependabot, GitHub Actions, or Codespaces).
## [Dependabot secrets](https://docs.github.com/en/code-security/getting-started/understanding-github-secret-types#dependabot-secrets)
Dependabot secrets are used to store credentials and sensitive information for use within Dependabot.
Dependabot secrets are referenced in a repository's `dependabot.yml` file.
### [Usage](https://docs.github.com/en/code-security/getting-started/understanding-github-secret-types#usage)
Dependabot secrets are typically used by Dependabot to authenticate to private package registries. This allows Dependabot to open pull requests to update vulnerable or outdated dependencies in private repositories. Used for authentication, these Dependabot secrets are referenced in a repository's `dependabot.yml` file.
Dependabot secrets can also include secrets required for workflows initiated by Dependabot. For example, Dependabot can trigger GitHub Actions workflows when it creates pull requests to update dependencies, or comments on pull requests. In this case, Dependabot secrets can be referenced from workflow files (`.github/workflows/*.yml`) as long as the workflow is triggered by a Dependabot event.
### [Scope](https://docs.github.com/en/code-security/getting-started/understanding-github-secret-types#scope)
You can define Dependabot secrets at:
  * Repository level
  * Organization level


Dependabot secrets can be shared across repositories when set at the organization-level. You must specify which repositories in the organization can access the secret.
### [Access permissions](https://docs.github.com/en/code-security/getting-started/understanding-github-secret-types#access-permissions)
Dependabot secrets are accessed by Dependabot when authenticating to private registries to update dependencies.
Dependabot secrets are accessed by GitHub Actions workflows when the trigger event for the workflow is initiated by Dependabot. This is because when a workflow is initiated by Dependabot, only Dependabot secrets are available - Actions secrets are not accessible. Therefore, any secrets required for these workflows must be stored as Dependabot secrets, rather than Actions secrets. There are additional security restrictions for the `pull_request_target` event. See [Limitations and restrictions](https://docs.github.com/en/code-security/getting-started/understanding-github-secret-types#limitations-and-restrictions).
#### [User access permissions](https://docs.github.com/en/code-security/getting-started/understanding-github-secret-types#user-access-permissions)
Repository-level secrets:
  * Users with **admin access** to the repository can create and manage Dependabot secrets.
  * Users with **collaborator access** to the repository can use the secret for Dependabot.


Organization-level secrets:
  * **Organization owners** can create and manage Dependabot secrets.
  * Users with **collaborator access** to the repositories with access to each secret can use the secret for Dependabot.


### [Limitations and restrictions](https://docs.github.com/en/code-security/getting-started/understanding-github-secret-types#limitations-and-restrictions)
For workflows initiated by Dependabot, the `pull_request_target` event is treated differently to other events. For this event, if the base ref of the pull request was created by Dependabot (`github.event.pull_request.user.login == 'dependabot[bot]'`):
  * The workflow receives a read-only `GITHUB_TOKEN`.
  * Secrets are **not** available to the workflow.


This extra restriction helps prevent potential security risks that could arise from pull requests created by Dependabot.
Dependabot secrets are not passed to forks.
## [Actions secrets](https://docs.github.com/en/code-security/getting-started/understanding-github-secret-types#actions-secrets)
Actions secrets are used to store sensitive information such as API keys, authentication tokens, and other credentials in workflows.
### [Usage](https://docs.github.com/en/code-security/getting-started/understanding-github-secret-types#usage-1)
Actions secrets are referenced in workflow files (`.github/workflows/*.yml`).
### [Scope](https://docs.github.com/en/code-security/getting-started/understanding-github-secret-types#scope-1)
You can define Actions secrets at:
  * Repository level
  * Environment level
  * Organization level


Environment-level secrets are specific to a particular environment, such as production or staging. Actions secrets can be shared across repositories if set at the organization-level. You can use access policies to control which repositories have access to the secret.
### [Access permissions](https://docs.github.com/en/code-security/getting-started/understanding-github-secret-types#access-permissions-1)
Actions secrets are only available within GitHub Actions workflows. Despite running on Actions, Dependabot does not have access to Actions secrets.
For workflows initiated by Dependabot, Actions secrets are not available. These workflow secrets must be stored as Dependabot secrets in order to be accessible to the workflow.
The location where you store the Actions secret determines its accessibility:
  * Repository secret: all workflows in the repository can access the secret.
  * Environment secret: secret is limited to jobs referencing that particular environment.
  * Organization secret: all workflows in the repositories that have been granted access by the organization can access the organization secrets.


#### [User access permissions](https://docs.github.com/en/code-security/getting-started/understanding-github-secret-types#user-access-permissions-1)
Repository-level and environment secrets:
  * Users with **admin access** to the repository can create and manage Actions secrets.
  * Users with **collaborator access** to the repository can use the secret.


Organization-level secrets:
  * **Organization owners** can create and manage Actions secrets.
  * Users with **collaborator access** to the repositories with access to each secret can use the secret.


### [Limitations and restrictions](https://docs.github.com/en/code-security/getting-started/understanding-github-secret-types#limitations-and-restrictions-1)
  * Actions secrets are not available to workflows initiated by Dependabot.
  * Actions secrets are not passed to workflows that are triggered by a pull request from a fork.
  * GitHub Actions automatically redacts the contents of all GitHub secrets that are printed to workflow logs.
  * You can store up to 1,000 organization secrets, 100 repository secrets, and 100 environment secrets. Secrets are limited to 48 KB in size. For more information, see [Limits for secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#limits-for-secrets).


## [Codespaces secrets](https://docs.github.com/en/code-security/getting-started/understanding-github-secret-types#codespaces-secrets)
Codespaces secrets store credentials and sensitive information, such as API tokens and SSH keys, for use within GitHub Codespaces, allowing you to configure secure development environments.
### [Usage](https://docs.github.com/en/code-security/getting-started/understanding-github-secret-types#usage-2)
Codespaces secrets are referenced within the Codespaces development container configuration (`devcontainer.json`).
### [Scope](https://docs.github.com/en/code-security/getting-started/understanding-github-secret-types#scope-2)
You can define Codespaces secrets at:
  * User account level
  * Repository level
  * Organization level


For user account level secrets, you can choose which repositories have access to the secret. Codespaces secrets can be shared across repositories if set at the organization-level. You can use access policies to control which repositories have access to the secret.
### [Access permissions](https://docs.github.com/en/code-security/getting-started/understanding-github-secret-types#access-permissions-2)
Codespaces secrets are only accessible in Codespaces.
GitHub Actions cannot access Codespaces secrets.
#### [User access permissions](https://docs.github.com/en/code-security/getting-started/understanding-github-secret-types#user-access-permissions-2)
User account-level secrets:
  * Codespaces secrets are available to any codespace you create using repositories with access to that secret.


Repository-level secrets:
  * Users with **admin access** to the repository can create and manage Codespaces secrets.
  * Users with **collaborator access** to the repository can use the secret.


Organization-level secrets:
  * **Organization owners** can create and manage Codespaces secrets.
  * Users with **collaborator access** to the repositories with access to each secret can use the secret.


### [Limitations and restrictions](https://docs.github.com/en/code-security/getting-started/understanding-github-secret-types#limitations-and-restrictions-2)
  * You can store up to 100 secrets for GitHub Codespaces.
  * Secrets are limited to 48 KB in size.
  * Codespaces secrets are not passed to forks.


## [Further reading](https://docs.github.com/en/code-security/getting-started/understanding-github-secret-types#further-reading)
  * [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#storing-credentials-for-dependabot-to-use)
  * [Using secrets in GitHub Actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)
  * [Managing development environment secrets for your repository or organization](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/managing-development-environment-secrets-for-your-repository-or-organization)
  * [Managing your account-specific secrets for GitHub Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces)


