  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Manage Copilot](https://docs.github.com/en/copilot/managing-copilot "Manage Copilot")/
  * [Manage for organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization "Manage for organization")/
  * [Review activity](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/reviewing-activity-related-to-github-copilot-in-your-organization "Review activity")/
  * [User activity data](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/reviewing-activity-related-to-github-copilot-in-your-organization/reviewing-user-activity-data-for-copilot-in-your-organization "User activity data")


# Reviewing user activity data for Copilot in your organization
Review GitHub Copilot usage in your organization to make informed decisions about seat assignment.
## Who can use this feature?
Organization owners
Organizations with a plan to Copilot Business
## In this article
  * [Reviewing user activity data for Copilot](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/reviewing-activity-related-to-github-copilot-in-your-organization/reviewing-user-activity-data-for-copilot-in-your-organization#reviewing-user-activity-data-for-copilot)
  * [Using the API to retrieve assignment information](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/reviewing-activity-related-to-github-copilot-in-your-organization/reviewing-user-activity-data-for-copilot-in-your-organization#using-the-api-to-retrieve-assignment-information)
  * [Understanding the last_activity_at calculation](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/reviewing-activity-related-to-github-copilot-in-your-organization/reviewing-user-activity-data-for-copilot-in-your-organization#understanding-the-last_activity_at-calculation)
  * [Further reading](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/reviewing-activity-related-to-github-copilot-in-your-organization/reviewing-user-activity-data-for-copilot-in-your-organization#further-reading)


## [Reviewing user activity data for Copilot](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/reviewing-activity-related-to-github-copilot-in-your-organization/reviewing-user-activity-data-for-copilot-in-your-organization#reviewing-user-activity-data-for-copilot)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the "Code, planning, and automation" section of the sidebar, click **Access**.
  4. At the top of the page, under "GitHub Copilot," you can see an overview of your organization's GitHub Copilot usage. You can see the number seats assigned through your Copilot Business plan, and the estimated monthly cost.
![Screenshot of the GitHub Copilot usage overview.](https://docs.github.com/assets/cb-26806/images/help/copilot/copilot-usage-overview.png)
  5. For more detailed information, next to "Access management," click **Get report**.
GitHub generates a report for you, which you can download as a CSV file.
  6. Alternatively, under "Access management," you can use the **Sort** options to sort the list of users by when they last used GitHub Copilot.


## [Using the API to retrieve assignment information](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/reviewing-activity-related-to-github-copilot-in-your-organization/reviewing-user-activity-data-for-copilot-in-your-organization#using-the-api-to-retrieve-assignment-information)
You can use GitHub's REST API to get details about the assignment of GitHub Copilot seats in your organization. See [Get Copilot seat information and settings for an organization](https://docs.github.com/en/rest/copilot/copilot-user-management?apiVersion=2022-11-28#get-copilot-seat-information-and-settings-for-an-organization), [List all Copilot seat assignments for an organization](https://docs.github.com/en/rest/copilot/copilot-user-management?apiVersion=2022-11-28#list-all-copilot-seat-assignments-for-an-organization), and [Get Copilot seat assignment details for a user](https://docs.github.com/en/rest/copilot/copilot-user-management?apiVersion=2022-11-28#get-copilot-seat-assignment-details-for-a-user).
## [Understanding the `last_activity_at` calculation](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/reviewing-activity-related-to-github-copilot-in-your-organization/reviewing-user-activity-data-for-copilot-in-your-organization#understanding-the-last_activity_at-calculation)
This data is in public preview and subject to change.
To align the `last_activity_at` data point with _actual usage_ , the system returns the timestamp of a user's most recent interaction with Copilot functionality. These interactions are:
  * Receiving a code suggestion in an IDE
  * Chatting with Copilot Chat in an IDE
  * Interacting with Copilot on a mobile device
  * Interacting with Copilot Chat for CLI


The `last_activity_at` date is consistent across the CSV generated via `Get Report` in Copilot Access settings as well as through GitHub's REST API. The events which are tracked come from both client, and server-side telemetry. This allows the timestamp to be durable in the event that network conditions would impact client-telemetry.
### [Troubleshooting `last_activity_at` data](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/reviewing-activity-related-to-github-copilot-in-your-organization/reviewing-user-activity-data-for-copilot-in-your-organization#troubleshooting-last_activity_at-data)
Processing new telemetry events and updating a user's `last_activity_at` date can take up to 24 hours. Users must have telemetry enabled in their IDE for their usage to be reflected in `last_activity_at`.
If you believe a user's `last_activity_at` date should be more recent than shown in the CSV or API report, please wait 24 hours and check again. If their recent Copilot usage is still not reflected in their `last_activity_at` date, have the user check that telemetry is enabled in their IDE settings.
## [Further reading](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/reviewing-activity-related-to-github-copilot-in-your-organization/reviewing-user-activity-data-for-copilot-in-your-organization#further-reading)
  * [GitHub Copilot Trust Center](https://copilot.github.trust.page)
  * [Granting access to Copilot for members of your organization](https://docs.github.com/en/copilot/managing-github-copilot-in-your-organization/granting-access-to-copilot-for-members-of-your-organization)
  * [Revoking access to Copilot for members of your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-access-to-github-copilot-in-your-organization/revoking-access-to-copilot-for-members-of-your-organization)
  * [Reviewing changes to content exclusions for GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion/reviewing-changes-to-content-exclusions-for-github-copilot)


