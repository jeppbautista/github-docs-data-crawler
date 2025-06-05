  * [Organizations](https://docs.github.com/en/organizations "Organizations")/
  * [Manage organization settings](https://docs.github.com/en/organizations/managing-organization-settings "Manage organization settings")/
  * [Manage scheduled reminders](https://docs.github.com/en/organizations/managing-organization-settings/managing-scheduled-reminders-for-your-organization "Manage scheduled reminders")


# Managing scheduled reminders for your organization
You can get reminders in Slack for all pull requests that teams in your organization have been requested to review.
## In this article
  * [About scheduled reminders for pull requests](https://docs.github.com/en/organizations/managing-organization-settings/managing-scheduled-reminders-for-your-organization#about-scheduled-reminders-for-pull-requests)
  * [Creating a scheduled reminder for an organization](https://docs.github.com/en/organizations/managing-organization-settings/managing-scheduled-reminders-for-your-organization#creating-a-scheduled-reminder-for-an-organization)
  * [Managing a scheduled reminder for an organization](https://docs.github.com/en/organizations/managing-organization-settings/managing-scheduled-reminders-for-your-organization#managing-a-scheduled-reminder-for-an-organization)
  * [Deleting a scheduled reminder for an organization](https://docs.github.com/en/organizations/managing-organization-settings/managing-scheduled-reminders-for-your-organization#deleting-a-scheduled-reminder-for-an-organization)
  * [Further reading](https://docs.github.com/en/organizations/managing-organization-settings/managing-scheduled-reminders-for-your-organization#further-reading)


## [About scheduled reminders for pull requests](https://docs.github.com/en/organizations/managing-organization-settings/managing-scheduled-reminders-for-your-organization#about-scheduled-reminders-for-pull-requests)
Scheduled reminders help teams focus on the most important review requests that require their attention. Scheduled reminders for pull requests will send a message to your team in Slack with all open pull requests that you or your team have been asked to review, at a specified time. For example, you can create a scheduled reminder to send a message to your team's main communication channel in Slack, including all open pull requests that the team is requested to review, every Wednesday at 9:00 a.m.
Organization owners can schedule a reminder for one or more teams in their organization, for all pull requests the team or teams have been requested to review.
GitHub will only trigger reminders for up to five repositories per owner and 20 pull requests per repository. Reminders are not sent when changes are merged from upstream into a fork.
## [Creating a scheduled reminder for an organization](https://docs.github.com/en/organizations/managing-organization-settings/managing-scheduled-reminders-for-your-organization#creating-a-scheduled-reminder-for-an-organization)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the "Integrations" section of the sidebar, click 
  4. Under "Scheduled reminders", click **Add your first reminder**.
  5. Under "Slack workspace", click **Authorize Slack workspace** and follow the instructions.
  6. Under "Slack channel", type the name of the Slack channel where you'd like to receive notifications. 
If this Slack channel is private, you will need to invite the integration into the channel: `/invite @github`. In addition, you need to ask users to run `/github signin` in one of their Slack channels, otherwise they will not be @mentioned. For more information, see [Getting started](https://github.com/integrations/slack?tab=readme-ov-file#getting-started) in the Slack integrations documentation.
  7. Under "Days", click **Weekdays**
  8. Under "Times", click **9:00 AM**
![Screenshot of Scheduled reminder options used to select the hour and time zone for reminders. 9:00 AM and 10:00 AM are checked in the open hours menu.](https://docs.github.com/assets/cb-21377/images/help/settings/scheduled-reminders-times.png)
  9. Under "Tracked repositories," choose which repositories you'd like the team to receive pull request review reminders for. 
     * To receive reminders for all repositories that the chosen team has access to, click **All repositories**.
     * To receive reminders for a subset of repositories, click **Only select repositories** , then select one or more repositories that the chosen team has access to.
  10. Under "Filter by team assigned to review code", select the **Add a team** dropdown menu and click one or more teams. You can add up to 100 teams. If the team you select doesn't have access to the "Tracked repositories" selected above, you won't be able to create the scheduled reminder.
  11. Optionally, to exclude draft pull requests from scheduled reminders, select **Ignore drafts**. For more information, see [About pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests#draft-pull-requests).
  12. Optionally, to only include pull requests where a review is specifically requested from the team or a team member, select **Require review requests**. If you don't select this option, all pull requests are included in the scheduled reminder.
  13. Optionally, to send reminders to the pull request authors after the review requests have been fulfilled, select **Remind authors after reviews** and choose the number of reviews required before a reminder is sent.
  14. Optionally, to turn off scheduled reminders for pull requests that have already been reviewed and approved, select **Ignore approved pull requests**. Then, click **Ignore with 1 or more approvals** to choose how many approvals a pull request must have to be ignored.
  15. Under "Minimum age", type the age of a pull request, in hours. Scheduled reminders won't include pull requests that are newer than this age limit.
  16. Under "Minimum staleness", type the time since the last activity on a pull request, in hours. Scheduled reminders won't include pull requests whose last activity was more recent than this time.
  17. Under "Ignored terms", type a comma-separated list of terms that may appear in titles of pull requests. Scheduled reminders won't include any pull requests that contain one or more of these terms in their titles.
  18. Under "Ignored labels", type a comma-separated list of labels. Scheduled reminders won't include any pull requests that have one or more of these labels.
  19. Under "Required labels", type a comma-separated list of labels. Scheduled reminders will only include pull requests that haven't already been ignored, if they have one or more of these labels.
  20. Click **Create reminder**.
  21. Optionally, to test your reminder, click 


## [Managing a scheduled reminder for an organization](https://docs.github.com/en/organizations/managing-organization-settings/managing-scheduled-reminders-for-your-organization#managing-a-scheduled-reminder-for-an-organization)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the "Integrations" section of the sidebar, click 
  4. Next to the scheduled reminder you'd like to update, click **Edit**.
  5. Make one or more changes to your scheduled reminder.
  6. To save your changes, click **Update reminder**.
  7. Optionally, to test your reminder, click 


## [Deleting a scheduled reminder for an organization](https://docs.github.com/en/organizations/managing-organization-settings/managing-scheduled-reminders-for-your-organization#deleting-a-scheduled-reminder-for-an-organization)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the "Integrations" section of the sidebar, click 
  4. At the bottom of the page, click **Delete this reminder**.
  5. To confirm that you want to delete the scheduled reminder, click **OK**.


## [Further reading](https://docs.github.com/en/organizations/managing-organization-settings/managing-scheduled-reminders-for-your-organization#further-reading)
  * [Getting started](https://github.com/integrations/slack?tab=readme-ov-file#getting-started) in the Slack integrations documentation
  * [Managing your scheduled reminders](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-your-membership-in-organizations/managing-your-scheduled-reminders)
  * [Managing scheduled reminders for your team](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-scheduled-reminders-for-your-team)


