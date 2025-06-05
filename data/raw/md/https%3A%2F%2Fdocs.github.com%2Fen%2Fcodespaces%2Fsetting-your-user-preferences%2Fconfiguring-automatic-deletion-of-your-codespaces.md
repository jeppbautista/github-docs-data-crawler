  * [Codespaces](https://docs.github.com/en/codespaces "Codespaces")/
  * [Setting your user preferences](https://docs.github.com/en/codespaces/setting-your-user-preferences "Setting your user preferences")/
  * [Configure automatic deletion](https://docs.github.com/en/codespaces/setting-your-user-preferences/configuring-automatic-deletion-of-your-codespaces "Configure automatic deletion")


# Configuring automatic deletion of your codespaces
Inactive codespaces are automatically deleted. You can choose how long your stopped codespaces are retained, up to a maximum of 30 days.
## Tool navigation
  * [GitHub CLI](https://docs.github.com/en/codespaces/setting-your-user-preferences/configuring-automatic-deletion-of-your-codespaces?tool=cli)
  * [Visual Studio Code](https://docs.github.com/en/codespaces/setting-your-user-preferences/configuring-automatic-deletion-of-your-codespaces?tool=vscode)
  * [Web browser](https://docs.github.com/en/codespaces/setting-your-user-preferences/configuring-automatic-deletion-of-your-codespaces?tool=webui)


## In this article
  * [Setting a default retention period for your codespaces](https://docs.github.com/en/codespaces/setting-your-user-preferences/configuring-automatic-deletion-of-your-codespaces#setting-a-default-retention-period-for-your-codespaces)
  * [Checking the remaining time until autodeletion](https://docs.github.com/en/codespaces/setting-your-user-preferences/configuring-automatic-deletion-of-your-codespaces#checking-the-remaining-time-until-autodeletion)
  * [Avoiding automatic deletion of codespaces](https://docs.github.com/en/codespaces/setting-your-user-preferences/configuring-automatic-deletion-of-your-codespaces#avoiding-automatic-deletion-of-codespaces)
  * [Setting a retention period for a codespace](https://docs.github.com/en/codespaces/setting-your-user-preferences/configuring-automatic-deletion-of-your-codespaces#setting-a-retention-period-for-a-codespace)
  * [Setting the retention period](https://docs.github.com/en/codespaces/setting-your-user-preferences/configuring-automatic-deletion-of-your-codespaces#setting-the-retention-period)
  * [Checking whether codespaces will be autodeleted soon](https://docs.github.com/en/codespaces/setting-your-user-preferences/configuring-automatic-deletion-of-your-codespaces#checking-whether-codespaces-will-be-autodeleted-soon)
  * [Further reading](https://docs.github.com/en/codespaces/setting-your-user-preferences/configuring-automatic-deletion-of-your-codespaces#further-reading)


By default, GitHub Codespaces are automatically deleted after they have been stopped and have remained inactive for 30 days.
However, because GitHub Codespaces incurs storage charges, you may prefer to reduce the retention period by changing your default period in your personal settings for GitHub Codespaces. For more information about storage charges, see [About billing for GitHub Codespaces](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#codespaces-pricing).
Whether or not you have set a personal codespace retention period, it's a good idea to get into the habit of deleting codespaces that you no longer need. See [Deleting a codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/deleting-a-codespace).
Automatic deletion happens irrespective of whether a codespace contains unpushed changes. To prevent automatic deletion of a codespace, just open the codespace again. The retention period is reset every time you connect to a codespace, and the retention countdown restarts when the codespace is stopped.
If a repository belongs to an organization, the organization owner may have set a retention period for the whole organization. If this period is less than the default retention period in your personal settings then the organization retention period will apply to codespaces you create for this repository. See [Restricting the retention period for codespaces](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-retention-period-for-codespaces).
Each codespace has its own retention period. You may, therefore, have codespaces with different retention periods. For example, if:
  * You created a codespace, changed your default retention period, then created another codespace.
  * You created a codespace using GitHub CLI and specified a different retention period.
  * You created a codespace for an organization-owned repository that has a retention period configured in the organization settings. The ownership of the codespaces you create is shown on the [Your codespaces](https://github.com/settings/codespaces) page.


The retention period is specified in days. A day represents a 24-hour period, beginning at the time of day when you stop a codespace.
## [Setting a default retention period for your codespaces](https://docs.github.com/en/codespaces/setting-your-user-preferences/configuring-automatic-deletion-of-your-codespaces#setting-a-default-retention-period-for-your-codespaces)
  1. In the upper-right corner of any page on GitHub, click your profile photo, then click 
  2. In the "Code, planning, and automation" section of the sidebar, click 
  3. Under "Default retention period", enter the number of days for which you want your codespaces to be retained, by default, after they have been stopped.
![Screenshot of the "Default retention period" setting, currently set to 1 day. Next to the number of days is the "Save" button.](https://docs.github.com/assets/cb-16014/images/help/codespaces/setting-default-retention.png)
You can set your default retention period between `0` and `30` days.
Setting the period to `0` will result in your codespaces being immediately deleted when you stop them, or when they timeout due to inactivity. See [Setting your timeout period for GitHub Codespaces](https://docs.github.com/en/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces).
  4. Click **Save**.


When you create a codespace using GitHub CLI you can override this default. If you create a codespace in an organization that specifies a shorter retention period, the organization-level value overrides your personal setting.
If you set a retention period of more than a day, you'll be sent an email notification one day prior to its deletion.
## [Checking the remaining time until autodeletion](https://docs.github.com/en/codespaces/setting-your-user-preferences/configuring-automatic-deletion-of-your-codespaces#checking-the-remaining-time-until-autodeletion)
You can check whether a codespace is due to be automatically deleted soon.
When an inactive codespace is approaching the end of its retention period, this is indicated in your list of codespaces on GitHub at <https://github.com/codespaces>.
![Screenshot of a list of three codespaces. The third of these is labeled "Expiring in 4 days" which is highlighted with a dark orange outline.](https://docs.github.com/assets/cb-48557/images/help/codespaces/retention-deletion-message.png)
## [Avoiding automatic deletion of codespaces](https://docs.github.com/en/codespaces/setting-your-user-preferences/configuring-automatic-deletion-of-your-codespaces#avoiding-automatic-deletion-of-codespaces)
You may have a codespace that you want to keep for longer than the retention period defined in your personal settings. You can do this by using the "Keep codespace" option. When you select this option, your codespace will be retained indefinitely, until you delete it manually.
The "Keep codespace" option is not available for organization-owned codespaces affected by an organization retention policy.
Codespaces incur storage costs, or consume your included storage allowance if the codespace is owned by your personal GitHub account. You should therefore be aware of the cost implications of storing codespaces indefinitely. See [About billing for GitHub Codespaces](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#about-billing-for-storage-usage).
  1. In the top-left corner of GitHub, select [github.com/codespaces](https://github.com/codespaces).
  2. To the right of the codespace you want to exempt from automatic deletion, click 
![Screenshot of the dropdown menu for an active codespace. The "Keep codespace" option has a tooltip saying "Expires 10 days after shutdown."](https://docs.github.com/assets/cb-103196/images/help/codespaces/keep-codespace.png)


Codespaces that you have exempted from automatic deletion are indicated in your list of codespaces with the bookmark icon (
![Screenshot of a section of the codespaces list, showing a codespace labeled with the bookmark icon.](https://docs.github.com/assets/cb-15854/images/help/codespaces/keep-codespace-bookmarked.png)
## [Setting a retention period for a codespace](https://docs.github.com/en/codespaces/setting-your-user-preferences/configuring-automatic-deletion-of-your-codespaces#setting-a-retention-period-for-a-codespace)
If you have installed GitHub CLI, you can use it to work with GitHub Codespaces. For installation instructions for GitHub CLI, see the [GitHub CLI repository](https://github.com/cli/cli#installation).
To set the codespace retention period when you create a codespace, use the `--retention-period` flag with the `codespace create` subcommand. Specify the period in days. The period must be between 0 and 30 days.
```
gh codespace create --retention-period DAYS

```

If you don't specify a retention period when you create a codespace, then either your default retention period, or an organization retention period, will be used, depending on which is lower. For information about setting your default retention period, click the "Web browser" tab on this page.
To learn more about GitHub CLI, see [About GitHub CLI](https://docs.github.com/en/github-cli/github-cli/about-github-cli).
## [Setting the retention period](https://docs.github.com/en/codespaces/setting-your-user-preferences/configuring-automatic-deletion-of-your-codespaces#setting-the-retention-period)
You can set your default retention period in your web browser, on GitHub. Alternatively, if you use GitHub CLI to create a codespace you can set a retention period for that particular codespace. For more information, click the appropriate tab above.
## [Checking whether codespaces will be autodeleted soon](https://docs.github.com/en/codespaces/setting-your-user-preferences/configuring-automatic-deletion-of-your-codespaces#checking-whether-codespaces-will-be-autodeleted-soon)
You can check, in the Visual Studio Code desktop application, whether a codespace is due to be automatically deleted soon.
  1. In VS Code, in the Activity Bar, click the Remote Explorer icon.
![Screenshot of the Activity Bar. The icon for the "Remote Explorer" side bar \(a rectangle overlaid by a circle\) is highlighted with an orange outline.](https://docs.github.com/assets/cb-48473/images/help/codespaces/click-remote-explorer-icon-vscode.png)
If the Remote Explorer is not displayed in the Activity Bar:
    1. Access the Command Palette. For example, by pressing `Shift`+`Command`+`P` (Mac) / `Ctrl`+`Shift`+`P` (Windows/Linux).
    2. Type: `details`.
    3. Click **Codespaces: Details**.
  2. Choose **GitHub Codespaces** from the dropdown menu at the top right of the Remote Explorer, if it is not already selected.
  3. Under "GITHUB CODESPACES," position the mouse pointer over the codespace that you're interested in. A pop-up box is displayed showing you information about the codespace.
If the codespace is nearing the end of its retention period, a line is included telling when this period is due to expire.
![Screenshot of the "Remote Explorer" side bar. In the right-click menu for a codespace, "Expiring in 19 days" is highlighted with an orange outline.](https://docs.github.com/assets/cb-74200/images/help/codespaces/vscode-deleting-in-5-days.png)


## [Further reading](https://docs.github.com/en/codespaces/setting-your-user-preferences/configuring-automatic-deletion-of-your-codespaces#further-reading)
  * [Customizing your codespace](https://docs.github.com/en/codespaces/customizing-your-codespace)
  * [Managing your codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces)


