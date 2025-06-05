  * [GitHub Issues](https://docs.github.com/en/issues "GitHub Issues")/
  * [Issues](https://docs.github.com/en/issues/tracking-your-work-with-issues "Issues")/
  * [Administering issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues "Administering issues")/
  * [Transfer an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues/transferring-an-issue-to-another-repository "Transfer an issue")


# Transferring an issue to another repository
To move an issue to a better fitting repository, you can transfer open issues to other repositories.
## Tool navigation
  * [GitHub CLI](https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues/transferring-an-issue-to-another-repository?tool=cli)
  * [Web browser](https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues/transferring-an-issue-to-another-repository?tool=webui)


## In this article
  * [Transferring an open issue to another repository](https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues/transferring-an-issue-to-another-repository#transferring-an-open-issue-to-another-repository)
  * [Further reading](https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues/transferring-an-issue-to-another-repository#further-reading)


To transfer an open issue to another repository, you must have write access to the repository the issue is in and the repository you're transferring the issue to. For more information, see [Repository roles for an organization](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization).
You can only transfer issues between repositories owned by the same user or organization account. A private repository issue cannot be transferred to a public repository.
When you transfer an issue, comments and assignees are retained. Labels and milestones are also retained if they're present in the target repository, with labels matching by name and milestones matching by both name and due date.
People or teams who are mentioned in the issue will receive a notification letting them know that the issue has been transferred to a new repository. The original URL redirects to the new issue's URL. People who don't have read permissions in the new repository will see a banner letting them know that the issue has been transferred to a new repository that they can't access.
## [Transferring an open issue to another repository](https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues/transferring-an-issue-to-another-repository#transferring-an-open-issue-to-another-repository)
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the main page of a repository. In the horizontal navigation bar, a tab, labeled "Issues," is outlined in dark orange.](https://docs.github.com/assets/cb-51267/images/help/repository/repo-tabs-issues-global-nav-update.png)
  3. In the list of issues, click the issue you'd like to transfer.
  4. In the right sidebar, click **Transfer issue**.
  5. Select the **Choose a repository** dropdown menu, and click the repository you want to transfer the issue to.
  6. Click **Transfer issue**.


To learn more about GitHub CLI, see [About GitHub CLI](https://docs.github.com/en/github-cli/github-cli/about-github-cli).
To transfer an issue, use the `gh issue transfer` subcommand. Replace the `issue` parameter with the number or URL of the issue. Replace the `owner/repo` parameter with the name of the repository that you want to transfer the issue to, such as `octocat/octo-repo`.
```
gh issue transfer ISSUE OWNER/REPO

```

## [Further reading](https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues/transferring-an-issue-to-another-repository#further-reading)
  * [About issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues)


