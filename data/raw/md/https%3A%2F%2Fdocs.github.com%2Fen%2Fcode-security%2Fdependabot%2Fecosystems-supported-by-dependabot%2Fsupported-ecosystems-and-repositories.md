  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Dependabot](https://docs.github.com/en/code-security/dependabot "Dependabot")/
  * [Dependabot ecosystems](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot "Dependabot ecosystems")/
  * [Dependabot ecosystem support](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories "Dependabot ecosystem support")


# Dependabot supported ecosystems and repositories
Dependabot supports a variety of ecosystems and repositories
## In this article
  * [About Dependabot](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#about-dependabot)
  * [Supported ecosystems and repositories](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#supported-ecosystems-and-repositories)


## [About Dependabot](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#about-dependabot)
Dependabot helps you stay on top of your dependency ecosystems. With Dependabot, you can keep the dependencies you rely on up-to-date, addressing any potential security issues in your supply chain.
Dependabot consists of three different features that help you manage your dependencies:
  * Dependabot alerts: Inform you about vulnerabilities in the dependencies that you use in your repository.
  * Dependabot security updates: Automatically raise pull requests to update the dependencies you use that have known security vulnerabilities.
  * Dependabot version updates: Automatically raise pull requests to keep your dependencies up-to-date.


For more information about Dependabot, see [Dependabot quickstart guide](https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide).
In this article, you can see what the supported ecosystems and repositories are.
## [Supported ecosystems and repositories](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#supported-ecosystems-and-repositories)
You can configure updates for repositories that contain a dependency manifest or lock file for one of the supported package managers. For some package managers, you can also configure vendoring for dependencies. For more information, see [`vendor`](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference#vendor). Dependabot also supports dependencies in private registries. For more information, see [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot).
  * When running security or version updates, some ecosystems must be able to resolve all dependencies from their source to verify that updates have been successful. If your manifest or lock files contain any private dependencies, Dependabot must be able to access the location at which those dependencies are hosted. Organization owners can grant Dependabot access to private repositories containing dependencies for a project within the same organization. For more information, see [Managing security and analysis settings for your organization](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-security-and-analysis-settings-for-your-organization#allowing-dependabot-to-access-private-dependencies). You can configure access to private registries in a repository's `dependabot.yml` configuration file. For more information, see [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot).
  * Dependabot doesn't support private GitHub dependencies for all package managers. See the details in the table below.


If your repository already uses an integration for dependency management, you will need to disable this before enabling Dependabot. For more information, see [About using integrations](https://docs.github.com/en/get-started/exploring-integrations/about-integrations).
Package manager | YAML value | Supported versions | Version updates | Security updates | Private repositories | Private registries | Vendoring  
---|---|---|---|---|---|---|---  
[Bun](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#bun) | `bun` | >=v1.1.39 |  |  |  |  |   
Bundler | `bundler` | v2 |  |  |  |  |   
[Cargo](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#cargo) | `cargo` | v1 |  |  |  |  |   
Composer | `composer` | v2 |  |  |  |  |   
[Dev containers](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#dev-containers) | `devcontainers` | Not applicable |  |  |  |  |   
[Docker](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#docker) | `docker` | v1 |  |  |  |  | Not applicable  
[Docker Compose](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#docker-compose) | `docker-compose` | v2, v3 |  |  |  |  | Not applicable  
.NET SDK | `dotnet-sdk` | >=.NET Core 3.1 |  |  | Not applicable | Not applicable | Not applicable  
[Helm Charts](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#helm-charts) | `helm` | v3 |  |  |  |  | Not applicable  
Hex | `mix` | v1 |  |  |  |  |   
elm-package | `elm` | v0.19 |  |  |  |  |   
git submodule | `gitsubmodule` | Not applicable |  |  |  |  | Not applicable  
[GitHub Actions](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#github-actions) | `github-actions` | Not applicable |  |  |  |  | Not applicable  
Go modules | `gomod` | v1 |  |  |  |  |   
[Gradle](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#gradle) | `gradle` | Not applicable |  |  |  |  |   
[Maven](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#maven) | `maven` | Not applicable |  |  |  |  |   
npm | `npm` | v7, v8, v9 |  |  |  |  |   
[NuGet](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#nuget-cli) | `nuget` | <=6.12.0 |  |  |  |  |   
[pip](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#pip-and-pip-compile) | `pip` | v21.1.2 |  |  |  |  |   
pipenv | `pip` | <= 2021-05-29 |  |  |  |  |   
[pip-compile](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#pip-and-pip-compile) | `pip` | 6.1.0 |  |  |  |  |   
pnpm | `npm` | v7, v8, v9 |  |  |  |  |   
poetry | `pip` | v1 |  |  |  |  |   
[pub](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#pub) | `pub` | v2 |  |  |  |  |   
[Swift](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#swift) | `swift` | v5 |  |  |  |  |   
[Terraform](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#terraform) | `terraform` | >= 0.13, <= 1.10.x |  |  |  |  | Not applicable  
uv | `uv` | v0 |  |  |  |  | Not applicable  
[yarn](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#yarn) | `npm` | v1, v2, v3 |  |  |  |  |   
For package managers such as `pipenv` and `poetry`, you need to use the `pip` YAML value. For example, if you use `poetry` to manage your Python dependencies and want Dependabot to monitor your dependency manifest file for new versions, use `package-ecosystem: "pip"` in your `dependabot.yml` file.
For further information about ecosystem support for Dependabot security updates, see also [Dependency graph supported package ecosystems](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/dependency-graph-supported-package-ecosystems).
#### [Bun](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#bun)
Dependabot supports the current default text-based `bun.lock` file, but not the legacy binary `bun.lockb` file. The `bun.lock` file is supported in version 1.1.39 and above. For more information, see [Lockfile](https://bun.sh/docs/install/lockfile) in the Bun documentation.
#### [Cargo](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#cargo)
Private registry support includes cargo registries, so you can use Dependabot to keep your Rust dependencies up-to-date. For more information, see [Guidance for the configuration of private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot#cargo).
#### [Dev containers](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#dev-containers)
You can use `devcontainers` as a `package-ecosystem` in your `dependabot.yml` file to update Features in your `devcontainer.json` configuration files. For more information about this support, and for configuration file examples, see [General Availability of Dependabot Integration](https://containers.dev/guide/dependabot) in the Development Containers documentation.
Dev containers are used in several tools and services, including Codespaces. For more information about Features and the supported services, see [Features](https://containers.dev/implementors/features/) and [Supporting tools and services](https://containers.dev/supporting) in the Development Containers documentation, respectively.
This updater ensures Features are pinned to the latest `major` version in the associated `devcontainer.json` file. If a dev container has a lockfile, that file will also be updated. For more information about lockfile specifications, see [Lockfiles](https://github.com/devcontainers/spec/blob/main/docs/specs/devcontainer-lockfile.md) in the `devcontainers/spec` repository.
Features in any valid dev container location will be updated in a single pull request. For more information about the dev container specification, see [Specification](https://containers.dev/implementors/spec/#devcontainerjson) in the Development Containers documentation.
#### [Docker](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#docker)
Dependabot can add metadata from Docker images to pull requests for version updates. The metadata includes release notes, changelogs and the commit history. Repository administrators can use the metadata to quickly evaluate the stability risk of the dependency update.
In order for Dependabot to fetch Docker metadata, maintainers of Docker images must add the `org.opencontainers.image.source` label to their Dockerfile, and include the URL of the source repository. Additionally, maintainers must tag the repository with the same tags as the published Docker images. For an example, see the [`dependabot-fixtures/docker-with-source`](https://github.com/dependabot-fixtures/docker-with-source) repository. For more information on Docker labels, see [Extension image labels](https://docs.docker.com/desktop/extensions-sdk/extensions/labels/) and [BUILDX_GIT_LABELS](https://docs.docker.com/build/building/env-vars/#buildx_git_labels) in the Docker documentation.
Dependabot can update Docker image tags in Kubernetes manifests. Add an entry to the Docker `package-ecosystem` element of your `dependabot.yml` file for each directory containing a Kubernetes manifest which references Docker image tags. Kubernetes manifests can be Kubernetes Deployment YAML files or Helm charts. For information about configuring your `dependabot.yml` file for `docker`, see "`package-ecosystem`" in [Dependabot options reference](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference#package-ecosystem).
Dependabot supports both public and private Docker registries. For a list of the supported registries, see "`docker-registry`" in [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#docker-registry).
Dependabot parses Docker image tags for Semantic Versioning ([SemVer](https://semver.org/)). If Dependabot detects a tag with a pre-release, then it will only suggest an update to the latest version with a matching pre-release, and it will not suggest a newer version that use a different pre-release label. For more information, see the `dependabot-docker` [README.md](https://github.com/dependabot/dependabot-core/blob/main/docker/README.md) file in the `dependabot/dependabot-core` repository.
#### [Docker Compose](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#docker-compose)
Dependabot supports Docker Compose in a similar way to Docker. For more information, see [Docker](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#docker).
#### [GitHub Actions](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#github-actions)
Dependabot supports version updates for GitHub Actions with the following caveats.
  * Dependabot only supports updates to GitHub Actions using the GitHub repository syntax, such as `actions/checkout@v4`. Dependabot will ignore actions or reusable workflows referenced locally (for example, `./.github/actions/foo.yml`).
  * Docker Hub and GitHub Packages Container registry URLs are currently not supported. For example, references to Docker container actions using `docker://` syntax aren't supported.
  * Dependabot supports both public and private repositories for GitHub Actions. For private registry configuration options, see "`git`" in [Dependabot options reference](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuration-options-for-the-dependabot.yml-file#git).


For more information about using Dependabot version updates with GitHub Actions, see [Using GitHub's security features to secure your use of GitHub Actions](https://docs.github.com/en/actions/security-guides/using-githubs-security-features-to-secure-your-use-of-github-actions#keeping-the-actions-in-your-workflows-secure-and-up-to-date).
#### [Gradle](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#gradle)
Dependabot doesn't run Gradle but supports updates to the following files:
  * `build.gradle`, `build.gradle.kts` (for Kotlin projects)
  * `gradle/libs.versions.toml` (for projects using a standard Gradle version catalog)
  * Files included via the `apply` declaration that have `dependencies` in the filename. Note that `apply` does not support `apply to`, recursion, or advanced syntaxes (for example, Kotlin's `apply` with `mapOf`, filenames defined by property).


Dependabot uses information from the `pom.xml` file of dependencies to add links to release information in update pull requests. If the information is omitted from the `pom.xml` file, then it cannot be included in Dependabot pull requests, see [Optimizing Java packages for Dependabot updates](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/optimizing-java-packages-dependabot).
For Dependabot security updates, Gradle support is limited to manual uploads of the dependency graph data using the dependency submission API. For more information about the dependency submission API, see [Using the dependency submission API](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/using-the-dependency-submission-api).
  * When you upload Gradle dependencies to the dependency graph using the dependency submission API, all project dependencies are uploaded, even transitive dependencies that aren't explicitly mentioned in any dependency file. When an alert is detected in a transitive dependency, Dependabot isn't able to find the vulnerable dependency in the repository, and therefore won't create a security update for that alert.
  * Dependabot version updates will, however, create pull requests when the parent dependency is explicitly declared as a direct dependency in the project's manifest file.


#### [Helm Charts](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#helm-charts)
Dependabot supports using a username and password for registries. For more information, see [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#helm-registry).
Dependabot works with any OCI-compliant registries that implement the Open Container Initiative (OCI) Distribution Specification.
When configuring Dependabot for Helm charts, it will also automatically update the Docker images referenced within those charts, ensuring that both the chart versions and their contained images stay up to date.
#### [Maven](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#maven)
Dependabot doesn't run Maven but supports updates to `pom.xml` files.
Dependabot uses information from the `pom.xml` file of dependencies to add links to release information in update pull requests. If the information is omitted from the `pom.xml` file, then it cannot be included in Dependabot pull requests, see [Optimizing Java packages for Dependabot updates](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/optimizing-java-packages-dependabot).
#### [NuGet CLI](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#nuget-cli)
Dependabot doesn't run the NuGet CLI but does support most features up until version 6.8.0.
#### [pip and pip-compile](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#pip-and-pip-compile)
Dependabot supports updates to any `.txt` file.
In addition, Dependabot supports updates to `pyproject.toml` files if they follow the PEP 621 standard.
#### [poetry](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#poetry)
The PEP 621 `project` section isn't currently supported for `poetry`.
#### [pub](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#pub)
Dependabot won't perform an update for `pub` when the version that it tries to update to is ignored, even if an earlier version is available.
You can use Dependabot to keep Dart dependencies up-to-date if you use private hosted pub repositories. For information about allowing Dependabot to access private GitHub dependencies, see [Allowing Dependabot to access private dependencies](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-security-and-analysis-settings-for-your-organization#allowing-dependabot-to-access-private-dependencies).
#### [Swift](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#swift)
Private registry support applies to git registries only. Swift registries are not supported. Non-declarative manifests are not supported. For more information on non-declarative manifests, see [Editing Non-Declarative Manifests](https://github.com/apple/swift-evolution/blob/7003da1439ad60896ec14657dfce829f04b0632c/proposals/0301-package-editing-commands.md#editing-non-declarative-manifests) in the Swift Evolution documentation.
#### [Terraform](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#terraform)
Terraform support includes:
  * Modules hosted on Terraform Registry or a publicly reachable Git repository.
  * Terraform providers.
  * Private Terraform Registry. You can configure access for private git repositories by specifying a git registry in your `dependabot.yml` file. For more information, see [`git`](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#git).


#### [yarn](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#yarn)
Dependabot supports vendored dependencies for v2 onwards.
