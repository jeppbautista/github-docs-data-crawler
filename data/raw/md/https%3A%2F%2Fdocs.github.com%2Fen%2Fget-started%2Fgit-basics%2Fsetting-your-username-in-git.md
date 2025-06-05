  * [Get started](https://docs.github.com/en/get-started "Get started")/
  * [Git basics](https://docs.github.com/en/get-started/git-basics "Git basics")/
  * [Set your username](https://docs.github.com/en/get-started/git-basics/setting-your-username-in-git "Set your username")


# Setting your username in Git
Git uses a username to associate commits with an identity. The Git username is not the same as your GitHub username.
## Platform navigation
  * [Mac](https://docs.github.com/en/get-started/git-basics/setting-your-username-in-git?platform=mac)
  * [Windows](https://docs.github.com/en/get-started/git-basics/setting-your-username-in-git?platform=windows)
  * [Linux](https://docs.github.com/en/get-started/git-basics/setting-your-username-in-git?platform=linux)


## In this article
  * [About Git usernames](https://docs.github.com/en/get-started/git-basics/setting-your-username-in-git#about-git-usernames)
  * [Setting your Git username for every repository on your computer](https://docs.github.com/en/get-started/git-basics/setting-your-username-in-git#setting-your-git-username-for-every-repository-on-your-computer)
  * [Setting your Git username for a single repository](https://docs.github.com/en/get-started/git-basics/setting-your-username-in-git#setting-your-git-username-for-a-single-repository)
  * [Further reading](https://docs.github.com/en/get-started/git-basics/setting-your-username-in-git#further-reading)


## [About Git usernames](https://docs.github.com/en/get-started/git-basics/setting-your-username-in-git#about-git-usernames)
You can change the name that is associated with your Git commits using the `git config` command. The new name you set will be visible in any future commits you push to GitHub from the command line. If you'd like to keep your real name private, you can use any text as your Git username.
Changing the name associated with your Git commits using `git config` will only affect future commits and will not change the name used for past commits.
## [Setting your Git username for every repository on your computer](https://docs.github.com/en/get-started/git-basics/setting-your-username-in-git#setting-your-git-username-for-every-repository-on-your-computer)
  1. Open TerminalTerminalGit Bash.
  2. Set a Git username:
```
git config --global user.name "Mona Lisa"

```

  3. Confirm that you have set the Git username correctly:
```
$ git config --global user.name
> Mona Lisa

```



## [Setting your Git username for a single repository](https://docs.github.com/en/get-started/git-basics/setting-your-username-in-git#setting-your-git-username-for-a-single-repository)
  1. Open TerminalTerminalGit Bash.
  2. Change the current working directory to the local repository where you want to configure the name that is associated with your Git commits.
  3. Set a Git username:
```
git config user.name "Mona Lisa"

```

  4. Confirm that you have set the Git username correctly:
```
$ git config user.name
> Mona Lisa

```



## [Further reading](https://docs.github.com/en/get-started/git-basics/setting-your-username-in-git#further-reading)
  * [Setting your commit email address](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address)
  * ["Git Configuration" from the _Pro Git_ book](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration)


