  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Supply chain security](https://docs.github.com/en/code-security/supply-chain-security "Supply chain security")/
  * [Understand your supply chain](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain "Understand your supply chain")/
  * [Configure dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-graph "Configure dependency graph")


# Configuring the dependency graph
You can allow users to identify their projects' dependencies by enabling the dependency graph.
## Who can use this feature?
Repository owners, organization owners, security managers, and users with the **admin** role
## In this article
  * [About the dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-graph#about-the-dependency-graph)
  * [Configuring the dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-graph#configuring-the-dependency-graph)
  * [Further reading](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-graph#further-reading)


## [About the dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-graph#about-the-dependency-graph)
The dependency graph is a summary of the manifest and lock files stored in a repository and any dependencies that are submitted for the repository using the dependency submission API. For each repository, it shows:
  * Dependencies, the ecosystems and packages it depends on
  * Dependents, the repositories and packages that depend on it


For each dependency, you can see the version, license information, the manifest file which included it, and whether it has known vulnerabilities. For package ecosystems supporting transitive dependencies, the relationship status will be displayed and you can click "
You can also search for a specific dependency using the search bar. Dependencies are sorted automatically with vulnerable packages at the top.
For more information, see [About the dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph).
## [Configuring the dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-graph#configuring-the-dependency-graph)
To generate a dependency graph, GitHub needs read-only access to the dependency manifest and lock files for a repository. The dependency graph can be enabled or disabled for all repositories. For more information on viewing the dependency graph, see [Exploring the dependencies of a repository](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exploring-the-dependencies-of-a-repository).
Additionally, you can use the dependency submission API to submit dependencies from the package manager or ecosystem of your choice, even if the ecosystem is not supported by dependency graph for manifest or lock file analysis. Dependencies submitted to a project using the dependency submission API will show which detector was used for their submission and when they were submitted. For more information on the dependency submission API, see [Using the dependency submission API](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/using-the-dependency-submission-api).
### [Enabling and disabling the dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-graph#enabling-and-disabling-the-dependency-graph)
Repository administrators can enable or disable the dependency graph for all repositories owned by your user account, regardless of their visibility. See [Managing security and analysis settings for your personal account](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-user-account-settings/managing-security-and-analysis-settings-for-your-personal-account).
You can also enable the dependency graph for multiple repositories in an organization at the same time. For more information, see [Securing your organization](https://docs.github.com/en/code-security/securing-your-organization).
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Security" section of the sidebar, click 
  4. Read the message about granting GitHub read-only access to the repository data to enable the dependency graph, then next to "Dependency Graph", click **Enable**.
You can disable the dependency graph at any time by clicking **Disable** next to "Dependency Graph" on the settings page for "Advanced Security".


When the dependency graph is first enabled, any manifest and lock files for supported ecosystems are parsed immediately. The graph is usually populated within minutes but this may take longer for repositories with many dependencies. Once enabled, the graph is automatically updated with every push to the repository and every push to other repositories in the graph.
## [Further reading](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-graph#further-reading)
  * [Configuring automatic dependency submission for your repository](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-automatic-dependency-submission-for-your-repository)
  * [Viewing insights for dependencies in your organization](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/viewing-insights-for-dependencies-in-your-organization)
  * [Viewing and updating Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/viewing-and-updating-dependabot-alerts)
  * [Troubleshooting the detection of vulnerable dependencies](https://docs.github.com/en/code-security/dependabot/troubleshooting-dependabot/troubleshooting-the-detection-of-vulnerable-dependencies)


