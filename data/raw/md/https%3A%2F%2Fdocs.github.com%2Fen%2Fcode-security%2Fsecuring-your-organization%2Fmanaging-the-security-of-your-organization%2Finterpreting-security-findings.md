  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secure your organization](https://docs.github.com/en/code-security/securing-your-organization "Secure your organization")/
  * [Manage organization security](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization "Manage organization security")/
  * [Interpret security data](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/interpreting-security-findings "Interpret security data")


# Interpreting security findings
You can analyze security data on repositories in your organization to determine if you need to make changes to your security setup.
## Who can use this feature?
Organization owners, security managers, and organization members with the **admin** role
## In this article
  * [About security findings](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/interpreting-security-findings#about-security-findings)
  * [Finding repositories with security alerts using security overview](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/interpreting-security-findings#finding-repositories-with-security-alerts-using-security-overview)
  * [Interpreting secret scanning alerts](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/interpreting-security-findings#interpreting-secret-scanning-alerts)
  * [Interpreting code scanning alerts](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/interpreting-security-findings#interpreting-code-scanning-alerts)
  * [Interpreting Dependabot alerts](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/interpreting-security-findings#interpreting-dependabot-alerts)
  * [Next steps](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/interpreting-security-findings#next-steps)


## [About security findings](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/interpreting-security-findings#about-security-findings)
After you apply a security configuration to a repository, the enabled security features will likely raise security findings on that repository. These findings may show up as feature-specific alerts, or as automatically generated pull requests designed to keep your repositories secure. You can analyze the findings across the organization and make any necessary adjustments to your security configuration.
To best secure your organization, you should encourage contributors to review and resolve security alerts and pull requests. In addition, you can collaborate with contributors to fix historical security alerts, see [Best practices for fixing security alerts at scale](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/best-practice-fix-alerts-at-scale).
## [Finding repositories with security alerts using security overview](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/interpreting-security-findings#finding-repositories-with-security-alerts-using-security-overview)
The information shown by security overview varies according to your access to repositories and organizations, and according to whether Advanced Security features are used by those repositories and organizations. For more information, see [About security overview](https://docs.github.com/en/code-security/security-overview/about-security-overview#permission-to-view-data-in-security-overview).
  1. On GitHub, navigate to the main page of the organization.
  2. Under your organization name, click 
![Screenshot of the horizontal navigation bar for an organization. A tab, labeled with a shield icon and "Security," is outlined in dark orange.](https://docs.github.com/assets/cb-22170/images/help/organizations/organization-security-tab.png)
  3. By default, the overview shows alerts for all native GitHub tools (filter: `tool:github`). To display alerts for a specific tool, replace `tool:github` in the filter text box. For example:
     * `tool:dependabot` to show only alerts for dependencies identified by Dependabot.
     * `tool:secret-scanning` to only show alerts for secrets identified by secret scanning.
     * `tool:codeql` to show only alerts for potential security vulnerabilities identified by CodeQL code scanning.
  4. You can add further filters to show only the repositories you want to assess. The list of repositories and metrics displayed on the page automatically update to match your current selection. For more information on filtering, see [Filtering alerts in security overview](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview).
  5. Optionally, use the sidebar on the left to explore alerts for a specific security feature in greater detail. On each page, you can use filters that are specific to that feature to refine your search. For more information about the available qualifiers, see [Filtering alerts in security overview](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview).


## [Interpreting secret scanning alerts](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/interpreting-security-findings#interpreting-secret-scanning-alerts)
Secret scanning is a security tool that scans the entire Git history of repositories, as well as issues, pull requests, discussions, and wikis in those repositories, for leaked secrets that have been accidentally committed, such as tokens or private keys. There are two types of secret scanning alerts:
  * Secret scanning alerts for partners, which are sent to the provider who issued the secret
  * Secret scanning alerts for users, which appear on GitHub and can be resolved


You can view secret scanning alerts for an organization by navigating to the main page of that organization, clicking the 
  * **Metrics**. To see detailed information on push protection events, see [Viewing metrics for secret scanning push protection](https://docs.github.com/en/code-security/security-overview/viewing-metrics-for-secret-scanning-push-protection).
  * **Alerts**. To see detailed information on **Default** and **Generic** alerts for exposed secrets in the organization.


For an introduction to secret scanning alerts, see [About secret scanning alerts](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/about-alerts).
To learn how to evaluate secret scanning alerts, see [Evaluating alerts from secret scanning](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts).
## [Interpreting code scanning alerts](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/interpreting-security-findings#interpreting-code-scanning-alerts)
Code scanning is a feature that you use to analyze the code in a GitHub repository to find security vulnerabilities and coding errors. Any problems identified by the analysis are shown in your repository. These problems are raised as code scanning alerts, which contain detailed information on the vulnerability or error detected.
You can view the code scanning alerts for an organization by navigating to the main page of that organization, clicking the 
  * **CodeQL pull request alerts**. To see information on code scanning alerts found and remediated in pull requests.
  * **Code scanning**. To see detailed information on alerts for potentially vulnerable code in the organization, see [Viewing metrics for pull request alerts](https://docs.github.com/en/code-security/security-overview/viewing-metrics-for-pull-request-alerts).


For an introduction to code scanning alerts, see [About code scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts).
To learn how to interpret and resolve code scanning alerts, see [Assessing code scanning alerts for your repository](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository) and [Resolving code scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/resolving-code-scanning-alerts).
## [Interpreting Dependabot alerts](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/interpreting-security-findings#interpreting-dependabot-alerts)
Dependabot alerts inform you about vulnerabilities in the dependencies that you use in repositories in your organization. You can view Dependabot alerts for an organization by navigating to the main page of that organization, clicking the 
For an introduction to Dependabot alerts, see [About Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts).
To learn how to interpret and resolve Dependabot alerts, see [Viewing and updating Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/viewing-and-updating-dependabot-alerts).
If you enabled Dependabot security updates, Dependabot can also automatically raise pull requests to update the dependencies used in the repositories of the organization. For more information, see [About Dependabot security updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates).
## [Next steps](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/interpreting-security-findings#next-steps)
If you are using the GitHub-recommended security configuration, and your findings indicate the security enablement settings are not meeting your needs, you should create a custom security configuration. To get started, see [Creating a custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/creating-a-custom-security-configuration).
If you are using a custom security configuration, and your findings indicate the security enablement settings are not meeting your needs, you can edit your existing configuration. For more information, see [Editing a custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/editing-a-custom-security-configuration).
Lastly, you can also edit your organization-level security settings with global settings. To learn more, see [Configuring global security settings for your organization](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization).
