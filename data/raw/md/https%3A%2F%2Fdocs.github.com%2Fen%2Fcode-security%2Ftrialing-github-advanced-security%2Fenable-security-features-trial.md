  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Trial GitHub Advanced Security](https://docs.github.com/en/code-security/trialing-github-advanced-security "Trial GitHub Advanced Security")/
  * [Enable security features in trial](https://docs.github.com/en/code-security/trialing-github-advanced-security/enable-security-features-trial "Enable security features in trial")


# Enabling security features in your trial enterprise
Quickly create an enterprise-level configuration and apply Secret Protection and Code Security features across all repositories in your trial enterprise.
## Who can use this feature?
Enterprise owners and members with the **admin** role
## In this article
  * [Step 1: Create an enterprise security configuration for your trial goals](https://docs.github.com/en/code-security/trialing-github-advanced-security/enable-security-features-trial#step-1-create-an-enterprise-security-configuration-for-your-trial-goals)
  * [Step 2: Apply your enterprise security configuration to repositories](https://docs.github.com/en/code-security/trialing-github-advanced-security/enable-security-features-trial#step-2-apply-your-enterprise-security-configuration-to-repositories)
  * [Next steps](https://docs.github.com/en/code-security/trialing-github-advanced-security/enable-security-features-trial#next-steps)


This article assumes that you have planned and then started a trial of GitHub Advanced Security. For more information, see [Planning a trial of GitHub Advanced Security](https://docs.github.com/en/code-security/trialing-github-advanced-security/planning-a-trial-of-ghas).
The aim is to enable all the security features you want to trial quickly, as a starting point for deeper exploration. You should start getting results soon on the repositories in your trial enterprise and you can fine-tune the configuration later.
## [Step 1: Create an enterprise security configuration for your trial goals](https://docs.github.com/en/code-security/trialing-github-advanced-security/enable-security-features-trial#step-1-create-an-enterprise-security-configuration-for-your-trial-goals)
When you planned your trial, you identified the features that you want to test and any enforcement needs. You should create one or more security configurations for your enterprise that enable these features and set any enforcement levels you require.
  1. In the top-right corner of GitHub, click your profile photo.
  2. Depending on your environment, click **Your enterprise** , or click **Your enterprises** then click your trial enterprise.
  3. On the left side of the page, in the enterprise account sidebar, click **Settings**.
  4. In the left sidebar, click 
  5. Click **New configuration** to create a new configuration.
  6. Give the configuration a meaningful name and description.
  7. You will see that most features are already enabled. Review the features that are **Not set** and enable any that you want to trial, for example: "Automatic dependency submission."
  8. In the "Policy" area, set the "Use as default for newly created repositories" option as needed to define whether or not to apply the configuration to new repositories created in the enterprise.
  9. In the "Policy" area, notice that the "Enforce configuration" option is set to **Enforce** so that applying the configuration to a repository enforces all settings apart from any left as "Not set". 
While you are testing Advanced Security, you may want to change this to **Don't enforce** to allow you to optimize repository settings as needed without modifying security configurations.
  10. When you have finished defining the configuration, click **Save configuration**.


The new enterprise security configuration is now available for use at the enterprise level and also within every organization in the enterprise.
## [Step 2: Apply your enterprise security configuration to repositories](https://docs.github.com/en/code-security/trialing-github-advanced-security/enable-security-features-trial#step-2-apply-your-enterprise-security-configuration-to-repositories)
You can apply an enterprise security configuration either at the enterprise level or at the organization level. The best option for you will depend on whether or not you want to apply the configuration to all repositories in the enterprise, or to a subset of repositories.
Although Secret Protection and Code Security are free of charge during trials, you will be charged for any actions minutes that you use. This includes actions minutes used by the default code scanning setup or by any other workflows you run.
  * Enterprise-level application: 
    * Add an enterprise configuration to all repositories in the enterprise, or all repositories without an existing configuration in the enterprise.
  * Organization-level application: 
    * Add an enterprise or an organization configuration to all repositories in the organization, or all repositories without an existing configuration in the organization.
    * Add an enterprise or an organization configuration to a subset of repositories in the organization.


You may find it helpful to apply an enterprise security configuration to all repositories in your enterprise, and then work at the organization-level to select a subset of repositories and apply an alternative security configuration.
### [Enterprise-level application](https://docs.github.com/en/code-security/trialing-github-advanced-security/enable-security-features-trial#enterprise-level-application)
  1. Open your trial enterprise.
  2. In the sidebar, click **Settings** and then **Advanced Security** to display the security configurations page.
  3. For the configuration you want to apply, click **Apply to** and choose whether to apply the configuration to all repositories in the enterprise or just to the repositories without an existing security configuration.


### [Organization-level application](https://docs.github.com/en/code-security/trialing-github-advanced-security/enable-security-features-trial#organization-level-application)
  1. Open an organization in your trial enterprise.
  2. Click the **Settings** tab to display the organization settings.
  3. In the sidebar, click **Advanced Security** and then **Configurations** to display the security configurations page.
  4. Optionally, select the **Apply to** dropdown menu and click either **All repositories** , to apply any configuration to all repositories in the organization, or **All repositories without configurations** , to configure just the repositories in the organization without an existing security configuration.
  5. Optionally, in the "Apply configurations" section use the "Search repositories" field or **Filter** button to filter repositories. Then select one or more repositories and use the **Apply configuration** button to choose a configuration to apply to those repositories.


For more information, see [Applying a custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/applying-a-custom-security-configuration).
## [Next steps](https://docs.github.com/en/code-security/trialing-github-advanced-security/enable-security-features-trial#next-steps)
Now that you have enabled the security features you want to test, you are ready to look more deeply into how GitHub Secret Protection and GitHub Code Security protect your code.
  1. [Exploring your enterprise trial of GitHub Secret Protection](https://docs.github.com/en/code-security/trialing-github-advanced-security/explore-trial-secret-scanning)
  2. [Exploring your enterprise trial of GitHub Code Security](https://docs.github.com/en/code-security/trialing-github-advanced-security/explore-trial-code-scanning)


