  * [GitHub Issues](https://docs.github.com/en/issues "GitHub Issues")/
  * [Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects "Projects")/
  * [Understanding fields](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields "Understanding fields")/
  * [About sub-issue fields](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-parent-issue-and-sub-issue-progress-fields "About sub-issue fields")


# About parent issue and sub-issue progress fields
You can show an issue's parent issue and view sub-issue progress in your projects.
## In this article
  * [Enabling the Parent issue field](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-parent-issue-and-sub-issue-progress-fields#enabling-the-parent-issue-field)
  * [Enabling the Sub-issue progress](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-parent-issue-and-sub-issue-progress-fields#enabling-the-sub-issue-progress)


If your organization uses sub-issues, you can enable the "Parent issue" and "Sub-issue progress" fields on your projects to see the relationships between your issues and the progress made on those issues.
The "Parent issue" field can be used to group items, allowing you to create views that break down your work using the sub-issue hierarchies you have created. For more about grouping views, see [Changing the layout of a view](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/changing-the-layout-of-a-view#grouping-by-field-values-in-table-layout).
You can also filter by the "Parent issue" field to only display items that are sub-issues of a particular issue. You can start by typing "parent-issue" and then selecting an issue from the list. Or, if you know the repository and issue number, you can type the filter in full:
```
parent-issue:"<OWNER>/<REPO>#<ISSUE NUMBER>"

```

To use the filter, replace `<OWNER>` with the repository owner, `<REPO>` with the repository name, and `<ISSUE NUMBER>` with the issue number. See [Filtering projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects).
## [Enabling the Parent issue field](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-parent-issue-and-sub-issue-progress-fields#enabling-the-parent-issue-field)
You can enable the "Parent issue" field to see which parent issues the issues in your project belong to.
  1. In table view, in the rightmost field header, click 
![Screenshot of a project. The "Add field" button, indicated by a plus icon, is highlighted with an orange outline.](https://docs.github.com/assets/cb-6180/images/help/projects-v2/new-field-button.png)
  2. Under "Hidden fields", click **Parent issue**.


## [Enabling the Sub-issue progress](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-parent-issue-and-sub-issue-progress-fields#enabling-the-sub-issue-progress)
You can enable the "Sub-issue progress" field to see how many sub-issues have been completed.
  1. In table view, in the rightmost field header, click 
![Screenshot of a project. The "Add field" button, indicated by a plus icon, is highlighted with an orange outline.](https://docs.github.com/assets/cb-6180/images/help/projects-v2/new-field-button.png)
  2. Under "Hidden fields", click **Sub-issue progress**.


