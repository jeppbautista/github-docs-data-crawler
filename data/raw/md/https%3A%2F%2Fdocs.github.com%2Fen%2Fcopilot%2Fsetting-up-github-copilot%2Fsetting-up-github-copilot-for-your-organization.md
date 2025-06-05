  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Set up](https://docs.github.com/en/copilot/setting-up-github-copilot "Set up")/
  * [Set up for organization](https://docs.github.com/en/copilot/setting-up-github-copilot/setting-up-github-copilot-for-your-organization "Set up for organization")


# Setting up GitHub Copilot for your organization
Follow these steps to set up GitHub Copilot in your organization.
## Who can use this feature?
Organization owners
Organizations with a Copilot Enterprise or Copilot Business plan
## In this article
  * [1. Subscribe your organization to GitHub Copilot](https://docs.github.com/en/copilot/setting-up-github-copilot/setting-up-github-copilot-for-your-organization#1-subscribe-your-organization-to-github-copilot)
  * [2. Set policies](https://docs.github.com/en/copilot/setting-up-github-copilot/setting-up-github-copilot-for-your-organization#2-set-policies)
  * [3. Set up networking (if necessary)](https://docs.github.com/en/copilot/setting-up-github-copilot/setting-up-github-copilot-for-your-organization#3-set-up-networking-if-necessary)
  * [4. Grant access to members](https://docs.github.com/en/copilot/setting-up-github-copilot/setting-up-github-copilot-for-your-organization#4-grant-access-to-members)
  * [5. Drive Copilot adoption](https://docs.github.com/en/copilot/setting-up-github-copilot/setting-up-github-copilot-for-your-organization#5-drive-copilot-adoption)
  * [6. Enhance the Copilot experience](https://docs.github.com/en/copilot/setting-up-github-copilot/setting-up-github-copilot-for-your-organization#6-enhance-the-copilot-experience)


## [1. Subscribe your organization to GitHub Copilot](https://docs.github.com/en/copilot/setting-up-github-copilot/setting-up-github-copilot-for-your-organization#1-subscribe-your-organization-to-github-copilot)
Set up a Copilot Business plan for your organization. See [Subscribing to Copilot for your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/subscribing-to-copilot-for-your-organization).
If your organization is part of an enterprise with a Copilot Enterprise or Copilot Business plan, your enterprise owner can instead enable Copilot for your organization. You can request access from your enterprise owner by going to <https://github.com/settings/copilot> and requesting access under "Get Copilot from an organization."
## [2. Set policies](https://docs.github.com/en/copilot/setting-up-github-copilot/setting-up-github-copilot-for-your-organization#2-set-policies)
Control which Copilot features are available in your organization. See [Managing policies for Copilot in your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-github-copilot-features-in-your-organization/managing-policies-for-copilot-in-your-organization).
## [3. Set up networking (if necessary)](https://docs.github.com/en/copilot/setting-up-github-copilot/setting-up-github-copilot-for-your-organization#3-set-up-networking-if-necessary)
If your organization members connect through an HTTP proxy server or firewall, ensure that key URLs are added to the allowlist for the proxy server or firewall. See [Configuring your proxy server or firewall for Copilot](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/configuring-your-proxy-server-or-firewall-for-copilot).
You may also need to install custom SSL certificates on your members' machines. See [Configuring network settings for GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-network-settings-for-github-copilot#-installing-custom-certificates).
## [4. Grant access to members](https://docs.github.com/en/copilot/setting-up-github-copilot/setting-up-github-copilot-for-your-organization#4-grant-access-to-members)
Enable Copilot for some or all members of your organization. See [Granting access to Copilot for members of your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-access-to-github-copilot-in-your-organization/granting-access-to-copilot-for-members-of-your-organization).
To help drive adoption of Copilot in your organization, think about what teams or members are most excited about Copilot or could benefit the most from Copilot. You may want to enable Copilot for those members before enabling Copilot for your whole organization. This can help you discover blockers, demonstrate early success, and set your organization up for a successful Copilot rollout.
GitHub has found that many successful rollouts offer a fully self-service model where developers can claim a license without approval. To learn about options for setting up this process, see [Setting up a self-serve process for GitHub Copilot licenses](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/setting-up-a-self-serve-process-for-github-copilot-licenses).
If your organization is part of an enterprise on GHE.com, users must perform some additional setup to authenticate to their account from their development environment. See [Using GitHub Copilot with an account on GHE.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/using-github-copilot-with-an-account-on-ghecom).
## [5. Drive Copilot adoption](https://docs.github.com/en/copilot/setting-up-github-copilot/setting-up-github-copilot-for-your-organization#5-drive-copilot-adoption)
Planning and implementing an effective enablement process is essential to drive adoption of Copilot in your organization. See [Driving Copilot adoption in your company](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/driving-copilot-adoption-in-your-company).
## [6. Enhance the Copilot experience](https://docs.github.com/en/copilot/setting-up-github-copilot/setting-up-github-copilot-for-your-organization#6-enhance-the-copilot-experience)
Enhance the Copilot experience for your organization by:
  * **Setting up knowledge bases** for use with Copilot Chat _(Copilot Enterprise only)_. See [Managing Copilot knowledge bases](https://docs.github.com/en/enterprise-cloud@latest/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-github-copilot-features-in-your-organization/managing-copilot-knowledge-bases).
  * **Fine tuning Copilot** by creating a custom large language model. See [Creating a custom model for GitHub Copilot](https://docs.github.com/en/copilot/customizing-copilot/creating-a-custom-model-for-github-copilot).
  * **Installing Copilot Extensions** to integrate other tools with Copilot Chat. See [Extending the capabilities of GitHub Copilot in your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-github-copilot-features-in-your-organization/installing-github-copilot-extensions-for-your-organization).
  * **Adding Copilot coding agent** as a team member to work asynchronously on issues. See [Using Copilot coding agent effectively in your organization](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/enabling-developers/using-copilot-coding-agent-in-org).


