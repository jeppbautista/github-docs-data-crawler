  * [Organizations](https://docs.github.com/en/organizations "Organizations")/
  * [Manage organization settings](https://docs.github.com/en/organizations/managing-organization-settings "Manage organization settings")/
  * [About private networking](https://docs.github.com/en/organizations/managing-organization-settings/about-networking-for-hosted-compute-products-in-your-organization "About private networking")


# About networking for hosted compute products in your organization
You can manage private networking for GitHub-hosted products using network configurations in your organization.
## Who can use this feature?
Organization owners with the GitHub Team plan can configure Azure private networking for GitHub-hosted runners at the organization level.
## In this article
  * [About network configurations](https://docs.github.com/en/organizations/managing-organization-settings/about-networking-for-hosted-compute-products-in-your-organization#about-network-configurations)
  * [About Azure private networking for GitHub-hosted runners](https://docs.github.com/en/organizations/managing-organization-settings/about-networking-for-hosted-compute-products-in-your-organization#about-azure-private-networking-for-github-hosted-runners)


## [About network configurations](https://docs.github.com/en/organizations/managing-organization-settings/about-networking-for-hosted-compute-products-in-your-organization#about-network-configurations)
Network configurations provide an overarching construct to manage private networking settings for GitHub-hosted compute products including GitHub-hosted runners.
By customizing network configurations for hosted compute products, you can securely access private resources, control outbound network access, and monitor network traffic. This allows you to control and manage network security for your development and CI/CD managed infrastructure within a single place.
## [About Azure private networking for GitHub-hosted runners](https://docs.github.com/en/organizations/managing-organization-settings/about-networking-for-hosted-compute-products-in-your-organization#about-azure-private-networking-for-github-hosted-runners)
You can use GitHub-hosted runners in an Azure VNET. This enables you to use GitHub-managed infrastructure for CI/CD while providing you with full control over the networking policies of your runners. For more information about Azure VNET, see [What is Azure Virtual Network?](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview) in the Azure documentation.
For more information about how using an Azure VNET with GitHub-hosted runners works, see [About Azure private networking for GitHub-hosted runners in your organization](https://docs.github.com/en/organizations/managing-organization-settings/about-azure-private-networking-for-github-hosted-runners-in-your-organization).
To use GitHub-hosted runners with an Azure VNET, you will need to configure your Azure resources and then create a networking configuration in GitHub.
For procedures to configure Azure private networking at the organization level, see [Configuring private networking for GitHub-hosted runners in your organization](https://docs.github.com/en/organizations/managing-organization-settings/configuring-private-networking-for-github-hosted-runners-in-your-organization).
