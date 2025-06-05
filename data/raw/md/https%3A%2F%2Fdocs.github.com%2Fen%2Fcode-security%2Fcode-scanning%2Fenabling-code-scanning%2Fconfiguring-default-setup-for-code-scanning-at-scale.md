  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Enable code scanning](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning "Enable code scanning")/
  * [Code scanning at scale](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning-at-scale "Code scanning at scale")


# Configuring default setup for code scanning at scale
You can quickly configure code scanning for repositories across your organization using default setup.
## Who can use this feature?
Organization owners, security managers, and organization members with the **admin** role
Code scanning is available for the following repository types:
  * Public repositories on GitHub.com
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [About configuring default setup at scale](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning-at-scale#about-configuring-default-setup-at-scale)
  * [Configuring default setup for all eligible repositories in an organization](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning-at-scale#configuring-default-setup-for-all-eligible-repositories-in-an-organization)
  * [Configuring default setup for a subset of repositories in an organization](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning-at-scale#configuring-default-setup-for-a-subset-of-repositories-in-an-organization)


## [About configuring default setup at scale](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning-at-scale#about-configuring-default-setup-at-scale)
With default setup for code scanning, you can quickly secure code in repositories across your organization.
You can enable code scanning for all repositories in your organization that are eligible for default setup. After enabling default setup, the code written in CodeQL-supported languages in repositories in the organization will be scanned:
  * On each push to the repository's default branch, or any protected branch. For more information on protected branches, see [About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
  * When creating or committing to a pull request based against the repository's default branch, or any protected branch, excluding pull requests from forks.
  * On a weekly schedule.


For more information, see [Configuring default setup for all eligible repositories in an organization](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning-at-scale#configuring-default-setup-for-all-eligible-repositories-in-an-organization).
For repositories that are not eligible for default setup, you can configure advanced setup at the repository level, or at the organization level using a script. For more information, see [Configuring advanced setup for code scanning with CodeQL at scale](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning-with-codeql-at-scale).
### [Eligible repositories for CodeQL default setup at scale](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning-at-scale#eligible-repositories-for-codeql-default-setup-at-scale)
A repository must meet all the following criteria to be eligible for default setup, otherwise you need to use advanced setup.
  * Advanced setup for code scanning is not already enabled.
  * Uses Go, JavaScript/TypeScript, Python, or Ruby.
  * GitHub Actions are enabled.
  * It is publicly visible, or GitHub Code Security is enabled.


We recommend enabling default setup for eligible repositories if there is any chance the repositories will include at least one CodeQL-supported language in the future. If you enable default setup on a repository that does not include any CodeQL-supported languages, default setup will not run any scans or use any GitHub Actions minutes. If CodeQL-supported languages are added to the repository's default branch, default setup will automatically begin scanning CodeQL-supported languages and using GitHub Actions minutes. For more information on CodeQL-supported languages, see [About code scanning with CodeQL](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql#about-codeql).
### [About adding languages to an existing default setup configuration](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning-at-scale#about-adding-languages-to-an-existing-default-setup-configuration)
If the code in a repository changes to include a CodeQL-supported language, GitHub will automatically update the code scanning configuration to include the new language. If code scanning fails with the new configuration, GitHub will resume the previous configuration automatically so the repository does not lose code scanning coverage.
### [Providing default setup access to private registries](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning-at-scale#providing-default-setup-access-to-private-registries)
When a repository uses code stored in a private registry, default setup needs access to the registry to work effectively. For more information, see [Giving security features access to private registries](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/giving-org-access-private-registries).
## [Configuring default setup for all eligible repositories in an organization](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning-at-scale#configuring-default-setup-for-all-eligible-repositories-in-an-organization)
You can enable default setup for all eligible repositories in your organization. For more information, see [About enabling security features at scale](https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/about-enabling-security-features-at-scale).
### [Extending CodeQL coverage in default setup](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning-at-scale#extending-codeql-coverage-in-default-setup)
Through your organization's security settings page, you can extend coverage in default setup using model packs for all eligible repositories in your organization. For more information, see [Editing your configuration of default setup](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/editing-your-configuration-of-default-setup#extending-coverage-for-all-repositories-in-an-organization).
## [Configuring default setup for a subset of repositories in an organization](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning-at-scale#configuring-default-setup-for-a-subset-of-repositories-in-an-organization)
You can filter for specific repositories you would like to configure default setup for. For more information, see [Applying a custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/applying-a-custom-security-configuration).
