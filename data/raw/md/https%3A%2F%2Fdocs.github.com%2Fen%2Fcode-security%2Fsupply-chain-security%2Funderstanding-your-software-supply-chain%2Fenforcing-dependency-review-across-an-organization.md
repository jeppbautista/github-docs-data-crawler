  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Supply chain security](https://docs.github.com/en/code-security/supply-chain-security "Supply chain security")/
  * [Understand your supply chain](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain "Understand your supply chain")/
  * [Enforce dependency review](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/enforcing-dependency-review-across-an-organization "Enforce dependency review")


# Enforcing dependency review across an organization
Dependency review lets you catch insecure dependencies before you introduce them to your environment. You can enforce the use of the dependency review action across your organization.
## Who can use this feature?
Organization owners, security managers, and organization members with the **admin** role
## In this article
  * [About dependency review enforcement](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/enforcing-dependency-review-across-an-organization#about-dependency-review-enforcement)
  * [Prerequisites](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/enforcing-dependency-review-across-an-organization#prerequisites)
  * [Enforcing dependency review for your organization](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/enforcing-dependency-review-across-an-organization#enforcing-dependency-review-for-your-organization)


## [About dependency review enforcement](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/enforcing-dependency-review-across-an-organization#about-dependency-review-enforcement)
The "dependency review action" refers to the specific action that can report on differences in a pull request within the GitHub Actions context. See [`dependency-review-action`](https://github.com/actions/dependency-review-action). You can use the dependency review action in your repository to enforce dependency reviews on your pull requests. The action scans for vulnerable versions of dependencies introduced by package version changes in pull requests, and warns you about the associated security vulnerabilities. This gives you better visibility of what's changing in a pull request, and helps prevent vulnerabilities being added to your repository. For more information, see [About dependency review](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review#about-the-dependency-review-action).
You can enforce the use of the dependency review action in your organization by setting up a repository ruleset that will require the `dependency-review-action` workflow to pass before pull requests can be merged. Repository rulesets are rule settings that allow you to control how users can interact with selected branches and tags in your repositories. For more information, see [About rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets) and [Require workflows to pass before merging](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-workflows-to-pass-before-merging).
## [Prerequisites](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/enforcing-dependency-review-across-an-organization#prerequisites)
You need to add the dependency review action to one of the repositories in your organization, and configure the action. For more information, see [Configuring the dependency review action](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-review-action).
## [Enforcing dependency review for your organization](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/enforcing-dependency-review-across-an-organization#enforcing-dependency-review-for-your-organization)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the left sidebar, in the "Code, planning, and automation" section, click **Rulesets**.
![Screenshot of an organization's settings page. In the sidebar, a link labeled "Rulesets" is outlined in orange.](https://docs.github.com/assets/cb-32436/images/help/organizations/sidebar-repository-rulesets.png)
  4. Click the **New ruleset** dropdown menu, and select **New branch ruleset**.
  5. To help identify your ruleset and clarify its purpose, give the ruleset a name in **Ruleset Name**.
  6. Set **Enforcement status** to 
  7. Optionally, you can target specific repositories in your organization. For more information, see [Choosing which repositories to target in your organization](https://docs.github.com/en/organizations/managing-organization-settings/creating-rulesets-for-repositories-in-your-organization#choosing-which-repositories-to-target-in-your-organization).
  8. In the "Rules" section, select the "Require workflows to pass before merging" option.
  9. In "Workflow configurations", click **Add workflow**.
  10. In the dialog, select the repository that you added the dependency review action to. For more information, see [Prerequisites](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/enforcing-dependency-review-across-an-organization#prerequisites).
  11. Select a branch and the workflow file for dependency review in the enhanced dialog.
![Screenshot of the Add required workflow dialog. You need to specify a repository, branch, and workflow.](https://docs.github.com/assets/cb-117046/images/help/repository/add-required-workflow-dialog.png)
  12. Click **Create**.


