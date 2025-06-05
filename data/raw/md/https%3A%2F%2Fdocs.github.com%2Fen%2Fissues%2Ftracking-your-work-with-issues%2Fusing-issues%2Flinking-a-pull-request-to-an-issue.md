  * [GitHub Issues](https://docs.github.com/en/issues "GitHub Issues")/
  * [Issues](https://docs.github.com/en/issues/tracking-your-work-with-issues "Issues")/
  * [Using issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues "Using issues")/
  * [Link PR to issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue "Link PR to issue")


# Linking a pull request to an issue
You can link a pull request or branch to an issue to show that a fix is in progress and to automatically close the issue when the pull request or branch is merged.
## In this article
  * [About linked issues and pull requests](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue#about-linked-issues-and-pull-requests)
  * [Linking a pull request to an issue using a keyword](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword)
  * [Manually linking a pull request to an issue using the pull request sidebar](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue#manually-linking-a-pull-request-to-an-issue-using-the-pull-request-sidebar)
  * [Manually linking a pull request or branch to an issue using the issue sidebar](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue#manually-linking-a-pull-request-or-branch-to-an-issue-using-the-issue-sidebar)
  * [Further reading](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue#further-reading)


## [About linked issues and pull requests](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue#about-linked-issues-and-pull-requests)
You can link an issue to a pull request manually or using a supported keyword in the pull request description, that is, the summary text added by the author when they created the pull request.
When you link a pull request to the issue the pull request addresses, collaborators can see that someone is working on the issue.
When you merge a linked pull request into the **default branch** of a repository, its linked issue is automatically closed. For more information about the default branch, see [Changing the default branch](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/changing-the-default-branch).
The special keywords in a pull request description are interpreted only when the pull request targets the repository's _default_ branch. If the pull request targets _any other branch_ , then these keywords are ignored, no links are created, and merging the PR has no effect on the issues.
## [Linking a pull request to an issue using a keyword](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword)
You can link a pull request to an issue by using a supported keyword in the pull request's description or in a commit message. The pull request **must be** on the default branch.
  * `close`
  * `closes`
  * `closed`
  * `fix`
  * `fixes`
  * `fixed`
  * `resolve`
  * `resolves`
  * `resolved`


If you use a keyword to reference a pull request comment in another pull request, the pull requests will be linked. Merging the referencing pull request also closes the referenced pull request.
The syntax for closing keywords depends on whether the issue is in the same repository as the pull request.
Linked issue | Syntax | Example  
---|---|---  
Issue in the same repository | KEYWORD #ISSUE-NUMBER | `Closes #10`  
Issue in a different repository | KEYWORD OWNER/REPOSITORY#ISSUE-NUMBER | `Fixes octo-org/octo-repo#100`  
Multiple issues | Use full syntax for each issue | `Resolves #10, resolves #123, resolves octo-org/octo-repo#100`  
The keywords can be followed by colons or in uppercase. For example: `Closes: #10`, `CLOSES #10`, or `CLOSES: #10`.
Only manually linked pull requests can be manually unlinked. To unlink an issue that you linked using a keyword, you must edit the pull request description to remove the keyword.
You can also use closing keywords in a commit message. The issue will be closed when you merge the commit into the default branch, but the pull request that contains the commit will not be listed as a linked pull request.
## [Manually linking a pull request to an issue using the pull request sidebar](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue#manually-linking-a-pull-request-to-an-issue-using-the-pull-request-sidebar)
Anyone with write permissions to a repository can manually link a pull request to an issue from the pull request sidebar.
You can manually link up to ten issues to each pull request. The issue and pull request must be in the same repository.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the main page of a repository. In the horizontal navigation bar, a tab, labeled "Pull requests," is outlined in dark orange.](https://docs.github.com/assets/cb-51156/images/help/repository/repo-tabs-pull-requests-global-nav-update.png)
  3. In the list of pull requests, click the pull request that you'd like to link to an issue.
  4. In the right sidebar, click **Development**.
![Screenshot of the issue sidebar. "Development" is outlined in dark orange.](https://docs.github.com/assets/cb-3532/images/help/pull_requests/development-menu.png)
  5. Click the issue you want to link to the pull request.


## [Manually linking a pull request or branch to an issue using the issue sidebar](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue#manually-linking-a-pull-request-or-branch-to-an-issue-using-the-issue-sidebar)
Anyone with write permissions to a repository can manually link a pull request or branch to an issue from the issue sidebar.
You can manually link up to ten issues to each pull request. The issue can be in a different repository than the linked pull request or branch. Your last selected repository will be remembered.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the main page of a repository. In the horizontal navigation bar, a tab, labeled "Issues," is outlined in dark orange.](https://docs.github.com/assets/cb-51267/images/help/repository/repo-tabs-issues-global-nav-update.png)
  3. In the list of issues, click the issue that you'd like to link a pull request or branch to.
  4. In the right sidebar, click **Development**.
![Screenshot of the issue sidebar. "Development" is outlined in dark orange.](https://docs.github.com/assets/cb-28720/images/help/issues/development-menu.png)
  5. Click the repository containing the pull request or branch you want to link to the issue.
  6. Click the pull request or branch you want to link to the issue.
  7. Click **Apply**.


## [Further reading](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue#further-reading)
  * [Autolinked references and URLs](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/autolinked-references-and-urls#issues-and-pull-requests)


