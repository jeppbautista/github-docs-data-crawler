  * [Codespaces](https://docs.github.com/en/codespaces "Codespaces")/
  * [Setting up your project](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces "Setting up your project")/
  * [Setting up your repository](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/setting-up-your-repository "Setting up your repository")/
  * [Facilitating codespace creation](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/setting-up-your-repository/facilitating-quick-creation-and-resumption-of-codespaces "Facilitating codespace creation")


# Facilitating quick creation and resumption of codespaces
You can add a link to take people straight to a page for creating a codespace, with your choice of options preconfigured. Alternatively you can link to the "Resume codespace" page.
## In this article
  * [Overview](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/setting-up-your-repository/facilitating-quick-creation-and-resumption-of-codespaces#overview)
  * [Creating a link to the codespace creation page for your repository](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/setting-up-your-repository/facilitating-quick-creation-and-resumption-of-codespaces#creating-a-link-to-the-codespace-creation-page-for-your-repository)
  * [Creating a link to resume a codespace](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/setting-up-your-repository/facilitating-quick-creation-and-resumption-of-codespaces#creating-a-link-to-resume-a-codespace)
  * [Creating an "Open in GitHub Codespaces" badge](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/setting-up-your-repository/facilitating-quick-creation-and-resumption-of-codespaces#creating-an-open-in-github-codespaces-badge)


## [Overview](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/setting-up-your-repository/facilitating-quick-creation-and-resumption-of-codespaces#overview)
You can make it easy for people to work on your repository in a codespace by providing a link to the codespace creation page. One place you might want to do this is in the README file for your repository. For example, you can add the link to an "Open in GitHub Codespaces" badge.
![Screenshot of an "Open in GitHub Codespaces" badge on a README page.](https://docs.github.com/assets/cb-42880/images/help/codespaces/codespaces-badge-on-readme.png)
The link to the codespace creation page can include specific configuration options to help people create an appropriate codespace. People who use the link will be able to choose different options, if they want, before creating the codespace. For information about the available options, see [Creating a codespace for a repository](https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-for-a-repository#creating-a-codespace-for-a-repository).
Alternatively, you can link to the "Resume codespace" page, which provides a quick way for people to open a codespace they were working on recently.
## [Creating a link to the codespace creation page for your repository](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/setting-up-your-repository/facilitating-quick-creation-and-resumption-of-codespaces#creating-a-link-to-the-codespace-creation-page-for-your-repository)
You can use these URLs to link to the codespace creation page for your repository. Replace the text in uppercase letters.
  * Create a codespace for the default branch of the repository: `https://codespaces.new/OWNER/REPO-NAME`
  * Create a codespace for a specific branch of the repository: `https://codespaces.new/OWNER/REPO-NAME/tree/BRANCH-NAME`
  * Create a codespace for the topic branch of a pull request: `https://codespaces.new/OWNER/REPO-NAME/pull/PR-SHA`


### [Configuring more options](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/setting-up-your-repository/facilitating-quick-creation-and-resumption-of-codespaces#configuring-more-options)
You can use the "Share a deep link" option to configure more options for the codespace and build a custom URL, then copy a Markdown or HTML snippet for an "Open in GitHub Codespaces" badge.
  1. On GitHub, navigate to the main page of the repository.
  2. If you want to create a link for a branch other than the repository's default branch, under the repository name, click the button labeled with the name of the current branch. In the dropdown menu, select the branch for which you want to create a link.
![Screenshot of the branch dropdown menu, listing various branches. The dropdown menu, labeled with a branch icon and "trunk," is outlined in orange.](https://docs.github.com/assets/cb-31088/images/help/codespaces/branch-drop-down.png)
  3. Click the **Codespaces** tab.
  4. To open the "Share codespace configuration" window, at the top right of the **Codespaces** tab, select **Share a deep link**.
![Screenshot of the options dropdown in the "Codespaces" tab. The "Share a deep link" option is highlighted with an orange outline.](https://docs.github.com/assets/cb-59090/images/help/codespaces/share-deep-link.png)
  5. Optionally, to take users to a page where they can quickly resume a recent codespace or create a new one, select **Quick start**. For more information, see [Creating a link to resume a codespace](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/setting-up-your-repository/facilitating-quick-creation-and-resumption-of-codespaces#creating-a-link-to-resume-a-codespace).
  6. Optionally, to specify a dev container configuration, select **Configuration file** , then use the dropdown menu to choose a configuration. If you don't specify a configuration, the default configuration for your repository is used. For more information, see [Introduction to dev containers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers).
  7. Under "Snippets," you can copy the URL you have built, or copy a Markdown or HTML snippet including an "Open in GitHub Codespaces" badge. To copy the URL or snippet, select between the **URL** , **HTML** , and **Markdown** tabs, then click 
![Screenshot of the "Share codespace configuration" window. Next to the "new codespace" URL, an icon of two overlapping squares is outlined in orange.](https://docs.github.com/assets/cb-63665/images/help/codespaces/copy-codespace-url.png)


## [Creating a link to resume a codespace](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/setting-up-your-repository/facilitating-quick-creation-and-resumption-of-codespaces#creating-a-link-to-resume-a-codespace)
You can create a link to a page for resuming your most recent codespace that matches the repository, branch, and other options specified in the URL.
Add `?quickstart=1` to a `codespaces.new` URL, such as the URLs listed in the previous section of this article. This produces a URL that displays a "Resume codespace" page.
For example, the URL `https://codespaces.new/octo-org/octo-repo?quickstart=1` opens a page to allow you to resume your most recent codespace for the default branch of the `octo-org/octo-repo` repository.
![Screenshot of the "Resume codespace" page showing the "Resume this codespace" and "Create a new one" buttons.](https://docs.github.com/assets/cb-63459/images/help/codespaces/resume-codespace.png)
  * If the `codespaces.new` URL already contains a query string, add `&quickstart=1` at the end of the query string.
  * This type of URL will always open a codespace in the VS Code web client, even if this is not set as your default editor for GitHub Codespaces.


If no matching codespaces are found, the page is titled "Create codespace" and a button is displayed for creating a new codespace with matching parameters.
This type of URL is useful, for instance, in a README for your repository as it gives people a way of either creating a codespace, or resuming their codespace, in just a couple of clicks.
## [Creating an "Open in GitHub Codespaces" badge](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/setting-up-your-repository/facilitating-quick-creation-and-resumption-of-codespaces#creating-an-open-in-github-codespaces-badge)
You can use the "Share a deep link" option to create a Markdown or HTML snippet that includes an "Open in GitHub Codespaces" badge with a custom URL. For more information, see [Configuring more options](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/setting-up-your-repository/facilitating-quick-creation-and-resumption-of-codespaces#configuring-more-options).
  1. Get the URL to the codespace creation page, or the "Resume codespace" page, as described in the previous sections.
  2. Add the following Markdown to, for example, the `README.md` file of your repository:
Markdown```
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](URL)

```
```
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](URL)

```

For example:
```
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/github/docs)

```

The example Markdown is rendered like this:
[](https://codespaces.new/github/docs)
[![Open in GitHub Codespaces.](https://github.com/codespaces/badge.svg)](https://codespaces.new/github/docs)


