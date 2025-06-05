  * [Get started](https://docs.github.com/en/get-started "Get started")/
  * [Using Git](https://docs.github.com/en/get-started/using-git "Using Git")/
  * [Push commits to a remote](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository "Push commits to a remote")


# Pushing commits to a remote repository
Use `git push` to push commits made on your local branch to a remote repository.
## In this article
  * [About git push](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository#about-git-push)
  * [Renaming branches](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository#renaming-branches)
  * [Dealing with "non-fast-forward" errors](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository#dealing-with-non-fast-forward-errors)
  * [Resolving blocked commits](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository#resolving-blocked-commits)
  * [Pushing tags](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository#pushing-tags)
  * [Deleting a remote branch or tag](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository#deleting-a-remote-branch-or-tag)
  * [Remotes and forks](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository#remotes-and-forks)
  * [Further reading](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository#further-reading)


## [About `git push`](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository#about-git-push)
The `git push` command takes two arguments:
  * A remote name, for example, `origin`
  * A branch name, for example, `main`


For example:
```
git push REMOTE-NAME BRANCH-NAME

```

As an example, you usually run `git push origin main` to push your local changes to your online repository.
## [Renaming branches](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository#renaming-branches)
To rename a branch, you'd use the same `git push` command, but you would add one more argument: the name of the new branch. For example:
```
git push REMOTE-NAME LOCAL-BRANCH-NAME:REMOTE-BRANCH-NAME

```

This pushes the `LOCAL-BRANCH-NAME` to your `REMOTE-NAME`, but it is renamed to `REMOTE-BRANCH-NAME`.
## [Dealing with "non-fast-forward" errors](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository#dealing-with-non-fast-forward-errors)
If your local copy of a repository is out of sync with, or "behind," the upstream repository you're pushing to, you'll get a message saying `non-fast-forward updates were rejected`. This means that you must retrieve, or "fetch," the upstream changes, before you are able to push your local changes.
For more information on this error, see [Dealing with non-fast-forward errors](https://docs.github.com/en/get-started/using-git/dealing-with-non-fast-forward-errors).
## [Resolving blocked commits](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository#resolving-blocked-commits)
To maintain the security of the repository you're pushing to, GitHub's push protection automatically protects you from accidentally committing secrets to public repositories on GitHub.com. Exposed secrets can pose serious security risks to your repository and your supply chain. If GitHub detects that the commit you're attempting to push contains a supported secret, it blocks the push. In order to resolve the block, you should either:
  * **Remove the secret** from your commit(s). For more information, see [Resolving a blocked push](https://docs.github.com/en/code-security/secret-scanning/working-with-secret-scanning-and-push-protection/working-with-push-protection-from-the-command-line#resolving-a-blocked-push).
  * **Follow the provided URL** to see options to allow the push. For more information, see [Bypassing push protection](https://docs.github.com/en/code-security/secret-scanning/working-with-secret-scanning-and-push-protection/working-with-push-protection-from-the-command-line#bypassing-push-protection)


To learn more about push protection, see [Push protection for users](https://docs.github.com/en/code-security/secret-scanning/working-with-secret-scanning-and-push-protection/push-protection-for-users).
## [Pushing tags](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository#pushing-tags)
By default, and without additional parameters, `git push` sends all matching branches that have the same names as remote branches.
To push a single tag, you can issue the same command as pushing a branch:
```
git push REMOTE-NAME TAG-NAME

```

To push all your tags, you can type the command:
```
git push REMOTE-NAME --tags

```

## [Deleting a remote branch or tag](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository#deleting-a-remote-branch-or-tag)
The syntax to delete a branch is a bit arcane at first glance:
```
git push REMOTE-NAME :BRANCH-NAME

```

Note that there is a space before the colon. The command resembles the same steps you'd take to rename a branch. However, here, you're telling Git to push _nothing_ into `BRANCH-NAME` on `REMOTE-NAME`. Because of this, `git push` deletes the branch on the remote repository.
## [Remotes and forks](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository#remotes-and-forks)
You might already know that [you can "fork" repositories](https://guides.github.com/overviews/forking/) on GitHub.
When you clone a repository you own, you provide it with a remote URL that tells Git where to fetch and push updates. If you want to collaborate with the original repository, you'd add a new remote URL, typically called `upstream`, to your local Git clone:
```
git remote add upstream THEIR_REMOTE_URL

```

Now, you can fetch updates and branches from _their_ fork:
```
git fetch upstream
# Grab the upstream remote's branches
> remote: Counting objects: 75, done.
> remote: Compressing objects: 100% (53/53), done.
> remote: Total 62 (delta 27), reused 44 (delta 9)
> Unpacking objects: 100% (62/62), done.
> From https://github.com/OCTOCAT/REPO
>  * [new branch]      main     -> upstream/main

```

When you're done making local changes, you can push your local branch to GitHub and [initiate a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).
For more information on working with forks, see [Syncing a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork).
## [Further reading](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository#further-reading)
  * [The "Remotes" chapter from the "Pro Git" book](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)
  * [`git remote` main page](https://git-scm.com/docs/git-remote.html)
  * [Git cheatsheet](https://docs.github.com/en/get-started/git-basics/git-cheatsheet)
  * [Git workflows](https://docs.github.com/en/get-started/git-basics/git-workflows)
  * [Git Handbook](https://guides.github.com/introduction/git-handbook/)
  * [Troubleshooting the 2 GB push limit](https://docs.github.com/en/get-started/using-git/troubleshooting-the-2-gb-push-limit)


