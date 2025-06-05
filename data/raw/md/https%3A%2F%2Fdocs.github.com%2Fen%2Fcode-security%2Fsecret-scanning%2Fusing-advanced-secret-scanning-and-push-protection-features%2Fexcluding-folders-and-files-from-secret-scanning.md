  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secret scanning](https://docs.github.com/en/code-security/secret-scanning "Secret scanning")/
  * [Advanced features](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features "Advanced features")/
  * [Exclude folders and files](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/excluding-folders-and-files-from-secret-scanning "Exclude folders and files")


# Excluding folders and files from secret scanning
You can customize secret scanning to automatically close alerts for secrets found in specific directories or files by configuring a `secret_scanning.yml` file in your repository.
## Who can use this feature?
Repository owners, organization owners, security managers, and users with the **admin** role
## In this article
  * [About secret scanning](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/excluding-folders-and-files-from-secret-scanning#about-secret-scanning)
  * [About excluding directories from secret scanning alerts for users](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/excluding-folders-and-files-from-secret-scanning#about-excluding-directories-from-secret-scanning-alerts-for-users)
  * [Excluding directories from secret scanning alerts for users](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/excluding-folders-and-files-from-secret-scanning#excluding-directories-from-secret-scanning-alerts-for-users)
  * [Verifying that the folder is excluded from secret scanning](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/excluding-folders-and-files-from-secret-scanning#verifying-that-the-folder-is-excluded-from-secret-scanning)
  * [Best practices](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/excluding-folders-and-files-from-secret-scanning#best-practices)


## [About secret scanning](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/excluding-folders-and-files-from-secret-scanning#about-secret-scanning)
Secret scanning automatically detects tokens or credentials that have been checked into a repository. You can view secret scanning alerts for users for any secrets that GitHub finds in your code, in the **Security** tab of the repository, so that you know which tokens or credentials to treat as compromised.For more information, see [About secret scanning alerts](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/about-alerts#about-user-alerts).
## [About excluding directories from secret scanning alerts for users](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/excluding-folders-and-files-from-secret-scanning#about-excluding-directories-from-secret-scanning-alerts-for-users)
You may have a reason to commit a secret to a repository, such as when you want to provide a fake secret in documentation, or in an example application. In these scenarios, you can quickly dismiss the alert and document the reasons. However, there may be cases where you want to ignore a directory entirely to avoid creating false positive alerts at scale. For example, you might have a monolithic application with several integrations containing a file of dummy keys that could set off numerous false alerts to triage.
You can configure a `secret_scanning.yml` file to automatically close alerts found in specific directories from secret scanning, and exclude these directories included in push protection. These alerts are closed as "ignored by configuration".
## [Excluding directories from secret scanning alerts for users](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/excluding-folders-and-files-from-secret-scanning#excluding-directories-from-secret-scanning-alerts-for-users)
  1. On GitHub, navigate to the main page of the repository.
  2. Above the list of files, select the **Add file**
Alternatively, you can click 
![Screenshot of the main page of a repository highlighting both the "Add file" and the "plus sign" icon, described above, with an orange outline.](https://docs.github.com/assets/cb-60263/images/help/repository/add-file-buttons.png)
  3. In the file name field, enter ".github/secret_scanning.yml".
  4. Under **Edit new file** , type `paths-ignore:` followed by the paths you want to exclude from secret scanning.
YAML```
paths-ignore:
  - "docs/**"

```
```
paths-ignore:
  - "docs/**"

```

This tells secret scanning to automatically close alerts for everything in the `docs` directory. You can use this example file as a template to add the files and folders you’d like to exclude from your own repositories.
You can also use special characters, such as `*` to filter paths. For more information about filter patterns, see [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions#filter-pattern-cheat-sheet).
YAML```
paths-ignore:
  - "foo/bar/*.js"

```
```
paths-ignore:
  - "foo/bar/*.js"

```

     * If there are more than 1,000 entries in `paths-ignore`, secret scanning will only exclude the first 1,000 directories from scans.
     * If `secret_scanning.yml` is larger than 1 MB, secret scanning will ignore the entire file.


## [Verifying that the folder is excluded from secret scanning](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/excluding-folders-and-files-from-secret-scanning#verifying-that-the-folder-is-excluded-from-secret-scanning)
  1. Open a file in a directory that you have excluded from secret scanning
  2. Paste a pre-invalidated secret, or a test secret.
  3. Commit the change.
  4. On GitHub, navigate to the main page of the repository.
  5. Under the repository name, click **Security**. 
![Screenshot of a repository header showing the tabs. The "Security" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-17801/images/help/repository/security-tab.png)
There should be no new open alerts for the secret you just introduced into the file.


## [Best practices](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/excluding-folders-and-files-from-secret-scanning#best-practices)
Best practices include:
  * Minimizing the number of directories excluded and being as precise as possible when defining exclusions. This ensures that the instructions are as clear as possible, and that exclusions work as intended.
  * Explaining why a particular file or folder is excluded in a comment in the `secret_scanning.yml` file. As with regular code, using comments clarifies your intention, making it easier for others to understand the desired behavior.
  * Reviewing the `secret_scanning.yml` file on a regular basis. Some exclusions may no longer apply with time, and it is good practice to keep the file clean and current. The use of comments, as advised above, can help with this.
  * Informing the security team what files and folders you've excluded, and why. Good communication is vital in ensuring that everyone is on the same page, and understands why specific folders or files are excluded.


