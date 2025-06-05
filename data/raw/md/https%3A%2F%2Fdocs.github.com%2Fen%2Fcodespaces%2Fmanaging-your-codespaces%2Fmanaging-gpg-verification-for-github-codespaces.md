  * [Codespaces](https://docs.github.com/en/codespaces "Codespaces")/
  * [Managing your codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces "Managing your codespaces")/
  * [GPG verification](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-gpg-verification-for-github-codespaces "GPG verification")


# Managing GPG verification for GitHub Codespaces
You can allow GitHub to automatically use GPG to sign commits you make in your codespaces, so other people can be confident that the changes come from a trusted source.
## In this article
  * [About GPG verification in GitHub Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-gpg-verification-for-github-codespaces#about-gpg-verification-in-github-codespaces)
  * [Enabling or disabling GPG verification](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-gpg-verification-for-github-codespaces#enabling-or-disabling-gpg-verification)
  * [Further reading](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-gpg-verification-for-github-codespaces#further-reading)


## [About GPG verification in GitHub Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-gpg-verification-for-github-codespaces#about-gpg-verification-in-github-codespaces)
After you enable GPG verification, GitHub will automatically sign commits you make in GitHub Codespaces, and the commits will have a verified status on GitHub. For more information about GitHub-signed commits, see [About commit signature verification](https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification).
By default, GPG verification is disabled for codespaces you create. If you enable GPG verification, your commits are signed in repositories that you trust.
Your list of trusted repositories for GitHub Codespaces is shared between the GPG verification and Settings Sync features. Assuming you have both features enabled, if you have added a selected list of trusted repositories for GPG verification, Settings Sync is turned on in codespaces created from these repositories. If you trust a new repository for Settings Sync, GPG verification is enabled for the same repository. Although the features share the same list of trusted repositories, you can enable or disable GPG verification and Settings Sync independently.
If you have previously enabled GPG verification for all repositories, we recommend changing your preferences to use a selected list of trusted repositories. For more information, see [Security in GitHub Codespaces](https://docs.github.com/en/codespaces/codespaces-reference/security-in-github-codespaces#using-settings-sync).
For more information about managing your preferences for Settings Sync, see [Personalizing GitHub Codespaces for your account](https://docs.github.com/en/codespaces/setting-your-user-preferences/personalizing-github-codespaces-for-your-account#managing-your-preferences-for-settings-sync).
If you have linked a dotfiles repository with GitHub Codespaces, the Git configuration in your dotfiles may conflict with the configuration that GitHub Codespaces requires to sign commits. For more information, see [Troubleshooting GPG verification for GitHub Codespaces](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-gpg-verification-for-github-codespaces).
## [Enabling or disabling GPG verification](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-gpg-verification-for-github-codespaces#enabling-or-disabling-gpg-verification)
  1. In the upper-right corner of any page on GitHub, click your profile photo, then click 
  2. In the "Code, planning, and automation" section of the sidebar, click 
  3. On the page that's displayed, under "GPG verification," enable or disable GPG verification by selecting or deselecting **Enable**.
  4. To change your trusted repositories for GPG verification and Settings Sync, under "Trusted repositories," either select **All repositories** , or select **Selected repositories** and use the "Select repositories" dropdown to add repositories you trust.
We recommend using a selected list of trusted repositories. For more information, see [Security in GitHub Codespaces](https://docs.github.com/en/codespaces/codespaces-reference/security-in-github-codespaces#using-settings-sync).


Once you enable GPG verification, it will automatically take effect in any new codespaces you create from the relevant repositories. To have GPG verification take effect in an existing active codespace, you will need to stop and restart the codespace. For more information, see [Stopping and starting a codespace](https://docs.github.com/en/codespaces/developing-in-codespaces/stopping-and-starting-a-codespace).
## [Further reading](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-gpg-verification-for-github-codespaces#further-reading)
  * [Setting your user preferences](https://docs.github.com/en/codespaces/setting-your-user-preferences)
  * [Customizing your codespace](https://docs.github.com/en/codespaces/customizing-your-codespace)


