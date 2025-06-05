  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Manage Copilot](https://docs.github.com/en/copilot/managing-copilot "Manage Copilot")/
  * [Manage for organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization "Manage for organization")/
  * [Allow Copilot traffic](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/configuring-your-proxy-server-or-firewall-for-copilot "Allow Copilot traffic")


# Configuring your proxy server or firewall for Copilot
You should allow certain traffic through your firewall or proxy server for Copilot to work as intended.
## Who can use this feature?
Proxy server maintainers or firewall maintainers
## In this article
  * [Further reading](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/configuring-your-proxy-server-or-firewall-for-copilot#further-reading)
  * [Footnotes](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/configuring-your-proxy-server-or-firewall-for-copilot#footnote-label)


If your company employs security measures like a firewall or proxy server, you should add the following URLs, ports, and protocols to an allowlist to ensure Copilot works as expected:
Domain and/or URL | Purpose  
---|---  
`https://github.com/login/*` | Authentication  
`https://github.com/enterprises/YOUR-ENTERPRISE/*` | Authentication for managed user accounts, only required with Enterprise Managed Users  
`https://api.github.com/user` | User Management  
`https://api.github.com/copilot_internal/*` | User Management  
`https://copilot-telemetry.githubusercontent.com/telemetry` | Telemetry  
`https://default.exp-tas.com` | Telemetry  
`https://copilot-proxy.githubusercontent.com` | API service for Copilot suggestions  
`https://origin-tracker.githubusercontent.com` | API service for Copilot suggestions  
`https://*.githubcopilot.com`[1](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/configuring-your-proxy-server-or-firewall-for-copilot#user-content-fn-1) | API service for Copilot suggestions  
`https://*.individual.githubcopilot.com`[2](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/configuring-your-proxy-server-or-firewall-for-copilot#user-content-fn-2) | API service for Copilot suggestions  
`https://*.business.githubcopilot.com`[3](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/configuring-your-proxy-server-or-firewall-for-copilot#user-content-fn-3) | API service for Copilot suggestions  
`https://*.enterprise.githubcopilot.com`[4](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/configuring-your-proxy-server-or-firewall-for-copilot#user-content-fn-4) | API service for Copilot suggestions  
Depending on the security policies and editors your organization uses, you may need to allowlist additional domains and URLs. For more information on specific editors, see [Further reading](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/configuring-your-proxy-server-or-firewall-for-copilot#further-reading).
Every user of the proxy server or firewall also needs to configure their own environment to connect to Copilot. See [Configuring network settings for GitHub Copilot](https://docs.github.com/en/copilot/configuring-github-copilot/configuring-network-settings-for-github-copilot).
## [Further reading](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/configuring-your-proxy-server-or-firewall-for-copilot#further-reading)
  * [Network Connections in Visual Studio Code](https://code.visualstudio.com/docs/setup/network) in the Visual Studio documentation
  * [Install and use Visual Studio and Azure Services behind a firewall or proxy server](https://learn.microsoft.com/en-us/visualstudio/install/install-and-use-visual-studio-behind-a-firewall-or-proxy-server) in the Microsoft documentation


## [Footnotes](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/configuring-your-proxy-server-or-firewall-for-copilot#footnote-label)
  1. Allows access to authorized users regardless of Copilot plan. Do not add this URL to your allowlist if you are using subscription-based network routing. For more information on subscription-based network routing, see [Managing GitHub Copilot access to your enterprise's network](https://docs.github.com/en/copilot/managing-copilot/managing-copilot-for-your-enterprise/managing-access-to-copilot-in-your-enterprise/managing-github-copilot-access-to-your-enterprises-network). [↩](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/configuring-your-proxy-server-or-firewall-for-copilot#user-content-fnref-1)
  2. Allows access to authorized users via a Copilot Individual plan. Do not add this URL to your allowlist if you are using subscription-based network routing. [↩](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/configuring-your-proxy-server-or-firewall-for-copilot#user-content-fnref-2)
  3. Allows access to authorized users via a Copilot Business plan. Do not add this URL to your allowlist if you want to use subscription-based network routing to block users from using Copilot Business on your network. [↩](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/configuring-your-proxy-server-or-firewall-for-copilot#user-content-fnref-3)
  4. Allows access to authorized users via a Copilot Enterprise plan. Do not add this URL to your allowlist if you want to use subscription-based network routing to block users from using Copilot Enterprise on your network. [↩](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/configuring-your-proxy-server-or-firewall-for-copilot#user-content-fnref-4)


