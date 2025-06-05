  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners "Self-hosted runners")/
  * [Manage self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners "Manage self-hosted runners")/
  * [Add self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/adding-self-hosted-runners "Add self-hosted runners")


# Adding self-hosted runners
You can add a self-hosted runner to a repository, an organization, or an enterprise.
## In this article
  * [Prerequisites](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/adding-self-hosted-runners#prerequisites)
  * [Adding a self-hosted runner to a repository](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/adding-self-hosted-runners#adding-a-self-hosted-runner-to-a-repository)
  * [Adding a self-hosted runner to an organization](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/adding-self-hosted-runners#adding-a-self-hosted-runner-to-an-organization)
  * [Adding a self-hosted runner to an enterprise](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/adding-self-hosted-runners#adding-a-self-hosted-runner-to-an-enterprise)


You can add a self-hosted runner to a repository, an organization, or an enterprise.
If you are an organization or enterprise administrator, you might want to add your self-hosted runners at the organization or enterprise level. This approach makes the runner available to multiple repositories in your organization or enterprise, and also lets you to manage your runners in one place.
We recommend that you only use self-hosted runners with private repositories. This is because forks of your public repository can potentially run dangerous code on your self-hosted runner machine by creating a pull request that executes the code in a workflow.
For more information, see [Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions).
You can set up automation to scale the number of self-hosted runners. For more information, see [Autoscaling with self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/autoscaling-with-self-hosted-runners).
You can register ephemeral runners that perform a single job before the registration is cleaned up by using just-in-time runner registration. For more information, see [Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions#using-just-in-time-runners).
## [Prerequisites](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/adding-self-hosted-runners#prerequisites)
  * You must have access to the machine you will use as a self-hosted runner in your environment.


## [Adding a self-hosted runner to a repository](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/adding-self-hosted-runners#adding-a-self-hosted-runner-to-a-repository)
You can add self-hosted runners to a single repository. To add a self-hosted runner to a user repository, you must be the repository owner. For an organization repository, you must be an organization owner or have admin access to the repository.
For information about how to add a self-hosted runner with the REST API, see [REST API endpoints for self-hosted runners](https://docs.github.com/en/rest/actions/self-hosted-runners).
Organization owners can choose which repositories are allowed to create repository-level self-hosted runners.
For more information, see [Disabling or limiting GitHub Actions for your organization](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#limiting-the-use-of-self-hosted-runners).
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the left sidebar, click **Runners**.
  4. Click **New self-hosted runner**.
  5. Select the operating system image and architecture of your self-hosted runner machine.
![Screenshot of the choice of operating system and architecture. These options are highlighted with a dark orange outline.](https://docs.github.com/assets/cb-35988/images/help/actions/creating-selfhosted-runner.png)
  6. You will see instructions showing you how to download the runner application and install it on your self-hosted runner machine.
Open a shell on your self-hosted runner machine and run each shell command in the order shown.
On Windows, if you want to install the self-hosted runner application as a service, you must open a shell with administrator privileges. We also recommend that you use `C:\actions-runner` as the directory for the self-hosted runner application so that Windows system accounts can access the runner directory.
The instructions walk you through completing these tasks:
     * Downloading and extracting the self-hosted runner application.
     * Running the `config` script to configure the self-hosted runner application and register it with GitHub Actions. The `config` script requires the destination URL and an automatically-generated time-limited token to authenticate the request. The token expires after one hour. 
       * On Windows, the `config` script also asks if you would like to install the self-hosted runner application as a service. For Linux and macOS, you can install a service after you finish adding the runner. For more information, see [Configuring the self-hosted runner application as a service](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/configuring-the-self-hosted-runner-application-as-a-service).
     * Running the self-hosted runner application to connect the machine to GitHub Actions.


### [Checking that your self-hosted runner was successfully added](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/adding-self-hosted-runners#checking-that-your-self-hosted-runner-was-successfully-added)
After completing the steps to add a self-hosted runner, the runner and its status are now listed under "Runners".
The self-hosted runner application must be active for the runner to accept jobs. When the runner application is connected to GitHub and ready to receive jobs, you will see the following message on the machine's terminal.
```
√ Connected to GitHub

2019-10-24 05:45:56Z: Listening for Jobs

```

For more information, see [Monitoring and troubleshooting self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/monitoring-and-troubleshooting-self-hosted-runners).
## [Adding a self-hosted runner to an organization](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/adding-self-hosted-runners#adding-a-self-hosted-runner-to-an-organization)
You can add self-hosted runners at the organization level, where they can be used to process jobs for multiple repositories in an organization. To add a self-hosted runner to an organization, you must be an organization owner. For information about how to add a self-hosted runner with the REST API, see [REST API endpoints for self-hosted runners](https://docs.github.com/en/rest/actions/self-hosted-runners).
  1. On GitHub, navigate to the main page of the organization.
  2. Under your organization name, click **Settings**.
![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](https://docs.github.com/assets/cb-49309/images/help/discussions/org-settings-global-nav-update.png)
  3. In the left sidebar, click **Runners**.
  4. Click **New runner** , then click **New self-hosted runner**.
  5. Select the operating system image and architecture of your self-hosted runner machine.
![Screenshot of the choice of operating system and architecture. These options are highlighted with a dark orange outline.](https://docs.github.com/assets/cb-35988/images/help/actions/creating-selfhosted-runner.png)
  6. You will see instructions showing you how to download the runner application and install it on your self-hosted runner machine.
Open a shell on your self-hosted runner machine and run each shell command in the order shown.
On Windows, if you want to install the self-hosted runner application as a service, you must open a shell with administrator privileges. We also recommend that you use `C:\actions-runner` as the directory for the self-hosted runner application so that Windows system accounts can access the runner directory.
The instructions walk you through completing these tasks:
     * Downloading and extracting the self-hosted runner application.
     * Running the `config` script to configure the self-hosted runner application and register it with GitHub Actions. The `config` script requires the destination URL and an automatically-generated time-limited token to authenticate the request. The token expires after one hour. 
       * On Windows, the `config` script also asks if you would like to install the self-hosted runner application as a service. For Linux and macOS, you can install a service after you finish adding the runner. For more information, see [Configuring the self-hosted runner application as a service](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/configuring-the-self-hosted-runner-application-as-a-service).
     * Running the self-hosted runner application to connect the machine to GitHub Actions.


### [Checking that your self-hosted runner was successfully added](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/adding-self-hosted-runners#checking-that-your-self-hosted-runner-was-successfully-added-1)
After completing the steps to add a self-hosted runner, the runner and its status are now listed under "Runners".
The self-hosted runner application must be active for the runner to accept jobs. When the runner application is connected to GitHub and ready to receive jobs, you will see the following message on the machine's terminal.
```
√ Connected to GitHub

2019-10-24 05:45:56Z: Listening for Jobs

```

For more information, see [Monitoring and troubleshooting self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/monitoring-and-troubleshooting-self-hosted-runners).
For security reasons, public repositories can't use runners in a runner group by default, but you can override this in the runner group's settings. For more information, see [Managing access to self-hosted runners using groups](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups#changing-the-access-policy-of-a-self-hosted-runner-group).
## [Adding a self-hosted runner to an enterprise](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/adding-self-hosted-runners#adding-a-self-hosted-runner-to-an-enterprise)
If you use GitHub Enterprise Cloud, you can add self-hosted runners to an enterprise, where they can be assigned to multiple organizations. The organization owner can control which repositories can use it. For more information, see the [GitHub Enterprise Cloud documentation](https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-self-hosted-runners/adding-self-hosted-runners#adding-a-self-hosted-runner-to-an-enterprise).
