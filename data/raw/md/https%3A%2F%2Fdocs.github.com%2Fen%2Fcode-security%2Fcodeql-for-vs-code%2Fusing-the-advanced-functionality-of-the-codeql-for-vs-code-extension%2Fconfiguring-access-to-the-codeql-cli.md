  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL for VS Code](https://docs.github.com/en/code-security/codeql-for-vs-code "CodeQL for VS Code")/
  * [Advanced functionality](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension "Advanced functionality")/
  * [CodeQL CLI access](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/configuring-access-to-the-codeql-cli "CodeQL CLI access")


# Configuring access to the CodeQL CLI
The CodeQL for Visual Studio Code extension uses the CodeQL CLI to compile and run queries.
## In this article
  * [Configuring access to the CodeQL CLI](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/configuring-access-to-the-codeql-cli#configuring-access-to-the-codeql-cli)
  * [Troubleshooting](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/configuring-access-to-the-codeql-cli#troubleshooting)


## [Configuring access to the CodeQL CLI](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/configuring-access-to-the-codeql-cli#configuring-access-to-the-codeql-cli)
If you already have the CodeQL CLI installed and added to your `PATH`, the extension will use that version. This might be the case if you create your own CodeQL databases instead of downloading them from GitHub. For more information, see [Preparing your code for CodeQL analysis](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/preparing-your-code-for-codeql-analysis).
Otherwise, the extension automatically manages access to the executable of the CodeQL CLI for you. This ensures that the CodeQL CLI is compatible with the CodeQL extension. You can also check for updates with the **CodeQL: Check for CLI Updates** command from the VS Code Command Palette.
  * The extension-managed CodeQL CLI is not accessible from the terminal. If you intend to use the CLI outside of the extension (for example to create databases), we recommend that you install your own copy of the CodeQL CLI."
  * To override the default behavior and use a specific version of the CodeQL CLI, you can specify the CodeQL CLI **Executable Path** in the extension settings. For more information, see [Customizing settings](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/customizing-settings).


## [Troubleshooting](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/configuring-access-to-the-codeql-cli#troubleshooting)
If you have any difficulty setting up access to the CodeQL CLI, check the CodeQL Extension log for error messages or to see the location of the CodeQL CLI being used. For more information, see [Accessing logs](https://docs.github.com/en/code-security/codeql-for-vs-code/troubleshooting-codeql-for-vs-code/accessing-logs). In particular, in the Extension log you can see the location of the CodeQL CLI that is being used. This is useful if you want to see whether this is an extension-managed CLI or an external one.
If you use the extension-managed CodeQL CLI, the extension checks for updates automatically (or with the **CodeQL: Check for CLI Updates** command) and prompts you to accept the updated version. If you use an external CLI, you need to update it manually (when updates are necessary).
