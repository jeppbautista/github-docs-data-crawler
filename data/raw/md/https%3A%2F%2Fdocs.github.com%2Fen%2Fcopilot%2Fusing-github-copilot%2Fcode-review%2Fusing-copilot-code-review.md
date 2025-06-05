  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Use GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot "Use GitHub Copilot")/
  * [Code review](https://docs.github.com/en/copilot/using-github-copilot/code-review "Code review")/
  * [Use code review](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review "Use code review")


# Using GitHub Copilot code review
Learn how to request a code review from GitHub Copilot.
## Tool navigation
  * [Visual Studio](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review?tool=visualstudio)
  * [Visual Studio Code](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review?tool=vscode)
  * [Web browser](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review?tool=webui)


## In this article
  * [About Copilot code review](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review#about-copilot-code-review)
  * [Requesting a review from Copilot](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review#requesting-a-review-from-copilot)
  * [Working with suggested changes provided by Copilot](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review#working-with-suggested-changes-provided-by-copilot)
  * [Providing feedback on Copilot's reviews](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review#providing-feedback-on-copilots-reviews)
  * [Requesting a re-review from Copilot](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review#requesting-a-re-review-from-copilot)
  * [Enabling automatic reviews](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review#enabling-automatic-reviews)
  * [Customizing Copilot's reviews with coding guidelines](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review#customizing-copilots-reviews-with-coding-guidelines)
  * [Working with suggested changes provided by Copilot](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review#working-with-suggested-changes-provided-by-copilot-1)
  * [Providing feedback on Copilot's reviews](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review#providing-feedback-on-copilots-reviews-1)
  * [Customizing Copilot's reviews with coding guidelines](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review#customizing-copilots-reviews-with-coding-guidelines-1)


## [About Copilot code review](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review#about-copilot-code-review)
GitHub Copilot can review your code and provide feedback. Where possible, Copilot's feedback includes suggested changes which you can apply with a couple of clicks.
Copilot code review in Visual Studio Code supports two types of review:
  * **Review selection:** Highlight code and ask for an initial review
  * **Review changes:** Request a deeper review of all your changes


The current functionality and availability of the two types of review is summarized in the following table:
| Review selection | Review changes  
---|---|---  
Available in | Visual Studio Code | Visual Studio Code and the GitHub website  
Premium/standard feature | Standard feature available to all Copilot subscribers | Premium feature. Available with the Copilot Pro, Copilot Pro+, Copilot Business, and Copilot Enterprise plans. Per-person monthly quota applies.  
Description | Initial review of a highlighted section of code with feedback and suggestions | Deeper review of all changes  
Language support | All | C, C#, C++, Go, Java, JavaScript, Kotlin, Markdown, Python, Ruby, Swift, TypeScript   
  
Public preview support for HTML and Text.  
Custom coding guidelines support | No | Yes, see [Customizing Copilot's reviews with coding guidelines](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review#customizing-copilots-reviews-with-coding-guidelines)  
### [Code review monthly quota](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review#code-review-monthly-quota)
The **review changes** type of Copilot code review is a premium feature with a per-person monthly quota.
The per-person quota for Copilot code review will commence on June 4, 2025.
When you assign Copilot as a reviewer for a pull request, one premium request is deducted from your monthly quota each time Copilot posts comments to the pull request. See [About premium requests](https://docs.github.com/en/copilot/managing-copilot/monitoring-usage-and-entitlements/about-premium-requests).
If a repository is configured to automatically request a code review from Copilot for all new pull requests, the premium request usage is applied to the quota of the pull request author. If a pull request is created by GitHub Actions or by a bot, the usage will apply to the user who triggered the workflow (if identifiable), or to a designated billing owner.
When you reach your monthly quota you will not be able to get a code review from Copilot until your quota resets—unless you upgrade your Copilot plan or enable additional premium requests.
Two types of Copilot code review are available:
  * **Review selection:** Highlight code and ask for an initial review _(only available in VS Code)_
  * **Review changes:** Request a deeper review of all your changes _(available in VS Code and the GitHub website)_


This version of the article relates to Copilot code review on the GitHub website. To see information about the review selection type of Copilot code review, click the "Visual Studio Code" tool switcher at the top of the page.
### [Availability](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review#availability)
Copilot code review on the GitHub website is a premium feature, available with the Copilot Pro, Copilot Pro+, Copilot Business, and Copilot Enterprise plans.
### [Code review monthly quota](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review#code-review-monthly-quota-1)
The **review changes** type of Copilot code review is a premium feature with a per-person monthly quota.
The per-person quota for Copilot code review will commence on June 4, 2025.
When you assign Copilot as a reviewer for a pull request, one premium request is deducted from your monthly quota each time Copilot posts comments to the pull request. See [About premium requests](https://docs.github.com/en/copilot/managing-copilot/monitoring-usage-and-entitlements/about-premium-requests).
If a repository is configured to automatically request a code review from Copilot for all new pull requests, the premium request usage is applied to the quota of the pull request author. If a pull request is created by GitHub Actions or by a bot, the usage will apply to the user who triggered the workflow (if identifiable), or to a designated billing owner.
When you reach your monthly quota you will not be able to get a code review from Copilot until your quota resets—unless you upgrade your Copilot plan or enable additional premium requests.
### [Language support](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review#language-support)
Copilot code review on the GitHub website supports all languages.
### [Validating Copilot code reviews](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review#validating-copilot-code-reviews)
Copilot isn't guaranteed to spot all problems or issues in a pull request, and sometimes it will make mistakes. Always validate Copilot's feedback carefully, and supplement Copilot's feedback with a human review.
For more information, see [Responsible use of GitHub Copilot code review](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-code-review).
## [Requesting a review from Copilot](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review#requesting-a-review-from-copilot)
These instructions explain how to use Copilot code review in the GitHub website. To see instructions for other popular coding environments, use the tool switcher at the top of the page.
### [Requesting a pull request review from Copilot](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review#requesting-a-pull-request-review-from-copilot)
  1. On GitHub.com, create a pull request or navigate to an existing pull request.
  2. Open the **Reviewers** menu, then select **Copilot**.
![Screenshot of selecting 'Copilot' from the 'Reviewers' menu.](https://docs.github.com/assets/cb-33497/images/help/copilot/code-review/request-review@2x.png)
  3. Wait for Copilot to review your pull request. This usually takes less than 30 seconds.
  4. Scroll down and read through Copilot's comments.
![Screenshot of a code review left by Copilot.](https://docs.github.com/assets/cb-132888/images/help/copilot/code-review/review-comment@2x.png)
Copilot always leaves a "Comment" review, not an "Approve" review or a "Request changes" review. This means that Copilot's reviews do not count toward required approvals for the pull request, and Copilot's reviews will not block merging changes. For more details, see [Approving a pull request with required reviews](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/approving-a-pull-request-with-required-reviews).
  5. Copilot's review comments behave like review comments from humans. You can add reactions to them, comment on them, resolve them and hide them.
Any comments you add to Copilot's review comments will be visible to humans, but they won't be visible to Copilot, and Copilot won't reply.


## [Working with suggested changes provided by Copilot](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review#working-with-suggested-changes-provided-by-copilot)
Where possible, Copilot's feedback includes suggested changes which you can apply with a couple of clicks.
If you're happy with the changes, you can accept a single suggestion from Copilot and commit it, or accept a group of suggestions together in a single commit. For more information, see [Incorporating feedback in your pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/incorporating-feedback-in-your-pull-request).
If you want to validate Copilot's suggested changes (for example by running automated tests or your linter), or if you want to make modifications before committing the suggested changes, click the **Open in Workspace** button. For more information, see [Using Copilot to help you work on a pull request](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-for-pull-requests/using-copilot-to-help-you-work-on-a-pull-request).
## [Providing feedback on Copilot's reviews](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review#providing-feedback-on-copilots-reviews)
You can provide feedback on Copilot's comments directly within each comment. We use this information to improve the product and the quality of Copilot's suggestions.
  1. On a pull request review comment from Copilot, click the thumbs up (👍) or thumbs down (👎) button.
![Screenshot showing a Copilot code review comment with the thumbs up and thumbs down buttons.](https://docs.github.com/assets/cb-19709/images/help/copilot/code-review/feedback-controls@2x.png)
  2. If you click the thumbs down button, you're asked to provide additional information. You can, optionally, pick the reason for your negative feedback and leave a comment before clicking **Submit feedback**.
![Screenshot of the form for providing additional information when you give negative feedback on a comment from Copilot.](https://docs.github.com/assets/cb-90167/images/help/copilot/code-review/feedback-modal@2x.png)


## [Requesting a re-review from Copilot](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review#requesting-a-re-review-from-copilot)
When you push changes to a pull request that Copilot has reviewed, it won't automatically re-review your changes.
To request a re-review from Copilot, click the **Reviewers** menu. For more information, see [Requesting a pull request review](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/requesting-a-pull-request-review).
When re-reviewing a pull request, Copilot may repeat the same comments again, even if they have been dismissed with the "Resolve conversation" button or downvoted with the thumbs down (👎) button.
## [Enabling automatic reviews](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review#enabling-automatic-reviews)
By default, you manually request a review from Copilot on each pull request, in the same way you would request a review from a human. However, you can set up Copilot to automatically review all pull requests. See [Configuring automatic code review by Copilot](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-automatic-code-review-by-copilot).
## [Customizing Copilot's reviews with coding guidelines](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review#customizing-copilots-reviews-with-coding-guidelines)
The custom coding guidelines feature is only available with the Copilot Enterprise plan, and is currently limited to selected customers.
When using Copilot code review to review changes in Visual Studio Code or the GitHub website, you can customize Copilot's review with custom coding guidelines written in natural language. Copilot will give feedback based on your coding guidelines when it reviews your code. For more information, see [Configuring coding guidelines for GitHub Copilot code review](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-coding-guidelines).
Comments generated based on a coding guideline will include a message, highlighting their source.
These instructions explain how to use Copilot code review in Visual Studio Code. To see instructions for other popular coding environments, use the tool switcher at the top of the page.
Copilot code review is only available in Visual Studio Code with version 0.22 or later of the GitHub Copilot Chat extension.
### [Reviewing a selection of code](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review#reviewing-a-selection-of-code)
You can request an initial review of a highlighted selection of code in Visual Studio Code.
  1. In Visual Studio Code, select the code you want to review.
  2. Open the VS Code Command Palette
     * For Mac: 
       * Use: `Shift`+`Command`+`P`
     * For Windows or Linux: 
       * Use `Ctrl`+`Shift`+`P`
  3. In the command palette, search for and select **GitHub Copilot: Review and Comment**.
![Screenshot of the command palette in Visual Studio Code with the GitHub Copilot: Review and Comment command selected.](https://docs.github.com/assets/cb-42682/images/help/copilot/vsc-review-and-comment.png)
  4. Wait for Copilot to review your changes. This usually takes less than 30 seconds.
![Screenshot of the progress indicator when Copilot is performing a review in Visual Studio Code.](https://docs.github.com/assets/cb-12269/images/help/copilot/code-review/vscode-review-progress@2x.png)
  5. If Copilot has any comments, they will be shown inline in your file, and in the **Problems** tab.
![Screenshot of a comment from Copilot in Visual Studio Code.](https://docs.github.com/assets/cb-73469/images/help/copilot/code-review/vscode-comment@2x.png)


### [Reviewing changes](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review#reviewing-changes)
You can request a review for your staged or unstaged changes in Visual Studio Code.
  1. In VS Code, switch to the **Source Control** tab.
  2. To request a review on your unstaged changes, hover over **Changes** in the sidebar, and then click the **Copilot code review - Changes** button.
![Screenshot of the "Copilot code review - Changes" button in Visual Studio Code. The code review button is outlined in dark orange.](https://docs.github.com/assets/cb-20176/images/help/copilot/code-review/vscode-review-button@2x.png)
  3. To request a review on your staged changes, hover over **Staged Changes** in the sidebar, and then click the **Copilot code review - Staged Changes** button.
  4. Wait for Copilot to review your changes. This usually takes less than 30 seconds.
![Screenshot of the progress indicator when Copilot is performing a review in Visual Studio Code.](https://docs.github.com/assets/cb-12269/images/help/copilot/code-review/vscode-review-progress@2x.png)
  5. If Copilot has any comments, they will be shown inline in your file(s), and in the **Problems** tab.
![Screenshot of a comment from Copilot in Visual Studio Code.](https://docs.github.com/assets/cb-73469/images/help/copilot/code-review/vscode-comment@2x.png)


## [Working with suggested changes provided by Copilot](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review#working-with-suggested-changes-provided-by-copilot-1)
Where possible, Copilot's feedback includes suggested changes which you can apply with a single click.
![Screenshot of a comment from Copilot in Visual Studio Code with a suggested change.](https://docs.github.com/assets/cb-73469/images/help/copilot/code-review/vscode-comment@2x.png)
If you're happy with the change, you can accept a suggestion from Copilot by clicking the **Apply and Go To Next** button. Any changes you apply will not be automatically committed.
If you don't want to apply Copilot's suggested change, click the **Discard and Go to Next** button.
## [Providing feedback on Copilot's reviews](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review#providing-feedback-on-copilots-reviews-1)
You can provide feedback on Copilot's comments directly within each comment. We use this information to improve the product and the quality of Copilot's suggestions.
To provide feedback, hover over the comment and click the thumbs up or thumbs down button.
![Screenshot of a comment from Copilot in Visual Studio Code with feedback buttons displayed. The buttons are outlined in dark orange.](https://docs.github.com/assets/cb-55468/images/help/copilot/code-review/vscode-comment-feedback@2x.png)
## [Customizing Copilot's reviews with coding guidelines](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review#customizing-copilots-reviews-with-coding-guidelines-1)
The custom coding guidelines feature is only available with the Copilot Enterprise plan, and is currently limited to selected customers.
When using Copilot code review to review changes in Visual Studio Code or the GitHub website, you can customize Copilot's review with custom coding guidelines written in natural language. Copilot will give feedback based on your coding guidelines when it reviews your code. For more information, see [Configuring coding guidelines for GitHub Copilot code review](https://docs.github.com/en/copilot/using-github-copilot/code-review/configuring-coding-guidelines).
Comments generated based on a coding guideline will include a message, highlighting their source.
These instructions explain how to use Copilot code review in Visual Studio. To see instructions for other popular coding environments, use the tool switcher at the top of the page.
To use Copilot code review, you must use Visual Studio version 17.14 or later. See the [Visual Studio downloads page](https://visualstudio.microsoft.com/downloads/).
  1. In the Git Changes window, click **Review changes with Copilot**. This button appears as a comment icon with a sparkle.
  2. Copilot will begin reviewing your changes. After a few moments, a link showing the number of code review comments appears in the Git Changes window.
  3. Click the link to view and navigate the comments. If no issues are found, you’ll see the message: Copilot did not comment on any files.
  4. Copilot displays comments in your code with a summary of each potential issue. You can:
     * Review and make changes based on the suggestions.
     * Dismiss a comment using the downward arrow in the top-right corner of the comment box.
  5. To remove all review comments, click 


For more information on enabling and configuring Copilot code review in Visual Studio, see [Review local changes with Copilot Chat](https://learn.microsoft.com/en-us/visualstudio/version-control/git-make-commit?view=vs-2022#review-local-changes-with-copilot-chat) in the Visual Studio documentation.
