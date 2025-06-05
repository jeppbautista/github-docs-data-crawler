  * [Organizations](https://docs.github.com/en/organizations "Organizations")/
  * [Manage organization settings](https://docs.github.com/en/organizations/managing-organization-settings "Manage organization settings")/
  * [Verify or approve a domain](https://docs.github.com/en/organizations/managing-organization-settings/verifying-or-approving-a-domain-for-your-organization "Verify or approve a domain")


# Verifying or approving a domain for your organization
You can verify your ownership of domains with GitHub to confirm your organization's identity.
## Who can use this feature?
Organization owners can verify or approve a domain for an organization.
## In this article
  * [About domain verification](https://docs.github.com/en/organizations/managing-organization-settings/verifying-or-approving-a-domain-for-your-organization#about-domain-verification)
  * [Verifying a domain for your organization](https://docs.github.com/en/organizations/managing-organization-settings/verifying-or-approving-a-domain-for-your-organization#verifying-a-domain-for-your-organization)
  * [Approving a domain for your organization](https://docs.github.com/en/organizations/managing-organization-settings/verifying-or-approving-a-domain-for-your-organization#approving-a-domain-for-your-organization)
  * [Removing an approved or verified domain](https://docs.github.com/en/organizations/managing-organization-settings/verifying-or-approving-a-domain-for-your-organization#removing-an-approved-or-verified-domain)


## [About domain verification](https://docs.github.com/en/organizations/managing-organization-settings/verifying-or-approving-a-domain-for-your-organization#about-domain-verification)
After verifying ownership of your organization's domains, a "Verified" badge will display on the organization's profile.
To display a "Verified" badge, the website and email information shown on an organization's profile must match the verified domain or domains. If the website and email address shown on your organization's profile are hosted on different domains, you must verify both domains. If the website and email address use variants of the same domain, you must verify both variants. For example, if the profile shows the website `www.example.com` and the email address `info@example.com`, you would need to verify both `www.example.com` and `example.com`.
If you confirm your organization’s identity by verifying your domain and restricting email notifications to only verified email domains, you can help prevent sensitive information from being exposed. For more information see [Best practices for preventing data leaks in your organization](https://docs.github.com/en/code-security/getting-started/best-practices-for-preventing-data-leaks-in-your-organization).
## [Verifying a domain for your organization](https://docs.github.com/en/organizations/managing-organization-settings/verifying-or-approving-a-domain-for-your-organization#verifying-a-domain-for-your-organization)
To verify a domain, you must have access to modify domain records with your domain hosting service.
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the "Security" section of the sidebar, click 
  4. Next to "Verified & approved domains for your enterprise account", click **Add a domain**.
  5. Under "What domain would you like to add?", type the domain you'd like to verify, then click **Add domain**.
  6. Follow the instructions under "Add a DNS TXT record" to create a DNS TXT record with your domain hosting service.
  7. Wait for your DNS configuration to change, which may take up to 72 hours. You can confirm your DNS configuration has changed by running the `dig` command on the command line, replacing `TXT-RECORD-NAME` with the name of the TXT record created in your DNS configuration. You should see your new TXT record listed in the command output.
```
dig TXT-RECORD-NAME +nostats +nocomments +nocmd TXT

```

  8. After confirming your TXT record is added to your DNS, follow steps one through three above to navigate to your organization's approved and verified domains.
  9. To the right of the domain that's pending verification, select the **Continue verifying**.
![Screenshot of the "Verified & approved domains" page. To the right of a domain that is pending verification, a kebab icon is outlined in dark orange.](https://docs.github.com/assets/cb-66704/images/help/organizations/continue-verifying-domain.png)
  10. Click **Verify**.
  11. Optionally, once the "Verified" badge is visible on your organization's profile page, you can delete the TXT entry from the DNS record at your domain hosting service.


## [Approving a domain for your organization](https://docs.github.com/en/organizations/managing-organization-settings/verifying-or-approving-a-domain-for-your-organization#approving-a-domain-for-your-organization)
The ability to approve a domain not owned by your organization or enterprise is currently in public preview and subject to change.
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the "Security" section of the sidebar, click 
  4. Next to "Verified & approved domains for your enterprise account", click **Add a domain**.
  5. Under "What domain would you like to add?", type the domain you'd like to verify, then click **Add domain**.
  6. To the right of "Can't verify this domain?", click **Approve it instead**.
![Screenshot of the "Verify domain" page. To the right of the "Verify" button, a link, labeled "Approve it instead," is outlined in dark orange.](https://docs.github.com/assets/cb-26751/images/help/organizations/domains-approve-it-instead.png)
  7. Read the information about domain approval, then click **Approve DOMAIN**.


## [Removing an approved or verified domain](https://docs.github.com/en/organizations/managing-organization-settings/verifying-or-approving-a-domain-for-your-organization#removing-an-approved-or-verified-domain)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the "Security" section of the sidebar, click 
  4. To the right of the domain to remove, select the **Delete**.
![Screenshot of the "Verified & approved domains" page. To the right of a domain, a kebab icon is outlined in dark orange.](https://docs.github.com/assets/cb-66704/images/help/organizations/continue-verifying-domain.png)


