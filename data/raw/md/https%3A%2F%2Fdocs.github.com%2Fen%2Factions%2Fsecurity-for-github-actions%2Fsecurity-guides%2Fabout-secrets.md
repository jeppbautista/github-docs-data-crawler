  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Security](https://docs.github.com/en/actions/security-for-github-actions "Security")/
  * [Security guides](https://docs.github.com/en/actions/security-for-github-actions/security-guides "Security guides")/
  * [About secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/about-secrets "About secrets")


# About secrets
Learn about secrets as they're used in GitHub Actions.
## In this article
  * [About secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/about-secrets#about-secrets)
  * [Naming your secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/about-secrets#naming-your-secrets)
  * [Using your secrets in workflows](https://docs.github.com/en/actions/security-for-github-actions/security-guides/about-secrets#using-your-secrets-in-workflows)
  * [Limiting credential permissions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/about-secrets#limiting-credential-permissions)
  * [Further reading](https://docs.github.com/en/actions/security-for-github-actions/security-guides/about-secrets#further-reading)


## [About secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/about-secrets#about-secrets)
Secrets allow you to store sensitive information in your organization, repository, or repository environments. Secrets are variables that you create to use in GitHub Actions workflows in an organization, repository, or repository environment.
GitHub Actions can only read a secret if you explicitly include the secret in a workflow.
## [Naming your secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/about-secrets#naming-your-secrets)
To help ensure that GitHub redacts your secrets in logs correctly, avoid using structured data as the values of secrets.
The following rules apply to secret names:
  * Can only contain alphanumeric characters (`[a-z]`, `[A-Z]`, `[0-9]`) or underscores (`_`). Spaces are not allowed.
  * Must not start with the `GITHUB_` prefix.
  * Must not start with a number.
  * Are case insensitive.
  * Must be unique to the repository, organization, or enterprise where they are created.


If a secret with the same name exists at multiple levels, the secret at the lowest level takes precedence. For example, if an organization-level secret has the same name as a repository-level secret, then the repository-level secret takes precedence. Similarly, if an organization, repository, and environment all have a secret with the same name, the environment-level secret takes precedence.
## [Using your secrets in workflows](https://docs.github.com/en/actions/security-for-github-actions/security-guides/about-secrets#using-your-secrets-in-workflows)
If a secret is used in a workflow job, GitHub automatically redacts secrets printed to the log. You should avoid printing secrets to the log intentionally.
Organization-level secrets let you share secrets between multiple repositories, which reduces the need for creating duplicate secrets. Updating an organization secret in one location also ensures that the change takes effect in all repository workflows that use that secret.
For environment secrets, you can enable required reviewers to control access to the secrets. A workflow job cannot access environment secrets until approval is granted by required approvers.
To make a secret available to an action, you must set the secret as an input or environment variable in your workflow file. Review the action's README file to learn about which inputs and environment variables the action expects. See [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstepsenv).
Organization and repository secrets are read when a workflow run is queued, and environment secrets are read when a job referencing the environment starts.
## [Limiting credential permissions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/about-secrets#limiting-credential-permissions)
When generating credentials, we recommend that you grant the minimum permissions possible. For example, instead of using personal credentials, use [deploy keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/managing-deploy-keys#deploy-keys) or a service account. Consider granting read-only permissions if that's all that is needed, and limit access as much as possible.
When generating a personal access token (classic), select the fewest scopes necessary. When generating a fine-grained personal access token, select the minimum permissions and repository access required.
Instead of using a personal access token, consider using a GitHub App, which uses fine-grained permissions and short lived tokens, similar to a fine-grained personal access token. Unlike a personal access token, a GitHub App is not tied to a user, so the workflow will continue to work even if the user who installed the app leaves your organization. For more information, see [Making authenticated API requests with a GitHub App in a GitHub Actions workflow](https://docs.github.com/en/apps/creating-github-apps/guides/making-authenticated-api-requests-with-a-github-app-in-a-github-actions-workflow).
## [Further reading](https://docs.github.com/en/actions/security-for-github-actions/security-guides/about-secrets#further-reading)
  * [Using secrets in GitHub Actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)
  * [REST API endpoints for GitHub Actions Secrets](https://docs.github.com/en/rest/actions/secrets)


