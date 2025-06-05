  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Security](https://docs.github.com/en/actions/security-for-github-actions "Security")/
  * [Security harden deployments](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments "Security harden deployments")/
  * [OpenID Connect in AWS](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services "OpenID Connect in AWS")


# Configuring OpenID Connect in Amazon Web Services
Use OpenID Connect within your workflows to authenticate with Amazon Web Services.
## In this article
  * [Overview](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services#overview)
  * [Prerequisites](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services#prerequisites)
  * [Adding the identity provider to AWS](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services#adding-the-identity-provider-to-aws)
  * [Updating your GitHub Actions workflow](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services#updating-your-github-actions-workflow)
  * [Further reading](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services#further-reading)


## [Overview](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services#overview)
OpenID Connect (OIDC) allows your GitHub Actions workflows to access resources in Amazon Web Services (AWS), without needing to store the AWS credentials as long-lived GitHub secrets.
This guide explains how to configure AWS to trust GitHub's OIDC as a federated identity, and includes a workflow example for the [`aws-actions/configure-aws-credentials`](https://github.com/aws-actions/configure-aws-credentials) that uses tokens to authenticate to AWS and access resources.
Support for custom claims for OIDC is unavailable in AWS.
## [Prerequisites](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services#prerequisites)
  * To learn the basic concepts of how GitHub uses OpenID Connect (OIDC), and its architecture and benefits, see [About security hardening with OpenID Connect](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect).
  * Before proceeding, you must plan your security strategy to ensure that access tokens are only allocated in a predictable way. To control how your cloud provider issues access tokens, you **must** define at least one condition, so that untrusted repositories can’t request access tokens for your cloud resources. For more information, see [About security hardening with OpenID Connect](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect#configuring-the-oidc-trust-with-the-cloud).


## [Adding the identity provider to AWS](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services#adding-the-identity-provider-to-aws)
To add the GitHub OIDC provider to IAM, see the [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html).
  * For the provider URL: Use `https://token.actions.githubusercontent.com`
  * For the "Audience": Use `sts.amazonaws.com` if you are using the [official action](https://github.com/aws-actions/configure-aws-credentials).


### [Configuring the role and trust policy](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services#configuring-the-role-and-trust-policy)
To configure the role and trust in IAM, see the AWS documentation [Configure AWS Credentials for GitHub Actions](https://github.com/aws-actions/configure-aws-credentials#configure-aws-credentials-for-github-actions) and [Configuring a role for GitHub OIDC identity provider](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp_oidc.html#idp_oidc_Create_GitHub).
AWS Identity and Access Management (IAM) recommends that users evaluate the IAM condition key, `token.actions.githubusercontent.com:sub`, in the trust policy of any role that trusts GitHub’s OIDC identity provider (IdP). Evaluating this condition key in the role trust policy limits which GitHub actions are able to assume the role.
Edit the trust policy, adding the `sub` field to the validation conditions. For example:
JSON```
"Condition": {
  "StringEquals": {
    "token.actions.githubusercontent.com:aud": "sts.amazonaws.com",
    "token.actions.githubusercontent.com:sub": "repo:octo-org/octo-repo:ref:refs/heads/octo-branch"
  }
}

```
```
"Condition": {
  "StringEquals": {
    "token.actions.githubusercontent.com:aud": "sts.amazonaws.com",
    "token.actions.githubusercontent.com:sub": "repo:octo-org/octo-repo:ref:refs/heads/octo-branch"
  }
}

```

If you use a workflow with an environment, the `sub` field must reference the environment name: `repo:ORG-NAME/REPO-NAME:environment:ENVIRONMENT-NAME`. For more information, see [About security hardening with OpenID Connect](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect#understanding-the-oidc-token).
When environments are used in workflows or in OIDC policies, we recommend adding protection rules to the environment for additional security. For example, you can configure deployment rules on an environment to restrict which branches and tags can deploy to the environment or access environment secrets. For more information, see [Managing environments for deployment](https://docs.github.com/en/actions/deployment/targeting-different-environments/managing-environments-for-deployment#deployment-protection-rules).
JSON```
"Condition": {
  "StringEquals": {
    "token.actions.githubusercontent.com:aud": "sts.amazonaws.com",
    "token.actions.githubusercontent.com:sub": "repo:octo-org/octo-repo:environment:prod"
  }
}

```
```
"Condition": {
  "StringEquals": {
    "token.actions.githubusercontent.com:aud": "sts.amazonaws.com",
    "token.actions.githubusercontent.com:sub": "repo:octo-org/octo-repo:environment:prod"
  }
}

```

In the following example, `StringLike` is used with a wildcard operator (`*`) to allow any branch, pull request merge branch, or environment from the `octo-org/octo-repo` organization and repository to assume a role in AWS.
JSON```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "arn:aws:iam::123456123456:oidc-provider/token.actions.githubusercontent.com"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringLike": {
                    "token.actions.githubusercontent.com:sub": "repo:octo-org/octo-repo:*"
                },
                "StringEquals": {
                    "token.actions.githubusercontent.com:aud": "sts.amazonaws.com"
                }
            }
        }
    ]
}

```
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "arn:aws:iam::123456123456:oidc-provider/token.actions.githubusercontent.com"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringLike": {
                    "token.actions.githubusercontent.com:sub": "repo:octo-org/octo-repo:*"
                },
                "StringEquals": {
                    "token.actions.githubusercontent.com:aud": "sts.amazonaws.com"
                }
            }
        }
    ]
}

```

## [Updating your GitHub Actions workflow](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services#updating-your-github-actions-workflow)
To update your workflows for OIDC, you will need to make two changes to your YAML:
  1. Add permissions settings for the token.
  2. Use the [`aws-actions/configure-aws-credentials`](https://github.com/aws-actions/configure-aws-credentials) action to exchange the OIDC token (JWT) for a cloud access token.


### [Adding permissions settings](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services#adding-permissions-settings)
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
### [Requesting the access token](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services#requesting-the-access-token)
The `aws-actions/configure-aws-credentials` action receives a JWT from the GitHub OIDC provider, and then requests an access token from AWS. For more information, see the AWS [documentation](https://github.com/aws-actions/configure-aws-credentials).
  * `BUCKET-NAME`: Replace this with the name of your S3 bucket.
  * `AWS-REGION`: Replace this with the name of your AWS region.
  * `ROLE-TO-ASSUME`: Replace this with your AWS role. For example, `arn:aws:iam::1234567890:role/example-role`


YAML```
# Sample workflow to access AWS resources when workflow is tied to branch
# The workflow Creates static website using aws s3
name: AWS example workflow
on:
  push
env:
  BUCKET_NAME : "BUCKET-NAME"
  AWS_REGION : "AWS-REGION"
# permission can be added at job level or workflow level
permissions:
  id-token: write   # This is required for requesting the JWT
  contents: read    # This is required for actions/checkout
jobs:
  S3PackageUpload:
    runs-on: ubuntu-latest
    steps:
      - name: Git clone the repository
        uses: actions/checkout@v4
      - name: configure aws credentials
        uses: aws-actions/configure-aws-credentials@e3dd6a429d7300a6a4c196c26e071d42e0343502
        with:
          role-to-assume: ROLE-TO-ASSUME
          role-session-name: samplerolesession
          aws-region: ${{ env.AWS_REGION }}
      # Upload a file to AWS s3
      - name: Copy index.html to s3
        run: |
          aws s3 cp ./index.html s3://${{ env.BUCKET_NAME }}/

```
```
# Sample workflow to access AWS resources when workflow is tied to branch
# The workflow Creates static website using aws s3
name: AWS example workflow
on:
  push
env:
  BUCKET_NAME : "BUCKET-NAME"
  AWS_REGION : "AWS-REGION"
# permission can be added at job level or workflow level
permissions:
  id-token: write   # This is required for requesting the JWT
  contents: read    # This is required for actions/checkout
jobs:
  S3PackageUpload:
    runs-on: ubuntu-latest
    steps:
      - name: Git clone the repository
        uses: actions/checkout@v4
      - name: configure aws credentials
        uses: aws-actions/configure-aws-credentials@e3dd6a429d7300a6a4c196c26e071d42e0343502
        with:
          role-to-assume: ROLE-TO-ASSUME
          role-session-name: samplerolesession
          aws-region: ${{ env.AWS_REGION }}
      # Upload a file to AWS s3
      - name: Copy index.html to s3
        run: |
          aws s3 cp ./index.html s3://${{ env.BUCKET_NAME }}/

```

## [Further reading](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services#further-reading)
  * [Using OpenID Connect with reusable workflows](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/using-openid-connect-with-reusable-workflows)
  * [Communicating with self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/communicating-with-self-hosted-runners)


