  * [Get started](https://docs.github.com/en/get-started "Get started")/
  * [Writing on GitHub](https://docs.github.com/en/get-started/writing-on-github "Writing on GitHub")/
  * [Work with advanced formatting](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting "Work with advanced formatting")/
  * [About tasklists](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/about-tasklists "About tasklists")


# About tasklists
You can use tasklists to break the work for an issue or pull request into smaller tasks, then track the full set of work to completion.
## Who can use this feature?
Markdown can be used in the GitHub web interface.
## In this article
  * [About tasklists](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/about-tasklists#about-tasklists)
  * [About issue tasklists](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/about-tasklists#about-issue-tasklists)
  * [Creating tasklists](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/about-tasklists#creating-tasklists)
  * [Reordering tasks](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/about-tasklists#reordering-tasks)
  * [Converting tasks into issues](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/about-tasklists#converting-tasks-into-issues)
  * [Navigating tracked issues](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/about-tasklists#navigating-tracked-issues)


## [About tasklists](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/about-tasklists#about-tasklists)
Tasklists are retired. You can read more about this on the [GitHub Blog](https://github.blog/changelog/2025-04-29-closing-down-code-scanning-alerts-tracked-in-tasklists/).
You can use sub-issues as the replacement for tasklist blocks. Sub-issues provide a dedicated section within each issue, making it easier to track related work without relying on Markdown. For more information about sub-issues, see [Adding sub-issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues).
A tasklist is a set of tasks that each render on a separate line with a clickable checkbox. You can select or deselect the checkboxes to mark the tasks as complete or incomplete.
You can use Markdown to create a tasklist in any comment on GitHub. If you reference an issue, pull request, or discussion in a tasklist, the reference will unfurl to show the title and state.
## [About issue tasklists](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/about-tasklists#about-issue-tasklists)
If you add a tasklist to the body of an issue, the list has added functionality.
  * To help you track your team's work on an issue, the progress of an issue's tasklist appears in various places on GitHub, such as a repository's list of issues.
  * If a task references another issue and someone closes that issue, the task's checkbox will automatically be marked as complete.
  * If a task requires further tracking or discussion, you can convert the task to an issue by hovering over the task and clicking [Keyboard shortcuts](https://docs.github.com/en/get-started/accessibility/keyboard-shortcuts#issues-and-pull-requests).
  * Any issues referenced in the tasklist will specify that they are tracked in the referencing issue.


![Screenshot of an issue showing a tasklist under the header "Features." Three list items link to other issues.](https://docs.github.com/assets/cb-127397/images/help/writing/task-list-rendered.png)
## [Creating tasklists](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/about-tasklists#creating-tasklists)
To create a task list, preface list items with a hyphen and space followed by `[ ]`. To mark a task as complete, use `[x]`.
```
- [x] #739
- [ ] https://github.com/octo-org/octo-repo/issues/740
- [ ] Add delight to the experience when all tasks are complete :tada:

```

![Screenshot showing the rendered version of the markdown. The references to issues are rendered as issue titles.](https://docs.github.com/assets/cb-64626/images/help/writing/task-list-rendered-simple.png)
You cannot create tasklist items within closed issues or issues with linked pull requests.
## [Reordering tasks](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/about-tasklists#reordering-tasks)
You can reorder the items in a tasklist. First, click or hover to the left of a task's checkbox until a grid of six dots appears. Then, drag and drop the grid to move the task to a new location.
You can reorder tasks across different lists in the same comment, but you cannot reorder tasks across different comments.
![Screenshot of a GitHub issue showing two tasks in a tasklist. A grid of six dots to the left of the second task is outlined in dark orange.](https://docs.github.com/assets/cb-26408/images/help/writing/task-list-reorder.png)
## [Converting tasks into issues](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/about-tasklists#converting-tasks-into-issues)
You can also convert tasks into issues. First, hover over one of the items in your tasklist and then click 
![Screenshot of an issue showing two tasks. The "Convert to issue" icon is highlighted with an orange outline.](https://docs.github.com/assets/cb-26453/images/help/writing/convert-task-lists-into-issues.png)
## [Navigating tracked issues](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/about-tasklists#navigating-tracked-issues)
Any issues that are referenced in a tasklist specify that they are tracked by the issue that contains the tasklist. To navigate to the tracking issue from the tracked issue, click on the tracking issue number in the **Tracked by** section next to the issue status.
![Screenshot of issue 3 showing the issue status of "Open" and the text "Tracked by issue #2", which is outlined in orange.](https://docs.github.com/assets/cb-111881/images/help/writing/task-list-tracked.png)
