  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Administer GitHub Actions](https://docs.github.com/en/actions/administering-github-actions "Administer GitHub Actions")/
  * [Share workflows with your organization](https://docs.github.com/en/actions/administering-github-actions/sharing-workflows-secrets-and-runners-with-your-organization "Share workflows with your organization")


# Sharing workflows, secrets, and runners with your organization
Learn how you can use organization features to collaborate with your team, by sharing workflow templates, secrets, variables, and self-hosted runners.
## In this article
  * [Overview](https://docs.github.com/en/actions/administering-github-actions/sharing-workflows-secrets-and-runners-with-your-organization#overview)
  * [Sharing workflows](https://docs.github.com/en/actions/administering-github-actions/sharing-workflows-secrets-and-runners-with-your-organization#sharing-workflows)
  * [Sharing secrets and variables within an organization](https://docs.github.com/en/actions/administering-github-actions/sharing-workflows-secrets-and-runners-with-your-organization#sharing-secrets-and-variables-within-an-organization)
  * [Share self-hosted runners within an organization](https://docs.github.com/en/actions/administering-github-actions/sharing-workflows-secrets-and-runners-with-your-organization#share-self-hosted-runners-within-an-organization)
  * [Next steps](https://docs.github.com/en/actions/administering-github-actions/sharing-workflows-secrets-and-runners-with-your-organization#next-steps)


## [Overview](https://docs.github.com/en/actions/administering-github-actions/sharing-workflows-secrets-and-runners-with-your-organization#overview)
If you need to share workflows and other GitHub Actions features with your team, then consider collaborating within a GitHub organization. An organization allows you to centrally store and manage secrets, artifacts, and self-hosted runners. You can also create workflow templates in the `.github` repository and share them with other users in your organization.
## [Sharing workflows](https://docs.github.com/en/actions/administering-github-actions/sharing-workflows-secrets-and-runners-with-your-organization#sharing-workflows)
Your organization can share workflows by reusing the workflows exactly or by creating workflow templates
### [Reusing workflows](https://docs.github.com/en/actions/administering-github-actions/sharing-workflows-secrets-and-runners-with-your-organization#reusing-workflows)
You can call one workflow from within another workflow. This allows you to reuse workflows, avoiding duplication and making your workflows easier to maintain. For more information, see [Reusing workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows).
### [Using workflow templates](https://docs.github.com/en/actions/administering-github-actions/sharing-workflows-secrets-and-runners-with-your-organization#using-workflow-templates)
Workflow templates allow everyone in your organization who has permission to create workflows to do so more quickly and easily. When you create a new workflow, you can choose a workflow template and some or all of the work of writing the workflow will be done for you. You can use workflow templates as a starting place to build your custom workflow or use them as-is. This not only saves time, it promotes consistency and best practice across your organization. For more information, see [Creating workflow templates for your organization](https://docs.github.com/en/actions/using-workflows/creating-starter-workflows-for-your-organization).
## [Sharing secrets and variables within an organization](https://docs.github.com/en/actions/administering-github-actions/sharing-workflows-secrets-and-runners-with-your-organization#sharing-secrets-and-variables-within-an-organization)
You can centrally manage your secrets and variables within an organization, and then make them available to selected repositories. This also means that you can update a secret or variable in one location, and have the change apply to all repository workflows that use it.
When creating a secret or variable in an organization, you can use a policy to limit which repositories can access it. For example, you can grant access to all repositories, or limit access to only private repositories or a specified list of repositories.
Organization owners can create secrets or variables at the organization level.
  1. On GitHub, navigate to the main page of the organization.
  2. Under your organization name, click **Settings**.
![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](https://docs.github.com/assets/cb-49309/images/help/discussions/org-settings-global-nav-update.png)
  3. In the "Security" section of the sidebar, select **Actions**.
  4. Click the **Secrets** or **Variables** tab, and create the secret or variable with your desired values and options.
For more information, see [Using secrets in GitHub Actions](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-an-organization) or [Store information in variables](https://docs.github.com/en/actions/learn-github-actions/variables#creating-configuration-variables-for-an-organization).


## [Share self-hosted runners within an organization](https://docs.github.com/en/actions/administering-github-actions/sharing-workflows-secrets-and-runners-with-your-organization#share-self-hosted-runners-within-an-organization)
Organization owners can add their self-hosted runners to groups, and then create policies that control which repositories can access the group.
For more information, see [Managing access to self-hosted runners using groups](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups).
## [Next steps](https://docs.github.com/en/actions/administering-github-actions/sharing-workflows-secrets-and-runners-with-your-organization#next-steps)
To continue learning about GitHub Actions, see [Creating workflow templates for your organization](https://docs.github.com/en/actions/using-workflows/creating-starter-workflows-for-your-organization).
