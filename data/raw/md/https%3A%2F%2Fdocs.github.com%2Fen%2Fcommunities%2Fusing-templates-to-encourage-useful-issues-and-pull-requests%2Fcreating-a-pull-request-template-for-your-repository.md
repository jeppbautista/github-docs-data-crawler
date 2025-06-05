  * [Building communities](https://docs.github.com/en/communities "Building communities")/
  * [Issue & PR templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests "Issue & PR templates")/
  * [Create a PR template](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository "Create a PR template")


# Creating a pull request template for your repository
When you add a pull request template to your repository, project contributors will automatically see the template's contents in the pull request body.
## In this article
  * [Adding a pull request template](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository#adding-a-pull-request-template)
  * [Further reading](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository#further-reading)


For more information, see [About issue and pull request templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates).
You can create a _PULL_REQUEST_TEMPLATE/_ subdirectory in any of the supported folders to contain multiple pull request templates, and use the `template` query parameter to specify the template that will fill the pull request body. For more information, see [Using query parameters to create a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/using-query-parameters-to-create-a-pull-request).
You can create default pull request templates for your organization or personal account. For more information, see [Creating a default community health file](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file).
## [Adding a pull request template](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository#adding-a-pull-request-template)
  1. On GitHub, navigate to the main page of the repository.
  2. Above the list of files, select the **Add file**
Alternatively, you can click 
![Screenshot of the main page of a repository highlighting both the "Add file" and the "plus sign" icon, described above, with an orange outline.](https://docs.github.com/assets/cb-60263/images/help/repository/add-file-buttons.png)
  3. In the file name field:
     * To make your pull request template visible in the repository's root directory, name the pull request template `pull_request_template.md`.
     * To make your pull request template visible in the repository's `docs` directory, name the pull request template `docs/pull_request_template.md`.
     * To store your file in a hidden directory, name the pull request template `.github/pull_request_template.md`.
     * To create multiple pull request templates and use the `template` query parameter to specify a template to fill the pull request body, type _.github/PULL_REQUEST_TEMPLATE/_ , then the name of your pull request template. For example, `.github/PULL_REQUEST_TEMPLATE/pull_request_template.md`. You can also store multiple pull request templates in a `PULL_REQUEST_TEMPLATE` subdirectory within the root or `docs/` directories. For more information, see [Using query parameters to create a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/using-query-parameters-to-create-a-pull-request).
  4. In the body of the new file, add your pull request template. This template could consist of asking to include:
     * A [reference to a related issue](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#referencing-issues-and-pull-requests) in your repository.
     * A description of the changes proposed in the pull request.
     * [@mentions](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#mentioning-people-and-teams) of the person or team responsible for reviewing proposed changes.
  5. Click **Commit changes...**
  6. In the "Commit message" field, type a short, meaningful commit message that describes the change you made to the file. You can attribute the commit to more than one author in the commit message. For more information, see [Creating a commit with multiple authors](https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/creating-a-commit-with-multiple-authors).
  7. Below the commit message fields, decide whether to add your commit to the current branch or to a new branch. If your current branch is the default branch, you should choose to create a new branch for your commit and then create a pull request. For more information, see [Creating a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).
![Screenshot of a GitHub pull request showing a radio button to commit directly to the main branch or to create a new branch. New branch is selected.](https://docs.github.com/assets/cb-27122/images/help/repository/choose-commit-branch.png)
Templates are available to collaborators when they are merged into the repository's default branch.
  8. Click **Commit changes** or **Propose changes**.


## [Further reading](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository#further-reading)
  * [About issue and pull request templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates)
  * [Creating an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue)
  * [Creating a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)


