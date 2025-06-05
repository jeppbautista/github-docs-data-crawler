  * [Codespaces](https://docs.github.com/en/codespaces "Codespaces")/
  * [Prebuilding your codespaces](https://docs.github.com/en/codespaces/prebuilding-your-codespaces "Prebuilding your codespaces")/
  * [Allow external repo access](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/allowing-a-prebuild-to-access-other-repositories "Allow external repo access")


# Allowing a prebuild to access other repositories
You can permit your prebuild to access other GitHub repositories so that it can be built successfully.
## Who can use this feature?
People with admin access to a repository can configure prebuilds for the repository.
Repository-level settings for GitHub Codespaces are available for all repositories owned by personal accounts.   
  

For repositories owned by organizations, repository-level settings for GitHub Codespaces are available for organizations on GitHub Team and GitHub Enterprise plans. To access the settings, the organization or its parent enterprise must have added a payment method and set a spending limit for GitHub Codespaces. For more information, see [Choosing who owns and pays for codespaces in your organization](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/choosing-who-owns-and-pays-for-codespaces-in-your-organization) and [GitHub’s plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans).
## In this article
  * [Allowing a prebuild read access to external resources](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/allowing-a-prebuild-to-access-other-repositories#allowing-a-prebuild-read-access-to-external-resources)
  * [Allowing a prebuild write access to external resources](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/allowing-a-prebuild-to-access-other-repositories#allowing-a-prebuild-write-access-to-external-resources)
  * [Further reading](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/allowing-a-prebuild-to-access-other-repositories#further-reading)


By default, the GitHub Actions workflow for a prebuild configuration can only access its own repository contents. Your project may use additional resources, located elsewhere, to build the development environment.
## [Allowing a prebuild read access to external resources](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/allowing-a-prebuild-to-access-other-repositories#allowing-a-prebuild-read-access-to-external-resources)
You can configure read access to other GitHub repositories, with the same repository owner, by specifying permissions in the `devcontainer.json` file used by your prebuild configuration. For more information, see [Managing access to other repositories within your codespace](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-repository-access-for-your-codespaces).
  * You can only authorize read permissions in this way, and the owner of the target repository must be the same as the owner of the repository for which you're creating a prebuild. For example, if you're creating a prebuild configuration for the `octo-org/octocatrepository`, then you'll be able to grant read permissions for other repositories, such as `octo-org/octodemo`, if this is specified in the `devcontainer.json` file, and provided you have the permissions yourself.
  * You can't use wildcards to specify repositories. You must define permissions for each repository for which you want to grant access.


When you create or edit a prebuild configuration for a `devcontainer.json` file that sets up read access to other repositories with the same repository owner, you'll be prompted to grant these permissions when you click **Create** or **Update**. For more information, see [Configuring prebuilds](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/configuring-prebuilds#configuring-prebuilds).
## [Allowing a prebuild write access to external resources](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/allowing-a-prebuild-to-access-other-repositories#allowing-a-prebuild-write-access-to-external-resources)
If your project requires write access to resources, or if the external resources reside in a repository with a different owner than the repository for which you are creating a prebuild configuration, you can use a personal access token to grant this access.
You will need to create a new personal account and then use this account to create a personal access token (classic) with the appropriate scopes.
  1. Create a new personal account on GitHub.
Although you can generate the personal access token (classic) using your existing personal account, we strongly recommend creating a new account with access only to the target repositories required for your scenario. This is because the access token's `repository` permission grants access to all of the repositories that the account has access to. For more information, see [Creating an account on GitHub](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github) and [Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions#considering-cross-repository-access).
  2. Give the new account read access to the required repositories. For more information, see [Managing an individual's access to an organization repository](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/managing-an-individuals-access-to-an-organization-repository).
  3. While signed into the new account, create a personal access token (classic) with the `repo` scope. Optionally, if the prebuild will need to download packages from the GitHub Container registry, also select the `read:packages` scope. For more information, see [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).
![Screenshot of the "Select scopes" configuration options for a personal access token \(classic\), with the "repo" and "read:packages" scopes selected.](https://docs.github.com/assets/cb-82382/images/help/codespaces/prebuilds-select-scopes.png)
If the prebuild will use a package from the GitHub Container registry, you will need to either grant the new account access to the package or configure the package to inherit the access permissions of the repository you are prebuilding. For more information, see [Configuring a package's access control and visibility](https://docs.github.com/en/packages/learn-github-packages/configuring-a-packages-access-control-and-visibility).
  4. Copy the token string. You will assign this to a Codespaces repository secret.
  5. Sign back into the account that has admin access to the repository.
  6. In the repository for which you want to create GitHub Codespaces prebuilds, create a new Codespaces repository secret called `CODESPACES_PREBUILD_TOKEN`, giving it the value of the token you created and copied. For more information, see [Managing development environment secrets for your repository or organization](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/managing-development-environment-secrets-for-your-repository-or-organization#adding-secrets-for-a-repository).


The personal access token will be used for all subsequent prebuilds created for your repository. Unlike other Codespaces repository secrets, the `CODESPACES_PREBUILD_TOKEN` secret is only used for prebuilding and will not be available for use in codespaces created from your repository.
## [Further reading](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/allowing-a-prebuild-to-access-other-repositories#further-reading)
  * [Configuring prebuilds](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/configuring-prebuilds)
  * [Troubleshooting prebuilds](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-prebuilds)


