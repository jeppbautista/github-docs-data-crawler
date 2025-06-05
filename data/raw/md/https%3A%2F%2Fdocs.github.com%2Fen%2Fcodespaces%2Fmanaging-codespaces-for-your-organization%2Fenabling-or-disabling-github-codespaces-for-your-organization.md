  * [Codespaces](https://docs.github.com/en/codespaces "Codespaces")/
  * [Managing your organization](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization "Managing your organization")/
  * [Enable or disable Codespaces](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/enabling-or-disabling-github-codespaces-for-your-organization "Enable or disable Codespaces")


# Enabling or disabling GitHub Codespaces for your organization
You can control which users can use GitHub Codespaces in your organization's private repositories.
## Who can use this feature?
Organization owners can control which users can use GitHub Codespaces.
Organizations on GitHub Team and GitHub Enterprise plans can choose to disable GitHub Codespaces in private repositories. For more information, see [GitHub’s plans](https://docs.github.com/en/get-started/learning-about-github/githubs-products).
## In this article
  * [About enabling and disabling GitHub Codespaces](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/enabling-or-disabling-github-codespaces-for-your-organization#about-enabling-and-disabling-github-codespaces)
  * [Prerequisites for enabling GitHub Codespaces](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/enabling-or-disabling-github-codespaces-for-your-organization#prerequisites-for-enabling-github-codespaces)
  * [About changing your settings](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/enabling-or-disabling-github-codespaces-for-your-organization#about-changing-your-settings)
  * [Enabling or disabling GitHub Codespaces](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/enabling-or-disabling-github-codespaces-for-your-organization#enabling-or-disabling-github-codespaces)


## [About enabling and disabling GitHub Codespaces](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/enabling-or-disabling-github-codespaces-for-your-organization#about-enabling-and-disabling-github-codespaces)
GitHub Codespaces is always available in an organization's public repositories, and any user can create a codespace from these repositories. If your organization is on a GitHub Free plan, GitHub Codespaces is always available in your organization's private repositories too, and any users with access to these repositories can create a codespace at their own expense.
If you're the owner of an organization on a GitHub Team or GitHub Enterprise Cloud plan, you can choose whether to enable or disable GitHub Codespaces in your organization's private repositories. If you enable GitHub Codespaces in these repositories, you can choose whether to enable for all users or for a selection of members and collaborators.
By enabling GitHub Codespaces, you can help your members and collaborators get started with projects quickly, without needing to install lots of tools and dependencies locally to start contributing. However, you might want to roll out GitHub Codespaces gradually across your organization by enabling it for groups of users at a time. Alternatively, if you need to comply with security regulations that require increased control over the private code in your organization, you might want to disable GitHub Codespaces for all your members.
If you have enabled GitHub Codespaces in private repositories for at least some users, you can choose to pay for these users' usage of GitHub Codespaces across all repositories in your organization. For more information, see [Choosing who owns and pays for codespaces in your organization](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/choosing-who-owns-and-pays-for-codespaces-in-your-organization).
If you cannot access the settings to enable GitHub Codespaces in your organization, this may be because an enterprise owner has disabled GitHub Codespaces for your organization. For more information, see [Enforcing policies for GitHub Codespaces in your enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-codespaces-in-your-enterprise) in the GitHub Enterprise Cloud documentation.
## [Prerequisites for enabling GitHub Codespaces](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/enabling-or-disabling-github-codespaces-for-your-organization#prerequisites-for-enabling-github-codespaces)
Only people who can either push changes to a repository, or fork the repository, can create a codespace for that repository. To allow a user to create codespaces for a repository owned by your organization, you must do one of the following things.
  * Ensure that the user has read access to the repository, and the repository permits forking, so that the user can create a codespace from the repository, push their changes to a fork, and create a pull request for any changes they want to make. For more information, see [Managing the forking policy for your organization](https://docs.github.com/en/organizations/managing-organization-settings/managing-the-forking-policy-for-your-organization).
  * Ensure that the user has write access to the repository, so that they can push changes directly to the repository without forking.


In addition, to allow users to create codespaces, you must ensure that your organization does not have an IP address allow list enabled. For more information, see [Managing allowed IP addresses for your organization](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-allowed-ip-addresses-for-your-organization) in the GitHub Enterprise Cloud documentation.
If you are a verified educator or a teacher, you must enable GitHub Codespaces from a GitHub Classroom to use your Codespaces Education benefit. For more information, see [Using GitHub Codespaces with GitHub Classroom](https://docs.github.com/en/education/manage-coursework-with-github-classroom/integrate-github-classroom-with-an-ide/using-github-codespaces-with-github-classroom#about-the-codespaces-education-benefit-for-verified-teachers).
## [About changing your settings](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/enabling-or-disabling-github-codespaces-for-your-organization#about-changing-your-settings)
If you remove a user's access to GitHub Codespaces, the user will immediately be unable to open existing codespaces they have created from your organization's private repositories. If you were previously paying for codespaces the user had created from your organization's public repositories, ownership of these codespaces will transfer the user.
Before removing users' access, you should alert the affected users. If they have unpublished work in a codespace, they can make sure the work is pushed to a branch in the repository before they lose access.
Once a user loses access to a codespace, the codespace is retained for a period of 7 days, then it is permanently deleted. During this 7-day period, to recover unpublished work from the codespace, the user must contact us through the [GitHub Support portal](https://support.github.com).
## [Enabling or disabling GitHub Codespaces](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/enabling-or-disabling-github-codespaces-for-your-organization#enabling-or-disabling-github-codespaces)
If you remove a user's access to GitHub Codespaces, the user will immediately be unable to open existing codespaces they have created from your organization's private repositories. For more information, see [About changing your settings](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/enabling-or-disabling-github-codespaces-for-your-organization#about-changing-your-settings).
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the left sidebar, click 
  4. Under **General**.
  5. On the Codespaces settings page, under "Codespaces access," select your preferred setting for GitHub Codespaces in your organization's private repositories.
You can disable Codespaces, enable for specific members or teams, enable for all members, or enable for all members and collaborators.


