  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Manage Copilot](https://docs.github.com/en/copilot/managing-copilot "Manage Copilot")/
  * [Configure content exclusion](https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion "Configure content exclusion")/
  * [Exclude content from Copilot](https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion/excluding-content-from-github-copilot "Exclude content from Copilot")


# Excluding content from GitHub Copilot
You can prevent Copilot from accessing certain content.
## Who can use this feature?
Repository administrators and organization owners can manage content exclusion settings. People with the "Maintain" role for a repository can view, but not edit, content exclusion settings for that repository.
Organizations with a Copilot Business or Copilot Enterprise plan.
## In this article
  * [About content exclusions for Copilot](https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion/excluding-content-from-github-copilot#about-content-exclusions-for-copilot)
  * [Configuring content exclusions for your repository](https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion/excluding-content-from-github-copilot#configuring-content-exclusions-for-your-repository)
  * [Configuring content exclusions for your organization](https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion/excluding-content-from-github-copilot#configuring-content-exclusions-for-your-organization)
  * [Testing changes to content exclusions](https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion/excluding-content-from-github-copilot#testing-changes-to-content-exclusions)
  * [Further reading](https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion/excluding-content-from-github-copilot#further-reading)


## [About content exclusions for Copilot](https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion/excluding-content-from-github-copilot#about-content-exclusions-for-copilot)
You can use content exclusions to configure Copilot to ignore certain files. When you exclude content from Copilot:
  * Code completion will not be available in the affected files.
  * The content in affected files will not inform code completion suggestions in other files.
  * The content in affected files will not inform GitHub Copilot Chat's responses.
  * Affected files will not be reviewed in a Copilot code review.


### [Who can configure content exclusion](https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion/excluding-content-from-github-copilot#who-can-configure-content-exclusion)
Repository administrators and organization owners can configure content exclusion.
  * **Repository administrators** can exclude content for their own repositories. This affects any Copilot users in the enterprise working within those specific repositories.
  * **Organization owners** can exclude content for users assigned a Copilot seat through their organization.


### [Availability of content exclusions](https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion/excluding-content-from-github-copilot#availability-of-content-exclusions)
Tool | Code completion support | Copilot Chat support  
---|---|---  
Visual Studio |  |   
Visual Studio Code |  |   
JetBrains IDEs |  |   
Vim/Neovim |  | Not applicable  
Xcode |  |   
Eclipse |  |   
Azure Data Studio |  | Not applicable  
The GitHub website | Not applicable |   
GitHub Mobile | Not applicable |   
Content exclusions also apply to Copilot code review on the GitHub website.
Content exclusion is in public preview on the GitHub website and in GitHub Mobile and is subject to change.
### [Limitations of content exclusions](https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion/excluding-content-from-github-copilot#limitations-of-content-exclusions)
It's possible that Copilot may use semantic information from an excluded file if the information is provided by the IDE indirectly. Examples of such content include type information and hover-over definitions for symbols used in code, as well as general project properties such as build configuration information.
Currently, content exclusions do not apply to symbolic links (symlinks).
### [Data sent to GitHub](https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion/excluding-content-from-github-copilot#data-sent-to-github)
After you configure content exclusion, the client (for example, the Copilot extension for VS Code) sends the current repository URL to the GitHub server so that the server can return the correct policy to the client. These URLs are not logged anywhere.
## [Configuring content exclusions for your repository](https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion/excluding-content-from-github-copilot#configuring-content-exclusions-for-your-repository)
You can use your repository settings to specify content in your repository that GitHub Copilot should ignore.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Code & automation" section of the sidebar, click 
If your repository inherits any exclusions from its parent organization, you'll see a gray box at the top of the page containing details of these exclusions. You cannot edit these settings.
  4. In the box following "Paths to exclude in this repository," enter the paths to files from which Copilot should be excluded.
Use the format: `- "/PATH/TO/DIRECTORY/OR/FILE"`, with each path on a separate line. You can add comments by starting a line with `#`.
You can use fnmatch pattern matching notation to specify file paths. Patterns are case insensitive. See [File](https://ruby-doc.org/core-2.5.1/File.html#method-c-fnmatch) in the ruby-doc.org documentation.


### [Example of paths specified in the repository settings](https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion/excluding-content-from-github-copilot#example-of-paths-specified-in-the-repository-settings)
YAML
BesideInline
```
# Ignore the `/src/some-dir/kernel.rs` file in this repository.
- "/src/some-dir/kernel.rs"

# Ignore files called `secrets.json` anywhere in this repository.
- "secrets.json"

# Ignore all files whose names begin with `secret` anywhere in this repository.
- "secret*"

# Ignore files whose names end with `.cfg` anywhere in this repository.
- "*.cfg"

# Ignore all files in or below the `/scripts` directory of this repository.
- "/scripts/**"

```

```
- "/src/some-dir/kernel.rs"
```

Ignore the `/src/some-dir/kernel.rs` file in this repository.
```
- "secrets.json"
```

Ignore files called `secrets.json` anywhere in this repository.
```
- "secret*"
```

Ignore all files whose names begin with `secret` anywhere in this repository.
```
- "*.cfg"
```

Ignore files whose names end with `.cfg` anywhere in this repository.
```
- "/scripts/**"
```

Ignore all files in or below the `/scripts` directory of this repository.
```
# Ignore the `/src/some-dir/kernel.rs` file in this repository.
- "/src/some-dir/kernel.rs"

# Ignore files called `secrets.json` anywhere in this repository.
- "secrets.json"

# Ignore all files whose names begin with `secret` anywhere in this repository.
- "secret*"

# Ignore files whose names end with `.cfg` anywhere in this repository.
- "*.cfg"

# Ignore all files in or below the `/scripts` directory of this repository.
- "/scripts/**"

```

## [Configuring content exclusions for your organization](https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion/excluding-content-from-github-copilot#configuring-content-exclusions-for-your-organization)
You can use your organization settings to specify files that GitHub Copilot should ignore. The files can be within a Git repository or anywhere on the file system that is not under Git control.
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the left sidebar, click **Content exclusion**.
  4. In the box following "Repositories and paths to exclude," enter the details of files from which Copilot should be excluded.
To exclude files located anywhere (within a Git repository or elsewhere), enter `"*":` followed by the path to the file, or files, you want to exclude. If you want to specify multiple file path patterns, list each pattern on a separate line.
To exclude files in a Git repository from Copilot, enter a reference to the repository on one line, followed by paths to locations within the repository, with each path on a separate line. Use the following format, replacing `REPOSITORY-REFERENCE` with a reference to the repository that contains the files you'd like to exclude:
```
REPOSITORY-REFERENCE:
  - "/PATH/TO/DIRECTORY/OR/FILE"
  - "/PATH/TO/DIRECTORY/OR/FILE"
  - ...

```

Repositories can be referenced using various protocols. You can use any of the following syntaxes for `REPOSITORY-REFERENCE` and Copilot will match them regardless of how the repository was cloned locally:
```
http[s]://host.xz[:port]/path/to/repo.git/

git://host.xz[:port]/path/to/repo.git/

[user@]host.xz:path/to/repo.git/

ssh://[user@]host.xz[:port]/path/to/repo.git/

```

The `user@` and `:port` parts of the `REPOSITORY-REFERENCE` are ignored in the calculation of which paths to ignore for a repository.
For Azure DevOps, you can use the new (dev.azure.com) or old (visualstudio.com) host format when specifying `REPOSITORY-REFERENCE`, and Copilot will match them regardless of which host was used to clone the repository locally.
You can use fnmatch pattern matching notation to specify file paths. Patterns are case insensitive. See [File](https://ruby-doc.org/core-2.5.1/File.html#method-c-fnmatch) in the ruby-doc.org documentation.


### [Example of repositories and paths in organization settings](https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion/excluding-content-from-github-copilot#example-of-repositories-and-paths-in-organization-settings)
YAML
BesideInline
```
# Ignore all `.env` files from all file system roots (Git and non-Git).
# For example, this excludes `REPOSITORY-PATH/.env` and also `/.env`.
# This could also have been written on a single line as:
#
# "*": ["**/.env"]
"*":
  - "**/.env"

# In the `octo-repo` repository in this organization:
octo-repo:
  # Ignore the `/src/some-dir/kernel.rs` file.
  - "/src/some-dir/kernel.rs"

# In the `primer/react` repository on GitHub:
https://github.com/primer/react.git:
  # Ignore files called `secrets.json` anywhere in this repository.
  - "secrets.json"
  # Ignore files called `temp.rb` in or below the `/src` directory.
  - "/src/**/temp.rb"

# In the `copilot` repository of any GitHub organization:
git@github.com:*/copilot:
  # Ignore any files in or below the `/__tests__` directory.
  - "/__tests__/**"
  # Ignore any files in the `/scripts` directory.
  - "/scripts/*"

# In the `gitlab-org/gitlab-runner` repository on GitLab:
git@gitlab.com:gitlab-org/gitlab-runner.git:
  # Ignore the `/main_test.go` file.
  - "/main_test.go"
  # Ignore any files with names beginning with `server` or `session` anywhere in this repository.
  - "{server,session}*"
  # Ignore any files with names ending with `.md` or `.mk` anywhere in this repository.
  - "*.m[dk]"
  # Ignore files directly within directories such as `packages` or `packaged` anywhere in this repository.
  - "**/package?/*"
  # Ignore files in or below any `security` directories, anywhere in this repository.
  - "**/security/**"

```

```
"*":
  - "**/.env"
```

Ignore all `.env` files from all file system roots (Git and non-Git). For example, this excludes `REPOSITORY-PATH/.env` and also `/.env`. This could also have been written on a single line as:
"*": ["**/.env"]
```
octo-repo:
```

In the `octo-repo` repository in this organization:
```
  - "/src/some-dir/kernel.rs"
```

Ignore the `/src/some-dir/kernel.rs` file.
```
https://github.com/primer/react.git:
```

In the `primer/react` repository on GitHub:
```
  - "secrets.json"
```

Ignore files called `secrets.json` anywhere in this repository.
```
  - "/src/**/temp.rb"
```

Ignore files called `temp.rb` in or below the `/src` directory.
```
git@github.com:*/copilot:
```

In the `copilot` repository of any GitHub organization:
```
  - "/__tests__/**"
```

Ignore any files in or below the `/__tests__` directory.
```
  - "/scripts/*"
```

Ignore any files in the `/scripts` directory.
```
git@gitlab.com:gitlab-org/gitlab-runner.git:
```

In the `gitlab-org/gitlab-runner` repository on GitLab:
```
  - "/main_test.go"
```

Ignore the `/main_test.go` file.
```
  - "{server,session}*"
```

Ignore any files with names beginning with `server` or `session` anywhere in this repository.
```
  - "*.m[dk]"
```

Ignore any files with names ending with `.md` or `.mk` anywhere in this repository.
```
  - "**/package?/*"
```

Ignore files directly within directories such as `packages` or `packaged` anywhere in this repository.
```
  - "**/security/**"
```

Ignore files in or below any `security` directories, anywhere in this repository.
```
# Ignore all `.env` files from all file system roots (Git and non-Git).
# For example, this excludes `REPOSITORY-PATH/.env` and also `/.env`.
# This could also have been written on a single line as:
#
# "*": ["**/.env"]
"*":
  - "**/.env"

# In the `octo-repo` repository in this organization:
octo-repo:
  # Ignore the `/src/some-dir/kernel.rs` file.
  - "/src/some-dir/kernel.rs"

# In the `primer/react` repository on GitHub:
https://github.com/primer/react.git:
  # Ignore files called `secrets.json` anywhere in this repository.
  - "secrets.json"
  # Ignore files called `temp.rb` in or below the `/src` directory.
  - "/src/**/temp.rb"

# In the `copilot` repository of any GitHub organization:
git@github.com:*/copilot:
  # Ignore any files in or below the `/__tests__` directory.
  - "/__tests__/**"
  # Ignore any files in the `/scripts` directory.
  - "/scripts/*"

# In the `gitlab-org/gitlab-runner` repository on GitLab:
git@gitlab.com:gitlab-org/gitlab-runner.git:
  # Ignore the `/main_test.go` file.
  - "/main_test.go"
  # Ignore any files with names beginning with `server` or `session` anywhere in this repository.
  - "{server,session}*"
  # Ignore any files with names ending with `.md` or `.mk` anywhere in this repository.
  - "*.m[dk]"
  # Ignore files directly within directories such as `packages` or `packaged` anywhere in this repository.
  - "**/package?/*"
  # Ignore files in or below any `security` directories, anywhere in this repository.
  - "**/security/**"

```

## [Testing changes to content exclusions](https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion/excluding-content-from-github-copilot#testing-changes-to-content-exclusions)
You can use your IDE to confirm that your changes to content exclusions are working as expected.
### [Propagate content exclusion changes to your IDE](https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion/excluding-content-from-github-copilot#propagate-content-exclusion-changes-to-your-ide)
After you add or change content exclusions, it can take up to 30 minutes to take effect in IDEs where the settings are already loaded. If you don't want to wait, you can manually reload the content exclusion settings using the following instructions.
  * **For JetBrains IDEs and Visual Studio** , reload the content exclusion settings by closing and reopening the application.
  * **For Visual Studio Code** , use the following steps to reload the content exclusion settings: 
    1. Access the Command Palette. For example, by pressing `Shift`+`Command`+`P` (Mac) / `Ctrl`+`Shift`+`P` (Windows/Linux).
    2. Type: `reload`.
    3. Select **Developer: Reload Window**.
  * **For Vim/Neovim** , content exclusions are automatically fetched from GitHub each time you open a file.


### [Test your content exclusions](https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion/excluding-content-from-github-copilot#test-your-content-exclusions)
There are a few different ways to test your content exclusions, depending on which IDE you're using.
  1. Open a file that you expect to be affected by your content exclusions.
  2. Use one or more of the following techniques to test if content is being excluded: 
     * **In JetBrains IDEs, Visual Studio, and Visual Studio Code** , check the Copilot icon in the status bar. If a Copilot content exclusion applies to the file, the Copilot icon will have a diagonal line through it. Hover over the icon to see whether an organization or the parent repository disabled Copilot for the file.
     * **In Vim/Neovim** , begin typing in the file. If GitHub Copilot no longer provides inline suggestions as you type, the file is excluded.
     * You can also test content exclusions in Copilot Chat. Open the Copilot Chat window, and ask Copilot Chat a question about the excluded file. If your content is excluded successfully, Copilot will be unable to answer your question, and will explain that some files were excluded from the conversation due to content exclusion rules.


## [Further reading](https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion/excluding-content-from-github-copilot#further-reading)
  * [Reviewing changes to content exclusions for GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-access-to-github-copilot-in-your-organization/reviewing-changes-to-content-exclusions-for-github-copilot)
  * [Configuring content exclusion for Visual Studio](https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-github-copilot-admin?view=vs-2022#configure-content-exclusion) in the Microsoft Learn documentation


