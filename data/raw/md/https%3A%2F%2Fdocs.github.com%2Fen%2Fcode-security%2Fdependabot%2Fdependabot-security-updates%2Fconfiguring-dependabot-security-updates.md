  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Dependabot](https://docs.github.com/en/code-security/dependabot "Dependabot")/
  * [Dependabot security updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates "Dependabot security updates")/
  * [Configure security updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates "Configure security updates")


# Configuring Dependabot security updates
You can use Dependabot security updates or manual pull requests to easily update vulnerable dependencies.
## Who can use this feature?
Users with **write** access
## In this article
  * [About configuring Dependabot security updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates#about-configuring-dependabot-security-updates)
  * [Supported repositories](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates#supported-repositories)
  * [Managing Dependabot security updates for your repositories](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates#managing-dependabot-security-updates-for-your-repositories)
  * [Grouping Dependabot security updates into a single pull request](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates#grouping-dependabot-security-updates-into-a-single-pull-request)
  * [Overriding the default behavior with a configuration file](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates#overriding-the-default-behavior-with-a-configuration-file)
  * [Further reading](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates#further-reading)


## [About configuring Dependabot security updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates#about-configuring-dependabot-security-updates)
You can enable Dependabot security updates for any repository that uses Dependabot alerts and the dependency graph. For more information, see [About Dependabot security updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates).
You can enable or disable Dependabot security updates for an individual repository, for a selection of repositories in an organization, or for all repositories owned by your personal account or organization. For more information about enabling security features in an organization, see [Enabling security features in your organization](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization).
When Dependabot security updates are enabled for a repository, Dependabot will automatically try to open pull requests to resolve **every** open Dependabot alert that has an available patch. If you prefer to customize which alerts Dependabot opens pull requests for, you should leave Dependabot security updates **disabled** and create an auto-triage rule. For more information, see [Customizing auto-triage rules to prioritize Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/customizing-auto-triage-rules-to-prioritize-dependabot-alerts).
Dependabot and all related features are covered by [GitHub's Terms of Service](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service).
## [Supported repositories](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates#supported-repositories)
GitHub automatically enables Dependabot security updates for newly created repositories if your personal account or organization has enabled **Automatically enable for new repositories** for Dependabot security updates. For more information, see [Managing Dependabot security updates for your repositories](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates#managing-dependabot-security-updates-for-your-repositories).
If you create a fork of a repository that has security updates enabled, GitHub will automatically disable Dependabot security updates for the fork. You can then decide whether to enable Dependabot security updates on the specific fork.
If security updates are not enabled for your repository and you don't know why, first try enabling them using the instructions given in the procedural sections below. If security updates are still not working, you can contact us through the [GitHub Support portal](https://support.github.com).
## [Managing Dependabot security updates for your repositories](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates#managing-dependabot-security-updates-for-your-repositories)
You can enable or disable Dependabot security updates for all qualifying repositories owned by your personal account or organization. For more information, see [Managing security and analysis settings for your personal account](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-personal-account-settings/managing-security-and-analysis-settings-for-your-personal-account) or [Managing security and analysis settings for your organization](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-security-and-analysis-settings-for-your-organization).
You can also enable or disable Dependabot security updates for an individual repository.
### [Enabling or disabling Dependabot security updates for an individual repository](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates#enabling-or-disabling-dependabot-security-updates-for-an-individual-repository)
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Security" section of the sidebar, click 
  4. To the right of "Dependabot security updates", click **Enable** to enable the feature or **Disable** to disable it. For public repositories, the button is disabled if the feature is always enabled.


## [Grouping Dependabot security updates into a single pull request](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates#grouping-dependabot-security-updates-into-a-single-pull-request)
To reduce the number of pull requests you may be seeing, you can enable grouped security updates for your repository or organization. When this is enabled, Dependabot will group security updates into one pull request for each package ecosystem. In order to use grouped security updates, you must first enable the following features:
  * **Dependency graph**. For more information, see [Configuring the dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-graph).
  * **Dependabot alerts**. For more information, see [Configuring Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/configuring-dependabot-alerts).
  * **Dependabot security updates**. For more information, see [Configuring Dependabot security updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates).


When grouped security updates are first enabled, Dependabot will immediately try to create grouped pull requests. You may notice Dependabot closing old pull requests and opening new ones.
You can enable grouped pull requests for Dependabot security updates in one, or both, of the following ways.
  * To group as many available security updates together as possible, across directories and per ecosystem, enable grouping in the "Advanced Security" settings for your repository, or in "Global settings" under Advanced Security for your organization.
  * For more granular control of grouping, such as grouping by package name, development/production dependencies, SemVer level, or across multiple directories per ecosystem, add configuration options to the `dependabot.yml` configuration file in your repository.


If you have configured group rules for Dependabot security updates in a `dependabot.yml` file, all available updates will be grouped according to the rules you've specified. Dependabot will only group across those directories not configured in your `dependabot.yml` if the setting for grouped security updates at the organization or repository level is also enabled.
### [Enabling or disabling grouped Dependabot security updates for an individual repository](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates#enabling-or-disabling-grouped-dependabot-security-updates-for-an-individual-repository)
Repository administrators can enable or disable grouped security updates for their repository. Changing the repository setting will override any default organization settings. Group rules configured in a `dependabot.yml` file will override the user interface settings for enabling or disabling grouped security updates at the organization or repository level.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Security" section of the sidebar, click 
  4. Under "Dependabot", to the right of "Grouped security updates", click **Enable** to enable the feature or **Disable** to disable it.


### [Enabling or disabling grouped Dependabot security updates for an organization](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates#enabling-or-disabling-grouped-dependabot-security-updates-for-an-organization)
You can enable grouped Dependabot security updates into a single pull request. For more information, see [Configuring global security settings for your organization](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#grouping-dependabot-security-updates).
## [Overriding the default behavior with a configuration file](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates#overriding-the-default-behavior-with-a-configuration-file)
You can override the default behavior of Dependabot security updates by adding a `dependabot.yml` file to your repository. With a `dependabot.yml` file, you can have more granular control of grouping, and override the default behavior of Dependabot security updates settings.
Use the `groups` option with the `applies-to: security-updates` key to create sets of dependencies (per package manager), so that Dependabot opens a single pull request to update multiple dependencies at the same time. You can define groups by package name (the `patterns` and `exclude-patterns` keys), dependency type (`dependency-type` key), and SemVer (the `update-types` key).
Dependabot creates groups in the order they appear in your `dependabot.yml` file. If a dependency update could belong to more than one group, it is only assigned to the first group it matches with.
If you only require _security_ updates and want to exclude _version_ updates, you can set `open-pull-requests-limit` to `0` in order to prevent version updates for a given `package-ecosystem`.
For more information about the configuration options available for security updates, see [Customizing pull requests for Dependabot security updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/customizing-dependabot-security-prs).
YAML```
# Example configuration file that:
#  - Has a private registry
#  - Ignores lodash dependency
#  - Disables version-updates
#  - Defines a group by package name, for security updates for golang dependencies

version: 2
registries:
  example:
    type: npm-registry
    url: https://example.com
    token: ${{secrets.NPM_TOKEN}}
updates:
  - package-ecosystem: "npm"
    directory: "/src/npm-project"
    schedule:
      interval: "daily"
    # For Lodash, ignore all updates
    ignore:
      - dependency-name: "lodash"
    # Disable version updates for npm dependencies
    open-pull-requests-limit: 0
    registries:
      - example
  - package-ecosystem: "gomod"
    groups:
      golang:
        applies-to: security-updates
        patterns:
          - "golang.org*"

```
```
# Example configuration file that:
#  - Has a private registry
#  - Ignores lodash dependency
#  - Disables version-updates
#  - Defines a group by package name, for security updates for golang dependencies

version: 2
registries:
  example:
    type: npm-registry
    url: https://example.com
    token: ${{secrets.NPM_TOKEN}}
updates:
  - package-ecosystem: "npm"
    directory: "/src/npm-project"
    schedule:
      interval: "daily"
    # For Lodash, ignore all updates
    ignore:
      - dependency-name: "lodash"
    # Disable version updates for npm dependencies
    open-pull-requests-limit: 0
    registries:
      - example
  - package-ecosystem: "gomod"
    groups:
      golang:
        applies-to: security-updates
        patterns:
          - "golang.org*"

```

In order for Dependabot to use this configuration for security updates, the `directory` must be the path to the manifest files, and you should not specify a `target-branch`.
## [Further reading](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates#further-reading)
  * [About Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts)
  * [Configuring Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/configuring-dependabot-alerts)
  * [Dependency graph supported package ecosystems](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/dependency-graph-supported-package-ecosystems#supported-package-ecosystems)


