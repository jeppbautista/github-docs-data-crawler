  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Use GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot "Use GitHub Copilot")/
  * [Coding agent](https://docs.github.com/en/copilot/using-github-copilot/coding-agent "Coding agent")/
  * [Using Copilot to work on an issue](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/using-copilot-to-work-on-an-issue "Using Copilot to work on an issue")


# Using Copilot to work on an issue
Learn how to assign issues to GitHub Copilot, monitor progress as Copilot works on the issue, and then use pull request review comments to prompt Copilot to iterate on its work.
## Who can use this feature?
Copilot coding agent is available with the GitHub Copilot Pro+ and GitHub Copilot Enterprise plans in repositories where it is enabled.  
[Sign up for Copilot ](https://github.com/features/copilot/plans?ref_cta=Copilot+plans+signup&ref_loc=using+copilot+to+work+on+an+issue&ref_page=docs)
## In this article
  * [Introduction](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/using-copilot-to-work-on-an-issue#introduction)
  * [Assigning an issue to Copilot](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/using-copilot-to-work-on-an-issue#assigning-an-issue-to-copilot)
  * [Tracking Copilot's progress on your issue](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/using-copilot-to-work-on-an-issue#tracking-copilots-progress-on-your-issue)
  * [Working with Copilot on a pull request](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/using-copilot-to-work-on-an-issue#working-with-copilot-on-a-pull-request)
  * [Further reading](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/using-copilot-to-work-on-an-issue#further-reading)


Copilot coding agent is in public preview and subject to change.
## [Introduction](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/using-copilot-to-work-on-an-issue#introduction)
You can assign a GitHub issue to Copilot, just like you would with a human software developer. Copilot will start working on the issue, raise a pull request and when it's finished working, request a review from you. For more information, see [About assigning tasks to Copilot](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/about-assigning-tasks-to-copilot).
If you haven't used Copilot to work on an issue before, you can find some useful advice for getting good results in [Best practices for using Copilot to work on tasks](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/best-practices-for-using-copilot-to-work-on-tasks).
## [Assigning an issue to Copilot](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/using-copilot-to-work-on-an-issue#assigning-an-issue-to-copilot)
You can ask Copilot to start working on an issue by assigning the issue to Copilot.
You can assign an issue to Copilot:
  * On GitHub.com (see the [next section](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/using-copilot-to-work-on-an-issue#assigning-an-issue-to-copilot-on-githubcom))
  * Via the GitHub API (see [later in this article](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/using-copilot-to-work-on-an-issue#assigning-an-issue-to-copilot-via-the-github-api))
  * From the beta version of GitHub Mobile ([Join iOS TestFlight](https://testflight.apple.com/join/NLskzwi5) or [Join Google Play Beta](https://play.google.com/apps/testing/com.github.android))
  * Using GitHub CLI (see [`gh issue edit`](https://cli.github.com/manual/gh_issue_edit))


### [Assigning an issue to Copilot on GitHub.com](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/using-copilot-to-work-on-an-issue#assigning-an-issue-to-copilot-on-githubcom)
You can assign an issue to Copilot on GitHub.com in exactly the same way as you assign another user.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the main page of a repository. In the horizontal navigation bar, a tab, labeled "Issues," is outlined in dark orange.](https://docs.github.com/assets/cb-51267/images/help/repository/repo-tabs-issues-global-nav-update.png)
  3. Open the issue that you want to assign to Copilot.
  4. In the right side menu, click **Assignees**.
![Screenshot of the right sidebar of an issue. A header, labeled "Assignees", is outlined in dark orange.](https://docs.github.com/assets/cb-19901/images/help/issues/assignee-menu.png)
  5. Click **Copilot** from assignees list.
![Screenshot of "Assignees" window on an issue. Copilot is available in the list.](https://docs.github.com/assets/cb-52480/images/help/copilot/coding-agent/assign-to-copilot.png)


When you assign an issue to Copilot, it gets sent the issue title, description, and any comments that currently exist. After assigning the issue, Copilot will not be aware of, and therefore won't react to, any further comments that are added to the issue. If you have more information, or changes to the original requirement, add this as a comment in the pull request that Copilot raises.
You can also assign issues to Copilot from other places on GitHub.com:
  * From the list of issues on a repository's 
  * When viewing an issue in GitHub Projects.


### [Assigning an issue to Copilot via the GitHub API](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/using-copilot-to-work-on-an-issue#assigning-an-issue-to-copilot-via-the-github-api)
You can assign an issue to Copilot by making a request to the GraphQL API.
  1. Make sure you're authenticating with the API using a user token, for example a personal access token or a GitHub App user-to-server token.
  2. Verify that Copilot coding agent is enabled in the repository by checking if the repository's `suggestedActors` in the GraphQL API includes Copilot. Replace `monalisa` with the repository owner, and `octocat` with the name.
GraphQL```
query {
  repository(owner: "monalisa", name: "octocat") {
    suggestedActors(capabilities: [CAN_BE_ASSIGNED], first: 100) {
      nodes {
        login
        __typename

        ... on Bot {
          id
        }

        ... on User {
          id
        }
      }
    }
  }
}

```
```
query {
  repository(owner: "monalisa", name: "octocat") {
    suggestedActors(capabilities: [CAN_BE_ASSIGNED], first: 100) {
      nodes {
        login
        __typename

        ... on Bot {
          id
        }

        ... on User {
          id
        }
      }
    }
  }
}

```

If Copilot coding agent is enabled for the user and in the repository, the first node returned from the query will have the `login` value `copilot-swe-agent`.
  3. Fetch the GraphQL global ID of the issue you want to assign to Copilot, replacing `monalisa` with the repository owner, `octocat` with the name and `9000` with the issue number.
GraphQL```
query {
  repository(owner: "monalisa", name: "octocat") {
    issue(number: 9000) {
      id
      title
    }
  }
}

```
```
query {
  repository(owner: "monalisa", name: "octocat") {
    issue(number: 9000) {
      id
      title
    }
  }
}

```

  4. Assign the issue to Copilot using the `replaceActorsForAssignable` GraphQL mutation. Replace `ISSUE_ID` with the ID returned from the previous step, and `BOT_ID` with the ID returned from the step before that.
GraphQL```
mutation {
  replaceActorsForAssignable(input: {assignableId: "ISSUE_ID", assigneeIds: ["BOT_ID"]}) {
    assignable {
      ... on Issue {
        id
        title
        assignees(first: 10) {
          nodes {
            login
          }
        }
      }
    }
  }
}

```
```
mutation {
  replaceActorsForAssignable(input: {assignableId: "ISSUE_ID", assigneeIds: ["BOT_ID"]}) {
    assignable {
      ... on Issue {
        id
        title
        assignees(first: 10) {
          nodes {
            login
          }
        }
      }
    }
  }
}

```



## [Tracking Copilot's progress on your issue](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/using-copilot-to-work-on-an-issue#tracking-copilots-progress-on-your-issue)
Shortly after you assign an issue to Copilot, Copilot will leave an 👀 reaction on the issue.
![Screenshot of an issue assigned to Copilot. Copilot has left an eyes icon reaction.](https://docs.github.com/assets/cb-129528/images/help/copilot/coding-agent/issue-assigned-to-copilot.png)
A few seconds later, Copilot will open a draft pull request, linked to your original issue. An event will appear in the issue's timeline, linking to the pull request.
![Screenshot of an issue with a timeline event showing that a linked pull request has been opened.](https://docs.github.com/assets/cb-73703/images/help/copilot/coding-agent/issue-link-to-pr.png)
Copilot will start an **agent session** to work on your issue. A "Copilot started work" event will appear in the pull request timeline, and as Copilot works, it will update the pull request body with regular status updates, and push commits to the branch.
![Screenshot of a pull request with a series of timeline events, including "Copilot started work."](https://docs.github.com/assets/cb-139955/images/help/copilot/coding-agent/copilot-started-work.png)
If you want to check what Copilot is doing, click **View session**. The session log viewer is displayed, showing you a live log as Copilot works on the issue. If you want to stop Copilot from working on the issue, click **Stop session**. See [Using the Copilot coding agent logs](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/using-the-copilot-coding-agent-logs).
Once Copilot has finished, the agent session will end, and Copilot will request a review from you, triggering a notification. In addition, a "Copilot finished work" event will appear in the pull request timeline.
![Screenshot of a pull request timeline with "Copilot requested review" and "Copilot finished work" events.](https://docs.github.com/assets/cb-43158/images/help/copilot/coding-agent/copilot-finished-work.png)
## [Working with Copilot on a pull request](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/using-copilot-to-work-on-an-issue#working-with-copilot-on-a-pull-request)
After Copilot has finished working on the issue, you should review the pull request thoroughly and comment on anything that needs changed. See [Reviewing a pull request created by Copilot](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/reviewing-a-pull-request-created-by-copilot).
## [Further reading](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/using-copilot-to-work-on-an-issue#further-reading)
  * [Best practices for using Copilot to work on tasks](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/best-practices-for-using-copilot-to-work-on-tasks)
  * [Troubleshooting Copilot coding agent](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/troubleshooting-copilot-coding-agent)


