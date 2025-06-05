  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [GitHub-hosted runners](https://docs.github.com/en/actions/using-github-hosted-runners "GitHub-hosted runners")/
  * [Private networking](https://docs.github.com/en/actions/using-github-hosted-runners/connecting-to-a-private-network "Private networking")/
  * [About private networking](https://docs.github.com/en/actions/using-github-hosted-runners/connecting-to-a-private-network/about-private-networking-with-github-hosted-runners "About private networking")


# About private networking with GitHub-hosted runners
You can connect GitHub-hosted runners to resources on a private network, including package registries, secret managers, and other on-premises services.
## In this article
  * [About GitHub-hosted runners networking](https://docs.github.com/en/actions/using-github-hosted-runners/connecting-to-a-private-network/about-private-networking-with-github-hosted-runners#about-github-hosted-runners-networking)
  * [Using an API Gateway with OIDC](https://docs.github.com/en/actions/using-github-hosted-runners/connecting-to-a-private-network/about-private-networking-with-github-hosted-runners#using-an-api-gateway-with-oidc)
  * [Using WireGuard to create a network overlay](https://docs.github.com/en/actions/using-github-hosted-runners/connecting-to-a-private-network/about-private-networking-with-github-hosted-runners#using-wireguard-to-create-a-network-overlay)
  * [Using an Azure Virtual Network (VNET)](https://docs.github.com/en/actions/using-github-hosted-runners/connecting-to-a-private-network/about-private-networking-with-github-hosted-runners#using-an-azure-virtual-network-vnet)


## [About GitHub-hosted runners networking](https://docs.github.com/en/actions/using-github-hosted-runners/connecting-to-a-private-network/about-private-networking-with-github-hosted-runners#about-github-hosted-runners-networking)
By default, GitHub-hosted runners have access to the public internet. However, you may also want these runners to access resources on your private network, such as a package registry, a secret manager, or other on-premise services.
GitHub-hosted runners are shared across all GitHub customers. However with private networking, you can configure hosted runners to be exclusively used to connect to your private network and resources while they are running your workflows.
There are a few different approaches you could take to configure this access, each with different advantages and disadvantages.
## [Using an API Gateway with OIDC](https://docs.github.com/en/actions/using-github-hosted-runners/connecting-to-a-private-network/about-private-networking-with-github-hosted-runners#using-an-api-gateway-with-oidc)
With GitHub Actions, you can use OpenID Connect (OIDC) tokens to authenticate your workflow outside of GitHub Actions. For more information, see [Using an API gateway with OIDC](https://docs.github.com/en/actions/using-github-hosted-runners/connecting-to-a-private-network/using-an-api-gateway-with-oidc).
## [Using WireGuard to create a network overlay](https://docs.github.com/en/actions/using-github-hosted-runners/connecting-to-a-private-network/about-private-networking-with-github-hosted-runners#using-wireguard-to-create-a-network-overlay)
If you don't want to maintain separate infrastructure for an API Gateway, you can create an overlay network between your runner and a service in your private network, by running WireGuard in both places. For more information, see [Using WireGuard to create a network overlay](https://docs.github.com/en/actions/using-github-hosted-runners/connecting-to-a-private-network/using-wireguard-to-create-a-network-overlay).
## [Using an Azure Virtual Network (VNET)](https://docs.github.com/en/actions/using-github-hosted-runners/connecting-to-a-private-network/about-private-networking-with-github-hosted-runners#using-an-azure-virtual-network-vnet)
You can use GitHub-hosted runners in an Azure VNET. This enables you to use GitHub-managed infrastructure for CI/CD while providing you with full control over the networking policies of your runners. For more information about Azure VNET, see [What is Azure Virtual Network?](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview) in the Azure documentation.
Organization owners using the GitHub Team plan can configure Azure private networking for GitHub-hosted runners at the organization level. For more information, see [About Azure private networking for GitHub-hosted runners in your organization](https://docs.github.com/en/organizations/managing-organization-settings/about-azure-private-networking-for-github-hosted-runners-in-your-organization).
