  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Use GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot "Use GitHub Copilot")/
  * [Use Copilot to create issues](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-to-create-issues "Use Copilot to create issues")


# Using GitHub Copilot to create issues
Use Copilot to quickly generate structured, high-quality issues from natural language or images, without filling out every field manually.
## In this article
  * [Creating an issue with Copilot](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-to-create-issues#creating-an-issue-with-copilot)
  * [Creating multiple issues at once](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-to-create-issues#creating-multiple-issues-at-once)
  * [Assigning issues to Copilot](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-to-create-issues#assigning-issues-to-copilot)


This feature is in public preview and subject to change.
Creating issues manually can be repetitive and time-consuming. With Copilot, you can create issues faster by prompting in natural language, or even by uploading a screenshot. Copilot fills out the title, body, labels, assignees, and more, using your repository’s templates and structure.
You stay in control: review and refine what Copilot suggests, or make changes directly in the issue form.
## [Creating an issue with Copilot](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-to-create-issues#creating-an-issue-with-copilot)
You can create issues from Copilot Chat's immersive view.
  1. Go to the immersive view of Copilot Chat (<https://github.com/copilot>).
  2. At the bottom of the page, in the "Ask Copilot" box, describe what you want to file. Specify the repository you would like to create your issue in using the org/repository format. If you do not specify a repository, Copilot will infer the repository based on the repository you last created an issue in. You can try:
     * "Create a feature request to add fuzzy matching to search."
     * "Log a bug for a 500 error when submitting the login form."
     * "Create a task and add a label for ‘needs design review’."
You can only use Copilot to create issues in repositories where you already have permission to create issues. This feature doesn't change your access or bypass repository permissions.
  3. Or, you can use one of the following methods to include an image in your prompt:
     * Copy an image and paste it into the prompt box at the bottom of the page.
     * Click **Image**. Browse to the image file you want to attach, select it and click **Open**.
     * Drag and drop an image file from your operating system's file explorer into the prompt box.
After you paste or upload the image, you can add text to your prompt, for example: "Create an issue because this error appears when trying to reset a password."
  4. Copilot will draft an issue that includes:
     * A suggested title.
     * A formatted body (based on your repository’s template)
Based on your prompt, Copilot will also suggest metadata such as labels, assignee, and issue type.
  5. Review the draft. You can:
     * Edit any part of the issue manually.
     * Ask Copilot to make changes with a follow-up prompt.
     * Switch templates without losing your input.
  6. Once the issue looks good, click **Create**.


Copilot tailors its suggestions based on the repository where you're creating the issue. It selects the most relevant template for your prompt and applies associated metadata, like labels or issue type. If you choose a different template, Copilot automatically reformats the content to match the new structure.
## [Creating multiple issues at once](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-to-create-issues#creating-multiple-issues-at-once)
If your prompt includes multiple tasks or bugs, Copilot can draft more than one issue at a time.
Each draft appears separately, and you can review and edit them individually. To publish the issues, click **Create** on each one you want to submit.
## [Assigning issues to Copilot](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-to-create-issues#assigning-issues-to-copilot)
To assign an issue to Copilot, you need to have Copilot coding agent enabled. See [Enabling Copilot coding agent](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/enabling-copilot-coding-agent).
You can assign the issue during creation in one of two ways:
  * **Natural language:** Prompt Copilot with something like “Assign this issue to Copilot."
  * **Manually:** Select "Copilot" from the assignee list.


Once the issue is assigned and created, Copilot will start working on it automatically. You’ll see a 👀 emoji reaction on the issue to indicate that Copilot is working on it.
