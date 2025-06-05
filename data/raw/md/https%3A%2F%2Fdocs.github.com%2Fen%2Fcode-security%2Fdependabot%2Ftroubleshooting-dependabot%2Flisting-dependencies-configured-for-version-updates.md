  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Dependabot](https://docs.github.com/en/code-security/dependabot "Dependabot")/
  * [Troubleshoot Dependabot](https://docs.github.com/en/code-security/dependabot/troubleshooting-dependabot "Troubleshoot Dependabot")/
  * [List configured dependencies](https://docs.github.com/en/code-security/dependabot/troubleshooting-dependabot/listing-dependencies-configured-for-version-updates "List configured dependencies")


# Listing dependencies configured for version updates
You can view the dependencies that Dependabot monitors for updates.
## Who can use this feature?
Users with **write** access
## [Viewing dependencies monitored by Dependabot](https://docs.github.com/en/code-security/dependabot/troubleshooting-dependabot/listing-dependencies-configured-for-version-updates#viewing-dependencies-monitored-by-dependabot)
After you've enabled version updates, you can confirm that your configuration is correct using the **Dependabot** tab in the dependency graph for the repository. For more information, see [Configuring Dependabot version updates](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuring-dependabot-version-updates).
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the main page of a repository. In the horizontal navigation bar, a tab, labeled with a graph icon and "Insights," is outlined in orange.](https://docs.github.com/assets/cb-52175/images/help/repository/repo-nav-insights-tab.png)
  3. In the left sidebar, click **Dependency graph**. 
![Screenshot of the "Dependency graph" tab. The tab is highlighted with an orange outline.](https://docs.github.com/assets/cb-3959/images/help/graphs/graphs-sidebar-dependency-graph.png)
  4. Under "Dependency graph", click **Dependabot**.
  5. Optionally, to view the files monitored for a package manager, to the right of the package manager, click 
![Screenshot of the Dependabot tab under "Insights". A dropdown menu, labeled with a kebab icon, is highlighted with an orange outline.](https://docs.github.com/assets/cb-24603/images/help/dependabot/monitored-dependency-files.png)


If any dependencies are missing, check the log files for errors. If any package managers are missing, review the configuration file.
For information about Dependabot job logs, see [Viewing Dependabot job logs](https://docs.github.com/en/code-security/dependabot/troubleshooting-dependabot/viewing-dependabot-job-logs).
