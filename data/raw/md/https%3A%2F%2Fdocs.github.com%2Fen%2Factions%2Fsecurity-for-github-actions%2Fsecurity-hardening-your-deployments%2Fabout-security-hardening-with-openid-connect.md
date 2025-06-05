  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Security](https://docs.github.com/en/actions/security-for-github-actions "Security")/
  * [Security harden deployments](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments "Security harden deployments")/
  * [Security hardening with OpenID Connect](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect "Security hardening with OpenID Connect")


# About security hardening with OpenID Connect
OpenID Connect allows your workflows to exchange short-lived tokens directly from your cloud provider.
## In this article
  * [Overview of OpenID Connect](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#overview-of-openid-connect)
  * [Configuring the OIDC trust with the cloud](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#configuring-the-oidc-trust-with-the-cloud)
  * [Updating your actions for OIDC](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#updating-your-actions-for-oidc)
  * [Customizing the token claims](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#customizing-the-token-claims)
  * [Updating your workflows for OIDC](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#updating-your-workflows-for-oidc)
  * [Enabling OpenID Connect for Python package publishing](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#enabling-openid-connect-for-python-package-publishing)
  * [Enabling OpenID Connect for your cloud provider](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#enabling-openid-connect-for-your-cloud-provider)
  * [Debugging your OIDC claims](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#debugging-your-oidc-claims)


## [Overview of OpenID Connect](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#overview-of-openid-connect)
GitHub Actions workflows are often designed to access a cloud provider (such as AWS, Azure, GCP, or HashiCorp Vault) in order to deploy software or use the cloud's services. Before the workflow can access these resources, it will supply credentials, such as a password or token, to the cloud provider. These credentials are usually stored as a secret in GitHub, and the workflow presents this secret to the cloud provider every time it runs.
However, using hardcoded secrets requires you to create credentials in the cloud provider and then duplicate them in GitHub as a secret.
With OpenID Connect (OIDC), you can take a different approach by configuring your workflow to request a short-lived access token directly from the cloud provider. Your cloud provider also needs to support OIDC on their end, and you must configure a trust relationship that controls which workflows are able to request the access tokens. Providers that currently support OIDC include Amazon Web Services, Azure, Google Cloud Platform, and HashiCorp Vault, among others.
### [Benefits of using OIDC](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#benefits-of-using-oidc)
By updating your workflows to use OIDC tokens, you can adopt the following good security practices:
  * **No cloud secrets:** You won't need to duplicate your cloud credentials as long-lived GitHub secrets. Instead, you can configure the OIDC trust on your cloud provider, and then update your workflows to request a short-lived access token from the cloud provider through OIDC.
  * **Authentication and authorization management:** You have more granular control over how workflows can use credentials, using your cloud provider's authentication (authN) and authorization (authZ) tools to control access to cloud resources.
  * **Rotating credentials:** With OIDC, your cloud provider issues a short-lived access token that is only valid for a single job, and then automatically expires.


### [Getting started with OIDC](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#getting-started-with-oidc)
The following diagram gives an overview of how GitHub's OIDC provider integrates with your workflows and cloud provider:
![Diagram of how a cloud provider integrates with GitHub Actions through access tokens and JSON web token cloud role IDs.](https://docs.github.com/assets/cb-63262/images/help/actions/oidc-architecture.png)
  1. In your cloud provider, create an OIDC trust between your cloud role and your GitHub workflow(s) that need access to the cloud.
  2. Every time your job runs, GitHub's OIDC Provider auto-generates an OIDC token. This token contains multiple claims to establish a security-hardened and verifiable identity about the specific workflow that is trying to authenticate.
  3. You could include a step or action in your job to request this token from GitHub's OIDC provider, and present it to the cloud provider.
  4. Once the cloud provider successfully validates the claims presented in the token, it then provides a short-lived cloud access token that is available only for the duration of the job.


## [Configuring the OIDC trust with the cloud](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#configuring-the-oidc-trust-with-the-cloud)
When you configure your cloud to trust GitHub's OIDC provider, you **must** add conditions that filter incoming requests, so that untrusted repositories or workflows can’t request access tokens for your cloud resources:
  * Before granting an access token, your cloud provider checks that the [`subject`](https://openid.net/specs/openid-connect-core-1_0.html#StandardClaims) and other claims used to set conditions in its trust settings match those in the request's JSON Web Token (JWT). As a result, you must take care to correctly define the _subject_ and other conditions in your cloud provider.
  * The OIDC trust configuration steps and the syntax to set conditions for cloud roles (using _Subject_ and other claims) will vary depending on which cloud provider you're using. For some examples, see [Example subject claims](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#example-subject-claims).


### [Understanding the OIDC token](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#understanding-the-oidc-token)
Each job requests an OIDC token from GitHub's OIDC provider, which responds with an automatically generated JSON web token (JWT) that is unique for each workflow job where it is generated. When the job runs, the OIDC token is presented to the cloud provider. To validate the token, the cloud provider checks if the OIDC token's subject and other claims are a match for the conditions that were preconfigured on the cloud role's OIDC trust definition.
The following example OIDC token uses a subject (`sub`) that references a job environment named `prod` in the `octo-org/octo-repo` repository.
```
{
  "typ": "JWT",
  "alg": "RS256",
  "x5t": "example-thumbprint",
  "kid": "example-key-id"
}
{
  "jti": "example-id",
  "sub": "repo:octo-org/octo-repo:environment:prod",
  "environment": "prod",
  "aud": "https://github.com/octo-org",
  "ref": "refs/heads/main",
  "sha": "example-sha",
  "repository": "octo-org/octo-repo",
  "repository_owner": "octo-org",
  "actor_id": "12",
  "repository_visibility": "private",
  "repository_id": "74",
  "repository_owner_id": "65",
  "run_id": "example-run-id",
  "run_number": "10",
  "run_attempt": "2",
  "runner_environment": "github-hosted",
  "actor": "octocat",
  "workflow": "example-workflow",
  "head_ref": "",
  "base_ref": "",
  "event_name": "workflow_dispatch",
  "ref_type": "branch",
  "job_workflow_ref": "octo-org/octo-automation/.github/workflows/oidc.yml@refs/heads/main",
  "iss": "https://token.actions.githubusercontent.com",
  "nbf": 1632492967,
  "exp": 1632493867,
  "iat": 1632493567
}

```

To see all the claims supported by GitHub's OIDC provider, review the `claims_supported` entries at <https://token.actions.githubusercontent.com/.well-known/openid-configuration>.
The token includes the standard audience, issuer, and subject claims.
Claim | Claim type | Description  
---|---|---  
`aud` | Audience | By default, this is the URL of the repository owner, such as the organization that owns the repository. You can set a custom audience with a toolkit command: [`core.getIDToken(audience)`](https://www.npmjs.com/package/@actions/core/v/1.6.0)  
`iss` | Issuer | The issuer of the OIDC token: `https://token.actions.githubusercontent.com`  
`sub` | Subject | Defines the subject claim that is to be validated by the cloud provider. This setting is essential for making sure that access tokens are only allocated in a predictable way.  
The OIDC token also includes additional standard JOSE header parameters and claims.
Header Parameter | Parameter type | Description  
---|---|---  
`alg` | Algorithm | The algorithm used by the OIDC provider.  
`kid` | Key identifier | Unique key for the OIDC token.  
`typ` | Type | Describes the type of token. This is a JSON Web Token (JWT).  
Claim | Claim type | Description  
---|---|---  
`exp` | Expires at | Identifies the expiry time of the JWT.  
`iat` | Issued at | The time when the JWT was issued.  
`jti` | JWT token identifier | Unique identifier for the OIDC token.  
`nbf` | Not before | JWT is not valid for use before this time.  
The token also includes custom claims provided by GitHub.
Claim | Description  
---|---  
`actor` | The personal account that initiated the workflow run.  
`actor_id` | The ID of personal account that initiated the workflow run.  
`base_ref` | The target branch of the pull request in a workflow run.  
`environment` | The name of the environment used by the job. If the `environment` claim is included (also via `include_claim_keys`), an environment is required and must be provided.  
`event_name` | The name of the event that triggered the workflow run.  
`head_ref` | The source branch of the pull request in a workflow run.  
`job_workflow_ref` | For jobs using a reusable workflow, the ref path to the reusable workflow. For more information, see [Using OpenID Connect with reusable workflows](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/using-openid-connect-with-reusable-workflows).  
`job_workflow_sha` | For jobs using a reusable workflow, the commit SHA for the reusable workflow file.  
`ref` |  _(Reference)_ The git ref that triggered the workflow run.  
`ref_type` | The type of `ref`, for example: "branch".  
`repository_visibility` | The visibility of the repository where the workflow is running. Accepts the following values: `internal`, `private`, or `public`.  
`repository` | The repository from where the workflow is running.  
`repository_id` | The ID of the repository from where the workflow is running.  
`repository_owner` | The name of the organization in which the `repository` is stored.  
`repository_owner_id` | The ID of the organization in which the `repository` is stored.  
`run_id` | The ID of the workflow run that triggered the workflow.  
`run_number` | The number of times this workflow has been run.  
`run_attempt` | The number of times this workflow run has been retried.  
`runner_environment` | The type of runner used by the job. Accepts the following values: `github-hosted` or `self-hosted`.  
`workflow` | The name of the workflow.  
`workflow_ref` | The ref path to the workflow. For example, `octocat/hello-world/.github/workflows/my-workflow.yml@refs/heads/my_branch`.  
`workflow_sha` | The commit SHA for the workflow file.  
### [Defining trust conditions on cloud roles using OIDC claims](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#defining-trust-conditions-on-cloud-roles-using-oidc-claims)
With OIDC, a GitHub Actions workflow requires a token in order to access resources in your cloud provider. The workflow requests an access token from your cloud provider, which checks the details presented by the JWT. If the trust configuration in the JWT is a match, your cloud provider responds by issuing a temporary token to the workflow, which can then be used to access resources in your cloud provider. You can configure your cloud provider to only respond to requests that originate from a specific organization's repository. You can also specify additional conditions, described below.
Audience and Subject claims are typically used in combination while setting conditions on the cloud role/resources to scope its access to the GitHub workflows.
  * **Audience:** By default, this value uses the URL of the organization or repository owner. This can be used to set a condition that only the workflows in the specific organization can access the cloud role.
  * **Subject:** By default, has a predefined format and is a concatenation of some of the key metadata about the workflow, such as the GitHub organization, repository, branch, or associated [`job`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idenvironment) environment. See [Example subject claims](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#example-subject-claims) to see how the subject claim is assembled from concatenated metadata.


If you need more granular trust conditions, you can customize the subject (`sub`) claim that's included with the JWT. For more information, see [Customizing the token claims](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#customizing-the-token-claims).
There are also many additional claims supported in the OIDC token that can be used for setting these conditions. In addition, your cloud provider could allow you to assign a role to the access tokens, letting you specify even more granular permissions.
To control how your cloud provider issues access tokens, you **must** define at least one condition, so that untrusted repositories can’t request access tokens for your cloud resources.
### [Example subject claims](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#example-subject-claims)
The following examples demonstrate how to use "Subject" as a condition, and explain how the "Subject" is assembled from concatenated metadata. The [subject](https://openid.net/specs/openid-connect-core-1_0.html#StandardClaims) uses information from the [`job` context](https://docs.github.com/en/actions/learn-github-actions/contexts#job-context), and instructs your cloud provider that access token requests may only be granted for requests from workflows running in specific branches, environments. The following sections describe some common subjects you can use.
#### [Filtering for a specific environment](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#filtering-for-a-specific-environment)
The subject claim includes the environment name when the job references an environment.
You can configure a subject that filters for a specific [environment](https://docs.github.com/en/actions/deployment/targeting-different-environments/managing-environments-for-deployment) name. In this example, the workflow run must have originated from a job that has an environment named `Production`, in a repository named `octo-repo` that is owned by the `octo-org` organization:
  * Syntax: `repo:ORG-NAME/REPO-NAME:environment:ENVIRONMENT-NAME`
  * Example: `repo:octo-org/octo-repo:environment:Production`


#### [Filtering for `pull_request` events](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#filtering-for-pull_request-events)
The subject claim includes the `pull_request` string when the workflow is triggered by a pull request event, but only if the job doesn't reference an environment.
You can configure a subject that filters for the [`pull_request`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#pull_request) event. In this example, the workflow run must have been triggered by a `pull_request` event in a repository named `octo-repo` that is owned by the `octo-org` organization:
  * Syntax: `repo:ORG-NAME/REPO-NAME:pull_request`
  * Example: `repo:octo-org/octo-repo:pull_request`


#### [Filtering for a specific branch](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#filtering-for-a-specific-branch)
The subject claim includes the branch name of the workflow, but only if the job doesn't reference an environment, and if the workflow is not triggered by a pull request event.
You can configure a subject that filters for a specific branch name. In this example, the workflow run must have originated from a branch named `demo-branch`, in a repository named `octo-repo` that is owned by the `octo-org` organization:
  * Syntax: `repo:ORG-NAME/REPO-NAME:ref:refs/heads/BRANCH-NAME`
  * Example: `repo:octo-org/octo-repo:ref:refs/heads/demo-branch`


#### [Filtering for a specific tag](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#filtering-for-a-specific-tag)
The subject claim includes the tag name of the workflow, but only if the job doesn't reference an environment, and if the workflow is not triggered by a pull request event.
You can create a subject that filters for specific tag. In this example, the workflow run must have originated with a tag named `demo-tag`, in a repository named `octo-repo` that is owned by the `octo-org` organization:
  * Syntax: `repo:ORG-NAME/REPO-NAME:ref:refs/tags/TAG-NAME`
  * Example: `repo:octo-org/octo-repo:ref:refs/tags/demo-tag`


### [Configuring the subject in your cloud provider](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#configuring-the-subject-in-your-cloud-provider)
To configure the subject in your cloud provider's trust relationship, you must add the subject string to its trust configuration. The following examples demonstrate how various cloud providers can accept the same `repo:octo-org/octo-repo:ref:refs/heads/demo-branch` subject in different ways:
Cloud provider | Example  
---|---  
Amazon Web Services | `"token.actions.githubusercontent.com:sub": "repo:octo-org/octo-repo:ref:refs/heads/demo-branch"`  
Azure | `repo:octo-org/octo-repo:ref:refs/heads/demo-branch`  
Google Cloud Platform | `(assertion.sub=='repo:octo-org/octo-repo:ref:refs/heads/demo-branch')`  
HashiCorp Vault | `bound_subject="repo:octo-org/octo-repo:ref:refs/heads/demo-branch"`  
For more information, see the guides listed in [Enabling OpenID Connect for your cloud provider](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#enabling-openid-connect-for-your-cloud-provider).
## [Updating your actions for OIDC](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#updating-your-actions-for-oidc)
To update your custom actions to authenticate using OIDC, you can use `getIDToken()` from the Actions toolkit to request a JWT from GitHub's OIDC provider. For more information, see "OIDC Token" in the [npm package documentation](https://www.npmjs.com/package/@actions/core/v/1.6.0).
You could also use a `curl` command to request the JWT, using the following environment variables.
Variable | Description  
---|---  
`ACTIONS_ID_TOKEN_REQUEST_URL` | The URL for GitHub's OIDC provider.  
`ACTIONS_ID_TOKEN_REQUEST_TOKEN` | Bearer token for the request to the OIDC provider.  
For example:
Shell```
curl -H "Authorization: bearer $ACTIONS_ID_TOKEN_REQUEST_TOKEN" "$ACTIONS_ID_TOKEN_REQUEST_URL&audience=api://AzureADTokenExchange"

```
```
curl -H "Authorization: bearer $ACTIONS_ID_TOKEN_REQUEST_TOKEN" "$ACTIONS_ID_TOKEN_REQUEST_URL&audience=api://AzureADTokenExchange"

```

### [Adding permissions settings](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#adding-permissions-settings)
The job or workflow run requires a `permissions` setting with [`id-token: write`](https://docs.github.com/en/actions/security-guides/automatic-token-authentication#permissions-for-the-github_token) to allow GitHub's OIDC provider to create a JSON Web Token for every run. You won't be able to request the OIDC JWT ID token if the `permissions` for `id-token` is not set to `write`, however this value doesn't imply granting write access to any resources, only being able to fetch and set the OIDC token for an action or step to enable authenticating with a short-lived access token. Any actual trust setting is defined using OIDC claims, for more information see [About security hardening with OpenID Connect](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#configuring-the-oidc-trust-with-the-cloud).
The `id-token: write` setting allows the JWT to be requested from GitHub's OIDC provider using one of these approaches:
  * Using environment variables on the runner (`ACTIONS_ID_TOKEN_REQUEST_URL` and `ACTIONS_ID_TOKEN_REQUEST_TOKEN`).
  * Using `getIDToken()` from the Actions toolkit.


If you need to fetch an OIDC token for a workflow, then the permission can be set at the workflow level. For example:
YAML```
permissions:
  id-token: write # This is required for requesting the JWT
  contents: read  # This is required for actions/checkout

```
```
permissions:
  id-token: write # This is required for requesting the JWT
  contents: read  # This is required for actions/checkout

```

If you only need to fetch an OIDC token for a single job, then this permission can be set within that job. For example:
YAML```
permissions:
  id-token: write # This is required for requesting the JWT

```
```
permissions:
  id-token: write # This is required for requesting the JWT

```

You may need to specify additional permissions here, depending on your workflow's requirements.
For reusable workflows that are owned by the same user, organization, or enterprise as the caller workflow, the OIDC token generated in the reusable workflow can be accessed from the caller's context. For reusable workflows outside your enterprise or organization, the `permissions` setting for `id-token` should be explicitly set to `write` at the caller workflow level or in the specific job that calls the reusable workflow. This ensures that the OIDC token generated in the reusable workflow is only allowed to be consumed in the caller workflows when intended.
For more information, see [Reusing workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows).
## [Customizing the token claims](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#customizing-the-token-claims)
You can security harden your OIDC configuration by customizing the claims that are included with the JWT. These customizations allow you to define more granular trust conditions on your cloud roles when allowing your workflows to access resources hosted in the cloud:
  * You can customize values for `audience` claims. See [Customizing the `audience` value](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#customizing-the-audience-value).
  * You can customize the format of your OIDC configuration by setting conditions on the subject (`sub`) claim that require JWT tokens to originate from a specific repository, reusable workflow, or other source.
  * You can define granular OIDC policies by using additional OIDC token claims, such as `repository_id` and `repository_visibility`. See [Understanding the OIDC token](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#understanding-the-oidc-token).


### [Customizing the `audience` value](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#customizing-the-audience-value)
When you use custom actions in your workflows, those actions may use the GitHub Actions Toolkit to enable you to supply a custom value for the `audience` claim. Some cloud providers also use this in their official login actions to enforce a default value for the `audience` claim. For example, the [GitHub Action for Azure Login](https://github.com/Azure/login/blob/master/action.yml) provides a default `aud` value of `api://AzureADTokenExchange`, or it allows you to set a custom `aud` value in your workflows. For more information on the GitHub Actions Toolkit, see the [OIDC token](https://github.com/actions/toolkit/tree/main/packages/core#oidc-token) section in the documentation.
If you do not want to use the default `aud` value offered by an action, you can provide a custom value for the `audience` claim. This allows you to set a condition that only workflows in a specific repository or organization can access the cloud role. If the action you are using supports this, you can use the `with` keyword in your workflow to pass a custom `aud` value to the action. For more information, see [Metadata syntax for GitHub Actions](https://docs.github.com/en/actions/creating-actions/metadata-syntax-for-github-actions#inputs).
### [Customizing the subject claims for an organization or repository](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#customizing-the-subject-claims-for-an-organization-or-repository)
To help improve security, compliance, and standardization, you can customize the standard claims to suit your required access conditions. If your cloud provider supports conditions on subject claims, you can create a condition that checks whether the `sub` value matches the path of the reusable workflow, such as `"job_workflow_ref:octo-org/octo-automation/.github/workflows/oidc.yml@refs/heads/main"`. The exact format will vary depending on your cloud provider's OIDC configuration. To configure the matching condition on GitHub, you can use the REST API to require that the `sub` claim must always include a specific custom claim, such as `job_workflow_ref`. You can use the REST API to apply a customization template for the OIDC subject claim; for example, you can require that the `sub` claim within the OIDC token must always include a specific custom claim, such as `job_workflow_ref`. For more information, see [REST API endpoints for GitHub Actions OIDC](https://docs.github.com/en/rest/actions/oidc).
When the organization template is applied, it will not affect any workflows already using OIDC unless their repository has opted in to custom organization templates. For all repositories, existing and new, the repository owner will need to use the repository-level REST API to opt in to receive this configuration by setting `use_default` to `false`. Alternatively, the repository owner could use the REST API to apply a different configuration specific to the repository. For more information, see [REST API endpoints for GitHub Actions OIDC](https://docs.github.com/en/rest/actions/oidc#set-the-customization-template-for-an-oidc-subject-claim-for-a-repository).
Customizing the claims results in a new format for the entire `sub` claim, which replaces the default predefined `sub` format in the token described in [About security hardening with OpenID Connect](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect#example-subject-claims).
The `sub` claim uses the shortened form `repo` (for example, `repo:ORG-NAME/REPO-NAME`) instead of `repository` to reference the repository. Any `:` within the context value will be replaced with `%3A`.
The following example templates demonstrate various ways to customize the subject claim. To configure these settings on GitHub, admins use the REST API to specify a list of claims that must be included in the subject (`sub`) claim.
To apply this configuration, submit a request to the API endpoint and include the required configuration in the request body. For organizations, see [REST API endpoints for GitHub Actions OIDC](https://docs.github.com/en/rest/actions/oidc#set-the-customization-template-for-an-oidc-subject-claim-for-an-organization), and for repositories, see [REST API endpoints for GitHub Actions OIDC](https://docs.github.com/en/rest/actions/oidc#set-the-customization-template-for-an-oidc-subject-claim-for-a-repository).
To customize your subject claims, you should first create a matching condition in your cloud provider's OIDC configuration, before customizing the configuration using the REST API. Once the configuration is completed, each time a new job runs, the OIDC token generated during that job will follow the new customization template. If the matching condition doesn't exist in the cloud provider's OIDC configuration before the job runs, the generated token might not be accepted by the cloud provider, since the cloud conditions may not be synchronized.
#### [Example: Allowing repository based on visibility and owner](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#example-allowing-repository-based-on-visibility-and-owner)
This example template allows the `sub` claim to have a new format, using `repository_owner` and `repository_visibility`:
```
{
   "include_claim_keys": [
       "repository_owner",
       "repository_visibility"
   ]
}

```

In your cloud provider's OIDC configuration, configure the `sub` condition to require that claims must include specific values for `repository_owner` and `repository_visibility`. For example: `"sub": "repository_owner:monalisa:repository_visibility:private"`. The approach lets you restrict cloud role access to only private repositories within an organization or enterprise.
#### [Example: Allowing access to all repositories with a specific owner](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#example-allowing-access-to-all-repositories-with-a-specific-owner)
This example template enables the `sub` claim to have a new format with only the value of `repository_owner`.
To apply this configuration, submit a request to the API endpoint and include the required configuration in the request body. For organizations, see [REST API endpoints for GitHub Actions OIDC](https://docs.github.com/en/rest/actions/oidc#set-the-customization-template-for-an-oidc-subject-claim-for-an-organization), and for repositories, see [REST API endpoints for GitHub Actions OIDC](https://docs.github.com/en/rest/actions/oidc#set-the-customization-template-for-an-oidc-subject-claim-for-a-repository).
```
{
   "include_claim_keys": [
       "repository_owner"
   ]
}


```

In your cloud provider's OIDC configuration, configure the `sub` condition to require that claims must include a specific value for `repository_owner`. For example: `"sub": "repository_owner:monalisa"`
#### [Example: Requiring a reusable workflow](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#example-requiring-a-reusable-workflow)
This example template allows the `sub` claim to have a new format that contains the value of the `job_workflow_ref` claim. This enables an enterprise to use [reusable workflows](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect#example-subject-claims) to enforce consistent deployments across its organizations and repositories.
To apply this configuration, submit a request to the API endpoint and include the required configuration in the request body. For organizations, see [REST API endpoints for GitHub Actions OIDC](https://docs.github.com/en/rest/actions/oidc#set-the-customization-template-for-an-oidc-subject-claim-for-an-organization), and for repositories, see [REST API endpoints for GitHub Actions OIDC](https://docs.github.com/en/rest/actions/oidc#set-the-customization-template-for-an-oidc-subject-claim-for-a-repository).
```
  {
     "include_claim_keys": [
         "job_workflow_ref"
     ]
  }

```

In your cloud provider's OIDC configuration, configure the `sub` condition to require that claims must include a specific value for `job_workflow_ref`. For example: `"sub": "job_workflow_ref:octo-org/octo-automation/.github/workflows/oidc.yml@refs/heads/main"`.
#### [Example: Requiring a reusable workflow and other claims](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#example-requiring-a-reusable-workflow-and-other-claims)
The following example template combines the requirement of a specific reusable workflow with additional claims.
To apply this configuration, submit a request to the API endpoint and include the required configuration in the request body. For organizations, see [REST API endpoints for GitHub Actions OIDC](https://docs.github.com/en/rest/actions/oidc#set-the-customization-template-for-an-oidc-subject-claim-for-an-organization), and for repositories, see [REST API endpoints for GitHub Actions OIDC](https://docs.github.com/en/rest/actions/oidc#set-the-customization-template-for-an-oidc-subject-claim-for-a-repository).
This example also demonstrates how to use `"context"` to define your conditions. This is the part that follows the repository in the [default `sub` format](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect#example-subject-claims). For example, when the job references an environment, the context contains: `environment:ENVIRONMENT-NAME`.
```
{
   "include_claim_keys": [
       "repo",
       "context",
       "job_workflow_ref"
   ]
}

```

In your cloud provider's OIDC configuration, configure the `sub` condition to require that claims must include specific values for `repo`, `context`, and `job_workflow_ref`.
This customization template requires that the `sub` uses the following format: `repo:ORG-NAME/REPO-NAME:environment:ENVIRONMENT-NAME:job_workflow_ref:REUSABLE-WORKFLOW-PATH`. For example: `"sub": "repo:octo-org/octo-repo:environment:prod:job_workflow_ref:octo-org/octo-automation/.github/workflows/oidc.yml@refs/heads/main"`
#### [Example: Granting access to a specific repository](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#example-granting-access-to-a-specific-repository)
This example template lets you grant cloud access to all the workflows in a specific repository, across all branches/tags and environments.
To apply this configuration, submit a request to the API endpoint and include the required configuration in the request body. For organizations, see [REST API endpoints for GitHub Actions OIDC](https://docs.github.com/en/rest/actions/oidc#set-the-customization-template-for-an-oidc-subject-claim-for-an-organization), and for repositories, see [REST API endpoints for GitHub Actions OIDC](https://docs.github.com/en/rest/actions/oidc#set-the-customization-template-for-an-oidc-subject-claim-for-a-repository).
```
{
   "include_claim_keys": [
       "repo"
   ]
}

```

In your cloud provider's OIDC configuration, configure the `sub` condition to require a `repo` claim that matches the required value.
#### [Example: Using system-generated GUIDs](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#example-using-system-generated-guids)
This example template enables predictable OIDC claims with system-generated GUIDs that do not change between renames of entities (such as renaming a repository).
To apply this configuration, submit a request to the API endpoint and include the required configuration in the request body. For organizations, see [REST API endpoints for GitHub Actions OIDC](https://docs.github.com/en/rest/actions/oidc#set-the-customization-template-for-an-oidc-subject-claim-for-an-organization), and for repositories, see [REST API endpoints for GitHub Actions OIDC](https://docs.github.com/en/rest/actions/oidc#set-the-customization-template-for-an-oidc-subject-claim-for-a-repository).
```
  {
     "include_claim_keys": [
         "repository_id"
     ]
  }

```

In your cloud provider's OIDC configuration, configure the `sub` condition to require a `repository_id` claim that matches the required value.
or:
```
{
   "include_claim_keys": [
       "repository_owner_id"
   ]
}

```

In your cloud provider's OIDC configuration, configure the `sub` condition to require a `repository_owner_id` claim that matches the required value.
#### [Example: Context value with `:`](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#example-context-value-with-)
This example demonstrates how to handle context value with `:`. For example, when the job references an environment named `production:eastus`.
To apply this configuration, submit a request to the API endpoint and include the required configuration in the request body. For organizations, see [REST API endpoints for GitHub Actions OIDC](https://docs.github.com/en/rest/actions/oidc#set-the-customization-template-for-an-oidc-subject-claim-for-an-organization), and for repositories, see [REST API endpoints for GitHub Actions OIDC](https://docs.github.com/en/rest/actions/oidc#set-the-customization-template-for-an-oidc-subject-claim-for-a-repository).
```
{
   "include_claim_keys": [
       "environment",
       "repository_owner"
   ]
}

```

In your cloud provider's OIDC configuration, configure the `sub` condition to require that claims must include a specific value for `environment` and `repository_owner`. For example: `"sub": "environment:production%3Aeastus:repository_owner:octo-org"`.
#### [Resetting organization template customizations](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#resetting-organization-template-customizations)
This example template resets the subject claims to the default format. This template effectively opts out of any organization-level customization policy.
To apply this configuration, submit a request to the API endpoint and include the required configuration in the request body. For organizations, see [REST API endpoints for GitHub Actions OIDC](https://docs.github.com/en/rest/actions/oidc#set-the-customization-template-for-an-oidc-subject-claim-for-an-organization), and for repositories, see [REST API endpoints for GitHub Actions OIDC](https://docs.github.com/en/rest/actions/oidc#set-the-customization-template-for-an-oidc-subject-claim-for-a-repository).
```
{
   "include_claim_keys": [
       "repo",
       "context"
   ]
}

```

In your cloud provider's OIDC configuration, configure the `sub` condition to require that claims must include specific values for `repo` and `context`.
#### [Resetting repository template customizations](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#resetting-repository-template-customizations)
All repositories in an organization have the ability to opt in or opt out of (organization and repository-level) customized `sub` claim templates.
To opt out a repository and reset back to the default `sub` claim format, a repository administrator must use the REST API endpoint at [REST API endpoints for GitHub Actions OIDC](https://docs.github.com/en/rest/actions/oidc#set-the-customization-template-for-an-oidc-subject-claim-for-a-repository).
To configure repositories to use the default `sub` claim format, use the `PUT /repos/{owner}/{repo}/actions/oidc/customization/sub` REST API endpoint at with the following request body.
```
{
   "use_default": true
}

```

#### [Example: Configuring a repository to use an organization template](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#example-configuring-a-repository-to-use-an-organization-template)
Once an organization has created a customized `sub` claim template, the REST API can be used to programmatically apply the template to repositories within the organization. A repository administrator can configure their repository to use the template created by the administrator of their organization.
To configure the repository to use the organization's template, a repository admin must use the `PUT /repos/{owner}/{repo}/actions/oidc/customization/sub` REST API endpoint at with the following request body. For more information, see [REST API endpoints for GitHub Actions OIDC](https://docs.github.com/en/rest/actions/oidc#set-the-customization-template-for-an-oidc-subject-claim-for-a-repository).
```
{
   "use_default": false
}

```

## [Updating your workflows for OIDC](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#updating-your-workflows-for-oidc)
You can now update your YAML workflows to use OIDC access tokens instead of secrets. Popular cloud providers have published their official login actions that make it easy for you to get started with OIDC. For more information about updating your workflows, see the cloud-specific guides listed below in [Enabling OpenID Connect for your cloud provider](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#enabling-openid-connect-for-your-cloud-provider).
## [Enabling OpenID Connect for Python package publishing](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#enabling-openid-connect-for-python-package-publishing)
You can use a GitHub Actions workflow in a repository as a trusted publisher for a PyPI project. Using a workflow as a trusted publisher allows OIDC access tokens to be exchanged for temporary PyPI API tokens. For more information, see [Configuring OpenID Connect in PyPI](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-pypi) and [Publishing to PyPI with a Trusted Publisher](https://docs.pypi.org/trusted-publishers/) in the PyPI documentation.
## [Enabling OpenID Connect for your cloud provider](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#enabling-openid-connect-for-your-cloud-provider)
To enable and configure OIDC for your specific cloud provider, see the following guides:
  * [Configuring OpenID Connect in Amazon Web Services](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services)
  * [Configuring OpenID Connect in Azure](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-azure)
  * [Configuring OpenID Connect in Google Cloud Platform](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-google-cloud-platform)
  * [Configuring OpenID Connect in HashiCorp Vault](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-hashicorp-vault)


To enable and configure OIDC for another cloud provider, see the following guide:
  * [Configuring OpenID Connect in cloud providers](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-cloud-providers)


## [Debugging your OIDC claims](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#debugging-your-oidc-claims)
You can use the [`github/actions-oidc-debugger`](https://github.com/github/actions-oidc-debugger) action to visualize the claims that would be sent, before integrating with a cloud provider. This action requests a JWT and prints the claims included within the JWT that were received from GitHub Actions.
