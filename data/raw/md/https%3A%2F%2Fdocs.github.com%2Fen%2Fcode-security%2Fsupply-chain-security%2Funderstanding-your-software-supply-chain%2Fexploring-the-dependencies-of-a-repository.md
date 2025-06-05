  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Supply chain security](https://docs.github.com/en/code-security/supply-chain-security "Supply chain security")/
  * [Understand your supply chain](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain "Understand your supply chain")/
  * [Explore dependencies](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exploring-the-dependencies-of-a-repository "Explore dependencies")


# Exploring the dependencies of a repository
You can use the dependency graph to see the packages your project depends on and the repositories that depend on it. In addition, you can see any vulnerabilities detected in its dependencies.
## Who can use this feature?
Repository administrators, organization owners, and people with **write** or **maintain** access to a repository
## In this article
  * [Viewing the dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exploring-the-dependencies-of-a-repository#viewing-the-dependency-graph)
  * [Enabling and disabling the dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exploring-the-dependencies-of-a-repository#enabling-and-disabling-the-dependency-graph)
  * [Changing the "Used by" package](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exploring-the-dependencies-of-a-repository#changing-the-used-by-package)
  * [Further reading](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exploring-the-dependencies-of-a-repository#further-reading)


## [Viewing the dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exploring-the-dependencies-of-a-repository#viewing-the-dependency-graph)
The dependency graph shows the dependencies and dependents of your repository. For each dependency, you can see the version, license information, the manifest file which included it, and whether it has known vulnerabilities. For package ecosystems supporting transitive dependencies, the relationship status will be displayed and you can click "
You can also search for a specific dependency using the search bar. Dependencies are sorted automatically with vulnerable packages at the top. For information about the detection of dependencies and which ecosystems are supported, see [Dependency graph supported package ecosystems](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/dependency-graph-supported-package-ecosystems).
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the main page of a repository. In the horizontal navigation bar, a tab, labeled with a graph icon and "Insights," is outlined in orange.](https://docs.github.com/assets/cb-52175/images/help/repository/repo-nav-insights-tab.png)
  3. In the left sidebar, click **Dependency graph**. 
![Screenshot of the "Dependency graph" tab. The tab is highlighted with an orange outline.](https://docs.github.com/assets/cb-3959/images/help/graphs/graphs-sidebar-dependency-graph.png)
  4. Optionally, use the search bar to find a specific dependency or set of dependencies. You can use the keywords `ecosystem:` to show only packages of a certain type, or `relationship:` to show only direct or transitive dependencies (if the ecosystem supports transitivity). Plain words in search bar will only match package names.
  5. Optionally, to view the repositories and packages that depend on your repository, under "Dependency graph", click **Dependents**.
![Screenshot of the "Dependency graph" page. The "Dependents" tab is highlighted with an orange outline.](https://docs.github.com/assets/cb-6905/images/help/graphs/dependency-graph-dependents-tab.png)
GitHub currently only determines dependents for public repositories.


### [Dependencies view](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exploring-the-dependencies-of-a-repository#dependencies-view)
For each dependency, you can see its ecosystem, the manifest file in which it was found, and its license (where detected).
  * Dependencies for private repositories, private packages, or unrecognized files are shown in plain text.
  * If the package manager for the dependency is in a public repository, you can hover on the dependency name to display a pop-up with the associated repository information.
  * You can sort and filter dependencies by typing filters as `key:value` pairs into the search bar.
    * Use `ecosystem: <ecosystem-name>` to display dependencies for the selected ecosystem.
    * Use `relationship:` to filter the list by relationship status. Possible values are `direct`, `transitive`, and `inconclusive`. Alternatively, you can click the relationship label adjacent to a dependency name to only show dependencies of the same relationship status. This filter is only available for ecosystems with transitive dependency support. See [Dependency graph supported package ecosystems](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/dependency-graph-supported-package-ecosystems) for more information.


Dependencies submitted to a project using the dependency submission API will show which detector was used for their submission and when they were submitted. For more information on using the dependency submission API, see [Using the dependency submission API](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/using-the-dependency-submission-api).
If vulnerabilities have been detected in the repository, these are shown at the top of the view for users with access to Dependabot alerts.
### [Dependents view](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exploring-the-dependencies-of-a-repository#dependents-view)
For public repositories, the dependents view shows how the repository is used by other repositories. To show only the repositories that contain a library in a package manager, click **NUMBER Packages** immediately above the list of dependent repositories. The dependent counts are approximate and may not always match the dependents listed.
## [Enabling and disabling the dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exploring-the-dependencies-of-a-repository#enabling-and-disabling-the-dependency-graph)
Repository administrators can enable or disable the dependency graph for all repositories owned by your user account, regardless of their visibility. See [Managing security and analysis settings for your personal account](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-user-account-settings/managing-security-and-analysis-settings-for-your-personal-account).
You can also enable the dependency graph for multiple repositories in an organization at the same time. For more information, see [Securing your organization](https://docs.github.com/en/code-security/securing-your-organization).
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Security" section of the sidebar, click 
  4. Read the message about granting GitHub read-only access to the repository data to enable the dependency graph, then next to "Dependency Graph", click **Enable**.
You can disable the dependency graph at any time by clicking **Disable** next to "Dependency Graph" on the settings page for "Advanced Security".


## [Changing the "Used by" package](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exploring-the-dependencies-of-a-repository#changing-the-used-by-package)
You may notice some repositories have a "Used by" section in the sidebar of the **Code** tab. Your repository will have a "Used by" section if:
  * The dependency graph is enabled for the repository (see the above section for more details).
  * Your repository contains a package that is published on a [supported package ecosystem](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/dependency-graph-supported-package-ecosystems#supported-package-ecosystems).
  * Within the ecosystem, your package has a link to a _public_ repository where the source is stored.
  * More than 100 repositories depend on your package.


The "Used by" section shows the number of public references to the package that were found, and displays the avatars of some of the owners of the dependent projects.
![Screenshot of the "Used by" section for a repository showing the summary of "13.4m" with details of 8 avatars and "+13,435,819."](https://docs.github.com/assets/cb-40707/images/help/repository/used-by-section.png)
Clicking any item in this section takes you to the **Dependents** tab of the dependency graph.
The "Used by" section represents a single package from the repository. If you have admin permissions to a repository that contains multiple packages, you can choose which package the "Used by" section represents.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Security" section of the sidebar, click 
  4. Under "Advanced Security", click the drop-down menu in the "Used by counter" section and choose a package.


## [Further reading](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exploring-the-dependencies-of-a-repository#further-reading)
  * [Troubleshooting the dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/troubleshooting-the-dependency-graph)
  * [About the dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph)
  * [Viewing and updating Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/viewing-and-updating-dependabot-alerts)
  * [Archiving your GitHub personal account and public repositories](https://docs.github.com/en/get-started/privacy-on-github)


