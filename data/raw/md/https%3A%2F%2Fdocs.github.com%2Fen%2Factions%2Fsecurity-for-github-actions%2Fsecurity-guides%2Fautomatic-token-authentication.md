  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Security](https://docs.github.com/en/actions/security-for-github-actions "Security")/
  * [Security guides](https://docs.github.com/en/actions/security-for-github-actions/security-guides "Security guides")/
  * [Automatic token authentication](https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication "Automatic token authentication")


# Automatic token authentication
GitHub provides a token that you can use to authenticate on behalf of GitHub Actions.
## In this article
  * [About the GITHUB_TOKEN secret](https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication#about-the-github_token-secret)
  * [Using the GITHUB_TOKEN in a workflow](https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication#using-the-github_token-in-a-workflow)
  * [Permissions for the GITHUB_TOKEN](https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication#permissions-for-the-github_token)


## [About the `GITHUB_TOKEN` secret](https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication#about-the-github_token-secret)
At the start of each workflow job, GitHub automatically creates a unique `GITHUB_TOKEN` secret to use in your workflow. You can use the `GITHUB_TOKEN` to authenticate in the workflow job.
When you enable GitHub Actions, GitHub installs a GitHub App on your repository. The `GITHUB_TOKEN` secret is a GitHub App installation access token. You can use the installation access token to authenticate on behalf of the GitHub App installed on your repository. The token's permissions are limited to the repository that contains your workflow. For more information, see [Permissions for the `GITHUB_TOKEN`](https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication#permissions-for-the-github_token).
Before each job begins, GitHub fetches an installation access token for the job. The `GITHUB_TOKEN` expires when a job finishes or after a maximum of 24 hours.
The token is also available in the `github.token` context. For more information, see [Accessing contextual information about workflow runs](https://docs.github.com/en/actions/learn-github-actions/contexts#github-context).
## [Using the `GITHUB_TOKEN` in a workflow](https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication#using-the-github_token-in-a-workflow)
You can use the `GITHUB_TOKEN` by using the standard syntax for referencing secrets: `${{ secrets.GITHUB_TOKEN }}`. Examples of using the `GITHUB_TOKEN` include passing the token as an input to an action, or using it to make an authenticated GitHub API request.
An action can access the `GITHUB_TOKEN` through the `github.token` context even if the workflow does not explicitly pass the `GITHUB_TOKEN` to the action. As a good security practice, you should always make sure that actions only have the minimum access they require by limiting the permissions granted to the `GITHUB_TOKEN`. For more information, see [Permissions for the `GITHUB_TOKEN`](https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication#permissions-for-the-github_token).
When you use the repository's `GITHUB_TOKEN` to perform tasks, events triggered by the `GITHUB_TOKEN`, with the exception of `workflow_dispatch` and `repository_dispatch`, will not create a new workflow run. This prevents you from accidentally creating recursive workflow runs. For example, if a workflow run pushes code using the repository's `GITHUB_TOKEN`, a new workflow will not run even when the repository contains a workflow configured to run when `push` events occur.
Commits pushed by a GitHub Actions workflow that uses the `GITHUB_TOKEN` do not trigger a GitHub Pages build.
### [Example 1: passing the `GITHUB_TOKEN` as an input](https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication#example-1-passing-the-github_token-as-an-input)
This example workflow uses the [GitHub CLI](https://docs.github.com/en/actions/using-workflows/using-github-cli-in-workflows), which requires the `GITHUB_TOKEN` as the value for the `GH_TOKEN` input parameter:
YAML```
name: Open new issue
on: workflow_dispatch

jobs:
  open-issue:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      issues: write
    steps:
      - run: |
          gh issue --repo ${{ github.repository }} \
            create --title "Issue title" --body "Issue body"
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}

```
```
name: Open new issue
on: workflow_dispatch

jobs:
  open-issue:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      issues: write
    steps:
      - run: |
          gh issue --repo ${{ github.repository }} \
            create --title "Issue title" --body "Issue body"
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}

```

### [Example 2: calling the REST API](https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication#example-2-calling-the-rest-api)
You can use the `GITHUB_TOKEN` to make authenticated API calls. This example workflow creates an issue using the GitHub REST API:
```
name: Create issue on commit

on: [ push ]

jobs:
  create_issue:
    runs-on: ubuntu-latest
    permissions:
      issues: write
    steps:
      - name: Create issue using REST API
        run: |
          curl --request POST \
          --url https://api.github.com/repos/${{ github.repository }}/issues \
          --header 'authorization: Bearer ${{ secrets.GITHUB_TOKEN }}' \
          --header 'content-type: application/json' \
          --data '{
            "title": "Automated issue for commit: ${{ github.sha }}",
            "body": "This issue was automatically created by the GitHub Action workflow **${{ github.workflow }}**. \n\n The commit hash was: _${{ github.sha }}_."
            }' \
          --fail

```

## [Permissions for the `GITHUB_TOKEN`](https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication#permissions-for-the-github_token)
For information about the API endpoints GitHub Apps can access with each permission, see [Permissions required for GitHub Apps](https://docs.github.com/en/rest/overview/permissions-required-for-github-apps).
The following table shows the permissions granted to the `GITHUB_TOKEN` by default. People with admin permissions to an enterprise, organization, or repository, can set the default permissions to be either permissive or restricted. For information on how to set the default permissions for the `GITHUB_TOKEN` for your enterprise, organization, or repository, see [Enforcing policies for GitHub Actions in your enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise#enforcing-a-policy-for-workflow-permissions-in-your-enterprise), [Disabling or limiting GitHub Actions for your organization](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#setting-the-permissions-of-the-github_token-for-your-organization), or [Managing GitHub Actions settings for a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#setting-the-permissions-of-the-github_token-for-your-repository).
Scope | Default access  
(permissive) | Default access  
(restricted) | Maximum access for  
pull requests from  
public forked repositories  
---|---|---|---  
actions | read/write | none | read  
attestations | read/write | none | read  
checks | read/write | none | read  
contents | read/write | read | read  
deployments | read/write | none | read  
discussions | read/write | none | read  
id-token | none | none | none  
issues | read/write | none | read  
metadata | read | read | read  
models | read | none | none  
packages | read/write | read | read  
pages | read/write | none | read  
pull-requests | read/write | none | read  
security-events | read/write | none | read  
statuses | read/write | none | read  
  * When a workflow is triggered by the [`pull_request_target`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#pull_request_target) event, the `GITHUB_TOKEN` is granted read/write repository permission, even when it is triggered from a public fork. For more information, see [Events that trigger workflows](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#pull_request_target).
  * Private repositories can control whether pull requests from forks can run workflows, and can configure the permissions assigned to `GITHUB_TOKEN`. For more information, see [Managing GitHub Actions settings for a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#enabling-workflows-for-forks-of-private-repositories).
  * Workflow runs triggered by Dependabot pull requests run as if they are from a forked repository, and therefore use a read-only `GITHUB_TOKEN`. These workflow runs cannot access any secrets. For information about strategies to keep these workflows secure, see [Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions).


### [Modifying the permissions for the `GITHUB_TOKEN`](https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication#modifying-the-permissions-for-the-github_token)
You can modify the permissions for the `GITHUB_TOKEN` in individual workflow files. If the default permissions for the `GITHUB_TOKEN` are restrictive, you may have to elevate the permissions to allow some actions and commands to run successfully. If the default permissions are permissive, you can edit the workflow file to remove some permissions from the `GITHUB_TOKEN`. As a good security practice, you should grant the `GITHUB_TOKEN` the least required access.
You can see the permissions that `GITHUB_TOKEN` had for a specific job in the "Set up job" section of the workflow run log. For more information, see [Using workflow run logs](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/using-workflow-run-logs).
You can use the `permissions` key in your workflow file to modify permissions for the `GITHUB_TOKEN` for an entire workflow or for individual jobs. This allows you to configure the minimum required permissions for a workflow or job.
You can use the `permissions` key to add and remove read permissions for forked repositories, but typically you can't grant write access. The exception to this behavior is where an admin user has selected the **Send write tokens to workflows from pull requests** option in the GitHub Actions settings. For more information, see [Managing GitHub Actions settings for a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#enabling-workflows-for-private-repository-forks).
The two workflow examples earlier in this article show the `permissions` key being used at the job level, as it is best practice to limit the permissions' scope.
For full details of the `permissions` key, see [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#permissions).
Organization owners can prevent you from granting write access to the `GITHUB_TOKEN` at the repository level. For more information, see [Disabling or limiting GitHub Actions for your organization](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#setting-the-permissions-of-the-github_token-for-your-organization).
When the `permissions` key is used, all unspecified permissions are set to no access, with the exception of the `metadata` scope, which always gets read access.
#### [How the permissions are calculated for a workflow job](https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication#how-the-permissions-are-calculated-for-a-workflow-job)
The permissions for the `GITHUB_TOKEN` are initially set to the default setting for the enterprise, organization, or repository. If the default is set to the restricted permissions at any of these levels then this will apply to the relevant repositories. For example, if you choose the restricted default at the organization level then all repositories in that organization will use the restricted permissions as the default. The permissions are then adjusted based on any configuration within the workflow file, first at the workflow level and then at the job level. Finally, if the workflow was triggered by a pull request from a forked repository, and the **Send write tokens to workflows from pull requests** setting is not selected, the permissions are adjusted to change any write permissions to read only.
### [Granting additional permissions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication#granting-additional-permissions)
If you need a token that requires permissions that aren't available in the `GITHUB_TOKEN`, you can create a GitHub App and generate an installation access token within your workflow. For more information, see [Making authenticated API requests with a GitHub App in a GitHub Actions workflow](https://docs.github.com/en/apps/creating-github-apps/guides/making-authenticated-api-requests-with-a-github-app-in-a-github-actions-workflow). Alternatively, you can create a personal access token, store it as a secret in your repository, and use the token in your workflow with the `${{ secrets.SECRET_NAME }}` syntax. For more information, see [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) and [Using secrets in GitHub Actions](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions).
### [Further reading](https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication#further-reading)
  * [Rate limits for the REST API](https://docs.github.com/en/rest/overview/rate-limits-for-the-rest-api)


