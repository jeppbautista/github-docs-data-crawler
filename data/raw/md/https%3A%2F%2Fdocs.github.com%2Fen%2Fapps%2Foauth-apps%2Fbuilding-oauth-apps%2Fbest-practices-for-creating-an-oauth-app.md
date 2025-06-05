  * [Apps](https://docs.github.com/en/apps "Apps")/
  * [OAuth apps](https://docs.github.com/en/apps/oauth-apps "OAuth apps")/
  * [Building OAuth apps](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps "Building OAuth apps")/
  * [Best practices](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/best-practices-for-creating-an-oauth-app "Best practices")


# Best practices for creating an OAuth app
Follow these best practices to improve the security and performance of your OAuth app.
## In this article
  * [Use a GitHub App instead](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/best-practices-for-creating-an-oauth-app#use-a-github-app-instead)
  * [Use minimal scopes](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/best-practices-for-creating-an-oauth-app#use-minimal-scopes)
  * [Authorize thoroughly and durably](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/best-practices-for-creating-an-oauth-app#authorize-thoroughly-and-durably)
  * [Secure your app's credentials](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/best-practices-for-creating-an-oauth-app#secure-your-apps-credentials)
  * [Use the appropriate token type](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/best-practices-for-creating-an-oauth-app#use-the-appropriate-token-type)
  * [Make a plan for handling security breaches](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/best-practices-for-creating-an-oauth-app#make-a-plan-for-handling-security-breaches)
  * [Conduct regular vulnerability scans](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/best-practices-for-creating-an-oauth-app#conduct-regular-vulnerability-scans)
  * [Choose an appropriate environment](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/best-practices-for-creating-an-oauth-app#choose-an-appropriate-environment)
  * [Use services in a secure manner](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/best-practices-for-creating-an-oauth-app#use-services-in-a-secure-manner)
  * [Add logging and monitoring](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/best-practices-for-creating-an-oauth-app#add-logging-and-monitoring)
  * [Enable data deletion](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/best-practices-for-creating-an-oauth-app#enable-data-deletion)
  * [Further reading](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/best-practices-for-creating-an-oauth-app#further-reading)


## [Use a GitHub App instead](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/best-practices-for-creating-an-oauth-app#use-a-github-app-instead)
If possible, consider using a GitHub App instead of an OAuth app. In general, GitHub Apps are preferred over OAuth apps. GitHub Apps use fine-grained permissions, give the user more control over which repositories the app can access, and use short-lived tokens. These properties can harden the security of your app by limiting the damage that could be done if your app's credentials are leaked.
Similar to OAuth apps, GitHub Apps can still use OAuth 2.0 and generate a type of OAuth token (called a user access token) and take actions on behalf of a user. However, GitHub Apps can also act independently of a user.
For more information about GitHub Apps, see [About creating GitHub Apps](https://docs.github.com/en/apps/creating-github-apps/setting-up-a-github-app/about-creating-github-apps).
For more information about migrating an existing OAuth app to a GitHub App, see [Migrating OAuth apps to GitHub Apps](https://docs.github.com/en/apps/creating-github-apps/guides/migrating-oauth-apps-to-github-apps).
## [Use minimal scopes](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/best-practices-for-creating-an-oauth-app#use-minimal-scopes)
Your OAuth app should only request the scopes that the app needs to perform its intended functionality. If any tokens for your app become compromised, this will limit the amount of damage that can occur. For more information, see [Authorizing OAuth apps](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps).
## [Authorize thoroughly and durably](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/best-practices-for-creating-an-oauth-app#authorize-thoroughly-and-durably)
After signing in a user, app developers must take additional steps to ensure that the user is meant to have access to the data in your system. Each sign in requires fresh checks around their memberships, access, and their current SSO status.
### [Use the durable, unique `id` to store the user](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/best-practices-for-creating-an-oauth-app#use-the-durable-unique-id-to-store-the-user)
When a user signs in and performs actions in your application, you have to remember which user took that action in order to grant them access to the same resources the next time they sign in.
To store users in your database correctly, always use the `id` of the user. This value will never change for the user or be used to point to a different user, so it ensures you are providing access to the user you intend. You can find a user's `id` with the `GET /user` REST API endpoint. See [REST API endpoints for users](https://docs.github.com/en/rest/users/users#get-a-user).
If you store references to repositories, organizations, and enterprises, use their `id` as well to ensure your links to them remain accurate.
_Never_ use identifiers that can change over time, including user handles, organization slugs, or email addresses.
### [Validate organization access for every new authentication](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/best-practices-for-creating-an-oauth-app#validate-organization-access-for-every-new-authentication)
When you sign in a user, you should track which organizations the user's token is authorized for. This can change over time after sign in as users are removed from organizations. If an organization uses SAML SSO and a user has not performed SAML SSO, the user access token will not have access to that organization. You should use the `GET /user/installations` REST API endpoint regularly to verify which organizations a user access token has access to. If the user is not authorized to access an organization, you should prevent their access to organization owned data within your own application until they perform SAML SSO or rejoin the organization. For more information, see [REST API endpoints for GitHub App installations](https://docs.github.com/en/rest/apps/installations#list-app-installations-accessible-to-the-user-access-token).
### [Store user data with organizational and enterprise contexts](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/best-practices-for-creating-an-oauth-app#store-user-data-with-organizational-and-enterprise-contexts)
Beyond tracking user identity via the `id` field, you should retain data for the organization or enterprise each user is operating under. This will help ensure you don't leak sensitive information if a user switches roles.
For example:
  1. A user is in the `Mona` organization, which requires SAML SSO, and signs into your app after performing SSO. Your app now has access to whatever the user does within `Mona`.
  2. The user pulls a bunch of code out of a repository in `Mona` and saves it in your app for analysis.
  3. Later, the user switches jobs, and is removed from the `Mona` organization.


When the user accesses your app, can they still see the code and analysis from the `Mona` organization in their user account?
This is why it's critical to track the source of the data that your app is saving. Otherwise, your app is a data protection threat for organizations, and they're likely to ban your app if they can't trust that your app correctly protects their data.
### [Verify a user's access to your app](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/best-practices-for-creating-an-oauth-app#verify-a-users-access-to-your-app)
Your OAuth app can be accessed by users outside your organization or enterprise. If you intend an app to be used only by members of your organization or enterprise, you should check the user's membership status when the user signs in to your app.
To find the list of organizations a user is a member of, you can use the "List organizations for the authenticated user" endpoint. Then you can validate this list against a list of approved organizations for your app. For more information, see [REST API endpoints for organizations](https://docs.github.com/en/rest/orgs/orgs#list-organizations-for-the-authenticated-user).
## [Secure your app's credentials](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/best-practices-for-creating-an-oauth-app#secure-your-apps-credentials)
With a client secret, your app can authorize a user and generate user access tokens. These tokens can be used to make API requests on behalf of a user.
You must store your app's client secret and any generated tokens securely. The storage mechanism depends on your integrations architecture and the platform that it runs on. In general, you should use a storage mechanism that is intended to store sensitive data on the platform that you are using.
### [Client secrets](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/best-practices-for-creating-an-oauth-app#client-secrets)
If your app is a website or web app, consider storing your client secret in a key vault, such as [Azure Key Vault](https://azure.microsoft.com/products/key-vault), or as an encrypted environment variable or secret on your server.
If your app is a native client, client-side app, or runs on a user device (as opposed to running on your servers), you cannot secure your client secret. You should use caution if you plan to gate access to your own services based on tokens generated by your app, because anyone can access the client secret to generate a token.
### [User access tokens](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/best-practices-for-creating-an-oauth-app#user-access-tokens)
If your app is a website or web app, you should encrypt the tokens on your back end and ensure there is security around the systems that can access the tokens. Consider storing refresh tokens in a separate place from active access tokens.
If your app is a native client, client-side app, or runs on a user device (as opposed to running on your servers), you may not be able to secure tokens as well as an app that runs on your servers. You should store tokens via the mechanism recommended for your app's platform, and keep in mind that the storage mechanism may not be fully secure.
## [Use the appropriate token type](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/best-practices-for-creating-an-oauth-app#use-the-appropriate-token-type)
OAuth apps can generate user access tokens in order to make authenticated API requests. Your app should never use a personal access token or GitHub password to authenticate.
## [Make a plan for handling security breaches](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/best-practices-for-creating-an-oauth-app#make-a-plan-for-handling-security-breaches)
You should have a plan in place so that you can handle any security breaches in a timely manner.
In the event that your app's client secret is compromised, you will need to generate a new secret, update your app to use the new secret, and delete your old secret.
In the event that user access tokens are compromised, you should immediately revoke these tokens. For more information, see [REST API endpoints for OAuth authorizations](https://docs.github.com/en/rest/apps/oauth-applications#delete-an-app-token).
## [Conduct regular vulnerability scans](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/best-practices-for-creating-an-oauth-app#conduct-regular-vulnerability-scans)
You should conduct regular vulnerability scans for your app. For example, you might set up code scanning and secret scanning for the repository that hosts your app's code. For more information, see [About code scanning](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning) and [About secret scanning](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning).
## [Choose an appropriate environment](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/best-practices-for-creating-an-oauth-app#choose-an-appropriate-environment)
If your app runs on a server, verify that your server environment is secure and that it can handle the volume of traffic that you expect for your app.
## [Use services in a secure manner](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/best-practices-for-creating-an-oauth-app#use-services-in-a-secure-manner)
If your app uses third-party services, they should be used in a secure manner:
  * Any services used by your app should have a unique login and password.
  * Apps should not share service accounts such as email or database services to manage your SaaS service.
  * Only employees with administrative duties should have admin access to the infrastructure that hosts your app.


## [Add logging and monitoring](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/best-practices-for-creating-an-oauth-app#add-logging-and-monitoring)
Consider adding logging and monitoring capabilities for your app. A security log could include:
  * Authentication and authorization events
  * Service configuration changes
  * Object reads and writes
  * User and group permission changes
  * Elevation of role to admin


Your logs should use consistent timestamping for each event and should record the users, IP addresses, or hostnames for all logged events.
## [Enable data deletion](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/best-practices-for-creating-an-oauth-app#enable-data-deletion)
If your app is available to other users, you should give users a way to delete their data. Users should not need to email or call a support person in order to delete their data.
## [Further reading](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/best-practices-for-creating-an-oauth-app#further-reading)
  * [Security best practices for apps on GitHub Marketplace](https://docs.github.com/en/apps/publishing-apps-to-github-marketplace/creating-apps-for-github-marketplace/security-best-practices-for-apps)
  * [Customer experience best practices for apps](https://docs.github.com/en/apps/publishing-apps-to-github-marketplace/creating-apps-for-github-marketplace/customer-experience-best-practices-for-apps)


