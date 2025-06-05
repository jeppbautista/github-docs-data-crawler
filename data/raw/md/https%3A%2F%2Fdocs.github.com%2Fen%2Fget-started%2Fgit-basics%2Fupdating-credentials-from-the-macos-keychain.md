  * [Get started](https://docs.github.com/en/get-started "Get started")/
  * [Git basics](https://docs.github.com/en/get-started/git-basics "Git basics")/
  * [macOS Keychain credentials](https://docs.github.com/en/get-started/git-basics/updating-credentials-from-the-macos-keychain "macOS Keychain credentials")


# Updating credentials from the macOS Keychain
You'll need to update your saved credentials in the `git-credential-osxkeychain` helper if you change your username, password, or personal access token on GitHub.
## In this article
  * [Updating your credentials via Keychain Access](https://docs.github.com/en/get-started/git-basics/updating-credentials-from-the-macos-keychain#updating-your-credentials-via-keychain-access)
  * [Deleting your credentials via the command line](https://docs.github.com/en/get-started/git-basics/updating-credentials-from-the-macos-keychain#deleting-your-credentials-via-the-command-line)
  * [Further reading](https://docs.github.com/en/get-started/git-basics/updating-credentials-from-the-macos-keychain#further-reading)


Updating credentials from the macOS Keychain only applies to users who manually configured a personal access token using the `osxkeychain` helper that is built-in to macOS.
We recommend you either [configure SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) or upgrade to the [Git Credential Manager](https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git) (GCM) instead. GCM can manage authentication on your behalf (no more manual personal access tokens) including 2FA (two-factor auth).
When Git prompts you for your password, enter your personal access token. Alternatively, you can use a credential helper like [Git Credential Manager](https://github.com/GitCredentialManager/git-credential-manager/blob/main/README.md). Password-based authentication for Git has been removed in favor of more secure authentication methods. For more information, see [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).
## [Updating your credentials via Keychain Access](https://docs.github.com/en/get-started/git-basics/updating-credentials-from-the-macos-keychain#updating-your-credentials-via-keychain-access)
  1. Click on the Spotlight icon (magnifying glass) on the right side of the menu bar.
  2. Type `Keychain Access`, then press the Enter key to launch the app.
  3. In Keychain Access, search for `github.com`.
  4. Find the "Internet password" entry for `github.com`.
  5. Edit or delete the entry accordingly.


## [Deleting your credentials via the command line](https://docs.github.com/en/get-started/git-basics/updating-credentials-from-the-macos-keychain#deleting-your-credentials-via-the-command-line)
Through the command line, you can use the credential helper directly to erase the keychain entry.
```
$ git credential-osxkeychain erase
host=github.com
protocol=https
> [Press Return]

```

If it's successful, nothing will print out. To test that it works, try and clone a private repository. If you are prompted for a password, the keychain entry was deleted.
## [Further reading](https://docs.github.com/en/get-started/git-basics/updating-credentials-from-the-macos-keychain#further-reading)
  * [Caching your GitHub credentials in Git](https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git)


