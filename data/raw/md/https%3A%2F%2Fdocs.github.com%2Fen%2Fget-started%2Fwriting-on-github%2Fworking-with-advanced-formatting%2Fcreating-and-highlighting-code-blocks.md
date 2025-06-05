  * [Get started](https://docs.github.com/en/get-started "Get started")/
  * [Writing on GitHub](https://docs.github.com/en/get-started/writing-on-github "Writing on GitHub")/
  * [Work with advanced formatting](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting "Work with advanced formatting")/
  * [Create code blocks](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks "Create code blocks")


# Creating and highlighting code blocks
Share samples of code with fenced code blocks and enabling syntax highlighting.
## Who can use this feature?
Markdown can be used in the GitHub web interface.
## In this article
  * [Fenced code blocks](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks#fenced-code-blocks)
  * [Syntax highlighting](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks#syntax-highlighting)
  * [Creating diagrams](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks#creating-diagrams)
  * [Further reading](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks#further-reading)


## [Fenced code blocks](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks#fenced-code-blocks)
You can create fenced code blocks by placing triple backticks ````` before and after the code block. We recommend placing a blank line before and after code blocks to make the raw formatting easier to read.
```
```
function test() {
  console.log("notice the blank line before this function?");
}
```

```

![Screenshot of rendered GitHub Markdown showing the use of triple backticks to create code blocks. The block begins with "function test\(\) {."](https://docs.github.com/assets/cb-30161/images/help/writing/fenced-code-block-rendered.png)
To preserve your formatting within a list, make sure to indent non-fenced code blocks by eight spaces.
To display triple backticks in a fenced code block, wrap them inside quadruple backticks.
```
````
```
Look! You can see my backticks.
```
````

```

![Screenshot of rendered Markdown showing that when you write triple backticks between quadruple backticks they are visible in the rendered content.](https://docs.github.com/assets/cb-4725/images/help/writing/fenced-code-show-backticks-rendered.png)
If you are frequently editing code snippets and tables, you may benefit from enabling a fixed-width font in all comment fields on GitHub. For more information, see [About writing and formatting on GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/about-writing-and-formatting-on-github#enabling-fixed-width-fonts-in-the-editor).
## [Syntax highlighting](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks#syntax-highlighting)
You can add an optional language identifier to enable syntax highlighting in your fenced code block.
Syntax highlighting changes the color and style of source code to make it easier to read.
For example, to syntax highlight Ruby code:
```
```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```

```

This will display the code block with syntax highlighting:
![Screenshot of three lines of Ruby code as displayed on GitHub. Elements of the code display in purple, blue, and red type for scannability.](https://docs.github.com/assets/cb-19380/images/help/writing/code-block-syntax-highlighting-rendered.png)
When you create a fenced code block that you also want to have syntax highlighting on a GitHub Pages site, use lower-case language identifiers. For more information, see [About GitHub Pages and Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll#syntax-highlighting).
We use [Linguist](https://github.com/github-linguist/linguist) to perform language detection and to select [third-party grammars](https://github.com/github-linguist/linguist/blob/main/vendor/README.md) for syntax highlighting. You can find out which keywords are valid in [the languages YAML file](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml).
## [Creating diagrams](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks#creating-diagrams)
You can also use code blocks to create diagrams in Markdown. GitHub supports Mermaid, GeoJSON, TopoJSON, and ASCII STL syntax. For more information, see [Creating diagrams](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams).
## [Further reading](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks#further-reading)
  * [GitHub Flavored Markdown Spec](https://github.github.com/gfm/)
  * [Basic writing and formatting syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)


