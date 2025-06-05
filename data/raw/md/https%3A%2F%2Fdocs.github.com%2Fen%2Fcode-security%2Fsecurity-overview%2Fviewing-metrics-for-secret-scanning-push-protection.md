  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Security overview](https://docs.github.com/en/code-security/security-overview "Security overview")/
  * [View secret scanning metrics](https://docs.github.com/en/code-security/security-overview/viewing-metrics-for-secret-scanning-push-protection "View secret scanning metrics")


# Viewing metrics for secret scanning push protection
You can use security overview to see how secret scanning push protection is performing in repositories across your organization, and to identify repositories where you may need to take action.
## Who can use this feature?
Access requires:
  * Organization views: **write** access to repositories in the organization
  * Enterprise views: organization owners and security managers


Organizations owned by a GitHub Team account with GitHub Secret Protection, or owned by a GitHub Enterprise account
## In this article
  * [About metrics for secret scanning push protection](https://docs.github.com/en/code-security/security-overview/viewing-metrics-for-secret-scanning-push-protection#about-metrics-for-secret-scanning-push-protection)
  * [Viewing metrics for secret scanning push protection for an organization](https://docs.github.com/en/code-security/security-overview/viewing-metrics-for-secret-scanning-push-protection#viewing-metrics-for-secret-scanning-push-protection-for-an-organization)


Secret scanning metrics for push protection is currently in public preview and subject to change.
## [About metrics for secret scanning push protection](https://docs.github.com/en/code-security/security-overview/viewing-metrics-for-secret-scanning-push-protection#about-metrics-for-secret-scanning-push-protection)
The metrics overview for secret scanning push protection helps you to understand how well you are preventing security leaks in your organization. You can use the metrics to assess how push protection is performing, and to easily identify the repositories where you may need to take action in order to prevent leaks of sensitive information.
The overview shows you a summary of how many pushes containing secrets have been successfully blocked by push protection, as well as how many times push protection was bypassed.
You can also find more granular metrics, such as:
  * The secret types that have been blocked or bypassed the most
  * The repositories that have had the most pushes blocked
  * The repositories that are bypassing push protection the most
  * The percentage distribution of reasons that users give when they bypass the protection


Use the date picker to set the time range that you want to view alert activity and metrics for, and click in the search box to add further filters on the alerts and metrics displayed. For more information, see [Filtering alerts in security overview](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview#additional-filters-for-secret-scanning-alert-views).
You can see secret scanning metrics if you have:
  * The `admin` role for the repository.
  * A custom repository role with the "View secret scanning results" fine-grained permissions for the repository. For more information, see [About custom repository roles](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/about-custom-repository-roles#security).
  * Access to alerts for the repository. For more information, see [Managing security and analysis settings for your repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-security-and-analysis-settings-for-your-repository#granting-access-to-security-alerts).


The metrics are based on activity from the default period or your selected period.
## [Viewing metrics for secret scanning push protection for an organization](https://docs.github.com/en/code-security/security-overview/viewing-metrics-for-secret-scanning-push-protection#viewing-metrics-for-secret-scanning-push-protection-for-an-organization)
  1. On GitHub, navigate to the main page of the organization.
  2. Under your organization name, click 
![Screenshot of the horizontal navigation bar for an organization. A tab, labeled with a shield icon and "Security," is outlined in dark orange.](https://docs.github.com/assets/cb-22170/images/help/organizations/organization-security-tab.png)
  3. In the sidebar, under "Metrics", click 
  4. Click on an individual secret type or repository to see the associated secret scanning alerts for your organization.
  5. You can use the options at the top of the page to filter the group of repositories that you want to see secret scanning metrics for.
     * Use the date picker to set the time range that you want to view metrics for. Note that the date used by the date picker corresponds to the date a secret was bypassed on.
     * Click in the search box to add further filters on the secret scanning metrics displayed. For more information, see [Filtering alerts in security overview](https://docs.github.com/en/code-security/security-overview/filtering-alerts-in-security-overview).


