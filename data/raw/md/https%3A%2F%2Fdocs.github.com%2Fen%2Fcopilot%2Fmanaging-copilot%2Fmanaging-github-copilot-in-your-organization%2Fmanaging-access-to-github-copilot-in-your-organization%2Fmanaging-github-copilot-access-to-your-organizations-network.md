  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Manage Copilot](https://docs.github.com/en/copilot/managing-copilot "Manage Copilot")/
  * [Manage for organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization "Manage for organization")/
  * [Manage access](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-access-to-github-copilot-in-your-organization "Manage access")/
  * [Manage network access](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-access-to-github-copilot-in-your-organization/managing-github-copilot-access-to-your-organizations-network "Manage network access")


# Managing GitHub Copilot access to your organization's network
Learn how to use subscription-based network routing to control Copilot access to your network.
## Who can use this feature?
Organization owners
Copilot Business
## In this article
  * [About Copilot subscription-based network routing](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-access-to-github-copilot-in-your-organization/managing-github-copilot-access-to-your-organizations-network#about-copilot-subscription-based-network-routing)
  * [Important steps to ensure continued access to Copilot](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-access-to-github-copilot-in-your-organization/managing-github-copilot-access-to-your-organizations-network#important-steps-to-ensure-continued-access-to-copilot)
  * [Configuring Copilot subscription-based network routing for your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-access-to-github-copilot-in-your-organization/managing-github-copilot-access-to-your-organizations-network#configuring-copilot-subscription-based-network-routing-for-your-organization)


## [About Copilot subscription-based network routing](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-access-to-github-copilot-in-your-organization/managing-github-copilot-access-to-your-organizations-network#about-copilot-subscription-based-network-routing)
As an organization owner, you can use your network firewall to explicitly allow access to GitHub Copilot Business, and/or block access to GitHub Copilot Pro or GitHub Copilot Free. This allows you to control which GitHub Copilot plans your members can use within your network.
Configuring Copilot subscription-based network routing will affect the following Copilot features:
  * Code completion in Visual Studio Code, Visual Studio, JetBrains IDEs, and Vim/NeoVim
  * Copilot Chat in Visual Studio Code, Visual Studio, and JetBrains IDEs
  * Copilot Chat on GitHub
  * GitHub Mobile Apps
  * Copilot in the CLI


Copilot subscription-based network routing is enabled for all users. This ensures that users access Copilot through an endpoint that is specific to their Copilot plan. Only Copilot Business users will be able to connect to the Copilot Business endpoint and only Copilot Enterprise users will be able to connect to the Copilot Enterprise endpoint.
## [Important steps to ensure continued access to Copilot](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-access-to-github-copilot-in-your-organization/managing-github-copilot-access-to-your-organizations-network#important-steps-to-ensure-continued-access-to-copilot)
You should ensure that your firewall allows access to all of the hostnames listed in [Configuring your proxy server or firewall for Copilot](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/configuring-your-proxy-server-or-firewall-for-copilot).
## [Configuring Copilot subscription-based network routing for your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-access-to-github-copilot-in-your-organization/managing-github-copilot-access-to-your-organizations-network#configuring-copilot-subscription-based-network-routing-for-your-organization)
Organization owners can add the endpoints for Copilot Business or Copilot Enterprise to their allow-list. This will ensure that members can only access Copilot through the allowed endpoint.
  1. Ensure your members have updated to at least the minimum version of their Copilot client listed below.
     * For Visual Studio Code, use Copilot Chat version 0.17 or later.
     * For JetBrains IDEs, use Copilot version 1.5.6.5692 or later.
     * For Visual Studio, use version VS 2022 17.11 or later.
  2. Update your corporate network firewall to include one, or both, of these paths in your allowlist:
     * For a Copilot Business plan, add `*.business.githubcopilot.com`
     * For a Copilot Enterprise plan, add `*.enterprise.githubcopilot.com`
The `*` indicates a wildcard character. A wildcard is necessary as there are multiple subdomains required for Copilot to function correctly.
  3. Update your corporate network firewall to include `*.individual.githubcopilot.com` in your blocklist.


