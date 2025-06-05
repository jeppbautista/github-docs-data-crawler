  * [Codespaces](https://docs.github.com/en/codespaces "Codespaces")/
  * [Prebuilding your codespaces](https://docs.github.com/en/codespaces/prebuilding-your-codespaces "Prebuilding your codespaces")/
  * [Manage prebuilds](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/managing-prebuilds "Manage prebuilds")


# Managing prebuilds
You can review, modify, and delete the prebuild configurations for your repository.
## Who can use this feature?
Repository-level settings for GitHub Codespaces are available for all repositories owned by personal accounts.   
  

For repositories owned by organizations, repository-level settings for GitHub Codespaces are available for organizations on GitHub Team and GitHub Enterprise plans. To access the settings, the organization or its parent enterprise must have added a payment method and set a spending limit for GitHub Codespaces. For more information, see [Choosing who owns and pays for codespaces in your organization](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/choosing-who-owns-and-pays-for-codespaces-in-your-organization) and [GitHub’s plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans).
## In this article
  * [About managing prebuilds](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/managing-prebuilds#about-managing-prebuilds)
  * [Viewing the progress of prebuilds](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/managing-prebuilds#viewing-the-progress-of-prebuilds)
  * [Editing a prebuild configuration](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/managing-prebuilds#editing-a-prebuild-configuration)
  * [Disabling a prebuild configuration](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/managing-prebuilds#disabling-a-prebuild-configuration)
  * [Deleting a prebuild configuration](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/managing-prebuilds#deleting-a-prebuild-configuration)
  * [Manually trigger prebuilds](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/managing-prebuilds#manually-trigger-prebuilds)
  * [Further reading](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/managing-prebuilds#further-reading)


## [About managing prebuilds](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/managing-prebuilds#about-managing-prebuilds)
The prebuilds that you configure for a repository are created and updated using a GitHub Actions workflow, managed by the GitHub Codespaces service.
Depending on the settings in a prebuild configuration, the workflow to update the prebuild may be triggered by these events:
  * Creating or updating the prebuild configuration
  * Pushing a commit or a pull request to a branch that's configured to have prebuilds
  * Changing any of the dev container configuration files
  * A schedule that you've defined in the prebuild configuration
  * Manually triggering the workflow


The settings in the prebuild configuration determine which events automatically trigger an update of the prebuild. See [Configuring prebuilds](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/configuring-prebuilds#configuring-prebuilds).
People with admin access to a repository can check the progress of prebuilds, edit, and delete prebuild configurations.
To locate all repositories that are hosting a prebuild configuration, you must obtain a copy of your usage report by following the steps for [Viewing your GitHub Codespaces usage](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-codespaces/viewing-your-github-codespaces-usage).
## [Viewing the progress of prebuilds](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/managing-prebuilds#viewing-the-progress-of-prebuilds)
You can view the current status of the latest workflow run for each prebuild configuration you've set up on the GitHub Codespaces page of your repository settings. For example, "Currently running" or "Last run 1 hour ago."
To see the log output for the latest prebuild workflow run, click **See output**.
![Screenshot of the "Prebuild configuration" page. Two prebuild configurations are listed. The "See output" button for one configuration is highlighted.](https://docs.github.com/assets/cb-48318/images/help/codespaces/prebuilds-see-output.png)
This displays the output of the most recent run of the workflow in the **Actions** tab.
![Screenshot of the prebuild workflow output in the "Actions" tab of GitHub.](https://docs.github.com/assets/cb-112161/images/help/codespaces/prebuilds-log-output.png)
Alternatively, to view all prebuild workflow runs associated with the specified branch, select the **View runs**.
![Screenshot of the options dropdown menu for a configuration, shown by clicking a button labeled with three dots. The "View runs" option is selected.](https://docs.github.com/assets/cb-26915/images/help/codespaces/prebuilds-view-runs.png)
This displays the workflow run history for prebuilds for the associated branch.
![Screenshot of the "Codespaces Prebuilds" list showing a run history for prebuild workflows.](https://docs.github.com/assets/cb-91872/images/help/codespaces/prebuilds-workflow-runs.png)
## [Editing a prebuild configuration](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/managing-prebuilds#editing-a-prebuild-configuration)
  1. On the Codespaces page of your repository settings, click the ellipsis to the right of the prebuild configuration you want to edit.
  2. In the dropdown menu, click **Edit**.
![Screenshot of the options dropdown menu for a configuration, displayed by clicking a button labeled with three dots. The "Edit" option is selected.](https://docs.github.com/assets/cb-27186/images/help/codespaces/prebuilds-edit.png)
  3. Make the required changes to the prebuild configuration, then click **Update**.
If the dev container configuration for the repository specifies permissions for accessing other repositories, you will be shown an authorization page. For more information on how this is specified in the `devcontainer.json` file, see [Managing access to other repositories within your codespace](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-repository-access-for-your-codespaces).
Click 
![Screenshot of an authorization page for a prebuild configuration. Three permissions are listed in this request.](https://docs.github.com/assets/cb-95634/images/help/codespaces/prebuild-authorization-page.png)
Click **Authorize and continue** to grant these permissions for creation of prebuilds. Alternatively, you can click **Continue without authorizing** but, if you do so, codespaces created from the resulting prebuilds may not work properly.
Users who create codespaces using this prebuild will also be asked to grant these permissions.


## [Disabling a prebuild configuration](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/managing-prebuilds#disabling-a-prebuild-configuration)
To pause the update of prebuilds for a configuration, you can disable workflow runs for the configuration. Disabling the workflow runs for a prebuild configuration does not delete any previously created prebuilds for that configuration and, as a result, codespaces will continue to be generated from an existing prebuild.
Disabling the workflow runs for a prebuild configuration is useful if you need to investigate prebuild creation failures.
  1. On the Codespaces page of your repository settings, click the ellipsis to the right of the prebuild configuration you want to disable.
  2. In the dropdown menu, click **Disable runs**.
![Screenshot of the prebuild configuration dropdown menu, shown by clicking a button labeled with three dots. The "Disable runs" option is selected.](https://docs.github.com/assets/cb-33546/images/help/codespaces/prebuilds-disable.png)
  3. To confirm that you want to disable this configuration, click **OK**.


## [Deleting a prebuild configuration](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/managing-prebuilds#deleting-a-prebuild-configuration)
You can find a list of the repositories that contain a prebuild by obtaining a copy of your “[usage report](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-codespaces/viewing-your-github-codespaces-usage).”
Deleting a prebuild configuration also deletes all previously created prebuilds for that configuration. As a result, shortly after you delete a configuration, prebuilds generated by that configuration will no longer be available when you create a new codespace.
After you delete a prebuild configuration, workflow runs for that configuration that have been queued or started will still run. They will be listed in the workflow run history, along with previously completed workflow runs.
  1. On the Codespaces page of your repository settings, click the ellipsis to the right of the prebuild configuration you want to delete.
  2. In the dropdown menu, click **Delete**.
![Screenshot of the prebuild configuration dropdown menu, displayed by clicking a button labeled with three dots. The "Delete" option is selected.](https://docs.github.com/assets/cb-36637/images/help/codespaces/prebuilds-delete.png)
  3. Click **OK** to confirm the deletion.


## [Manually trigger prebuilds](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/managing-prebuilds#manually-trigger-prebuilds)
It may be useful to manually trigger a workflow run for a prebuild configuration. Generally, this is only necessary if you are debugging a problem with the workflow for a prebuild configuration.
  1. On the Codespaces page of your repository settings, click the ellipsis to the right of the prebuild configuration whose workflow you want to trigger.
  2. In the dropdown menu, click **Manually trigger**.
![Screenshot of the prebuild configuration dropdown menu, shown by clicking a button labeled with three dots. The "Manually trigger" option is selected.](https://docs.github.com/assets/cb-30904/images/help/codespaces/prebuilds-manually-trigger.png)


## [Further reading](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/managing-prebuilds#further-reading)
  * [Troubleshooting prebuilds](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-prebuilds)


