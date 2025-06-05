  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Manage Copilot](https://docs.github.com/en/copilot/managing-copilot "Manage Copilot")/
  * [Configure personal settings](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings "Configure personal settings")/
  * [Configure in your environment](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment "Configure in your environment")


# Configuring GitHub Copilot in your environment
You can enable, configure, or disable GitHub Copilot in a supported IDE.
## Tool navigation
  * [Eclipse](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment?tool=eclipse)
  * [JetBrains IDEs](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment?tool=jetbrains)
  * [Vim/Neovim](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment?tool=vimneovim)
  * [Visual Studio](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment?tool=visualstudio)
  * [Visual Studio Code](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment?tool=vscode)
  * [Xcode](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment?tool=xcode)


## In this article
  * [About GitHub Copilot in JetBrains IDEs](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#about-github-copilot-in-jetbrains-ides)
  * [Prerequisites](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#prerequisites)
  * [Using or rebinding keyboard shortcuts for GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#using-or-rebinding-keyboard-shortcuts-for-github-copilot)
  * [Enabling or disabling GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#enabling-or-disabling-github-copilot)
  * [Configuring advanced settings for GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#configuring-advanced-settings-for-github-copilot)
  * [Configuring language settings for GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#configuring-language-settings-for-github-copilot)
  * [Configuring Copilot settings on GitHub.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#configuring-copilot-settings-on-githubcom)
  * [Authenticating to an account on GHE.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#authenticating-to-an-account-on-ghecom)
  * [Further reading](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#further-reading)
  * [About GitHub Copilot in Visual Studio](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#about-github-copilot-in-visual-studio)
  * [Prerequisites](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#prerequisites-1)
  * [Using or rebinding keyboard shortcuts for GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#using-or-rebinding-keyboard-shortcuts-for-github-copilot-1)
  * [Enabling or disabling GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#enabling-or-disabling-github-copilot-1)
  * [Configuring ReSharper for GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#configuring-resharper-for-github-copilot)
  * [Configuring Copilot settings on GitHub.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#configuring-copilot-settings-on-githubcom-1)
  * [Authenticating to an account on GHE.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#authenticating-to-an-account-on-ghecom-1)
  * [Enabling next edit suggestions](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#enabling-next-edit-suggestions)
  * [Further reading](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#further-reading-1)
  * [About GitHub Copilot in Visual Studio Code](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#about-github-copilot-in-visual-studio-code)
  * [Keyboard shortcuts for GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#keyboard-shortcuts-for-github-copilot)
  * [Enabling or disabling GitHub Copilot code completion](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#enabling-or-disabling-github-copilot-code-completion)
  * [Enabling or disabling inline suggestions](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#enabling-or-disabling-inline-suggestions)
  * [Enabling next edit suggestions](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#enabling-next-edit-suggestions-1)
  * [Enabling or disabling GitHub Copilot for specific languages](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#enabling-or-disabling-github-copilot-for-specific-languages)
  * [Revoking GitHub Copilot authorization](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#revoking-github-copilot-authorization)
  * [Re-authorizing GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#re-authorizing-github-copilot)
  * [Configuring Copilot settings on GitHub.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#configuring-copilot-settings-on-githubcom-2)
  * [Authenticating to an account on GHE.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#authenticating-to-an-account-on-ghecom-2)
  * [Further reading](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#further-reading-2)
  * [Configuring GitHub Copilot in Vim/Neovim](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#configuring-github-copilot-in-vimneovim)
  * [Rebinding keyboard shortcuts](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#rebinding-keyboard-shortcuts-1)
  * [Configuring Copilot settings on GitHub.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#configuring-copilot-settings-on-githubcom-3)
  * [Authenticating to an account on GHE.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#authenticating-to-an-account-on-ghecom-3)
  * [Further reading](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#further-reading-3)
  * [About GitHub Copilot in Xcode](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#about-github-copilot-in-xcode)
  * [Prerequisites](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#prerequisites-2)
  * [Using or rebinding keyboard shortcuts for GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#using-or-rebinding-keyboard-shortcuts-for-github-copilot-2)
  * [Enabling or disabling GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#enabling-or-disabling-github-copilot-2)
  * [Automatically updating GitHub Copilot for Xcode](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#automatically-updating-github-copilot-for-xcode)
  * [Configuring Copilot settings on GitHub.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#configuring-copilot-settings-on-githubcom-4)
  * [Authenticating to an account on GHE.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#authenticating-to-an-account-on-ghecom-4)
  * [About GitHub Copilot in Eclipse](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#about-github-copilot-in-eclipse)
  * [Prerequisites](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#prerequisites-3)
  * [Using or rebinding keyboard shortcuts for GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#using-or-rebinding-keyboard-shortcuts-for-github-copilot-3)
  * [Rebinding keyboard shortcuts](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#rebinding-keyboard-shortcuts-3)
  * [Settings and configurations](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#settings-and-configurations)
  * [Configuring Copilot settings on GitHub.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#configuring-copilot-settings-on-githubcom-5)
  * [Authenticating to an account on GHE.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#authenticating-to-an-account-on-ghecom-5)


## [About GitHub Copilot in JetBrains IDEs](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#about-github-copilot-in-jetbrains-ides)
If you use a JetBrains IDE, GitHub Copilot can help you with a variety of tasks, including generating code suggestions, explaining how the code in your editor works, and suggesting code fixes. After installation, you can enable or disable GitHub Copilot, and you can configure advanced settings within your IDE or on GitHub. This article describes how to configure GitHub Copilot in the IntelliJ IDE, but the user interfaces of other JetBrains IDEs may differ.
## [Prerequisites](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#prerequisites)
To configure GitHub Copilot in a JetBrains IDE, you must install the GitHub Copilot plugin. For more information, see [Installing the GitHub Copilot extension in your environment](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/installing-the-github-copilot-extension-in-your-environment?tool=jetbrains).
## [Using or rebinding keyboard shortcuts for GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#using-or-rebinding-keyboard-shortcuts-for-github-copilot)
You can use the default keyboard shortcuts for inline suggestions in your JetBrains IDE when using GitHub Copilot. Alternatively, you can rebind the shortcuts to your preferred keyboard shortcuts for each specific command. For more information on rebinding keyboard shortcuts in your JetBrains IDE, see the JetBrains documentation. For example, you can view the [IntelliJ IDEA](https://www.jetbrains.com/help/idea/mastering-keyboard-shortcuts.html#choose-keymap) documentation.
### [Keyboard shortcuts for macOS](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#keyboard-shortcuts-for-macos)
Action | Shortcut  
---|---  
Accept an inline suggestion | `Tab`  
Dismiss an inline suggestion | `Esc`  
Show next inline suggestion |  `Option (⌥) or Alt`+`]`  
Show previous inline suggestion |  `Option (⌥) or Alt`+`[`  
Trigger inline suggestion |  `Option (⌥)`+`\`  
Open GitHub Copilot (additional suggestions in separate pane) |  `Option (⌥) or Alt`+`Return`  
### [Keyboard shortcuts for Windows](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#keyboard-shortcuts-for-windows)
Action | Shortcut  
---|---  
Accept an inline suggestion | `Tab`  
Dismiss an inline suggestion | `Esc`  
Show next inline suggestion |  `Alt`+`]`  
Show previous inline suggestion |  `Alt`+`[`  
Trigger inline suggestion |  `Alt`+`\`  
Open GitHub Copilot (additional suggestions in separate pane) |  `Alt`+`Enter`  
### [Keyboard shortcuts for Linux](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#keyboard-shortcuts-for-linux)
Action | Shortcut  
---|---  
Accept an inline suggestion | `Tab`  
Dismiss an inline suggestion | `Esc`  
Show next inline suggestion |  `Alt`+`]`  
Show previous inline suggestion |  `Alt`+`[`  
Trigger inline suggestion |  `Alt`+`\`  
Open GitHub Copilot (additional suggestions in separate pane) |  `Alt`+`Enter`  
## [Enabling or disabling GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#enabling-or-disabling-github-copilot)
You can enable or disable GitHub Copilot from within your JetBrains IDE. The GitHub Copilot status icon in the bottom panel of the JetBrains window indicates whether GitHub Copilot is enabled or disabled. When enabled, the icon is highlighted. When disabled, the icon is grayed out.
  1. To enable or disable GitHub Copilot, click the status icon in the bottom panel on the right of the JetBrains window.
![Screenshot of the bottom panel in a JetBrains IDE. The GitHub Copilot status icon is outlined in dark orange.](https://docs.github.com/assets/cb-3500/images/help/copilot/status-icon-jetbrains.png)
  2. If you are disabling GitHub Copilot, you will be asked whether you want to disable it globally, or for the language of the file you are currently editing. To disable globally, click **Disable Completions**. Alternatively, click the language-specific button to disable GitHub Copilot for the specified language.
![Screenshot of the menu to disable GitHub Copilot globally or for the current language in a JetBrains IDE.](https://docs.github.com/assets/cb-27124/images/help/copilot/disable-copilot-global-or-language-jetbrains.png)


## [Configuring advanced settings for GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#configuring-advanced-settings-for-github-copilot)
You can manage advanced settings for GitHub Copilot in your JetBrains IDE, such as how your IDE displays code completions, and which languages you want to enable or disable for GitHub Copilot.
  1. In your JetBrains IDE, click the **File** menu (Windows), or the name of the application in the menu bar (macOS), then click **Settings**.
  2. Under **Languages & Frameworks**, click **GitHub Copilot**.
  3. Edit the settings according to your personal preferences. 
     * To adjust the behavior and appearance of code suggestions, and whether to automatically check for updates, select or deselect the corresponding checkboxes.
     * If you have selected to receive automatic updates, you can choose whether to receive stable, but less frequent updates, or nightly updates, which may be less stable. Click the **Update channel** dropdown and select **Stable** for stable updates, or **Nightly** for nightly updates.


## [Configuring language settings for GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#configuring-language-settings-for-github-copilot)
You can specify which languages you want to activate or deactivate GitHub Copilot for either in the IDE or by editing your `github-copilot.xml` file. If you make changes to language settings in your IDE, you can individually select and deselect the languages you want to activate or deactivate.
If you make changes to the language settings in your `github-copilot.xml` file, you can specify individual languages, or you can use a wildcard to activate or deactivate GitHub Copilot for all languages. You can also specify exceptions, which will override the wild card setting for the specified languages. For example, you can deactivate GitHub Copilot for all languages, except for Python and YAML. By default, when you install the GitHub Copilot extension, GitHub Copilot is activated for all languages.
### [Configuring language settings in the IDE](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#configuring-language-settings-in-the-ide)
  1. In your JetBrains IDE, click the **File** menu (Windows), or the name of the application in the menu bar (macOS), then click **Settings**.
  2. Under **Languages & Frameworks**, click **GitHub Copilot**.
  3. Under "Languages," select or deselect the checkboxes for the languages you want to activate or deactivate GitHub Copilot for.
  4. Click **Apply** , and then click **OK**.
  5. Restart your JetBrains IDE for the changes to take effect.


### [Editing your `github-copilot.xml` file](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#editing-your-github-copilotxml-file)
To configure language settings in the `github-copilot.xml` file, you must edit the `languageAllowList`. Every line you add to the `languageAllowList` must contain an entry key and a value. The entry key is the name of the language, or (`*`) for a wildcard. The value is either `true` or `false`. If the value is `true`, GitHub Copilot is activated for the specified language. If the value is `false`, GitHub Copilot is deactivated for the specified language.
The file is located in the following directory:
  * **macOS:** `~/Library/Application Support/JetBrains/<product><version>/options/github-copilot.xml`
  * **Windows:** `%APPDATA%\JetBrains\<product><version>\options\github-copilot.xml`
  * **Linux:** `~/.config/JetBrains/<product><version>/options/github-copilot.xml`


For example, if you are using IntelliJ IDEA 2021.1 on macOS, the file is located at `~/Library/Application Support/JetBrains/IdeaIC2021.1/options/github-copilot.xml`.
The `github-copilot.xml` file might not be generated until you make a change to your default language configuration in the IDE's settings. If you cannot locate the file, you should try modifying the default language settings in the IDE. For more information, see [Configuring language settings in the IDE](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#configuring-language-settings-in-the-ide).
Alternatively, you can create the file manually and save it in the location for your operating system listed above. For more information, see [Example language configurations](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#example-language-configurations).
  1. Open the `github-copilot.xml` file in a text editor.
  2. Between the `<map>` tags, add the line or lines for the languages you want to activate or deactivate GitHub Copilot for. For example, to deactivate GitHub Copilot for all languages:
XML```
<entry key="*" value="false" />

```
```
<entry key="*" value="false" />

```

  3. Save the changes to the `github-copilot.xml` file.
  4. Restart your JetBrains IDE for the changes to take effect.


### [Example language configurations](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#example-language-configurations)
The default configuration of the `github-copilot.xml` file, which enables GitHub Copilot for all languages is as follows:
XML```
<application>
  <component name="github-copilot">
    <languageAllowList>
      <map>
        <entry key="*" value="true" />
      </map>
    </languageAllowList>
  </component>
</application>

```
```
<application>
  <component name="github-copilot">
    <languageAllowList>
      <map>
        <entry key="*" value="true" />
      </map>
    </languageAllowList>
  </component>
</application>

```

To deactivate GitHub Copilot for all languages, the wildcard (`*`) value is changed to `false`:
XML```
<application>
  <component name="github-copilot">
    <languageAllowList>
      <map>
        <entry key="*" value="false" />
      </map>
    </languageAllowList>
  </component>
</application>

```
```
<application>
  <component name="github-copilot">
    <languageAllowList>
      <map>
        <entry key="*" value="false" />
      </map>
    </languageAllowList>
  </component>
</application>

```

To specify languages individually, add an entry for each language you want to activate or deactivate GitHub Copilot for. Specific language settings will override the wildcard. For example, to activate GitHub Copilot for Python and YAML, and deactivate GitHub Copilot for all other languages, add the following entries:
XML```
<application>
  <component name="github-copilot">
    <languageAllowList>
      <map>
        <entry key="*" value="false" />
        <entry key="Python" value="true" />
        <entry key="YAML" value="true" />
      </map>
    </languageAllowList>
  </component>
</application>

```
```
<application>
  <component name="github-copilot">
    <languageAllowList>
      <map>
        <entry key="*" value="false" />
        <entry key="Python" value="true" />
        <entry key="YAML" value="true" />
      </map>
    </languageAllowList>
  </component>
</application>

```

You can also add a configuration to make the `languageAllowList` readonly in the IDE's settings. This will prevent you from changing the language settings in the IDE. For example:
XML```
<application>
  <component name="github-copilot">
    <option name="languageAllowListReadOnly" value="true" />
    <languageAllowList>
      <map>
        <entry key="*" value="true" />
      </map>
    </languageAllowList>
  </component>
</application>

```
```
<application>
  <component name="github-copilot">
    <option name="languageAllowListReadOnly" value="true" />
    <languageAllowList>
      <map>
        <entry key="*" value="true" />
      </map>
    </languageAllowList>
  </component>
</application>

```

## [Configuring Copilot settings on GitHub.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#configuring-copilot-settings-on-githubcom)
If you are using a Copilot Pro plan, you can choose to allow or block code completion suggestions that match publicly available code. You can also allow or block the collection and retention of the prompts you enter and Copilot's suggestions. You configure this in your personal settings on GitHub.com. See [Managing Copilot policies as an individual subscriber](https://docs.github.com/en/copilot/configuring-github-copilot/configuring-your-personal-github-copilot-settings-on-githubcom).
## [Authenticating to an account on GHE.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#authenticating-to-an-account-on-ghecom)
If you're using a Copilot plan for a managed user account on GHE.com, you'll need to update some settings before you sign in. See [Using GitHub Copilot with an account on GHE.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/using-github-copilot-with-an-account-on-ghecom).
## [Further reading](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#further-reading)
  * [GitHub Copilot FAQ](https://github.com/features/copilot/#faq)


## [About GitHub Copilot in Visual Studio](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#about-github-copilot-in-visual-studio)
If you use Visual Studio, GitHub Copilot can help you with a variety of tasks, including generating code suggestions, explaining how the code in your editor works, and suggesting code fixes. After installation, you can enable or disable GitHub Copilot, and you can configure advanced settings within Visual Studio or on GitHub.
## [Prerequisites](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#prerequisites-1)
To configure GitHub Copilot in Visual Studio, you must install the GitHub Copilot plugin. For more information, see [Installing the GitHub Copilot extension in your environment](https://docs.github.com/en/copilot/configuring-github-copilot/installing-the-github-copilot-extension-in-your-environment?tool=visualstudio).
## [Using or rebinding keyboard shortcuts for GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#using-or-rebinding-keyboard-shortcuts-for-github-copilot-1)
You can use the default keyboard shortcuts in Visual Studio when using GitHub Copilot. Alternatively, you can rebind the shortcuts in the Tools settings for Visual Studio using your preferred keyboard shortcuts for each specific command. You can search for each keyboard shortcut by its command name in the Keyboard Shortcuts editor.
### [Using default keyboard shortcuts](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#using-default-keyboard-shortcuts)
Action | Shortcut | Command name  
---|---|---  
Show next inline suggestion |  `Alt`+`.` | Edit.NextSuggestion  
Show previous inline suggestion |  `Alt`+`,` | Edit.PreviousSuggestion  
### [Rebinding keyboard shortcuts](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#rebinding-keyboard-shortcuts)
If you don't want to use the default keyboard shortcuts in Visual Studio when using GitHub Copilot, you can rebind the shortcuts in the Keyboard editor using your preferred keyboard shortcuts for each specific command.
  1. In the Visual Studio menu bar, under **Tools** , click **Options**.
![Screenshot of the Visual Studio menu bar. The "Tools" menu is expanded, and the "Options" item is highlighted with an orange outline.](https://docs.github.com/assets/cb-37169/images/help/copilot/vs-toolbar-options.png)
  2. In the "Options" dialog, under **Environment** , click **Keyboard**.
  3. Under "Show commands containing:", search for the command you want to rebind.
![Screenshot of the "Show commands containing" search bar. The string "tools.next" is entered in the search field.](https://docs.github.com/assets/cb-3955/images/help/copilot/vs-show-commands-containing.png)
  4. Under "Press shortcut keys," type the shortcut you want to assign to the command, then click **Assign**.
![Screenshot of the fields for entering a new keyboard shortcut assignment.](https://docs.github.com/assets/cb-6734/images/help/copilot/vs-rebind-shortcut.png)


## [Enabling or disabling GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#enabling-or-disabling-github-copilot-1)
The GitHub Copilot status icon in the bottom panel of the Visual Studio window indicates whether GitHub Copilot is enabled or disabled. When enabled, the background color of the icon will match the color of the status bar. When disabled, it will have a diagonal line through it.
  1. To enable or disable GitHub Copilot, click the GitHub Copilot icon in the bottom panel of the Visual Studio window.
![Screenshot of editor margin in Visual Studio with the GitHub Copilot icon emphasized.](https://docs.github.com/assets/cb-4947/images/help/copilot/editor-margin-visual-studio.png)
  2. If you are disabling GitHub Copilot, you will be asked whether you want to disable suggestions globally, or for the language of the file you are currently editing.
     * To disable suggestions from GitHub Copilot globally, click **Enable Globally**.
     * To disable suggestions from GitHub Copilot for the specified language, click **Enable for LANGUAGE**.


## [Configuring ReSharper for GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#configuring-resharper-for-github-copilot)
If you use ReSharper, GitHub Copilot may work best when you configure ReSharper to use GitHub Copilot's native IntelliSense. For more information about ReSharper, see the [ReSharper documentation](https://www.jetbrains.com/resharper/documentation/documentation.html)
  1. In the Visual Studio menu bar, under **Extensions** , click **ReSharper** , then click **Options**.
  2. In the "Options" dialog, under **Environment** , click **IntelliSense** and then click **General**.
  3. Under "General" select **Visual Studio** and then click **Save**.


## [Configuring Copilot settings on GitHub.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#configuring-copilot-settings-on-githubcom-1)
If you are using a Copilot Pro plan, you can choose to allow or block code completion suggestions that match publicly available code. You can also allow or block the collection and retention of the prompts you enter and Copilot's suggestions. You configure this in your personal settings on GitHub.com. See [Managing Copilot policies as an individual subscriber](https://docs.github.com/en/copilot/configuring-github-copilot/configuring-your-personal-github-copilot-settings-on-githubcom).
## [Authenticating to an account on GHE.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#authenticating-to-an-account-on-ghecom-1)
If you're using a Copilot plan for a managed user account on GHE.com, you'll need to update some settings before you sign in. See [Using GitHub Copilot with an account on GHE.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/using-github-copilot-with-an-account-on-ghecom).
## [Enabling next edit suggestions](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#enabling-next-edit-suggestions)
To use next edit suggestions in Visual Studio, you need to enable the feature first.
  1. In the Visual Studio menu bar, under **Tools** , click **Options**.
  2. In the "Options" dialog, under **GitHub** , click **Copilot** and then click **Copilot Completions**.
  3. Check **Enable next edit suggestions**.


## [Further reading](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#further-reading-1)
  * [GitHub Copilot FAQ](https://github.com/features/copilot/#faq)


## [About GitHub Copilot in Visual Studio Code](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#about-github-copilot-in-visual-studio-code)
If you use Visual Studio Code, GitHub Copilot can help you with a variety of tasks, including generating code suggestions, explaining how the code in your editor works, and suggesting edits based on your instructions. You can enable or disable GitHub Copilot, and configure advanced settings within Visual Studio Code or on GitHub.
You can learn more about scenarios and setup in the [VS Code documentation](https://code.visualstudio.com/docs/copilot/overview#_use-cases-for-github-copilot-in-vs-code).
## [Keyboard shortcuts for GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#keyboard-shortcuts-for-github-copilot)
You can use the default keyboard shortcuts for GitHub Copilot in GitHub Copilot. Search keyboard shortcuts by command name in the Keyboard Shortcuts editor.
Alternatively, you can rebind the shortcut for each command in the Keyboard Shortcuts editor. For more information, see the [VS Code documentation on editing shortcuts](https://code.visualstudio.com/Docs/editor/keybindings).
### [Keyboard shortcuts for macOS](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#keyboard-shortcuts-for-macos-1)
Action | Shortcut | Command name  
---|---|---  
Accept an inline suggestion | `Tab` | editor.action.inlineSuggest.commit  
Dismiss an inline suggestion | `Esc` | editor.action.inlineSuggest.hide  
Show next inline suggestion |  `Option (⌥)`+`]`  
| editor.action.inlineSuggest.showNext  
Show previous inline suggestion |  `Option (⌥)`+`[`  
| editor.action.inlineSuggest.showPrevious  
Trigger inline suggestion |  `Option (⌥)`+`\`  
| editor.action.inlineSuggest.trigger  
Open GitHub Copilot (additional suggestions in separate pane) |  `Ctrl`+`Return` | github.copilot.generate  
Toggle GitHub Copilot on/off | _No default shortcut_ | github.copilot.toggleCopilot  
### [Keyboard shortcuts for Windows](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#keyboard-shortcuts-for-windows-1)
Action | Shortcut | Command name  
---|---|---  
Accept an inline suggestion | `Tab` | editor.action.inlineSuggest.commit  
Dismiss an inline suggestion | `Esc` | editor.action.inlineSuggest.hide  
Show next inline suggestion |  `Alt`+`]` | editor.action.inlineSuggest.showNext  
Show previous inline suggestion |  `Alt`+`[` | editor.action.inlineSuggest.showPrevious  
Trigger inline suggestion |  `Alt`+`\` | editor.action.inlineSuggest.trigger  
Open GitHub Copilot (additional suggestions in separate pane) |  `Ctrl`+`Enter` | github.copilot.generate  
Toggle GitHub Copilot on/off | _No default shortcut_ | github.copilot.toggleCopilot  
### [Keyboard shortcuts for Linux](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#keyboard-shortcuts-for-linux-1)
Action | Shortcut | Command name  
---|---|---  
Accept an inline suggestion | `Tab` | editor.action.inlineSuggest.commit  
Dismiss an inline suggestion | `Esc` | editor.action.inlineSuggest.hide  
Show next inline suggestion |  `Alt`+`]` | editor.action.inlineSuggest.showNext  
Show previous inline suggestion |  `Alt`+`[` | editor.action.inlineSuggest.showPrevious  
Trigger inline suggestion |  `Alt`+`\` | editor.action.inlineSuggest.trigger  
Open GitHub Copilot (additional suggestions in separate pane) |  `Ctrl`+`Enter` | github.copilot.generate  
Toggle GitHub Copilot on/off | _No default shortcut_ | github.copilot.toggleCopilot  
## [Enabling or disabling GitHub Copilot code completion](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#enabling-or-disabling-github-copilot-code-completion)
You can enable or disable GitHub Copilot from within Visual Studio Code.
  1. To configure code completion, click the arrow next to the **Configure code completions**.
![Screenshot of the option in the GitHub Copilot dropdown. Configure code completions is highlighted in orange.](https://docs.github.com/assets/cb-92287/images/help/copilot/configure-code-completions-option-vscode.png)
  2. In the "Configure Copilot Completions" dialog, select **Enable Completions** or **Disable Completions**.
![Screenshot of the "Configure Copilot Completions" dialog. Enable Completions and Disable Completions options are highlighted in orange.](https://docs.github.com/assets/cb-18235/images/help/copilot/disable-completions-dialog.png)


## [Enabling or disabling inline suggestions](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#enabling-or-disabling-inline-suggestions)
You can choose to enable or disable inline suggestions for GitHub Copilot in Visual Studio Code.
  1. In the **File** menu, navigate to **Preferences** and click **Settings**.
![Screenshot of Visual Studio Code settings.](https://docs.github.com/assets/cb-99970/images/help/copilot/vsc-settings.png)
  2. In the left-side panel of the settings tab, click **Extensions** and then select **Copilot**.
  3. Under "Inline Suggest:Enable," select or deselect the checkbox to enable or disable inline suggestions.


## [Enabling next edit suggestions](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#enabling-next-edit-suggestions-1)
You can enable next edit suggestions via the VS Code setting `github.copilot.nextEditSuggestions.enabled`. For more detailed instructions, see [Enabling edit suggestions](https://code.visualstudio.com/docs/copilot/ai-powered-suggestions#_enabling-edit-suggestions) in the VS Code documentation.
If you're using a Copilot Business plan, the organization that provides your plan must enable the **Editor preview features** setting. See [Managing policies for Copilot in your organization](https://docs.github.com/en/enterprise-cloud@latest/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization#enabling-copilot-features-in-your-organization).
## [Enabling or disabling GitHub Copilot for specific languages](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#enabling-or-disabling-github-copilot-for-specific-languages)
You can specify which languages you want to enable or disable GitHub Copilot for.
  1. From the Visual Studio Code, click the **Extensions** tab, then navigate to the **Copilot** section. For more information, see [Enabling or disabling inline suggestions](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#enabling-or-disabling-inline-suggestions).
  2. Under "Enable or disable Copilot for specified languages," click **Edit in settings.json**.
  3. In the _settings.json_ file, add or remove the languages you want to enable or disable GitHub Copilot for. For example, to enable Python in GitHub Copilot, add `"python": true` to the list, ensuring there is a trailing comma after all but the last list item.
```
{
    "editor.inlineSuggest.enabled": true,
    "github.copilot.enable": {
        "*": true,
        "yaml": false,
        "plaintext": false,
        "markdown": true,
        "javascript": true,
        "python": true
    }
}

```



## [Revoking GitHub Copilot authorization](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#revoking-github-copilot-authorization)
Visual Studio Code retains authorization to use GitHub Copilot through a particular GitHub account. If you want to prevent your GitHub account being used for GitHub Copilot on a device you no longer have access to, you can revoke authorization and then go through the authorization process again. The device you previously used will not have the new authorization.
  1. In the upper-right corner of any page on GitHub, click your profile photo, then click 
  2. In the "Integrations" section of the sidebar, click 
  3. Click the **Authorized OAuth Apps** tab.
![Screenshot of the "Applications" page. A tab, labeled "Authorized OAuth Apps," is highlighted with an orange outline.](https://docs.github.com/assets/cb-25464/images/help/settings/settings-authorized-oauth-apps-tab.png)
  4. Click the **...** next to **GitHub for VS Code** and click **Revoke**.
  5. Click the **Authorized GitHub Apps** tab.
  6. If the **GitHub Copilot** extension is listed, click **Revoke**.


After revoking authorization, Visual Studio Code will be able to continue using GitHub Copilot in a current session for a maximum of 30 minutes. After that time, you will need to reauthorize GitHub Copilot for use in Visual Studio Code again.
## [Re-authorizing GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#re-authorizing-github-copilot)
After you have revoked authorization, if you want to continue using GitHub Copilot, you will need to complete the reauthorization process.
  1. In the bottom left corner of Visual Studio Code, click the **Accounts** icon, hover over your username, and click **Sign out**.
![Screenshot of the menu in Visual Studio Code. The "Sign out" option is outlined in dark orange.](https://docs.github.com/assets/cb-35190/images/help/copilot/vsc-sign-out.png)
  2. In the "Visual Studio Code" pop-up, click **Sign Out**.
  3. In the bottom left corner of Visual Studio Code, click the **Accounts** icon, hover over your username, and click **Sign in with GitHub to use GitHub Copilot**.
![Screenshot of the accounts menu in Visual Studio Code. The "Sign in with GitHub to use GitHub Copilot \(1\)" option is outlined in dark orange.](https://docs.github.com/assets/cb-25979/images/help/copilot/vsc-sign-in.png)
  4. In your browser, GitHub will request the necessary permissions for GitHub Copilot. To approve these permissions, click **Continue**.
  5. In the "Open Visual Studio Code?" pop-up, click **Open Visual Studio Code**.


## [Configuring Copilot settings on GitHub.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#configuring-copilot-settings-on-githubcom-2)
If you are using a Copilot Pro plan, you can choose to allow or block code completion suggestions that match publicly available code. You can also allow or block the collection and retention of the prompts you enter and Copilot's suggestions. You configure this in your personal settings on GitHub.com. See [Managing Copilot policies as an individual subscriber](https://docs.github.com/en/copilot/configuring-github-copilot/configuring-your-personal-github-copilot-settings-on-githubcom).
## [Authenticating to an account on GHE.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#authenticating-to-an-account-on-ghecom-2)
If you're using a Copilot plan for a managed user account on GHE.com, you'll need to update some settings before you sign in. See [Using GitHub Copilot with an account on GHE.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/using-github-copilot-with-an-account-on-ghecom).
## [Further reading](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#further-reading-2)
  * [GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/overview)
  * [GitHub Copilot FAQ](https://github.com/features/copilot/#faq)


## [Configuring GitHub Copilot in Vim/Neovim](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#configuring-github-copilot-in-vimneovim)
For guidance on configuring GitHub Copilot in Vim/Neovim, invoke the GitHub Copilot documentation in Vim/Neovim by running the following command:
```
:help copilot

```

## [Rebinding keyboard shortcuts](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#rebinding-keyboard-shortcuts-1)
You can rebind the keyboard shortcuts in Vim/Neovim when using GitHub Copilot to use your preferred keyboard shortcuts for each specific command. For more information, see the [Map](https://neovim.io/doc/user/map.html) article in the Neovim documentation.
## [Configuring Copilot settings on GitHub.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#configuring-copilot-settings-on-githubcom-3)
If you are using a Copilot Pro plan, you can choose to allow or block code completion suggestions that match publicly available code. You can also allow or block the collection and retention of the prompts you enter and Copilot's suggestions. You configure this in your personal settings on GitHub.com. See [Managing Copilot policies as an individual subscriber](https://docs.github.com/en/copilot/configuring-github-copilot/configuring-your-personal-github-copilot-settings-on-githubcom).
## [Authenticating to an account on GHE.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#authenticating-to-an-account-on-ghecom-3)
If you're using a Copilot plan for a managed user account on GHE.com, you'll need to update some settings before you sign in. See [Using GitHub Copilot with an account on GHE.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/using-github-copilot-with-an-account-on-ghecom).
## [Further reading](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#further-reading-3)
  * [GitHub Copilot FAQ](https://github.com/features/copilot/#faq)


## [About GitHub Copilot in Xcode](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#about-github-copilot-in-xcode)
If you use Xcode, GitHub Copilot can help you with a variety of tasks, including generating code suggestions, explaining how the code in your editor works, and suggesting code fixes. After installation, you can enable or disable GitHub Copilot, and you can configure advanced settings within Xcode or on GitHub.
## [Prerequisites](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#prerequisites-2)
To configure GitHub Copilot for Xcode, you must install the GitHub Copilot extension. See [Installing the GitHub Copilot extension in your environment](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/installing-the-github-copilot-extension-in-your-environment?tool=xcode).
## [Using or rebinding keyboard shortcuts for GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#using-or-rebinding-keyboard-shortcuts-for-github-copilot-2)
You can use the default keyboard shortcuts for inline suggestions in Xcode when using GitHub Copilot. Alternatively, you can rebind the shortcuts to your preferred keyboard shortcuts for each specific command.
### [Default keyboard shortcuts](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#default-keyboard-shortcuts)
Action | Shortcut  
---|---  
Accept the first line of a suggestion | `Tab`  
View full suggestion | Hold `Option`  
Accept full suggestion |  `Option`+`Tab`  
### [Rebinding keyboard shortcuts](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#rebinding-keyboard-shortcuts-2)
If you don't want to use the default keyboard shortcuts for GitHub Copilot, you can rebind the shortcuts in the Key Bindings editor and use your preferred keyboard shortcuts.
If you want to use something besides `Tab` to accept the first line of a suggestion, you need to disable the "Accept suggestions with Tab" option in the advanced settings in the GitHub Copilot for Xcode application. Additionally, we currently only support the `Option` key for the "View full suggestion" action.
  1. In the Xcode menu, click **Xcode** then **Settings**.
  2. Click **Key Bindings** and search for "Copilot" to find the commands you want to rebind.


## [Enabling or disabling GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#enabling-or-disabling-github-copilot-2)
You can enable or disable the GitHub Copilot extension from within the application.
  1. Open the GitHub Copilot for Xcode application.
  2. At the top of the application window, click **Advanced**.
  3. In the "Suggestion Settings" section, use the "Request suggestions while typing" toggle to enable or disable the extension.


## [Automatically updating GitHub Copilot for Xcode](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#automatically-updating-github-copilot-for-xcode)
You can configure the GitHub Copilot extension to automatically check for updates.
  1. Open the GitHub Copilot for Xcode application.
  2. Select **Automatically check for updates**.


After updating the extension, Xcode must be restarted for the changes to take effect.
## [Configuring Copilot settings on GitHub.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#configuring-copilot-settings-on-githubcom-4)
If you are using a Copilot Pro plan, you can choose to allow or block code completion suggestions that match publicly available code. You can also allow or block the collection and retention of the prompts you enter and Copilot's suggestions. You configure this in your personal settings on GitHub.com. See [Managing Copilot policies as an individual subscriber](https://docs.github.com/en/copilot/configuring-github-copilot/configuring-your-personal-github-copilot-settings-on-githubcom).
## [Authenticating to an account on GHE.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#authenticating-to-an-account-on-ghecom-4)
If you're using a Copilot plan for a managed user account on GHE.com, you'll need to update some settings before you sign in. See [Using GitHub Copilot with an account on GHE.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/using-github-copilot-with-an-account-on-ghecom).
## [About GitHub Copilot in Eclipse](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#about-github-copilot-in-eclipse)
If you use Eclipse, GitHub Copilot can provide code suggestions as you work in the IDE. You can also use the Copilot Chat panel to work with Copilot as your AI pair programmer.
After you install GitHub Copilot in Eclipse, you can enable or disable it, and you can configure advanced settings within the IDE.
## [Prerequisites](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#prerequisites-3)
To configure GitHub Copilot in Eclipse, you must install the GitHub Copilot extension. See [Installing the GitHub Copilot extension in your environment](https://docs.github.com/en/copilot/configuring-github-copilot/installing-the-github-copilot-extension-in-your-environment?tool=eclipse).
## [Using or rebinding keyboard shortcuts for GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#using-or-rebinding-keyboard-shortcuts-for-github-copilot-3)
You can use the default keyboard shortcuts for inline suggestions in Eclipse when using GitHub Copilot. Alternatively, you can rebind the shortcuts to your preferred keyboard shortcuts for each specific command.
## [Rebinding keyboard shortcuts](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#rebinding-keyboard-shortcuts-3)
If you don't want to use the default keyboard shortcuts for GitHub Copilot, you can rebind the shortcuts in the Key Bindings editor and use your preferred keyboard shortcuts.
  1. In the IDE, click 
  2. Click **Edit Keyboard Shortcuts...** to rebind the shortcuts.


## [Settings and configurations](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#settings-and-configurations)
For advanced settings, you can set auto-completion behavior, configure proxy, and assign a GitHub Enterprise authentication endpoint.
## [Configuring Copilot settings on GitHub.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#configuring-copilot-settings-on-githubcom-5)
If you are using a Copilot Pro plan, you can choose to allow or block code completion suggestions that match publicly available code. You can also allow or block the collection and retention of the prompts you enter and Copilot's suggestions. You configure this in your personal settings on GitHub.com. See [Managing Copilot policies as an individual subscriber](https://docs.github.com/en/copilot/configuring-github-copilot/configuring-your-personal-github-copilot-settings-on-githubcom).
## [Authenticating to an account on GHE.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#authenticating-to-an-account-on-ghecom-5)
If you're using a Copilot plan for a managed user account on GHE.com, you'll need to update some settings before you sign in. See [Using GitHub Copilot with an account on GHE.com](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/using-github-copilot-with-an-account-on-ghecom).
