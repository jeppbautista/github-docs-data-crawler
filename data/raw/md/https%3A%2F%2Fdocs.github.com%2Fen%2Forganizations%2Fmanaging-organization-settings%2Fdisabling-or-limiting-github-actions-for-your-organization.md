  * [Organizations](https://docs.github.com/en/organizations "Organizations")/
  * [Manage organization settings](https://docs.github.com/en/organizations/managing-organization-settings "Manage organization settings")/
  * [Disable or limit actions](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization "Disable or limit actions")


# Disabling or limiting GitHub Actions for your organization
You can enable, disable, and limit GitHub Actions for an organization.
## Who can use this feature?
Organization owners can enable, disable, and limit GitHub Actions for an organization.
## In this article
  * [About GitHub Actions permissions for your organization](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#about-github-actions-permissions-for-your-organization)
  * [Managing GitHub Actions permissions for your organization](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#managing-github-actions-permissions-for-your-organization)
  * [Limiting the use of self-hosted runners](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#limiting-the-use-of-self-hosted-runners)
  * [Configuring required approval for workflows from public forks](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#configuring-required-approval-for-workflows-from-public-forks)
  * [Enabling workflows for private repository forks](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#enabling-workflows-for-private-repository-forks)
  * [Setting the permissions of the GITHUB_TOKEN for your organization](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#setting-the-permissions-of-the-github_token-for-your-organization)
  * [Managing GitHub Actions cache storage for your organization](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#managing-github-actions-cache-storage-for-your-organization)


## [About GitHub Actions permissions for your organization](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#about-github-actions-permissions-for-your-organization)
By default, GitHub Actions is enabled on all repositories and organizations. You can choose to disable GitHub Actions or limit it to actions and reusable workflows in your organization. For more information about GitHub Actions, see [Writing workflows](https://docs.github.com/en/actions/learn-github-actions).
You can enable GitHub Actions for all repositories in your organization. When you enable GitHub Actions, workflows are able to run actions and reusable workflows located within your repository and any other public repository. You can disable GitHub Actions for all repositories in your organization. When you disable GitHub Actions, no workflows run in your repository.
Alternatively, you can enable GitHub Actions for all repositories in your organization but limit the actions and reusable workflows a workflow can run.
## [Managing GitHub Actions permissions for your organization](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#managing-github-actions-permissions-for-your-organization)
You can choose to disable GitHub Actions for all repositories in your organization, or only allow specific repositories. You can also limit the use of public actions and reusable workflows, so that people can only use local actions and reusable workflows that exist in your organization.
You might not be able to manage these settings if your organization is managed by an enterprise that has overriding policy. For more information, see [Enforcing policies for GitHub Actions in your enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise).
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the left sidebar, click **General**.
  4. Under "Policies", select an option.
If you choose **Allow _OWNER_ , and select non-_OWNER_ , actions and reusable workflows**, actions and reusable workflows within your organization are allowed, and there are additional options for allowing other specific actions and reusable workflows. For more information, see [Allowing select actions and reusable workflows to run](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#allowing-select-actions-and-reusable-workflows-to-run).
When you allow actions and reusable workflows from only in your organization, the policy blocks all access to actions authored by GitHub. For example, the [`actions/checkout`](https://github.com/actions/checkout) action would not be accessible.
  5. Click **Save**.


### [Allowing select actions and reusable workflows to run](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#allowing-select-actions-and-reusable-workflows-to-run)
When you choose **Allow _OWNER_ , and select non-_OWNER_ , actions and reusable workflows**, local actions and reusable workflows are allowed, and there are additional options for allowing other specific actions and reusable workflows:
You might not be able to manage these settings if your organization has an overriding policy or is managed by an enterprise that has overriding policy. For more information, see [Disabling or limiting GitHub Actions for your organization](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization) or [Enforcing policies for GitHub Actions in your enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise).
  * **Allow actions created by GitHub:** You can allow all actions created by GitHub to be used by workflows. Actions created by GitHub are located in the `actions` and `github` organizations. For more information, see the [`actions`](https://github.com/actions) and [`github`](https://github.com/github) organizations.
  * **Allow Marketplace actions by verified creators:** You can allow all GitHub Marketplace actions created by verified creators to be used by workflows. When GitHub has verified the creator of the action as a partner organization, the 
  * **Allow specified actions and reusable workflows:** You can restrict workflows to use actions and reusable workflows in specific organizations and repositories. Specified actions cannot be set to more than 1000.
To restrict access to specific tags or commit SHAs of an action or reusable workflow, use the same syntax used in the workflow to select the action or reusable workflow.
    * For an action, the syntax is `OWNER/REPOSITORY@TAG-OR-SHA`. For example, use `actions/javascript-action@v1.0.1` to select a tag or `actions/javascript-action@a824008085750b8e136effc585c3cd6082bd575f` to select a SHA. For more information, see [Using pre-written building blocks in your workflow](https://docs.github.com/en/actions/learn-github-actions/finding-and-customizing-actions#using-release-management-for-your-custom-actions).
    * For a reusable workflow, the syntax is `OWNER/REPOSITORY/PATH/FILENAME@TAG-OR-SHA`. For example, `octo-org/another-repo/.github/workflows/workflow.yml@v1`. For more information, see [Reusing workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows#calling-a-reusable-workflow).
You can use the `*` wildcard character to match patterns. For example, to allow all actions and reusable workflows in organizations that start with `space-org`, you can specify `space-org*/*`. To allow all actions and reusable workflows in repositories that start with octocat, you can use `*/octocat**@*`. For more information about using the `*` wildcard, see [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#filter-pattern-cheat-sheet).
Use `,` to separate patterns. For example, to allow `octocat` and `octokit`, you can specify `octocat/*, octokit/*`.
For GitHub Free, GitHub Pro, GitHub Free for organizations, or GitHub Team plans, the **Allow specified actions and reusable workflows** option is only available in public repositories.


This procedure demonstrates how to add specific actions and reusable workflows to the allow list.
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the left sidebar, click **General**.
  4. Under "Policies", select **Allow _OWNER_ , and select non-_OWNER_ , actions and reusable workflows** and add your required actions and reusable workflows to the list.
  5. Click **Save**.


## [Limiting the use of self-hosted runners](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#limiting-the-use-of-self-hosted-runners)
There is no guarantee that self-hosted runners for GitHub will be hosted on ephemeral, clean virtual machines. As a result, they may be compromised by untrusted code in a workflow.
Similarly, anyone who can fork the repository and open a pull request (generally those with read access to the repository) can compromise the self-hosted runner environment, including gaining access to secrets and the `GITHUB_TOKEN` which, depending on its settings, can grant write access to the repository. Although workflows can control access to environment secrets by using environments and required reviews, these workflows are not run in an isolated environment and are still susceptible to the same risks when run on a self-hosted runner.
For these and other reasons, you may decide to prevent people creating self-hosted runners at the repository level.
If a repository already has self-hosted runners when you disable their use, these will be listed with the status "Disabled" and they will not be assigned any new workflow jobs.
![Screenshot of the "Runners" list showing a self-hosted runner with the status "Disabled."](https://docs.github.com/assets/cb-88252/images/help/actions/actions-runners-disabled.png)
When creation of repository-level self-hosted runners is disabled, workflows can still access self-hosted runners at the enterprise or organization level.
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the left sidebar, click **General**.
  4. Under "Runners," use the dropdown menu to choose your preferred setting: 
     * **All repositories** - self-hosted runners can be used for any repository in your organization.
     * **Selected repositories** - self-hosted runners can only be used for the repositories you select.
     * **Disabled** - self-hosted runners cannot be created at the repository level.
  5. If you choose **Selected repositories** : 
    1. Click 
    2. Select the check boxes for the repositories for which you want to allow self-hosted runners.
    3. Click **Select repositories**.


## [Configuring required approval for workflows from public forks](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#configuring-required-approval-for-workflows-from-public-forks)
Anyone can fork a public repository, and then submit a pull request that proposes changes to the repository's GitHub Actions workflows. Although workflows from forks do not have access to sensitive data such as secrets, they can be an annoyance for maintainers if they are modified for abusive purposes.
To help prevent this, workflows on pull requests to public repositories from some outside contributors will not run automatically, and might need to be approved first. Depending on the "Approval for running fork pull request workflows from contributors" setting, workflows on pull requests to public repositories will not run automatically and may need approval if:
  * The pull request is **created by** a user that requires approvals based on the selected policy.
  * The pull request event is **triggered by** a user that requires approvals based on the selected policy.


By default, all first-time contributors require approval to run workflows.
Workflows triggered by `pull_request_target` events are run in the context of the base branch. Since the base branch is considered trusted, workflows triggered by these events will always run, regardless of approval settings. For more information about the `pull_request_target` event, see [Events that trigger workflows](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#pull_request_target).
These workflow approval policies are intended to restrict the set of users that can execute workflows in GitHub Actions runners that could lead to unexpected resource and compute consumption when using GitHub-hosted runners. If you are using self-hosted runners, potentially malicious user-controlled workflow code will execute automatically if the user is allowed to bypass approval in the set approval policy or if the pull request is approved. You must consider the risk of executing this code in your infrastructure and should review and follow the self-hosted runner security recommendations regardless of the approval settings utilized. See [Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions#hardening-for-self-hosted-runners).
You can configure this behavior for an organization using the procedure below. Modifying this setting overrides the configuration set at the enterprise level.
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the left sidebar, click **General**.
  4. Under **Approval for running fork pull request workflows from contributors** , choose which subset of users will require approval before running workflows on their pull requests. Both the pull request author and the actor of the pull request event triggering the workflow will be checked to determine if approval is required. If approval is required, a user with write access to the repository must approve the pull request workflow to be run. See [Approving workflow runs from public forks](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/approving-workflow-runs-from-public-forks).
When requiring approvals only for first-time contributors (the first two settings), a user that has had any commit or pull request merged into the repository will not require approval. A malicious user could meet this requirement by getting a simple typo or other innocuous change accepted by a maintainer, either as part of a pull request they have authored or as part of another user's pull request.
     * **Require approval for first-time contributors who are new to GitHub**. Only users who are both new on GitHub and who have never had a commit or pull request merged into this repository will require approval to run workflows.
     * **Require approval for first-time contributors**. Only users who have never had a commit or pull request merged into this repository will require approval to run workflows.
     * **Require approval for all external contributors** All users that are not a member or owner of this repository and not a member of the organization will require approval to run workflows.
  5. Click **Save** to apply the settings.


For more information about approving workflow runs that this policy applies to, see [Approving workflow runs from public forks](https://docs.github.com/en/actions/managing-workflow-runs/approving-workflow-runs-from-public-forks).
## [Enabling workflows for private repository forks](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#enabling-workflows-for-private-repository-forks)
If you rely on using forks of your private repositories, you can configure policies that control how users can run workflows on `pull_request` events. Available to private repositories only, you can configure these policy settings for organizations or repositories.
If a policy is disabled for an organization, it cannot be enabled for repositories. If an organization enables a policy, the policy can be disabled for individual repositories.
  * **Run workflows from fork pull requests** - Allows users to run workflows from fork pull requests, using a `GITHUB_TOKEN` with read-only permission, and with no access to secrets.
  * **Send write tokens to workflows from pull requests** - Allows pull requests from forks to use a `GITHUB_TOKEN` with write permission.
  * **Send secrets to workflows from pull requests** - Makes all secrets available to the pull request.
  * **Require approval for fork pull request workflows** - Workflow runs on pull requests from collaborators without write permission will require approval from someone with write permission before they will run.


### [Configuring the private fork policy for an organization](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#configuring-the-private-fork-policy-for-an-organization)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the left sidebar, click **General**.
  4. Under **Fork pull request workflows** , select your options.
  5. Click **Save** to apply the settings.


## [Setting the permissions of the `GITHUB_TOKEN` for your organization](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#setting-the-permissions-of-the-github_token-for-your-organization)
You can set the default permissions granted to the `GITHUB_TOKEN`. For more information about the `GITHUB_TOKEN`, see [Automatic token authentication](https://docs.github.com/en/actions/security-guides/automatic-token-authentication). You can choose a restricted set of permissions as the default, or apply permissive settings.
You can set the default permissions for the `GITHUB_TOKEN` in the settings for your organization or your repositories. If you select a restrictive option as the default in your organization settings, the same option is selected in the settings for repositories within your organization, and the permissive option is disabled. If your organization belongs to a GitHub Enterprise account and a more restrictive default has been selected in the enterprise settings, you won't be able to select the more permissive default in your organization settings.
Anyone with write access to a repository can modify the permissions granted to the `GITHUB_TOKEN`, adding or removing access as required, by editing the `permissions` key in the workflow file. For more information, see [`permissions`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#permissions).
### [Configuring the default `GITHUB_TOKEN` permissions](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#configuring-the-default-github_token-permissions)
By default, when you create a new organization, `GITHUB_TOKEN` only has read access for the `contents` and `packages` scopes.
  1. In the top right corner of GitHub, click your profile photo, then click **Your profile**.
![Screenshot of the dropdown menu under @octocat's profile picture. "Your profile" is outlined in dark orange.](https://docs.github.com/assets/cb-13593/images/help/profile/profile-button-avatar-menu-global-nav-update.png)
  2. In the upper-right corner of GitHub, select your profile photo, then click 
  3. Next to the organization, click **Settings**.
  4. In the left sidebar, click **General**.
  5. Under "Workflow permissions", choose whether you want the `GITHUB_TOKEN` to have read and write access for all permissions (the permissive setting), or just read access for the `contents` and `packages` permissions (the restricted setting).
  6. Click **Save** to apply the settings.


### [Preventing GitHub Actions from creating or approving pull requests](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#preventing-github-actions-from-creating-or-approving-pull-requests)
You can choose to allow or prevent GitHub Actions workflows from creating or approving pull requests.
By default, when you create a new organization, workflows are not allowed to create or approve pull requests.
  1. In the top right corner of GitHub, click your profile photo, then click **Your profile**.
![Screenshot of the dropdown menu under @octocat's profile picture. "Your profile" is outlined in dark orange.](https://docs.github.com/assets/cb-13593/images/help/profile/profile-button-avatar-menu-global-nav-update.png)
  2. In the upper-right corner of GitHub, select your profile photo, then click 
  3. Next to the organization, click **Settings**.
  4. In the left sidebar, click **General**.
  5. Under "Workflow permissions", use the **Allow GitHub Actions to create and approve pull requests** setting to configure whether `GITHUB_TOKEN` can create and approve pull requests.
  6. Click **Save** to apply the settings.


## [Managing GitHub Actions cache storage for your organization](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#managing-github-actions-cache-storage-for-your-organization)
Organization administrators can view GitHub Actions cache storage for all repositories in the organization.
### [Viewing GitHub Actions cache storage by repository](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#viewing-github-actions-cache-storage-by-repository)
For each repository in your organization, you can see how much cache storage a repository is using, the number of active caches, and if a repository is near the total cache size limit. For more information about the cache usage and eviction process, see [Caching dependencies to speed up workflows](https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows#usage-limits-and-eviction-policy).
  1. In the top right corner of GitHub, click your profile photo, then click **Your profile**.
![Screenshot of the dropdown menu under @octocat's profile picture. "Your profile" is outlined in dark orange.](https://docs.github.com/assets/cb-13593/images/help/profile/profile-button-avatar-menu-global-nav-update.png)
  2. In the upper-right corner of GitHub, select your profile photo, then click 
  3. Next to the organization, click **Settings**.
  4. In the left sidebar, click **Caches**.
  5. Review the list of repositories for information about their GitHub Actions caches. You can click on a repository name to see more detail about the repository's caches.


