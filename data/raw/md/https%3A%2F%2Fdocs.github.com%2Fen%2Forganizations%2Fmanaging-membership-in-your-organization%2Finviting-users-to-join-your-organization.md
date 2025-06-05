  * [Organizations](https://docs.github.com/en/organizations "Organizations")/
  * [Manage membership](https://docs.github.com/en/organizations/managing-membership-in-your-organization "Manage membership")/
  * [Invite users to join](https://docs.github.com/en/organizations/managing-membership-in-your-organization/inviting-users-to-join-your-organization "Invite users to join")


# Inviting users to join your organization
You can invite anyone to become a member of your organization using their username or email address for GitHub.
## Who can use this feature?
Organization owners can invite users to join an organization.
## In this article
  * [About organization invitations](https://docs.github.com/en/organizations/managing-membership-in-your-organization/inviting-users-to-join-your-organization#about-organization-invitations)
  * [Inviting a user to join your organization](https://docs.github.com/en/organizations/managing-membership-in-your-organization/inviting-users-to-join-your-organization#inviting-a-user-to-join-your-organization)
  * [Retrying or canceling expired invitations](https://docs.github.com/en/organizations/managing-membership-in-your-organization/inviting-users-to-join-your-organization#retrying-or-canceling-expired-invitations)
  * [Further reading](https://docs.github.com/en/organizations/managing-membership-in-your-organization/inviting-users-to-join-your-organization#further-reading)


This article does not apply to Enterprise Managed Users. Managed user accounts are provisioned using SCIM, not invited.
## [About organization invitations](https://docs.github.com/en/organizations/managing-membership-in-your-organization/inviting-users-to-join-your-organization#about-organization-invitations)
When you invite someone to become a member of your organization, the person receives an email with an invitation link. To join the organization, the invitee clicks the invitation link in the email.
You can use a person's GitHub username or email address for the invitation.
If you use an email address for the invitation, the invitee will only be able to accept the invitation if the email address matches with a verified email address associated with the invitee's personal account on GitHub. For more information, see [Verifying your email address](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/verifying-your-email-address).
If an invitee's personal account has been flagged, the invitee won't be able to accept any new or pending invitations to join organizations.
If your organization has a paid per-user subscription, an unused license must be available before you can invite a new member to join the organization or reinstate a former organization member. For more information, see [About per-user pricing](https://docs.github.com/en/billing/managing-the-plan-for-your-github-account/about-per-user-pricing).
If an invitee does not accept the invitation within seven days, the pending invitation expires automatically.
If your organization requires members to use two-factor authentication, users that you invite must enable two-factor authentication before accepting the invitation. For more information, see [Requiring two-factor authentication in your organization](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-two-factor-authentication-for-your-organization/requiring-two-factor-authentication-in-your-organization) and [Securing your account with two-factor authentication (2FA)](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa).
Organizations that use GitHub Enterprise Cloud can implement SCIM to add, manage, and remove organization members' access to GitHub through an identity provider (IdP). For more information, see [About SCIM for organizations](https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-saml-single-sign-on-for-your-organization/about-scim-for-organizations)" in the GitHub Enterprise Cloud documentation.
To prevent abuse, you can only create 50 organization invitations within a 24-hour period. If your organization is more than one month old or on a paid plan, the limit is 500 invitations per 24 hour period.
## [Inviting a user to join your organization](https://docs.github.com/en/organizations/managing-membership-in-your-organization/inviting-users-to-join-your-organization#inviting-a-user-to-join-your-organization)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Click the name of your organization.
  3. Under your organization name, click 
![Screenshot of the horizontal navigation bar for an organization. A tab, labeled with a person icon and "People," is outlined in dark orange.](https://docs.github.com/assets/cb-18976/images/help/organizations/organization-people-tab.png)
  4. Click **Invite member**.
  5. In the search field, type the username, full name, or email address of the person you want to invite and click **Invite**.
  6. If the person you're inviting was an organization member within the last three months, select whether to restore their privileges or start fresh, then click **Invite and reinstate** or **Invite and start fresh**.
  7. If the person you're inviting has never been a member of the organization or if you cleared their privileges, under "Role in the organization," select an organization role for the user.
  8. Optionally, to add the user to a team in the organization, select the team.
  9. Click **Send invitation**.
  10. The invited person will receive an email inviting them to the organization. They will need to accept the invitation before becoming a member of the organization. You can [edit or cancel an invitation](https://docs.github.com/en/organizations/managing-membership-in-your-organization/canceling-or-editing-an-invitation-to-join-your-organization) any time before the user accepts.


## [Retrying or canceling expired invitations](https://docs.github.com/en/organizations/managing-membership-in-your-organization/inviting-users-to-join-your-organization#retrying-or-canceling-expired-invitations)
Invitations expire after 7 days. You can retry or cancel expired invitations, either one by one or in bulk. Failed invitations to outside collaborators can also be found in this view.
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Click the name of your organization.
  3. Under your organization name, click 
![Screenshot of the horizontal navigation bar for an organization. A tab, labeled with a person icon and "People," is outlined in dark orange.](https://docs.github.com/assets/cb-18976/images/help/organizations/organization-people-tab.png)
  4. In the "Organization permissions" sidebar, click **Failed invitations**.
  5. Next to an invitation, select the **Retry invitation** or **Cancel invitation**.
![Screenshot of the list of failed invitations for an organization. To the right of the first entry, a kebab icon is outlined in dark orange.](https://docs.github.com/assets/cb-27352/images/help/organizations/retry-or-cancel-invitation.png)
  6. To confirm, click **Retry invitation** or **Cancel invitation**.


## [Further reading](https://docs.github.com/en/organizations/managing-membership-in-your-organization/inviting-users-to-join-your-organization#further-reading)
  * [Adding organization members to a team](https://docs.github.com/en/organizations/organizing-members-into-teams/adding-organization-members-to-a-team)


