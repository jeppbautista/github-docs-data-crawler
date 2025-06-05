  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Security advisories](https://docs.github.com/en/code-security/security-advisories "Security advisories")/
  * [Repository security advisories](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories "Repository security advisories")/
  * [Remove collaborators](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/removing-a-collaborator-from-a-repository-security-advisory "Remove collaborators")


# Removing a collaborator from a repository security advisory
When you remove a collaborator from a repository security advisory, they lose read and write access to the security advisory's discussion and metadata.
## Who can use this feature?
Repository owners, organization owners, security managers, and users with the **admin** role
## In this article
  * [Removing a collaborator from a security advisory](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/removing-a-collaborator-from-a-repository-security-advisory#removing-a-collaborator-from-a-security-advisory)
  * [Further reading](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/removing-a-collaborator-from-a-repository-security-advisory#further-reading)


This article applies to editing repository-level advisories as an owner of a public repository.
Users who are not repository owners can contribute to global security advisories in the GitHub Advisory Database at [github.com/advisories](https://github.com/advisories). Edits to global advisories will not change or affect how the advisory appears on the repository. For more information, see [Editing security advisories in the GitHub Advisory Database](https://docs.github.com/en/code-security/security-advisories/working-with-global-security-advisories-from-the-github-advisory-database/editing-security-advisories-in-the-github-advisory-database).
## [Removing a collaborator from a security advisory](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/removing-a-collaborator-from-a-repository-security-advisory#removing-a-collaborator-from-a-security-advisory)
If you remove a user from a repository or organization, and the user is also a collaborator on a security advisory, GitHub will automatically remove the user as a collaborator for the security advisory. This prevents any unauthorized access from ex-collaborators.
  1. On GitHub, navigate to the main page of the repository.
  2. Under the repository name, click **Security**. 
![Screenshot of a repository header showing the tabs. The "Security" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-17801/images/help/repository/security-tab.png)
  3. In the left sidebar, under "Reporting", click 
  4. In the "Security Advisories" list, click the name of the security advisory you'd like to remove a collaborator from.
  5. On the right side of the page, under "Collaborators", find the name of the user or team you'd like to remove from the security advisory.
  6. Next to the collaborator you want to remove, click **Remove**.
![Screenshot of the "Collaborators" area in the right sidebar of a draft security advisory. The "Remove username" button is outlined in dark orange.](https://docs.github.com/assets/cb-28882/images/help/security/security-advisory-remove-collaborator.png)


## [Further reading](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/removing-a-collaborator-from-a-repository-security-advisory#further-reading)
  * [Permission levels for repository security advisories](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/permission-levels-for-repository-security-advisories)
  * [Adding a collaborator to a repository security advisory](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/adding-a-collaborator-to-a-repository-security-advisory)


