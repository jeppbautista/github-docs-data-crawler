  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Dependabot](https://docs.github.com/en/code-security/dependabot "Dependabot")/
  * [Work with Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot "Work with Dependabot")/
  * [Guidance for configuring private registries](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot "Guidance for configuring private registries")


# Guidance for the configuration of private registries for Dependabot
This article contains detailed information about configuring private registries, as well as commands you can run from the command line to configure your package managers locally.
## Who can use this feature?
Users with **write** access
## In this article
  * [About configuring private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#about-configuring-private-registries-for-dependabot)
  * [Configuring package managers](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#configuring-package-managers)
  * [Configuring private registry hosts](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#configuring-private-registry-hosts)


## [About configuring private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#about-configuring-private-registries-for-dependabot)
This article contains recommendations and advice to help you configure Dependabot to access your private registry, along with:
  * Detailed snippets of the `dependabot.yml` configuration file for each package manager.
  * Important limitations or caveats.
  * Steps explaining how to test that the configuration is working.
  * Extra configuration options, wherever appropriate (for example, npm has a configuration file that needs to be set).
  * Advice about configuring registry hosts.


You'll find detailed guidance for the setup of the following package managers:
  * [Bun](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#bun)
  * [Bundler](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#bundler)
  * [Cargo](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#cargo)
  * [Docker](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#docker)
  * [Docker Compose](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#docker-compose)
  * [Gradle](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#gradle)
  * [Helm Charts](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#helm-charts)
  * [Maven](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#maven)
  * [npm](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#npm)
  * [NuGet](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#nuget)
  * [pub](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#pub)
  * [Python](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#python)
  * [Yarn](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#yarn)


You'll also find recommendations for the setup of the following registry hosts:
  * [Artifactory](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#artifactory)
  * [Azure Artifacts](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#azure-artifacts)
  * [Cloudsmith](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#cloudsmith)
  * [GitHub Packages registry](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#github-packages-registry)
  * [Nexus](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#nexus)
  * [ProGet](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#proget)


To have greater control over Dependabot's access to your private registries and internal network resources, you can configure Dependabot to run on GitHub Actions self-hosted runners. For more information, see [About Dependabot on GitHub Actions runners](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/about-dependabot-on-github-actions-runners) and [Managing Dependabot on self-hosted runners](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/managing-dependabot-on-self-hosted-runners).
## [Configuring package managers](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#configuring-package-managers)
### [Bun](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#bun)
Bun adheres to the same configuration guidelines as npm. Note that the `.npmrc` file is not required, but can be provided in order to customize the configuration. For detailed steps, see [npm](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#npm).
### [Bundler](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#bundler)
Supported by Artifactory, Artifacts, Cloudsmith, GitHub Packages registry, Nexus, and ProGet.
You can authenticate with either a username and password, or a token. For more information, see `rubygems-server` in [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#rubygems-server).
Snippet of a `dependabot.yml` file using a username and password.
YAML```
registries:
  ruby-example:
    type: rubygems-server
    url: https://rubygems.example.com
    username: octocat@example.com
    password: ${{secrets.MY_RUBYGEMS_PASSWORD}}

```
```
registries:
  ruby-example:
    type: rubygems-server
    url: https://rubygems.example.com
    username: octocat@example.com
    password: ${{secrets.MY_RUBYGEMS_PASSWORD}}

```

The snippet of `dependabot.yml` file below uses a token. For this type of registry using the GitHub Packages registry (`xyz.pkg.github.com`), the token is in fact a GitHub personal access token (PAT) .
YAML```
registries:
  ruby-github:
    type: rubygems-server
    url: https://rubygems.pkg.github.com/octocat/github_api
    token: ${{secrets.MY_GITHUB_PERSONAL_TOKEN}}

```
```
registries:
  ruby-github:
    type: rubygems-server
    url: https://rubygems.pkg.github.com/octocat/github_api
    token: ${{secrets.MY_GITHUB_PERSONAL_TOKEN}}

```

#### [Notes](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#notes)
Dependencies sourced directly from a GitHub repository give Dependabot access to the repository through the GitHub UI. For information about allowing Dependabot to access private GitHub dependencies, see [Allowing Dependabot to access private dependencies](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-security-and-analysis-settings-for-your-organization#allowing-dependabot-to-access-private-dependencies).
### [Cargo](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#cargo)
Cargo supports username, password and token-based authentication. For more information, see `cargo-registry` in [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#cargo-registry).
The snippet below shows a `dependabot.yml` file configuration that uses a token.
```
registries:
  cargo-example:
    type: cargo-registry
    registry: "name-of-your-registry"
    url: https://cargo.cloudsmith.io/foobaruser/test/
    token: "Token ${{secrets.CARGO_TOKEN}}"

```

We tested this configuration against the `https://cargo.cloudsmith.io` private registry.
### [Docker](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#docker)
Docker supports using a username and password for registries. For more information, see `docker-registry` in [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#docker-registry).
Snippet of `dependabot.yml` file using a username and password.
YAML```
registries:
  dockerhub:
    type: docker-registry
    url: https://registry.hub.docker.com
    username: octocat
    password: ${{secrets.MY_DOCKERHUB_PASSWORD}}

```
```
registries:
  dockerhub:
    type: docker-registry
    url: https://registry.hub.docker.com
    username: octocat
    password: ${{secrets.MY_DOCKERHUB_PASSWORD}}

```

`docker-registry` can also be used to pull from private Amazon ECR using static AWS credentials.
YAML```
registries:
  ecr-docker:
    type: docker-registry
    url: https://1234567890.dkr.ecr.us-east-1.amazonaws.com
    username: ${{secrets.ECR_AWS_ACCESS_KEY_ID}}
    password: ${{secrets.ECR_AWS_SECRET_ACCESS_KEY}}

```
```
registries:
  ecr-docker:
    type: docker-registry
    url: https://1234567890.dkr.ecr.us-east-1.amazonaws.com
    username: ${{secrets.ECR_AWS_ACCESS_KEY_ID}}
    password: ${{secrets.ECR_AWS_SECRET_ACCESS_KEY}}

```

#### [Notes](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#notes-1)
Dependabot works with any container registries that implement the Open Container Initiative (OCI) Distribution Specification. For more information, see <https://github.com/opencontainers/distribution-spec/blob/main/spec.md>.
Dependabot supports authentication to private registries via a central token service or HTTP Basic Auth. For more information, see [Token Authentication Specification](https://docs.docker.com/registry/spec/auth/token/) in the Docker documentation and [Basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication) on Wikipedia.
#### [Limitations and workarounds](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#limitations-and-workarounds)
  * Image names may not always be detected in Containerfiles, Helm files, or yaml files.
  * Dockerfiles may only receive a version update to the first `FROM` directive.
  * Dockerfiles do not receive updates to images specified with the `ARG` directive. There is a workaround available for the `COPY` directive. For more information, see [Dependabot ignores image references in COPY Dockerfile statement](https://github.com/dependabot/dependabot-core/issues/5103#issuecomment-1692420920) in the `dependabot/dependabot-core` repository.
  * Dependabot doesn't support multi-stage Docker builds. For more information, see [Support for Docker multi-stage builds](https://github.com/dependabot/dependabot-core/issues/7640) in the `dependabot/dependabot-core` repository.


### [Docker Compose](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#docker-compose)
Docker Compose adheres to the same configuration guidelines as Docker. For more information, see [Docker](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#docker).
### [Helm Charts](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#helm-charts)
Helm supports using a username and password for registries. For more information, see [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#helm-registry).
Snippet of `dependabot.yml` file using a username and password.
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

#### [Notes](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#notes-2)
Dependabot works with any OCI-compliant registries that implement the Open Container Initiative (OCI) Distribution Specification. For more information, see [Helm Registry Login](https://helm.sh/docs/helm/helm_registry_login/) in the Helm docs.
Dependabot supports authentication to private registries via a central token service or HTTP Basic Auth. For more information, see [Token Authentication Specification](https://docs.docker.com/registry/spec/auth/token/) in the Docker documentation and [Basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication) on Wikipedia.
When configuring Dependabot for Helm charts, it will also automatically update the Docker images referenced within those charts, ensuring that both the chart versions and their contained images stay up to date.
#### [Limitations and workarounds](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#limitations-and-workarounds-1)
  * Dependabot only updates dependencies in `Chart.yaml` files.
  * Images in `values.yaml` files and `Chart.yaml` files are updated.
  * Helm dependency updates are first attempted via the Helm CLI, with fallback to searching `index.yaml`.
  * Images that have an array of versions in the YAML cannot be updated.
  * Image names may not always be detected in Helm files or YAML files.
  * For Helm v2 updates, use the [Docker ecosystem](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#docker).


### [Gradle](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#gradle)
Dependabot doesn't run Gradle but supports updates to certain Gradle files. For more information, see "Gradle" in [Dependabot supported ecosystems and repositories](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#gradle).
Gradle supports the `maven-repository` registry type. For more information, see `maven-repository` in [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#maven-repository).
The `maven-repository` type supports username and password. If the account is a GitHub account, you can use a GitHub personal access token in place of the password.
YAML```
registries:
  gradle-artifactory:
    type: maven-repository
    url: https://acme.jfrog.io/artifactory/my-gradle-registry
    username: octocat
    password: ${{secrets.MY_ARTIFACTORY_PASSWORD}}
updates:
  - package-ecosystem: "gradle"
    directory: "/"
    registries:
      - gradle-artifactory
    schedule:
      interval: "monthly"

```
```
registries:
  gradle-artifactory:
    type: maven-repository
    url: https://acme.jfrog.io/artifactory/my-gradle-registry
    username: octocat
    password: ${{secrets.MY_ARTIFACTORY_PASSWORD}}
updates:
  - package-ecosystem: "gradle"
    directory: "/"
    registries:
      - gradle-artifactory
    schedule:
      interval: "monthly"

```

#### [Notes](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#notes-3)
You may not see all of your dependencies represented in the dependency graph, especially if some dependencies are build-time dependencies. You can use the dependency submission API to inform GitHub about your other dependencies, and receive security updates for them. For more information, see [Using the dependency submission API](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/using-the-dependency-submission-api).
### [Maven](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#maven)
Maven supports username and password authentication. For more information, see `maven-repository` in [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#maven-repository).
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

If the account is a GitHub account, you can use a GitHub personal access token in place of the password.
YAML```
version: 2
registries:
  maven-github:
    type: maven-repository
    url: https://maven.pkg.github.com/octocat
    username: octocat
    password: ${{secrets.OCTOCAT_GITHUB_PAT}}
updates:
  - package-ecosystem: "maven"
    directory: "/"
    registries:
      - maven-github
    schedule:
      interval: "monthly"

```
```
version: 2
registries:
  maven-github:
    type: maven-repository
    url: https://maven.pkg.github.com/octocat
    username: octocat
    password: ${{secrets.OCTOCAT_GITHUB_PAT}}
updates:
  - package-ecosystem: "maven"
    directory: "/"
    registries:
      - maven-github
    schedule:
      interval: "monthly"

```

#### [Notes](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#notes-4)
You may not see all of your dependencies represented in the dependency graph, especially if some dependencies are build-time dependencies. You can use the dependency submission API to inform GitHub about your other dependencies, and receive security updates for them. For more information, see [Using the dependency submission API](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/using-the-dependency-submission-api).
### [npm](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#npm)
You can define the configuration in the `dependabot.yml` file using the `npm-registry` type, or configure Dependabot to send all registry requests through a specified base URL.
#### [Using the `npm-registry` type in the configuration file](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#using-the-npm-registry-type-in-the-configuration-file)
You can define the private registry configuration in a `dependabot.yml` file using the `npm-registry` type. For more information, see [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#npm-registry).
The snippet of a `dependabot.yml` file below uses a token. For this type of registry using the GitHub Packages registry (`xyz.pkg.github.com`), the token is in fact a GitHub personal access token (PAT) .
YAML```
registries:
  npm-github:
    type: npm-registry
    url: https://npm.pkg.github.com
    token: ${{secrets.MY_GITHUB_PERSONAL_TOKEN}}

```
```
registries:
  npm-github:
    type: npm-registry
    url: https://npm.pkg.github.com
    token: ${{secrets.MY_GITHUB_PERSONAL_TOKEN}}

```

The npm ecosystem requires a `.npmrc` file with the private registry URL to be checked into the repository.
Example of the content of a `.npmrc` file:
```
registry=https://<private-registry-url>

```

Alternatively you can add the private registry URL to an existing `.npmrc` file using the following command.
```
npm config set registry <url>

```

For more information, see [registry](https://docs.npmjs.com/cli/v9/using-npm/config?v=true#registry) in the npm documentation.
You can also scope the configuration to only a single dependency or organization, in which case the token will only be valid for the organization, and different tokens can be used for different organizations for the same repository.
```
npm config set @<org-name>:registry <url>

```

This would result in a '.npmrc' with the registry:
```
@<org-name>:registry=https://<private-registry-url>

```

npm can be configured to use the private registry's URL in lockfiles with `replace-registry-host`. For more information, see [replace-registry-host](https://docs.npmjs.com/cli/v9/using-npm/config?v=true#replace-registry-host) in the npm documentation.
```
npm config set replace-registry-host "never"

```

If you use `replace-registry-host`, you must locally run `npm install` in order to regenerate the lockfile to use the private registry URL. Dependabot will use the same URL when providing updates.
Once the registry is configured, you can also run `npm login` to verify that your configuration is correct and valid. The lockfile can also be regenerated to use the new private registry by running `npm install` again.
You need to ensure that the `.npmrc` file is checked into the same directory as the project's `package.json` and that the file doesn't include any environment variables or secrets. If you use a monorepo, the `.npmrc` file should live in the project's root directory.
#### [Configuring Dependabot to send registry requests through a specified base URL](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#configuring-dependabot-to-send-registry-requests-through-a-specified-base-url)
You can configure Dependabot to send all registry requests through a specified base URL. In order for Dependabot to access a public dependency, the registry must either have a cloned copy of the dependency with the requested version, or allow traffic to fetch from a public registry if the dependency is not available.
If there is no global registry defined in a `.npmrc` file, you can set `replaces-base` to `true` in the `dependabot.yml` file. For more information, see "`replaces-base`" in [Top-level `registries` key](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference#top-level-registries-key).
#### [Notes](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#notes-5)
Dependencies sourced directly from a GitHub repository give Dependabot access to the repository through the GitHub UI. For information about allowing Dependabot to access private GitHub dependencies, see [Allowing Dependabot to access private dependencies](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-security-and-analysis-settings-for-your-organization#allowing-dependabot-to-access-private-dependencies).
For scoped dependencies (`@my-org/my-dep`), Dependabot requires that the private registry is defined in the project's `.npmrc` file. To define private registries for individual scopes, use `@myscope:registry=https://private_registry_url`.
Registries should be configured using the `https` protocol.
### [NuGet](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#nuget)
Supported by Artifactory, Artifacts, Cloudsmith, GitHub Packages registry, Nexus, and ProGet.
The `nuget-feed` type supports username and password, or token. For more information, see `nuget-feed` in [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#nuget-feed).
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

#### [Notes](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#notes-6)
You can also use a token in your `dependabot.yml` file. For this type of registry using the GitHub Packages registry (`xyz.pkg.github.com`), the token is in fact a GitHub personal access token (PAT) .
YAML```
registries:
  nuget-azure-devops:
    type: nuget-feed
    url: https://pkgs.dev.azure.com/.../_packaging/My_Feed/nuget/v3/index.json
    token: ${{secrets.MY_AZURE_DEVOPS_TOKEN}}

```
```
registries:
  nuget-azure-devops:
    type: nuget-feed
    url: https://pkgs.dev.azure.com/.../_packaging/My_Feed/nuget/v3/index.json
    token: ${{secrets.MY_AZURE_DEVOPS_TOKEN}}

```

### [pub](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#pub)
You can define the private registry configuration in a `dependabot.yml` file using the `pub-repository` type. For more information, see [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#pub-repository).
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

#### [Notes](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#notes-7)
Dependencies sourced directly from a GitHub repository give Dependabot access to the repository through the GitHub UI. For information about allowing Dependabot to access private GitHub dependencies, see [Allowing Dependabot to access private dependencies](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-security-and-analysis-settings-for-your-organization#allowing-dependabot-to-access-private-dependencies).
pub supports URL and token authentication. The URL used for the registry should match the pub-hosted URL. For more information, see [Hosted Pub Repository Specification Version 2](https://github.com/dart-lang/pub/blob/master/doc/repository-spec-v2.md#hosted-url) in the `github/dart-lang/pub` repository.
Dependabot doesn't support overrides to the default package registry. For more information about overrides and why some users may implement them, see [Overriding the default package repository](https://dart.dev/tools/pub/custom-package-repositories#default-override) in the Dart documentation.
### [Python](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#python)
Supported by Artifactory, Azure Artifacts, Cloudsmith, Nexus, and ProGet. The GitHub Packages registry is not supported.
The `python-index` type supports username and password, or token. For more information, see `python-index` in [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#python-index).
YAML```
registries:
  python-example:
    type: python-index
    url: https://example.com/_packaging/my-feed/pypi/example
    username: octocat
    password: ${{secrets.MY_BASIC_AUTH_PASSWORD}}

```
```
registries:
  python-example:
    type: python-index
    url: https://example.com/_packaging/my-feed/pypi/example
    username: octocat
    password: ${{secrets.MY_BASIC_AUTH_PASSWORD}}

```

YAML```
registries:
  python-azure:
    type: python-index
    url: https://pkgs.dev.azure.com/octocat/_packaging/my-feed/pypi/example
    username: octocat@example.com
    password: ${{secrets.MY_AZURE_DEVOPS_TOKEN}}

```
```
registries:
  python-azure:
    type: python-index
    url: https://pkgs.dev.azure.com/octocat/_packaging/my-feed/pypi/example
    username: octocat@example.com
    password: ${{secrets.MY_AZURE_DEVOPS_TOKEN}}

```

YAML```
registries:
  python-gemfury:
    type: python-index
    url: https://pypi.fury.io/my_org
    token: ${{secrets.MY_GEMFURY_TOKEN}}

```
```
registries:
  python-gemfury:
    type: python-index
    url: https://pypi.fury.io/my_org
    token: ${{secrets.MY_GEMFURY_TOKEN}}

```

#### [Notes](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#notes-8)
Dependencies sourced directly from a GitHub repository give Dependabot access to the repository through the GitHub UI. For information about allowing Dependabot to access private GitHub dependencies, see [Allowing Dependabot to access private dependencies](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-security-and-analysis-settings-for-your-organization#allowing-dependabot-to-access-private-dependencies).
`url` should contain the URL, organization, and the "feed" or repository.
### [Yarn](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#yarn)
The Yarn registry uses a configuration similar to that of the npm registry. For more information, see "`npm-registry`" in [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#npm-registry).
YAML```
registries:
  yarn-github:
    type: npm-registry
    url: https://npm.pkg.github.com
    token: ${{secrets.MY_GITHUB_PERSONAL_TOKEN}}

```
```
registries:
  yarn-github:
    type: npm-registry
    url: https://npm.pkg.github.com
    token: ${{secrets.MY_GITHUB_PERSONAL_TOKEN}}

```

  * For private registries, you have to check in a `.yarnrc.yml` file (for Yarn 3) or a `.yarnrc` file (for Yarn Classic).
  * The yarn config files should not contain environment variables.
  * You should configure private registries listed in the `dependabot.yml` file using `https`.


#### [Yarn Classic](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#yarn-classic)
You can either specify the private registry configuration in the `dependabot.yml` file, or set up Yarn Classic according to the standard package manager instructions.
##### [Defining the private registry configuration in the `dependabot.yml` file](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#defining-the-private-registry-configuration-in-the-dependabotyml-file)
You can define the private registry configuration in your `dependabot.yml` file. For more information, see [Top-level `registries` key](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference#top-level-registries-key).
To ensure that the private registry is listed as the dependency source in the project's `yarn.lock` file, you need to run `yarn install` on a machine with private registry access. Yarn should update the resolved field to include the private registry URL.
```
encoding@^0.1.11:
  version "0.1.13"
  resolved "https://private_registry_url/encoding/-/encoding-0.1.13.tgz#56574afdd791f54a8e9b2785c0582a2d26210fa9"
  integrity sha512-ETBauow1T35Y/WZMkio9jiM0Z5xjHHmJ4XmjZOq1l/dXz3lr2sRn87nJy20RupqSh1F2m3HHPSp8ShIPQJrJ3A==
  dependencies:
    iconv-lite "^0.6.2"

```

##### [Following the standard instructions from your package manager](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#following-the-standard-instructions-from-your-package-manager)
If the `yarn.lock` file doesn't list the private registry as the dependency source, you can set up Yarn Classic according to the standard package manager instructions.
  1. Define the private registry configuration in the `dependabot.yml` file.
  2. You can then either:
     * Manually set the private registry to the `.yarnrc` file by adding the registry to a `.yarnrc.yml` file in the project root with the key registry, or
     * Perform the same action by running `yarn config set registry <private registry URL>` in your terminal.
Example of a `.yarnrc` with a private registry defined: `registry https://nexus.example.com/repository/yarn-all`


#### [Yarn Berry (v3)](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#yarn-berry-v3)
For information on the configuration, see [Settings (.yarnrc.yml)](https://yarnpkg.com/configuration/yarnrc/) in the Yarn documentation.
As with Yarn Classic, you can either specify the private registry configuration in the `dependabot.yml` file, or set up Yarn Berry according to the package manager instructions.
##### [Defining the private registry configuration in the `dependabot.yml` file](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#defining-the-private-registry-configuration-in-the-dependabotyml-file-1)
You can define the private registry configuration in your `dependabot.yml` file. For more information, see [Top-level `registries` key](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference#top-level-registries-key).
To ensure the private registry is listed as the dependency source in the project's `yarn.lock` file, run `yarn install` on a machine with private registry access. Yarn should update the resolved field to include the private registry URL.
```
encoding@^0.1.11:
  version "0.1.13"
  resolved "https://private_registry_url/encoding/-/encoding-0.1.13.tgz#56574afdd791f54a8e9b2785c0582a2d26210fa9"
  integrity sha512-ETBauow1T35Y/WZMkio9jiM0Z5xjHHmJ4XmjZOq1l/dXz3lr2sRn87nJy20RupqSh1F2m3HHPSp8ShIPQJrJ3A==
  dependencies:
    iconv-lite "^0.6.2"

```

You can also configure private registries with `npmAuthIdent` or `npmAuthToken`. For more information, see "npmAuthIdent" and "npmAuthToken" in the [Yarn documentation](https://yarnpkg.com/configuration/yarnrc/#npmAuthIdent).
```
yarn config set registry <url>

```

You can scope the configuration to only cover a single dependency or organization.
```
yarn config set @<SCOPE>:registry <url>

```

Finally, we recommend you run `yarn login` to verify that your configuration is correct and valid. The lockfile can also be regenerated to use the new private registry by running `yarn install` again.
##### [Following the standard instructions from your package manager](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#following-the-standard-instructions-from-your-package-manager-1)
If the `yarn.lock` file doesn't list the private registry as the dependency source, you can set up Yarn Berry according to the standard package manager instructions.
  1. Define the private registry configuration in the `dependabot.yml` file.
  2. You can then either:
     * Manually set the private registry to the `.yarnrc` file by adding the registry to a `.yarnrc.yml` file in the project root with the key `npmRegistryServer`, or
     * Perform the same action by running `yarn config set npmRegistryServer <private registry URL>` in your terminal.
Example of a `.yarnrc.yml` file with a private registry configured: `npmRegistryServer: "https://nexus.example.com/repository/yarn-all"`
For more information, see [npmRegistryServer](https://yarnpkg.com/configuration/yarnrc#npmRegistryServer) in the Yarn documentation.


#### [Notes](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#notes-9)
Dependencies sourced directly from a GitHub repository give Dependabot access to the repository through the GitHub UI. For information about allowing Dependabot to access private GitHub dependencies, see [Allowing Dependabot to access private dependencies](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-security-and-analysis-settings-for-your-organization#allowing-dependabot-to-access-private-dependencies).
For scoped dependencies (`@my-org/my-dep`), Dependabot requires that the private registry is defined in the project's `.yarnrc file`. To define private registries for individual scopes, use `@myscope:registry" "https://private_registry_url"`.
## [Configuring private registry hosts](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#configuring-private-registry-hosts)
### [Artifactory](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#artifactory)
For information about the configuration of Artifactory, see [Configuring Artifactory](https://jfrog.com/help/r/jfrog-artifactory-documentation/configuring-artifactory) in the JFrog Artifactory documentation.
#### [Remote repositories](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#remote-repositories)
Remote repositories serve as a cache for build artifacts and dependencies. Instead of having to reach out to a global dependency repository, your build tool can use the artifactory cache, which will speed up build times. For more information, see [Remote Repositories](https://jfrog.com/help/r/jfrog-artifactory-documentation/remote-repositories) in the JFrog Artifactory documentation.
If you use the `replace-base` setting, you should also configure a remote repository for Artifactory if you want Dependabot to access another registry whenever the dependency isn't found in the private registry.
#### [Virtual registry](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#virtual-registry)
You can use a virtual registry to group together all private and public dependencies under a single domain. For more information, see [npm Registry](https://jfrog.com/help/r/jfrog-artifactory-documentation/npm-registry) in the JFrog Artifactory documentation.
### [Azure Artifacts](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#azure-artifacts)
For information about Azure Artifacts and instructions on how to configure Dependabot to work with Azure Artifacts, see [Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/artifacts/?view=azure-devops) in the Azure Artifacts documentation, and [Use Dependabot in GitHub with Azure Artifacts](https://josh-ops.com/posts/github-dependabot-with-azure-artifacts/), respectively.
Example of Azure Artifacts registry:
YAML```
registries:
  nuget-azure-devops:
    type: nuget-feed
    url: https://pkgs.dev.azure.com/my_org/_packaging/public/nuget/v3/index.json
    token: ${{secrets.AZURE_DEVOPS_TOKEN}}

```
```
registries:
  nuget-azure-devops:
    type: nuget-feed
    url: https://pkgs.dev.azure.com/my_org/_packaging/public/nuget/v3/index.json
    token: ${{secrets.AZURE_DEVOPS_TOKEN}}

```

The Azure Artifacts password must be an unencoded token and should include a `:` after the token. In addition, the password cannot be base64-encoded.
You can check whether the private registry is successfully accessed by looking at the Dependabot logs.
### [Cloudsmith](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#cloudsmith)
For information about Cloudsmith and instructions on how to configure Dependabot to work with Cloudsmith, see [Getting Started with Cloudsmith](https://help.cloudsmith.io/docs/welcome-to-cloudsmith-docs) and [Integrate GitHub Dependabot with Cloudsmith](https://help.cloudsmith.io/docs/dependabot) in the Cloudsmith documentation.
### [GitHub Packages registry](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#github-packages-registry)
For information about GitHub Packages registries, see [Working with a GitHub Packages registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry). From that article, you can access pages describing how to configure the following registries.
  * Bundler (rubygems)
  * Docker (containers)
  * GitHub Actions
  * Gradle
  * Maven
  * Npm
  * NuGet
  * Yarn


YAML```
registries:
  github:
    type: npm-registry
    url: https://npm.pkg.github.com
    token: ${{ secrets.<token> }}

```
```
registries:
  github:
    type: npm-registry
    url: https://npm.pkg.github.com
    token: ${{ secrets.<token> }}

```

#### [Notes](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#notes-10)
There is no Python container registry.
For private registries that are scoped to a particular organization, Dependabot expects the URL to include the organization name in the `dependabot.yml` file.
### [Nexus](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#nexus)
For information about the configuration of Nexus, see [Repository Manager 3](https://help.sonatype.com/repomanager3) in the Sonatype documentation.
#### [Notes](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#notes-11)
With Nexus Repository Pro, you can enable user tokens. For more information, see [User Tokens](https://help.sonatype.com/repomanager3/nexus-repository-administration/user-authentication/user-tokens) in the Sonatype documentation.
Example of Nexus registry:
YAML```
registries:
  npm-nexus:
    type: npm-registry
    url: https://registry.example.com/repository/npm-internal/
    token: ${{secrets.NEXUS_NPM_TOKEN}}

```
```
registries:
  npm-nexus:
    type: npm-registry
    url: https://registry.example.com/repository/npm-internal/
    token: ${{secrets.NEXUS_NPM_TOKEN}}

```

If you are running Nexus behind a reverse proxy, you need to ensure that the server is accessible using an Auth token by using `curl -v -H 'Authorization: Bearer <token>' 'https://<nexus-repo-url>/repository/<repo-name>/@<scope>%2<package>'`. For more information, see [Run Behind a Reverse Proxy](https://help.sonatype.com/repomanager3/planning-your-implementation/run-behind-a-reverse-proxy) in the Sonatype documentation.
If you are restricting which IPs can reach your Nexus host, you need to add the Dependabot IPs to the allowlist.
  * You can find the IP addresses Dependabot uses to access the registry in the meta API endpoint, under the dependabot key. For more information, see [REST API endpoints for meta data](https://docs.github.com/en/rest/meta).
  * These are the current IPs: 
    * "18.213.123.130/32"
    * "3.217.79.163/32"
    * "3.217.93.44/32" For more information, see [Securing Nexus Repository Manager](https://help.sonatype.com/repomanager3/planning-your-implementation/securing-nexus-repository-manager) in the Sonatype documentation.


Registries can be proxied to reach out to a public registry in case a dependency is not available in the private registry. However, you may want Dependabot to only access the private registry and not access the public registry at all. For more information, see [Quick Start Guide - Proxying Maven and NPM](https://help.sonatype.com/repomanager3/planning-your-implementation/quick-start-guide---proxying-maven-and-npm) in the Sonatype documentation, and [Removing Dependabot access to public registries](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/removing-dependabot-access-to-public-registries).
### [ProGet](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#proget)
For information about ProGet and instructions on how to configure Dependabot to work with feeds in ProGet, see the [ProGet documentation](https://docs.inedo.com/docs/proget-overview).
Example of ProGet registry configuration for a NuGet feed:
YAML```
registries:
  proget-nuget-feed:
    type: nuget-feed
    url: https://proget.corp.local/nuget/MyNuGetFeed/v3/index.json
    token: ${{secrets.PROGET_APK_KEY}}

```
```
registries:
  proget-nuget-feed:
    type: nuget-feed
    url: https://proget.corp.local/nuget/MyNuGetFeed/v3/index.json
    token: ${{secrets.PROGET_APK_KEY}}

```

Example of ProGet registry configuration for Bundler (rubygems):
YAML```
registries:
  proget-gems-feed:
    type: rubygems-server
    url: https://proget.corp.local/rubygems/MyRubygemsFeed
    token: ${{secrets.PROGET_APK_KEY}}

```
```
registries:
  proget-gems-feed:
    type: rubygems-server
    url: https://proget.corp.local/rubygems/MyRubygemsFeed
    token: ${{secrets.PROGET_APK_KEY}}

```

Example of ProGet registry configuration for Python (PyPI):
YAML```
registries:
  proget-python-feed:
    type: python-index
    url: https://proget.corp.local/pypi/MyPythonFeed
    token: ${{secrets.PROGET_APK_KEY}}

```
```
registries:
  proget-python-feed:
    type: python-index
    url: https://proget.corp.local/pypi/MyPythonFeed
    token: ${{secrets.PROGET_APK_KEY}}

```

#### [Notes](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#notes-12)
The `token` should be an API Key with access to view packages. For more information, see [API Access and API Keys](https://docs.inedo.com/docs/buildmaster-administration-security-api-keys) in the ProGet documentation.
You can check whether the private registry is successfully accessed by looking at the Dependabot logs.
