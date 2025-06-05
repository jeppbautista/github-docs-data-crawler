  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners "Self-hosted runners")/
  * [Actions Runner Controller](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller "Actions Runner Controller")/
  * [Authenticating](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/authenticating-to-the-github-api "Authenticating")


# Authenticating to the GitHub API
Learn how to authenticate to the GitHub API to use Actions Runner Controller with GitHub.
## In this article
  * [Overview](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/authenticating-to-the-github-api#overview)
  * [Authenticating ARC with a GitHub App](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/authenticating-to-the-github-api#authenticating-arc-with-a-github-app)
  * [Authenticating ARC with a personal access token (classic)](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/authenticating-to-the-github-api#authenticating-arc-with-a-personal-access-token-classic)
  * [Legal notice](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/authenticating-to-the-github-api#legal-notice)


[Legal notice](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/authenticating-to-the-github-api#legal-notice)
## [Overview](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/authenticating-to-the-github-api#overview)
You can authenticate Actions Runner Controller (ARC) to the GitHub API by using a GitHub App or by using a personal access token (classic).
You cannot authenticate using a GitHub App for runners at the enterprise level. For more information, see [Managing access to self-hosted runners using groups](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups#about-runner-groups).
## [Authenticating ARC with a GitHub App](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/authenticating-to-the-github-api#authenticating-arc-with-a-github-app)
  1. Create a GitHub App that is owned by an organization. For more information, see [Registering a GitHub App](https://docs.github.com/en/apps/creating-github-apps/creating-github-apps/creating-a-github-app). Configure the GitHub App as follows.
    1. For "Homepage URL," enter `https://github.com/actions/actions-runner-controller`.
    2. Under "Permissions," click **Repository permissions**. Then use the dropdown menus to select the following access permissions.
       * **Administration:** Read and write
`Administration: Read and write` is only required when configuring Actions Runner Controller to register at the repository scope. It is not required to register at the organization scope.
       * **Metadata:** Read-only
    3. Under "Permissions," click **Organization permissions**. Then use the dropdown menus to select the following access permissions.
       * **Self-hosted runners:** Read and write
  2. After creating the GitHub App, on the GitHub App's page, note the value for "App ID". You will use this value later.
  3. Under "Private keys", click **Generate a private key** , and save the `.pem` file. You will use this key later.
  4. In the menu at the top-left corner of the page, click **Install app** , and next to your organization, click **Install** to install the app on your organization.
  5. After confirming the installation permissions on your organization, note the app installation ID. You will use it later. You can find the app installation ID on the app installation page, which has the following URL format:
`https://github.com/organizations/ORGANIZATION/settings/installations/INSTALLATION_ID`
  6. Register the app ID, installation ID, and the downloaded `.pem` private key file from the previous steps to Kubernetes as a secret.
To create a Kubernetes secret with the values of your GitHub App, run the following command.
Create the secret in the same namespace where the `gha-runner-scale-set` chart is installed. In this example, the namespace is `arc-runners` to match the quickstart documentation. For more information, see [Quickstart for Actions Runner Controller](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/quickstart-for-actions-runner-controller#configuring-a-runner-scale-set).
Bash```
kubectl create secret generic pre-defined-secret \
   --namespace=arc-runners \
   --from-literal=github_app_id=123456 \
   --from-literal=github_app_installation_id=654321 \
   --from-literal=github_app_private_key='-----BEGIN RSA PRIVATE KEY-----********'

```
```
kubectl create secret generic pre-defined-secret \
   --namespace=arc-runners \
   --from-literal=github_app_id=123456 \
   --from-literal=github_app_installation_id=654321 \
   --from-literal=github_app_private_key='-----BEGIN RSA PRIVATE KEY-----********'

```

Then using the `githubConfigSecret` property in your copy of the [`values.yaml`](https://github.com/actions/actions-runner-controller/blob/master/charts/gha-runner-scale-set/values.yaml) file, pass the secret name as a reference.
```
githubConfigSecret: pre-defined-secret

```



For additional Helm configuration options, see [`values.yaml`](https://github.com/actions/actions-runner-controller/blob/master/charts/gha-runner-scale-set/values.yaml) in the ARC repository.
## [Authenticating ARC with a personal access token (classic)](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/authenticating-to-the-github-api#authenticating-arc-with-a-personal-access-token-classic)
ARC can use personal access tokens (classic) to register self-hosted runners.
  1. Create a personal access token (classic) with the required scopes. The required scopes are different depending on whether you are registering runners at the repository or organization level. For more information on how to create a personal access token (classic), see [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#creating-a-personal-access-token-classic).
The following is the list of required personal access token scopes for ARC runners.
     * Repository runners: `repo`
     * Organization runners: `admin:org`
  2. To create a Kubernetes secret with the value of your personal access token (classic), use the following command.
Create the secret in the same namespace where the `gha-runner-scale-set` chart is installed. In this example, the namespace is `arc-runners` to match the quickstart documentation. For more information, see [Quickstart for Actions Runner Controller](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/quickstart-for-actions-runner-controller#configuring-a-runner-scale-set).
Bash```
kubectl create secret generic pre-defined-secret \
   --namespace=arc-runners \
   --from-literal=github_token='YOUR-PAT'

```
```
kubectl create secret generic pre-defined-secret \
   --namespace=arc-runners \
   --from-literal=github_token='YOUR-PAT'

```

  3. In your copy of the [`values.yaml`](https://github.com/actions/actions-runner-controller/blob/master/charts/gha-runner-scale-set/values.yaml) file, pass the secret name as a reference.
```
githubConfigSecret: pre-defined-secret

```

For additional Helm configuration options, see [`values.yaml`](https://github.com/actions/actions-runner-controller/blob/master/charts/gha-runner-scale-set/values.yaml) in the ARC repository.


## [Legal notice](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/authenticating-to-the-github-api#legal-notice)
Portions have been adapted from <https://github.com/actions/actions-runner-controller/> under the Apache-2.0 license:
```
Copyright 2019 Moto Ishizawa

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

```

