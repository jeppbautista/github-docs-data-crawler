  * [Organizations](https://docs.github.com/en/organizations "Organizations")/
  * [Manage repository access](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories "Manage repository access")/
  * [Manage repository roles](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles "Manage repository roles")/
  * [Repository roles](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization "Repository roles")


# Repository roles for an organization
You can customize access to each repository in your organization by assigning granular roles, giving people access to the features and tasks they need.
## In this article
  * [Repository roles for organizations](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization#repository-roles-for-organizations)
  * [Permissions for each role](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization#permissions-for-each-role)
  * [Further reading](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization#further-reading)


## [Repository roles for organizations](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization#repository-roles-for-organizations)
You can give organization members, outside collaborators, and teams of people different levels of access to repositories owned by an organization by assigning them to roles. Choose the role that best fits each person or team's function in your project without giving people more access to the project than they need.
From least access to most access, the roles for an organization repository are:
  * **Read:** Recommended for non-code contributors who want to view or discuss your project
  * **Triage:** Recommended for contributors who need to proactively manage issues, discussions, and pull requests without write access
  * **Write:** Recommended for contributors who actively push to your project
  * **Maintain:** Recommended for project managers who need to manage the repository without access to sensitive or destructive actions
  * **Admin:** Recommended for people who need full access to the project, including sensitive and destructive actions like managing security or deleting a repository


If your organization uses GitHub Enterprise Cloud, you can create custom repository roles. For more information, see [Managing custom repository roles for an organization](https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/managing-custom-repository-roles-for-an-organization) in the GitHub Enterprise Cloud documentation.
Organization owners can set base permissions that apply to all members of an organization when accessing any of the organization's repositories. For more information, see [Setting base permissions for an organization](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/setting-base-permissions-for-an-organization#setting-base-permissions).
Organization owners can also choose to further limit access to certain settings and actions across the organization. For more information on options for specific settings, see [Managing organization settings](https://docs.github.com/en/organizations/managing-organization-settings).
In addition to managing organization-level settings, organization owners have admin access to every repository owned by the organization. For more information, see [Roles in an organization](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization).
When someone adds a deploy key to a repository, any user who has the private key can read from or write to the repository (depending on the key settings), even if they're later removed from the organization.
## [Permissions for each role](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization#permissions-for-each-role)
Some of the features listed below are limited to organizations using GitHub Enterprise Cloud. For more information about how you can try GitHub Enterprise Cloud for free, see [Setting up a trial of GitHub Enterprise Cloud](https://docs.github.com/en/enterprise-cloud@latest/admin/overview/setting-up-a-trial-of-github-enterprise-cloud).
The roles required to use security features are listed in [Access requirements for security features](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization#access-requirements-for-security-features) below.
Repository action | Read | Triage | Write | Maintain | Admin  
---|---|---|---|---|---  
Manage [individual](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/managing-an-individuals-access-to-an-organization-repository), [team](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/managing-team-access-to-an-organization-repository), and [outside collaborator](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-outside-collaborators/adding-outside-collaborators-to-repositories-in-your-organization) access to the repository |  |  |  |  |   
Pull from the person or team's assigned repositories |  |  |  |  |   
Fork the person or team's assigned repositories |  |  |  |  |   
Edit and delete their own comments |  |  |  |  |   
Open issues |  |  |  |  |   
Close issues they opened themselves |  |  |  |  |   
Reopen issues they closed themselves |  |  |  |  |   
Have an issue assigned to them |  |  |  |  |   
Send pull requests from forks of the team's assigned repositories |  |  |  |  |   
[Submit reviews on pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/reviewing-proposed-changes-in-a-pull-request) |  |  |  |  |   
[Approve or request changes to a pull request with required reviews](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/approving-a-pull-request-with-required-reviews) |  |  |  |  |   
[Apply suggested changes](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/incorporating-feedback-in-your-pull-request) to pull requests |  |  |  |  |   
View published releases |  |  |  |  |   
View [GitHub Actions workflow runs](https://docs.github.com/en/actions/managing-workflow-runs) |  |  |  |  |   
Edit wikis in public repositories |  |  |  |  |   
Edit wikis in private repositories |  |  |  |  |   
[Report abusive or spammy content](https://docs.github.com/en/communities/maintaining-your-safety-on-github/reporting-abuse-or-spam) |  |  |  |  |   
Apply/dismiss labels |  |  |  |  |   
Create, edit, delete labels |  |  |  |  |   
Close, reopen, and assign all issues and pull requests |  |  |  |  |   
[Enable and disable auto-merge on a pull request](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-auto-merge-for-pull-requests-in-your-repository) |  |  |  |  |   
Create, edit, delete milestones |  |  |  |  |   
Apply milestones |  |  |  |  |   
Mark [duplicate issues and pull requests](https://docs.github.com/en/issues/tracking-your-work-with-issues/marking-issues-or-pull-requests-as-a-duplicate) |  |  |  |  |   
Request [pull request reviews](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/requesting-a-pull-request-review) |  |  |  |  |   
Merge a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges) |  |  |  |  |   
Push to (write) the person or team's assigned repositories |  |  |  |  |   
Edit and delete anyone's comments on commits, pull requests, and issues |  |  |  |  |   
[Hide anyone's comments](https://docs.github.com/en/communities/moderating-comments-and-conversations/managing-disruptive-comments) |  |  |  |  |   
Transfer issues (see [Transferring an issue to another repository](https://docs.github.com/en/issues/tracking-your-work-with-issues/transferring-an-issue-to-another-repository) for details) |  |  |  |  |   
[Act as a designated code owner for a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) |  |  |  |  |   
[Mark a draft pull request as ready for review](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/changing-the-stage-of-a-pull-request) |  |  |  |  |   
[Convert a pull request to a draft](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/changing-the-stage-of-a-pull-request) |  |  |  |  |   
Create [status checks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks) |  |  |  |  |   
Create, edit, run, re-run, and cancel [GitHub Actions workflows](https://docs.github.com/en/actions) |  |  |  |  |   
Create, update, and delete [GitHub Actions secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions) on GitHub.com |  |  |  |  |   
Create, update, and delete [GitHub Actions secrets](https://docs.github.com/en/rest/actions/secrets) using the REST API |  |  |  |  |   
Create and edit releases |  |  |  |  |   
View draft releases |  |  |  |  |   
Edit a repository's description |  |  |  |  |   
[View and install packages](https://docs.github.com/en/packages/learn-github-packages) |  |  |  |  |   
[Publish packages](https://docs.github.com/en/packages/learn-github-packages/publishing-a-package) |  |  |  |  |   
[Delete and restore packages](https://docs.github.com/en/packages/learn-github-packages/deleting-and-restoring-a-package) |  |  |  |  |   
Manage [topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics) |  |  |  |  |   
Enable wikis and restrict wiki editors |  |  |  |  |   
Configure [pull request merges](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges) |  |  |  |  |   
Configure [a publishing source for GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) |  |  |  |  |   
View [content exclusion settings](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-github-copilot-features-in-your-organization/about-content-exclusions-for-github-copilot) for GitHub Copilot |  |  |  |  |   
Manage [branch protection rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule) and [repository rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets) |  |  |  |  |   
View [rulesets for a repository](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets) |  |  |  |  |   
[Push to protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)  
Doesn't apply to rulesets as these have a different bypass model. See [Granting bypass permissions for your branch or tag ruleset](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository#granting-bypass-permissions-for-your-branch-or-tag-ruleset). |  |  |  |  |   
Merge pull requests on protected branches, even if there are no approving reviews |  |  |  |  |   
[Create and edit repository social cards](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview) |  |  |  |  |   
Limit [interactions in a repository](https://docs.github.com/en/communities/moderating-comments-and-conversations/limiting-interactions-in-your-repository) |  |  |  |  |   
Delete an issue (see [Deleting an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/deleting-an-issue)) |  |  |  |  |   
[Define code owners for a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) |  |  |  |  |   
Add a repository to a team (see [Managing team access to an organization repository](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-team-access-to-an-organization-repository#giving-a-team-access-to-a-repository) for details) |  |  |  |  |   
[Manage outside collaborator access to a repository](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-outside-collaborators/adding-outside-collaborators-to-repositories-in-your-organization) |  |  |  |  |   
[Change a repository's visibility](https://docs.github.com/en/organizations/managing-organization-settings/restricting-repository-visibility-changes-in-your-organization) |  |  |  |  |   
Make a repository a template (see [Creating a template repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository)) |  |  |  |  |   
Change a repository's settings |  |  |  |  |   
Manage team and collaborator access to the repository |  |  |  |  |   
Edit the repository's default branch |  |  |  |  |   
Rename the repository's default branch (see [Renaming a branch](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/renaming-a-branch)) |  |  |  |  |   
Rename a branch other than the repository's default branch (see [Renaming a branch](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/renaming-a-branch)) |  |  |  |  |   
Manage webhooks and deploy keys |  |  |  |  |   
[Manage the forking policy for a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-the-forking-policy-for-your-repository) |  |  |  |  |   
[Transfer repositories into the organization](https://docs.github.com/en/organizations/managing-organization-settings/restricting-repository-creation-in-your-organization) |  |  |  |  |   
[Delete or transfer repositories out of the organization](https://docs.github.com/en/organizations/managing-organization-settings/setting-permissions-for-deleting-or-transferring-repositories) |  |  |  |  |   
[Archive repositories](https://docs.github.com/en/repositories/archiving-a-github-repository/archiving-repositories) |  |  |  |  |   
Display a sponsor button (see [Displaying a sponsor button in your repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/displaying-a-sponsor-button-in-your-repository)) |  |  |  |  |   
Create autolink references to external resources, like Jira or Zendesk (see [Configuring autolinks to reference external resources](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/configuring-autolinks-to-reference-external-resources)) |  |  |  |  |   
[Enable GitHub Discussions](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/enabling-or-disabling-github-discussions-for-a-repository) in a repository |  |  |  |  |   
[Create and edit categories](https://docs.github.com/en/discussions/managing-discussions-for-your-community/managing-categories-for-discussions) for GitHub Discussions |  |  |  |  |   
[Move a discussion to a different category](https://docs.github.com/en/discussions/managing-discussions-for-your-community/managing-discussions) |  |  |  |  |   
[Manage pinned discussions](https://docs.github.com/en/discussions/managing-discussions-for-your-community/managing-discussions) |  |  |  |  |   
[Convert issues to discussions in bulk](https://docs.github.com/en/discussions/managing-discussions-for-your-community/managing-discussions) |  |  |  |  |   
[Lock and unlock discussions](https://docs.github.com/en/discussions/managing-discussions-for-your-community/moderating-discussions) |  |  |  |  |   
[Individually convert issues to discussions](https://docs.github.com/en/discussions/managing-discussions-for-your-community/moderating-discussions) |  |  |  |  |   
[Create new discussions and comment on existing discussions](https://docs.github.com/en/discussions/collaborating-with-your-community-using-discussions/participating-in-a-discussion) |  |  |  |  |   
[Delete a discussion](https://docs.github.com/en/discussions/managing-discussions-for-your-community/managing-discussions#deleting-a-discussion) |  |  |  |  |   
[Create codespaces](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository?tool=webui) for private repositories |  |  |  |  |   
[Create codespaces](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository?tool=webui) for private repositories with [Codespaces secrets access](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/managing-development-environment-secrets-for-your-repository-or-organization?tool=webui) |  |  |  |  |   
[Create codespaces](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository?tool=webui) for public repositories  
(users with read-only access can only create codespaces at their own expense) |  |  |  |  |   
### [Access requirements for security features](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization#access-requirements-for-security-features)
In this section, you can find the access required for security features, such as GitHub Advanced Security features.
Repository writers and maintainers can only see secret scanning alert information for their own commits.
Repository action | Read | Triage | Write | Maintain | Admin  
---|---|---|---|---|---  
Receive [Dependabot alerts for insecure dependencies](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts) in a repository |  |  |  |  |   
[Dismiss Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/viewing-and-updating-dependabot-alerts) |  |  |  |  |   
Create [security advisories](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/about-repository-security-advisories) |  |  |  |  |   
[Enable the dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exploring-the-dependencies-of-a-repository) for a private repository |  |  |  |  |   
[View code scanning alerts on pull requests](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/triaging-code-scanning-alerts-in-pull-requests) |  |  |  |  |   
[List, dismiss, and delete code scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/resolving-code-scanning-alerts) |  |  |  |  |   
[View and dismiss secret scanning alerts in a repository](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning) |  |  |  |  |   
## [Further reading](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization#further-reading)
  * [Managing user access to your organization's repositories](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories)
  * [Adding outside collaborators to repositories in your organization](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-outside-collaborators/adding-outside-collaborators-to-repositories-in-your-organization)


