  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Build Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions "Build Copilot Extensions")/
  * [Extensions FAQ](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-faq "Extensions FAQ")


# Copilot Extensions FAQ
Find answers to common questions about GitHub Copilot Extensions.
## In this article
  * [General](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-faq#general)
  * [Data and Permissions](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-faq#data-and-permissions)
  * [Policies](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-faq#policies)


## [General](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-faq#general)
This section answers common questions about GitHub Copilot Extensions.
  * [What is the difference between a GitHub Copilot Extension and a Visual Studio Code chat participant?](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-faq#what-is-the-difference-between-a-github-copilot-extension-and-a-visual-studio-code-chat-participant)
  * [Is indemnity provided for Copilot Extensions?](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-faq#is-indemnity-provided-for-copilot-extensions)


### [What is the difference between a GitHub Copilot Extension and a Visual Studio Code chat participant?](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-faq#what-is-the-difference-between-a-github-copilot-extension-and-a-visual-studio-code-chat-participant)
GitHub Copilot Extensions and Visual Studio Code chat participants use the same backend platform to route requests to extensions. Both provide similar end-user experiences, integrate with Copilot Chat, and can leverage the Copilot API or other LLMs.
While they share similarities, below are several key differences:
  * GitHub Copilot Extensions and Visual Studio Code chat participants are accessed through different marketplaces.
  * GitHub Copilot Extensions are server-side extensions, requiring server infrastructure to build. These extensions provide a built-in connection to your GitHub workspaces, as set by your organization admin.
  * Visual Studio Code chat participants are client-side extensions that have read and write access to your local files. They do not require server infrastructure.
  * GitHub Copilot Extensions can be used in any editor where extensions are supported, while Visual Studio Code Chat Participants are only available in Visual Studio Code.


For more information, see [About building Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions).
### [Is indemnity provided for Copilot Extensions?](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-faq#is-indemnity-provided-for-copilot-extensions)
No, Copilot Extensions are not covered by GitHub Copilot’s indemnity policy. However, this exclusion applies only to issues that arise within extension chat threads.
Installing and using extensions does not affect indemnity coverage for any issues that occur while using other Copilot features such as code completion and chat.
## [Data and Permissions](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-faq#data-and-permissions)
This section explains what data is collected and shared when using Copilot Extensions.
  * [What data is being collected and shared with Copilot Extensions?](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-faq#what-data-is-being-collected-and-shared-with-copilot-extensions)
  * [What permissions are required for Copilot Extensions?](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-faq#what-permissions-are-required-for-copilot-extensions)
  * [Who can provide permissions for Copilot Extensions to access organization resources?](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-faq#who-can-provide-permissions-for-copilot-extensions-to-access-organization-resources)
  * [Can a user use Copilot Extensions that the organization has not provided permissions for?](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-faq#can-a-user-use-copilot-extensions-that-the-organization-has-not-provided-permissions-for)


### [What data is being collected and shared with Copilot Extensions?](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-faq#what-data-is-being-collected-and-shared-with-copilot-extensions)
The following data is shared when interacting with Copilot Extensions:
  * Data attached to your account and Copilot Chat usage, such as GitHub user ID, and timestamps of messages.
  * Past messages within the chat thread where you are invoking an extension. Only one extension can be used per thread, preventing data sharing across extensions. The data retention period for thread context is 30 days.
  * Any additional organization and repository data that is authorized for the extension by your organization admin. Admins installing extensions must approve access to the required permissions prior to completing installation.
  * For Copilot Chat in GitHub, if your admin has approved the extension to access repository or organization metadata , that data will be shared as well.


### [What permissions are required for Copilot Extensions?](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-faq#what-permissions-are-required-for-copilot-extensions)
Permissions vary by extension, depending on the level of authorization that the extension requires in order to respond to your query. You can view the required permissions on the extension’s installation page, located after the billing information step and before the install and authorize step.
**For developers** : At a minimum, the **Copilot Chat** permissions must be set to "Read-only". Additional permissions may include executing write actions on other surfaces and authorizing read access to repository and organization level data in GitHub.
**For builders** : In addition to the above, you may also request local context from a user’s editor to further tailor responses. To do so, the **Copilot Editor Context** permissions must be set to "Read-only". Users will be notified to provide the required authorization.
For more information on GitHub App permissions, see [Choosing permissions for a GitHub App](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app)
### [Who can provide permissions for Copilot Extensions to access organization resources?](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-faq#who-can-provide-permissions-for-copilot-extensions-to-access-organization-resources)
Only organization admins can grant permissions for Copilot Extensions to access organization resources. Organization members may encounter cases where an extension cannot access a repository or query context. This typically happens because the organization admin has not yet provided permissions or authorized the extension. See [Granting permissions to access organization resources](https://docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions#granting-permissions-to-access-organization-resources).
### [Can a user use Copilot Extensions that the organization has not provided permissions for?](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-faq#can-a-user-use-copilot-extensions-that-the-organization-has-not-provided-permissions-for)
Yes, any user can install and use Copilot Extensions. However, to query organization resources and repositories, an extension must be installed and authorized by an organization admin. See [Granting permissions to access organization resources](https://docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions#granting-permissions-to-access-organization-resources).
Users should contact their organization admin to request installation and authorization. Company context cannot be accessed without admin permissions.
## [Policies](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-faq#policies)
This section covers administrative policies for Copilot Extensions
  * [How do I control which Copilot Extensions can be used in my enterprise?](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-faq#how-do-i-control-which-copilot-extensions-can-be-used-in-my-enterprise)
  * [Is there an allowlist/blocklist at the enterprise level?](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-faq#is-there-an-allowlistblocklist-at-the-enterprise-level)
  * [As a member of an organization, how can I get access to Copilot Extensions?](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-faq#as-a-member-of-an-organization-how-can-i-get-access-to-copilot-extensions)


### [How do I control which Copilot Extensions can be used in my enterprise?](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-faq#how-do-i-control-which-copilot-extensions-can-be-used-in-my-enterprise)
Enterprise admins can disable Copilot Extensions across their enterprise by setting the **Copilot Extensions** policy to "Disabled" or "No Policy".
### [Is there an allowlist/blocklist at the enterprise level?](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-faq#is-there-an-allowlistblocklist-at-the-enterprise-level)
No, there is no allowlist or blocklist at the enterprise level.
### [As a member of an organization, how can I get access to Copilot Extensions?](https://docs.github.com/en/copilot/building-copilot-extensions/copilot-extensions-faq#as-a-member-of-an-organization-how-can-i-get-access-to-copilot-extensions)
To access Copilot Extensions as a member of an organization, the organization that assigned you a GitHub seat must enable the Copilot Extensions policy. Additionally, the same organization must install and authorize the extension to access any organization owned repositories.
For example, if you are a member of multiple organizations and Organization A has assigned you a GitHub seat, you will only have access to extensions if Organization A has enabled the policy. If Organization B has enabled extensions but you do not have access, it is because Organization A has disabled the Copilot Extensions policy.
