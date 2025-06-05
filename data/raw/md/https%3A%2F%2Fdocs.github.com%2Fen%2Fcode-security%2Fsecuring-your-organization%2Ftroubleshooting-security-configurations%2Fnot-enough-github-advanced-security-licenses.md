  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secure your organization](https://docs.github.com/en/code-security/securing-your-organization "Secure your organization")/
  * [Troubleshooting configurations](https://docs.github.com/en/code-security/securing-your-organization/troubleshooting-security-configurations "Troubleshooting configurations")/
  * [Not enough GHAS licenses](https://docs.github.com/en/code-security/securing-your-organization/troubleshooting-security-configurations/not-enough-github-advanced-security-licenses "Not enough GHAS licenses")


# Not enough GitHub Advanced Security licenses
If you are on a subscription-based billing model for GHAS, you need available GHAS licenses to enable GHAS features on a private repository.
## Who can use this feature?
Organization owners, security managers, and organization members with the **admin** role
If you are on a volume / subscription-based billing model for GitHub Advanced Security (GHAS), you must have an available GHAS license for any additional unique active committers to enable GHAS features on a private repository. To learn about GHAS licensing, as well as unique and active committers, see [About billing for GitHub Advanced Security](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-advanced-security/about-billing-for-github-advanced-security).
If you try to apply a security configuration with GHAS features to your repositories and don't have enough GHAS licenses, the configuration will only be successfully applied to public repositories. For private repositories, only free security features will be enabled due to the license limitation, resulting in the following outcomes:
  * Free security features enabled in the configuration _will_ be enabled for _all_ private repositories.
  * GHAS features _will not_ be enabled for _any_ private repositories.
  * The security configuration _will not_ be applied to _any_ private repositories, since only some features from the configuration are enabled.


For more information on managing GHAS licenses for your organization, see [Managing your paid use of Advanced Security](https://docs.github.com/en/code-security/securing-your-organization/managing-the-security-of-your-organization/managing-your-github-advanced-security-license-usage).
