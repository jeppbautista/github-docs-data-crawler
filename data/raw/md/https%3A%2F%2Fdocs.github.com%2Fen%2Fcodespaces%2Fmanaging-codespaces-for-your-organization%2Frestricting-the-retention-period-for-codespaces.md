  * [Codespaces](https://docs.github.com/en/codespaces "Codespaces")/
  * [Managing your organization](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization "Managing your organization")/
  * [Restrict the retention period](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-retention-period-for-codespaces "Restrict the retention period")


# Restricting the retention period for codespaces
You can set a maximum retention period for any codespaces owned by your organization.
## Who can use this feature?
To manage retention constraints for an organization's codespaces, you must be an owner of the organization.
Organizations on GitHub Team and GitHub Enterprise plans can pay for members' and collaborators' use of GitHub Codespaces. These organizations can then access settings and policies to manage codespaces paid for by the organization. For more information, see [Choosing who owns and pays for codespaces in your organization](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/choosing-who-owns-and-pays-for-codespaces-in-your-organization#about-ownership-of-codespaces) and [GitHub’s plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans).
## In this article
  * [Overview](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-retention-period-for-codespaces#overview)
  * [Adding a policy to set a maximum codespace retention period](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-retention-period-for-codespaces#adding-a-policy-to-set-a-maximum-codespace-retention-period)
  * [Editing a policy](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-retention-period-for-codespaces#editing-a-policy)
  * [Deleting a policy](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-retention-period-for-codespaces#deleting-a-policy)


## [Overview](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-retention-period-for-codespaces#overview)
GitHub Codespaces are automatically deleted after they have been stopped and have remained inactive for a defined number of days. The retention period for each codespace is set when the codespace is created and does not change. The default retention period is 30 days.
GitHub users can set a personal retention period of less than 30 days for codespaces they create. For more information, see [Configuring automatic deletion of your codespaces](https://docs.github.com/en/codespaces/setting-your-user-preferences/configuring-automatic-deletion-of-your-codespaces).
As an organization owner, you may want to configure constraints on the maximum retention period for codespaces created for the repositories owned by your organization. This can help you to limit the storage costs associated with codespaces that are stopped and then left unused until they are automatically deleted. For more information about storage charges, see [About billing for GitHub Codespaces](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#codespaces-pricing). You can set a maximum retention period for all, or for specific, repositories owned by your organization.
Setting a maximum retention policy for a repository prevents people from exempting a codespace from automatic deletion. The "Keep codespace" option will be unavailable for codespaces created for that repository. For more information, see [Configuring automatic deletion of your codespaces](https://docs.github.com/en/codespaces/setting-your-user-preferences/configuring-automatic-deletion-of-your-codespaces?tool=webui#avoiding-automatic-deletion-of-codespaces).
### [Setting organization-wide and repository-specific policies](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-retention-period-for-codespaces#setting-organization-wide-and-repository-specific-policies)
When you create a policy, you choose whether it applies to all repositories in your organization, or only to specified repositories. If you create an organization-wide policy with a codespace retention constraint, then the retention constraints in any policies that are targeted at specific repositories should be shorter than the restriction configured for the entire organization, or they will have no effect. The shortest retention period - in an organization-wide policy, a policy targeted at specified repositories, or the default retention period in someone's personal settings - is applied.
If you add an organization-wide policy with a retention constraint, you should set the retention period to the longest acceptable period. You can then add separate policies that set the maximum retention to a shorter period for specific repositories in your organization.
Codespaces policies only apply to codespaces that your organizations pays for. If someone creates a codespace for a repository in your organization at their own expense, then the codespace will not be bound by these policies. For more information, see [Choosing who owns and pays for codespaces in your organization](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/choosing-who-owns-and-pays-for-codespaces-in-your-organization).
## [Adding a policy to set a maximum codespace retention period](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-retention-period-for-codespaces#adding-a-policy-to-set-a-maximum-codespace-retention-period)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the "Code, planning, and automation" section of the sidebar, select **Policies**.
  4. On the "Codespaces policies" page, click **Create Policy**.
  5. Enter a name for your new policy.
  6. Click **Add constraint** and choose **Retention period**.
  7. Click 
  8. Enter the maximum number of days codespaces can remain stopped before they are automatically deleted, then click **Save**.
![Screenshot of a dropdown with a field labeled "Maximum value" set to 8 days. Below this are "Cancel" and "Save" buttons.](https://docs.github.com/assets/cb-23271/images/help/codespaces/maximum-days-retention.png)
     * A day, in this context, is a 24-hour period, beginning at the time of day when the codespace was stopped.
     * The valid range is 0-30 days.
     * Setting the period to `0` will result in codespaces being immediately deleted when they are stopped, or when they timeout due to inactivity.
  9. By default the policy is set to apply to all repositories, if you want it to apply only to some of the repositories in your organization, click **All repositories** and then click **Selected repositories** in the dropdown menu.
![Screenshot of the repository selection dropdown, showing the options "All repositories" and "Selected repositories."](https://docs.github.com/assets/cb-48372/images/help/codespaces/selected-repositories.png)
If you're adding a constraint to an existing policy that already contains the "Maximum codespaces per user" constraint, you won't be able to apply the policy to selected repositories. This is because the "Maximum codespaces per user" constraint always applies to all repositories in the organization.
With **Selected repositories** selected:
    1. Click 
![Screenshot of the settings icon \(a gear symbol\) to the left of a button labeled "Selected repositories."](https://docs.github.com/assets/cb-7694/images/help/codespaces/policy-edit.png)
    2. Select the repositories you want this policy to apply to.
    3. At the bottom of the repository list, click **Select repositories**.
![Screenshot of a list of repositories, each with a checkbox. Three repositories are selected.](https://docs.github.com/assets/cb-53629/images/help/codespaces/policy-select-repos.png)
  10. If you want to add another constraint to the policy, click **Add constraint** and choose another constraint. For information about other constraints, see:
     * [Restricting access to machine types](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-access-to-machine-types)
     * [Restricting the number of organization-billed codespaces a user can create](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-number-of-organization-billed-codespaces-a-user-can-create)
     * [Restricting the base image for codespaces](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-base-image-for-codespaces)
     * [Restricting the visibility of forwarded ports](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-visibility-of-forwarded-ports)
     * [Restricting the idle timeout period](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-idle-timeout-period)
  11. After you've finished adding constraints to your policy, click **Save**.


The policy will be applied to all new codespaces that are billable to your organization. The retention period constraint is only applied on codespace creation.
## [Editing a policy](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-retention-period-for-codespaces#editing-a-policy)
You can edit an existing policy. For example, you may want to add or remove constraints to or from a policy.
The retention period constraint is only applied to codespaces when they are created. Editing a policy has no effect on existing codespaces.
  1. Display the "Codespaces policies" page. For more information, see [Adding a policy to set a maximum codespace retention period](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-retention-period-for-codespaces#adding-a-policy-to-set-a-maximum-codespace-retention-period).
  2. Click the name of the policy you want to edit.
  3. Beside the "Retention period" constraint, click 
  4. Make the required changes then click **Save**.


## [Deleting a policy](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-retention-period-for-codespaces#deleting-a-policy)
You can delete a policy at any time. Deleting a policy has no effect on existing codespaces.
  1. Display the "Codespaces policies" page. For more information, see [Adding a policy to set a maximum codespace retention period](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-retention-period-for-codespaces#adding-a-policy-to-set-a-maximum-codespace-retention-period).
  2. Click the delete button to the right of the policy you want to delete.
  3. Click 
![Screenshot of a policy with the delete button \(a trash can icon\) highlighted with a dark orange outline.](https://docs.github.com/assets/cb-9797/images/help/codespaces/policy-delete.png)


