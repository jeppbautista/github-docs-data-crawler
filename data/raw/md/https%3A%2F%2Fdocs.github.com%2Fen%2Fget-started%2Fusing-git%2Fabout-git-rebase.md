  * [Get started](https://docs.github.com/en/get-started "Get started")/
  * [Using Git](https://docs.github.com/en/get-started/using-git "Using Git")/
  * [About Git rebase](https://docs.github.com/en/get-started/using-git/about-git-rebase "About Git rebase")


# About Git rebase
The `git rebase` command allows you to easily change a series of commits, modifying the history of your repository. You can reorder, edit, or squash commits together.
## In this article
  * [Rebasing commits against a branch](https://docs.github.com/en/get-started/using-git/about-git-rebase#rebasing-commits-against-a-branch)
  * [Rebasing commits against a point in time](https://docs.github.com/en/get-started/using-git/about-git-rebase#rebasing-commits-against-a-point-in-time)
  * [Commands available while rebasing](https://docs.github.com/en/get-started/using-git/about-git-rebase#commands-available-while-rebasing)
  * [An example of using git rebase](https://docs.github.com/en/get-started/using-git/about-git-rebase#an-example-of-using-git-rebase)
  * [Further reading](https://docs.github.com/en/get-started/using-git/about-git-rebase#further-reading)


Typically, you would use `git rebase` to:
  * Edit previous commit messages
  * Combine multiple commits into one
  * Delete or revert commits that are no longer necessary


Because changing your commit history can make things difficult for everyone else using the repository, it's considered bad practice to rebase commits when you've already pushed to a repository. To learn how to safely rebase, see [About pull request merges](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges).
## [Rebasing commits against a branch](https://docs.github.com/en/get-started/using-git/about-git-rebase#rebasing-commits-against-a-branch)
To rebase all the commits between another branch and the current branch state, you can enter the following command in your shell (either the command prompt for Windows, or the terminal for Mac and Linux):
```
git rebase --interactive OTHER-BRANCH-NAME

```

## [Rebasing commits against a point in time](https://docs.github.com/en/get-started/using-git/about-git-rebase#rebasing-commits-against-a-point-in-time)
To rebase the last few commits in your current branch, you can enter the following command in your shell:
```
git rebase --interactive HEAD~7

```

## [Commands available while rebasing](https://docs.github.com/en/get-started/using-git/about-git-rebase#commands-available-while-rebasing)
There are six commands available while rebasing: 

`pick`
     `pick` simply means that the commit is included. Rearranging the order of the `pick` commands changes the order of the commits when the rebase is underway. If you choose not to include a commit, you should delete the entire line.  

`reword`
    The `reword` command is similar to `pick`, but after you use it, the rebase process will pause and give you a chance to alter the commit message. Any changes made by the commit are not affected.  

`edit`
    If you choose to `edit` a commit, you'll be given the chance to amend the commit, meaning that you can add or change the commit entirely. You can also make more commits before you continue the rebase. This allows you to split a large commit into smaller ones, or, remove erroneous changes made in a commit.  

`squash`
    This command lets you combine two or more commits into a single commit. A commit is squashed into the commit above it. Git gives you the chance to write a new commit message describing both changes. 

`fixup`
    This is similar to `squash`, but the commit to be merged has its message discarded. The commit is simply merged into the commit above it, and the earlier commit's message is used to describe both changes. 

`exec`
    This lets you run arbitrary shell commands against a commit.
## [An example of using `git rebase`](https://docs.github.com/en/get-started/using-git/about-git-rebase#an-example-of-using-git-rebase)
No matter which command you use, Git will launch [your default text editor](https://docs.github.com/en/get-started/git-basics/associating-text-editors-with-git) and open a file that details the commits in the range you've chosen. That file looks something like this:
```
pick 1fc6c95 Patch A
pick 6b2481b Patch B
pick dd1475d something I want to split
pick c619268 A fix for Patch B
pick fa39187 something to add to patch A
pick 4ca2acc i cant' typ goods
pick 7b36971 something to move before patch B

# Rebase 41a72e6..7b36971 onto 41a72e6
#
# Commands:
#  p, pick = use commit
#  r, reword = use commit, but edit the commit message
#  e, edit = use commit, but stop for amending
#  s, squash = use commit, but meld into previous commit
#  f, fixup = like "squash", but discard this commit's log message
#  x, exec = run command (the rest of the line) using shell
#
# If you remove a line here THAT COMMIT WILL BE LOST.
# However, if you remove everything, the rebase will be aborted.
#

```

Breaking this information, from top to bottom, we see that:
  * Seven commits are listed, which indicates that there were seven changes between our starting point and our current branch state.
  * The commits you chose to rebase are sorted in the order of the oldest changes (at the top) to the newest changes (at the bottom).
  * Each line lists a command (by default, `pick`), the commit SHA, and the commit message. The entire `git rebase` procedure centers around your manipulation of these three columns. The changes you make are _rebased_ onto your repository.
  * After the commits, Git tells you the range of commits we're working with (`41a72e6..7b36971`).
  * Finally, Git gives some help by telling you the commands that are available to you when rebasing commits.


## [Further reading](https://docs.github.com/en/get-started/using-git/about-git-rebase#further-reading)
  * [Using Git rebase on the command line](https://docs.github.com/en/get-started/using-git/using-git-rebase-on-the-command-line)
  * [The "Git Branching" chapter from the _Pro Git_ book](https://git-scm.com/book/en/v2/Git-Branching-Rebasing)
  * [The "Interactive Rebasing" chapter from the _Pro Git_ book](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History#_changing_multiple)
  * [Squashing commits with rebase](http://gitready.com/advanced/2009/02/10/squashing-commits-with-rebase.html)
  * [Syncing your branch in GitHub Desktop](https://docs.github.com/en/desktop/working-with-your-remote-repository-on-github-or-github-enterprise/syncing-your-branch-in-github-desktop) in the GitHub Desktop documentation


