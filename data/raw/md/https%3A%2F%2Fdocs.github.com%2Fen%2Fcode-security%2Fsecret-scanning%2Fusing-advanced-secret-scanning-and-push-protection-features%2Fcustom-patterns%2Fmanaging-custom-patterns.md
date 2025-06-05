  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secret scanning](https://docs.github.com/en/code-security/secret-scanning "Secret scanning")/
  * [Advanced features](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features "Advanced features")/
  * [Custom patterns](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns "Custom patterns")/
  * [Manage custom patterns](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/managing-custom-patterns "Manage custom patterns")


# Managing custom patterns
You can view, edit, and remove custom patterns, as well as enable push protection for custom patterns.
## Who can use this feature?
Repository owners, organization owners, security managers, enterprise administrators, and users with the **admin** role
## In this article
  * [Editing a custom pattern](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/managing-custom-patterns#editing-a-custom-pattern)
  * [Removing a custom pattern](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/managing-custom-patterns#removing-a-custom-pattern)
  * [Enabling push protection for a custom pattern](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/managing-custom-patterns#enabling-push-protection-for-a-custom-pattern)


Custom patterns are user-defined patterns that you can use to identify secrets that are not detected by the default patterns supported by secret scanning. For more information, see [Defining custom patterns for secret scanning](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/defining-custom-patterns-for-secret-scanning).
At the enterprise level, only the creator of a custom pattern can edit the pattern, and use it in a dry run. There are no similar restrictions for editing custom patterns at repository and organization level.
## [Editing a custom pattern](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/managing-custom-patterns#editing-a-custom-pattern)
When you save a change to a custom pattern, this closes all the secret scanning alerts that were created using the previous version of the pattern.
  1. Navigate to where the custom pattern was created. A custom pattern can be created in a repository, organization, or enterprise account.
     * For a repository or organization, display the "Advanced Security" settings for the repository or organization where the custom pattern was created. For more information, see [Defining a custom pattern for a repository](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/defining-custom-patterns-for-secret-scanning#defining-a-custom-pattern-for-a-repository) or [Defining a custom pattern for an organization](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/defining-custom-patterns-for-secret-scanning#defining-a-custom-pattern-for-an-organization).
     * For an enterprise, under "Policies" display the "Advanced Security" area, and then click **Security features**. For more information, see [Defining a custom pattern for an enterprise account](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/defining-custom-patterns-for-secret-scanning#defining-a-custom-pattern-for-an-enterprise-account).
  2. Under "Custom patterns", to the right of the custom pattern you want to edit, click 
  3. When you're ready to test your edited custom pattern, to identify matches without creating alerts, click **Save and dry run**.
  4. When you have reviewed and tested your changes, click **Publish changes**.
  5. Optionally, to enable push protection for your custom pattern, click **Enable**.
     * Push protection for custom patterns will only apply to repositories that have secret scanning as push protection enabled. For more information about enabling push protection, see [About push protection](https://docs.github.com/en/code-security/secret-scanning/protecting-pushes-with-secret-scanning).
     * Enabling push protection for commonly found custom patterns can be disruptive to contributors.
![Screenshot of custom pattern page with the button to enable push protection emphasized.](https://docs.github.com/assets/cb-20409/images/help/repository/secret-scanning-custom-pattern-enable-push-protection.png)
  6. Optionally, to disable push protection for your custom pattern, click **Disable**.
![Screenshot of the custom pattern page with the button to disable push protection highlighted with a dark orange outline.](https://docs.github.com/assets/cb-20669/images/help/repository/secret-scanning-disable-push-protection-custom-pattern.png)


## [Removing a custom pattern](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/managing-custom-patterns#removing-a-custom-pattern)
When you remove a custom pattern, GitHub gives you the option to close the secret scanning alerts relating to the pattern, or keep these alerts.
  1. Navigate to where the custom pattern was created. A custom pattern can be created in a repository, organization, or enterprise account. 
     * For a repository or organization, display the "Advanced Security" settings for the repository or organization where the custom pattern was created. For more information, see [Defining a custom pattern for a repository](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/defining-custom-patterns-for-secret-scanning#defining-a-custom-pattern-for-a-repository) or [Defining a custom pattern for an organization](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/defining-custom-patterns-for-secret-scanning#defining-a-custom-pattern-for-an-organization).
     * For an enterprise, under "Policies" display the "Advanced Security" area, and then click **Security features**. For more information, see [Defining a custom pattern for an enterprise account](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/defining-custom-patterns-for-secret-scanning#defining-a-custom-pattern-for-an-enterprise-account).
  2. To the right of the custom pattern you want to remove, click 
  3. Review the confirmation, and select a method for dealing with any open alerts relating to the custom pattern.
  4. Click **Yes, delete this pattern**.


## [Enabling push protection for a custom pattern](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/managing-custom-patterns#enabling-push-protection-for-a-custom-pattern)
You can enable secret scanning as a push protection for custom patterns stored at the enterprise, organization, or repository level.
### [Enabling push protection for a custom pattern stored in an enterprise](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/managing-custom-patterns#enabling-push-protection-for-a-custom-pattern-stored-in-an-enterprise)
  * To enable push protection for custom patterns, secret scanning as push protection needs to be enabled at the enterprise level. For more information, see [About push protection](https://docs.github.com/en/code-security/secret-scanning/protecting-pushes-with-secret-scanning#enabling-secret-scanning-as-a-push-protection-for-your-enterprise).
  * Enabling push protection for commonly found custom patterns can be disruptive to contributors.


Before enabling push protection for a custom pattern at enterprise level, you must also test your custom patterns using dry runs. You can only perform a dry run on repositories that you have administration access to. If an enterprise owner wants access to perform dry runs on any repository in an organization, they must be assigned the organization owner role. For more information, see [Managing your role in an organization owned by your enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/user-management/managing-organizations-in-your-enterprise/managing-your-role-in-an-organization-owned-by-your-enterprise).
  1. On the left side of the page, in the enterprise account sidebar, click 
  2. Under **Advanced Security**.
  3. Under "Advanced Security", click **Security features**.
  4. Under "Secret scanning", under "Custom patterns", click 
At the enterprise level, you can only edit and enable push protection for custom patterns that you created.
  5. To enable push protection for your custom pattern, scroll down to "Push Protection", and click **Enable**.
The option to enable push protection is visible for published patterns only.
![Screenshot of the custom pattern page with the button to enable push protection highlighted with a dark orange outline.](https://docs.github.com/assets/cb-20409/images/help/repository/secret-scanning-custom-pattern-enable-push-protection.png)


### [Enabling secret scanning as a push protection in an organization for a custom pattern](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/managing-custom-patterns#enabling-secret-scanning-as-a-push-protection-in-an-organization-for-a-custom-pattern)
Before enabling push protection for a custom pattern at organization level, you must ensure that you enable secret scanning for the repositories that you want to scan in your organization. To enable secret scanning on all repositories in your organization, see [Managing security and analysis settings for your organization](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-security-and-analysis-settings-for-your-organization).
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the "Security" section of the sidebar, select the **Advanced Security** dropdown menu, then click **Global settings**.
  4. Under "Custom patterns", click 
  5. To enable push protection for your custom pattern, scroll down to "Push Protection", and click **Enable**.
     * The option to enable push protection is visible for published patterns only.
     * Push protection for custom patterns will only apply to repositories in your organization that have secret scanning as push protection enabled. For more information, see [About push protection](https://docs.github.com/en/code-security/secret-scanning/protecting-pushes-with-secret-scanning#enabling-secret-scanning-as-a-push-protection-for-an-organization).
     * Enabling push protection for commonly found custom patterns can be disruptive to contributors.
![Screenshot of the "Push protection" section of the custom pattern page. A button, labeled "Enable", is outlined in dark orange.](https://docs.github.com/assets/cb-20409/images/help/repository/secret-scanning-custom-pattern-enable-push-protection.png)


### [Enabling secret scanning as a push protection in a repository for a custom pattern](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/managing-custom-patterns#enabling-secret-scanning-as-a-push-protection-in-a-repository-for-a-custom-pattern)
Before enabling push protection for a custom pattern at repository level, you must define the custom pattern for the repository, and test it in the repository. For more information, see [Defining custom patterns for secret scanning](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/defining-custom-patterns-for-secret-scanning#defining-a-custom-pattern-for-a-repository).
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Security" section of the sidebar, click 
  4. Under "Secret Protection", under "Custom patterns", click 
  5. To enable push protection for your custom pattern, scroll down to "Push Protection", and click **Enable**.
The option to enable push protection is visible for published patterns only.
![Screenshot of the "Push protection" section of the custom pattern page. A button, labeled "Enable", is outlined in dark orange.](https://docs.github.com/assets/cb-20409/images/help/repository/secret-scanning-custom-pattern-enable-push-protection.png)


