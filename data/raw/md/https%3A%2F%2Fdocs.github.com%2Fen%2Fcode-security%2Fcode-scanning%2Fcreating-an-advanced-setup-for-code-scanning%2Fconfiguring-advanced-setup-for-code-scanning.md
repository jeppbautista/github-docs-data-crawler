  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Create advanced setup](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning "Create advanced setup")/
  * [Configure advanced setup](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning "Configure advanced setup")


# Configuring advanced setup for code scanning
You can configure advanced setup for a repository to find security vulnerabilities in your code using a highly customizable code scanning configuration.
## Who can use this feature?
Repository owners, organization owners, security managers, and users with the **admin** role
Code scanning is available for the following repository types:
  * Public repositories on GitHub.com
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [About advanced setup for code scanning](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning#about-advanced-setup-for-code-scanning)
  * [Configuring advanced setup for code scanning with CodeQL](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning#configuring-advanced-setup-for-code-scanning-with-codeql)
  * [Configuring code scanning using third-party actions](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning#configuring-code-scanning-using-third-party-actions)
  * [Next steps](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning#next-steps)


## [About advanced setup for code scanning](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning#about-advanced-setup-for-code-scanning)
Advanced setup for code scanning is helpful when you need to customize your code scanning. By creating and editing a workflow file, you can define how to build compiled languages, choose which queries to run, select the languages to scan, use a matrix build, and more. You also have access to all the options for controlling workflows, for example: changing the scan schedule, defining workflow triggers, specifying specialist runners to use. For more information about GitHub Actions workflows, see [About workflows](https://docs.github.com/en/actions/using-workflows/about-workflows).
You can also configure code scanning with third-party tools. For more information, see [Configuring code scanning using third-party actions](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning#configuring-code-scanning-using-third-party-actions).
If you run code scanning using multiple configurations, an alert will sometimes have multiple analysis origins. If an alert has multiple analysis origins, you can view the status of the alert for each analysis origin on the alert page. For more information, see [About code scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts#about-analysis-origins).
If you do not need a highly customizable code scanning configuration, consider using default setup for code scanning. For more information on eligibility for default setup, see [Configuring default setup for code scanning](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning#requirements-for-using-default-setup).
### [Prerequisites](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning#prerequisites)
Your repository is eligible for advanced setup if it meets these requirements.
  * It uses CodeQL-supported languages or you plan to generate code scanning results with a third-party tool.
  * GitHub Actions are enabled.
  * It is publicly visible, or GitHub Code Security is enabled.


## [Configuring advanced setup for code scanning with CodeQL](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning#configuring-advanced-setup-for-code-scanning-with-codeql)
You can customize your CodeQL analysis by creating and editing a workflow file. Selecting advanced setup generates a basic workflow file for you to customize using standard workflow syntax and specifying options for the CodeQL action. See [About workflows](https://docs.github.com/en/actions/using-workflows/about-workflows) and [Customizing your advanced setup for code scanning](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/customizing-your-advanced-setup-for-code-scanning).
Using actions to run code scanning will use minutes. For more information, see [About billing for GitHub Actions](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions).
You can configure code scanning for any public repository where you have write access.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Security" section of the sidebar, click 
  4. Scroll down to "Code Security", in the "CodeQL analysis" row select **Set up** **Advanced**.
If you are switching from default setup to advanced setup, in the "CodeQL analysis" row, select **Disable CodeQL**.
![Screenshot of the "Code Security" section of "Advanced Security" settings. The "Advanced setup" button is highlighted with an orange outline.](https://docs.github.com/assets/cb-92287/images/help/security/advanced-code-scanning-setup.png)
  5. To customize how code scanning scans your code, edit the workflow.
Generally, you can commit the CodeQL analysis workflow without making any changes to it. However, many of the third-party workflows require additional configuration, so read the comments in the workflow before committing.
For more information, see [Customizing your advanced setup for code scanning](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/customizing-your-advanced-setup-for-code-scanning) and [CodeQL code scanning for compiled languages](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages).
  6. Click **Commit changes...** to display the commit changes form.
![Screenshot of the form to create a new file. To the right of the file name, a green button, labeled "Commit changes...", is outlined in dark orange.](https://docs.github.com/assets/cb-72018/images/help/repository/start-commit-commit-new-file.png)
  7. In the commit message field, type a commit message.
  8. Choose whether you'd like to commit directly to the default branch, or create a new branch and start a pull request.
  9. Click **Commit new file** to commit the workflow file to the default branch or click **Propose new file** to commit the file to a new branch.
  10. If you created a new branch, click **Create pull request** and open a pull request to merge your change into the default branch.


In the suggested CodeQL analysis workflow, code scanning is configured to analyze your code each time you either push a change to the default branch or any protected branches, or raise a pull request against the default branch. As a result, code scanning will now commence.
The `on:pull_request` and `on:push` triggers for code scanning are each useful for different purposes. See [Customizing your advanced setup for code scanning](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/customizing-your-advanced-setup-for-code-scanning#configuring-frequency) and [Triggering a workflow](https://docs.github.com/en/actions/using-workflows/triggering-a-workflow).
For information on bulk enablement, see [Configuring advanced setup for code scanning with CodeQL at scale](https://docs.github.com/en/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/configuring-advanced-setup-for-code-scanning-with-codeql-at-scale).
## [Configuring code scanning using third-party actions](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning#configuring-code-scanning-using-third-party-actions)
GitHub includes workflow templates for third-party actions, as well as the CodeQL action. Using a workflow template is much easier than writing a workflow unaided.
Using actions to run code scanning will use minutes. For more information, see [About billing for GitHub Actions](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions).
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the tabs for the "github/docs" repository. The "Actions" tab is highlighted with an orange outline.](https://docs.github.com/assets/cb-12958/images/help/repository/actions-tab-global-nav-update.png)
  3. If the repository has already at least one workflow configured and running, click **New workflow** to display workflow templates. If there are currently no workflows configured for the repository, go to the next step.
![Screenshot of the Actions tab for a repository. The "New workflow" button is outlined in dark orange.](https://docs.github.com/assets/cb-41859/images/help/security/actions-new-workflow-button.png)
  4. In the "Choose a workflow" or "Get started with GitHub Actions" view, scroll down to the "Security" category and click **Configure** under the workflow you want to configure. You may need to click **View all** to find the security workflow you want to configure.
![Screenshot of the Security category of workflow templates. The Configure button and "View all" link are highlighted with an orange outline.](https://docs.github.com/assets/cb-41796/images/help/security/actions-workflows-security-section.png)
  5. Follow any instructions in the workflow to customize it to your needs. For more general assistance about workflows, click **Documentation** on the right pane of the workflow page.
![Screenshot showing a workflow template file open for editing. The "Documentation" button is highlighted with an orange outline.](https://docs.github.com/assets/cb-58384/images/help/security/actions-workflows-documentation.png)
  6. When you have finished defining your configuration, add the new workflow to your default branch.
For more information, see [Using workflow templates](https://docs.github.com/en/actions/learn-github-actions/using-starter-workflows#choosing-and-using-a-starter-workflow) and [Customizing your advanced setup for code scanning](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/customizing-your-advanced-setup-for-code-scanning).


## [Next steps](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning#next-steps)
After your workflow runs successfully at least once, you are ready to start examining and resolving code scanning alerts. For more information on code scanning alerts, see [About code scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts) and [Assessing code scanning alerts for your repository](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository).
Learn how code scanning runs behave as checks on pull requests, see [Triaging code scanning alerts in pull requests](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/triaging-code-scanning-alerts-in-pull-requests#about-code-scanning-as-a-pull-request-check).
You can find detailed information about your code scanning configuration, including timestamps for each scan and the percentage of files scanned, on the tool status page. For more information, see [About the tool status page for code scanning](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/about-the-tool-status-page).
### [Further reading](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning#further-reading)
  * [Triaging code scanning alerts in pull requests](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/triaging-code-scanning-alerts-in-pull-requests).
  * [Configuring notifications](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications#github-actions-notification-options).
  * [Customizing your advanced setup for code scanning](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/customizing-your-advanced-setup-for-code-scanning).
  * [Viewing code scanning logs](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/viewing-code-scanning-logs).


