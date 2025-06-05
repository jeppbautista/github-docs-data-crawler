  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Dependabot](https://docs.github.com/en/code-security/dependabot "Dependabot")/
  * [Work with Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot "Work with Dependabot")/
  * [About Dependabot on Actions](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/about-dependabot-on-github-actions-runners "About Dependabot on Actions")


# About Dependabot on GitHub Actions runners
GitHub automatically runs the jobs that generate Dependabot pull requests on GitHub Actions if you have GitHub Actions enabled for the repository. When Dependabot is enabled, these jobs will run by bypassing Actions policy checks and disablement at the repository or organization level.
## Who can use this feature?
Dependabot on GitHub Actions is enabled by default for all repositories for which GitHub Actions is enabled
## In this article
  * [About Dependabot on GitHub Actions runners](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/about-dependabot-on-github-actions-runners#about-dependabot-on-github-actions-runners)
  * [Enabling or disabling Dependabot on GitHub-hosted runners](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/about-dependabot-on-github-actions-runners#enabling-or-disabling-dependabot-on-github-hosted-runners)
  * [Enabling or disabling Dependabot on larger runners](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/about-dependabot-on-github-actions-runners#enabling-or-disabling-dependabot-on-larger-runners)
  * [Managing Dependabot on GitHub Actions runners](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/about-dependabot-on-github-actions-runners#managing-dependabot-on-github-actions-runners)
  * [Further reading](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/about-dependabot-on-github-actions-runners#further-reading)


## [About Dependabot on GitHub Actions runners](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/about-dependabot-on-github-actions-runners#about-dependabot-on-github-actions-runners)
If Dependabot is enabled for a repository, it will always run on GitHub Actions, **bypassing both Actions policy checks and disablement at the repository or organization level**. This ensures that security and version update workflows always run when Dependabot is enabled.
If you enable Dependabot on a new repository and have GitHub Actions enabled, Dependabot will run on GitHub Actions by default.
If you enable Dependabot on a new repository and have GitHub Actions disabled, Dependabot will run on the legacy application in GitHub to perform Dependabot updates. This doesn't provide as good performance, visibility, or control of Dependabot updates jobs as GitHub Actions does. If you want to use Dependabot with GitHub Actions, you must ensure that your repository enables GitHub Actions, then enable "Dependabot on Actions runners" from the repository's "Advanced Security" settings page.
Future releases of GitHub will always run Dependabot using GitHub Actions, and you will no longer have the option to enable or disable this setting.
Using GitHub Actions runners allows you to more easily identify Dependabot job errors and manually detect and troubleshoot failed runs. You can also integrate Dependabot into your CI/CD pipelines by using GitHub Actions APIs and webhooks to detect Dependabot job status such as failed runs, and perform downstream processing. For more information, see [REST API endpoints for GitHub Actions](https://docs.github.com/en/rest/actions) and [Webhook events and payloads](https://docs.github.com/en/webhooks/webhook-events-and-payloads).
Running Dependabot on GitHub-hosted and self-hosted runners **does not** count towards your included GitHub Actions minutes. For more information, see [About billing for GitHub Actions](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions).
You can run Dependabot on GitHub Actions using:
  * GitHub-hosted runners
  * Larger runners. These runners are GitHub-hosted, with advanced features, such as more RAM, CPU, and disk space. For more information, see [Using larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-larger-runners).
  * Self-hosted runners. For more information on assigning a `dependabot` label on self-hosted runners, see [Managing Dependabot on self-hosted runners](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/managing-dependabot-on-self-hosted-runners).


Private networking is supported with either an Azure Virtual Network (VNET) or the Actions Runner Controller (ARC) for Dependabot on GitHub Actions. See [Setting up Dependabot to run on self-hosted action runners using the Actions Runner Controller](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-self-hosted-runners-using-arc) and [Setting up Dependabot to run on github-hosted action runners using the Azure Private Network](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-github-hosted-runners-using-vnet) for more information, and instruction.
Enabling Dependabot on GitHub Actions may increase the number of concurrent jobs run in your account. If required, customers on enterprise plans can request a higher limit for concurrent jobs. For more information, contact us through the [GitHub Support portal](https://support.github.com/), or contact your sales representative.
If you are transitioning to using Dependabot on GitHub Actions runners and you restrict access to your organization's or repository's private resources, you may need to update your list of allowed IP addresses. For example, if you currently limit access to your private resources to the IP addresses that Dependabot uses, you should update your allowlist to use the GitHub-hosted runners IP addresses sourced from the meta API endpoint. For more information, see [REST API endpoints for meta data](https://docs.github.com/en/rest/meta).
Dependabot on GitHub Actions relies on the `ubuntu-latest` label to select the appropriate runner. To ensure Dependabot runs on GitHub-hosted runners, you should not use the label `ubuntu-latest` for self-hosted runners.
## [Enabling or disabling Dependabot on GitHub-hosted runners](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/about-dependabot-on-github-actions-runners#enabling-or-disabling-dependabot-on-github-hosted-runners)
This section only applies to standard GitHub-hosted runners, not larger runners.
New repositories that you create in your user account or in your organization will automatically be configured to run Dependabot on GitHub Actions if any of the following is true:
  * Dependabot is installed and enabled, and GitHub Actions is enabled and in use.
  * The "Dependabot on GitHub Actions runners" setting for your organization is enabled.


For existing repositories, you can opt in to run Dependabot on GitHub Actions as follows.
Future releases of GitHub will remove the ability to disable running Dependabot on GitHub Actions.
If you restrict access to your organization's or repository's private resources, you may need to update your list of allowed IP addresses prior to enabling Dependabot on GitHub Actions runners. You can update your IP allow list to use the GitHub-hosted runners IP addresses (instead of the Dependabot IP addresses), sourced from the [meta](https://docs.github.com/en/rest/meta) REST API endpoint.
You should not rely on the GitHub Actions IP addresses for authentication to private registries. These GitHub Actions addresses are not only used by GitHub, and should not be trusted for authentication. Instead, use a self-hosted runner to ensure greater control over your network access. For more information, see [Managing Dependabot on self-hosted runners](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/managing-dependabot-on-self-hosted-runners).
Note, disabling and re-enabling the "Dependabot on GitHub Actions runners" settings will not trigger a new Dependabot run.
### [Enabling or disabling for your repository](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/about-dependabot-on-github-actions-runners#enabling-or-disabling-for-your-repository)
You can manage Dependabot on GitHub Actions for your public or private repository.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Security" section of the sidebar, click 
  4. Under "Dependabot", to the right of "Dependabot on Actions runners", click **Enable** to enable the feature or **Disable** to disable it.


### [Enabling or disabling for your organization](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/about-dependabot-on-github-actions-runners#enabling-or-disabling-for-your-organization)
You can enable Dependabot on GitHub Actions for all existing repositories in an organization.
Only repositories with the following configuration will be updated to run Dependabot on GitHub Actions the next time a Dependabot job is triggered.
  * Dependabot is enabled in the repository.
  * GitHub Actions is enabled in the repository.


If a repository in your organization has Dependabot enabled but GitHub Actions disabled, Dependabot will not run on GitHub Actions, but will continue to run using the built-in Dependabot application.
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the "Security" section of the sidebar, click **Global settings**.
  4. Under "Dependabot", select "Dependabot on Actions runners" to enable the feature or deselect to disable it.


For more information, see [Configuring global security settings for your organization](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization#enabling-dependency-updates-on-github-actions-runners).
## [Enabling or disabling Dependabot on larger runners](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/about-dependabot-on-github-actions-runners#enabling-or-disabling-dependabot-on-larger-runners)
If you run into Dependabot timeouts and out-of-memory errors, you may want to use larger runners, as you can configure these runners to have more resources.
You can only enable larger runners for Dependabot _at the organization level_. GitHub will bill your organization at the regular Actions runner pricing. For more information, see [About billing for GitHub Actions](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions#per-minute-rates).
  1. Add a larger runner to your organization and ensure the name specified is `dependabot`. For more information, see [Managing larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-larger-runners/managing-larger-runners#adding-a-larger-runner-to-an-organization).
  2. Opt in the organization to self-hosted runners. For more information, see [Managing Dependabot on self-hosted runners](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/managing-dependabot-on-self-hosted-runners#enabling-or-disabling-for-your-organization). This step is required, as it ensures that future Dependabot jobs will run on the larger GitHub-hosted runner that has the `dependabot` name.


## [Managing Dependabot on GitHub Actions runners](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/about-dependabot-on-github-actions-runners#managing-dependabot-on-github-actions-runners)
When a Dependabot on GitHub Actions job is run, you can review the workflow run history directly from the Dependabot job logs. For more information, see [Viewing Dependabot job logs](https://docs.github.com/en/code-security/dependabot/troubleshooting-dependabot/viewing-dependabot-job-logs).
You can also navigate to a Dependabot workflow run from the **Actions** tab in a repository. For more information, see [Viewing workflow run history](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/viewing-workflow-run-history).
To re-run a Dependabot version updates or Dependabot security updates job, use the appropriate procedure below. You cannot re-run a Dependabot job on GitHub Actions as you would for other GitHub Actions workflows and jobs, that is, by using the **Actions** tab in a repository. You cannot view usage data for Dependabot updates workflows and jobs in your organization's GitHub Actions usage metrics.
### [Re-running a Dependabot version updates job](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/about-dependabot-on-github-actions-runners#re-running-a-dependabot-version-updates-job)
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the main page of a repository. In the horizontal navigation bar, a tab, labeled with a graph icon and "Insights," is outlined in orange.](https://docs.github.com/assets/cb-52175/images/help/repository/repo-nav-insights-tab.png)
  3. In the left sidebar, click **Dependency graph**. 
![Screenshot of the "Dependency graph" tab. The tab is highlighted with an orange outline.](https://docs.github.com/assets/cb-3959/images/help/graphs/graphs-sidebar-dependency-graph.png)
  4. Under "Dependency graph", click **Dependabot**.
  5. To the right of the name of manifest file that you're interested in, click **Recent update jobs**.
  6. To the right of the affected manifest file, click **Check for updates** to re-run a Dependabot version updates job and check for new updates to dependencies for that ecosystem.


### [Re-running a Dependabot security updates job](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/about-dependabot-on-github-actions-runners#re-running-a-dependabot-security-updates-job)
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
  3. In the left sidebar, under "Vulnerability alerts", click **Dependabot**.
  4. Under "Dependabot", click the alert you want to view.
  5. In the section displaying the error details for the alert, click **Try again** to re-run the Dependabot security updates job.


## [Further reading](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/about-dependabot-on-github-actions-runners#further-reading)
  * [Troubleshooting Dependabot on GitHub Actions](https://docs.github.com/en/code-security/dependabot/troubleshooting-dependabot/troubleshooting-dependabot-on-github-actions)


