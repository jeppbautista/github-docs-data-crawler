  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners "Self-hosted runners")/
  * [Manage self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners "Manage self-hosted runners")/
  * [Remove self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/removing-self-hosted-runners "Remove self-hosted runners")


# Removing self-hosted runners
You can permanently remove a self-hosted runner from a repository or organization.
## In this article
  * [Removing a runner from a repository](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/removing-self-hosted-runners#removing-a-runner-from-a-repository)
  * [Removing a runner from an organization](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/removing-self-hosted-runners#removing-a-runner-from-an-organization)
  * [Removing a runner from an enterprise](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/removing-self-hosted-runners#removing-a-runner-from-an-enterprise)


## [Removing a runner from a repository](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/removing-self-hosted-runners#removing-a-runner-from-a-repository)
  * This procedure permanently removes the self-hosted runner. If you only want to temporarily stop a runner from being assigned jobs, you can either shut down the machine or stop the `run` application. The runner will remain assigned in an "Offline" state, and won't execute any jobs until you restart the runner using the `run` application.
  * A self-hosted runner is automatically removed from GitHub if it has not connected to GitHub Actions for more than 14 days. An ephemeral self-hosted runner is automatically removed from GitHub if it has not connected to GitHub Actions for more than 1 day.
  * Just-in-time (JIT) runners can only run a single job. If JIT runners never run a job, they will automatically be removed. To remove a JIT runner before automatic removal, you must remove the JIT runner on GitHub.


To remove a self-hosted runner from a user repository you must be the repository owner. Organization owners can remove a runner from a repository in the organization.
We recommend that you also have access to the self-hosted runner machine.
For information about how to remove a self-hosted runner with the REST API, see [REST API endpoints for self-hosted runners](https://docs.github.com/en/rest/actions/self-hosted-runners).
Alternatively, if you don't have access to the repository or organization on GitHub to remove a runner, but you would like to re-use the runner machine, then you can delete the `.runner` file inside the self-hosted runner application directory (that is, the directory into which you downloaded and unpacked the runner software). This allows the runner to be registered without having to re-download the self-hosted runner application.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the left sidebar, click **Runners**.
  4. In the list of runners, click on the name of the runner you'd like to configure.
  5. Click **Remove**.
  6. You will see instructions for removing the self-hosted runner. Complete either of the following steps to remove the runner, depending on whether it is still accessible:
     * **If you have access to the runner machine:** Follow the on-screen instructions for your machine's operating system to run the removal command. The instructions include the required URL and an automatically-generated, time-limited token.
The removal command does the following tasks:
       * Removes the runner from GitHub.
       * Removes any self-hosted runner application configuration files on the machine.
       * Removes any services configured if not running in interactive mode.
     * **If you don't have access to the machine:** Click **Force remove this runner** to force GitHub to remove the runner.


## [Removing a runner from an organization](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/removing-self-hosted-runners#removing-a-runner-from-an-organization)
  * This procedure permanently removes the self-hosted runner. If you only want to temporarily stop a runner from being assigned jobs, you can either shut down the machine or stop the `run` application. The runner will remain assigned in an "Offline" state, and won't execute any jobs until you restart the runner using the `run` application.
  * A self-hosted runner is automatically removed from GitHub if it has not connected to GitHub Actions for more than 14 days. An ephemeral self-hosted runner is automatically removed from GitHub if it has not connected to GitHub Actions for more than 1 day.
  * Just-in-time (JIT) runners can only run a single job. If JIT runners never run a job, they will automatically be removed. To remove a JIT runner before automatic removal, you must remove the JIT runner on GitHub.


To remove a self-hosted runner from an organization, you must be an organization owner. We recommend that you also have access to the self-hosted runner machine. For information about how to remove a self-hosted runner with the REST API, see [REST API endpoints for self-hosted runners](https://docs.github.com/en/rest/actions/self-hosted-runners).
Alternatively, if you don't have access to the repository or organization on GitHub to remove a runner, but you would like to re-use the runner machine, then you can delete the `.runner` file inside the self-hosted runner application directory (that is, the directory into which you downloaded and unpacked the runner software). This allows the runner to be registered without having to re-download the self-hosted runner application.
  1. On GitHub, navigate to the main page of the organization.
  2. Under your organization name, click **Settings**.
![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](https://docs.github.com/assets/cb-49309/images/help/discussions/org-settings-global-nav-update.png)
  3. In the left sidebar, click **Runners**.
  4. In the list of runners, click on the name of the runner you'd like to configure.
  5. Click **Remove**.
  6. You will see instructions for removing the self-hosted runner. Complete either of the following steps to remove the runner, depending on whether it is still accessible:
     * **If you have access to the runner machine:** Follow the on-screen instructions for your machine's operating system to run the removal command. The instructions include the required URL and an automatically-generated, time-limited token.
The removal command does the following tasks:
       * Removes the runner from GitHub.
       * Removes any self-hosted runner application configuration files on the machine.
       * Removes any services configured if not running in interactive mode.
     * **If you don't have access to the machine:** Click **Force remove this runner** to force GitHub to remove the runner.


## [Removing a runner from an enterprise](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/removing-self-hosted-runners#removing-a-runner-from-an-enterprise)
If you use GitHub Enterprise Cloud, you can also remove runners from an enterprise. For more information, see the [GitHub Enterprise Cloud documentation](https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-self-hosted-runners/removing-self-hosted-runners#removing-a-runner-from-an-enterprise).
