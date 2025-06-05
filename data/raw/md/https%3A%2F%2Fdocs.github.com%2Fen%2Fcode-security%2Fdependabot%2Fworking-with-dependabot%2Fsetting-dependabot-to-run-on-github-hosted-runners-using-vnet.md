  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Dependabot](https://docs.github.com/en/code-security/dependabot "Dependabot")/
  * [Work with Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot "Work with Dependabot")/
  * [Configure VNET](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-github-hosted-runners-using-vnet "Configure VNET")


# Setting up Dependabot to run on github-hosted action runners using the Azure Private Network
You can configure an Azure Virtual Network (VNET) to run Dependabot on GitHub-hosted runners.
## Who can use this feature?
Users with **write** access
## In this article
  * [Configuring VNET for Dependabot updates](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-github-hosted-runners-using-vnet#configuring-vnet-for-dependabot-updates)
  * [Configuring Azure resources](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-github-hosted-runners-using-vnet#configuring-azure-resources)
  * [Configuring a VNET-injected runner for Dependabot updates in your enterprise](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-github-hosted-runners-using-vnet#configuring-a-vnet-injected-runner-for-dependabot-updates-in-your-enterprise)
  * [Enabling Dependabot for the organization](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-github-hosted-runners-using-vnet#enabling-dependabot-for-the-organization)
  * [Triggering a Dependabot run](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-github-hosted-runners-using-vnet#triggering-a-dependabot-run)
  * [Checking logs and active jobs for Dependabot updates](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-github-hosted-runners-using-vnet#checking-logs-and-active-jobs-for-dependabot-updates)
  * [Configuring Azure VNET firewall IP rules](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-github-hosted-runners-using-vnet#configuring-azure-vnet-firewall-ip-rules)


## [Configuring VNET for Dependabot updates](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-github-hosted-runners-using-vnet#configuring-vnet-for-dependabot-updates)
This article provides step-by-step instructions for running Dependabot on GitHub-hosted runners configured with VNET. The article explains:
  * How to create runner groups for your enterprise or organization with a VNET configuration.
  * How to create GitHub-hosted runners for Dependabot in the runner group.
  * How to enable Dependabot on large runners.
  * How to configure Azure VNET firewall IP rules.


To use GitHub-hosted runners with Azure VNET, you first need to configure your Azure resources, then create a private network configuration in GitHub.
## [Configuring Azure resources](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-github-hosted-runners-using-vnet#configuring-azure-resources)
To learn how to use GitHub-hosted runners with an Azure private network, see [Configuring your Azure resources](https://docs.github.com/en/enterprise-cloud@latest/admin/configuring-settings/configuring-private-networking-for-hosted-compute-products/configuring-private-networking-for-github-hosted-runners-in-your-enterprise#configuring-your-azure-resources).
  * The `databaseId` which is required in the script for configuring the Azure resources can refer to any of the following depending on whether you are configuring the resources for an enterprise or an organization:
  * The enterprise slug, which you can identify by looking at the URL for your enterprise, `https://github.com/enterprises/SLUG`, or
  * The login for the organization account, which you can identify by looking at the URL for your organization, `https://github.com/organizations/ORGANIZATION_LOGIN`.
  * The script will return the full payload for the created resource. The `GitHubId` hash value returned in the payload for the created resource is the network settings resource ID you will use in the next steps while setting up a network configuration in GitHub


## [Configuring a VNET-injected runner for Dependabot updates in your enterprise](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-github-hosted-runners-using-vnet#configuring-a-vnet-injected-runner-for-dependabot-updates-in-your-enterprise)
After configuring your Azure resources, you can use an Azure Virtual Network (VNET) for private networking by creating a network configuration at the organization level. Then, you can associate that network configuration to runner groups.
  1. Add a new network configuration for your enterprise. See [Add a new network configuration for your enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/configuring-settings/configuring-private-networking-for-hosted-compute-products/configuring-private-networking-for-github-hosted-runners-in-your-enterprise#1-add-a-new-network-configuration-for-your-enterprise)
  2. Create a runner group for the enterprise and select the organizations that you want to run Dependabot updates for. See [Create a runner group for your enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/configuring-settings/configuring-private-networking-for-hosted-compute-products/configuring-private-networking-for-github-hosted-runners-in-your-enterprise#2-create-a-runner-group-for-your-enterprise)
  3. Create and add a GitHub-hosted runner to the enterprise runner group. See [Adding a larger runner to an enterprise](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/managing-larger-runners#adding-a-larger-runner-to-an-enterprise). Important points are as follows: 
     * The runner name must be **dependabot**
     * Choose a Linux x64 platform.
     * Select the suitable Ubuntu version.
     * When adding your GitHub-hosted runner to a runner group, select the runner group you created in the previous step.
Naming the GitHub-hosted runner **dependabot** assigns the **dependabot** label to the runner, which enables it to pick up jobs triggered by Dependabot on actions.


## [Enabling Dependabot for the organization](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-github-hosted-runners-using-vnet#enabling-dependabot-for-the-organization)
You now need to enable Dependabot on _self-hosted runners_ for your organization in order to enable Dependabot on large runners. See [Enabling or disabling Dependabot on larger runners](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/about-dependabot-on-github-actions-runners#enabling-or-disabling-dependabot-on-larger-runners).
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Under your organization name, click **Settings**.
![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](https://docs.github.com/assets/cb-49309/images/help/discussions/org-settings-global-nav-update.png)
  3. In the "Security" section of the sidebar, select the **Advanced Security** dropdown menu, then click **Global settings**.
  4. Under **Dependabot** , select **Dependabot on self-hosted runners**. This step is required, as it ensures that future Dependabot jobs will run on the larger GitHub-hosted runner that has the `dependabot` name.


## [Triggering a Dependabot run](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-github-hosted-runners-using-vnet#triggering-a-dependabot-run)
Now that you've set up private networking with VNET, you can start a Dependabot run.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click the 
  3. In the left sidebar, click **Dependency graph**. 
![Screenshot of the "Dependency graph" tab. The tab is highlighted with an orange outline.](https://docs.github.com/assets/cb-3959/images/help/graphs/graphs-sidebar-dependency-graph.png)
  4. Under "Dependency graph", click **Dependabot**.
  5. To the right of the name of manifest file you're interested in, click **Recent update jobs**.
  6. If there are no recent update jobs for the manifest file, click **Check for updates** to re-run a Dependabot version updates'job and check for new updates to dependencies for that ecosystem.


## [Checking logs and active jobs for Dependabot updates](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-github-hosted-runners-using-vnet#checking-logs-and-active-jobs-for-dependabot-updates)
  * You can view the logs of the Dependabot workflow in the **Actions** tab of your repository. Ensure you select the Dependabot job on the left sidebar of the Actions page.
![Example of log for a "Dependabot in vnet" workflow. The Dependabot job is highlighted with an orange outline. ](https://docs.github.com/assets/cb-400297/images/help/dependabot/dependabot-vnet-logs.png)
  * You can view the active jobs in the page containing informatuon about the runner. To access that page, click the **Policies** tab for the enterprise, select **Actions** on the left sidebar, click the **Runner group** tab, and select your runner.
![Screenshot showing a Dependabot runner's active jobs.](https://docs.github.com/assets/cb-462465/images/help/dependabot/dependabot-vnet-active-jobs.png)


## [Configuring Azure VNET firewall IP rules](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-github-hosted-runners-using-vnet#configuring-azure-vnet-firewall-ip-rules)
If your Azure VNET environment is configured with a firewall with an IP allowlist, you may need to update your list of allowed IP addresses to use the GitHub-hosted runners IP addresses sourced from the meta API endpoint.
  * GitHub provides the following public endpoint for its IP ranges:
> GET <https://api.github.com/meta>
  * Copy and paste the following curl command in your terminal or command prompt and replace the placeholder bearer token value with your actual value.
Bash```
      curl -L \
      -H "Accept: application/vnd.github+json" \
      -H "Authorization: Bearer YOUR-TOKEN" \
      -H "X-GitHub-Api-Version: 2022-11-28" \
      https://api.github.com/meta

```
```
      curl -L \
      -H "Accept: application/vnd.github+json" \
      -H "Authorization: Bearer YOUR-TOKEN" \
      -H "X-GitHub-Api-Version: 2022-11-28" \
      https://api.github.com/meta

```

  * From the response, look for the **actions** key.
```
    "actions": [ ... ]

```

These are the IP ranges used by GitHub Actions runners, including Dependabot and hosted runners.
  * Add these IPs to your firewall allowlist.


