  * [Organizations](https://docs.github.com/en/organizations "Organizations")/
  * [Manage organization settings](https://docs.github.com/en/organizations/managing-organization-settings "Manage organization settings")/
  * [Troubleshooting Azure private networking](https://docs.github.com/en/organizations/managing-organization-settings/troubleshooting-azure-private-network-configurations-for-github-hosted-runners-in-your-organization "Troubleshooting Azure private networking")


# Troubleshooting Azure private network configurations for GitHub-hosted runners in your organization
Learn how to fix common issues while creating Azure private network configurations to use GitHub-hosted runners with an Azure VNET.
## Who can use this feature?
Organization owners with the GitHub Team plan can configure Azure private networking for GitHub-hosted runners at the organization level.
## [Troubleshooting configuring private networking for GitHub-hosted runners in your organization](https://docs.github.com/en/organizations/managing-organization-settings/troubleshooting-azure-private-network-configurations-for-github-hosted-runners-in-your-organization#troubleshooting-configuring-private-networking-for-github-hosted-runners-in-your-organization)
### [Configuring Azure resources before creating a network configuration in GitHub](https://docs.github.com/en/organizations/managing-organization-settings/troubleshooting-azure-private-network-configurations-for-github-hosted-runners-in-your-organization#configuring-azure-resources-before-creating-a-network-configuration-in-github)
Ensure your Azure resources have been configured _before_ adding a network configuration in GitHub.
### [Supported regions](https://docs.github.com/en/organizations/managing-organization-settings/troubleshooting-azure-private-network-configurations-for-github-hosted-runners-in-your-organization#supported-regions)
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
### [Runner failed to connect to the internet](https://docs.github.com/en/organizations/managing-organization-settings/troubleshooting-azure-private-network-configurations-for-github-hosted-runners-in-your-organization#runner-failed-to-connect-to-the-internet)
GitHub-hosted runners need to be able to make outbound connections to GitHub as well as other necessary URLs for GitHub Actions.
If GitHub Actions cannot communicate with the runners, the pool will never be able to bring runners online and so no jobs will be picked up. In this case, the pool will have the following error code.
```
VNetInjectionFailedToConnectToInternet

```

To fix this, ensure that you have configured your Azure resources according to the "Configuring your Azure resources" procedures.
### [Deployment scope is locked](https://docs.github.com/en/organizations/managing-organization-settings/troubleshooting-azure-private-network-configurations-for-github-hosted-runners-in-your-organization#deployment-scope-is-locked)
You can put locks on the Azure subscription or resource group, which can prevent NIC creation or deletion.
Locks that prevent NIC creation fail to pick up jobs, while locks that prevent NIC deletion either exhaust subnet address space (by continuing to create NICs) or have long queue-to-assign (QTA) times as the service retries deployment exceptions.
In this case, the pool will have the following error code.
```
RunnerDeploymentScopeLocked

```

To fix this, remove the lock or change the subnet you are using to one without a lock.
### [Deployment blocked by policy](https://docs.github.com/en/organizations/managing-organization-settings/troubleshooting-azure-private-network-configurations-for-github-hosted-runners-in-your-organization#deployment-blocked-by-policy)
You can create policies on their management group, subscription, resource group, or individual resources. The most common policy is requiring a resource to have certain tags or to have a specific name.
The policy will prevent creation of NICs, which means the pool will not pick up jobs since no VMs can come online.
In this case, the pool will have the following error code.
```
RunnerDeploymentBlockedByPolicy

```

To fix this, remove the policy or change the subnet you are using to one without a policy.
### [Subnet is full](https://docs.github.com/en/organizations/managing-organization-settings/troubleshooting-azure-private-network-configurations-for-github-hosted-runners-in-your-organization#subnet-is-full)
Subnets have a limited amount of IP addresses to distribute. Each runner consumes one IP address. If the service attempts to scale up beyond the maximum runner count setting, it will encounter deployment errors.
This impacts the ability of the pool to add additional runners. If the queue depth is high enough, you may experience increased queue-to-assign (QTA) times. Jobs will still be processed, but not at a level of concurrency that you may expect.
In this case, the pool will have the following error code.
```
VNetInjectionSubnetIsFull

```

To fix this, either increase the size of the subnet you are using or reduce the pool's maximum runner count to match your subnet size.
### [Cannot delete subnet](https://docs.github.com/en/organizations/managing-organization-settings/troubleshooting-azure-private-network-configurations-for-github-hosted-runners-in-your-organization#cannot-delete-subnet)
In some cases, a subnet cannot be deleted because it has a Service Association Link (SAL) applied to it. For more information, see [Configuring private networking for GitHub-hosted runners in your organization](https://docs.github.com/en/organizations/managing-organization-settings/configuring-private-networking-for-github-hosted-runners-in-your-organization#deleting-a-subnet).
If you need to identify the network settings resource associated with the subnet, you can run the following `curl` command. To obtain an Azure Entra token, please refer to the [Azure documentation](https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli). Use the same `api-version` you used to create the resource.
```
curl --request GET \
  --url "https://management.azure.com/subscriptions/{subscriptionId}/providers/GitHub.Network/NetworkSettings?api-version={api-version}&subnetId={subnetId}" \
  --header 'Content-Type: application/json' \
  --header "Authorization: Bearer {entra_token}"

```

### [Incorrect NSG or firewall rules](https://docs.github.com/en/organizations/managing-organization-settings/troubleshooting-azure-private-network-configurations-for-github-hosted-runners-in-your-organization#incorrect-nsg-or-firewall-rules)
The "Configuring your Azure resources" procedures list the required openings. However, you may have complex production networks with multiple downstream proxies or firewalls.
If runners are failing to come online, no jobs will be picked up. Your setup process may involve setting up the runner application and communicating back to the GitHub Actions service to indicate it is ready, as well as fetching and installing anti-abuse tooling. If either of these processes fail, the runner cannot pick up any jobs.
If you are experiencing these issues, try setting up a virtual machine on the same subnet that you are using for private networking with GitHub-hosted runners. However, if you have a service association link (SAL) in place, this is not possible.
If you have a SAL in place, try setting up a similar subnet in the virtual network and place a virtual machine on that network. Then attempt to register a self-hosted runner on it.
### [HTTP request payload failure when configuring Azure resources](https://docs.github.com/en/organizations/managing-organization-settings/troubleshooting-azure-private-network-configurations-for-github-hosted-runners-in-your-organization#http-request-payload-failure-when-configuring-azure-resources)
While running the command to configure Azure resources, ensure you are using the correct API version and the `businessId` property. If you are using a different property, your command may return the following error.
```
(HttpRequestPayloadAPISpecValidationFailed) HTTP request payload failed validation against API specification with one or more errors. Please see details for more information.

```

If you experience this error, you can see more information by running the command using the `---debug` flag.
### [Network settings configured at the wrong level](https://docs.github.com/en/organizations/managing-organization-settings/troubleshooting-azure-private-network-configurations-for-github-hosted-runners-in-your-organization#network-settings-configured-at-the-wrong-level)
If network settings were configured using an organization's `databaseId` instead of an enterprise `databaseId`, an error will occur. The error message will indicate that a private network cannot be established with the provided resource ID because it is already associated with a different enterprise or organization. To resolve this, delete the existing network settings and recreate them using the enterprise `databaseId`.
