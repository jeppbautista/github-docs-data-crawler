  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Use cases and examples](https://docs.github.com/en/actions/use-cases-and-examples "Use cases and examples")/
  * [Project management](https://docs.github.com/en/actions/use-cases-and-examples/project-management "Project management")/
  * [Schedule issue creation](https://docs.github.com/en/actions/use-cases-and-examples/project-management/scheduling-issue-creation "Schedule issue creation")


# Scheduling issue creation
You can use GitHub Actions to create an issue on a regular basis for things like daily meetings or quarterly reviews.
## In this article
  * [Introduction](https://docs.github.com/en/actions/use-cases-and-examples/project-management/scheduling-issue-creation#introduction)
  * [Creating the workflow](https://docs.github.com/en/actions/use-cases-and-examples/project-management/scheduling-issue-creation#creating-the-workflow)
  * [Expected results](https://docs.github.com/en/actions/use-cases-and-examples/project-management/scheduling-issue-creation#expected-results)
  * [Next steps](https://docs.github.com/en/actions/use-cases-and-examples/project-management/scheduling-issue-creation#next-steps)


## [Introduction](https://docs.github.com/en/actions/use-cases-and-examples/project-management/scheduling-issue-creation#introduction)
This tutorial demonstrates how to use the GitHub CLI to create an issue on a regular basis. For example, you can create an issue each week to use as the agenda for a team meeting. For more information about GitHub CLI, see [Using GitHub CLI in workflows](https://docs.github.com/en/actions/using-workflows/using-github-cli-in-workflows).
In the tutorial, you will first make a workflow file that uses the GitHub CLI. Then, you will customize the workflow to suit your needs.
## [Creating the workflow](https://docs.github.com/en/actions/use-cases-and-examples/project-management/scheduling-issue-creation#creating-the-workflow)
  1. Choose a repository where you want to apply this project management workflow. You can use an existing repository that you have write access to, or you can create a new repository. For more information about creating a repository, see [Creating a new repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository).
  2. In your repository, create a file called `.github/workflows/YOUR_WORKFLOW.yml`, replacing `YOUR_WORKFLOW` with a name of your choice. This is a workflow file. For more information about creating new files on GitHub, see [Creating new files](https://docs.github.com/en/repositories/working-with-files/managing-files/creating-new-files).
  3. Copy the following YAML contents into your workflow file.
YAML```
name: Weekly Team Sync
on:
  schedule:
    - cron: 20 07 * * 1

jobs:
  create_issue:
    name: Create team sync issue
    runs-on: ubuntu-latest
    permissions:
      issues: write
    steps:
      - name: Create team sync issue
        run: |
          if [[ $CLOSE_PREVIOUS == true ]]; then
            previous_issue_number=$(gh issue list \
              --label "$LABELS" \
              --json number \
              --jq '.[0].number')
            if [[ -n $previous_issue_number ]]; then
              gh issue close "$previous_issue_number"
              gh issue unpin "$previous_issue_number"
            fi
          fi
          new_issue_url=$(gh issue create \
            --title "$TITLE" \
            --assignee "$ASSIGNEES" \
            --label "$LABELS" \
            --body "$BODY")
          if [[ $PINNED == true ]]; then
            gh issue pin "$new_issue_url"
          fi
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          GH_REPO: ${{ github.repository }}
          TITLE: Team sync
          ASSIGNEES: monalisa,doctocat,hubot
          LABELS: weekly sync,docs-team
          BODY: |
            ### Agenda

            - [ ] Start the recording
            - [ ] Check-ins
            - [ ] Discussion points
            - [ ] Post the recording

            ### Discussion Points
            Add things to discuss below

            - [Work this week](https://github.com/orgs/github/projects/3)
          PINNED: false
          CLOSE_PREVIOUS: false

```
```
name: Weekly Team Sync
on:
  schedule:
    - cron: 20 07 * * 1

jobs:
  create_issue:
    name: Create team sync issue
    runs-on: ubuntu-latest
    permissions:
      issues: write
    steps:
      - name: Create team sync issue
        run: |
          if [[ $CLOSE_PREVIOUS == true ]]; then
            previous_issue_number=$(gh issue list \
              --label "$LABELS" \
              --json number \
              --jq '.[0].number')
            if [[ -n $previous_issue_number ]]; then
              gh issue close "$previous_issue_number"
              gh issue unpin "$previous_issue_number"
            fi
          fi
          new_issue_url=$(gh issue create \
            --title "$TITLE" \
            --assignee "$ASSIGNEES" \
            --label "$LABELS" \
            --body "$BODY")
          if [[ $PINNED == true ]]; then
            gh issue pin "$new_issue_url"
          fi
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          GH_REPO: ${{ github.repository }}
          TITLE: Team sync
          ASSIGNEES: monalisa,doctocat,hubot
          LABELS: weekly sync,docs-team
          BODY: |
            ### Agenda

            - [ ] Start the recording
            - [ ] Check-ins
            - [ ] Discussion points
            - [ ] Post the recording

            ### Discussion Points
            Add things to discuss below

            - [Work this week](https://github.com/orgs/github/projects/3)
          PINNED: false
          CLOSE_PREVIOUS: false

```

  4. Customize the parameters in your workflow file:
     * Change the value for `on.schedule` to dictate when you want this workflow to run. In the example above, the workflow will run every Monday at 7:20 UTC. For more information about scheduled workflows, see [Events that trigger workflows](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#scheduled-events).
     * Change the value for `ASSIGNEES` to the list of GitHub usernames that you want to assign to the issue.
     * Change the value for `LABELS` to the list of labels that you want to apply to the issue.
     * Change the value for `TITLE` to the title that you want the issue to have.
     * Change the value for `BODY` to the text that you want in the issue body. The `|` character allows you to use a multi-line value for this parameter.
     * If you want to pin this issue in your repository, set `PINNED` to `true`. For more information about pinned issues, see [Pinning an issue to your repository](https://docs.github.com/en/issues/tracking-your-work-with-issues/pinning-an-issue-to-your-repository).
     * If you want to close the previous issue generated by this workflow each time a new issue is created, set `CLOSE_PREVIOUS` to `true`. The workflow will close the most recent issue that has the labels defined in the `labels` field. To avoid closing the wrong issue, use a unique label or combination of labels.
  5. Commit your workflow file to the default branch of your repository. For more information, see [Creating new files](https://docs.github.com/en/repositories/working-with-files/managing-files/creating-new-files).


## [Expected results](https://docs.github.com/en/actions/use-cases-and-examples/project-management/scheduling-issue-creation#expected-results)
Based on the `schedule` parameter (for example, every Monday at 7:20 UTC), your workflow will create a new issue with the assignees, labels, title, and body that you specified. If you set `PINNED` to `true`, the workflow will pin the issue to your repository. If you set `CLOSE_PREVIOUS` to true, the workflow will close the most recent issue with matching labels.
The `schedule` event can be delayed during periods of high loads of GitHub Actions workflow runs. High load times include the start of every hour. If the load is sufficiently high enough, some queued jobs may be dropped. To decrease the chance of delay, schedule your workflow to run at a different time of the hour.
You can view the history of your workflow runs to see this workflow run periodically. For more information, see [Viewing workflow run history](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/viewing-workflow-run-history).
## [Next steps](https://docs.github.com/en/actions/use-cases-and-examples/project-management/scheduling-issue-creation#next-steps)
  * To learn more about additional things you can do with the GitHub CLI, like using an issue template, see the [`gh issue create` documentation](https://cli.github.com/manual/gh_issue_create).
  * [Search GitHub Marketplace](https://github.com/marketplace?category=&type=actions&verification=&query=schedule+issue) for actions related to scheduled issues.


