  * [Organizations](https://docs.github.com/en/organizations "Organizations")/
  * [Manage programmatic access](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization "Manage programmatic access")/
  * [Set a token policy](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/setting-a-personal-access-token-policy-for-your-organization "Set a token policy")


# Setting a personal access token policy for your organization
Organization owners can control access to resources by applying policies to personal access tokens
## In this article
  * [Restricting access by personal access tokens](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/setting-a-personal-access-token-policy-for-your-organization#restricting-access-by-personal-access-tokens)
  * [Enforcing a maximum lifetime policy for personal access tokens](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/setting-a-personal-access-token-policy-for-your-organization#enforcing-a-maximum-lifetime-policy-for-personal-access-tokens)
  * [Enforcing an approval policy for fine-grained personal access tokens](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/setting-a-personal-access-token-policy-for-your-organization#enforcing-an-approval-policy-for-fine-grained-personal-access-tokens)


## [Restricting access by personal access tokens](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/setting-a-personal-access-token-policy-for-your-organization#restricting-access-by-personal-access-tokens)
Organization owners can prevent personal access tokens from accessing resources owned by the organization with the following options:
  * **Restrict access via personal access tokens:** Personal access tokens (classic) or fine-grained personal access tokens cannot access resources owned by the organization. SSH keys created by personal access tokens will continue to work.
  * **Allow access via personal access tokens:** Personal access tokens (classic) or fine-grained personal access tokens can access resources owned by the organization.


Regardless of the chosen policy, Personal access tokens will have access to public resources within the organization. By default, both Personal access tokens (classic) and fine-grained personal access tokens are enabled.
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the left sidebar, under **Settings**.
  4. Select either the **Fine-grained tokens** or **Tokens (classic)** tab to enforce this policy based on the token type.
  5. Under **Fine-grained personal access tokens** or **Restrict personal access tokens (classic) from accessing your organizations** , select your access policy.
  6. Click **Save**.


## [Enforcing a maximum lifetime policy for personal access tokens](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/setting-a-personal-access-token-policy-for-your-organization#enforcing-a-maximum-lifetime-policy-for-personal-access-tokens)
Organization owners can set maximum lifetime allowances for both fine-grained personal access tokens and personal access tokens (classic) to control access to organization resources.
For fine-grained personal access tokens, the default the maximum lifetime policy for organizations is set to expire within 366 days. Personal access tokens (classic) do not have an expiration requirement.
When you set a policy, tokens with non-compliant lifetimes will be blocked from accessing your organization if the token belongs to a member of your organization. Setting this policy does not revoke or disable these tokens. Users will learn that their existing token is non-compliant when API calls for your organization are rejected.
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the left sidebar, click 
  4. Select either the **Fine-grained tokens** or **Tokens (classic)** tab to enforce this policy based on the token type.
  5. Under **Set maximum lifetimes for personal access tokens** , set the maximum lifetime.
  6. Click **Save**.


## [Enforcing an approval policy for fine-grained personal access tokens](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/setting-a-personal-access-token-policy-for-your-organization#enforcing-an-approval-policy-for-fine-grained-personal-access-tokens)
Organization owners can manage approval requirements for each fine-grained personal access token that can access the organization with the following options:
  * **Require administrator approval:** An organization owner must approve each fine-grained personal access token that can access the organization. Fine-grained personal access tokens created by organization owners will not need approval. This is the default value.
  * **Do not require administrator approval:** Fine-grained personal access tokens created by organization members can access resources in the organization without prior approval.


Fine-grained personal access tokens will still be able to read public resources within the organization without approval.
Only fine-grained personal access tokens, not personal access tokens (classic), are subject to approval. Unless the organization has restricted access by personal access tokens (classic), any personal access token (classic) can access organization resources without prior approval. For more information, see [Restricting access by personal access tokens](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/setting-a-personal-access-token-policy-for-your-organization#restricting-access-by-personal-access-tokens) on this page.
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the left sidebar, under **Settings**.
  4. Select the **Fine-grained tokens** tab.
  5. Under **Require approval of fine-grained personal access tokens** , select the option that meets your needs:
  6. Click **Save**.


