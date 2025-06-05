  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Share automations](https://docs.github.com/en/actions/sharing-automations "Share automations")/
  * [Share from your private repository](https://docs.github.com/en/actions/sharing-automations/sharing-actions-and-workflows-from-your-private-repository "Share from your private repository")


# Sharing actions and workflows from your private repository
You can share an action or reusable workflow without publishing them publicly.
## In this article
  * [About GitHub Actions access to private repositories](https://docs.github.com/en/actions/sharing-automations/sharing-actions-and-workflows-from-your-private-repository#about-github-actions-access-to-private-repositories)
  * [Sharing actions and workflows from your private repository](https://docs.github.com/en/actions/sharing-automations/sharing-actions-and-workflows-from-your-private-repository#sharing-actions-and-workflows-from-your-private-repository)
  * [Further reading](https://docs.github.com/en/actions/sharing-automations/sharing-actions-and-workflows-from-your-private-repository#further-reading)


## [About GitHub Actions access to private repositories](https://docs.github.com/en/actions/sharing-automations/sharing-actions-and-workflows-from-your-private-repository#about-github-actions-access-to-private-repositories)
You can share actions and reusable workflows from your private repository, without making them public, by allowing GitHub Actions workflows to access a private repository that contains the action or reusable workflow.
Any actions or reusable workflows stored in the private repository can be used in workflows defined in other private repositories owned by the same organization or user. Actions and reusable workflows stored in private repositories cannot be used in public repositories.
  * If you make a private repository accessible to GitHub Actions workflows in other repositories, outside collaborators on the other repositories can indirectly access the private repository, even though they do not have direct access to these repositories. The outside collaborators can view logs for workflow runs when actions or workflows from the private repository are used.
  * To allow runners to download these actions, GitHub passes a scoped installation token to the runner. This token has read access to the repository, and automatically expires after one hour.


## [Sharing actions and workflows from your private repository](https://docs.github.com/en/actions/sharing-automations/sharing-actions-and-workflows-from-your-private-repository#sharing-actions-and-workflows-from-your-private-repository)
  1. Store the action or reusable workflow in a private repository. For more information, see [About repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories#about-repository-visibility).
  2. Configure the repository to allow access to workflows in other private repositories. For more information, see [Managing GitHub Actions settings for a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#allowing-access-to-components-in-a-private-repository).


## [Further reading](https://docs.github.com/en/actions/sharing-automations/sharing-actions-and-workflows-from-your-private-repository#further-reading)
  * [Reusing workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows)


