  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Use cases and examples](https://docs.github.com/en/actions/use-cases-and-examples "Use cases and examples")/
  * [Project management](https://docs.github.com/en/actions/use-cases-and-examples/project-management "Project management")/
  * [Close inactive issues](https://docs.github.com/en/actions/use-cases-and-examples/project-management/closing-inactive-issues "Close inactive issues")


# Closing inactive issues
You can use GitHub Actions to comment on or close issues that have been inactive for a certain period of time.
## In this article
  * [Introduction](https://docs.github.com/en/actions/use-cases-and-examples/project-management/closing-inactive-issues#introduction)
  * [Creating the workflow](https://docs.github.com/en/actions/use-cases-and-examples/project-management/closing-inactive-issues#creating-the-workflow)
  * [Expected results](https://docs.github.com/en/actions/use-cases-and-examples/project-management/closing-inactive-issues#expected-results)
  * [Next steps](https://docs.github.com/en/actions/use-cases-and-examples/project-management/closing-inactive-issues#next-steps)


## [Introduction](https://docs.github.com/en/actions/use-cases-and-examples/project-management/closing-inactive-issues#introduction)
This tutorial demonstrates how to use the [`actions/stale` action](https://github.com/marketplace/actions/close-stale-issues) to comment on and close issues that have been inactive for a certain period of time. For example, you can comment if an issue has been inactive for 30 days to prompt participants to take action. Then, if no additional activity occurs after 14 days, you can close the issue.
In the tutorial, you will first make a workflow file that uses the [`actions/stale` action](https://github.com/marketplace/actions/close-stale-issues). Then, you will customize the workflow to suit your needs.
## [Creating the workflow](https://docs.github.com/en/actions/use-cases-and-examples/project-management/closing-inactive-issues#creating-the-workflow)
  1. Choose a repository where you want to apply this project management workflow. You can use an existing repository that you have write access to, or you can create a new repository. For more information about creating a repository, see [Creating a new repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository).
  2. In your repository, create a file called `.github/workflows/YOUR_WORKFLOW.yml`, replacing `YOUR_WORKFLOW` with a name of your choice. This is a workflow file. For more information about creating new files on GitHub, see [Creating new files](https://docs.github.com/en/repositories/working-with-files/managing-files/creating-new-files).
  3. Copy the following YAML contents into your workflow file.
YAML```
name: Close inactive issues
on:
  schedule:
    - cron: "30 1 * * *"

jobs:
  close-issues:
    runs-on: ubuntu-latest
    permissions:
      issues: write
      pull-requests: write
    steps:
      - uses: actions/stale@v9
        with:
          days-before-issue-stale: 30
          days-before-issue-close: 14
          stale-issue-label: "stale"
          stale-issue-message: "This issue is stale because it has been open for 30 days with no activity."
          close-issue-message: "This issue was closed because it has been inactive for 14 days since being marked as stale."
          days-before-pr-stale: -1
          days-before-pr-close: -1
          repo-token: ${{ secrets.GITHUB_TOKEN }}

```
```
name: Close inactive issues
on:
  schedule:
    - cron: "30 1 * * *"

jobs:
  close-issues:
    runs-on: ubuntu-latest
    permissions:
      issues: write
      pull-requests: write
    steps:
      - uses: actions/stale@v9
        with:
          days-before-issue-stale: 30
          days-before-issue-close: 14
          stale-issue-label: "stale"
          stale-issue-message: "This issue is stale because it has been open for 30 days with no activity."
          close-issue-message: "This issue was closed because it has been inactive for 14 days since being marked as stale."
          days-before-pr-stale: -1
          days-before-pr-close: -1
          repo-token: ${{ secrets.GITHUB_TOKEN }}

```

  4. Customize the parameters in your workflow file:
     * Change the value for `on.schedule` to dictate when you want this workflow to run. In the example above, the workflow will run every day at 1:30 UTC. For more information about scheduled workflows, see [Events that trigger workflows](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#scheduled-events).
     * Change the value for `days-before-issue-stale` to the number of days without activity before the `actions/stale` action labels an issue. If you never want this action to label issues, set this value to `-1`.
     * Change the value for `days-before-issue-close` to the number of days without activity before the `actions/stale` action closes an issue. If you never want this action to close issues, set this value to `-1`.
     * Change the value for `stale-issue-label` to the label that you want to apply to issues that have been inactive for the amount of time specified by `days-before-issue-stale`.
     * Change the value for `stale-issue-message` to the comment that you want to add to issues that are labeled by the `actions/stale` action.
     * Change the value for `close-issue-message` to the comment that you want to add to issues that are closed by the `actions/stale` action.
  5. Commit your workflow file to the default branch of your repository. For more information, see [Creating new files](https://docs.github.com/en/repositories/working-with-files/managing-files/creating-new-files).


## [Expected results](https://docs.github.com/en/actions/use-cases-and-examples/project-management/closing-inactive-issues#expected-results)
Based on the `schedule` parameter (for example, every day at 1:30 UTC), your workflow will find issues that have been inactive for the specified period of time and will add the specified comment and label. Additionally, your workflow will close any previously labeled issues if no additional activity has occurred for the specified period of time.
The `schedule` event can be delayed during periods of high loads of GitHub Actions workflow runs. High load times include the start of every hour. If the load is sufficiently high enough, some queued jobs may be dropped. To decrease the chance of delay, schedule your workflow to run at a different time of the hour.
You can view the history of your workflow runs to see this workflow run periodically. For more information, see [Viewing workflow run history](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/viewing-workflow-run-history).
This workflow will only label and/or close 30 issues at a time in order to avoid exceeding a rate limit. You can configure this with the `operations-per-run` setting. For more information, see the [`actions/stale` action documentation](https://github.com/marketplace/actions/close-stale-issues).
## [Next steps](https://docs.github.com/en/actions/use-cases-and-examples/project-management/closing-inactive-issues#next-steps)
  * To learn more about additional things you can do with the `actions/stale` action, like closing inactive pull requests, ignoring issues with certain labels or milestones, or only checking issues with certain labels, see the [`actions/stale` action documentation](https://github.com/marketplace/actions/close-stale-issues).
  * [Search GitHub](https://github.com/search?q=%22uses%3A+actions%2Fstale%22&type=code) for examples of workflows using this action.


