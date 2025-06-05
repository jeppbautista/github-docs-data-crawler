  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL for VS Code](https://docs.github.com/en/code-security/codeql-for-vs-code "CodeQL for VS Code")/
  * [Getting started](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code "Getting started")/
  * [Queries at scale](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/running-codeql-queries-at-scale-with-multi-repository-variant-analysis "Queries at scale")


# Running CodeQL queries at scale with multi-repository variant analysis
You can run CodeQL queries on a large number of repositories on GitHub from Visual Studio Code.
## In this article
  * [About running CodeQL queries at scale with multi-repository variant analysis](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/running-codeql-queries-at-scale-with-multi-repository-variant-analysis#about-running-codeql-queries-at-scale-with-multi-repository-variant-analysis)
  * [Setting up a controller repository for MRVA](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/running-codeql-queries-at-scale-with-multi-repository-variant-analysis#setting-up-a-controller-repository-for-mrva)
  * [Running a query at scale using MRVA](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/running-codeql-queries-at-scale-with-multi-repository-variant-analysis#running-a-query-at-scale-using-mrva)
  * [Selecting a single GitHub repository or organization for analysis](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/running-codeql-queries-at-scale-with-multi-repository-variant-analysis#selecting-a-single-github-repository-or-organization-for-analysis)
  * [Exploring your results](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/running-codeql-queries-at-scale-with-multi-repository-variant-analysis#exploring-your-results)
  * [Creating a custom list of repositories](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/running-codeql-queries-at-scale-with-multi-repository-variant-analysis#creating-a-custom-list-of-repositories)
  * [Running CodeQL queries with multi-repository variant analysis on self-hosted runners](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/running-codeql-queries-at-scale-with-multi-repository-variant-analysis#running-codeql-queries-with-multi-repository-variant-analysis-on-self-hosted-runners)


## [About running CodeQL queries at scale with multi-repository variant analysis](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/running-codeql-queries-at-scale-with-multi-repository-variant-analysis#about-running-codeql-queries-at-scale-with-multi-repository-variant-analysis)
With multi-repository variant analysis (MRVA), you can run CodeQL queries on a list of up to 1,000 repositories on GitHub from Visual Studio Code.
When you run MRVA against a list of repositories, your query is run against each repository that has a CodeQL database available to analyze. GitHub creates and stores the latest CodeQL database for the default branch of thousands of public repositories, including every repository that runs code scanning using CodeQL.
You need to enable code scanning using CodeQL on GitHub, using either default setup or advanced setup, before adding your repository to a list for analysis. For information about enabling code scanning using CodeQL, see [Configuring default setup for code scanning](https://docs.github.com/en/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/configuring-code-scanning-for-a-repository#configuring-code-scanning-automatically).
### [How MRVA runs queries against CodeQL databases on GitHub.com](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/running-codeql-queries-at-scale-with-multi-repository-variant-analysis#how-mrva-runs-queries-against-codeql-databases-on-githubcom)
When you run MRVA, the analysis is run entirely using GitHub Actions. You don't need to create any workflows, but you must specify which repository the CodeQL for Visual Studio Code extension should use as a controller repository. As the analysis of each repository completes, the results are sent to VS Code for you to view.
The CodeQL extension builds a CodeQL pack with your library and any library dependencies. The CodeQL pack and your selected repository list are posted to an API endpoint on GitHub, which triggers a GitHub Actions dynamic workflow in your controller repository. The workflow spins up multiple parallel jobs to execute the CodeQL query against the repositories in the list, optimizing query execution. As each repository is analyzed, the results are processed and displayed in VS Code.
### [Prerequisites](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/running-codeql-queries-at-scale-with-multi-repository-variant-analysis#prerequisites)
  * You must define a controller repository before you can run your first multi-repository variant analysis.
  * Controller repositories can be empty, but they must have at least one commit.
  * On GitHub.com, the controller repository visibility can be "public" if you plan to analyze only public repositories. The variant analysis will be free.
  * The controller repository visibility must be "private" if you need to analyze any private or internal repositories on GitHub.com.


Any actions minutes that you use to run variant analysis on private or internal repositories, above the free limit, is charged to the repository owner. For more information about free minutes and billing, see [About billing for GitHub Actions](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions).
## [Setting up a controller repository for MRVA](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/running-codeql-queries-at-scale-with-multi-repository-variant-analysis#setting-up-a-controller-repository-for-mrva)
  1. In the "Variant Analysis Repositories" view, click **Set up controller repository** to display a field for the controller repository.
![Screenshot of the "Variant Analysis Repositories" view. The button to "Set up controller repository" is highlighted in dark orange.](https://docs.github.com/assets/cb-22000/images/help/security/codeql-for-vs-code-controller-repository.png)
  2. Type the owner and name of the repository on GitHub that you want to use as your controller repository and press the **Enter** key.
  3. If you are prompted to authenticate with GitHub, follow the instructions and sign in to your account. When you have finished, a prompt from GitHub Authentication may ask for permission to open in Visual Studio Code, click **Open**.


The name of the controller repository is saved in your settings for the CodeQL extension. For information on how to edit the controller repository, see [Customizing settings](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/customizing-settings).
## [Running a query at scale using MRVA](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/running-codeql-queries-at-scale-with-multi-repository-variant-analysis#running-a-query-at-scale-using-mrva)
  1. By default, the "Variant Analysis Repositories" view shows the default lists of the Top 10, Top 100, and Top 1000 public repositories on GitHub.com for the language that you are analyzing. If your controller repository is hosted on SUBDOMAIN.ghe.com, these lists are not available.
  2. Optionally, you can add a new repository, organization, or list.
    1. In the "Variant Analysis Repositories" view, click **+** to add a new database.
    2. From the dropdown menu, select **From a GitHub repository** or **All repositories of GitHub org or owner**.
    3. Type the identifier of the repository or organization that you want to use into the field.
  3. Select which GitHub repository or repositories you want to run your query against.
![Screenshot of the "Variant Analysis Repositories" view. The "octo-org/octo-repo" row is highlighted blue and its "Select" button outlined in orange.](https://docs.github.com/assets/cb-30188/images/help/security/codeql-for-vs-code-variant-analysis-repo-lists.png)
  4. Open the query you want to run, right-click in the query file, and select **CodeQL: Run Variant Analysis** to start variant analysis.


To a cancel a variant analysis run, click **Stop query** in the "Variant Analysis Results" view.
## [Selecting a single GitHub repository or organization for analysis](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/running-codeql-queries-at-scale-with-multi-repository-variant-analysis#selecting-a-single-github-repository-or-organization-for-analysis)
  1. In the "Variant Analysis Repositories" view, click **+** to add a new database.
  2. From the dropdown menu, select **From a GitHub repository** or **All repositories of GitHub org or owner**.
  3. Type the identifier of the repository or organization that you want to use into the field.


### [Errors and warnings](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/running-codeql-queries-at-scale-with-multi-repository-variant-analysis#errors-and-warnings)
When you run MRVA, there are two key places where errors and warnings are displayed:
  * Visual Studio Code errors: any problems with creating a CodeQL pack and sending the analysis to GitHub are reported as Visual Studio Code errors in the bottom right corner of the application. Information is also available in the "Problems" view.
  * "Variant Analysis Results": any problems with the variant analysis run are reported in this view.


## [Exploring your results](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/running-codeql-queries-at-scale-with-multi-repository-variant-analysis#exploring-your-results)
As soon as a workflow to run your variant analysis on GitHub is running, a "Variant Analysis Results" view opens to display the results as they are ready. You can use this view to monitor progress, see any errors, and access the workflow logs in your controller repository.
![Screenshot of "Variant Analysis Results" showing a run for "FileAccessToHttp.ql". Blue circles show the number of results found or "-" still running.](https://docs.github.com/assets/cb-41107/images/help/security/codeql-for-vs-code-variant-analysis-results-view.png)
When your variant analysis run is scheduled, the "Results" view automatically opens. Initially, the view shows a list of every repository that was scheduled for analysis. As each repository is analyzed, the view is updated to show a summary of the number of results. To view the detailed results for a repository (including results paths), click the repository name.
For each repository, you can see:
  * Number of results found by the query
  * Visibility of the repository
  * Whether analysis is still running or has finished
  * Number of stars the repository has on GitHub


### [Seeing the results for a repository](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/running-codeql-queries-at-scale-with-multi-repository-variant-analysis#seeing-the-results-for-a-repository)
  1. Click the repository name to show a summary of each result.
  2. Explore the information available for each result using links to the source files on GitHub. For data flow queries, there'll be an additional "Show paths" link.
![Screenshot of the "Variant Analysis Results" view, with blue links to GitHub source files. There is a "Show paths" link, highlighted in dark orange.](https://docs.github.com/assets/cb-66657/images/help/security/codeql-for-vs-code-variant-analysis-result.png)


### [Exporting your results](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/running-codeql-queries-at-scale-with-multi-repository-variant-analysis#exporting-your-results)
You can export your results for further analysis or to discuss them with collaborators. In the "Results" view, click **Export results** to export the results to a secret gist on GitHub or to a Markdown file in your workspace.
## [Creating a custom list of repositories](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/running-codeql-queries-at-scale-with-multi-repository-variant-analysis#creating-a-custom-list-of-repositories)
CodeQL analysis always requires a CodeQL database to run queries against. When you run variant analysis against a list of repositories, your query will only be executed against the repositories that currently have a CodeQL database available to download. The best way to make a repository available for variant analysis is to enable code scanning with CodeQL. For information about enabling code scanning using CodeQL, see [Configuring default setup for code scanning](https://docs.github.com/en/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/configuring-code-scanning-for-a-repository#configuring-code-scanning-automatically).
  1. In the "Variant Analysis Repositories" view, click the "Add list" icon.
![Screenshot of the "Variant Analysis Results" view. The "add-list" icon is highlighted in dark orange.](https://docs.github.com/assets/cb-10555/images/help/security/codeql-for-vs-code-add-list.png)
  2. Type a name for the new list and press **Enter**.
  3. Select your list in the view, then click **+** to add a repository to your list.


### [Managing your custom lists of repositories](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/running-codeql-queries-at-scale-with-multi-repository-variant-analysis#managing-your-custom-lists-of-repositories)
You can manage and edit your custom lists by right-clicking on either the list name, or a repository name within the list, and selecting an option from the context menu.
The custom lists are stored in your workspace in a `databases.json` file. If you want to edit this file directly in Visual Studio Code, you can open it by clicking **{ }** in the view header.
For example, if you want to continue analyzing a set of repositories that had results for your query, click **Copy repository list** in the "Variant Analysis Results" view to add a list of only the repositories that have results to the clipboard as JSON.
In the following example snippet, `my-organization/my-repository` had results for a query:
```
{
    "name": "new-repo-list",
    "repositories": [
        "my-organization/my-repository"
    ]
}

```

You can then insert the `new-repo-list` of repositories into `databases.json`for easy access in the "Variant Analysis Repositories" view.
### [Using GitHub code search to add repositories to a custom list](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/running-codeql-queries-at-scale-with-multi-repository-variant-analysis#using-github-code-search-to-add-repositories-to-a-custom-list)
This feature uses the legacy code search via the GitHub code search API. For more information on the syntax to use, see [Searching code (legacy)](https://docs.github.com/en/search-github/searching-on-github/searching-code).
You can use code search directly in the CodeQL extension to add a subset of repositories from GitHub to a custom list.
For example, to add all repositories in the `rails` organization on GitHub, search `org:rails`.
You can add a maximum of 1,000 repositories to a custom list per search.
  1. In the "Variant Analysis Repositories" view, choose the list that you want to add repositories to. You can create a new list or choose an existing list that already contains repositories.
  2. Right-click on the list you have chosen and then click **Add repositories with GitHub code search**.
  3. In the pop-up that appears at the top of the application, under the search bar, select a language for your search from the choices in the dropdown.
  4. In the search bar, type the search query that you want to use and press **Enter**.


You can view the progress of your search in the bottom right corner of the application in a box with the text `Searching for repositories...`. If you click **Cancel** , no repositories will be added to your list. Once complete, you will see the resulting repositories appear in the dropdown under your custom list in the Variant Analysis Repositories view.
Some of the resulting repositories will not have CodeQL databases and some may not allow access by the CodeQL extension for Visual Studio Code. When you run an analysis on the list, the "Variant Analysis Results" view will show you which repositories were analyzed, which denied access, and which had no CodeQL database.
## [Running CodeQL queries with multi-repository variant analysis on self-hosted runners](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/running-codeql-queries-at-scale-with-multi-repository-variant-analysis#running-codeql-queries-with-multi-repository-variant-analysis-on-self-hosted-runners)
To run CodeQL queries with multi-repository variant analysis on self-hosted runners, you first need to ensure that you have added a self-hosted runner to your controller repository, or ensure that the controller repository has access to an organization- or enterprise-level runner.
You then need to add a new Actions repository variable in your controller repository with the name `MRVA_RUNNER_OS` containing a JSON-formatted list of the labels of the self-hosted runner you wish to use. For example:
```
["self-hosted", "macOS", "ARM64"]

```

You must set the `MRVA_RUNNER_OS` variable under the Actions repository variables in your controller repository's settings, and not an environment variable or Actions secret under your Actions settings or in your workflow's `.yml` file. See [Store information in variables](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/store-information-in-variables#creating-configuration-variables-for-a-repository).
For more information, see [Adding self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/adding-self-hosted-runners#adding-a-self-hosted-runner-to-a-repository) and [Managing access to self-hosted runners using groups](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups#changing-which-repositories-can-access-a-runner-group).
When you run a query with multi-repository variant analysis on a self-hosted runner, the analysis is run entirely on the self-hosted runner. You don't need to create any new workflows, but you must specify which repository the CodeQL for Visual Studio Code extension should use as a controller repository. As the analysis of each repository completes, the results are sent to VS Code for you to view.
