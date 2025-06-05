  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Security overview](https://docs.github.com/en/code-security/security-overview "Security overview")/
  * [Filter security overview](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview "Filter security overview")


# Filtering alerts in security overview
Use filters to view specific categories of alerts
## Who can use this feature?
Access requires:
  * Organization views: **write** access to repositories in the organization
  * Enterprise views: organization owners and security managers


Organizations owned by a GitHub Team account with GitHub Secret Protection or GitHub Code Security, or owned by a GitHub Enterprise account
## In this article
  * [About filtering security overview](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview#about-filtering-security-overview)
  * [Filter logic for security overview](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview#filter-logic-for-security-overview)
  * [Filter methods](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview#filter-methods)
  * [Repository name, visibility, and status filters](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview#repository-name-visibility-and-status-filters)
  * [Team and topic filters](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview#team-and-topic-filters)
  * [Custom repository property filters](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview#custom-repository-property-filters)
  * [Security feature enablement filters](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview#security-feature-enablement-filters)
  * [Alert number filters](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview#alert-number-filters)
  * [Alert type and property filters](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview#alert-type-and-property-filters)
  * [Dependabot alert view filters](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview#dependabot-alert-view-filters)
  * [Code scanning alert view filters](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview#code-scanning-alert-view-filters)
  * [Secret scanning alert view filters](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview#secret-scanning-alert-view-filters)


## [About filtering security overview](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview#about-filtering-security-overview)
You can use filters in a security overview to narrow your focus based on a range of factors, like alert risk level, alert type, and feature enablement. Different filters are available depending on the specific view, and whether you are viewing data at the enterprise or organization level.
The information shown by security overview varies according to your access to repositories and organizations, and according to whether Advanced Security features are used by those repositories and organizations. For more information, see [About security overview](https://docs.github.com/en/code-security/security-overview/about-security-overview#permission-to-view-data-in-security-overview).
## [Filter logic for security overview](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview#filter-logic-for-security-overview)
You can apply filters and use logical operators to display results that meet specific criteria on security overview. By default, if you apply several different filters, you are using AND logic, meaning you will only see results that match _every_ filter you apply. For example, if you add the filter `is:public dependabot:enabled`, you will only see results from repositories that are public _and_ have Dependabot enabled.
Currently, there are two logical operators that you can apply to your filters on security overview:
  * The `-` operator applies NOT logic, displaying all results _except_ those that match the specified filter. To use the `-` operator, add it to the beginning of a filter. For example, filtering for `-repo:REPOSITORY-NAME` will display data from all repositories _except_ `REPOSITORY-NAME`.
  * The `,` operator applies OR logic, displaying results that match _any_ of the specified values for a single filter. To use the `,` operator, add it between each listed value for a filter. For example, filtering for `is:public,private` will display data from all repositories that are public _or_ private. Similarly, if you apply the same filter multiple times with different values, you are using OR logic. For example, `is:public is:private` is equivalent to `is:public,private`.


## [Filter methods](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview#filter-methods)
All security views have features to help you define filters. These provide an easy way to set up filters and understand the options available.
  * **Interactive search text box.** When you click in the search box and press the keyboard "Space" key, a pop-up text box shows the filter options available in that view. You can use the mouse or keyboard arrow keys to select the options you want in the text box before pressing the keyboard "Return" key to add the filter. Supported for all views.
  * **Dropdown selectors and toggles.** Shown at the end of the "Search text box" or in the header of the data table. As you choose the data to view, the filters shown in the search text box are updated accordingly. Supported on the alert views.
  * **Advanced filters dialog.** When you click the 


## [Repository name, visibility, and status filters](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview#repository-name-visibility-and-status-filters)
In all views, there are two methods for filtering results by repository name.
  * **Free text or keyword search.** Display data for all repositories with a name that contains the keyword. For example, search for `test` to show data for both the "test-repository" and "octocat-testing" repositories.
  * **`repo`qualifier.** Display data only for the repository that exactly matches the value of the qualifier. For example, search for `repo:octocat-testing` to show data for only the "octocat-testing" repository.


You can also filter by repository visibility (internal, private, or public) and archive status.
Qualifier | Description | Views  
---|---|---  
`visibility` | Display data for all repositories that are `public`, `private`, or `internal`. | "Overview" and metrics  
`is` | Display data for all repositories that are `public`, `private`, or `internal`. | "Risk" and "Coverage"  
`archived` | Display only data for archived (`true`) or active (`false`) repositories. | All except "Alerts" views  
## [Team and topic filters](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview#team-and-topic-filters)
These qualifiers are available in all views.
Qualifier | Description  
---|---  
`team` | Display data for all repositories that the specified team has write access or admin access to. For more information on repository roles, see [Repository roles for an organization](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization).  
`topic` | Display data for all repositories that are classified with a specific topic. For more information on repository topics, see [Classifying your repository with topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics).  
## [Custom repository property filters](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview#custom-repository-property-filters)
Repository properties are in public preview and subject to change.
Custom repository properties are metadata that organization owners can add to repositories in an organization, providing a way to group repositories by the information you are interested in. For example, you can add custom repository properties for compliance frameworks or data sensitivity. For more information on adding custom repository properties, see [Managing custom properties for repositories in your organization](https://docs.github.com/en/organizations/managing-organization-settings/managing-custom-properties-for-repositories-in-your-organization).
If you add custom properties to your organization and set values for repositories, you can filter the "Overview" using those custom properties as qualifiers. These qualifiers are currently only available in the organization-level views.
  * **`props.CUSTOM_PROPERTY_NAME`qualifier.** The qualifier consists of a `props.` prefix, followed by the name of the custom property. For example, `props.data_sensitivity:high` displays results for repositories with the `data_sensitivity` property set to the value `high`. |


In enterprise-level views, you can limit the data to repositories owned by a single organization in your enterprise. Use the `org` qualifier to display data for repositories owned by one organization.
## [Security feature enablement filters](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview#security-feature-enablement-filters)
In the "Risk" and "Coverage" views, you can show data only for repositories where security features are enabled (`enabled`), or not enabled (`not-enabled`).
Qualifier | Description  
---|---  
`code-scanning-alerts` | Display repositories that have configured code scanning.  
`dependabot-alerts` | Display repositories that have enabled Dependabot alerts.  
`secret-scanning-alerts` | Display repositories that have enabled secret scanning alerts.  
`any-feature` | Display repositories where at least one security feature is enabled.  
### [Extra filters for the "Coverage" view](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview#extra-filters-for-the-coverage-view)
Qualifier | Description  
---|---  
`code-scanning-default-setup` | Display data for repositories where code scanning is enabled or not enabled using CodeQL default setup.  
`code-scanning-pull-request-alerts` | Display data for repositories where code scanning is enabled or not enabled to run on pull requests.  
`dependabot-security-updates` | Display data for repositories where Dependabot security updates is enabled or not enabled.  
`secret-scanning-push-protection` | Display data for repositories where push protection for secret scanning is enabled or not enabled.  
## [Alert number filters](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview#alert-number-filters)
In the "Risk" view, you can filter repositories by the number of alerts they have of a specific type.
Qualifier | Description  
---|---  
`code-scanning-alerts` | Display data for repositories that have exactly (`=`), more than (`>`) or fewer than (`<`) a specific number of code scanning alerts. For example: `code-scanning-alerts:>100` for repositories with more than 100 alerts.  
`dependabot-alerts` | Display data for repositories that have a specific number (`=`), more than (`>`) or fewer than (`<`) a specific number of Dependabot alerts. For example: `dependabot-alerts:<=10` for repositories with fewer than or equal to 10 alerts.  
`secret-scanning-alerts` | Display data for repositories that have a specific number (`=`), more than (`>`) or fewer than (`<`) a specific number of secret scanning alerts. For example: `secret-scanning-alerts:=10` for repositories with exactly 10 alerts.  
## [Alert type and property filters](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview#alert-type-and-property-filters)
You can filter the "Overview" view by the type and property of alerts. Use the `tool` qualifier to display only data for alerts generated by a specific tool or type of tool.
  * `tool:codeql` to show data only for code scanning alerts generated using CodeQL.
  * `tool:dependabot` to show data only for Dependabot alerts.
  * `tool:secret-scanning` to show data only for secret scanning alerts.
  * `tool:github` or `tool:third-party` to show data for all types of alerts generated by GitHub tools or by third-party tools.
  * `tool:TOOL-NAME` to show data for all alerts generated by a third-party tool for code scanning.


You can also filter the "Overview" view by properties of alerts.
Qualifier | Description  
---|---  
`codeql.rule` | Display data only for code scanning identified by a specific rule for CodeQL.  
`dependabot.ecosystem` | Display data only for Dependabot alerts for a specific ecosystem, for example: `npm`.  
`dependabot.package` | Display data only for Dependabot alerts for a specific package, for example: `tensorflow`.  
`dependabot.scope` | Display data only for Dependabot alerts with a `runtime` or `development` scope.  
`secret-scanning.bypassed` | Display data only for secret scanning alerts where push protection was bypassed (`true`) or not bypassed (`false`).  
`secret-scanning.provider` | Display data only for secret scanning alerts issued by a specific provider, for example: `secret-scanning.provider:adafruit`.  
`secret-scanning.secret-type` | Display data only for secret scanning alerts for a specific type of secret, for example: `secret-scanning.secret-type:adafruit_io_key`.  
`secret-scanning.validity` | Display data only for secret scanning alerts for a specific validity (`active`, `inactive`, or `unknown`).  
`severity` | Display data only for alerts of a specific severity (`critical`, `high`, `medium`, or `low`).  
`third-party.rule` | Display data only for code scanning identified by a specific rule for a tool developed by a third party. For example, `third-party.rule:CVE-2021-26291-maven-artifact` shows only results for the `CVE-2021-26291-maven-artifact` rule of a third-party code scanning tool.  
## [Dependabot alert view filters](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview#dependabot-alert-view-filters)
You can filter the view to show Dependabot alerts that are ready to fix or where additional information about exposure is available. You can click any result to see full details of the alert.
Qualifier | Description  
---|---  
`ecosystem` | Display Dependabot alerts detected in a specified ecosystem, for example: `ecosystem:Maven`.  
`has` | Display Dependabot alerts for vulnerabilities where either a secure version is already available (`patch`) or where at least one call from the repository to a vulnerable function is detected (`vulnerable-calls`). For more information, see [Viewing and updating Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/viewing-and-updating-dependabot-alerts#about-the-detection-of-calls-to-vulnerable-functions).  
`is` | Display Dependabot alerts that are open (`open`) or closed (`closed`).  
`package` | Display Dependabot alerts detected in the specified package, for example: `package:semver`.  
`resolution` | Display Dependabot alerts closed as "auto-dismissed" (`auto-dismissed`), "a fix has already been started" (`fix-started`), "fixed" (`fixed`), "this alert is inaccurate or incorrect" (`inaccurate`), "no bandwidth to fix this" (`no-bandwidth`), "vulnerable code is not actually used" (`not-used`), or "risk is tolerable to this project" (`tolerable-risk`).  
`scope` | Display Dependabot alerts from the development dependency (`development`) or from the runtime dependency (`runtime`).  
`sort` | Groups Dependabot alerts by the manifest file path the alerts point to (`manifest-path`) or by the name of the package where the alert was detected (`package-name`). Alternatively, displays alerts from most important to least important, as determined by CVSS score, vulnerability impact, relevancy, and actionability (`most-important`), from newest to oldest (`newest`), from oldest to newest (`oldest`), or from most to least severe (`severity`).  
## [Code scanning alert view filters](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview#code-scanning-alert-view-filters)
All code scanning alerts have one of the categories shown below. You can click any result to see full details of the relevant query and the line of code that triggered the alert.
Qualifier | Description  
---|---  
`is` | Display code scanning alerts that are open (`open`) or closed (`closed`).  
`resolution` | Display code scanning alerts closed as "false positive" (`false-postive`), "fixed" (`fixed`), "used in tests" (`used-in-tests`), or "won't fix" (`wont-fix`).  
`rule` | Display code scanning alerts identified by the specified rule.  
`severity` | Display code scanning alerts categorized as `critical`, `high`, `medium`, or `low` security alerts. Alternatively, displays code scanning alerts categorized as `error`, `warning`, `note` problems.  
`sort` | Display alerts from newest to oldest (`created-desc`), oldest to newest (`created-asc`), most recently updated (`updated-desc`), or least recently updated (`updated-asc`).  
`tool` | Display code scanning alerts detected by the specified tool, for example: `tool:CodeQL` for alerts created using the CodeQL application in GitHub.  
## [Secret scanning alert view filters](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview#secret-scanning-alert-view-filters)
Qualifier | Description  
---|---  
`bypassed` | Display secret scanning alerts where push protection was bypassed (`true`) or not bypassed (`false`).  
`results` | Display default (`default`) or generic (`generic`) secret scanning alerts.  
`is` | Display secret scanning alerts that are open (`open`) or closed (`closed`).  
`provider` | Display alerts for all secrets issued by a specified provider, for example: `adafruit`.  
`resolution` | Display secret scanning alerts closed as "false positive" (`false-positive`), "pattern deleted" (`pattern-deleted`), "pattern edited' (`pattern-edited`), "revoked" (`revoked`) "used in tests" (`used-in-tests`), or "won't fix" (`wont-fix`).  
`sort` | Display alerts from newest to oldest (`created-desc`), oldest to newest (`created-asc`), most recently updated (`updated-desc`), or least recently updated (`updated-asc`).  
`secret-type` | Display alerts for the specified secret and provider (`provider-pattern`) or custom pattern (`custom-pattern`).
