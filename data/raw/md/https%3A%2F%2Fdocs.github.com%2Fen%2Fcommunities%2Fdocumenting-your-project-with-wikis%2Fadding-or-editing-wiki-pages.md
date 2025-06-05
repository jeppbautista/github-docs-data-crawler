  * [Building communities](https://docs.github.com/en/communities "Building communities")/
  * [Using wikis](https://docs.github.com/en/communities/documenting-your-project-with-wikis "Using wikis")/
  * [Manage wiki pages](https://docs.github.com/en/communities/documenting-your-project-with-wikis/adding-or-editing-wiki-pages "Manage wiki pages")


# Adding or editing wiki pages
You can add and edit wiki pages directly on GitHub or locally using the command line.
## Who can use this feature?
Wikis are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud and GitHub Enterprise Server. For more information, see [GitHub’s plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans).
## In this article
  * [Adding wiki pages](https://docs.github.com/en/communities/documenting-your-project-with-wikis/adding-or-editing-wiki-pages#adding-wiki-pages)
  * [Editing wiki pages](https://docs.github.com/en/communities/documenting-your-project-with-wikis/adding-or-editing-wiki-pages#editing-wiki-pages)
  * [Adding or editing wiki pages locally](https://docs.github.com/en/communities/documenting-your-project-with-wikis/adding-or-editing-wiki-pages#adding-or-editing-wiki-pages-locally)
  * [About wiki filenames](https://docs.github.com/en/communities/documenting-your-project-with-wikis/adding-or-editing-wiki-pages#about-wiki-filenames)


## [Adding wiki pages](https://docs.github.com/en/communities/documenting-your-project-with-wikis/adding-or-editing-wiki-pages#adding-wiki-pages)
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the menu in a repository. The "Wiki" option is outlined in dark orange.](https://docs.github.com/assets/cb-50193/images/help/wiki/wiki-menu-link.png)
  3. In the upper-right corner of the page, click **New Page**.
  4. Optionally, to write in a format other than Markdown, use the "Edit mode" dropdown to choose a different format.
![Screenshot of the "Create new page" page. The "Edit mode" dropdown is outlined in dark orange.](https://docs.github.com/assets/cb-109248/images/help/wiki/wiki-edit-mode-dropdown.png)
  5. Use the text editor to add your page's content.
  6. In the "Edit message" field, type a commit message describing the new file you’re adding.
  7. To commit your changes to the wiki, click **Save Page**.


## [Editing wiki pages](https://docs.github.com/en/communities/documenting-your-project-with-wikis/adding-or-editing-wiki-pages#editing-wiki-pages)
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the menu in a repository. The "Wiki" option is outlined in dark orange.](https://docs.github.com/assets/cb-50193/images/help/wiki/wiki-menu-link.png)
  3. Using the wiki sidebar on the right, navigate to the page you want to change. In the upper-right corner of the page, click **Edit**.
  4. Use the text editor to edit the page's content.
  5. In the "Edit message" field, type a commit message describing the new file you’re adding.
  6. To commit your changes to the wiki, click **Save Page**.


## [Adding or editing wiki pages locally](https://docs.github.com/en/communities/documenting-your-project-with-wikis/adding-or-editing-wiki-pages#adding-or-editing-wiki-pages-locally)
Wikis are part of Git repositories, so you can make changes locally and push them to your repository using a Git workflow.
### [Cloning wikis to your computer](https://docs.github.com/en/communities/documenting-your-project-with-wikis/adding-or-editing-wiki-pages#cloning-wikis-to-your-computer)
Every wiki provides an easy way to clone its contents down to your computer. Once you've created an initial page on GitHub, you can clone the repository to your computer with the provided URL:
```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.wiki.git
# Clones the wiki locally

```

Once you have cloned the wiki, you can add new files, edit existing ones, and commit your changes. You and your collaborators can create branches when working on wikis, but only changes pushed to the default branch will be made live and available to your readers.
## [About wiki filenames](https://docs.github.com/en/communities/documenting-your-project-with-wikis/adding-or-editing-wiki-pages#about-wiki-filenames)
The filename determines the title of your wiki page, and the file extension determines how your wiki content is rendered.
Wikis use [our open-source Markup library](https://github.com/github/markup) to convert the markup, and it determines which converter to use by a file's extension. For example, if you name a file _foo.md_ or _foo.markdown_ , wiki will use the Markdown converter, while a file named _foo.textile_ will use the Textile converter.
Don't use the following characters in your wiki page's titles: `\ / : * ? " < > |`. Users on certain operating systems won't be able to work with filenames containing these characters. Be sure to write your content using a markup language that matches the extension, or your content won't render properly.
