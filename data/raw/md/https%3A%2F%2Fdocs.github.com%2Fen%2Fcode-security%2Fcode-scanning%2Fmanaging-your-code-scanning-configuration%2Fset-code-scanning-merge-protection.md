  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Manage code scanning](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration "Manage code scanning")/
  * [Set merge protection](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/set-code-scanning-merge-protection "Set merge protection")


# Set code scanning merge protection
You can use rulesets to set code scanning merge protection for pull requests.
## Who can use this feature?
Organization owners, security managers, and organization members with the **admin** role
Code scanning is available for the following repository types:
  * Public repositories on GitHub.com
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [About using rulesets for code scanning merge protection](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/set-code-scanning-merge-protection#about-using-rulesets-for-code-scanning-merge-protection)
  * [Creating a merge protection ruleset for a repository](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/set-code-scanning-merge-protection#creating-a-merge-protection-ruleset-for-a-repository)
  * [Creating a merge protection ruleset with the REST API](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/set-code-scanning-merge-protection#creating-a-merge-protection-ruleset-with-the-rest-api)


## [About using rulesets for code scanning merge protection](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/set-code-scanning-merge-protection#about-using-rulesets-for-code-scanning-merge-protection)
  * Merge protection with rulesets is not related to status checks. For more information about status checks, see [About status checks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks).
  * Merge protection with rulesets will not apply to merge queue groups or Dependabot pull requests analyzed by default setup.


You can use rulesets to prevent pull requests from being merged when one of the following conditions is met:
  * A required tool found a code scanning alert of a severity that is defined in a ruleset.
  * A required code scanning tool's analysis is still in progress.
  * A required code scanning tool is not configured for the repository.


Typically you should use rulesets target long-lived feature branches, where you would like to guarantee that code has been analyzed before pull requests can be merged.
Configuring a code scanning rule will not automatically enable code scanning. For more information about how to enable code scanning, see [Configuring default setup for code scanning](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning).
For more information about code scanning alerts, see [About code scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts).
You can set merge protection with rulesets at the repository level, and for repositories configured with either default setup or advanced setup. You can also use the REST API to set merge protection with rulesets.
For more information about rulesets, see [About rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets).
## [Creating a merge protection ruleset for a repository](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/set-code-scanning-merge-protection#creating-a-merge-protection-ruleset-for-a-repository)
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the left sidebar, under "Code and automation," click **Rules** , then click **Rulesets**.
![Screenshot of the sidebar of the "Settings" page for a repository. The "Rules" sub-menu is expanded, and the "Rulesets" option is outlined in orange.](https://docs.github.com/assets/cb-80504/images/help/repository/rulesets-settings.png)
  4. Click **New ruleset**.
  5. To create a ruleset targeting branches, click **New branch ruleset**.
  6. Under "Ruleset name," type a name for the ruleset.
  7. Optionally, to change the default enforcement status, click [About rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets#using-ruleset-enforcement-statuses).
  8. Under "Branch protections", select **Require code scanning results**.
  9. Under "Required tools and alert thresholds", click 
  10. Next to the name of a code scanning tool:
     * Click **Alerts** and select one of: **None** , **Errors** , **Errors and Warnings** or **All**.
     * Click **Security alerts** and select one of: **None** , **Critical** , **High or higher** , **Medium or higher** , or **All**.
![Screenshot of the "Required tools and alert thresholds" section of "Rulesets" settings.](https://docs.github.com/assets/cb-42772/images/help/repository/rulesets-require-code-scanning.png)


For more information about alert severity and security severity levels, see [About code scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts#about-alert-severity-and-security-severity-levels).
For more information about managing rulesets in a repository, see [Managing rulesets for a repository](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets).
## [Creating a merge protection ruleset with the REST API](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/set-code-scanning-merge-protection#creating-a-merge-protection-ruleset-with-the-rest-api)
You can use the REST API to create a ruleset with the `code_scanning` rule, which allows you to define specific tools and set alert thresholds. For more information, see [REST API endpoints for rules](https://docs.github.com/en/rest/repos/rules?apiVersion=2022-11-28#create-a-repository-ruleset).
