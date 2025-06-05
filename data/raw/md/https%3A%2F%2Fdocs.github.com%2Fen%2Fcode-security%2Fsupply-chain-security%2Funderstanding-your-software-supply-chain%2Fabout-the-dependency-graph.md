  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Supply chain security](https://docs.github.com/en/code-security/supply-chain-security "Supply chain security")/
  * [Understand your supply chain](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain "Understand your supply chain")/
  * [Dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph "Dependency graph")


# About the dependency graph
You can use the dependency graph to identify all your project's dependencies. The dependency graph supports a range of popular package ecosystems.
## Who can use this feature?
The dependency graph is available for the following repository types:
  * Public repositories (on by default)
  * Private repositories
  * Forks


## In this article
  * [About the dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph#about-the-dependency-graph)
  * [Dependency graph availability](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph#dependency-graph-availability)
  * [Dependencies included](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph#dependencies-included)
  * [Dependents included](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph#dependents-included)
  * [Using the dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph#using-the-dependency-graph)
  * [Further reading](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph#further-reading)


## [About the dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph#about-the-dependency-graph)
The dependency graph is a summary of the manifest and lock files stored in a repository and any dependencies that are submitted for the repository using the dependency submission API. For each repository, it shows:
  * Dependencies, the ecosystems and packages it depends on
  * Dependents, the repositories and packages that depend on it


For each dependency, you can see the version, license information, the manifest file which included it, and whether it has known vulnerabilities. For package ecosystems supporting transitive dependencies, the relationship status will be displayed and you can click "
You can also search for a specific dependency using the search bar. Dependencies are sorted automatically with vulnerable packages at the top.
When you push a commit to GitHub that changes or adds a supported manifest or lock file to the default branch, the dependency graph is automatically updated. In addition, the graph is updated when anyone pushes a change to the repository of one of your dependencies.
For information on the supported ecosystems and manifest files, see [Dependency graph supported package ecosystems](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/dependency-graph-supported-package-ecosystems#supported-package-ecosystems).
Additionally, you can use the dependency submission API to submit dependencies from the package manager or ecosystem of your choice, even if the ecosystem is not supported by dependency graph for manifest or lock file analysis. Dependencies submitted to a project using the dependency submission API will show which detector was used for their submission and when they were submitted. For more information on the dependency submission API, see [Using the dependency submission API](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/using-the-dependency-submission-api).
When you create a pull request containing changes to dependencies that targets the default branch, GitHub uses the dependency graph to add dependency reviews to the pull request. These indicate whether the dependencies contain vulnerabilities and, if so, the version of the dependency in which the vulnerability was fixed. For more information, see [About dependency review](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review).
If you have at least read access to the repository, you can export the dependency graph for the repository as an SPDX-compatible, Software Bill of Materials (SBOM), via the GitHub UI or GitHub REST API. For more information, see [Exporting a software bill of materials for your repository](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exporting-a-software-bill-of-materials-for-your-repository).
## [Dependency graph availability](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph#dependency-graph-availability)
Repository administrators can enable or disable the dependency graph for repositories. For more information, see [Managing security and analysis settings for your repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-security-and-analysis-settings-for-your-repository).
Repository administrators can enable or disable the dependency graph for repositories. See [Configuring the dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-graph).
## [Dependencies included](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph#dependencies-included)
The dependency graph includes all the dependencies of a repository that are detailed in the manifest and lock files, or their equivalent, for supported ecosystems, as well as any dependencies that are submitted using the dependency submission API. This includes:
  * Direct dependencies, that are explicitly defined in a manifest or lock file or have been submitted using the dependency submission API
  * Indirect dependencies of these direct dependencies, also known as transitive dependencies or sub-dependencies


The dependency graph identifies indirect dependencies only if they are defined in a lock file or have been submitted using the dependency submission API. For the most reliable graph, you should use lock files (or their equivalent) because they define exactly which versions of the direct and indirect dependencies you currently use. If you use lock files, you also ensure that all contributors to the repository are using the same versions, which will make it easier for you to test and debug code. If your ecosystem does not have lock files, you can use pre-made actions that resolve transitive dependencies for many ecosystems. For more information, see [Using the dependency submission API](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/using-the-dependency-submission-api#using-pre-made-actions).
For more information on how GitHub helps you understand the dependencies in your environment, see [About supply chain security](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-supply-chain-security).
## [Dependents included](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph#dependents-included)
For public repositories, only public repositories that depend on it or on packages that it publishes are reported. This information is not reported for private repositories.
## [Using the dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph#using-the-dependency-graph)
You can use the dependency graph to:
  * Explore the repositories your code depends on, and those that depend on it. For more information, see [Exploring the dependencies of a repository](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exploring-the-dependencies-of-a-repository).
  * View a summary of the dependencies used in your organization's repositories in a single dashboard. For more information, see [Viewing insights for dependencies in your organization](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/viewing-insights-for-dependencies-in-your-organization#viewing-organization-dependency-insights).
  * View and update vulnerable dependencies for your repository. For more information, see [About Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts).
  * See information about vulnerable dependencies in pull requests. For more information, see [Reviewing dependency changes in a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/reviewing-dependency-changes-in-a-pull-request).


## [Further reading](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph#further-reading)
  * [Dependency graph](https://en.wikipedia.org/wiki/Dependency_graph) on Wikipedia
  * [Exploring the dependencies of a repository](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exploring-the-dependencies-of-a-repository)
  * [Viewing and updating Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/viewing-and-updating-dependabot-alerts)
  * [Troubleshooting the detection of vulnerable dependencies](https://docs.github.com/en/code-security/dependabot/troubleshooting-dependabot/troubleshooting-the-detection-of-vulnerable-dependencies)


