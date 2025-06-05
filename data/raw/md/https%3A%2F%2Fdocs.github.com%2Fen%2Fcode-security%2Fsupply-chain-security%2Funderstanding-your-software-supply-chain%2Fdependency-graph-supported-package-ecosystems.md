  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Supply chain security](https://docs.github.com/en/code-security/supply-chain-security "Supply chain security")/
  * [Understand your supply chain](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain "Understand your supply chain")/
  * [Dependency graph ecosystem support](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/dependency-graph-supported-package-ecosystems "Dependency graph ecosystem support")


# Dependency graph supported package ecosystems
Dependency graph supports a variety of ecosystems.
## In this article
  * [About the dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/dependency-graph-supported-package-ecosystems#about-the-dependency-graph)
  * [Building the dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/dependency-graph-supported-package-ecosystems#building-the-dependency-graph)
  * [Package ecosystems supported via dependency submission actions](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/dependency-graph-supported-package-ecosystems#package-ecosystems-supported-via-dependency-submission-actions)
  * [Supported package ecosystems](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/dependency-graph-supported-package-ecosystems#supported-package-ecosystems)
  * [Deduplication of manifests](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/dependency-graph-supported-package-ecosystems#deduplication-of-manifests)


## [About the dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/dependency-graph-supported-package-ecosystems#about-the-dependency-graph)
For an introduction to the dependency graph, see [About the dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph).
## [Building the dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/dependency-graph-supported-package-ecosystems#building-the-dependency-graph)
If dependency graph is enabled, it will scan your repository for manifest files used by programming language package ecosystems. When it finds one of the supported manifest files, it will parse the file and build a representation of its contents, including each package's name and version. This is called "static analysis".
Some files explicitly define which versions are used for all direct and all indirect dependencies. They lock the package versions to those included in the build and enable Dependabot to find vulnerable versions in both direct and indirect dependencies. If you use these formats, your dependency graph is more accurate, so they're listed under the "Recommended files" column in the "Supported package ecosystems" table. See [Supported package ecosystems](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/dependency-graph-supported-package-ecosystems#supported-package-ecosystems). Indirect dependencies that are inferred from a manifest file (or equivalent) are excluded from Dependabot's checks for insecure dependencies.
For ecosystems that resolve transitive dependencies at build-time, static analysis does not provide a comprehensive view of the dependency tree. For these ecosystems, there are two approaches that use GitHub Actions: automatic and manual dependency submission. In both cases, an external action will generate a full dependency tree and upload it to the dependency submission API. You can enable automatic submission for supported ecosystems in your repository's settings page. For more information, see [Configuring automatic dependency submission for your repository](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-automatic-dependency-submission-for-your-repository).
## [Package ecosystems supported via dependency submission actions](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/dependency-graph-supported-package-ecosystems#package-ecosystems-supported-via-dependency-submission-actions)
In addition to dependency graph's static analysis and auto-submission, you can use the dependency submission API to add build-time dependencies to the dependency graph, or to add dependencies from package managers and ecosystems of your choice to the dependency graph, even if the ecosystem is not in the "Supported package ecosystems" table. Dependency information from these submitted dependencies will, in turn, flow into Dependabot updates and Dependabot alerts.
Dependencies submitted to a project using the dependency submission API will show which detector was used for their submission and when they were submitted. For more information on the dependency submission API, see [Using the dependency submission API](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/using-the-dependency-submission-api).
## [Supported package ecosystems](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/dependency-graph-supported-package-ecosystems#supported-package-ecosystems)
Package manager | Languages | Static transitive dependencies | Automatic dependency submission | Recommended files | Additional files  
---|---|---|---|---|---  
Cargo | Rust |  |  | `Cargo.lock` | `Cargo.toml`  
Composer | PHP |  |  | `composer.lock` | `composer.json`  
NuGet | .NET languages (C#, F#, VB), C++ |  |  |  `.csproj`, `.vbproj`, `.nuspec`, `.vcxproj`, `.fsproj` | `packages.config`  
GitHub Actions workflows | YAML |  |  |  `.yml`, `.yaml` |   
Go modules | Go |  |  | `go.mod` |   
Gradle | Java |  |  |  |   
Maven | Java, Scala |  |  | `pom.xml` |   
npm | JavaScript |  |  | `package-lock.json` | `package.json`  
pip | Python |  |  |  `requirements.txt`, `pipfile.lock` |  `pipfile`, `setup.py`  
pnpm | JavaScript |  |  | `pnpm-lock.yaml` | `package.json`  
pub | Dart |  |  | `pubspec.lock` | `pubspec.yaml`  
Poetry | Python |  |  | `poetry.lock` | `pyproject.toml`  
RubyGems | Ruby |  |  | `Gemfile.lock` |  `Gemfile`, `*.gemspec`  
Swift Package Manager | Swift |  |  | `Package.resolved` |   
Yarn | JavaScript |  |  | `yarn.lock` | `package.json`  
  * The **Static transitive dependencies** column indicates whether static analysis will add `direct` and `transitive` labels for dependent packages in that ecosystem. Dependency submission actions (automatic or manually configured) can add transitive information for ecosystems where static analysis cannot.
  * If you list your Python dependencies within a `setup.py` file, we may not be able to parse and list every dependency in your project.
  * GitHub Actions workflows must be located in the `.github/workflows/` directory of a repository to be recognized as manifests. Any actions or workflows referenced using the syntax `jobs[*].steps[*].uses` or `jobs.<job_id>.uses` will be parsed as dependencies. For more information, see [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions).
  * Dependabot will only create Dependabot alerts for vulnerable GitHub Actions that use semantic versioning. You will not receive alerts for a vulnerable action that uses SHA versioning. If you use GitHub Actions with SHA versioning, we recommend enabling Dependabot version updates for your repository or organization to keep the actions you use updated to the latest versions. For more information, see [About Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts) and [About Dependabot version updates](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/about-dependabot-version-updates).


## [Deduplication of manifests](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/dependency-graph-supported-package-ecosystems#deduplication-of-manifests)
Dependency graph can learn about dependencies in three different ways: static analysis, automatic submission, and manual submission. A repository can have multiple methods configured, which can cause the same package manifest to be scanned multiple times, potentially with different outputs from each scan. Dependency graph uses deduplication logic to parse the outputs, prioritizing the most accurate information for each manifest file.
Dependency graph displays only one instance of each manifest file using the following precedence rules.
  1. **User submissions** take the highest priority, because they are usually created during artifact builds they have the most complete information. 
     * If there are multiple manual snapshots from different detectors, they are sorted alphabetically by correlator and the first one used.
     * If there are two correlators with the same detector, the resolved dependencies are merged. For more information about correlators and detectors, see [REST API endpoints for dependency submission](https://docs.github.com/en/rest/dependency-graph/dependency-submission).
  2. **Automatic submissions** have the second-highest priority since they are also created during artifact builds, but are not submitted by users.
  3. **Static analysis results** are used when no other data is available.


