  * [Get started](https://docs.github.com/en/get-started "Get started")/
  * [Git basics](https://docs.github.com/en/get-started/git-basics "Git basics")/
  * [Caching credentials](https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git "Caching credentials")


# Caching your GitHub credentials in Git
If you're [cloning GitHub repositories using HTTPS](https://docs.github.com/en/github/getting-started-with-github/about-remote-repositories), we recommend you use GitHub CLI or Git Credential Manager (GCM) to remember your credentials.
## Platform navigation
  * [Mac](https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git?platform=mac)
  * [Windows](https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git?platform=windows)
  * [Linux](https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git?platform=linux)


## In this article
  * [GitHub CLI](https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git#github-cli)
  * [Git Credential Manager](https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git#git-credential-manager)


If you clone GitHub repositories using SSH, then you can authenticate using an SSH key instead of using other credentials. For information about setting up an SSH connection, see [Connecting to GitHub with SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).
## [GitHub CLI](https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git#github-cli)
GitHub CLI will automatically store your Git credentials for you when you choose `HTTPS` as your preferred protocol for Git operations and answer "yes" to the prompt asking if you would like to authenticate to Git with your GitHub credentials.
  1. [Install](https://github.com/cli/cli#installation) GitHub CLI on macOS, Windows, or Linux.
  2. In the command line, enter `gh auth login`, then follow the prompts. 
     * When prompted for your preferred protocol for Git operations, select `HTTPS`.
     * When asked if you would like to authenticate to Git with your GitHub credentials, enter `Y`.


For more information about authenticating with GitHub CLI, see [`gh auth login`](https://cli.github.com/manual/gh_auth_login).
## [Git Credential Manager](https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git#git-credential-manager)
[Git Credential Manager](https://github.com/GitCredentialManager/git-credential-manager) (GCM) is another way to store your credentials securely and connect to GitHub over HTTPS. With GCM, you don't have to manually [create and store a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens), as GCM manages authentication on your behalf, including 2FA (two-factor authentication).
  1. Install Git using [Homebrew](https://brew.sh/):
```
brew install git

```

  2. Install GCM using Homebrew:
```
brew install --cask git-credential-manager

```



For macOS, you don't need to run `git config` because GCM automatically configures Git for you.
The next time you clone an HTTPS URL that requires authentication, Git will prompt you to log in using a browser window. You may first be asked to authorize an OAuth app. If your account or organization requires [two-factor auth](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa), you'll also need to complete the 2FA challenge.
Once you've authenticated successfully, your credentials are stored in the macOS keychain and will be used every time you clone an HTTPS URL. Git will not require you to type your credentials in the command line again unless you change your credentials.
  1. Install Git for Windows, which includes GCM. For more information, see [Git for Windows releases](https://github.com/git-for-windows/git/releases/latest) from its [releases page](https://github.com/git-for-windows/git/releases/latest).


We recommend always installing the latest version. At a minimum, install version 2.29 or higher, which is the first version offering OAuth support for GitHub.
The next time you clone an HTTPS URL that requires authentication, Git will prompt you to log in using a browser window. You may first be asked to authorize an OAuth app. If your account or organization requires [two-factor auth](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa), you'll also need to complete the 2FA challenge.
Once you've authenticated successfully, your credentials are stored in the Windows credential manager and will be used every time you clone an HTTPS URL. Git will not require you to type your credentials in the command line again unless you change your credentials.
  

Older versions of Git for Windows came with Git Credential Manager for Windows. This older product is no longer supported and cannot connect to GitHub via OAuth. We recommend you upgrade to [the latest version of Git for Windows](https://github.com/git-for-windows/git/releases/latest).
If you cached incorrect or outdated credentials in Credential Manager for Windows, Git will fail to access GitHub. To reset your cached credentials so that Git prompts you to enter your credentials, access the Credential Manager in the Windows Control Panel under User Accounts > Credential Manager. Look for the GitHub entry and delete it.
For Linux, install Git and GCM, then configure Git to use GCM.
  1. Install Git from your distro's packaging system. Instructions will vary depending on the flavor of Linux you run.
  2. Install GCM. See the [instructions in the GCM repo](https://github.com/git-ecosystem/git-credential-manager/blob/release/docs/install.md), as they'll vary depending on the flavor of Linux you run.
  3. Configure Git to use GCM. There are several backing stores that you may choose from, so see the GCM docs to complete your setup. For more information, see [GCM Linux](https://aka.ms/gcmcore-linuxcredstores).


The next time you clone an HTTPS URL that requires authentication, Git will prompt you to log in using a browser window. You may first be asked to authorize an OAuth app. If your account or organization requires [two-factor auth](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa), you'll also need to complete the 2FA challenge.
Once you've authenticated successfully, your credentials are stored on your system and will be used every time you clone an HTTPS URL. Git will not require you to type your credentials in the command line again unless you change your credentials.
For more options for storing your credentials on Linux, see [Credential Storage](https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage) in Pro Git.
  

For more information or to report issues with GCM, see the official GCM docs at [Git Credential Manager](https://github.com/GitCredentialManager/git-credential-manager).
