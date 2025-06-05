  * [Get started](https://docs.github.com/en/get-started "Get started")/
  * [Using Git](https://docs.github.com/en/get-started/using-git "Using Git")/
  * [Splitting a subfolder](https://docs.github.com/en/get-started/using-git/splitting-a-subfolder-out-into-a-new-repository "Splitting a subfolder")


# Splitting a subfolder out into a new repository
You can turn a folder within a Git repository into a brand new repository.
## Platform navigation
  * [Mac](https://docs.github.com/en/get-started/using-git/splitting-a-subfolder-out-into-a-new-repository?platform=mac)
  * [Windows](https://docs.github.com/en/get-started/using-git/splitting-a-subfolder-out-into-a-new-repository?platform=windows)
  * [Linux](https://docs.github.com/en/get-started/using-git/splitting-a-subfolder-out-into-a-new-repository?platform=linux)


You need Git version 2.22.0 or later to follow these instructions, otherwise `git filter-repo` will not work.
If you create a new clone of the repository, you won't lose any of your Git history or changes when you split a folder into a separate repository. However, note that the new repository won't have the branches and tags of the original repository.
  1. Open TerminalTerminalGit Bash.
  2. Change the current working directory to the location where you want to create your new repository.
  3. Clone the repository that contains the subfolder.
```
git clone https://github.com/USERNAME/REPOSITORY-NAME

```

  4. Change the current working directory to your cloned repository.
```
cd REPOSITORY-NAME

```

  5. To filter out the subfolder from the rest of the files in the repository, install [`git-filter-repo`](https://github.com/newren/git-filter-repo), then run `git filter-repo` with the following arguments.
     * `FOLDER-NAME`: The folder within your project where you'd like to create a separate repository.
Windows users should use `/` to delimit folders.
```
$ git filter-repo --path FOLDER-NAME/
# Filter the specified branch in your directory and remove empty commits

```

The repository should now only contain the files that were in your subfolder(s).
If you want one specific subfolder to be the new root folder of the new repository, you can use the following command:
```
$ git filter-repo --subdirectory-filter FOLDER-NAME
# Filter the specific branch by using a single sub-directory as the root for the new repository

```

  6. [Create a new repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository) on GitHub.
  7. At the top of your new repository on GitHub's Quick Setup page, click 
![Screenshot of the "Quick Setup" header in a repository. Next to the remote URL, an icon of two overlapping squares is outlined in orange.](https://docs.github.com/assets/cb-48146/images/help/repository/copy-remote-repository-url-quick-setup.png)
For information on the difference between HTTPS and SSH URLs, see [About remote repositories](https://docs.github.com/en/get-started/git-basics/about-remote-repositories).
  8. Add a new remote name with the URL you copied for your repository. For example, `origin` or `upstream` are two common choices.
```
git remote add origin https://github.com/USERNAME/REPOSITORY-NAME.git

```

  9. Verify that the remote URL was added with your new repository name.
```
$ git remote -v
# Verify new remote URL
> origin  https://github.com/USERNAME/NEW-REPOSITORY-NAME.git (fetch)
> origin  https://github.com/USERNAME/NEW-REPOSITORY-NAME.git (push)

```

  10. Push your changes to the new repository on GitHub.
```
git push -u origin BRANCH-NAME

```



