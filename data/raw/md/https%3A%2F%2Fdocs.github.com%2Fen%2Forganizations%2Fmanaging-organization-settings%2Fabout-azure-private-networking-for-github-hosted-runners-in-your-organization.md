  * [Organizations](https://docs.github.com/en/organizations "Organizations")/
  * [Manage organization settings](https://docs.github.com/en/organizations/managing-organization-settings "Manage organization settings")/
  * [About Azure private networking](https://docs.github.com/en/organizations/managing-organization-settings/about-azure-private-networking-for-github-hosted-runners-in-your-organization "About Azure private networking")


# About Azure private networking for GitHub-hosted runners in your organization
You can create a private network configuration for your organization to use GitHub-hosted runners in your Azure Virtual Network(s) (VNET).
## Who can use this feature?
Organization owners with the GitHub Team plan can configure Azure private networking for GitHub-hosted runners at the organization level.
## In this article
  * [About Azure private networking for GitHub-hosted runners](https://docs.github.com/en/organizations/managing-organization-settings/about-azure-private-networking-for-github-hosted-runners-in-your-organization#about-azure-private-networking-for-github-hosted-runners)
  * [About using larger runners with Azure VNET](https://docs.github.com/en/organizations/managing-organization-settings/about-azure-private-networking-for-github-hosted-runners-in-your-organization#about-using-larger-runners-with-azure-vnet)
  * [About network communication](https://docs.github.com/en/organizations/managing-organization-settings/about-azure-private-networking-for-github-hosted-runners-in-your-organization#about-network-communication)
  * [About supported regions](https://docs.github.com/en/organizations/managing-organization-settings/about-azure-private-networking-for-github-hosted-runners-in-your-organization#about-supported-regions)
  * [About the GitHub Actions service permissions](https://docs.github.com/en/organizations/managing-organization-settings/about-azure-private-networking-for-github-hosted-runners-in-your-organization#about-the-github-actions-service-permissions)
  * [Using your VNET's network policies](https://docs.github.com/en/organizations/managing-organization-settings/about-azure-private-networking-for-github-hosted-runners-in-your-organization#using-your-vnets-network-policies)
  * [Using GitHub-hosted runners with an Azure VNET](https://docs.github.com/en/organizations/managing-organization-settings/about-azure-private-networking-for-github-hosted-runners-in-your-organization#using-github-hosted-runners-with-an-azure-vnet)


## [About Azure private networking for GitHub-hosted runners](https://docs.github.com/en/organizations/managing-organization-settings/about-azure-private-networking-for-github-hosted-runners-in-your-organization#about-azure-private-networking-for-github-hosted-runners)
You can use GitHub-hosted runners in an Azure VNET. This enables you to use GitHub-managed infrastructure for CI/CD while providing you with full control over the networking policies of your runners. For more information about Azure VNET, see [What is Azure Virtual Network?](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview) in the Azure documentation.
You can connect multiple VNET subnets to GitHub and manage private resource access for your runners via runner groups. For more information about runner groups, see [Controlling access to larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-larger-runners/controlling-access-to-larger-runners).
Using GitHub-hosted runners within Azure VNET allows you to perform the following actions.
  * Privately connect a runner to resources inside an Azure VNET without opening internet ports, including on-premises resources accessible from the Azure VNET.
  * Restrict what GitHub-hosted runners can access or connect to with full control over outbound network policies.
  * Monitor network logs for GitHub-hosted runners and view all connectivity to and from a runner.


## [About using larger runners with Azure VNET](https://docs.github.com/en/organizations/managing-organization-settings/about-azure-private-networking-for-github-hosted-runners-in-your-organization#about-using-larger-runners-with-azure-vnet)
2-64 vCPU Ubuntu and Windows runners are supported with Azure VNET. For more information on these runner types, see [About larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-larger-runners/about-larger-runners#about-ubuntu-and-windows-larger-runners).
Private networking for GitHub-hosted runners does not support static IP addresses for larger runners. You must use dynamic IP addresses, which is the default configuration for larger runners. For more information about networking for larger runners, see [About larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-larger-runners/about-larger-runners#networking-for-larger-runners).
## [About network communication](https://docs.github.com/en/organizations/managing-organization-settings/about-azure-private-networking-for-github-hosted-runners-in-your-organization#about-network-communication)
To facilitate communication between GitHub networks and your VNET, a GitHub-hosted runner's network interface card (NIC) deploys into your Azure VNET.
Because the NIC lives within your VNET, GitHub cannot block inbound connections. By default, Azure virtual machines will accept inbound connections from the same VNET. For more information, see [`AllowVNetInBound`](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview#allowvnetinbound) on Microsoft Learn. It is recommended to explicitly block all inbound connections to the runners. GitHub will never require inbound connections to these machines.
A NIC enables an Azure virtual machine (VM) to communicate with internet, Azure, and on-premises resources. This way, all communication is kept private within the network boundaries, and networking policies applied to the VNET also apply to the runner. For more information on how to manage a network interface, see [Change network interface settings](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-network-interface?tabs=azure-portal#change-network-interface-settings) on Microsoft Learn.
Multiple NICs may appear for a single job in your subscription because the GitHub Actions service over-provisions resources to run jobs. Once a runner is idle, the GitHub Actions service automatically de-provisions the resource and removes the corresponding NIC.
![Diagram of network communication between GitHub and your private networks. Each step is numbered and corresponds to a step listed below the diagram.](https://docs.github.com/assets/cb-289537/images/help/actions/actions-vnet-injected-larger-runners-architecture.png)
  1. A GitHub Actions workflow is triggered.
  2. The GitHub Actions service creates a runner.
  3. The runner service deploys the GitHub-hosted runner's network interface card (NIC) into your Azure VNET.
  4. The runner agent picks up the workflow job. The GitHub Actions service queues the job.
  5. The runner sends logs back to the GitHub Actions service.
  6. The NIC accesses on-premise resources.


## [About supported regions](https://docs.github.com/en/organizations/managing-organization-settings/about-azure-private-networking-for-github-hosted-runners-in-your-organization#about-supported-regions)
The GitHub Actions service supports a subset of all the regions that Azure provides. To facilitate communication between the GitHub Actions service and your subnet, your subnet must be in one of the supported regions.
If you use data residency on GHE.com, the supported regions are different. See [Network details for GHE.com](https://docs.github.com/en/enterprise-cloud@latest/admin/data-residency/network-details-for-ghecom#supported-regions-for-azure-private-networking).
The following regions are supported on GitHub.com.
  * `AustraliaEast`
  * `BrazilSouth`
  * `CanadaCentral`
  * `CanadaEast`
  * `CentralUs`
  * `EastAsia`
  * `EastUs`
  * `EastUs2`
  * `FranceCentral`
  * `GermanyWestCentral`
  * `JapanEast`
  * `KoreaCentral`
  * `NorthCentralUs`
  * `NorthEurope`
  * `NorwayEast`
  * `SouthCentralUs`
  * `SoutheastAsia`
  * `SouthIndia`
  * `SwedenCentral`
  * `SwitzerlandNorth`
  * `UkSouth`
  * `WestUs`
  * `WestUs2`
  * `WestUs3`


Azure private networking supports GPU runners in the following regions.
  * `EastUs`
  * `NorthCentralUs`
  * `SouthCentralUs`
  * `WestUs`


Azure private networking supports arm64 runners in the following regions.
  * `CentralUs`
  * `EastUs`
  * `EastUs2`
  * `NorthCentralUs`
  * `SouthCentralUs`
  * `WestUs`
  * `WestUs2`
  * `WestUs3`


If your desired region is not supported, please submit a request for new region availability in [this GitHub form](https://resources.github.com/private-networking-for-github-hosted-runners-with-azure-virtual-networks/). You may also use global virtual network peering to connect virtual networks across Azure regions. For more information, see [Virtual network peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-peering-overview) in the Azure documentation.
## [About the GitHub Actions service permissions](https://docs.github.com/en/organizations/managing-organization-settings/about-azure-private-networking-for-github-hosted-runners-in-your-organization#about-the-github-actions-service-permissions)
In order to successfully deploy a NIC and join a NIC to a subnet, the GitHub Actions service maintains the following Azure role-based access control (RBAC) permissions in your Azure subscription. For more information about fine-grained access management of Azure resources, see [Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/) in the Azure documentation.
  * `GitHub.Network/operations/read`
  * `GitHub.Network/networkSettings/read`
  * `GitHub.Network/networkSettings/write`
  * `GitHub.Network/networkSettings/delete`
  * `GitHub.Network/RegisteredSubscriptions/read`
  * `Microsoft.Network/locations/operations/read`
  * `Microsoft.Network/locations/operationResults/read`
  * `Microsoft.Network/locations/usages/read`
  * `Microsoft.Network/networkInterfaces/read`
  * `Microsoft.Network/networkInterfaces/write`
  * `Microsoft.Network/networkInterfaces/delete`
  * `Microsoft.Network/networkInterfaces/join/action`
  * `Microsoft.Network/networkSecurityGroups/join/action`
  * `Microsoft.Network/networkSecurityGroups/read`
  * `Microsoft.Network/publicIpAddresses/read`
  * `Microsoft.Network/publicIpAddresses/write`
  * `Microsoft.Network/publicIPAddresses/join/action`
  * `Microsoft.Network/routeTables/join/action`
  * `Microsoft.Network/virtualNetworks/read`
  * `Microsoft.Network/virtualNetworks/subnets/join/action`
  * `Microsoft.Network/virtualNetworks/subnets/read`
  * `Microsoft.Network/virtualNetworks/subnets/write`
  * `Microsoft.Network/virtualNetworks/subnets/serviceAssociationLinks/delete`
  * `Microsoft.Network/virtualNetworks/subnets/serviceAssociationLinks/read`
  * `Microsoft.Network/virtualNetworks/subnets/serviceAssociationLinks/write`
  * `Microsoft.Network/virtualNetworks/subnets/serviceAssociationLinks/details/read`
  * `Microsoft.Network/virtualNetworks/subnets/serviceAssociationLinks/validate/action`
  * `Microsoft.Resources/subscriptions/resourceGroups/read`
  * `Microsoft.Resources/subscriptions/resourcegroups/deployments/read`
  * `Microsoft.Resources/subscriptions/resourcegroups/deployments/write`
  * `Microsoft.Resources/subscriptions/resourcegroups/deployments/operations/read`
  * `Microsoft.Resources/deployments/read`
  * `Microsoft.Resources/deployments/write`
  * `Microsoft.Resources/deployments/operationStatuses/read`


The following permissions will be present on two enterprise applications in your Azure tenant. You will see the enterprise applications your Azure tenant after configuring Azure private networking.
  * `GitHub CPS Network Service` id: `85c49807-809d-4249-86e7-192762525474`
  * `GitHub Actions API` id: `4435c199-c3da-46b9-a61d-76de3f2c9f82`


## [Using your VNET's network policies](https://docs.github.com/en/organizations/managing-organization-settings/about-azure-private-networking-for-github-hosted-runners-in-your-organization#using-your-vnets-network-policies)
Because the GitHub-hosted runner's NIC is deployed into your Azure VNET, networking policies applied to the VNET also apply to the runner.
For example, if your VNET is configured with an Azure ExpressRoute to provide access to on-premises resources (e.g. Artifactory) or connected to a VPN tunnel to provide access to other cloud-based resources, those access policies also apply to your runners. Additionally, any outbound rules applied to your VNET's network security group (NSG) also apply, giving you the ability to control outbound access for your runners.
If you have enabled any network logs monitoring for your VNET, you can also monitor network traffic for your runners.
GitHub-hosted runners use whatever outbound control your network is using. If your network relies on Azure's default outbound access, the IPs are not predictable and cannot be added to the GitHub IP allow list. For recommendations on using a stable outbound IP, see [Default outbound access](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/default-outbound-access) in the Azure documentation.
## [Using GitHub-hosted runners with an Azure VNET](https://docs.github.com/en/organizations/managing-organization-settings/about-azure-private-networking-for-github-hosted-runners-in-your-organization#using-github-hosted-runners-with-an-azure-vnet)
To use GitHub-hosted runners with an Azure VNET, you will need to configure your Azure resources and then create a networking configuration in GitHub.
For procedures to configure Azure private networking at the organization level, see [Configuring private networking for GitHub-hosted runners in your organization](https://docs.github.com/en/organizations/managing-organization-settings/configuring-private-networking-for-github-hosted-runners-in-your-organization).
