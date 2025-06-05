  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Manage Copilot](https://docs.github.com/en/copilot/managing-copilot "Manage Copilot")/
  * [Configure personal settings](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings "Configure personal settings")/
  * [Configure in the CLI](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-the-cli "Configure in the CLI")


# Configuring GitHub Copilot in the CLI
Learn how to configure settings and set up aliases for Copilot in the CLI.
## In this article
  * [Setting up aliases](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-the-cli#setting-up-aliases)
  * [Changing the default execution confirmation](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-the-cli#changing-the-default-execution-confirmation)
  * [Changing usage analytics](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-the-cli#changing-usage-analytics)


## [Setting up aliases](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-the-cli#setting-up-aliases)
You can create aliases for Copilot in the CLI to reduce keystrokes, and to allow Copilot in the CLI to execute commands on your behalf.
To allow Copilot in the CLI to execute commands, you must run the following commands to create the aliases (as opposed to creating an alias like you would for another shell command).
After executing the following commands to create the aliases, you can run `ghcs` and `ghce` instead of `gh copilot suggest` and `gh copilot explain`.
### [Bash](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-the-cli#bash)
Shell```
echo 'eval "$(gh copilot alias -- bash)"' >> ~/.bashrc

```
```
echo 'eval "$(gh copilot alias -- bash)"' >> ~/.bashrc

```

### [PowerShell](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-the-cli#powershell)
Shell```
$GH_COPILOT_PROFILE = Join-Path -Path $(Split-Path -Path $PROFILE -Parent) -ChildPath "gh-copilot.ps1"
gh copilot alias -- pwsh | Out-File ( New-Item -Path $GH_COPILOT_PROFILE -Force )
echo ". `"$GH_COPILOT_PROFILE`"" >> $PROFILE

```
```
$GH_COPILOT_PROFILE = Join-Path -Path $(Split-Path -Path $PROFILE -Parent) -ChildPath "gh-copilot.ps1"
gh copilot alias -- pwsh | Out-File ( New-Item -Path $GH_COPILOT_PROFILE -Force )
echo ". `"$GH_COPILOT_PROFILE`"" >> $PROFILE

```

### [Zsh](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-the-cli#zsh)
Shell```
echo 'eval "$(gh copilot alias -- zsh)"' >> ~/.zshrc

```
```
echo 'eval "$(gh copilot alias -- zsh)"' >> ~/.zshrc

```

## [Changing the default execution confirmation](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-the-cli#changing-the-default-execution-confirmation)
When you use the `ghcs` alias and you select **Execute command** , Copilot in the CLI will ask for confirmation before executing the command. You can change the default confirmation.
  1. Execute the following command:
Shell```
gh copilot config

```
```
gh copilot config

```

  2. Select **Default value for confirming command execution**.
  3. Choose the desired default.


## [Changing usage analytics](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-the-cli#changing-usage-analytics)
Unless you opt out, Copilot in the CLI will send a payload in the format below to the analytics system. This data helps improve the product. GitHub does not look at the data of specific individuals or at specific queries.
```
{
  "platform": "darwin",
  "architecture": "arm64",
  "version": "0.3.0-beta",
  "custom_event": "true",
  "event_parent_command": "explain",
  "event_name": "Explain",
  "sha": "089a53215fc4383179869f7f6132ce9d6e58754a",
  "thread_id": "e61d0d08-f6ba-465b-81cf-c30fd9127d70"
}

```

To opt in or out of data collection:
  1. Execute the following command:
Shell```
gh copilot config

```
```
gh copilot config

```

  2. Select **Optional Usage Analytics**.
  3. Choose the desired default.


