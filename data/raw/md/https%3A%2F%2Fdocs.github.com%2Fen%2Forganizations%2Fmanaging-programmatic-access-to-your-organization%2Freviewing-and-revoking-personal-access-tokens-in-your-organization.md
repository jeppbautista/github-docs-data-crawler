  * [Organizations](https://docs.github.com/en/organizations "Organizations")/
  * [Manage programmatic access](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization "Manage programmatic access")/
  * [Review token access](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/reviewing-and-revoking-personal-access-tokens-in-your-organization "Review token access")


# Reviewing and revoking personal access tokens in your organization
Organization owners can review the fine-grained personal access tokens that can access their organization. They can also revoke access of specific fine-grained personal access tokens.
## In this article
  * [About reviewing and revoking fine-grained personal access tokens](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/reviewing-and-revoking-personal-access-tokens-in-your-organization#about-reviewing-and-revoking-fine-grained-personal-access-tokens)
  * [Reviewing and revoking fine-grained personal access tokens](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/reviewing-and-revoking-personal-access-tokens-in-your-organization#reviewing-and-revoking-fine-grained-personal-access-tokens)


## [About reviewing and revoking fine-grained personal access tokens](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/reviewing-and-revoking-personal-access-tokens-in-your-organization#about-reviewing-and-revoking-fine-grained-personal-access-tokens)
Organization owners can view all fine-grained personal access tokens that can access resources owned by the organization. Organization owners can also revoke access by fine-grained personal access tokens. When a fine-grained personal access token is revoked, SSH keys created by the token will continue to work and the token will still be able to read public resources within the organization.
When a token is revoked, the user who created the token will receive an email notification.
Organization owners can only view and revoke fine-grained personal access tokens in this UI, not personal access tokens (classic). Unless the organization has restricted access by personal access tokens (classic), any personal access token (classic) can access organization resources until the token expires. For more information about restricting access by personal access tokens (classic), see [Setting a personal access token policy for your organization](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/setting-a-personal-access-token-policy-for-your-organization).
Organization owners can also use the REST API to review and revoke fine-grained personal access tokens. These endpoints can only be called by GitHub Apps, and cannot be called with personal access tokens or OAuth apps. For more information, see [REST API endpoints for organizations](https://docs.github.com/en/rest/orgs/orgs#list-fine-grained-personal-access-tokens-with-access-to-organization-resources).
## [Reviewing and revoking fine-grained personal access tokens](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/reviewing-and-revoking-personal-access-tokens-in-your-organization#reviewing-and-revoking-fine-grained-personal-access-tokens)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the left sidebar, under **Active tokens**. Any fine-grained personal access tokens that can access your organization will be displayed.
  4. Click the name of the token that you want review or revoke.
  5. Review the access and permissions that the token has.
  6. To revoke access by the token to the organization, click **Revoke**.


Alternatively, you can revoke multiple tokens at once:
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the left sidebar, under **Active tokens**. Any fine-grained personal access tokens that can access your organization will be displayed.
  4. Optionally, use filters to only display certain tokens. 
     * Use the **Owner** dropdown to filter the tokens by the member who created the token.
     * Use the **Repository** dropdown to filter the tokens by repository access.
     * Use the **Permissions** dropdown to filter the tokens by permission.
  5. Select each token that you want to revoke.
  6. Select the **tokens selected...** dropdown menu and click **Revoke...**.


