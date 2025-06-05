  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Security](https://docs.github.com/en/actions/security-for-github-actions "Security")/
  * [Security harden deployments](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments "Security harden deployments")/
  * [OpenID Connect in Google Cloud Platform](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-google-cloud-platform "OpenID Connect in Google Cloud Platform")


# Configuring OpenID Connect in Google Cloud Platform
Use OpenID Connect within your workflows to authenticate with Google Cloud Platform.
## In this article
  * [Overview](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-google-cloud-platform#overview)
  * [Prerequisites](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-google-cloud-platform#prerequisites)
  * [Adding a Google Cloud Workload Identity Provider](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-google-cloud-platform#adding-a-google-cloud-workload-identity-provider)
  * [Updating your GitHub Actions workflow](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-google-cloud-platform#updating-your-github-actions-workflow)
  * [Further reading](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-google-cloud-platform#further-reading)


## [Overview](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-google-cloud-platform#overview)
OpenID Connect (OIDC) allows your GitHub Actions workflows to access resources in Google Cloud Platform (GCP), without needing to store the GCP credentials as long-lived GitHub secrets.
This guide gives an overview of how to configure GCP to trust GitHub's OIDC as a federated identity, and includes a workflow example for the [`google-github-actions/auth`](https://github.com/google-github-actions/auth) action that uses tokens to authenticate to GCP and access resources.
## [Prerequisites](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-google-cloud-platform#prerequisites)
  * To learn the basic concepts of how GitHub uses OpenID Connect (OIDC), and its architecture and benefits, see [About security hardening with OpenID Connect](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect).
  * Before proceeding, you must plan your security strategy to ensure that access tokens are only allocated in a predictable way. To control how your cloud provider issues access tokens, you **must** define at least one condition, so that untrusted repositories can’t request access tokens for your cloud resources. For more information, see [About security hardening with OpenID Connect](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect#configuring-the-oidc-trust-with-the-cloud).


## [Adding a Google Cloud Workload Identity Provider](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-google-cloud-platform#adding-a-google-cloud-workload-identity-provider)
To configure the OIDC identity provider in GCP, you will need to perform the following configuration. For instructions on making these changes, refer to [the GCP documentation](https://github.com/google-github-actions/auth).
  1. Create a new identity pool.
  2. Configure the mapping and add conditions.
  3. Connect the new pool to a service account.


Additional guidance for configuring the identity provider:
  * For security hardening, make sure you've reviewed [Configuring the OIDC trust with the cloud](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect#configuring-the-oidc-trust-with-the-cloud). For an example, see [Configuring the subject in your cloud provider](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect#configuring-the-subject-in-your-cloud-provider).
  * For the service account to be available for configuration, it needs to be assigned to the `roles/iam.workloadIdentityUser` role. For more information, see [the GCP documentation](https://cloud.google.com/iam/docs/workload-identity-federation?_ga=2.114275588.-285296507.1634918453#conditions).
  * The Issuer URL to use: `https://token.actions.githubusercontent.com`


## [Updating your GitHub Actions workflow](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-google-cloud-platform#updating-your-github-actions-workflow)
To update your workflows for OIDC, you will need to make two changes to your YAML:
  1. Add permissions settings for the token.
  2. Use the [`google-github-actions/auth`](https://github.com/google-github-actions/auth) action to exchange the OIDC token (JWT) for a cloud access token.


When environments are used in workflows or in OIDC policies, we recommend adding protection rules to the environment for additional security. For example, you can configure deployment rules on an environment to restrict which branches and tags can deploy to the environment or access environment secrets. For more information, see [Managing environments for deployment](https://docs.github.com/en/actions/deployment/targeting-different-environments/managing-environments-for-deployment#deployment-protection-rules).
### [Adding permissions settings](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-google-cloud-platform#adding-permissions-settings)
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
### [Requesting the access token](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-google-cloud-platform#requesting-the-access-token)
The `google-github-actions/auth` action receives a JWT from the GitHub OIDC provider, and then requests an access token from GCP. For more information, see the GCP [documentation](https://github.com/google-github-actions/auth).
This example has a job called `Get_OIDC_ID_token` that uses actions to request a list of services from GCP.
  * `WORKLOAD-IDENTITY-PROVIDER`: Replace this with the path to your identity provider in GCP. For example, `projects/example-project-id/locations/global/workloadIdentityPools/name-of-pool/providers/name-of-provider`
  * `SERVICE-ACCOUNT`: Replace this with the name of your service account in GCP.


This action exchanges a GitHub OIDC token for a Google Cloud access token, using [Workload Identity Federation](https://cloud.google.com/iam/docs/workload-identity-federation).
YAML```
name: List services in GCP
on:
  pull_request:
    branches:
      - main

permissions:
  id-token: write

jobs:
  Get_OIDC_ID_token:
    runs-on: ubuntu-latest
    steps:
    - id: 'auth'
      name: 'Authenticate to GCP'
      uses: 'google-github-actions/auth@f1e2d3c4b5a6f7e8d9c0b1a2c3d4e5f6a7b8c9d0'
      with:
          create_credentials_file: 'true'
          workload_identity_provider: 'WORKLOAD-IDENTITY-PROVIDER'
          service_account: 'SERVICE-ACCOUNT'
    - id: 'gcloud'
      name: 'gcloud'
      run: |-
        gcloud auth login --brief --cred-file="${{ steps.auth.outputs.credentials_file_path }}"
        gcloud services list

```
```
name: List services in GCP
on:
  pull_request:
    branches:
      - main

permissions:
  id-token: write

jobs:
  Get_OIDC_ID_token:
    runs-on: ubuntu-latest
    steps:
    - id: 'auth'
      name: 'Authenticate to GCP'
      uses: 'google-github-actions/auth@f1e2d3c4b5a6f7e8d9c0b1a2c3d4e5f6a7b8c9d0'
      with:
          create_credentials_file: 'true'
          workload_identity_provider: 'WORKLOAD-IDENTITY-PROVIDER'
          service_account: 'SERVICE-ACCOUNT'
    - id: 'gcloud'
      name: 'gcloud'
      run: |-
        gcloud auth login --brief --cred-file="${{ steps.auth.outputs.credentials_file_path }}"
        gcloud services list

```

## [Further reading](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-google-cloud-platform#further-reading)
  * [Using OpenID Connect with reusable workflows](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/using-openid-connect-with-reusable-workflows)
  * [Communicating with self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/communicating-with-self-hosted-runners)


