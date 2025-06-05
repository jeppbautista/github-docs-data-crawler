  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Write workflows](https://docs.github.com/en/actions/writing-workflows "Write workflows")/
  * [Choose what workflows do](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does "Choose what workflows do")/
  * [Permissions for `GITHUB_TOKEN`](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/controlling-permissions-for-github_token "Permissions for `GITHUB_TOKEN`")


# Controlling permissions for GITHUB_TOKEN
Modify the default permissions granted to `GITHUB_TOKEN`.
## In this article
  * [Overview](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/controlling-permissions-for-github_token#overview)
  * [Defining access for the GITHUB_TOKEN permissions](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/controlling-permissions-for-github_token#defining-access-for-the-github_token-permissions)
  * [Setting the GITHUB_TOKEN permissions for all jobs in a workflow](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/controlling-permissions-for-github_token#setting-the-github_token-permissions-for-all-jobs-in-a-workflow)
  * [Setting the GITHUB_TOKEN permissions for a specific job](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/controlling-permissions-for-github_token#setting-the-github_token-permissions-for-a-specific-job)


## [Overview](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/controlling-permissions-for-github_token#overview)
You can use `permissions` to modify the default permissions granted to the `GITHUB_TOKEN`, adding or removing access as required, so that you only allow the minimum required access. For more information, see [Automatic token authentication](https://docs.github.com/en/actions/security-guides/automatic-token-authentication#permissions-for-the-github_token).
You can use `permissions` either as a top-level key, to apply to all jobs in the workflow, or within specific jobs. When you add the `permissions` key within a specific job, all actions and run commands within that job that use the `GITHUB_TOKEN` gain the access rights you specify. For more information, see [`jobs.<job_id>.permissions`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idpermissions).
For each of the available permissions, shown in the table below, you can assign one of the access levels: `read` (if applicable), `write`, or `none`. `write` includes `read`. If you specify the access for any of these permissions, all of those that are not specified are set to `none`.
Available permissions and details of what each allows an action to do:
Permission | Allows an action using `GITHUB_TOKEN` to  
---|---  
`actions` | Work with GitHub Actions. For example, `actions: write` permits an action to cancel a workflow run. For more information, see [Permissions required for GitHub Apps](https://docs.github.com/en/rest/overview/permissions-required-for-github-apps?apiVersion=2022-11-28#repository-permissions-for-actions).  
`attestations` | Work with artifact attestations. For example, `attestations: write` permits an action to generate an artifact attestation for a build. For more information, see [Using artifact attestations to establish provenance for builds](https://docs.github.com/en/actions/security-guides/using-artifact-attestations-to-establish-provenance-for-builds)  
`checks` | Work with check runs and check suites. For example, `checks: write` permits an action to create a check run. For more information, see [Permissions required for GitHub Apps](https://docs.github.com/en/rest/overview/permissions-required-for-github-apps?apiVersion=2022-11-28#repository-permissions-for-checks).  
`contents` | Work with the contents of the repository. For example, `contents: read` permits an action to list the commits, and `contents: write` allows the action to create a release. For more information, see [Permissions required for GitHub Apps](https://docs.github.com/en/rest/overview/permissions-required-for-github-apps?apiVersion=2022-11-28#repository-permissions-for-contents).  
`deployments` | Work with deployments. For example, `deployments: write` permits an action to create a new deployment. For more information, see [Permissions required for GitHub Apps](https://docs.github.com/en/rest/overview/permissions-required-for-github-apps?apiVersion=2022-11-28#repository-permissions-for-deployments).  
`discussions` | Work with GitHub Discussions. For example, `discussions: write` permits an action to close or delete a discussion. For more information, see [Using the GraphQL API for Discussions](https://docs.github.com/en/graphql/guides/using-the-graphql-api-for-discussions).  
`id-token` | Fetch an OpenID Connect (OIDC) token. This requires `id-token: write`. For more information, see [About security hardening with OpenID Connect](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect#updating-your-actions-for-oidc)  
`issues` | Work with issues. For example, `issues: write` permits an action to add a comment to an issue. For more information, see [Permissions required for GitHub Apps](https://docs.github.com/en/rest/overview/permissions-required-for-github-apps?apiVersion=2022-11-28#repository-permissions-for-issues).  
`models` | Generate AI inference responses with GitHub Models. For example, `models: read` permits an action to use the GitHub Models inference API. See [Prototyping with AI models](https://docs.github.com/en/github-models/prototyping-with-ai-models).  
`packages` | Work with GitHub Packages. For example, `packages: write` permits an action to upload and publish packages on GitHub Packages. For more information, see [About permissions for GitHub Packages](https://docs.github.com/en/packages/learn-github-packages/about-permissions-for-github-packages#about-scopes-and-permissions-for-package-registries).  
`pages` | Work with GitHub Pages. For example, `pages: write` permits an action to request a GitHub Pages build. For more information, see [Permissions required for GitHub Apps](https://docs.github.com/en/rest/overview/permissions-required-for-github-apps?apiVersion=2022-11-28#repository-permissions-for-pages).  
`pull-requests` | Work with pull requests. For example, `pull-requests: write` permits an action to add a label to a pull request. For more information, see [Permissions required for GitHub Apps](https://docs.github.com/en/rest/overview/permissions-required-for-github-apps?apiVersion=2022-11-28#repository-permissions-for-pull-requests).  
`security-events` | Work with GitHub code scanning and Dependabot alerts. For example, `security-events: read` permits an action to list the Dependabot alerts for the repository, and `security-events: write` allows an action to update the status of a code scanning alert. For more information, see [Repository permissions for 'Code scanning alerts'](https://docs.github.com/en/rest/overview/permissions-required-for-github-apps?apiVersion=2022-11-28#repository-permissions-for-code-scanning-alerts) and [Repository permissions for 'Dependabot alerts'](https://docs.github.com/en/rest/overview/permissions-required-for-github-apps?apiVersion=2022-11-28#repository-permissions-for-dependabot-alerts) in "Permissions required for GitHub Apps."  
`statuses` | Work with commit statuses. For example, `statuses:read` permits an action to list the commit statuses for a given reference. For more information, see [Permissions required for GitHub Apps](https://docs.github.com/en/rest/overview/permissions-required-for-github-apps?apiVersion=2022-11-28#repository-permissions-for-commit-statuses).  
## [Defining access for the `GITHUB_TOKEN` permissions](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/controlling-permissions-for-github_token#defining-access-for-the-github_token-permissions)
You can define the access that the `GITHUB_TOKEN` will permit by specifying `read`, `write`, or `none` as the value of the available permissions within the `permissions` key.
```
permissions:
  actions: read|write|none
  attestations: read|write|none
  checks: read|write|none
  contents: read|write|none
  deployments: read|write|none
  id-token: write|none
  issues: read|write|none
  models: read|none
  discussions: read|write|none
  packages: read|write|none
  pages: read|write|none
  pull-requests: read|write|none
  security-events: read|write|none
  statuses: read|write|none

```

If you specify the access for any of these permissions, all of those that are not specified are set to `none`.
You can use the following syntax to define one of `read-all` or `write-all` access for all of the available permissions:
```
permissions: read-all

```
```
permissions: write-all

```

You can use the following syntax to disable permissions for all of the available permissions:
```
permissions: {}

```

### [Changing the permissions in a forked repository](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/controlling-permissions-for-github_token#changing-the-permissions-in-a-forked-repository)
You can use the `permissions` key to add and remove read permissions for forked repositories, but typically you can't grant write access. The exception to this behavior is where an admin user has selected the **Send write tokens to workflows from pull requests** option in the GitHub Actions settings. For more information, see [Managing GitHub Actions settings for a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#enabling-workflows-for-private-repository-forks).
## [Setting the `GITHUB_TOKEN` permissions for all jobs in a workflow](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/controlling-permissions-for-github_token#setting-the-github_token-permissions-for-all-jobs-in-a-workflow)
You can specify `permissions` at the top level of a workflow, so that the setting applies to all jobs in the workflow.
### [Example: Setting the `GITHUB_TOKEN` permissions for an entire workflow](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/controlling-permissions-for-github_token#example-setting-the-github_token-permissions-for-an-entire-workflow)
This example shows permissions being set for the `GITHUB_TOKEN` that will apply to all jobs in the workflow. All permissions are granted read access.
```
name: "My workflow"

on: [ push ]

permissions: read-all

jobs:
  ...

```

## [Setting the `GITHUB_TOKEN` permissions for a specific job](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/controlling-permissions-for-github_token#setting-the-github_token-permissions-for-a-specific-job)
For a specific job, you can use `jobs.<job_id>.permissions` to modify the default permissions granted to the `GITHUB_TOKEN`, adding or removing access as required, so that you only allow the minimum required access. For more information, see [Automatic token authentication](https://docs.github.com/en/actions/security-guides/automatic-token-authentication#permissions-for-the-github_token).
By specifying the permission within a job definition, you can configure a different set of permissions for the `GITHUB_TOKEN` for each job, if required. Alternatively, you can specify the permissions for all jobs in the workflow. For information on defining permissions at the workflow level, see [`permissions`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#permissions).
### [Example: Setting the `GITHUB_TOKEN` permissions for one job in a workflow](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/controlling-permissions-for-github_token#example-setting-the-github_token-permissions-for-one-job-in-a-workflow)
This example shows permissions being set for the `GITHUB_TOKEN` that will only apply to the job named `stale`. Write access is granted for the `issues` and `pull-requests` permissions. All other permissions will have no access.
```
jobs:
  stale:
    runs-on: ubuntu-latest

    permissions:
      issues: write
      pull-requests: write

    steps:
      - uses: actions/stale@v9

```

