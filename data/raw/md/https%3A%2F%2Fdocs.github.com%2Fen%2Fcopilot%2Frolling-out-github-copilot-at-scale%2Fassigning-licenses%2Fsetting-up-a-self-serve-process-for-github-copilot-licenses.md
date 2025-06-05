  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Roll out Copilot at scale](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale "Roll out Copilot at scale")/
  * [Assigning licenses](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/assigning-licenses "Assigning licenses")/
  * [Self-serve licenses](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/assigning-licenses/setting-up-a-self-serve-process-for-github-copilot-licenses "Self-serve licenses")


# Setting up a self-serve process for GitHub Copilot licenses
Learn how users can request a license and receive access immediately.
## In this article
  * [Approach 1: Use GitHub's "request access" feature](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/assigning-licenses/setting-up-a-self-serve-process-for-github-copilot-licenses#approach-1-use-githubs-request-access-feature)
  * [Approach 2: Integrate with the API](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/assigning-licenses/setting-up-a-self-serve-process-for-github-copilot-licenses#approach-2-integrate-with-the-api)
  * [Further reading](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/assigning-licenses/setting-up-a-self-serve-process-for-github-copilot-licenses#further-reading)


When you've enabled GitHub Copilot in an organization or enterprise, you can set up a self-serve workflow to allow users to request licenses. This allows you to allocate licenses to people who want them, and means people can get started with Copilot quickly.
GitHub has found that many successful rollouts offer a fully self-service model where developers can claim a license without approval.
This article outlines two approaches your company can take:
  * GitHub's **request access** feature for Copilot Business, which requires no setup but does require explicit approvals from an administrator
  * Your own integration with **GitHub's API** , which allows you to create your own process with instant access


## [Approach 1: Use GitHub's "request access" feature](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/assigning-licenses/setting-up-a-self-serve-process-for-github-copilot-licenses#approach-1-use-githubs-request-access-feature)
If you have a Copilot Business plan, members of an organization can request access to GitHub Copilot on their settings page. Then, an organization owner must review and approve each request.
The process, which you should **communicate with users** , is as follows.
  1. An organization or enterprise owner ensures Copilot Business is enabled in the organization where you want to manage access.
  2. Members of the organization go to their personal settings page at <https://github.com/settings/copilot> and click **Ask admin for access**.
  3. An organization owner reviews and approves requests on the "Requests from members" page in the organization. See [Managing requests for Copilot Business in your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-access-to-github-copilot-in-your-organization/managing-requests-for-copilot-business-in-your-organization).


You should set up a process where requests are reviewed regularly, so that interested users can get access to Copilot quickly.
Users can also request access from organizations where Copilot Business is not enabled. In this case, organization owners will be prompted to ask an enterprise owner to enable Copilot for the organization.
## [Approach 2: Integrate with the API](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/assigning-licenses/setting-up-a-self-serve-process-for-github-copilot-licenses#approach-2-integrate-with-the-api)
For a more streamlined approach, you can set up a self-serve process by integrating with GitHub's API. The benefits of this approach are that it allows you to build the process into your existing tooling, and it gives you the option to allow users to receive access instantly, without a manual approval process.
To set up the integration, you will use the [Add users to the Copilot subscription for an organization](https://docs.github.com/en/rest/copilot/copilot-user-management#add-users-to-the-copilot-subscription-for-an-organization) endpoint, providing the username of the user who has requested access.
For example, the API call in a GitHub Actions workflow might look as follows, where the organization and selected usernames are provided by the context of the workflow trigger:
```
const { Octokit } = require("@octokit/action");
const octokit = new Octokit();
const response = await octokit.request('POST /orgs/{org}/copilot/billing/selected_users', {
  org: context.repo.owner,
  selected_usernames: [context.payload.sender.login],
  headers: {
    'X-GitHub-Api-Version': '2022-11-28'
  }
})

```

This endpoint only works if you use organizations on GitHub. If GitHub has provided you with a **dedicated enterprise for managing Copilot Business licenses** , you will need to add users to enterprise teams instead. To request API documentation, please contact your account manager.
### [Example implementations](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/assigning-licenses/setting-up-a-self-serve-process-for-github-copilot-licenses#example-implementations)
  * You could create the process entirely within GitHub, having users create issues to request access, then using a GitHub Actions workflow to call the API. For a demo of this approach, see the [microsoft/GitHubCopilotLicenseAssignment](https://github.com/microsoft/GitHubCopilotLicenseAssignment) repository. Note that this is **an external example that isn't covered by GitHub Support**.
  * You could add a "Request access" button to users' profiles on your company's internal website, which will pass the user's GitHub username to the API. You could grant access instantly or validate the user first, such as checking for their membership of a certain team.


## [Further reading](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/assigning-licenses/setting-up-a-self-serve-process-for-github-copilot-licenses#further-reading)
  * [Driving Copilot adoption in your company](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/driving-copilot-adoption-in-your-company)
  * [Reminding inactive users to use their GitHub Copilot license](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/reminding-inactive-users)
  * [Analyzing usage over time with the Copilot metrics API](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/analyzing-usage-over-time-with-the-copilot-metrics-api)
  * [Managing requests for Copilot Business from organizations in your enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-accounts-and-repositories/managing-organizations-in-your-enterprise/managing-requests-for-copilot-business-from-organizations-in-your-enterprise) in the GitHub Enterprise Cloud documentation


