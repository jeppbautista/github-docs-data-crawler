  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Write workflows](https://docs.github.com/en/actions/writing-workflows "Write workflows")/
  * [Use workflow templates](https://docs.github.com/en/actions/writing-workflows/using-workflow-templates "Use workflow templates")


# Using workflow templates
GitHub provides workflow templates for a variety of languages and tooling.
## In this article
  * [About workflow templates](https://docs.github.com/en/actions/writing-workflows/using-workflow-templates#about-workflow-templates)
  * [Choosing and using a workflow template](https://docs.github.com/en/actions/writing-workflows/using-workflow-templates#choosing-and-using-a-workflow-template)
  * [Further reading](https://docs.github.com/en/actions/writing-workflows/using-workflow-templates#further-reading)


## [About workflow templates](https://docs.github.com/en/actions/writing-workflows/using-workflow-templates#about-workflow-templates)
Workflow templates are templates that help you to create your own GitHub Actions workflows for a repository. They offer an alternative to starting from a blank workflow file and are useful because some of the work will already have been done for you.
GitHub offers workflow templates for a variety of languages and tooling. When you set up workflows in your repository, GitHub analyzes the code in your repository and recommends workflows based on the language and framework in your repository. For example, if you use Node.js, GitHub will suggest a workflow template file that installs your Node.js packages and runs your tests. You can search and filter to find relevant workflow templates.
GitHub provides ready-to-use workflow templates for the following high level categories:
  * **Deployment (CD)**. For more information, see [About continuous deployment with GitHub Actions](https://docs.github.com/en/actions/deployment/about-deployments/about-continuous-deployment).


  * **Security**. For more information, see [Configuring advanced setup for code scanning](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning#configuring-code-scanning-using-third-party-actions).


  * **Continuous Integration (CI)**. For more information, see [About continuous integration with GitHub Actions](https://docs.github.com/en/actions/automating-builds-and-tests/about-continuous-integration).
  * **Automation**. Automation workflow templates offer solutions for automating workflows, such as triaging pull requests and applying a label based on the paths that are modified in the pull request, or greeting users who are first time contributors to the repository.


Use these workflows as a starting place to build your custom workflow or use them as-is. You can browse the full list of workflow templates in the [actions/starter-workflows](https://github.com/actions/starter-workflows) repository. For more information, see [Using workflow templates](https://docs.github.com/en/actions/writing-workflows/using-starter-workflows).
You can also create your own workflow template to share with your organization. These workflow templates will appear alongside the GitHub-provided workflow templates. Anyone with write access to the organization's `.github` repository can set up a workflow template. For more information, see [Creating workflow templates for your organization](https://docs.github.com/en/actions/using-workflows/creating-starter-workflows-for-your-organization).
## [Choosing and using a workflow template](https://docs.github.com/en/actions/writing-workflows/using-workflow-templates#choosing-and-using-a-workflow-template)
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the tabs for the "github/docs" repository. The "Actions" tab is highlighted with an orange outline.](https://docs.github.com/assets/cb-12958/images/help/repository/actions-tab-global-nav-update.png)
  3. If you already have a workflow in your repository, click **New workflow**.
  4. The "Choose a workflow" page shows a selection of recommended workflow templates. Find the workflow template that you want to use, then click **Configure**. To help you find the workflow template that you want, you can search for keywords or filter by category.
  5. If the workflow template contains comments detailing additional setup steps, follow these steps.
There are guides to accompany many of the workflow templates for building and testing projects. For more information, see [Building and testing](https://docs.github.com/en/actions/automating-builds-and-tests).
  6. Some workflow templates use secrets. For example, `${{ secrets.npm_token }}`. If the workflow template uses a secret, store the value described in the secret name as a secret in your repository. For more information, see [Using secrets in GitHub Actions](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions).
  7. Optionally, make additional changes. For example, you might want to change the value of `on` to change when the workflow runs.
  8. Click **Start commit**.
  9. Write a commit message and decide whether to commit directly to the default branch or to open a pull request.


## [Further reading](https://docs.github.com/en/actions/writing-workflows/using-workflow-templates#further-reading)
  * [About continuous integration with GitHub Actions](https://docs.github.com/en/actions/automating-builds-and-tests/about-continuous-integration)
  * [Managing workflow runs and deployments](https://docs.github.com/en/actions/managing-workflow-runs)
  * [Monitoring and troubleshooting workflows](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/about-monitoring-and-troubleshooting)
  * [Managing billing for GitHub Actions](https://docs.github.com/en/billing/managing-billing-for-github-actions)


