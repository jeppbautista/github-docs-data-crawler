  * [Organizations](https://docs.github.com/en/organizations "Organizations")/
  * [Manage organization settings](https://docs.github.com/en/organizations/managing-organization-settings "Manage organization settings")/
  * [Manage the commit signoff policy](https://docs.github.com/en/organizations/managing-organization-settings/managing-the-commit-signoff-policy-for-your-organization "Manage the commit signoff policy")


# Managing the commit signoff policy for your organization
You can require users to automatically sign off all commits they make in GitHub's web interface to repositories owned by your organization.
## Who can use this feature?
Organization owners can require all commits to repositories owned by the organization be signed off by the commit author.
## In this article
  * [About commit signoffs](https://docs.github.com/en/organizations/managing-organization-settings/managing-the-commit-signoff-policy-for-your-organization#about-commit-signoffs)
  * [Managing compulsory commit signoffs for your organization](https://docs.github.com/en/organizations/managing-organization-settings/managing-the-commit-signoff-policy-for-your-organization#managing-compulsory-commit-signoffs-for-your-organization)


## [About commit signoffs](https://docs.github.com/en/organizations/managing-organization-settings/managing-the-commit-signoff-policy-for-your-organization#about-commit-signoffs)
To affirm that a commit complies with the rules and licensing governing a repository, many organizations require developers to sign off on every commit. If your organization requires commit signoffs, you can make signing off a seamless part of the commit process by enabling compulsory commit signoffs for users committing through GitHub's web interface. After you enable compulsory commit signoffs for an organization, every commit made to repositories in that organization through the web interface will automatically be signed off on by the commit author.
People with admin access to a repository can also enable compulsory commit signoffs at the repository level. For more information, see [Managing the commit signoff policy for your repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-the-commit-signoff-policy-for-your-repository).
Compulsory commit signoffs only apply to commits made via the web interface. For commits made via the Git command line interface, the commit author must sign off on the commit using the `--signoff` option. For more information, see the [Git documentation](https://git-scm.com/docs/git-commit).
You can determine whether a repository you are contributing to has compulsory commit signoffs enabled by checking the header of the commit form at the bottom of the file you are editing. After compulsory commit signoff has been enabled, the header will read "Sign off and commit changes."
![Screenshot of the commit form in a repository. The title of the form is "Sign off and commit changes."](https://docs.github.com/assets/cb-14661/images/help/commits/commit-form-with-signoff-enabled.png)
Before signing off on a commit, you should ensure that your commit is in compliance with the rules and licensing governing the repository you're committing to. The repository may use a sign off agreement, such as the Developer Certificate of Origin from the Linux Foundation. For more information, see the [Developer Certificate of Origin](https://developercertificate.org/).
Signing off on a commit differs from signing a commit. For more information about signing a commit, see [About commit signature verification](https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification).
## [Managing compulsory commit signoffs for your organization](https://docs.github.com/en/organizations/managing-organization-settings/managing-the-commit-signoff-policy-for-your-organization#managing-compulsory-commit-signoffs-for-your-organization)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the "Code, planning, and automation" section of the sidebar, select **Repository defaults**.
  4. Select or deselect **Require contributors to sign off on web-based commits**.


