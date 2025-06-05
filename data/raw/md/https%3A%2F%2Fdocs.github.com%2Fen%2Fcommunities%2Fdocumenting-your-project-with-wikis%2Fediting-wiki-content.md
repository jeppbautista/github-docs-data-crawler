  * [Building communities](https://docs.github.com/en/communities "Building communities")/
  * [Using wikis](https://docs.github.com/en/communities/documenting-your-project-with-wikis "Using wikis")/
  * [Editing wiki content](https://docs.github.com/en/communities/documenting-your-project-with-wikis/editing-wiki-content "Editing wiki content")


# Editing wiki content
You can add images and links to content in your wiki, and use some supported MediaWiki formats.
## Who can use this feature?
Wikis are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud and GitHub Enterprise Server. For more information, see [GitHub’s plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans).
## In this article
  * [Adding links](https://docs.github.com/en/communities/documenting-your-project-with-wikis/editing-wiki-content#adding-links)
  * [Adding images](https://docs.github.com/en/communities/documenting-your-project-with-wikis/editing-wiki-content#adding-images)
  * [Adding mathematical expressions and diagrams](https://docs.github.com/en/communities/documenting-your-project-with-wikis/editing-wiki-content#adding-mathematical-expressions-and-diagrams)
  * [Supported MediaWiki formats](https://docs.github.com/en/communities/documenting-your-project-with-wikis/editing-wiki-content#supported-mediawiki-formats)


## [Adding links](https://docs.github.com/en/communities/documenting-your-project-with-wikis/editing-wiki-content#adding-links)
You can create links in wikis using one of the following formats. For example:
  * If your pages are rendered with Markdown, the link syntax is `[Link Text](full-URL-of-wiki-page)`.
  * With MediaWiki syntax, the link syntax is `[[Nameofwikipage|Link Text]]`.


## [Adding images](https://docs.github.com/en/communities/documenting-your-project-with-wikis/editing-wiki-content#adding-images)
Wikis can display PNG, JPEG, and GIF images.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the menu in a repository. The "Wiki" option is outlined in dark orange.](https://docs.github.com/assets/cb-50193/images/help/wiki/wiki-menu-link.png)
  3. Using the wiki sidebar, navigate to the page you want to change, and then click **Edit**.
  4. In the wiki toolbar, click 
![Screenshot of the toolbar on the edit page of the wiki. The icon to add an image is outlined in dark orange.](https://docs.github.com/assets/cb-23763/images/help/wiki/wiki-add-image.png)
  5. In the "Insert Image" dialog box, type the image URL and the alt text (which is used by search engines and screen readers).
  6. Click **OK**.


### [Linking to images in a repository](https://docs.github.com/en/communities/documenting-your-project-with-wikis/editing-wiki-content#linking-to-images-in-a-repository)
You can link to an image in a repository on GitHub by copying the URL in your browser and using that as the path to the image. For example, embedding an image in your wiki using Markdown might look like this:
```
[[https://github.com/USERNAME/REPOSITORY/blob/main/img/octocat.png|alt=octocat]]

```

## [Adding mathematical expressions and diagrams](https://docs.github.com/en/communities/documenting-your-project-with-wikis/editing-wiki-content#adding-mathematical-expressions-and-diagrams)
You can use Markdown to add rendered math expressions, diagrams, maps, and 3D models to your wiki. For more information on creating rendered math expressions, see [Writing mathematical expressions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions). For more information on creating diagrams, maps and 3D models, see [Creating diagrams](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams).
## [Supported MediaWiki formats](https://docs.github.com/en/communities/documenting-your-project-with-wikis/editing-wiki-content#supported-mediawiki-formats)
No matter which markup language your wiki page is written in, certain MediaWiki syntax will always be available to you.
  * Horizontal rules via `---`
  * Shorthand symbol entities (such as `&delta;` or `&euro;`)


For security and performance reasons, some syntaxes are unsupported.
  * [Transclusion](https://www.mediawiki.org/wiki/Transclusion)
  * Definition lists
  * Indentation
  * Table of contents


