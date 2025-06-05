  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [GitHub-hosted runners](https://docs.github.com/en/actions/using-github-hosted-runners "GitHub-hosted runners")/
  * [Using larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners "Using larger runners")/
  * [Manage larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/managing-larger-runners "Manage larger runners")


# Managing larger runners
You can configure larger runners for your organization or enterprise.
## Who can use this feature?
Larger runners are only available for organizations and enterprises using the GitHub Team or GitHub Enterprise Cloud plans.  
  
Enterprise or organization owners can manage larger runners.
## In this article
  * [Adding a larger runner to an organization](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/managing-larger-runners#adding-a-larger-runner-to-an-organization)
  * [Allowing repositories to access larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/managing-larger-runners#allowing-repositories-to-access-larger-runners)
  * [Changing the name of a larger runner](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/managing-larger-runners#changing-the-name-of-a-larger-runner)
  * [Changing the size of a larger runner](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/managing-larger-runners#changing-the-size-of-a-larger-runner)
  * [Changing the image of a larger runner](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/managing-larger-runners#changing-the-image-of-a-larger-runner)
  * [Configuring autoscaling for larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/managing-larger-runners#configuring-autoscaling-for-larger-runners)
  * [Creating static IP addresses for larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/managing-larger-runners#creating-static-ip-addresses-for-larger-runners)


  * The information and instructions in this article only apply to larger runners with Linux and Windows operating systems.


## [Adding a larger runner to an organization](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/managing-larger-runners#adding-a-larger-runner-to-an-organization)
Organization owners can add a larger runner to an organization control which repositories can use it. When you create a new runner for an organization, by default, all repositories in the organization have access to the runner. To limit which repositories can use the runner, assign it to a runner group with access to specific repositories. For more information, see [Allowing repositories to access larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/managing-larger-runners#allowing-repositories-to-access-larger-runners).
You can choose an operating system and a hardware configuration from the list of available options. When new instances of this runner are deployed through autoscaling, they'll use the same operating system and hardware configuration you've defined here.
New runners are automatically assigned to the default group, or you can choose which group the runners must join during the runner creation process. In addition, you can modify the runner's group membership after you've registered the runner. For more information, see [Controlling access to larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/controlling-access-to-larger-runners).
  1. On GitHub, navigate to the main page of the organization.
  2. Under your organization name, click **Settings**.
![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](https://docs.github.com/assets/cb-49309/images/help/discussions/org-settings-global-nav-update.png)
  3. In the left sidebar, click **Runners**.
  4. Click **New runner** , then click 
  5. Complete the required details to configure your new runner:
     * **Name:** Enter a name for your new runner. For easier identification, this should indicate its hardware and operating configuration, such as `ubuntu-20.04-16core`.
     * **Platform:** Choose a platform from the available options. Once you've selected a platform, you will be able to choose a specific image.
     * **Image:** Choose an image from the available options. Once you've selected an image, you will be able to choose a specific size.
       * **GitHub-owned:** For images managed by GitHub, select an image under this tab.
       * **Partner:** For images managed by a partner, select an image under this tab. ex: Base Windows 11 desktop, GPU-optimized, and arm64 images are located under this tab.
     * **Size:** Choose a hardware configuration from the list of available options. The available sizes depend on the image that you selected in a previous step. For GPU runners, select a size under the **GPU-powered** tab.
     * **Maximum concurrency:** Choose the maximum number of jobs that can be active at any time.
     * **Runner group:** Choose the group that your runner will be a member of. This group will host multiple instances of your runner, as they scale up and down to suit demand.
The names of larger runners can dictate their functionality. For example, to use a larger runner for code scanning default setup, the runner must be named `code-scanning`. For more information on code scanning with larger runners, see [Configuring larger runners for default setup](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/configuring-larger-runners-for-default-setup).
  6. Click **Create runner**.
  7. To allow repositories to access your larger runners, add them to the list of repositories that can use it. For more information, see [Allowing repositories to access larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/managing-larger-runners#allowing-repositories-to-access-larger-runners).


## [Allowing repositories to access larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/managing-larger-runners#allowing-repositories-to-access-larger-runners)
Repositories are granted access to larger runners through runner groups. Enterprise administrators can choose which organizations are granted access to enterprise-level runner groups, and organization owners control repository-level access to all larger runners.
Organization owners can use and configure enterprise-level runner groups for the repositories in their organization, or they can create organization-level runner groups to control access.
  * **For enterprise-level runner groups:** By default, repositories in an organization do not have access to enterprise-level runner groups. To give repositories access to enterprise runner groups, organization owners must configure each enterprise runner group and choose which repositories have access.
  * **For organization-level runner groups:** By default, all repositories in an organization are granted access to organization-level runner groups. To restrict which repositories have access, organization owners must configure organization runner groups and choose which repositories have access.


Once a repository has access to larger runners, the larger runners can be added to workflow files. For more information, see [Running jobs on larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/running-jobs-on-larger-runners).
  1. Navigate to the main page of the organization where your runner groups are located.
  2. Click 
  3. In the left sidebar, click **Runner groups**.
  4. Select a runner group from either list on the page. Organization-level runner groups are listed at the top of the page, and enterprise-level runner groups are listed under "Shared by the Enterprise."
  5. On the runner group page, under "Repository access," select **All repositories** or **Selected repositories**. If you choose to grant access to specific repositories, click 


If you are using a Fixed IP range, we recommend that you only use larger runners with private repositories. Forks of your repository can potentially run dangerous code on your larger runner by creating a pull request that executes the code in a workflow. For more information, see [Controlling access to larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/controlling-access-to-larger-runners).
## [Changing the name of a larger runner](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/managing-larger-runners#changing-the-name-of-a-larger-runner)
The names of larger runners can dictate their functionality. For example, to use a larger runner for code scanning default setup, the runner must be named `code-scanning`. For more information on code scanning with larger runners, see [Configuring larger runners for default setup](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/configuring-larger-runners-for-default-setup).
  1. On GitHub, navigate to the main page of the organization.
  2. Under your organization name, click **Settings**.
![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](https://docs.github.com/assets/cb-49309/images/help/discussions/org-settings-global-nav-update.png)
  3. In the left sidebar, click **Runners**.
  4. In the list of runners, select the runner you would like to edit.
  5. Enter a new name for the runner in the text field under "Name."
  6. Click **Save**.


## [Changing the size of a larger runner](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/managing-larger-runners#changing-the-size-of-a-larger-runner)
  1. On GitHub, navigate to the main page of the organization.
  2. Under your organization name, click **Settings**.
![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](https://docs.github.com/assets/cb-49309/images/help/discussions/org-settings-global-nav-update.png)
  3. In the left sidebar, click **Runners**.
  4. In the list of runners, select the runner you would like to edit.
  5. Select a new size for the runner from the list of available options under "Size." The available sizes depend on the image that is installed on the runner.
  6. Click **Save**.


## [Changing the image of a larger runner](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/managing-larger-runners#changing-the-image-of-a-larger-runner)
  1. On GitHub, navigate to the main page of the organization.
  2. Under your organization name, click **Settings**.
![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](https://docs.github.com/assets/cb-49309/images/help/discussions/org-settings-global-nav-update.png)
  3. In the left sidebar, click **Runners**.
  4. In the list of runners, select the runner you would like to edit.
  5. Select a new image for the runner from the list of available options under "Image." The available images are limited to GitHub-owned images.
  6. Click **Save**.


## [Configuring autoscaling for larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/managing-larger-runners#configuring-autoscaling-for-larger-runners)
You can control the maximum number of jobs allowed to run concurrently for specific runner sets. Setting this field to a higher value can help prevent workflows being blocked due to parallelism.
  1. On GitHub, navigate to the main page of the organization.
  2. Under your organization name, click **Settings**.
![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](https://docs.github.com/assets/cb-49309/images/help/discussions/org-settings-global-nav-update.png)
  3. In the left sidebar, click **Runners**.
  4. In the list of runners, select the runner you would like to edit.
  5. In the "Auto-scaling" section, under "Maximum Job Concurrency," enter the maximum number of jobs you would like to allow to run at the same time.
  6. Click **Save**.


## [Creating static IP addresses for larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/managing-larger-runners#creating-static-ip-addresses-for-larger-runners)
To use static IP addresses, your organization must use GitHub Enterprise Cloud. For more information about how you can try GitHub Enterprise Cloud for free, see [Setting up a trial of GitHub Enterprise Cloud](https://docs.github.com/en/enterprise-cloud@latest/admin/overview/setting-up-a-trial-of-github-enterprise-cloud).
You can enable static IP addresses for larger runners. When you do this, the larger runners are assigned static IP address ranges. All IP addresses in the range assigned are usable and not in CIDR notation. By default, you can configure up to 10 different larger runners with IP ranges for your account. If you would like to use more than 10 larger runners with static IP address ranges, please contact us through the [GitHub Support portal](https://support.github.com).
The number of available IP addresses in the assigned ranges does not restrict number of concurrent jobs specified for autoscaling. Within a runner pool, there is a load balancer which allows for high reuse of the IP addresses in the assigned ranges. This ensures your workflows can run concurrently at scale while each machine is assigned a static IP address.
  1. On GitHub, navigate to the main page of the organization.
  2. Under your organization name, click **Settings**.
![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](https://docs.github.com/assets/cb-49309/images/help/discussions/org-settings-global-nav-update.png)
  3. In the left sidebar, click **Runners**.
  4. In the list of runners, select the runner you would like to edit.
  5. To assign static IP addresses to the runner, under "Networking," check **Assign unique & static public IP address ranges for this runner**.
  6. Click **Save**.


