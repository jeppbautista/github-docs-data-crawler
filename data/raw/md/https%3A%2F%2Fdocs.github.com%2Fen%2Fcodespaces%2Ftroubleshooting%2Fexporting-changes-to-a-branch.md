  * [Codespaces](https://docs.github.com/en/codespaces "Codespaces")/
  * [Troubleshooting](https://docs.github.com/en/codespaces/troubleshooting "Troubleshooting")/
  * [Exporting changes](https://docs.github.com/en/codespaces/troubleshooting/exporting-changes-to-a-branch "Exporting changes")


# Exporting changes to a branch
This article provides steps for exporting your codespace changes to a branch.
## In this article
  * [About exporting changes](https://docs.github.com/en/codespaces/troubleshooting/exporting-changes-to-a-branch#about-exporting-changes)
  * [Exporting changes to a branch](https://docs.github.com/en/codespaces/troubleshooting/exporting-changes-to-a-branch#exporting-changes-to-a-branch)


## [About exporting changes](https://docs.github.com/en/codespaces/troubleshooting/exporting-changes-to-a-branch#about-exporting-changes)
While using GitHub Codespaces, you may want to export your changes to a branch without launching your codespace. This can be useful when you have hit a [spending limit](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-codespaces/managing-the-spending-limit-for-github-codespaces) or have a general issue accessing your codespace.
You can export your changes in one of several ways, depending on how you created the codespace. In every case, only the Git branch that is currently checked out in the codespace is exported. Work contained in other branches is not exported.
  * If you created the codespace from a repository to which you have write access, you can export your changes to a new branch of the repository.
  * If you created the codespace from a repository to which you only have read access, you can export your changes to a fork of the repository. GitHub Codespaces will create a new fork for you, or link your codespace to an existing fork if you already have one for the repository, and export your changes to a new branch of the fork. For more information, see [Using source control in your codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-source-control-in-your-codespace#about-automatic-forking).
  * If you created the codespace from a template, and have not yet published it, you can publish the codespace to a new repository.


GitHub blocks pushes containing files larger than 100 MiB. If your codespace contains large files you will not be able to export your changes to a branch or fork. For more information, see [About large files on GitHub](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).
## [Exporting changes to a branch](https://docs.github.com/en/codespaces/troubleshooting/exporting-changes-to-a-branch#exporting-changes-to-a-branch)
The following steps describe how to export your changes to a branch or fork. For information on exporting an unpublished codespace to a new repository, see [Creating a codespace from a template](https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-from-a-template#publishing-from-githubcom).
  1. In the top-left corner of GitHub, select [github.com/codespaces](https://github.com/codespaces). Or, for an individual repository, click the 
  2. Click the ellipsis (**...**) to the right of the codespace you want to export from.
  3. Select 
![Screenshot of a list of codespaces with the dropdown menu for one of them displayed, showing the "Export changes to a branch" option.](https://docs.github.com/assets/cb-89112/images/help/codespaces/export-changes-to-a-branch.png)
  4. In the dialog box, click **Create branch** or **Create fork**.


The name of the new branch will be the permanent name of your codespace prefixed by the string `codespace-`, for example `codespace-ideal-space-engine-w5vg5ww5p793g7g9`.
