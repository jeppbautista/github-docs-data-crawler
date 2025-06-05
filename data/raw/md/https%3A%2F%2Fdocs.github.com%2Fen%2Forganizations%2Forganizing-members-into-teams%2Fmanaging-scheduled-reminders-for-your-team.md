  * [Organizations](https://docs.github.com/en/organizations "Organizations")/
  * [Organize members into teams](https://docs.github.com/en/organizations/organizing-members-into-teams "Organize members into teams")/
  * [Scheduled reminders](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-scheduled-reminders-for-your-team "Scheduled reminders")


# Managing scheduled reminders for your team
You can get reminders in Slack when your team has pull requests waiting for review.
## In this article
  * [About scheduled reminders for teams](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-scheduled-reminders-for-your-team#about-scheduled-reminders-for-teams)
  * [Creating a scheduled reminder for a team](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-scheduled-reminders-for-your-team#creating-a-scheduled-reminder-for-a-team)
  * [Managing a scheduled reminder for a team](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-scheduled-reminders-for-your-team#managing-a-scheduled-reminder-for-a-team)
  * [Deleting a scheduled reminder for a team](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-scheduled-reminders-for-your-team#deleting-a-scheduled-reminder-for-a-team)
  * [Further reading](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-scheduled-reminders-for-your-team#further-reading)


## [About scheduled reminders for teams](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-scheduled-reminders-for-your-team#about-scheduled-reminders-for-teams)
Scheduled reminders help teams focus on the most important review requests that require their attention. Scheduled reminders for pull requests will send a message to your team in Slack with all open pull requests that you or your team have been asked to review, at a specified time. For example, you can create a scheduled reminder to send a message to your team's main communication channel in Slack, including all open pull requests that the team is requested to review, every Wednesday at 9:00 a.m.
Team maintainers and organization owners can set scheduled reminders for any pull requests that a team has been requested to review. Before you can create a scheduled reminder for your team, an organization owner must authorize your Slack workspace. For more information, see [Managing scheduled reminders for your organization](https://docs.github.com/en/organizations/managing-organization-settings/managing-scheduled-reminders-for-your-organization).
GitHub will only trigger reminders for up to five repositories per owner and 20 pull requests per repository. Reminders are not sent when changes are merged from upstream into a fork.
## [Creating a scheduled reminder for a team](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-scheduled-reminders-for-your-team#creating-a-scheduled-reminder-for-a-team)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Click the name of your organization.
  3. Under your organization name, click 
![Screenshot of the horizontal navigation bar for an organization. A tab, labeled with the people icon and "Teams," is outlined in dark orange.](https://docs.github.com/assets/cb-22213/images/help/organizations/organization-teams-tab.png)
  4. Click the name of the team.
  5. At the top of the team page, click 
![Screenshot of the header of a team's page. A tab, labeled with a gear icon and "Settings", is outlined in dark orange.](https://docs.github.com/assets/cb-13532/images/help/teams/team-settings-global-nav-update.png)
  6. In the "Integrations" section of the sidebar, click 
  7. Under "Scheduled reminders", click **Add your first reminder**.
  8. Under "Slack workspace", click **Authorize Slack workspace** and follow the instructions.
  9. Under "Slack channel", type the name of the Slack channel where you'd like to receive notifications.
If this Slack channel is private, you will need to invite the integration into the channel: `/invite @github`. In addition, you need to ask users to run `/github signin` in one of their Slack channels, otherwise they will not be @mentioned. For more information, see [Getting started](https://github.com/integrations/slack?tab=readme-ov-file#getting-started) in the Slack integrations documentation.
  10. Under "Days", click **Weekdays**
  11. Under "Times", click **9:00 AM**
![Screenshot of Scheduled reminder options used to select the hour and time zone for reminders. 9:00 AM and 10:00 AM are checked in the open hours menu.](https://docs.github.com/assets/cb-21377/images/help/settings/scheduled-reminders-times.png)
  12. Under "Tracked repositories," choose which repositories you'd like the team to receive pull request review reminders for.
     * To receive reminders for all repositories that the chosen team has access to, click **All repositories**.
     * To receive reminders for a subset of repositories, click **Only select repositories** , then select one or more repositories that the chosen team has access to.
  13. Optionally, to exclude draft pull requests from scheduled reminders, select **Ignore drafts**. For more information, see [About pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests#draft-pull-requests).
  14. Optionally, to only include pull requests where a review is specifically requested from the team or a team member, select **Require review requests**. If you don't select this option, all pull requests are included in the scheduled reminder.
  15. Optionally, to send reminders to the pull request authors after the review requests have been fulfilled, select **Remind authors after reviews** and choose the number of reviews required before a reminder is sent.
  16. Optionally, to turn off scheduled reminders for pull requests that have already been reviewed and approved, select **Ignore approved pull requests**. Then, click **Ignore with 1 or more approvals** to choose how many approvals a pull request must have to be ignored.
  17. Under "Minimum age", type the age of a pull request, in hours. Scheduled reminders won't include pull requests that are newer than this age limit.
  18. Under "Minimum staleness", type the time since the last activity on a pull request, in hours. Scheduled reminders won't include pull requests whose last activity was more recent than this time.
  19. Under "Ignored terms", type a comma-separated list of terms that may appear in titles of pull requests. Scheduled reminders won't include any pull requests that contain one or more of these terms in their titles.
  20. Under "Ignored labels", type a comma-separated list of labels. Scheduled reminders won't include any pull requests that have one or more of these labels.
  21. Under "Required labels", type a comma-separated list of labels. Scheduled reminders will only include pull requests that haven't already been ignored, if they have one or more of these labels.
  22. Click **Create reminder**.
  23. Optionally, to test your reminder, click 


## [Managing a scheduled reminder for a team](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-scheduled-reminders-for-your-team#managing-a-scheduled-reminder-for-a-team)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Click the name of your organization.
  3. Under your organization name, click 
![Screenshot of the horizontal navigation bar for an organization. A tab, labeled with the people icon and "Teams," is outlined in dark orange.](https://docs.github.com/assets/cb-22213/images/help/organizations/organization-teams-tab.png)
  4. Click the name of the team.
  5. At the top of the team page, click 
![Screenshot of the header of a team's page. A tab, labeled with a gear icon and "Settings", is outlined in dark orange.](https://docs.github.com/assets/cb-13532/images/help/teams/team-settings-global-nav-update.png)
  6. In the "Integrations" section of the sidebar, click 
  7. Next to the scheduled reminder you'd like to update, click **Edit**.
  8. Make one or more changes to your scheduled reminder.
  9. To save your changes, click **Update reminder**.
  10. Optionally, to test your reminder, click 


## [Deleting a scheduled reminder for a team](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-scheduled-reminders-for-your-team#deleting-a-scheduled-reminder-for-a-team)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Click the name of your organization.
  3. Under your organization name, click 
![Screenshot of the horizontal navigation bar for an organization. A tab, labeled with the people icon and "Teams," is outlined in dark orange.](https://docs.github.com/assets/cb-22213/images/help/organizations/organization-teams-tab.png)
  4. Click the name of the team.
  5. At the top of the team page, click 
![Screenshot of the header of a team's page. A tab, labeled with a gear icon and "Settings", is outlined in dark orange.](https://docs.github.com/assets/cb-13532/images/help/teams/team-settings-global-nav-update.png)
  6. In the "Integrations" section of the sidebar, click 
  7. At the bottom of the page, click **Delete this reminder**.
  8. To confirm that you want to delete the scheduled reminder, click **OK**.


## [Further reading](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-scheduled-reminders-for-your-team#further-reading)
  * [Getting started](https://github.com/integrations/slack?tab=readme-ov-file#getting-started) in the Slack integrations documentation
  * [Managing scheduled reminders for your organization](https://docs.github.com/en/organizations/managing-organization-settings/managing-scheduled-reminders-for-your-organization)
  * [Managing your scheduled reminders](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-your-membership-in-organizations/managing-your-scheduled-reminders)


