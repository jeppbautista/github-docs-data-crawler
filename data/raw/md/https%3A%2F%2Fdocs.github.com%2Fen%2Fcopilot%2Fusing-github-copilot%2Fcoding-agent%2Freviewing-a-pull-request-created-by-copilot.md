  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Use GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot "Use GitHub Copilot")/
  * [Coding agent](https://docs.github.com/en/copilot/using-github-copilot/coding-agent "Coding agent")/
  * [Review Copilot PRs](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/reviewing-a-pull-request-created-by-copilot "Review Copilot PRs")


# Reviewing a pull request created by Copilot
After Copilot creates a pull request you should review it and comment on anything that needs changes.
## Who can use this feature?
Copilot coding agent is available with the GitHub Copilot Pro+ and GitHub Copilot Enterprise plans in repositories where it is enabled.  
[Sign up for Copilot ](https://github.com/features/copilot/plans?ref_cta=Copilot+plans+signup&ref_loc=reviewing+a+pull+request+created+by+copilot&ref_page=docs)
## In this article
  * [Reviewing Copilot's changes](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/reviewing-a-pull-request-created-by-copilot#reviewing-copilots-changes)
  * [Managing GitHub Actions workflow runs](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/reviewing-a-pull-request-created-by-copilot#managing-github-actions-workflow-runs)
  * [Giving feedback on Copilot's work](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/reviewing-a-pull-request-created-by-copilot#giving-feedback-on-copilots-work)
  * [Further reading](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/reviewing-a-pull-request-created-by-copilot#further-reading)


Copilot coding agent is in public preview and subject to change.
## [Reviewing Copilot's changes](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/reviewing-a-pull-request-created-by-copilot#reviewing-copilots-changes)
After Copilot has finished working on a coding task, and has requested a pull request review from you, you should review Copilot's work thoroughly before merging the pull request.
If you have the "Required approvals" rule or branch protection enabled, you won't be able to approve pull requests that you initiated by assigning the related issue to Copilot. Someone else must approve the pull request before it can be merged.
You can ask Copilot to make changes using pull request comments, or you can check out Copilot's branch and make changes yourself.
We recommend you batch your review comments instead of submitting them individually.
When you leave a comment on Copilot's pull request, Copilot will consider your comment, and decide whether to start a new agent session to respond.
Copilot only responds to comments from people who have write access to the repository.
If Copilot starts a new agent session in response to your comment, an eyes emoji (👀) is added as a reaction to the comment, and a "Copilot has started work" event is added to the pull request timeline.
![Screenshot of a pull request timeline with a review comment with the eyes reaction and a "Copilot started work" timeline event.](https://docs.github.com/assets/cb-156524/images/help/copilot/coding-agent/comment-to-agent-on-pr.png)
Copilot may ignore a comment if it considers that the comment was not intended for it. If you are sure that you want Copilot to respond to your comment, you can @mention Copilot by including `@copilot` in your comment.
If you don't want Copilot to respond to comments on a pull request, you can unassign Copilot from the pull request. If you later reassign Copilot to the same pull request it will respond to new comments and push more changes. It will not respond to comment that were added while it was not assigned.
For more information, see the section "Use comments to iterate on a pull request" in [Best practices for using Copilot to work on tasks](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/best-practices-for-using-copilot-to-work-on-tasks#using-comments-to-iterate-on-a-pull-request).
## [Managing GitHub Actions workflow runs](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/reviewing-a-pull-request-created-by-copilot#managing-github-actions-workflow-runs)
GitHub Actions workflows will not run automatically when Copilot pushes changes to a pull request.
GitHub Actions workflows can be privileged and have access to sensitive secrets, so you should review code written by Copilot before allowing workflows to run.
To allow GitHub Actions workflows to run, click the **Approve and run workflows** button in the pull request's merge box.
![Screenshot of the merge box on a pull request from Copilot with the "Approve and run workflows" button.](https://docs.github.com/assets/cb-150864/images/help/copilot/coding-agent/approve-and-run-workflows.png)
## [Giving feedback on Copilot's work](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/reviewing-a-pull-request-created-by-copilot#giving-feedback-on-copilots-work)
You can provide feedback on Copilot's work using the feedback buttons on Copilot's pull requests and comments. We use your feedback to improve the product and the quality of Copilot's solutions.
  1. On a pull request or comment from Copilot, click the thumbs up (👍) or thumbs down (👎) button.
  2. If you click the thumbs down button, you're asked to provide additional information. You can, optionally, pick the reason for your negative feedback and leave a comment before clicking **Submit feedback**.


## [Further reading](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/reviewing-a-pull-request-created-by-copilot#further-reading)
  * [Best practices for using Copilot to work on tasks](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/best-practices-for-using-copilot-to-work-on-tasks)
  * [Using the Copilot coding agent logs](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/using-the-copilot-coding-agent-logs)
  * [Troubleshooting Copilot coding agent](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/troubleshooting-copilot-coding-agent)


