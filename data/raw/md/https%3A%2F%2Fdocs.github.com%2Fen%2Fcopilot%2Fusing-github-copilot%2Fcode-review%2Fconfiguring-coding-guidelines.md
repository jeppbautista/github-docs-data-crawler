  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Use GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot "Use GitHub Copilot")/
  * [Code review](https://docs.github.com/en/copilot/using-github-copilot/code-review "Code review")/
  * [Configure coding guidelines](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-coding-guidelines "Configure coding guidelines")


# Configuring coding guidelines for GitHub Copilot code review
Learn how to customize Copilot code review with custom coding guidelines.
## In this article
  * [About coding guidelines](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-coding-guidelines#about-coding-guidelines)
  * [Dos and don'ts for coding guidelines](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-coding-guidelines#dos-and-donts-for-coding-guidelines)
  * [Creating a coding guideline](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-coding-guidelines#creating-a-coding-guideline)
  * [Running a review with coding guidelines](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-coding-guidelines#running-a-review-with-coding-guidelines)
  * [Coding guidelines examples](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-coding-guidelines#coding-guidelines-examples)


The custom coding guidelines feature is only available with the Copilot Enterprise plan, and is currently limited to selected customers.
## [About coding guidelines](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-coding-guidelines#about-coding-guidelines)
You can customize Copilot code review with custom coding guidelines written in natural language. For more information on Copilot code review, see [Using GitHub Copilot code review](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review).
With coding guidelines, Copilot can give feedback based on your organization's specific coding style and best practices.
Because Copilot code review is powered by a large language model, it can help with enforcing coding guidelines that are not covered by your linter or static analysis tool.
Coding guidelines are configured at the repository level. You can create and enable up to 6 coding guidelines per repository.
  * Coding guidelines only work with languages supported by Copilot code review. For a list of supported languages, see [Using GitHub Copilot code review](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review#supported-programming-languages).
  * Coding guidelines only apply to code reviews carried out by Copilot. The guidelines do not affect Copilot code completion suggestions, or code suggested in Copilot Chat responses.


## [Dos and don'ts for coding guidelines](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-coding-guidelines#dos-and-donts-for-coding-guidelines)
  * **Do** use simple, clear and concise language to describe your coding guideline.
  * **Do** be as specific as possible about what Copilot should look for - that is, what you do or don't want to see in your code.
  * **Do** take a look at the [Coding guidelines examples](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-coding-guidelines#coding-guidelines-examples) below for some inspiration.
  * **Don't** try to use coding guidelines to enforce style guidelines that can be covered by your linter or static analysis tool.
  * **Don't** use wording that is ambiguous or could be interpreted in different ways.
  * **Don't** try to fit multiple different ideas into a single coding guideline.


## [Creating a coding guideline](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-coding-guidelines#creating-a-coding-guideline)
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Code & automation" section of the sidebar, click **Code review**.
  4. Click **Create guideline**.
  5. Under "Name," give the coding guideline a name.
  6. Under "Description," provide a description of the coding guideline up to 600 characters long. This will be used by Copilot to understand your coding style and to decide when to leave a comment.
How you write your description has a big impact on the quality of comments that Copilot will generate. For help with writing effective coding guidelines, see [Dos and don'ts for coding guidelines](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-coding-guidelines#dos-and-donts-for-coding-guidelines) above, and [Coding guidelines examples](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-coding-guidelines#coding-guidelines-examples) below.
  7. Optionally, limit the coding guideline to specific file types or paths by clicking **Add file path** and adding path patterns.
You can use `fnmatch` syntax to define paths to target, with `*` as a wildcard to match any string of characters.
Because GitHub uses the `File::FNM_PATHNAME` flag for the `File.fnmatch` syntax, the `*` wildcard does not match directory separators (`/`). For example, `qa/*` will match all branches beginning with `qa/` and containing a single slash, but will not match `qa/foo/bar`. You can include any number of slashes after `qa` with `qa/**/*`, which would match, for example, `qa/foo/bar/foobar/hello-world`. You can also extend the `qa` string with `qa**/**/*` to make the rule more inclusive.
For more information about syntax options, see the [fnmatch documentation](https://ruby-doc.org/core-2.5.1/File.html#method-c-fnmatch).
  8. Test your coding guideline to make sure it works as expected.
    1. Click **Add sample**.
    2. Add your own sample, or press 
    3. Click **Save** to save the code sample.
    4. Test the coding guideline against your sample by pressing 
  9. Save your coding guideline, and turn it on, by clicking **Save guideline**.


## [Running a review with coding guidelines](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-coding-guidelines#running-a-review-with-coding-guidelines)
When you request a review from Copilot, it will automatically use the repository's enabled coding guidelines to review your code. For more information, see [Using GitHub Copilot code review](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review).
Comments generated based on a coding guideline will include a message, highlighting their source.
## [Coding guidelines examples](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-coding-guidelines#coding-guidelines-examples)
### [Example 1: Avoid using magic numbers](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-coding-guidelines#example-1-avoid-using-magic-numbers)
**Title:** `Avoid using magic numbers`
**Description:** `Don't use magic numbers in code. Numbers should be defined as constants or variables with meaningful names.`
**Path patterns:** `**/*.py`
### [Example 2: Don't use `SELECT *` in SQL queries](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-coding-guidelines#example-2-dont-use-select--in-sql-queries)
**Title:** `Don't use `SELECT *` in SQL queries`
**Description:** `Don't use `SELECT *` in SQL queries. Always specify the columns you want to select. `COUNT(*)` is allowed.`
**Path patterns:** None (applies to all file types, as SQL queries may be embedded in code).
### [Example 3: Use `fetch` for HTTP requests](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-coding-guidelines#example-3-use-fetch-for-http-requests)
**Title:** `Use `fetch` for HTTP requests`
**Description:** `Use `fetch` for HTTP requests, not `axios` or `superagent` or other libraries.`
**Path patterns:** `**/*.ts`, `**/*.js`, `**/*.jsx`, `**/*.tsx`
### [Example 4: Always tag metrics with the current environment](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-coding-guidelines#example-4-always-tag-metrics-with-the-current-environment)
**Title:** `Always tag metrics with the current environment`
**Description:** `Always include a `env` tag with the current environment when emitting metrics, for example, `env:prod` or `env:dev`.`
**Path patterns:** `*/*.go`, `*/*.java`
