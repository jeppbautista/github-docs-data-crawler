  * [Organizations](https://docs.github.com/en/organizations "Organizations")/
  * [Organization security](https://docs.github.com/en/organizations/keeping-your-organization-secure "Organization security")/
  * [Manage security settings](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization "Manage security settings")/
  * [IP addresses in audit log](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/displaying-ip-addresses-in-the-audit-log-for-your-organization "IP addresses in audit log")


# Displaying IP addresses in the audit log for your organization
You can display the source IP address for events in your organization's audit log.
## Who can use this feature?
Organization owners can display IP addresses in the audit log for an enterprise.
## In this article
  * [About display of IP addresses in the audit log](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/displaying-ip-addresses-in-the-audit-log-for-your-organization#about-display-of-ip-addresses-in-the-audit-log)
  * [Events that display IP addresses in the audit log](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/displaying-ip-addresses-in-the-audit-log-for-your-organization#events-that-display-ip-addresses-in-the-audit-log)
  * [Enabling display of IP addresses in the audit log](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/displaying-ip-addresses-in-the-audit-log-for-your-organization#enabling-display-of-ip-addresses-in-the-audit-log)


Displaying IP addresses in the audit log for an organization is in public preview and subject to change.
## [About display of IP addresses in the audit log](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/displaying-ip-addresses-in-the-audit-log-for-your-organization#about-display-of-ip-addresses-in-the-audit-log)
By default, GitHub does not display the source IP address for events in your organization's audit log. Optionally, to ensure compliance and respond to threats, you can display the full IP address associated with the actor responsible for each event. Actors are typically users, but can also be apps or integrations. If you enable this setting, the IP address will be displayed for **new and existing events** in the audit log.
You are responsible for meeting any legal obligations that accompany the viewing or storage of IP addresses displayed within your organization's audit log.
When anyone creates an account on GitHub, the person agrees to GitHub's collection of basic information about connections to GitHub's services, including source IP address. For more information, see [GitHub General Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement#usage-information).
After you enable the feature, you can access the audit log to view events that include IP addresses. For more information, see [Reviewing the audit log for your organization](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/reviewing-the-audit-log-for-your-organization).
## [Events that display IP addresses in the audit log](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/displaying-ip-addresses-in-the-audit-log-for-your-organization#events-that-display-ip-addresses-in-the-audit-log)
GitHub displays an IP address for each event in the organization audit log that meets these criteria.
  * The actor is an organization member or owner
  * The target is either an organization-owned repository that is private or internal, or an organization resource that is not a repository, such as a project.


## [Enabling display of IP addresses in the audit log](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/displaying-ip-addresses-in-the-audit-log-for-your-organization#enabling-display-of-ip-addresses-in-the-audit-log)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the "Archive" section of the sidebar, click **Audit log**.
  4. On the **Settings** tab, under "Disclose actor IP addresses in audit logs", select **Enable source IP disclosure**.
  5. Click **Save**.


