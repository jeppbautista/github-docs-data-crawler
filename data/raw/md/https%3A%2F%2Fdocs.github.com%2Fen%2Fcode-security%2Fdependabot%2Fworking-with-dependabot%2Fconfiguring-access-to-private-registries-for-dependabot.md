  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Dependabot](https://docs.github.com/en/code-security/dependabot "Dependabot")/
  * [Work with Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot "Work with Dependabot")/
  * [Configure access to private registries](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot "Configure access to private registries")


# Configuring access to private registries for Dependabot
You can configure Dependabot to access dependencies stored in private registries. You can store authentication information, like passwords and access tokens, as encrypted secrets and then reference these in the Dependabot configuration file. If you have registries on private networks, you can also configure Dependabot access when running Dependabot on self-hosted runners.
## Who can use this feature?
Users with **write** access
## In this article
  * [About private registries](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#about-private-registries)
  * [Configuring private registries](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#configuring-private-registries)
  * [Storing credentials for Dependabot to use](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#storing-credentials-for-dependabot-to-use)
  * [Configuring firewall IP rules](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#configuring-firewall-ip-rules)
  * [Allowing external code execution](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#allowing-external-code-execution)
  * [Supported private registeries](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#supported-private-registeries)


## [About private registries](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#about-private-registries)
Dependabot version updates keeps your dependencies up-to-date and Dependabot security updates updates vulnerable dependencies. Dependabot can access public registries. In addition, you can give Dependabot access to private package registries and private GitHub repositories so that you can keep your private and innersource dependencies as up-to-date and secure as your public dependencies.
In most ecosystems, private dependencies are usually published to private package registries. These private registries are similar to their public equivalents, but they require authentication.
For specific ecosystems, you can configure Dependabot to access _only_ private registries by removing calls to public registries. For more information, see [Removing Dependabot access to public registries](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/removing-dependabot-access-to-public-registries).
To allow Dependabot access to registries hosted privately or restricted to internal networks, configure Dependabot to run on GitHub Actions self-hosted runners. For more information, see [Managing Dependabot on self-hosted runners](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/managing-dependabot-on-self-hosted-runners).
## [Configuring private registries](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#configuring-private-registries)
You configure Dependabot's access to private registries in the `dependabot.yml` file. The top-level `registries` key is optional and specifies authentication details.
There are 2 locations in the `dependabot.yml` file where you can use the `registries` key:
  * At the top level, where you define the registries and their access information, if needed.
  * Within the `updates` blocks, where you can use `registries: "*"` to tell Dependabot to use any or all of the registries you defined at the top level.

```
# registries: gradle-artifactory - provides access details for the gradle-artifactory registry
# registries: "*" - allows Dependabot to use all the defined registries specified at the top level

version: 2
registries:
  gradle-artifactory:
    type: maven-repository
    url: https://acme.jfrog.io/artifactory/my-gradle-registry
    username: octocat
    password: ${{secrets.MY_ARTIFACTORY_PASSWORD}}
updates:
  - package-ecosystem: "gradle"
    directory: "/"
    registries: "*"
    schedule:
      interval: "monthly"


```

You use the following options to specify access settings. Registry settings must contain a `type` and a `url`, and typically either a `username` and `password` combination or a `token`.
Parameters | Purpose  
---|---  
`REGISTRY_NAME` |  **Required:** Defines an identifier for the registry.  
`type` |  **Required:** Identifies the type of registry.  
Authentication details |  **Required:** The parameters supported for supplying authentication details vary for registries of different types.  
`url` |  **Required:** The URL to use to access the dependencies in this registry. The protocol is optional. If not specified, `https://` is assumed. Dependabot adds or ignores trailing slashes as required.  
`replaces-base` | If the boolean value is `true`, Dependabot resolves dependencies using the specified `url` rather than the base URL of that ecosystem.  
`nuget-feed` doesn't support the `replaces-base` parameter.
For more information about the configuration options that are available and about the supported types, see [Dependabot options reference](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference#top-level-registries-key).
## [Storing credentials for Dependabot to use](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#storing-credentials-for-dependabot-to-use)
To give Dependabot access to the private registries supported by GitHub, you store the registry’s access token or secret in the secret store for your repository or organization.
### [About encrypted secrets for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#about-encrypted-secrets-for-dependabot)
Dependabot secrets are encrypted credentials that you create at either the organization level or the repository level. When you add a secret at the organization level, you can specify which repositories can access the secret. You can use secrets to allow Dependabot to update dependencies located in private package registries. When you add a secret, it's encrypted before it reaches GitHub and it remains encrypted until it's used by Dependabot to access a private package registry.
Dependabot secrets also include secrets that are used by GitHub Actions workflows triggered by Dependabot pull requests. Dependabot itself may not use these secrets, but the workflows require them. For more information, see [Troubleshooting Dependabot on GitHub Actions](https://docs.github.com/en/code-security/dependabot/troubleshooting-dependabot/troubleshooting-dependabot-on-github-actions#accessing-secrets).
After you add a Dependabot secret, you can reference it in the `dependabot.yml` configuration file like this: `${{secrets.NAME}}`, where "NAME" is the name you chose for the secret. For example:
YAML```
password: ${{secrets.MY_ARTIFACTORY_PASSWORD}}

```
```
password: ${{secrets.MY_ARTIFACTORY_PASSWORD}}

```

#### [Naming your secrets](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#naming-your-secrets)
The name of a Dependabot secret:
  * Can only contain alphanumeric characters (`[A-Z]`, `[0-9]`) or underscores (`_`). Spaces are not allowed. If you enter lowercase letters these are changed to uppercase.
  * Must not start with the `GITHUB_` prefix.
  * Must not start with a number.


### [Adding a repository secret for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#adding-a-repository-secret-for-dependabot)
To create secrets for a personal account repository, you must be the repository owner. To create secrets for an organization repository, you must have `admin` access.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Security" section of the sidebar, select **Dependabot**.
  4. Click **New repository secret**.
  5. Type a name for your secret in the **Name** input box.
  6. Enter the value for your secret.
  7. Click **Add secret**.
The name of the secret is listed on the Dependabot secrets page. You can click **Update** to change the secret value. You can click **Remove** to delete the secret.


### [Adding an organization secret for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#adding-an-organization-secret-for-dependabot)
When creating a secret in an organization, you can use a policy to limit which repositories can access that secret. For example, you can grant access to all repositories, or limit access to only private repositories or a specified list of repositories.
To create secrets at the organization level, you must have `admin` access.
  1. On GitHub, navigate to the main page of the organization.
  2. Under your organization name, click **Settings**.
![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](https://docs.github.com/assets/cb-49309/images/help/discussions/org-settings-global-nav-update.png)
  3. In the "Security" section of the sidebar, select **Dependabot**. Ignore the "Private Registries" option, this is used only by code scanning default setup.
  4. Click **New organization secret**.
  5. Type a name for your secret in the **Name** input box.
  6. Enter the **Value** for your secret.
  7. From the **Repository access** dropdown list, choose an access policy.
  8. If you chose **Selected repositories** :
     * Click 
     * In the dialog box, select the repositories that can access this secret.
     * Click **Update selection**.
  9. Click **Add secret**.
The name of the secret is listed on the Dependabot secrets page. You can click **Update** to change the secret value or its access policy. You can click **Remove** to delete the secret.


## [Configuring firewall IP rules](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#configuring-firewall-ip-rules)
You can add Dependabot-related IP addresses to your registries IP allow list.
If your private registry is configured with an IP allow list, you can find the IP addresses Dependabot uses to access the registry in the meta API endpoint, under the `dependabot` key. If you run Dependabot on GitHub Actions self-hosted runners, you should instead use the IP addresses under the `actions` key. For more information, see [REST API endpoints for meta data](https://docs.github.com/en/rest/meta/meta) and [About Dependabot on GitHub Actions runners](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/about-dependabot-on-github-actions-runners).
## [Allowing external code execution](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#allowing-external-code-execution)
When you give Dependabot access to one or more registries, external code execution is automatically disabled to protect your code from compromised packages. However, some version updates may fail.
If you need to allow Dependabot to access a private package registry and enable limited external code execution, you can set `insecure-external-code-execution` to `allow`. Allowing Dependabot to execute external code in the manifest during updates is not as scary as it sounds:
  * Any external code execution will only have access to the package managers in the registries associated with the enclosing `updates` setting.
  * There is no access allowed to any of the registries defined in the top level `registries` configuration.


It is common for tooling, such as `bundler`, `mix`, `pip`, and `swift`, to allow the execution of external code by default.
In this example, the configuration file allows Dependabot to access the `ruby-github` private package registry. In the same `updates`setting, `insecure-external-code-execution`is set to `allow`, which means that the code executed by dependencies will only access the `ruby-github` registry, and not the `dockerhub` registry.
YAML```
# Allow external code execution when updating dependencies from private registries

version: 2
registries:
  ruby-github:
    type: rubygems-server
    url: https://rubygems.pkg.github.com/octocat/github_api
    token: ${{secrets.MY_GITHUB_PERSONAL_TOKEN}}
updates:
  - package-ecosystem: "bundler"
    directory: "/rubygems-server"
    insecure-external-code-execution: allow
    registries: "*"
    schedule:
      interval: "monthly"

```
```
# Allow external code execution when updating dependencies from private registries

version: 2
registries:
  ruby-github:
    type: rubygems-server
    url: https://rubygems.pkg.github.com/octocat/github_api
    token: ${{secrets.MY_GITHUB_PERSONAL_TOKEN}}
updates:
  - package-ecosystem: "bundler"
    directory: "/rubygems-server"
    insecure-external-code-execution: allow
    registries: "*"
    schedule:
      interval: "monthly"

```

## [Supported private registeries](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#supported-private-registeries)
Examples of how to configure access to the private registries supported by Dependabot.
  * [`cargo-registry`](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#cargo-registry)
  * [`composer-repository`](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#composer-repository)
  * [`docker-registry`](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#docker-registry)
  * [`git`](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#git)
  * [`hex-organization`](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#hex-organization)
  * [`hex-repository`](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#hex-repository)
  * [`maven-repository`](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#maven-repository)
  * [`npm-registry`](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#npm-registry)
  * [`nuget-feed`](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#nuget-feed)
  * [`pub-repository`](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#pub-repository)
  * [`python-index`](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#python-index)
  * [`rubygems-server`](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#rubygems-server)
  * [`terraform-registry`](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#terraform-registry)


### [`cargo-registry`](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#cargo-registry)
The `cargo-registry` type supports a token.
This registry type will prefix-match the path provided in the `url` option. This means you can provide multiple credentials to the same host, which can be used to access distinct paths. However, if you don't have multiple registries on the same host, we recommend that you omit the path from the `url`, so that all paths to the registry will receive credentials.
```
registries:
  cargo-example:
    type: cargo-registry
    registry: "name-of-your-registry"
    url: https://cargo.cloudsmith.io/foobaruser/test/
    token: "Token ${{secrets.CARGO_TOKEN}}"

```

We tested this configuration against the `https://cargo.cloudsmith.io` private registry.
### [`composer-repository`](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#composer-repository)
The `composer-repository` type supports username and password. If the account is a GitHub account, you can use a GitHub personal access token in place of the password.
This registry type will prefix-match the path provided in the `url` option. This means you can provide multiple credentials to the same host, which can be used to access distinct paths. However, if you don't have multiple registries on the same host, we recommend that you omit the path from the `url`, so that all paths to the registry will receive credentials.
YAML```
registries:
  composer:
    type: composer-repository
    url: https://repo.packagist.com/example-company/
    username: octocat
    password: ${{secrets.MY_PACKAGIST_PASSWORD}}

```
```
registries:
  composer:
    type: composer-repository
    url: https://repo.packagist.com/example-company/
    username: octocat
    password: ${{secrets.MY_PACKAGIST_PASSWORD}}

```

### [`docker-registry`](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#docker-registry)
Dependabot works with any container registries that implement the OCI container registry spec. For more information, see <https://github.com/opencontainers/distribution-spec/blob/main/spec.md>. Dependabot supports authentication to private registries via a central token service or HTTP Basic Auth. For further details, see [Token Authentication Specification](https://docs.docker.com/registry/spec/auth/token/) in the Docker documentation and [Basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication) on Wikipedia.
The `docker-registry` type supports username and password. If the account is a GitHub account, you can use a GitHub personal access token in place of the password.
This registry type will prefix-match the path provided in the `url` option. This means you can provide multiple credentials to the same host, which can be used to access distinct paths. However, if you don't have multiple registries on the same host, we recommend that you omit the path from the `url`, so that all paths to the registry will receive credentials.
YAML```
registries:
  dockerhub:
    type: docker-registry
    url: https://registry.hub.docker.com
    username: octocat
    password: ${{secrets.MY_DOCKERHUB_PASSWORD}}
    replaces-base: true

```
```
registries:
  dockerhub:
    type: docker-registry
    url: https://registry.hub.docker.com
    username: octocat
    password: ${{secrets.MY_DOCKERHUB_PASSWORD}}
    replaces-base: true

```

The `docker-registry` type can also be used to pull from private Amazon ECR using static AWS credentials.
YAML```
registries:
  ecr-docker:
    type: docker-registry
    url: https://1234567890.dkr.ecr.us-east-1.amazonaws.com
    username: ${{secrets.ECR_AWS_ACCESS_KEY_ID}}
    password: ${{secrets.ECR_AWS_SECRET_ACCESS_KEY}}
    replaces-base: true

```
```
registries:
  ecr-docker:
    type: docker-registry
    url: https://1234567890.dkr.ecr.us-east-1.amazonaws.com
    username: ${{secrets.ECR_AWS_ACCESS_KEY_ID}}
    password: ${{secrets.ECR_AWS_SECRET_ACCESS_KEY}}
    replaces-base: true

```

### [`git`](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#git)
The `git` type supports username and password. If the account is a GitHub account, you can use a GitHub personal access token in place of the password.
YAML```
registries:
  github-octocat:
    type: git
    url: https://github.com
    username: x-access-token
    password: ${{secrets.MY_GITHUB_PERSONAL_TOKEN}}

```
```
registries:
  github-octocat:
    type: git
    url: https://github.com
    username: x-access-token
    password: ${{secrets.MY_GITHUB_PERSONAL_TOKEN}}

```

### [`helm-registry`](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#helm-registry)
Dependabot works with any OCI-compliant registries that implement the Open Container Initiative (OCI) Distribution Specification. For more information, see [Open Container Initiative Distribution Specification](https://github.com/opencontainers/distribution-spec/blob/main/spec.md) in the `opencontainers/distribution-spec` repository. Dependabot supports authentication to private registries via a central token service or HTTP Basic Auth. For further details, see [Token Authentication Specification](https://helm.sh/docs/helm/helm_registry_login/) in the Docker documentation and [Basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication) on Wikipedia.
The `helm-registry` type supports username and password. If the account is a GitHub account, you can use a GitHub personal access token in place of the password.
This registry type will prefix-match the path provided in the `url` option. This means you can provide multiple credentials to the same host, which can be used to access distinct paths. However, if you don't have multiple registries on the same host, we recommend that you omit the path from the `url`, so that all paths to the registry will receive credentials.
YAML```
registries:
  helm_registry:
    type: helm-registry
    url: https://registry.example.com
    username: octocat
    password: ${{secrets.MY_REGISTRY_PASSWORD}}

```
```
registries:
  helm_registry:
    type: helm-registry
    url: https://registry.example.com
    username: octocat
    password: ${{secrets.MY_REGISTRY_PASSWORD}}

```

### [`hex-organization`](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#hex-organization)
The `hex-organization` type supports organization and key.
This registry type will prefix-match the path provided in the `url` option. This means you can provide multiple credentials to the same host, which can be used to access distinct paths. However, if you don't have multiple registries on the same host, we recommend that you omit the path from the `url`, so that all paths to the registry will receive credentials.
YAML```
registries:
  github-hex-org:
    type: hex-organization
    organization: github
    key: ${{secrets.MY_HEX_ORGANIZATION_KEY}}

```
```
registries:
  github-hex-org:
    type: hex-organization
    organization: github
    key: ${{secrets.MY_HEX_ORGANIZATION_KEY}}

```

### [`hex-repository`](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#hex-repository)
The `hex-repository` type supports an authentication key.
`repo` is a required field, which must match the name of the repository used in your dependency declaration.
The `public-key-fingerprint` is an optional configuration field, representing the fingerprint of the public key for the Hex repository. `public-key-fingerprint` is used by Hex to establish trust with the private repository. The `public-key-fingerprint` field can be either listed in plaintext or stored as a Dependabot secret.
YAML```
registries:
   github-hex-repository:
     type: hex-repository
     repo: private-repo
     url: https://private-repo.example.com
     auth-key: ${{secrets.MY_AUTH_KEY}}
     public-key-fingerprint: ${{secrets.MY_PUBLIC_KEY_FINGERPRINT}}

```
```
registries:
   github-hex-repository:
     type: hex-repository
     repo: private-repo
     url: https://private-repo.example.com
     auth-key: ${{secrets.MY_AUTH_KEY}}
     public-key-fingerprint: ${{secrets.MY_PUBLIC_KEY_FINGERPRINT}}

```

### [`maven-repository`](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#maven-repository)
The `maven-repository` type supports username and password. If the account is a GitHub account, you can use a GitHub personal access token in place of the password.
This registry type will prefix-match the path provided in the `url` option. This means you can provide multiple credentials to the same host, which can be used to access distinct paths. However, if you don't have multiple registries on the same host, we recommend that you omit the path from the `url`, so that all paths to the registry will receive credentials.
YAML```
registries:
  maven-artifactory:
    type: maven-repository
    url: https://acme.jfrog.io/artifactory/my-maven-registry
    username: octocat
    password: ${{secrets.MY_ARTIFACTORY_PASSWORD}}

```
```
registries:
  maven-artifactory:
    type: maven-repository
    url: https://acme.jfrog.io/artifactory/my-maven-registry
    username: octocat
    password: ${{secrets.MY_ARTIFACTORY_PASSWORD}}

```

### [`npm-registry`](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#npm-registry)
The `npm-registry` type supports username and password, or token. If the account is a GitHub account, you can use a GitHub personal access token in place of the password.
When using username and password, your `.npmrc`'s auth token may contain a `base64` encoded `_password`; however, the password referenced in your Dependabot configuration file must be the original (unencoded) password.
When using `npm.pkg.github.com`, don't include a path. Instead use the `https://npm.pkg.github.com` URL without a path.
YAML```
registries:
  npm-npmjs:
    type: npm-registry
    url: https://registry.npmjs.org
    username: octocat
    password: ${{secrets.MY_NPM_PASSWORD}}  # Must be an unencoded password
    replaces-base: true

```
```
registries:
  npm-npmjs:
    type: npm-registry
    url: https://registry.npmjs.org
    username: octocat
    password: ${{secrets.MY_NPM_PASSWORD}}  # Must be an unencoded password
    replaces-base: true

```

YAML```
registries:
  npm-github:
    type: npm-registry
    url: https://npm.pkg.github.com
    token: ${{secrets.MY_GITHUB_PERSONAL_TOKEN}}
    replaces-base: true

```
```
registries:
  npm-github:
    type: npm-registry
    url: https://npm.pkg.github.com
    token: ${{secrets.MY_GITHUB_PERSONAL_TOKEN}}
    replaces-base: true

```

For security reasons, Dependabot does not set environment variables. Yarn (v2 and later) requires that any accessed environment variables are set. When accessing environment variables in your `.yarnrc.yml` file, you should provide a fallback value such as `${ENV_VAR-fallback}` or `${ENV_VAR:-fallback}`. For more information, see [Yarnrc files](https://yarnpkg.com/configuration/yarnrc) in the Yarn documentation.
### [`nuget-feed`](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#nuget-feed)
The `nuget-feed` type supports username and password, or token. If the account is a GitHub account, you can use a GitHub personal access token in place of the password.
`nuget-feed` doesn't support the `replaces-base` parameter.
YAML```
registries:
  nuget-example:
    type: nuget-feed
    url: https://nuget.example.com/v3/index.json
    username: octocat@example.com
    password: ${{secrets.MY_NUGET_PASSWORD}}

```
```
registries:
  nuget-example:
    type: nuget-feed
    url: https://nuget.example.com/v3/index.json
    username: octocat@example.com
    password: ${{secrets.MY_NUGET_PASSWORD}}

```

YAML```
registries:
  nuget-azure-devops:
    type: nuget-feed
    url: https://pkgs.dev.azure.com/.../_packaging/My_Feed/nuget/v3/index.json
    username: octocat@example.com
    password: ${{secrets.MY_AZURE_DEVOPS_TOKEN}}

```
```
registries:
  nuget-azure-devops:
    type: nuget-feed
    url: https://pkgs.dev.azure.com/.../_packaging/My_Feed/nuget/v3/index.json
    username: octocat@example.com
    password: ${{secrets.MY_AZURE_DEVOPS_TOKEN}}

```

### [`pub-repository`](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#pub-repository)
The `pub-repository` type supports a URL and a token.
YAML```
registries:
  my-pub-registry:
    type: pub-repository
    url: https://example-private-pub-repo.dev/optional-path
    token: ${{secrets.MY_PUB_TOKEN}}
updates:
  - package-ecosystem: "pub"
    directory: "/"
    schedule:
      interval: "weekly"
    registries:
      - my-pub-registry

```
```
registries:
  my-pub-registry:
    type: pub-repository
    url: https://example-private-pub-repo.dev/optional-path
    token: ${{secrets.MY_PUB_TOKEN}}
updates:
  - package-ecosystem: "pub"
    directory: "/"
    schedule:
      interval: "weekly"
    registries:
      - my-pub-registry

```

### [`python-index`](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#python-index)
The `python-index` type supports username and password, or token. If the account is a GitHub account, you can use a GitHub personal access token in place of the password.
This registry type will prefix-match the path provided in the `url` option. This means you can provide multiple credentials to the same host, which can be used to access distinct paths. However, if you don't have multiple registries on the same host, we recommend that you omit the path from the `url`, so that all paths to the registry will receive credentials.
YAML```
registries:
  python-example:
    type: python-index
    url: https://example.com/_packaging/my-feed/pypi/example
    username: octocat
    password: ${{secrets.MY_BASIC_AUTH_PASSWORD}}
    replaces-base: true

```
```
registries:
  python-example:
    type: python-index
    url: https://example.com/_packaging/my-feed/pypi/example
    username: octocat
    password: ${{secrets.MY_BASIC_AUTH_PASSWORD}}
    replaces-base: true

```

YAML```
registries:
  python-azure:
    type: python-index
    url: https://pkgs.dev.azure.com/octocat/_packaging/my-feed/pypi/example
    username: octocat@example.com
    password: ${{secrets.MY_AZURE_DEVOPS_TOKEN}}
    replaces-base: true

```
```
registries:
  python-azure:
    type: python-index
    url: https://pkgs.dev.azure.com/octocat/_packaging/my-feed/pypi/example
    username: octocat@example.com
    password: ${{secrets.MY_AZURE_DEVOPS_TOKEN}}
    replaces-base: true

```

### [`rubygems-server`](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#rubygems-server)
The `rubygems-server` type supports username and password, or token. If the account is a GitHub account, you can use a GitHub personal access token in place of the password.
This registry type will prefix-match the path provided in the `url` option. This means you can provide multiple credentials to the same host, which can be used to access distinct paths. However, if you don't have multiple registries on the same host, we recommend that you omit the path from the `url`, so that all paths to the registry will receive credentials.
YAML```
registries:
  ruby-example:
    type: rubygems-server
    url: https://rubygems.example.com
    username: octocat@example.com
    password: ${{secrets.MY_RUBYGEMS_PASSWORD}}
    replaces-base: true

```
```
registries:
  ruby-example:
    type: rubygems-server
    url: https://rubygems.example.com
    username: octocat@example.com
    password: ${{secrets.MY_RUBYGEMS_PASSWORD}}
    replaces-base: true

```

YAML```
registries:
  ruby-github:
    type: rubygems-server
    url: https://rubygems.pkg.github.com/octocat/github_api
    token: ${{secrets.MY_GITHUB_PERSONAL_TOKEN}}
    replaces-base: true

```
```
registries:
  ruby-github:
    type: rubygems-server
    url: https://rubygems.pkg.github.com/octocat/github_api
    token: ${{secrets.MY_GITHUB_PERSONAL_TOKEN}}
    replaces-base: true

```

### [`terraform-registry`](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#terraform-registry)
The `terraform-registry` type supports a token.
YAML```
registries:
  terraform-example:
    type: terraform-registry
    url: https://terraform.example.com
    token: ${{secrets.MY_TERRAFORM_API_TOKEN}}

```
```
registries:
  terraform-example:
    type: terraform-registry
    url: https://terraform.example.com
    token: ${{secrets.MY_TERRAFORM_API_TOKEN}}

```

