  * [Codespaces](https://docs.github.com/en/codespaces "Codespaces")/
  * [Managing your organization](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization "Managing your organization")/
  * [Billing and ownership](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/choosing-who-owns-and-pays-for-codespaces-in-your-organization "Billing and ownership")


# Choosing who owns and pays for codespaces in your organization
You can choose whether codespaces are paid for and owned by your organization or by your members.
## Who can use this feature?
Organization owners can change an organization's billing details and control who owns and pays for codespaces.
Organizations on GitHub Team and GitHub Enterprise plans can pay for their members' use of GitHub Codespaces. These organizations can then access policies that apply to codespaces paid for by the organization. See [GitHub’s plans](https://docs.github.com/en/get-started/learning-about-github/githubs-products).
## In this article
  * [Overview](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/choosing-who-owns-and-pays-for-codespaces-in-your-organization#overview)
  * [About choosing who pays for codespaces](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/choosing-who-owns-and-pays-for-codespaces-in-your-organization#about-choosing-who-pays-for-codespaces)
  * [About ownership of codespaces](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/choosing-who-owns-and-pays-for-codespaces-in-your-organization#about-ownership-of-codespaces)
  * [About changing your settings](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/choosing-who-owns-and-pays-for-codespaces-in-your-organization#about-changing-your-settings)
  * [Choosing who owns and pays for codespaces](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/choosing-who-owns-and-pays-for-codespaces-in-your-organization#choosing-who-owns-and-pays-for-codespaces)
  * [Setting a spending limit](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/choosing-who-owns-and-pays-for-codespaces-in-your-organization#setting-a-spending-limit)


## [Overview](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/choosing-who-owns-and-pays-for-codespaces-in-your-organization#overview)
If you're the owner of an organization on a GitHub Team or GitHub Enterprise Cloud plan, you can pay for your members' and collaborators' usage of GitHub Codespaces. Paying for usage will allow people to use GitHub Codespaces to work in your repositories without having to do so at their own expense and will give your organization more control over the codespaces created from your repositories.
To pay for usage, you must do all of the following things:
  * Allow at least some of your members and collaborators to use GitHub Codespaces in your organization's private repositories. See [Enabling or disabling GitHub Codespaces for your organization](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/enabling-or-disabling-github-codespaces-for-your-organization#enabling-or-disabling-github-codespaces).
  * Choose for codespaces created from your organization's repositories to be **organization-owned**. See [Choosing who owns and pays for codespaces](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/choosing-who-owns-and-pays-for-codespaces-in-your-organization#choosing-who-owns-and-pays-for-codespaces).
  * Set a non-zero spending limit for GitHub Codespaces. See [Managing the spending limit for GitHub Codespaces](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-codespaces/managing-the-spending-limit-for-github-codespaces#managing-the-github-codespaces-spending-limit-for-your-organization-account).


## [About choosing who pays for codespaces](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/choosing-who-owns-and-pays-for-codespaces-in-your-organization#about-choosing-who-pays-for-codespaces)
Paying for a codespace means paying for the storage and compute costs of the codespace over the codespace's lifetime. See [About billing for GitHub Codespaces](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-codespaces/about-billing-for-github-codespaces).
Organizations on a GitHub Free plan cannot pay for GitHub Codespaces, so the user who creates the codespace always pays.
For organizations on a GitHub Team or GitHub Enterprise Cloud plan, when a user creates a codespace from a repository in the organization, either the user or the organization can pay for the codespace. The user who creates a codespace can't choose who pays for it, but the organization can choose to pay for certain users. In an organization's settings, you can choose for codespaces to be **user-owned** or **organization-owned**.
If an organization chooses for codespaces to be **user-owned** , a user who creates a codespace from a repository in the organization always pays for the codespace. The user's access to create codespaces depends on the visibility of the repository and your organization's access settings.
If an organization chooses for codespaces to be **organization-owned** , the organization will pay for a codespace if all the following things are true:
  * The organization has set a non-zero spending limit for GitHub Codespaces.
  * The codespace is created from one of the organization's repositories, or from a fork of one of the organization's repositories. This includes both public and private repositories.
  * The user creating the codespace is a member or collaborator of the organization, and the organization has enabled GitHub Codespaces for this user. This can include all members and collaborators if the organization has chosen to enable Codespaces for all users. If Codespaces isn't enabled for a user, they can still create codespaces from public repositories in the organization, but the user will pay for these codespaces.


For more information about enabling GitHub Codespaces for members and collaborators, see [Enabling or disabling GitHub Codespaces for your organization](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/enabling-or-disabling-github-codespaces-for-your-organization).
## [About ownership of codespaces](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/choosing-who-owns-and-pays-for-codespaces-in-your-organization#about-ownership-of-codespaces)
A codespace is paid for by the account that owns it. The codespace owner can be the user who created the codespace, or it can be an organization.
If your organization owns a codespace, your organization has control over that codespace. For example, for codespaces owned by your organization, you can:
  * Use the [REST API](https://docs.github.com/en/rest/codespaces/organizations) to manage codespaces, such as stopping or deleting a codespace
  * Access audit logs to review actions related to GitHub Codespaces
  * Set policies to manage constraints, such as restricting the dev container image or machine type that can be used in codespaces, or setting a default timeout and retention period


If a user owns a codespace, your organization does not have any of these options for managing the codespace, even if the codespace was created from one of your organization's repositories.
When a user creates a codespace, they're told who will pay for it, and therefore who owns it. From a user's point of view, apart from the policies your organization can use to set constraints on codespaces, the experience with GitHub Codespaces will be similar regardless of who owns a codespace. For example, most of a user's personal settings for GitHub Codespaces, such as dotfiles, secrets, and GPG verification, apply regardless of who owns the codespace.
## [About changing your settings](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/choosing-who-owns-and-pays-for-codespaces-in-your-organization#about-changing-your-settings)
When you change your ownership settings, existing codespaces can transfer to a new owner.
If you change from **organization ownership** to **user ownership** , codespaces that are currently owned by your organization will be transferred to the ownership of the user who created the codespace. Before you make this change, you should ask each user to review the codespaces that will be transferred to their ownership. These codespaces will now incur usage on the user's personal account.
If you change from **user ownership** to **organization ownership** , existing codespaces may be transferred to your organization's ownership. A codespace will be transferred if the user who currently owns the codespace is a member or collaborator, and you have enabled GitHub Codespaces for this user. Otherwise, a codespace will remain under the ownership of the user.
## [Choosing who owns and pays for codespaces](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/choosing-who-owns-and-pays-for-codespaces-in-your-organization#choosing-who-owns-and-pays-for-codespaces)
If you cannot access the option to make codespaces **organization-owned** , this may be because you have disabled GitHub Codespaces for all users in your organization's private repositories. See [About choosing who pays for codespaces](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/choosing-who-owns-and-pays-for-codespaces-in-your-organization#about-choosing-who-pays-for-codespaces).
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the left sidebar, click 
  4. Under **General**.
  5. On the Codespaces settings page, under "Codespace ownership," select the setting you want for your organization:
     * **Organization ownership:** Codespaces can be owned and paid for by your organization.
     * **User ownership:** Codespaces are always owned and paid for by the user who creates the codespace.
  6. Optionally, under "Codespaces access," review the members and collaborators for whom you have enabled Codespaces. These are the only users who can create codespaces that your organization pays for. See [Enabling or disabling GitHub Codespaces for your organization](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/enabling-or-disabling-github-codespaces-for-your-organization).


## [Setting a spending limit](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/choosing-who-owns-and-pays-for-codespaces-in-your-organization#setting-a-spending-limit)
You must set a non-zero spending limit on your personal, organization, or enterprise account before the account can be billed for use of GitHub Codespaces.
By default, all accounts have a GitHub Codespaces spending limit of $0 USD. This prevents new codespaces being created, or existing codespaces being opened, if doing so would incur a billable cost to your personal, organization, or enterprise account. For personal accounts, if you have access to create a codespace, you can do so as long as the account has not reached the limit of its monthly included usage. For organizations and enterprises, the default spending limit means that, to allow people to create codespaces that are billed to the organization, or its parent enterprise, the limit must be changed to a value above $0 USD.
For information on managing and changing your account's spending limit, see [Managing the spending limit for GitHub Codespaces](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-codespaces/managing-the-spending-limit-for-github-codespaces#managing-the-github-codespaces-spending-limit-for-your-organization-account).
