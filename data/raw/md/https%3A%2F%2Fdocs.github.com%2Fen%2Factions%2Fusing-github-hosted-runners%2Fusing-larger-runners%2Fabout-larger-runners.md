  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [GitHub-hosted runners](https://docs.github.com/en/actions/using-github-hosted-runners "GitHub-hosted runners")/
  * [Using larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners "Using larger runners")/
  * [About larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners "About larger runners")


# About larger runners
GitHub offers runners with advanced features to support more customized use cases.
## Who can use this feature?
Larger runners are only available for organizations and enterprises using the GitHub Team or GitHub Enterprise Cloud plans.
## In this article
  * [Overview of larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners#overview-of-larger-runners)
  * [Machine sizes for larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners#machine-sizes-for-larger-runners)
  * [About runner groups](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners#about-runner-groups)
  * [Architectural overview of larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners#architectural-overview-of-larger-runners)
  * [Autoscaling larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners#autoscaling-larger-runners)
  * [Assigning static IP addresses to larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners#assigning-static-ip-addresses-to-larger-runners)
  * [Networking for larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners#networking-for-larger-runners)


## [Overview of larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners#overview-of-larger-runners)
Customers on GitHub Team and GitHub Enterprise Cloud plans can choose from a range of managed virtual machines that have more resources than the [standard GitHub-hosted runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners#supported-runners-and-hardware-resources). These machines are referred to as "larger runner." They offer the following advanced features:
  * More RAM, CPU, and disk space
  * Static IP addresses
  * Azure private networking
  * The ability to group runners
  * Autoscaling to support concurrent workflows
  * GPU-powered runners


These larger runners are hosted by GitHub and have the runner application and other tools preinstalled.
GitHub offers larger runners with macOS, Ubuntu, or Windows operating systems, and different features and sizes are available depending on which operating system you use. For more information, see [Additional features for larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners#additional-features-for-larger-runners).
### [About Ubuntu and Windows larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners#about-ubuntu-and-windows-larger-runners)
Larger runners with Ubuntu or Windows operating systems are configured in your organization or enterprise. When you add a larger runner, you are defining a type of machine from a selection of available hardware specifications and operating system images. GitHub will then create multiple instances of this runner that scale up and down to match the job demands of your organization, based on the autoscaling limits you define. For more information, see [Managing larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/managing-larger-runners).
Ubuntu and Windows larger runners offer autoscaling capabilities and the ability to assign the runners static IP addresses from a specific range. They can also be managed using runner groups, which enables you to control access to the larger runners. For more information, see [Additional features for larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners#additional-features-for-larger-runners).
### [About macOS larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners#about-macos-larger-runners)
Larger runners with a macOS operating system are used by updating the YAML workflow label to the desired runner image. To run your workflows on a macOS larger runner, update the `runs-on` key to use one of the GitHub-defined macOS larger runner labels. No additional configuration is required. For more information, see [Running jobs on larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/running-jobs-on-larger-runners?platform=mac).
The following machines sizes are available for macOS larger runners.
Runner Size | Architecture | Processor (CPU) | Memory (RAM) | Storage (SSD) | Workflow label  
---|---|---|---|---|---  
Large | Intel | 12 | 30 GB | 14 GB |  `macos-latest-large`, `macos-13-large`, `macos-14-large` [latest], `macos-15-large`  
XLarge | arm64 (M1) | 6 (+ 8 GPU hardware acceleration) | 14 GB | 14 GB |  `macos-latest-xlarge`, `macos-13-xlarge` , `macos-14-xlarge` [latest], `macos-15-xlarge`  
#### [Limitations for macOS larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners#limitations-for-macos-larger-runners)
  * All actions provided by GitHub are compatible with arm64 GitHub-hosted runners. However, community actions may not be compatible with arm64 and need to be manually installed at runtime.
  * Nested-virtualization and Metal Performance Shaders (MPS) are not supported due to the limitation of Apple's Virtualization Framework.
  * Networking capabilities such as Azure private networking and assigning static IPs are not currently available for macOS larger runners.
  * The arm64 macOS runners do not have a static UUID/UDID assigned to them because Apple does not support this feature. However, Intel MacOS runners are assigned a static UDID, specifically `4203018E-580F-C1B5-9525-B745CECA79EB`. If you are building and signing on the same host you plan to test the build on, you can sign with a [development provisioning profile](https://developer.apple.com/help/account/manage-profiles/create-a-development-provisioning-profile/). If you do require a static UDID, you can use Intel runners and add their UDID to your Apple Developer account.


### [Additional features for larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners#additional-features-for-larger-runners)
Compared to standard GitHub-hosted runners, larger runners have additional features, and their availability varies depending on the larger runner's operating system.
| Ubuntu | Windows | macOS  
---|---|---|---  
Static IP addresses |  |  |   
Azure private networking |  |  |   
Autoscaling |  |  |   
Runner groups |  |  |   
These features can enhance your CI/CD pipelines in the following ways.
  * Assigning larger runners static IP addresses from a specific range enables you to use this range to configure a firewall allowlist. For more information, see [Networking for larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners#networking-for-larger-runners).
  * Autoscaling enables larger runners to scale up to a maximum limit set by you, so your workflows can run concurrently. For more information, see [Autoscaling larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners#autoscaling-larger-runners).
  * Runner groups allow you to control access to larger runners for your organizations, repositories, and workflows. For more information, see [Controlling access to larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/controlling-access-to-larger-runners).


### [Runner images](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners#runner-images)
Larger runners run on virtual machines (VMs), and GitHub installs a virtual hard disk (VHD) on this machine during the VM creation process. You can choose from different VM images to install on your runners.
**GitHub-owned images:** These images are maintained by GitHub and are available for Linux x64, Windows x64, and macOS (x64 and arm) runners. For more information on these images and a full list of included tools for each runner operating system, see the [GitHub Actions Runner Images](https://github.com/actions/runner-images) repository.
**Partner Images:** Partner images are not managed by GitHub and are pulled from the Azure Marketplace. See below for resources on where to find more information and to report issues for partner images.
  * [Base Windows 11 desktop image](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/microsoftwindowsdesktop.windows-11?tab=Overview).
  * [NVIDIA GPU-Optimized VMI](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/nvidia.ngc_azure_17_11)
  * [Data Science Virtual Machine - Windows 2019](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/microsoft-dsvm.dsvm-win-2019?tab=overview).
  * arm64 images: [`actions/partner-runner-images` repository](https://github.com/actions/partner-runner-images).


### [Understanding billing](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners#understanding-billing)
Larger runners are not eligible for the use of included minutes on private repositories. For both private and public repositories, when larger runners are in use, they will always be billed at the per-minute rate.
Compared to standard GitHub-hosted runners, larger runners are billed differently. Larger runners are only billed at the per-minute rate for the amount of time workflows are executed on them. There is no cost associated with creating a larger runner that is not being used by a workflow. For more information, see [About billing for GitHub Actions](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions#per-minute-rates).
## [Machine sizes for larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners#machine-sizes-for-larger-runners)
You can choose from several specifications for larger runners.
### [Specifications for general larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners#specifications-for-general-larger-runners)
CPU | Memory (RAM) | Storage (SSD) | Architecture | Operating system (OS)  
---|---|---|---|---  
6 | 14 GB | 14 GB | arm64 | macOS  
12 | 30 GB | 14 GB | x64 | macOS  
2 | 8 GB | 75 GB | x64, arm64 | Ubuntu  
4 | 16 GB | 150 GB | x64, arm64 | Ubuntu, Windows  
8 | 32 GB | 300 GB | x64, arm64 | Ubuntu, Windows  
16 | 64 GB | 600 GB | x64, arm64 | Ubuntu, Windows  
32 | 128 GB | 1200 GB | x64, arm64 | Ubuntu, Windows  
64 | 208 GB | 2040 GB | arm64 | Ubuntu, Windows  
64 | 256 GB | 2040 GB | x64 | Ubuntu, Windows  
96 | 384 GB | 2040 GB | x64 | Ubuntu, Windows  
The 4-vCPU Windows runner only works with the Windows Server 2025 or the Base Windows 11 Desktop image.
### [Specifications for GPU larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners#specifications-for-gpu-larger-runners)
CPU | GPU | GPU card | Memory (RAM) | GPU memory (VRAM) | Storage (SSD) | Operating system (OS)  
---|---|---|---|---|---|---  
4 | 1 | Tesla T4 | 28 GB | 16 GB | 176 GB | Ubuntu, Windows  
## [About runner groups](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners#about-runner-groups)
Only larger runners with Linux or Windows operating systems can be assigned to runner groups.
Runner groups enable administrators to control access to runners at the organization and enterprise levels. With runner groups, you can collect sets of runners and create a security boundary around them. You can then decide which organizations or repositories are permitted to run jobs on those sets of machines. During the larger runner deployment process, the runner can be added to an existing group, otherwise it will join a default group. You can create a group by following the steps in [Controlling access to larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/controlling-access-to-larger-runners).
## [Architectural overview of larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners#architectural-overview-of-larger-runners)
This architecture diagram only applies to larger runners with Linux or Windows operating systems.
Larger runners are managed at the organization level, where they are arranged into groups that can contain multiple instances of the runner. They can also be created at the enterprise level and shared with organizations in the hierarchy. Once you've created a group, you can then add a runner to the group and update your workflows to target either the group name or the label assigned to the larger runner. You can also control which repositories are permitted to send jobs to the group for processing. For more information about groups, see [Controlling access to larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/controlling-access-to-larger-runners).
In the following diagram, a class of hosted runner named `ubuntu-20.04-16core` has been defined with customized hardware and operating system configuration.
![Diagram showing a larger runner being used by a workflow because of the runner's label.](https://docs.github.com/assets/cb-127441/images/help/actions/hosted-runner.png)
  1. Instances of this runner are automatically created and added to a group called `grp-ubuntu-20.04-16core`.
  2. The runners have been assigned the label `ubuntu-20.04-16core`.
  3. Workflow jobs use the `ubuntu-20.04-16core` label in their `runs-on` key to indicate the type of runner they need to execute the job.
  4. GitHub Actions checks the runner group to see if your repository is authorized to send jobs to the runner.
  5. The job runs on the next available instance of the `ubuntu-20.04-16core` runner.


## [Autoscaling larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners#autoscaling-larger-runners)
Autoscaling is only available for larger runners with Linux or Windows operating systems.
Larger runners can automatically scale to suit your needs. You can provision machines to run a specified maximum number of jobs when jobs are submitted for processing. Each machine only handles one job at a time, so these settings effectively determine the number of jobs that can be run concurrently.
You can configure the maximum job concurrency, which allows you to control your costs by setting the maximum parallel number of jobs that can be run using this set. A higher value here can help avoid workflows being blocked due to parallelism. For more information on how to set limits, see [Managing larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/managing-larger-runners#configuring-autoscaling-for-larger-runners). For more information on the maximum auto-scaling limits for GitHub-hosted runners, see [Usage limits, billing, and administration](https://docs.github.com/en/actions/learn-github-actions/usage-limits-billing-and-administration#usage-limits).
## [Assigning static IP addresses to larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners#assigning-static-ip-addresses-to-larger-runners)
You can assign static IP addresses only to larger runners that use Linux or Windows operating systems.
Static IP addresses assigned are all usable and are not in CIDR notation.
Private networking for GitHub-hosted runners does not support static IP addresses for larger runners. For more information about private networking for GitHub-hosted runners, see [About Azure private networking for GitHub-hosted runners in your enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/configuration/configuring-private-networking-for-hosted-compute-products/about-azure-private-networking-for-github-hosted-runners-in-your-enterprise).
## [Networking for larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners#networking-for-larger-runners)
By default, larger runners receive a dynamic IP address that changes for each job run. Optionally, GitHub Enterprise Cloud customers can configure their larger runners to receive static IP addresses from GitHub's IP address pool. For more information, see [About GitHub's IP addresses](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-githubs-ip-addresses).
When enabled, instances of the larger runner will receive IP addresses from specific ranges that are unique to the runner, allowing you to use the ranges to configure a firewall allowlist. You can use up to 10 larger runners with static IP address ranges in total across all your larger runners. For more information, see [Managing larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/managing-larger-runners#networking-for-larger-runners).
If you would like to use more than 10 larger runners with static IP address ranges, please contact us through the [GitHub Support portal](https://support.github.com).
If runners are unused for more than 30 days, their IP address ranges are automatically removed and cannot be recovered.
