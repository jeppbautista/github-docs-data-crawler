  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Manage Copilot](https://docs.github.com/en/copilot/managing-copilot "Manage Copilot")/
  * [Manage for organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization "Manage for organization")/
  * [Manage access](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-access-to-github-copilot-in-your-organization "Manage access")/
  * [Revoke access](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-access-to-github-copilot-in-your-organization/revoking-access-to-copilot-for-members-of-your-organization "Revoke access")


# Revoking access to Copilot for members of your organization
Remove access to GitHub Copilot for some or all of the members of your organization.
## Who can use this feature?
Organization owners for organizations with a Copilot Business plan.
## In this article
  * [How revoking access affects billing](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-access-to-github-copilot-in-your-organization/revoking-access-to-copilot-for-members-of-your-organization#how-revoking-access-affects-billing)
  * [Revoking access to Copilot for your whole organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-access-to-github-copilot-in-your-organization/revoking-access-to-copilot-for-members-of-your-organization#revoking-access-to-copilot-for-your-whole-organization)
  * [Revoking access to Copilot for specific users in your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-access-to-github-copilot-in-your-organization/revoking-access-to-copilot-for-members-of-your-organization#revoking-access-to-copilot-for-specific-users-in-your-organization)
  * [Using the API to revoke access to Copilot](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-access-to-github-copilot-in-your-organization/revoking-access-to-copilot-for-members-of-your-organization#using-the-api-to-revoke-access-to-copilot)
  * [Further reading](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-access-to-github-copilot-in-your-organization/revoking-access-to-copilot-for-members-of-your-organization#further-reading)


## [How revoking access affects billing](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-access-to-github-copilot-in-your-organization/revoking-access-to-copilot-for-members-of-your-organization#how-revoking-access-affects-billing)
Revoking access takes effect from the start of the next billing cycle. If you remove a seat during a cycle, the user will have access to Copilot for the remainder of the billing cycle. For more information, see [About billing for GitHub Copilot](https://docs.github.com/en/billing/managing-billing-for-github-copilot/about-billing-for-github-copilot).
## [Revoking access to Copilot for your whole organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-access-to-github-copilot-in-your-organization/revoking-access-to-copilot-for-members-of-your-organization#revoking-access-to-copilot-for-your-whole-organization)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the "Access" section of the sidebar, click **Licensing** (new platform). Alternatively, in the "Code planning, and automation" section of the sidebar, click **Access** (original platform).
If you have not configured all policies for Copilot, you will not be able to complete the following steps. If that is the case, click **Go to policies** and ensure all policies are configured before proceeding.
  4. Under "Copilot Business is active in your organization," to revoke GitHub Copilot access for all users in your organization, select **Disabled**.
  5. In the "Remove Copilot access" dialog, click **Confirm and remove seats**.


## [Revoking access to Copilot for specific users in your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-access-to-github-copilot-in-your-organization/revoking-access-to-copilot-for-members-of-your-organization#revoking-access-to-copilot-for-specific-users-in-your-organization)
Removing a user from the organization(s) that had granted them Copilot access will automatically revoke their Copilot access. Alternatively, you can revoke Copilot access while preserving their organization membership.
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the "Code, planning, and automation" section of the sidebar, click **Access**.
  4. Under "Copilot Business is active in your organization," select **Enabled For: selected members**.
     * In the "Confirm policy update" dialog, click **Renew seats**.
  5. Under "Access management," in the search bar, type the member's username or full name.
  6. To remove the member from the list of users who have access to Copilot, select the checkbox to the left of their username, then click **Cancel seat**.
![Screenshot of the Access management section, with a user selected and the 'Cancel seat' button highlighted.](https://docs.github.com/assets/cb-31963/images/help/copilot/cancel-copilot-seat.png)
  7. In the "Confirm seat removal" dialog, click **Remove seats**.


## [Using the API to revoke access to Copilot](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-access-to-github-copilot-in-your-organization/revoking-access-to-copilot-for-members-of-your-organization#using-the-api-to-revoke-access-to-copilot)
You can use GitHub's REST API to revoke access to Copilot for teams, or specific users, in your organization. For example, you might want to write a script to automatically revoke seats for organization members who have not been using Copilot. See [Remove teams from the Copilot subscription for an organization](https://docs.github.com/en/rest/copilot/copilot-user-management?apiVersion=2022-11-28#remove-teams-from-the-copilot-subscription-for-an-organization) and [Remove users from the Copilot subscription for an organization](https://docs.github.com/en/rest/copilot/copilot-user-management?apiVersion=2022-11-28#remove-users-from-the-copilot-subscription-for-an-organization).
## [Further reading](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-access-to-github-copilot-in-your-organization/revoking-access-to-copilot-for-members-of-your-organization#further-reading)
  * [GitHub Copilot Trust Center](https://copilot.github.trust.page)
  * [Granting access to Copilot for members of your organization](https://docs.github.com/en/copilot/managing-github-copilot-in-your-organization/granting-access-to-copilot-for-members-of-your-organization).
  * [Reviewing user activity data for Copilot in your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/reviewing-github-copilot-activity-in-your-organization/reviewing-usage-data-for-github-copilot-in-your-organization)


