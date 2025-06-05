  * [Organizations](https://docs.github.com/en/organizations "Organizations")/
  * [Organize members into teams](https://docs.github.com/en/organizations/organizing-members-into-teams "Organize members into teams")/
  * [Code review settings](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-code-review-settings-for-your-team "Code review settings")


# Managing code review settings for your team
You can decrease noise for your team by limiting notifications when your team is requested to review a pull request.
## Who can use this feature?
Team maintainers and organization owners can configure code review settings.
Code review settings are available in all public repositories owned by an organization, and all private repositories owned by organizations on GitHub Team, GitHub Enterprise Server, and GitHub Enterprise Cloud. For more information, see [GitHub’s plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans).
## In this article
  * [About code review settings](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-code-review-settings-for-your-team#about-code-review-settings)
  * [About team notifications](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-code-review-settings-for-your-team#about-team-notifications)
  * [About auto assignment](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-code-review-settings-for-your-team#about-auto-assignment)
  * [Configuring team notifications](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-code-review-settings-for-your-team#configuring-team-notifications)
  * [Configuring auto assignment](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-code-review-settings-for-your-team#configuring-auto-assignment)
  * [Disabling auto assignment](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-code-review-settings-for-your-team#disabling-auto-assignment)


## [About code review settings](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-code-review-settings-for-your-team#about-code-review-settings)
To reduce noise for your team and clarify individual responsibility for pull request reviews, you can configure code review settings.
  * Team notifications
  * Auto assignment


## [About team notifications](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-code-review-settings-for-your-team#about-team-notifications)
When you choose to only notify requested team members, you disable sending notifications to the entire team when the team is requested to review a pull request if a specific member of that team is also requested for review. This is especially useful when a repository is configured with teams as code owners, but contributors to the repository often know a specific individual that would be the correct reviewer for their pull request. For more information, see [About code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners).
## [About auto assignment](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-code-review-settings-for-your-team#about-auto-assignment)
When you enable auto assignment, any time your team has been requested to review a pull request, the team is removed as a reviewer and a specified subset of team members are assigned in the team's place. Code review assignments allow you to decide whether the whole team or just a subset of team members are notified when a team is requested for review.
When code owners are automatically requested for review, the team is still removed and replaced with individuals unless a branch protection rule is configured to require review from code owners. If such a branch protection rule is in place, the team request cannot be removed and so the individual request will appear in addition to the team. Once the individual completes their review, the team is removed.
### [Routing algorithms](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-code-review-settings-for-your-team#routing-algorithms)
Code review assignments automatically choose and assign reviewers based on one of two possible algorithms.
The round robin algorithm chooses reviewers based on who's received the least recent review request, focusing on alternating between all members of the team regardless of the number of outstanding reviews they currently have.
The load balance algorithm chooses reviewers based on each member's total number of recent review requests and considers the number of outstanding reviews for each member. The load balance algorithm tries to ensure that each team member reviews an equal number of pull requests in any 30 day period.
Any team members that have set their status to "Busy" will not be selected for review. If all team members are busy, the pull request will remain assigned to the team itself. For more information about user statuses, see [Personalizing your profile](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/personalizing-your-profile#setting-a-status).
## [Configuring team notifications](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-code-review-settings-for-your-team#configuring-team-notifications)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Click the name of your organization.
  3. Under your organization name, click 
![Screenshot of the horizontal navigation bar for an organization. A tab, labeled with the people icon and "Teams," is outlined in dark orange.](https://docs.github.com/assets/cb-22213/images/help/organizations/organization-teams-tab.png)
  4. Click the name of the team.
  5. At the top of the team page, click 
![Screenshot of the header of a team's page. A tab, labeled with a gear icon and "Settings", is outlined in dark orange.](https://docs.github.com/assets/cb-13532/images/help/teams/team-settings-global-nav-update.png)
  6. In the left sidebar, click 
  7. Select **Only notify requested team members.**
  8. Click **Save changes**.


## [Configuring auto assignment](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-code-review-settings-for-your-team#configuring-auto-assignment)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Click the name of your organization.
  3. Under your organization name, click 
![Screenshot of the horizontal navigation bar for an organization. A tab, labeled with the people icon and "Teams," is outlined in dark orange.](https://docs.github.com/assets/cb-22213/images/help/organizations/organization-teams-tab.png)
  4. Click the name of the team.
  5. At the top of the team page, click 
![Screenshot of the header of a team's page. A tab, labeled with a gear icon and "Settings", is outlined in dark orange.](https://docs.github.com/assets/cb-13532/images/help/teams/team-settings-global-nav-update.png)
  6. In the left sidebar, click 
  7. Select **Enable auto assignment**.
  8. Under "How many team members should be assigned to review?", select the dropdown menu and choose a number of reviewers to be assigned to each pull request.
  9. Under "Routing algorithm", use the dropdown menu and choose which algorithm you'd like to use. For more information, see [Routing algorithms](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-code-review-settings-for-your-team#routing-algorithms).
  10. Optionally, to always skip certain members of the team, select **Never assign certain team members**. Then, select one or more team members you'd like to always skip.
  11. Optionally, to include members of child teams as potential reviewers when assigning requests, select **Child team members**.
  12. Optionally, to count any members whose review has already been requested against the total number of members to assign, select **Count existing requests**.
  13. Optionally, to remove the review request from the team when assigning team members, select **Team review request**.
  14. Click **Save changes**.


## [Disabling auto assignment](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-code-review-settings-for-your-team#disabling-auto-assignment)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Click the name of your organization.
  3. Under your organization name, click 
![Screenshot of the horizontal navigation bar for an organization. A tab, labeled with the people icon and "Teams," is outlined in dark orange.](https://docs.github.com/assets/cb-22213/images/help/organizations/organization-teams-tab.png)
  4. Click the name of the team.
  5. At the top of the team page, click 
![Screenshot of the header of a team's page. A tab, labeled with a gear icon and "Settings", is outlined in dark orange.](https://docs.github.com/assets/cb-13532/images/help/teams/team-settings-global-nav-update.png)
  6. Deselect **Enable auto assignment**.
  7. Click **Save changes**.


