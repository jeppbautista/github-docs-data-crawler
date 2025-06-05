  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Use GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot "Use GitHub Copilot")/
  * [Code review](https://docs.github.com/en/copilot/using-github-copilot/code-review "Code review")/
  * [Automatic code review](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-automatic-code-review-by-copilot "Automatic code review")


# Configuring automatic code review by Copilot
Learn how to configure Copilot to automatically review pull requests.
## In this article
  * [About automatic code review](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-automatic-code-review-by-copilot#about-automatic-code-review)
  * [Configuring automatic code review for all pull requests you create](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-automatic-code-review-by-copilot#configuring-automatic-code-review-for-all-pull-requests-you-create)
  * [Configuring automatic code review for a single repository](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-automatic-code-review-by-copilot#configuring-automatic-code-review-for-a-single-repository)
  * [Configuring automatic code review for repositories in an organization](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-automatic-code-review-by-copilot#configuring-automatic-code-review-for-repositories-in-an-organization)


## [About automatic code review](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-automatic-code-review-by-copilot#about-automatic-code-review)
By default, Copilot will only review a pull request if it's assigned to the pull request in the same way you would assign a human reviewer. However:
  * Individual users on the Copilot Pro or Copilot Pro+ plan can configure Copilot to automatically review all pull requests they create.
  * Repository owners can configure Copilot to automatically review all pull requests in the repository that are created by people with access to Copilot.
  * Organization owners can configure Copilot to automatically review all pull requests in some or all of the repositories in the organization where the pull request is created by a Copilot user.


### [Triggering an automatic pull request review](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-automatic-code-review-by-copilot#triggering-an-automatic-pull-request-review)
After you configure automatic code review, Copilot will review pull requests in the following situations:
  * When a pull request is created as an "Open" pull request.
A review is not triggered if the pull request is created as a "Draft" pull request.
  * The first time a "Draft" pull request is switched to "Open".


Copilot only automatically reviews a pull request once. If you make changes to the pull request after it has been automatically reviewed and you want Copilot to re-review the pull request, you must request this manually. To do this, click the **Reviewers** menu.
### [Limits on automatic pull request reviews](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-automatic-code-review-by-copilot#limits-on-automatic-pull-request-reviews)
Copilot code review is a premium feature with a per-person monthly quota. When Copilot carries out an automatic review, it uses one premium request from the quota of the user who created the pull request. For more information, see [Using GitHub Copilot code review](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review#code-review-monthly-quota).
## [Configuring automatic code review for all pull requests you create](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-automatic-code-review-by-copilot#configuring-automatic-code-review-for-all-pull-requests-you-create)
This is only available if you are on the Copilot Pro or Copilot Pro+ plan.
  1. In the upper-right corner of any page, click your profile photo, then click 
  2. Locate the **Automatic Copilot code review** option and click the dropdown button.
![Screenshot of the "Automatic Copilot code review" setting with the dropdown menu displayed.](https://docs.github.com/assets/cb-86751/images/help/copilot/code-review/automatic-code-review-personal.png)
  3. In the dropdown menu, select **Enabled**.


## [Configuring automatic code review for a single repository](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-automatic-code-review-by-copilot#configuring-automatic-code-review-for-a-single-repository)
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the left sidebar, under "Code and automation," click **Rules** , then click **Rulesets**.
![Screenshot of the sidebar of the "Settings" page for a repository. The "Rules" sub-menu is expanded, and the "Rulesets" option is outlined in orange.](https://docs.github.com/assets/cb-80504/images/help/repository/rulesets-settings.png)
  4. Click **New ruleset**.
  5. Click **New branch ruleset**.
  6. Under "Ruleset name," type a name for the ruleset.
  7. To activate the ruleset, under "Enforcement Status", select **Active**.
  8. Under "Target branches," click **Add target** and choose one of the options—for example, **Include default branch** or **Include all branches**.
  9. Under "Branch rules," select the **Require a pull request before merging** checkbox.
This expands a set of subsidiary options.
  10. Select the **Request pull request review from Copilot** checkbox.
![Screenshot of the "Request pull request review from Copilot" branch ruleset option.](https://docs.github.com/assets/cb-144409/images/help/copilot/code-review/automatic-code-review.png)
  11. At the bottom of the page, click **Create**.


## [Configuring automatic code review for repositories in an organization](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-automatic-code-review-by-copilot#configuring-automatic-code-review-for-repositories-in-an-organization)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the left sidebar, in the "Code, planning, and automation" section, click **Rulesets**.
![Screenshot of an organization's settings page. In the sidebar, a link labeled "Rulesets" is outlined in orange.](https://docs.github.com/assets/cb-32436/images/help/organizations/sidebar-repository-rulesets.png)
  4. Click **New ruleset**.
  5. Click **New branch ruleset**.
  6. Under "Ruleset name," type a name for the ruleset.
  7. To activate the ruleset, under "Enforcement Status", select **Active**.
  8. Under "Target repositories," click **Add target** and choose either **Include by pattern** or **Exclude by pattern**.
  9. In the dialog box that's displayed, type a pattern that will match the names of repositories in your organization—for example, `*feature` to match all repositories with names that end in `feature`.
For information about pattern-matching syntax, see [Creating rulesets for repositories in your organization](https://docs.github.com/en/organizations/managing-organization-settings/creating-rulesets-for-repositories-in-your-organization#using-fnmatch-syntax).
  10. In the dialog box, click **Add inclusion pattern** or **Add exclusion pattern**.
  11. Repeat the process for any additional patterns you want to add.
You can add multiple targeting criteria to the same ruleset. Exclusion patterns are applied after inclusion patterns. For example, you could include any repositories matching the pattern `*cat*`, and specifically exclude a repository matching the pattern `not-a-cat`.
  12. Under "Target branches," click **Add target** and choose one of the target options.
  13. Under "Branch rules," select the **Require a pull request before merging** checkbox.
This expands a set of subsidiary options.
  14. Select the **Request pull request review from Copilot** checkbox.
  15. At the bottom of the page, click **Create**.


