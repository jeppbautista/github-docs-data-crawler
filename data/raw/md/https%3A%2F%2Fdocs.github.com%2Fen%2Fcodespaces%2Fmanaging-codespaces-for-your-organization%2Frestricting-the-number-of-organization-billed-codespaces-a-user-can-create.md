  * [Codespaces](https://docs.github.com/en/codespaces "Codespaces")/
  * [Managing your organization](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization "Managing your organization")/
  * [Restrict codespace creation](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-number-of-organization-billed-codespaces-a-user-can-create "Restrict codespace creation")


# Restricting the number of organization-billed codespaces a user can create
You can specify the maximum number of codespaces that any member of your organization, or collaborator, can create for the repositories in your organization.
## Who can use this feature?
To manage this constraint for an organization, you must be an owner of the organization.
Organizations on GitHub Team and GitHub Enterprise plans can pay for members' and collaborators' use of GitHub Codespaces. These organizations can then access settings and policies to manage codespaces paid for by the organization. For more information, see [Choosing who owns and pays for codespaces in your organization](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/choosing-who-owns-and-pays-for-codespaces-in-your-organization#about-ownership-of-codespaces) and [GitHub’s plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans).
## In this article
  * [Overview](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-number-of-organization-billed-codespaces-a-user-can-create#overview)
  * [Adding a policy to define the maximum codespaces per user](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-number-of-organization-billed-codespaces-a-user-can-create#adding-a-policy-to-define-the-maximum-codespaces-per-user)
  * [Editing a policy](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-number-of-organization-billed-codespaces-a-user-can-create#editing-a-policy)
  * [Deleting a policy](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-number-of-organization-billed-codespaces-a-user-can-create#deleting-a-policy)


## [Overview](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-number-of-organization-billed-codespaces-a-user-can-create#overview)
By default, if organization members, or collaborators, are permitted to create codespaces that are billable to your organization, they can create multiple such codespaces. The number of organization-billed codespaces someone can create is governed by a limit to the total number of codespaces that they can create across all repositories they can access. This limit is set by GitHub.
As an organization owner, you can restrict the number of codespaces that each user can create, where the costs of the codespace are billable to the organization. This can help to reduce the overall cost of GitHub Codespaces to the organization, as there is a charge for codespace storage. For more information, see [About billing for GitHub Codespaces](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#about-billing-for-storage-usage).
To restrict the maximum number of organization-billed codespaces that users can create, you create a policy in the Codespaces settings for your organization. For example, if you set the maximum to 2, users who already have 2 active or stopped codespaces that are billed to your organization will have to delete one of these before they can create a new codespace that's billed to the organization.
This setting does not restrict users from creating codespaces that are not billed to your organization. For example, they can create additional codespaces for public repositories, using their personal Codespaces usage allowance. However, users who are permitted to create organization-billed codespaces, but have reached the limit for such codespaces, cannot choose to create a codespace for an organization-owned repository using their personal included allowance.
For information about the free use of GitHub Codespaces for personal accounts, see [About billing for GitHub Codespaces](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts). For information on how to choose who can create codespaces that are billed to your organization, see [Enabling or disabling GitHub Codespaces for your organization](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/enabling-or-disabling-github-codespaces-for-your-organization#choose-who-can-create-codespaces-that-are-billed-to-your-organization).
Policies with the "Maximum codespaces per user" constraint are applied to every repository in your organization. You can't, therefore, add this constraint to an existing policy that is configured to apply only to selected repositories.
## [Adding a policy to define the maximum codespaces per user](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-number-of-organization-billed-codespaces-a-user-can-create#adding-a-policy-to-define-the-maximum-codespaces-per-user)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the "Code, planning, and automation" section of the sidebar, select **Policies**.
  4. On the "Codespaces policies" page, click **Create Policy**.
  5. Enter a name for your new policy.
  6. Click **Add constraint** and choose **Maximum codespaces per user**.
  7. Click 
  8. In the "Maximum value" field, enter the maximum number of organization-billed codespaces that each user can create.
![Screenshot of the 'Maximum value' dialog with the value '2' being entered, and 'Cancel' and 'Save' buttons.](https://docs.github.com/assets/cb-19420/images/help/codespaces/maximum-value-policy-setting.png)
  9. Click **Save**.
  10. If you want to add another constraint to the policy, click **Add constraint** and choose another constraint. For information about other constraints, see:
     * [Restricting access to machine types](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-access-to-machine-types)
     * [Restricting the base image for codespaces](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-base-image-for-codespaces)
     * [Restricting the visibility of forwarded ports](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-visibility-of-forwarded-ports)
     * [Restricting the idle timeout period](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-idle-timeout-period)
     * [Restricting the retention period for codespaces](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-retention-period-for-codespaces)
When you add a constraint to a policy that already contains the "Maximum codespaces per user" constraint, you won't be able to restrict the additional constraint to specific repositories, as the "Maximum codespaces per user" constraint applies to all repositories in the organization.
  11. After you've finished adding constraints to your policy, click **Save**.


The policy is applied when anyone attempts to create a new codespace that is billable to your organization.
## [Editing a policy](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-number-of-organization-billed-codespaces-a-user-can-create#editing-a-policy)
You can edit an existing policy. For example, you may want to add or remove constraints to or from a policy.
  1. Display the "Codespaces policies" page. For more information, see [Adding a policy to define the maximum codespaces per user](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-number-of-organization-billed-codespaces-a-user-can-create#adding-a-policy-to-define-the-maximum-codespaces-per-user).
  2. Click the name of the policy you want to edit.
  3. Beside the "Maximum codespaces per user" constraint, click 
  4. Edit the maximum number of codespaces.
  5. Click **Save**.


## [Deleting a policy](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-number-of-organization-billed-codespaces-a-user-can-create#deleting-a-policy)
  1. Display the "Codespaces policies" page. For more information, see [Adding a policy to define the maximum codespaces per user](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-number-of-organization-billed-codespaces-a-user-can-create#adding-a-policy-to-define-the-maximum-codespaces-per-user).
  2. Click 


