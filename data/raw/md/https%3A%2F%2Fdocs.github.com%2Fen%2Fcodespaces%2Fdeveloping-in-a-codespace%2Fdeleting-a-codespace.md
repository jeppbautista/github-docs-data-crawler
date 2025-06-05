  * [Codespaces](https://docs.github.com/en/codespaces "Codespaces")/
  * [Developing in a codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace "Developing in a codespace")/
  * [Delete a codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/deleting-a-codespace "Delete a codespace")


# Deleting a codespace
You can delete a codespace you no longer need.
## Tool navigation
  * [GitHub CLI](https://docs.github.com/en/codespaces/developing-in-a-codespace/deleting-a-codespace?tool=cli)
  * [Visual Studio Code](https://docs.github.com/en/codespaces/developing-in-a-codespace/deleting-a-codespace?tool=vscode)
  * [Web browser](https://docs.github.com/en/codespaces/developing-in-a-codespace/deleting-a-codespace?tool=webui)


## In this article
  * [Overview](https://docs.github.com/en/codespaces/developing-in-a-codespace/deleting-a-codespace#overview)
  * [Why you should delete unused codespaces](https://docs.github.com/en/codespaces/developing-in-a-codespace/deleting-a-codespace#why-you-should-delete-unused-codespaces)
  * [Deleting a codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/deleting-a-codespace#deleting-a-codespace)
  * [Bulk deleting codespaces](https://docs.github.com/en/codespaces/developing-in-a-codespace/deleting-a-codespace#bulk-deleting-codespaces)
  * [Deleting codespaces in your organization](https://docs.github.com/en/codespaces/developing-in-a-codespace/deleting-a-codespace#deleting-codespaces-in-your-organization)
  * [Further reading](https://docs.github.com/en/codespaces/developing-in-a-codespace/deleting-a-codespace#further-reading)


## [Overview](https://docs.github.com/en/codespaces/developing-in-a-codespace/deleting-a-codespace#overview)
GitHub Codespaces are automatically deleted after they have been stopped and have remained inactive for a defined number of days. The retention period for each codespace is set when the codespace is created and does not change. The default retention period is 30 days. See [Configuring automatic deletion of your codespaces](https://docs.github.com/en/codespaces/setting-your-user-preferences/configuring-automatic-deletion-of-your-codespaces?tool=webui).
You can manually delete a codespace in a variety of ways:
  * In the terminal by using GitHub CLI
  * In Visual Studio Code
  * In your web browser


Use the tabs at the top of this article to display instructions for each of these ways of deleting a codespace.
You can't delete a codespace from within JupyterLab.
## [Why you should delete unused codespaces](https://docs.github.com/en/codespaces/developing-in-a-codespace/deleting-a-codespace#why-you-should-delete-unused-codespaces)
There are costs associated with storing codespaces. You should therefore delete any codespaces you no longer need. See [About billing for GitHub Codespaces](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-codespaces/about-billing-for-github-codespaces).
There are limits to the number of codespaces you can create, and the number of codespaces you can run at the same time. These limits vary based on a number of factors. If you reach the maximum number of codespaces and try to create another, a message is displayed telling you that you must remove an existing codespace before you can create a new one.
## [Deleting a codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/deleting-a-codespace#deleting-a-codespace)
  1. In the top-left corner of GitHub, select [github.com/codespaces](https://github.com/codespaces).
  2. To the right of the codespace you want to delete, click 
![Screenshot of a list of codespaces with the dropdown menu for one of them displayed, showing the "Delete" option.](https://docs.github.com/assets/cb-89126/images/help/codespaces/delete-codespace.png)


You may have prebuild codespaces that are consuming additional storage which are not displayed on this dashboard. To delete them, follow the steps for “[Deleting a prebuild configuration](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/managing-prebuilds#deleting-a-prebuild-configuration).”
You can delete codespaces from within VS Code when you are not currently working in a codespace.
  1. In VS Code, in the Activity Bar, click the Remote Explorer icon.
![Screenshot of the Activity Bar. The icon for the "Remote Explorer" side bar \(a rectangle overlaid by a circle\) is highlighted with an orange outline.](https://docs.github.com/assets/cb-48473/images/help/codespaces/click-remote-explorer-icon-vscode.png)
If the Remote Explorer is not displayed in the Activity Bar:
    1. Access the Command Palette. For example, by pressing `Shift`+`Command`+`P` (Mac) / `Ctrl`+`Shift`+`P` (Windows/Linux).
    2. Type: `details`.
    3. Click **Codespaces: Details**.
  2. Under "GitHub Codespaces," right-click the codespace you want to delete.
  3. Click **Delete Codespace**.


To learn more about GitHub CLI, see [About GitHub CLI](https://docs.github.com/en/github-cli/github-cli/about-github-cli).
To delete a codespace use the `gh codespace delete` subcommand and then choose a codespace from the list that's displayed.
```
gh codespace delete

```

If you have unsaved changes, you'll be prompted to confirm deletion. You can use the `--force` flag to force deletion, avoiding this prompt.
For more information about this command, see [the GitHub CLI manual](https://cli.github.com/manual/gh_codespace_delete).
## [Bulk deleting codespaces](https://docs.github.com/en/codespaces/developing-in-a-codespace/deleting-a-codespace#bulk-deleting-codespaces)
You can use GitHub CLI to delete several or all of your codespaces with a single command. For more information, click the "GitHub CLI" tab near the top of this page.
You can use GitHub CLI to delete several or all of your codespaces with a single command. For more information, click the "GitHub CLI" tab near the top of this page.
You can delete several or all of your codespaces with a single command, using `gh codespace delete` followed by one of these flags:
`--all` - Delete all of your codespaces.
`--repo REPOSITORY` - Delete all of your codespaces for this repository. Or use together with the `--days` flag to filter by age of the codespace.
`--days NUMBER` - Delete all of your codespaces that are older than the specified number of days. Can be used together with the `--repo` flag.
By default you are prompted to confirm deletion of any codespaces that contain unsaved changes. You can use the `--force` flag to skip this confirmation.
### [Example](https://docs.github.com/en/codespaces/developing-in-a-codespace/deleting-a-codespace#example)
Delete all of the codespaces for the `octo-org/octo-repo` repository that you created more than 7 days ago.
```
gh codespace delete --repo octo-org/octo-repo --days 7

```

## [Deleting codespaces in your organization](https://docs.github.com/en/codespaces/developing-in-a-codespace/deleting-a-codespace#deleting-codespaces-in-your-organization)
As an organization owner, you can use GitHub CLI to delete any codespace in your organization.
For more information, click the "GitHub CLI" tab near the top of this page.
For more information, click the "GitHub CLI" tab near the top of this page.
  1. Enter one of these commands to display a list of codespaces.
     * `gh codespace delete --org ORGANIZATION` - Lists the current codespaces in the specified organization.
     * `gh codespace delete --org ORGANIZATION --user USER` - Lists only those codespaces created by the specified user. You must be an owner of the specified organization.
  2. In the list of codespaces, navigate to the codespace you want to delete.
  3. To delete the selected codespace press `Enter`.
If the codespace contains unsaved changes you will be prompted to confirm deletion.


You can also use the REST API to delete codespaces for your organization. See [REST API endpoints for Codespaces organizations](https://docs.github.com/en/rest/codespaces/organizations#delete-a-codespace-from-the-organization).
## [Further reading](https://docs.github.com/en/codespaces/developing-in-a-codespace/deleting-a-codespace#further-reading)
  * [Understanding the codespace lifecycle](https://docs.github.com/en/codespaces/about-codespaces/understanding-the-codespace-lifecycle)
  * [Configuring automatic deletion of your codespaces](https://docs.github.com/en/codespaces/setting-your-user-preferences/configuring-automatic-deletion-of-your-codespaces)
  * [Restricting the retention period for codespaces](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-retention-period-for-codespaces)


