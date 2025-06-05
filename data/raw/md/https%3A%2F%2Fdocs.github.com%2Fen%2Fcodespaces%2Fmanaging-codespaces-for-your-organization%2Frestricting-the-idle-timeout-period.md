  * [Codespaces](https://docs.github.com/en/codespaces "Codespaces")/
  * [Managing your organization](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization "Managing your organization")/
  * [Restrict timeout periods](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-idle-timeout-period "Restrict timeout periods")


# Restricting the idle timeout period
You can set a maximum timeout period for any codespaces owned by your organization.
## Who can use this feature?
To manage timeout constraints for an organization's codespaces, you must be an owner of the organization.
Organizations on GitHub Team and GitHub Enterprise plans can pay for members' and collaborators' use of GitHub Codespaces. These organizations can then access settings and policies to manage codespaces paid for by the organization. For more information, see [Choosing who owns and pays for codespaces in your organization](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/choosing-who-owns-and-pays-for-codespaces-in-your-organization#about-ownership-of-codespaces) and [GitHub’s plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans).
## In this article
  * [Overview](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-idle-timeout-period#overview)
  * [Adding a policy to set a maximum idle timeout period](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-idle-timeout-period#adding-a-policy-to-set-a-maximum-idle-timeout-period)
  * [Editing a policy](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-idle-timeout-period#editing-a-policy)
  * [Deleting a policy](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-idle-timeout-period#deleting-a-policy)


## [Overview](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-idle-timeout-period#overview)
By default, codespaces time out after 30 minutes of inactivity. When a codespace times out it is stopped and will no longer incur charges for compute usage.
The personal settings of a GitHub user allow them to define their own timeout period for codespaces they create. This may be longer than the default 30-minute period. For more information, see [Setting your timeout period for GitHub Codespaces](https://docs.github.com/en/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces).
As an organization owner, you may want to configure constraints on the maximum idle timeout period for codespaces created for repositories owned by your organization. This can help you to limit costs associated with codespaces that are left to timeout after long periods of inactivity. You can set a maximum timeout for the codespaces for all repositories owned by your organization, or for the codespaces of specific repositories.
Maximum idle timeout constraints only apply to codespaces that are owned by your organization.
For more information about pricing for GitHub Codespaces compute usage, see [About billing for GitHub Codespaces](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#codespaces-pricing).
### [Inactivity defined](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-idle-timeout-period#inactivity-defined)
In the context of the Codespaces idle timeout, inactivity is defined as the absence of activity indicative of a user's presence. Personal interaction with a codespace, such as typing or using the mouse, resets the idle timeout period. Terminal activity, either input or output, also resets the idle timeout period. For example, if you publish a web app on a port from a codespace and page requests generate output in a terminal on the codespace, then each time terminal output occurs the timeout will be reset. However, if you share a port, and then don't interact with the codespace, and no terminal output is generated, the codespace will time out after the configured period.
### [Behavior when you set a maximum idle timeout constraint](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-idle-timeout-period#behavior-when-you-set-a-maximum-idle-timeout-constraint)
If someone sets the default idle timeout to 90 minutes in their personal settings and they then start a codespace for a repository that has a maximum idle timeout constraint of 60 minutes, the codespace will time out after 60 minutes of inactivity. When codespace creation completes, a message explaining this will be displayed:
> Idle timeout for this codespace is set to 60 minutes in compliance with your organization’s policy.
### [Setting organization-wide and repository-specific policies](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-idle-timeout-period#setting-organization-wide-and-repository-specific-policies)
When you create a policy, you choose whether it applies to all repositories in your organization, or only to specified repositories. If you create an organization-wide policy with a timeout constraint, then the timeout constraints in any policies that are targeted at specific repositories must fall within the restriction configured for the entire organization. The shortest timeout period - in an organization-wide policy, a policy targeted at specified repositories, or in someone's personal settings - is applied.
If you add an organization-wide policy with a timeout constraint, you should set the timeout to the longest acceptable period. You can then add separate policies that set the maximum timeout to a shorter period for specific repositories in your organization.
Codespaces policies only apply to codespaces that your organizations pays for. If someone creates a codespace for a repository in your organization at their own expense, then the codespace will not be bound by these policies. For more information, see [Choosing who owns and pays for codespaces in your organization](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/choosing-who-owns-and-pays-for-codespaces-in-your-organization).
## [Adding a policy to set a maximum idle timeout period](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-idle-timeout-period#adding-a-policy-to-set-a-maximum-idle-timeout-period)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the "Code, planning, and automation" section of the sidebar, select **Policies**.
  4. On the "Codespaces policies" page, click **Create Policy**.
  5. Enter a name for your new policy.
  6. Click **Add constraint** and choose **Maximum idle timeout**.
  7. Click 
  8. Enter the maximum number of minutes codespaces can remain inactive before they time out, then click **Save**.
![Screenshot of a dropdown with a field labeled "Maximum value" set to 60 minutes. To the right of the field is a "Save" button.](https://docs.github.com/assets/cb-21708/images/help/codespaces/maximum-minutes-timeout.png)
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
     * [Restricting the retention period for codespaces](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-retention-period-for-codespaces)
  11. After you've finished adding constraints to your policy, click **Save**.


The policy will be applied to all new codespaces that are billable to your organization. The timeout constraint is also applied to existing codespaces the next time they are started.
## [Editing a policy](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-idle-timeout-period#editing-a-policy)
You can edit an existing policy. For example, you may want to add or remove constraints to or from a policy.
  1. Display the "Codespaces policies" page. For more information, see [Adding a policy to set a maximum idle timeout period](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-idle-timeout-period#adding-a-policy-to-set-a-maximum-idle-timeout-period).
  2. Click the name of the policy you want to edit.
  3. Beside the "Maximum idle timeout" constraint, click 
  4. Make the required changes then click **Save**.


## [Deleting a policy](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-idle-timeout-period#deleting-a-policy)
  1. Display the "Codespaces policies" page. For more information, see [Adding a policy to set a maximum idle timeout period](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-idle-timeout-period#adding-a-policy-to-set-a-maximum-idle-timeout-period).
  2. Click 
![Screenshot of a policy with the delete button \(a trash can icon\) highlighted with a dark orange outline.](https://docs.github.com/assets/cb-9797/images/help/codespaces/policy-delete.png)


