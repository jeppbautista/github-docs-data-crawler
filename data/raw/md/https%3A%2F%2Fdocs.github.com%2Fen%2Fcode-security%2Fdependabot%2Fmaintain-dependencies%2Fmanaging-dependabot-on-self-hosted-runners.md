  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Dependabot](https://docs.github.com/en/code-security/dependabot "Dependabot")/
  * [Maintain dependencies at scale](https://docs.github.com/en/code-security/dependabot/maintain-dependencies "Maintain dependencies at scale")/
  * [Manage Dependabot on self-hosted runners](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/managing-dependabot-on-self-hosted-runners "Manage Dependabot on self-hosted runners")


# Managing Dependabot on self-hosted runners
You can configure self-hosted runners that Dependabot uses to access your private registries and internal network resources.
## Who can use this feature?
Organization owners and repository administrators
## In this article
  * [About Dependabot on GitHub Actions self-hosted runners](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/managing-dependabot-on-self-hosted-runners#about-dependabot-on-github-actions-self-hosted-runners)
  * [Prerequisites](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/managing-dependabot-on-self-hosted-runners#prerequisites)
  * [Configuring self-hosted runners for Dependabot updates](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/managing-dependabot-on-self-hosted-runners#configuring-self-hosted-runners-for-dependabot-updates)
  * [Enabling self-hosted runners for Dependabot updates](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/managing-dependabot-on-self-hosted-runners#enabling-self-hosted-runners-for-dependabot-updates)


## [About Dependabot on GitHub Actions self-hosted runners](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/managing-dependabot-on-self-hosted-runners#about-dependabot-on-github-actions-self-hosted-runners)
If you enable Dependabot on a new repository and have GitHub Actions enabled, Dependabot will run on GitHub Actions by default.
If you enable Dependabot on a new repository and have GitHub Actions disabled, Dependabot will run on the legacy application in GitHub to perform Dependabot updates. This doesn't provide as good performance, visibility, or control of Dependabot updates jobs as GitHub Actions does. If you want to use Dependabot with GitHub Actions, you must ensure that your repository enables GitHub Actions, then enable "Dependabot on Actions runners" from the repository's "Advanced Security" settings page. For more information, see [About Dependabot on GitHub Actions runners](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/about-dependabot-on-github-actions-runners).
Future releases of GitHub will always run Dependabot using GitHub Actions, and you will no longer have the option to enable or disable this setting.
You can help users of your organization and repositories to create and maintain secure code by setting up Dependabot security and version updates. With Dependabot updates, developers can configure repositories so that their dependencies are updated and kept secure automatically. Running Dependabot on GitHub Actions allows for better performance, and increased visibility and control of Dependabot jobs.
Private networking is supported with either an Azure Virtual Network (VNET) or the Actions Runner Controller (ARC) for Dependabot on GitHub Actions. See [Setting up Dependabot to run on self-hosted action runners using the Actions Runner Controller](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-self-hosted-runners-using-arc) and [Setting up Dependabot to run on github-hosted action runners using the Azure Private Network](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-github-hosted-runners-using-vnet) for more information, and instruction.
To have greater control over Dependabot access to your private registries and internal network resources, you can configure Dependabot to run on GitHub Actions self-hosted runners.
For security reasons, when running Dependabot on GitHub Actions self-hosted runners, Dependabot updates will not be run on public repositories.
For more information about configuring Dependabot access to private registries when using GitHub-hosted runners, see [Guidance for the configuration of private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot). For information about which ecosystems are supported as private registries, see [Removing Dependabot access to public registries](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/removing-dependabot-access-to-public-registries).
## [Prerequisites](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/managing-dependabot-on-self-hosted-runners#prerequisites)
You must have Dependabot installed and enabled, and GitHub Actions enabled and in use. The "Dependabot on GitHub Actions Runners" setting for your organization should also be enabled. For more information, see [About Dependabot on GitHub Actions runners](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/about-dependabot-on-github-actions-runners).
Your organization may have configured a policy to restrict actions and self-hosted runners from running in specific repositories, which in turn will not allow Dependabot to run on GitHub Actions self-hosted runners. In this case, the organization or repository level setting to enable "Dependabot on self-hosted runners" will not be visible in the web UI. For more information, see [Disabling or limiting GitHub Actions for your organization](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization).
## [Configuring self-hosted runners for Dependabot updates](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/managing-dependabot-on-self-hosted-runners#configuring-self-hosted-runners-for-dependabot-updates)
After you configure your organization or repository to run Dependabot on GitHub Actions, and before you enable Dependabot on self-hosted runners, you need to configure self-hosted runners for Dependabot updates.
### [System requirements for Dependabot runners](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/managing-dependabot-on-self-hosted-runners#system-requirements-for-dependabot-runners)
Any virtual machine (VM) that you use for Dependabot runners must meet the requirements for self-hosted runners. In addition, they must meet the following requirements.
  * Linux operating system
  * x64 architecture
  * Docker installed with access for the runner users:
    * We recommend installing Docker in rootless mode and configuring the runners to access Docker without `root` privileges.
    * Alternatively, install Docker and give the runner users raised privileges to run Docker.


The CPU and memory requirements will depend on the number of concurrent runners you deploy on a given VM. As guidance, we have successfully set up 20 runners on a single 2 CPU 8GB machine, but ultimately, your CPU and memory requirements will heavily depend on the repositories being updated. Some ecosystems will require more resources than others.
If you specify more than 14 concurrent runners on a VM, you must also update the Docker `/etc/docker/daemon.json` configuration to increase the default number of networks Docker can create.
```
{
  "default-address-pools": [
    {"base":"10.10.0.0/16","size":24}
  ]
}

```

### [Network requirements for Dependabot runners](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/managing-dependabot-on-self-hosted-runners#network-requirements-for-dependabot-runners)
Dependabot runners require access to the public internet, GitHub.com, and any internal registries that will be used in Dependabot updates. To minimize the risk to your internal network, you should limit access from the Virtual Machine (VM) to your internal network. This reduces the potential for damage to internal systems if a runner were to download a hijacked dependency.
You must also allow outbound traffic to `dependabot-actions.githubapp.com` to prevent the jobs for Dependabot security updates from failing. For more information, see [Communicating with self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/communicating-with-self-hosted-runners).
### [Certificate configuration for Dependabot runners](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/managing-dependabot-on-self-hosted-runners#certificate-configuration-for-dependabot-runners)
If Dependabot needs to interact with registries that use self-signed certificates, those certificates must also be installed on the self-hosted runners that run Dependabot jobs. This security hardens the connection. You must also configure Node.js to use the certificate, because most actions are written in JavaScript and run using Node.js, which does not use the operating system certificate store.
### [Adding self-hosted runners for Dependabot updates](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/managing-dependabot-on-self-hosted-runners#adding-self-hosted-runners-for-dependabot-updates)
  1. Provision self-hosted runners, at the repository or organization level. For more information, see [About self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners) and [Adding self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/adding-self-hosted-runners).
  2. Set up the self-hosted runners with the requirements described above. For example, on a VM running Ubuntu 20.04 you would:
     * Install Docker and ensure that the runner users have access to Docker. For more information, see the Docker documentation. 
       * [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
       * Recommended approach: [Run the Docker daemon as a non-root user (Rootless mode)](https://docs.docker.com/engine/security/rootless/)
       * Alternative approach: [Manage Docker as a non-root user](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user)
     * Verify that the runners have access to the public internet and can only access the internal networks that Dependabot needs.
     * Install any self-signed certificates for registries that Dependabot will need to interact with.
  3. Assign a `dependabot` label to each runner you want Dependabot to use. For more information, see [Using labels with self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/using-labels-with-self-hosted-runners#assigning-a-label-to-a-self-hosted-runner).
  4. Optionally, enable workflows triggered by Dependabot to use more than read-only permissions and to have access to any secrets that are normally available. For more information, see [Troubleshooting Dependabot on GitHub Actions](https://docs.github.com/en/code-security/dependabot/troubleshooting-dependabot/troubleshooting-dependabot-on-github-actions#restrictions-when-dependabot-triggers-events).


## [Enabling self-hosted runners for Dependabot updates](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/managing-dependabot-on-self-hosted-runners#enabling-self-hosted-runners-for-dependabot-updates)
Once you have configured self-hosted runners for Dependabot updates, you can enable or disable Dependabot updates on self-hosted runners at the organization or repository level.
Note, disabling and re-enabling the "Dependabot on self-hosted runners" settings will not trigger a new Dependabot run.
### [Enabling or disabling for your repository](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/managing-dependabot-on-self-hosted-runners#enabling-or-disabling-for-your-repository)
You can manage Dependabot on self-hosted runners for your private repository.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Security" section of the sidebar, click 
  4. Under "Dependabot", to the right of "Dependabot on self-hosted runners", click **Enable** to enable the feature or **Disable** to disable it.


### [Enabling or disabling for your organization](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/managing-dependabot-on-self-hosted-runners#enabling-or-disabling-for-your-organization)
You can enable Dependabot on self-hosted runners for all existing private repositories in an organization. Only repositories already configured to run Dependabot on GitHub Actions will be updated to run Dependabot on self-hosted runners the next time a Dependabot job is triggered.
You need to enable self-hosted runners for your organization if you use larger runners. For more information, see [About Dependabot on GitHub Actions runners](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/about-dependabot-on-github-actions-runners#enabling-or-disabling-dependabot-on-larger-runners).
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the "Security" section of the sidebar, click **Global settings**.
  4. Under "Dependabot", select "Dependabot on self-hosted runners" to enable the feature or deselect to disable it. This action enables or disables the feature for all new repositories in the organization.


For more information, see [Configuring global security settings for your organization](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/configuring-global-security-settings-for-your-organization).
