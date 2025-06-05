  * [Codespaces](https://docs.github.com/en/codespaces "Codespaces")/
  * [Troubleshooting](https://docs.github.com/en/codespaces/troubleshooting "Troubleshooting")/
  * [Personalization](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-personalization-for-codespaces "Personalization")


# Troubleshooting personalization options for GitHub Codespaces
Troubleshooting steps for common issues with dotfiles and Settings Sync.
## In this article
  * [Troubleshooting dotfiles](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-personalization-for-codespaces#troubleshooting-dotfiles)
  * [Troubleshooting Settings Sync](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-personalization-for-codespaces#troubleshooting-settings-sync)


You can personalize GitHub Codespaces by using a `dotfiles` repository on GitHub or by using Settings Sync. For more information, see [Personalizing GitHub Codespaces for your account](https://docs.github.com/en/codespaces/setting-your-user-preferences/personalizing-github-codespaces-for-your-account).
## [Troubleshooting dotfiles](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-personalization-for-codespaces#troubleshooting-dotfiles)
If your codespace fails to pick up configuration settings from dotfiles, you should work through the following debugging steps.
  1. Enable dotfiles by selecting **Automatically install dotfiles** in [your personal GitHub Codespaces settings](https://github.com/settings/codespaces).
![Screenshot of the "Dotfiles" section of the codespace settings, with the "Automatically install dotfiles" option cleared.](https://docs.github.com/assets/cb-21429/images/help/codespaces/install-custom-dotfiles.png)
  2. Check `/workspaces/.codespaces/.persistedshare/dotfiles` to see if your dotfiles were cloned.
     * If your dotfiles were cloned, try manually re-running your install script to verify that it is executable.
     * If your dotfiles were not cloned, check `/workspaces/.codespaces/.persistedshare/EnvironmentLog.txt` to see if there was a problem cloning them.
  3. Check `/workspaces/.codespaces/.persistedshare/creation.log` for possible issues. For more information, see [Creation logs](https://docs.github.com/en/codespaces/troubleshooting/github-codespaces-logs#creation-logs).


If the configuration from your dotfiles is correctly picked up, but part of the configuration is incompatible with codespaces, use the `$CODESPACES` environment variable to add conditional logic for codespace-specific configuration settings. For more information about configuration that may be incompatible with codespaces, see:
  * [Troubleshooting authentication to a repository](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-authentication-to-a-repository#problems-with-the-repository-from-which-you-created-the-codespace)
  * [Troubleshooting GPG verification for GitHub Codespaces](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-gpg-verification-for-github-codespaces#errors-caused-by-conflicting-configuration)


## [Troubleshooting Settings Sync](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-personalization-for-codespaces#troubleshooting-settings-sync)
You can turn off Settings Sync to stop syncing settings to and from an instance of VS Code.
When you turn off Settings Sync in a codespace, new codespaces continue to use the settings cached from the last time your settings were pushed to the cloud. If you use the VS Code web client for codespaces, and want codespaces to use the default settings instead of your cached settings, you can disable Settings Sync. For more information, see [Managing your preferences for Settings Sync](https://docs.github.com/en/codespaces/setting-your-user-preferences/personalizing-github-codespaces-for-your-account#managing-your-preferences-for-settings-sync).
If you want to return to using the default VS Code settings in all instances of VS Code, including the desktop application, you can clear the cache in the cloud when you turn off Settings Sync.
  1. If Settings Sync is currently turned off in your instance of VS Code, and you want to clear your cached settings, you must first turn it on. For instructions, see [Personalizing GitHub Codespaces for your account](https://docs.github.com/en/codespaces/setting-your-user-preferences/personalizing-github-codespaces-for-your-account#turning-on-settings-sync-in-a-codespace).
  2. At the bottom of the Activity Bar, select **Settings Sync is On**.
  3. In the dropdown, click **Settings Sync: Turn Off**.
![Screenshot of the dropdown menu with the "Settings Sync: Turn Off" option highlighted with a dark orange outline.](https://docs.github.com/assets/cb-24345/images/help/codespaces/settings-sync-turn-off.png)
  4. To clear your cached settings, in the dialog, select **Turn off sync on all your devices and clear the data from the cloud**.
![Screenshot of the "Do you want to turn off sync?" dialog, with the option to clear data from the cloud selected.](https://docs.github.com/assets/cb-99137/images/help/codespaces/turn-off-sync-dialog.png)
  5. Click **Turn off**.


