  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Security](https://docs.github.com/en/actions/security-for-github-actions "Security")/
  * [Security harden deployments](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments "Security harden deployments")/
  * [OpenID Connect in JFrog](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-jfrog "OpenID Connect in JFrog")


# Configuring OpenID Connect in JFrog
Use OpenID Connect within your workflows to authenticate with JFrog.
## In this article
  * [Overview](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-jfrog#overview)
  * [Prerequisites](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-jfrog#prerequisites)
  * [Adding the identity provider to JFrog](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-jfrog#adding-the-identity-provider-to-jfrog)
  * [Updating your GitHub Actions workflow](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-jfrog#updating-your-github-actions-workflow)


## [Overview](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-jfrog#overview)
OpenID Connect (OIDC) allows your GitHub Actions workflows to authenticate with [JFrog](https://jfrog.com/) to download and publish artifacts without storing JFrog passwords, tokens, or API keys in GitHub.
This guide gives an overview of how to configure JFrog to trust GitHub's OIDC as a federated identity, and demonstrates how to use this configuration in a GitHub Actions workflow.
For an example GitHub Actions workflow, see [Sample GitHub Actions Integration](https://jfrog.com/help/r/jfrog-platform-administration-documentation/sample-github-actions-integration) in the JFrog documentation.
For an example GitHub Actions workflow using the JFrog CLI, see [`build-publish.yml`](https://github.com/jfrog/jfrog-github-oidc-example/blob/main/.github/workflows/build-publish.yml) in the `jfrog-github-oidc-example` repository.
## [Prerequisites](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-jfrog#prerequisites)
  * To learn the basic concepts of how GitHub uses OpenID Connect (OIDC), and its architecture and benefits, see [About security hardening with OpenID Connect](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect).
  * Before proceeding, you must plan your security strategy to ensure that access tokens are only allocated in a predictable way. To control how your cloud provider issues access tokens, you **must** define at least one condition, so that untrusted repositories can’t request access tokens for your cloud resources. For more information, see [About security hardening with OpenID Connect](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect#configuring-the-oidc-trust-with-the-cloud).
  * To be secure, you need to set a Claims JSON in JFrog when configuring identity mappings. For more information, see [AUTOTITLE](https://jfrog.com/help/r/jfrog-platform-administration-documentation/configure-identity-mappings) and [About security hardening with OpenID Connect](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect#customizing-the-token-claims).
For example, you can set `iss` to `https://token.actions.githubusercontent.com`, and the `repository` to something like "octo-org/octo-repo"`. This will ensure only Actions workflows from the specified repository will have access to your JFrog platform. The following is an example Claims JSON when configuring identity mappings.
JSON```
{
    "iss": "https://token.actions.githubusercontent.com",
    "repository": "octo-org/octo-repo"
}

```
```
{
    "iss": "https://token.actions.githubusercontent.com",
    "repository": "octo-org/octo-repo"
}

```



## [Adding the identity provider to JFrog](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-jfrog#adding-the-identity-provider-to-jfrog)
To use OIDC with JFrog, establish a trust relationship between GitHub Actions and the JFrog platform. For more information about this process, see [OpenID Connect Integration](https://jfrog.com/help/r/jfrog-platform-administration-documentation/openid-connect-integration) in the JFrog documentation.
  1. Sign in to your JFrog Platform.
  2. Configure trust between JFrog and your GitHub Actions workflows.
  3. Configure identity mappings.


## [Updating your GitHub Actions workflow](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-jfrog#updating-your-github-actions-workflow)
Once you establish a trust relationship between GitHub Actions and the JFrog platform, you can update your GitHub Actions workflow file.
In your GitHub Actions workflow file, ensure you are using the provider name and audience you configured in the JFrog Platform.
The following example uses the placeholder `YOUR_PROVIDER_NAME`.
```
- name: Fetch Access Token from Artifactory
        id: fetch_access_token
        env:
          ID_TOKEN: $
        run: |
          ACCESS_TOKEN=$(curl \
          -X POST \
          -H "Content-type: application/json" \
          https://example.jfrog.io/access/api/v1/oidc/token \
          -d \
          "{\"grant_type\": \"urn:ietf:params:oauth:grant-type:token-exchange\", \"subject_token_type\":\"urn:ietf:params:oauth:token-type:id_token\", \"subject_token\": \"$ID_TOKEN\", \"provider_name\": \"YOUR_PROVIDER_NAME\"}" | jq .access_token | tr -d '"')
          echo ACCESS_TOKEN=$ACCESS_TOKEN >> $GITHUB_OUTPUT

```

The following example shows part of a GitHub Actions workflow file using cURL.
```
- name: Get ID Token (cURL method)
        id: idtoken
        run: |
          ID_TOKEN=$(curl -sLS -H "User-Agent: actions/oidc-client" -H "Authorization: Bearer $ACTIONS_ID_TOKEN_REQUEST_TOKEN" \
          "${ACTIONS_ID_TOKEN_REQUEST_URL}&audience=jfrog-github" | jq .value | tr -d '"')
          echo "ID_TOKEN=${ID_TOKEN}" >> $GITHUB_OUTPUT

```

Alternatively, you can set the audience as an environment variable using the `env` context. For more information about the `env` context, see [Accessing contextual information about workflow runs](https://docs.github.com/en/actions/learn-github-actions/contexts#env-context).
When environments are used in workflows or in OIDC policies, we recommend adding protection rules to the environment for additional security. For example, you can configure deployment rules on an environment to restrict which branches and tags can deploy to the environment or access environment secrets. For more information, see [Managing environments for deployment](https://docs.github.com/en/actions/deployment/targeting-different-environments/managing-environments-for-deployment#deployment-protection-rules).
```
jobs:
  build:
    runs-on: ubuntu-latest
    env:
      OIDC_AUDIENCE: 'YOUR_AUDIENCE'

```

Then, in your workflow file, retrieve the value of the variables stored in the `env` context. The following example uses the `env` context to retrieve the OIDC audience.
```
- name: Get ID Token (using env context)
        uses: actions/github-script@v7
        id: idtoken
        with:
          script: |
            const coredemo = require('@actions/core');
            let id_token = await coredemo.getIDToken(process.env.OIDC_AUDIENCE);
            coredemo.setOutput('id_token', id_token);

```

