  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Use GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot "Use GitHub Copilot")/
  * [Copilot for pull requests](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-for-pull-requests "Copilot for pull requests")/
  * [Work on a PR](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-for-pull-requests/using-copilot-to-help-you-work-on-a-pull-request "Work on a PR")


# Using Copilot to help you work on a pull request
You can iterate, validate, and integrate suggested changes to code by using Copilot Workspace.
## Who can use this feature?
This feature is not available in GitHub Copilot Free.
## In this article
  * [About using Copilot to help you work on your pull requests](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-for-pull-requests/using-copilot-to-help-you-work-on-a-pull-request#about-using-copilot-to-help-you-work-on-your-pull-requests)
  * [Prerequisites](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-for-pull-requests/using-copilot-to-help-you-work-on-a-pull-request#prerequisites)
  * [Editing files in a pull request](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-for-pull-requests/using-copilot-to-help-you-work-on-a-pull-request#editing-files-in-a-pull-request)
  * [Using Copilot to work on pull request comments](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-for-pull-requests/using-copilot-to-help-you-work-on-a-pull-request#using-copilot-to-work-on-pull-request-comments)
  * [Chatting with Copilot about a pull request](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-for-pull-requests/using-copilot-to-help-you-work-on-a-pull-request#chatting-with-copilot-about-a-pull-request)
  * [Verifying your changes](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-for-pull-requests/using-copilot-to-help-you-work-on-a-pull-request#verifying-your-changes)
  * [Changing the Workspace options](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-for-pull-requests/using-copilot-to-help-you-work-on-a-pull-request#changing-the-workspace-options)


Copilot Workspace is in limited public preview. The waitlist for admission to this preview is currently closed.
## [About using Copilot to help you work on your pull requests](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-for-pull-requests/using-copilot-to-help-you-work-on-a-pull-request#about-using-copilot-to-help-you-work-on-your-pull-requests)
After you create a pull request, you can continue working on the PR on the GitHub website. This article is about Copilot Workspace, which provides a Copilot-enabled environment for:
  * **Refining** your pull requests
  * **Validating** changes
  * **Integrating** suggestions from reviewers


Copilot Workspace enables you to work on your pull requests in one place - on GitHub - from pull request creation to merge.
Copilot can help with pull requests in other ways too. These are explained in separate articles. Copilot can:
  * Write a pull request summary for you - see [Creating a pull request summary with GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-for-pull-requests/creating-a-pull-request-summary-with-github-copilot).
  * Review a pull request for you - see [Using GitHub Copilot code review](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review).
  * Suggest fixes for coding problems identified by CodeQL code scanning - see [Responsible use of Copilot Autofix for code scanning](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/responsible-use-autofix-code-scanning).


### [Benefits of Copilot Workspace](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-for-pull-requests/using-copilot-to-help-you-work-on-a-pull-request#benefits-of-copilot-workspace)
Copilot Workspace:
  * Allows you to work on a pull request without having to switch back and forward between the GitHub website and your IDE.
  * Gives you easy access to view/test/modify/apply coding suggestions, from Copilot code reviews and Copilot Autofix, as well as reviews by human reviewers.
  * Gives you Copilot code completion suggestions on GitHub. Previously these were only available in an IDE.
  * Shows you a list of files changed by the pull request, within the browser-based editor, but also allows you to find and edit any file from across the repo.
  * Enables you to build, test, and run your code directly from the Workspace environment on GitHub.


## [Prerequisites](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-for-pull-requests/using-copilot-to-help-you-work-on-a-pull-request#prerequisites)
Using Copilot Workspace requires an existing pull request on the GitHub website and either of the following:
  * Access to this public preview from the waitlist (now closed).
  * Access to GitHub Advanced Security (GHAS) features on a private repository owned by an organization on a GitHub Team or GitHub Enterprise plan. See [About GitHub Advanced Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security).


Without access to Copilot Workspace you can still edit the files in pull requests by going to the **Files changed** tab, clicking the ellipsis (**...**) next to the file you want to edit, and then clicking **Edit file**.
## [Editing files in a pull request](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-for-pull-requests/using-copilot-to-help-you-work-on-a-pull-request#editing-files-in-a-pull-request)
To work on a pull request in Copilot Workspace:
  1. Click the 
Copilot Workspace opens, displaying an overview of the pull request.
At the left of the Copilot Workspace window is a list of the files changed by the pull request.
![Screenshot of the list of files in a PR, at the left of Copilot Workspace.](https://docs.github.com/assets/cb-97851/images/help/copilot/workspace-files-in-pr.png)
  2. To work on a file that is not currently changed by this pull request, click **Files in this pull request** and, from the dropdown, select **All files in this repository**.
  3. Click a file in the list to open the file in the Workspace editor.
The file is displayed in a diff view. You can change the view if required. See [Changing the Workspace options](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-for-pull-requests/using-copilot-to-help-you-work-on-a-pull-request#changing-the-workspace-options) later in this article.
You can open and change multiple files before committing your changes.
  4. After you have finished making changes, click **Review and commit**.
The **Commit changes** panel is displayed. Copilot autogenerates a commit message for you, based on the changes you have made. You can edit the message and add an extended description if you want.
![Screenshot of the "Commit changes" panel showing an autogenerated commit message and three changed files.](https://docs.github.com/assets/cb-72020/images/help/copilot/workspace-commit-changes.png)
The panel lists the files you have changed. You can expand each file to see the changes you have made.
  5. Optionally, if you edited multiple files and you decide you don't want to commit all of the changes in a single commit, clear the check box beside the files whose changes you don't want to commit. When you click **Commit changes** , the changes you applied to those files will remain applied but uncommitted, and you can add them to the pull request in a separate commit.
If you clear the check box beside some files you may need to rewrite the commit message to avoid mentioning the changes to those files.
  6. Click **Commit changes**.
Alternatively, click **Reset all changes** to return the files to their current state in the pull request, losing the changes you made in the Workspace editor panel. Resetting your changes cannot be undone.


## [Using Copilot to work on pull request comments](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-for-pull-requests/using-copilot-to-help-you-work-on-a-pull-request#using-copilot-to-work-on-pull-request-comments)
You can use Copilot Workspace to work through all comments on your pull request, one after the other, and then commit any changes you choose to make in a single commit.
  1. On a comment that includes a code change suggestion, click **Open in Workspace**.
![Screenshot of a coding suggestion by Copilot code review.](https://docs.github.com/assets/cb-119264/images/help/copilot/workspace-copilot-review-suggestion.png)
Copilot Workspace opens, displaying the suggested change in the Suggestions panel on the right of the Workspace window.
  2. Review the suggested change, then click one of the two buttons at the bottom of the Suggestions panel:
     * **Apply** - If you agree with the suggested change.
     * **Dismiss** - If you do not want to make the suggested change.
  3. If there are multiple comments in the pull request, you can step through to the next comment by clicking the **>** arrow at the bottom of the Suggestions panel.
![Screenshot of the Suggestions panel, showing the ">" arrow and "Dismiss" and "Apply" buttons.](https://docs.github.com/assets/cb-23421/images/help/copilot/workspace-next-comment.png)
  4. Optionally, to see a list of all of the comments in the pull request, click the back arrow at the top left of the Suggestions panel.
![Screenshot of the Suggestions panel, showing the back arrow at the top left.](https://docs.github.com/assets/cb-76575/images/help/copilot/workspace-all-comments.png)
If you have accepted or dismissed any suggestions, these are shown within "applied" and "dismissed" dropdowns, which make it easy to see which suggestions you have not yet dealt with.
![Screenshot a list of comments in the Suggestions panel. Two are awaiting action. Beneath this are dropdown links headed "1 applied" and "1 dismissed."](https://docs.github.com/assets/cb-43119/images/help/copilot/workspace-applied-dismissed.png)
  5. After you have finished reviewing the suggested changes, click **Review and commit**.
  6. Optionally, if you decide you don't want to commit all of the applied changes in a single commit, clear the check box beside the files whose changes you don't want to commit. When you click **Commit changes** , the changes you applied to those files will remain applied but uncommitted, and you can add them to the pull request in a separate commit.
  7. Click **Commit changes**.
Alternatively, click **Reset all changes** to return the suggestions to their initial state, losing the apply or dismiss choices you made, and losing any changes you made by editing files directly in the Workspace editor panel. Resetting your changes cannot be undone.


## [Chatting with Copilot about a pull request](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-for-pull-requests/using-copilot-to-help-you-work-on-a-pull-request#chatting-with-copilot-about-a-pull-request)
  1. At the top of the Workspace window, click the 
  2. At the bottom of the Copilot panel, type a question in the "Ask Copilot" box then press `Enter`.
You can ask questions about:
     * **The currently displayed file** - for example, "how could I improve this file?"
     * **The whole pull request** - for example, "what frameworks are referenced in this pull request?"
     * **General programming topics** - for example, "what is the latest version of ruby?"
For more information, see [Asking GitHub Copilot questions in GitHub](https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-githubcom).


Currently not all Copilot Chat features are available in the public preview of Copilot Workspace.
## [Verifying your changes](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-for-pull-requests/using-copilot-to-help-you-work-on-a-pull-request#verifying-your-changes)
Workspace includes a built-in terminal and a quick way to build, run, and test your code.
### [Opening the terminal](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-for-pull-requests/using-copilot-to-help-you-work-on-a-pull-request#opening-the-terminal)
To open the terminal, click 
The terminal requires a codespace to be running. If you don't see the 
### [Running terminal commands](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-for-pull-requests/using-copilot-to-help-you-work-on-a-pull-request#running-terminal-commands)
You can type commands directly into the terminal, or you can use quick commands to run commonly used commands with a couple of clicks.
#### [Configuring personal quick commands](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-for-pull-requests/using-copilot-to-help-you-work-on-a-pull-request#configuring-personal-quick-commands)
You can configure **Build** , **Run** , and **Test** commands that you can use when you work on a specific project in Copilot Workspace. If commands have already been configured for the repository, you can replace them with alternative commands for your own personal use.
  1. At the top of the Workspace window, click 
If **Build** , **Run** , and **Test** quick commands have already been defined, the 
![Screenshot of the "Commands" dropdown menu with the "Configure" option highlighted with a dark orange outline.](https://docs.github.com/assets/cb-30499/images/help/copilot/workspace-configure-commands.png)
  2. In the "Configure commands" dialog, enter the commands you want to use for **Build** , **Run** , and **Test** options.
  3. Click **Save**.


#### [Configuring quick commands for your repository](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-for-pull-requests/using-copilot-to-help-you-work-on-a-pull-request#configuring-quick-commands-for-your-repository)
You can set default **Build** , **Run** , and **Test** commands for everyone who uses Copilot Workspace to work on pull requests for your repository.
  1. Create or edit a file in the root of your repository called `.devcontainer/devcontainer.json`.
The `.devcontainer/devcontainer.json` file is a configuration file for codespaces created for a repository. For more information, see [Introduction to dev containers](https://docs.github.com/en/enterprise-cloud@latest/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers#devcontainerjson).
  2. Add a `commands` section as follows, replacing the example commands shown here with the commands that people working on your repository should use.
```
{
  "commands": {
    "Build": "make",
    "Run": "./bin/start",
    "Test": "make test"
  }
}

```

  3. Click **Save**.


#### [Using Workspace quick commands](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-for-pull-requests/using-copilot-to-help-you-work-on-a-pull-request#using-workspace-quick-commands)
  1. To run the first of the defined quick commands (typically **Build**), click the button at the top of the Workspace window.
  2. To run a different quick command, click the dropdown arrow beside the button and then click the command you want to run from the dropdown menu.
![Screenshot of the "Commands" dropdown menu with the "Run" option highlighted with a dark orange outline.](https://docs.github.com/assets/cb-30670/images/help/copilot/workspace-run-command.png)
  3. After clicking **Run** , while the process is running, you can click the dropdown arrow again and choose from options to stop or restart the process, or view the output from the run command.
![Screenshot of the dropdown menu for a running application with the "Stop" option highlighted with a dark orange outline.](https://docs.github.com/assets/cb-26856/images/help/copilot/workspace-stop-command.png)


#### [Previewing a web application](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-for-pull-requests/using-copilot-to-help-you-work-on-a-pull-request#previewing-a-web-application)
If your run command starts a web server, the 
Click this button to preview the server output in a new tab of your browser.
## [Changing the Workspace options](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-for-pull-requests/using-copilot-to-help-you-work-on-a-pull-request#changing-the-workspace-options)
You can change how files are displayed in Copilot Workspace.
### [Changing the diff view](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-for-pull-requests/using-copilot-to-help-you-work-on-a-pull-request#changing-the-diff-view)
  1. Click the compare picker icon (
  2. Choose a view option:
     * **Unified** - Shows changes in a single view, with added lines highlighted in green and removed lines highlighted in red.
     * **Split** - Shows changes in a split view, with the original file on the left and the new file on the right.
     * **Hidden** - Shows the current state of the file in this pull request, without showing what changes the PR makes.


### [Wrapping long lines](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-for-pull-requests/using-copilot-to-help-you-work-on-a-pull-request#wrapping-long-lines)
  1. Click the ellipsis (**...**), at the top right of the Workspace editor panel.
  2. Click **Wrap lines** to toggle line wrapping on or off.


