  * [Codespaces](https://docs.github.com/en/codespaces "Codespaces")/
  * [Prebuilding your codespaces](https://docs.github.com/en/codespaces/prebuilding-your-codespaces "Prebuilding your codespaces")/
  * [Configure prebuilds](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/configuring-prebuilds "Configure prebuilds")


# Configuring prebuilds
You can configure your project to prebuild a codespace automatically each time you push a change to your repository.
## Who can use this feature?
People with admin access to a repository can configure prebuilds for the repository.
Repository-level settings for GitHub Codespaces are available for all repositories owned by personal accounts.   
  

For repositories owned by organizations, repository-level settings for GitHub Codespaces are available for organizations on GitHub Team and GitHub Enterprise plans. To access the settings, the organization or its parent enterprise must have added a payment method and set a spending limit for GitHub Codespaces. For more information, see [Choosing who owns and pays for codespaces in your organization](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/choosing-who-owns-and-pays-for-codespaces-in-your-organization) and [GitHub’s plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans).
## In this article
  * [Prerequisites](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/configuring-prebuilds#prerequisites)
  * [Configuring prebuilds](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/configuring-prebuilds#configuring-prebuilds)
  * [Configuring environment variables](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/configuring-prebuilds#configuring-environment-variables)
  * [Configuring time-consuming tasks to be included in the prebuild](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/configuring-prebuilds#configuring-time-consuming-tasks-to-be-included-in-the-prebuild)
  * [Further reading](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/configuring-prebuilds#further-reading)


You can set up a prebuild configuration for the combination of a specific branch of your repository with a specific dev container configuration file.
Any branches created from a prebuild-enabled parent branch will typically also get prebuilds for the same dev container configuration. This is because prebuilds for child branches that use the same dev container configuration as the parent branch are, for the most part, identical, so developers can benefit from faster codespace creation times on those branches also. See [Introduction to dev containers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers).
Typically, when you configure prebuilds for a branch, prebuilds will be available for multiple machine types. However, if your repository is greater than 32 GB, prebuilds won't be available for 2-core and 4-core machine types, since the storage these provide is limited to 32 GB.
## [Prerequisites](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/configuring-prebuilds#prerequisites)
Prebuilds are created using GitHub Actions. As a result, GitHub Actions must be enabled for the repository for which you are configuring prebuilds. See [Managing GitHub Actions settings for a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository).
You can set up prebuilds in any repository owned by a personal account. The prebuild will consume storage space that will either incur a billable charge or, for repositories owned by your personal account, will use some of your monthly included storage.
If you create prebuilds for a forked repository, the storage cost of those prebuilds is subtracted from your monthly included storage, while available. If you have used all of your included storage, and you have set up billing, your personal account will be billed. This is true even when the codespaces you create for a fork are paid for by the organization that owns the parent repository. See [About billing for GitHub Codespaces](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#how-billing-is-handled-for-forked-repositories).
For repositories owned by an organization, you can set up prebuilds if the organization is on a GitHub Team or GitHub Enterprise plan. Additionally, you must have added a payment method and set a spending limit for GitHub Codespaces on the organization account or its parent enterprise. See [Managing the spending limit for GitHub Codespaces](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-codespaces/managing-the-spending-limit-for-github-codespaces#managing-the-github-codespaces-spending-limit-for-your-organization-account) and [GitHub’s plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans).
## [Configuring prebuilds](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/configuring-prebuilds#configuring-prebuilds)
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Code & automation" section of the side bar, click 
  4. In the "Prebuild configuration" section of the page, click **Set up prebuild**.
![Screenshot of the "Prebuild configuration" section of the "Codespaces" settings page, showing the "Set up prebuilds" button.](https://docs.github.com/assets/cb-48427/images/help/codespaces/prebuilds-set-up.png)
  5. Choose the branch for which you want to set up prebuilds.
![Screenshot of the "Configuration" settings for a prebuild with a dropdown menu listing branches to select. The "main" branch is currently selected.](https://docs.github.com/assets/cb-68610/images/help/codespaces/prebuilds-choose-branch.png)
Any branches created from a prebuild-enabled base branch will typically also get prebuilds for the same dev container configuration. For example, if you enable prebuilds for a dev container configuration file on the default branch of the repository, branches based on the default branch will, in most cases, also get prebuilds for the same dev container configuration.
  6. Optionally, in the **Configuration file** dropdown menu that's displayed, choose the `devcontainer.json` configuration file that you want to use for your prebuilds. See [Introduction to dev containers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers#devcontainerjson).
![Screenshot of the configuration file dropdown menu. Four configuration files are listed, with ".devcontainer/devcontainer.json" currently selected.](https://docs.github.com/assets/cb-49883/images/help/codespaces/prebuilds-choose-configfile.png)
  7. Choose how you want to automatically trigger prebuild updates.
     * **Every push** (the default setting) - With this setting, prebuilds will be updated on every push made to the given branch. This will ensure that codespaces generated from a prebuild always contain the latest codespace configuration, including any recently added or updated dependencies.
     * **On configuration change** - With this setting, prebuilds will be updated every time any of the following files is changed:
       * `.devcontainer/devcontainer.json`
Prebuild updates are not triggered by changes to `devcontainer.json` files within subdirectories of `.devcontainer`.
       * The Dockerfile referenced in the `build.dockerfile` property of the `.devcontainer/devcontainer.json` file.
This setting ensures that changes to the dev container configuration files for the repository are used when a codespace is generated from a prebuild. The GitHub Actions workflow that updates the prebuilds will run less often, so this option will use fewer GitHub Actions minutes. However, this option will not guarantee that codespaces always include recently added or updated dependencies, so these may have to be added or updated manually after a codespace has been created.
     * **Scheduled** - With this setting, you can have your prebuilds updated on a custom schedule that's defined by you. This can reduce consumption of GitHub Actions minutes, however, with this option, codespaces may be created that do not use the latest dev container configuration changes.
![Screenshot of the "Prebuild triggers" settings. The "Scheduled" option is selected and set to "Every day" at "1pm" and "3:30pm."](https://docs.github.com/assets/cb-65096/images/help/codespaces/prebuilds-triggers.png)
  8. Optionally, select **Reduce prebuild available to only specific regions** to create prebuilds only in specified regions. Select the regions in which you want prebuilds to be available.
By default, prebuilds are created in all of the available regions, incurring storage charges per prebuild.
![Screenshot of the "Region availability" settings. "Reduce prebuild available to only specific regions" is selected with two regions selected.](https://docs.github.com/assets/cb-46139/images/help/codespaces/prebuilds-regions.png)
     * The prebuild in each region incurs individual storage charges. You should, therefore, only enable prebuilds for regions in which you know they'll be used. See [About billing for GitHub Codespaces](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#about-billing-for-codespaces-prebuilds).
     * Developers can set their default region for GitHub Codespaces, which can allow you to enable prebuilds for fewer regions. See [Setting your default region for GitHub Codespaces](https://docs.github.com/en/codespaces/setting-your-user-preferences/setting-your-default-region-for-github-codespaces).
  9. Optionally, under **Template history** , set the number of prebuild versions to be retained. You can input any number between 1 and 5. The default number of saved versions is 2, which means that only the latest prebuild and the previous version are saved.
![Screenshot of the "Template history" setting. It is set to 2 versions.](https://docs.github.com/assets/cb-24261/images/help/codespaces/prebuilds-template-history-setting.png)
Depending on your prebuild trigger settings, your prebuild could change with each push or on each dev container configuration change. Retaining older versions of prebuilds enables you to create a prebuild from an older commit with a different dev container configuration than the current prebuild. This setting allows you to set the number of retained versions to a level that is appropriate for your needs.
If you set the number of prebuild versions to save to 1, GitHub Codespaces will only save the latest version of the prebuild and will delete the older version each time the template is updated. This means you will not get a prebuilt codespace if you go back to an older dev container configuration.
There is a storage cost associated with each prebuild version that's retained. For example, if you are generating prebuilds in 4 regions and retaining 2 versions, you will be charged for storage of up to 8 prebuilds. See [About billing for GitHub Codespaces](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#codespaces-pricing).
  10. Optionally, add users or teams to notify when the prebuild workflow run fails for this configuration. You can begin typing a username, team name, or full name, then click the name once it appears to add them to the list. The users or teams you add will receive an email when prebuild failures occur, containing a link to the workflow run logs to help with further investigation.
![Screenshot of the "Failure notifications" setting. The team named "octocat-team" has been added.](https://docs.github.com/assets/cb-34068/images/help/codespaces/prebuilds-failure-notification-setting.png)
People will only receive notifications of failed prebuilds if they have enabled notifications for failed Actions workflows in their personal settings. See [Configuring notifications](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications#github-actions-notification-options).
  11. Optionally, at the bottom of the page, click **Show advanced options**.
![Screenshot of the bottom of the prebuilds configuration page. The link "Show advanced options" is highlighted with a dark orange outline.](https://docs.github.com/assets/cb-45746/images/help/codespaces/show-advanced-options.png)
In the "Advanced options" section, if you select **Disable prebuild optimization** , codespaces will be created without a prebuild if the latest prebuild workflow has failed or is currently running. See [Troubleshooting prebuilds](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-prebuilds#preventing-out-of-date-prebuilds-being-used).
  12. Click **Create**.
If the dev container configuration for the repository specifies permissions for accessing other repositories, you will be shown an authorization page. For more information on how this is specified in the `devcontainer.json` file, see [Managing access to other repositories within your codespace](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-repository-access-for-your-codespaces).
Click 
![Screenshot of an authorization page for a prebuild configuration. Three permissions are listed in this request.](https://docs.github.com/assets/cb-95634/images/help/codespaces/prebuild-authorization-page.png)
Click **Authorize and continue** to grant these permissions for creation of prebuilds. Alternatively, you can click **Continue without authorizing** but, if you do so, codespaces created from the resulting prebuilds may not work properly.
Users who create codespaces using this prebuild will also be asked to grant these permissions.


After you create a prebuild configuration it is listed on the GitHub Codespaces page of your repository settings. A GitHub Actions workflow is queued and then run to create prebuilds in the regions you specified, based on the branch and dev container configuration file you selected.
![Screenshot of the list of prebuild configurations. One prebuild is listed, labeled "Currently running." To the right of it is a "See output" button.](https://docs.github.com/assets/cb-32132/images/help/codespaces/prebuild-configs-list.png)
For information about editing and deleting prebuild configurations, see [Managing prebuilds](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/managing-prebuilds).
## [Configuring environment variables](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/configuring-prebuilds#configuring-environment-variables)
To allow the prebuild process to access environment variables required to create your development environment, you can set these either as Codespaces repository secrets or as Codespaces organization secrets. Secrets that you create in this way will be accessible by anyone who creates a codespace from this repository. See [Managing development environment secrets for your repository or organization](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/managing-development-environment-secrets-for-your-repository-or-organization#adding-secrets-for-a-repository).
Prebuilds cannot use any user-level secrets while building your environment, because these are not available until after the codespace has been created.
## [Configuring time-consuming tasks to be included in the prebuild](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/configuring-prebuilds#configuring-time-consuming-tasks-to-be-included-in-the-prebuild)
You can use the `onCreateCommand` and `updateContentCommand` commands in your `devcontainer.json` to include time-consuming processes as part of the prebuild creation. See the Visual Studio Code documentation, [devcontainer.json reference](https://code.visualstudio.com/docs/remote/devcontainerjson-reference#_lifecycle-scripts).
`onCreateCommand` is run only once, when the prebuild is created, whereas `updateContentCommand` is run at creation of the prebuild and at subsequent updates to it. Incremental builds should be included in `updateContentCommand` since they represent the source of your project and need to be included for every prebuild update.
## [Further reading](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/configuring-prebuilds#further-reading)
  * [Allowing a prebuild to access other repositories](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/allowing-a-prebuild-to-access-other-repositories)
  * [Troubleshooting prebuilds](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-prebuilds)


