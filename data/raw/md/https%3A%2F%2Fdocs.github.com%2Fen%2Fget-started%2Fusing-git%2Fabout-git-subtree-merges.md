  * [Get started](https://docs.github.com/en/get-started "Get started")/
  * [Using Git](https://docs.github.com/en/get-started/using-git "Using Git")/
  * [About Git subtree merges](https://docs.github.com/en/get-started/using-git/about-git-subtree-merges "About Git subtree merges")


# About Git subtree merges
If you need to manage multiple projects within a single repository, you can use a _subtree merge_ to handle all the references.
## Platform navigation
  * [Mac](https://docs.github.com/en/get-started/using-git/about-git-subtree-merges?platform=mac)
  * [Windows](https://docs.github.com/en/get-started/using-git/about-git-subtree-merges?platform=windows)
  * [Linux](https://docs.github.com/en/get-started/using-git/about-git-subtree-merges?platform=linux)


## In this article
  * [About subtree merges](https://docs.github.com/en/get-started/using-git/about-git-subtree-merges#about-subtree-merges)
  * [Setting up the empty repository for a subtree merge](https://docs.github.com/en/get-started/using-git/about-git-subtree-merges#setting-up-the-empty-repository-for-a-subtree-merge)
  * [Adding a new repository as a subtree](https://docs.github.com/en/get-started/using-git/about-git-subtree-merges#adding-a-new-repository-as-a-subtree)
  * [Synchronizing with updates and changes](https://docs.github.com/en/get-started/using-git/about-git-subtree-merges#synchronizing-with-updates-and-changes)
  * [Further reading](https://docs.github.com/en/get-started/using-git/about-git-subtree-merges#further-reading)


## [About subtree merges](https://docs.github.com/en/get-started/using-git/about-git-subtree-merges#about-subtree-merges)
Typically, a subtree merge is used to contain a repository within a repository. The "subrepository" is stored in a folder of the main repository.
The best way to explain subtree merges is to show by example. We will:
  * Make an empty repository called `test` that represents our project.
  * Merge another repository into it as a subtree called `Spoon-Knife`.
  * The `test` project will use that subproject as if it were part of the same repository.
  * Fetch updates from `Spoon-Knife` into our `test` project.


## [Setting up the empty repository for a subtree merge](https://docs.github.com/en/get-started/using-git/about-git-subtree-merges#setting-up-the-empty-repository-for-a-subtree-merge)
  1. Open TerminalTerminalGit Bash.
  2. Create a new directory and navigate to it.
```
mkdir test
cd test

```

  3. Initialize a new Git repository.
```
$ git init
> Initialized empty Git repository in /Users/octocat/tmp/test/.git/

```

  4. Create and commit a new file.
```
$ touch .gitignore
$ git add .gitignore
$ git commit -m "initial commit"
> [main (root-commit) 3146c2a] initial commit
>  0 files changed, 0 insertions(+), 0 deletions(-)
>  create mode 100644 .gitignore

```



## [Adding a new repository as a subtree](https://docs.github.com/en/get-started/using-git/about-git-subtree-merges#adding-a-new-repository-as-a-subtree)
  1. Add a new remote URL pointing to the separate project that we're interested in.
```
$ git remote add -f spoon-knife https://github.com/octocat/Spoon-Knife.git
> Updating spoon-knife
> warning: no common commits
> remote: Counting objects: 1732, done.
> remote: Compressing objects: 100% (750/750), done.
> remote: Total 1732 (delta 1086), reused 1558 (delta 967)
> Receiving objects: 100% (1732/1732), 528.19 KiB | 621 KiB/s, done.
> Resolving deltas: 100% (1086/1086), done.
> From https://github.com/octocat/Spoon-Knife
>  * [new branch]      main     -> Spoon-Knife/main

```

  2. Merge the `Spoon-Knife` project into the local Git project. This doesn't change any of your files locally, but it does prepare Git for the next step.
If you're using Git 2.9 or above:
```
$ git merge -s ours --no-commit --allow-unrelated-histories spoon-knife/main
> Automatic merge went well; stopped before committing as requested

```

If you're using Git 2.8 or below:
```
$ git merge -s ours --no-commit spoon-knife/main
> Automatic merge went well; stopped before committing as requested

```

  3. Create a new directory called **spoon-knife** , and copy the Git history of the `Spoon-Knife` project into it.
```
$ git read-tree --prefix=spoon-knife/ -u spoon-knife/main
> fatal: refusing to merge unrelated histories

```

  4. Commit the changes to keep them safe.
```
$ git commit -m "Subtree merged in spoon-knife"
> [main fe0ca25] Subtree merged in spoon-knife

```



Although we've only added one subproject, any number of subprojects can be incorporated into a Git repository.
If you create a fresh clone of the repository in the future, the remotes you've added will not be created for you. You will have to add them again using [the `git remote add` command](https://docs.github.com/en/get-started/git-basics/managing-remote-repositories).
## [Synchronizing with updates and changes](https://docs.github.com/en/get-started/using-git/about-git-subtree-merges#synchronizing-with-updates-and-changes)
When a subproject is added, it is not automatically kept in sync with the upstream changes. You will need to update the subproject with the following command:
```
git pull -s subtree REMOTE-NAME BRANCH-NAME

```

For the example above, this would be:
```
git pull -s subtree spoon-knife main

```

## [Further reading](https://docs.github.com/en/get-started/using-git/about-git-subtree-merges#further-reading)
  * [The "Advanced Merging" chapter from the _Pro Git_ book](https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging)
  * [How to use the subtree merge strategy](https://www.kernel.org/pub/software/scm/git/docs/howto/using-merge-subtree.html)


