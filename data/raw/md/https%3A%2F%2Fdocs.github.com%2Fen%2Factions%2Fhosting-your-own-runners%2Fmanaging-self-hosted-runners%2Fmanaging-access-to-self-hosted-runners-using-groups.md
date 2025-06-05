  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners "Self-hosted runners")/
  * [Manage self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners "Manage self-hosted runners")/
  * [Manage access with runner groups](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups "Manage access with runner groups")


# Managing access to self-hosted runners using groups
You can use policies to limit access to self-hosted runners that have been added to an organization.
## Who can use this feature?
Enterprise accounts, organizations owned by enterprise accounts, and organizations using GitHub Team or GitHub Free plans can create and manage additional runner groups using self-hosted runners.  
  

## In this article
  * [About runner groups](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups#about-runner-groups)
  * [Creating a self-hosted runner group for an organization](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups#creating-a-self-hosted-runner-group-for-an-organization)
  * [Changing which repositories can access a runner group](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups#changing-which-repositories-can-access-a-runner-group)
  * [Changing the name of a runner group](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups#changing-the-name-of-a-runner-group)
  * [Automatically adding a self-hosted runner to a group](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups#automatically-adding-a-self-hosted-runner-to-a-group)
  * [Moving a self-hosted runner to a group](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups#moving-a-self-hosted-runner-to-a-group)
  * [Removing a self-hosted runner group](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups#removing-a-self-hosted-runner-group)


## [About runner groups](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups#about-runner-groups)
To control access to runners at the organization level, organizations using the GitHub Team plan can use runner groups. Runner groups are used to collect sets of runners and create a security boundary around them.
When you grant access to a runner group, you can see the runner group listed in the organization's runner settings. Optionally, you can assign additional granular repository access policies to the runner group.
When new runners are created, they are automatically assigned to the default group unless otherwise specified. Runners can only be in one group at a time. You can move runners from one runner group to another. For more information, see [Moving a runner to a group](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups#moving-a-runner-to-a-group).
For information on how to route jobs to runners in a specific group, see [Choosing the runner for a job](https://docs.github.com/en/actions/using-jobs/choosing-the-runner-for-a-job#choosing-runners-in-a-group).
## [Creating a self-hosted runner group for an organization](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups#creating-a-self-hosted-runner-group-for-an-organization)
We recommend that you only use self-hosted runners with private repositories. This is because forks of your public repository can potentially run dangerous code on your self-hosted runner machine by creating a pull request that executes the code in a workflow.
For more information, see [Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions).
When creating a runner group, you must choose a policy that defines which repositories have access to the runner group. To change which repositories and workflows can access the runner group, organization owners can set a policy for the organization. For more information, see [Enforcing policies for GitHub Actions in your enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise#disabling-repository-level-self-hosted-runners).
All organizations have a single default runner group. Organization owners using the GitHub Team plan can create additional organization-level runner groups.
If no group is specified during the registration process, runners are automatically added to the default group. You can later move the runner from the default group to a custom group. For more information, see [Moving a runner to a group](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups#moving-a-runner-to-a-group).
For information about how to create a runner group with the REST API, see [REST API endpoints for GitHub Actions](https://docs.github.com/en/rest/actions#self-hosted-runner-groups).
  1. On GitHub, navigate to the main page of the organization.
  2. Under your organization name, click **Settings**.
![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](https://docs.github.com/assets/cb-49309/images/help/discussions/org-settings-global-nav-update.png)
  3. In the left sidebar, click **Runner groups**.
  4. In the "Runner groups" section, click **New runner group**.
  5. Enter a name for your runner group.
  6. Assign a policy for repository access.
You can configure a runner group to be accessible to a specific list of repositories, or to all repositories in the organization. By default, only private repositories can access runners in a runner group, but you can override this. This setting can't be overridden if configuring an organization's runner group that was shared by an enterprise.
  7. Click **Create group** to create the group and apply the policy.


## [Changing which repositories can access a runner group](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups#changing-which-repositories-can-access-a-runner-group)
We recommend that you only use self-hosted runners with private repositories. This is because forks of your public repository can potentially run dangerous code on your self-hosted runner machine by creating a pull request that executes the code in a workflow.
For more information, see [Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions).
For runner groups in an organization, you can change what repositories in the organization can access a runner group.
  1. Navigate to the main page of the organization where your runner groups are located.
  2. Click 
  3. In the left sidebar, click **Runner groups**.
  4. In the list of groups, click the runner group you'd like to configure.
  5. Under "Repository access," use the dropdown menu to click **Selected repositories**.
    1. To the right of the dropdown menu, click 
    2. In the popup, use the checkboxes to select repositories that can access this runner group.
  6. Click **Save group**.


## [Changing the name of a runner group](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups#changing-the-name-of-a-runner-group)
  1. Navigate to the main page of the organization where your runner groups are located.
  2. Click 
  3. In the left sidebar, click **Runner groups**.
  4. In the list of groups, click the runner group you'd like to configure.
  5. Enter the new runner group name in the text field under "Group name."
  6. Click **Save**.


## [Automatically adding a self-hosted runner to a group](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups#automatically-adding-a-self-hosted-runner-to-a-group)
You can use the configuration script to automatically add a new runner to a group. For example, this command registers a new runner and uses the `--runnergroup` parameter to add it to a group named `rg-runnergroup`.
```
./config.sh --url $org_or_enterprise_url --token $token --runnergroup rg-runnergroup

```

The command will fail if the runner group doesn't exist:
```
Could not find any self-hosted runner group named "rg-runnergroup".

```

## [Moving a self-hosted runner to a group](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups#moving-a-self-hosted-runner-to-a-group)
If you don't specify a runner group during the registration process, your new runners are automatically assigned to the default group, and can then be moved to another group.
  1. On GitHub, navigate to the main page of the organization.
  2. Under your organization name, click **Settings**.
![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](https://docs.github.com/assets/cb-49309/images/help/discussions/org-settings-global-nav-update.png)
  3. In the left sidebar, click **Runners**.
  4. In the "Runners" list, click the runner that you want to configure.
  5. Select the **Runner group** drop-down.
  6. In "Move runner to group", choose a destination group for the runner.


## [Removing a self-hosted runner group](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups#removing-a-self-hosted-runner-group)
In order to remove a runner group, you must first move or remove all of the runners from the group.
  1. Navigate to the main page of the organization where your runner groups are located.
  2. Click 
  3. In the left sidebar, click **Runner groups**.
  4. In the list of groups, to the right of the group you want to delete, click 
  5. To remove the group, click **Remove group**.
  6. Review the confirmation prompts, and click **Remove this runner group**.


