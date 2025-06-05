  * [GitHub Issues](https://docs.github.com/en/issues "GitHub Issues")/
  * [Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects "Projects")/
  * [Customizing views](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project "Customizing views")/
  * [Filtering projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects "Filtering projects")


# Filtering projects
Use filters to choose which items appear in your project's views.
## In this article
  * [Filtering for fields](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects#filtering-for-fields)
  * [Combining filters](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects#combining-filters)
  * [Negating a filter](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects#negating-a-filter)
  * [Filtering for items that have a value](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects#filtering-for-items-that-have-a-value)
  * [Filtering for items that are missing a value](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects#filtering-for-items-that-are-missing-a-value)
  * [Filtering by item location](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects#filtering-by-item-location)
  * [Filtering for item state or item type](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects#filtering-for-item-state-or-item-type)
  * [Filtering by close reason](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects#filtering-by-close-reason)
  * [Filtering for when an item was last updated](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects#filtering-for-when-an-item-was-last-updated)
  * [Filtering number, date, and iteration fields](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects#filtering-number-date-and-iteration-fields)
  * [Filtering assignees and reviewers using keywords](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects#filtering-assignees-and-reviewers-using-keywords)
  * [Filtering iteration and date fields using keywords](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects#filtering-iteration-and-date-fields-using-keywords)
  * [Filtering by text fields](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects#filtering-by-text-fields)
  * [Filtering by issue type](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects#filtering-by-issue-type)
  * [Filtering by parent issue](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects#filtering-by-parent-issue)


You can customize which items appear in your views using filters for item metadata, such as assignees and the labels applied to issues, and by the fields in your project. You can combine filters and save them as views. For more information, see [Managing your views](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/managing-your-views).
To filter a view, click `Command`+`K` (Mac) or `Ctrl`+`K` (Windows/Linux), and type "Filter by" to choose from the available filters.
![Screenshot of "Mona's project". A field labeled "Filter by keyword or by field" is highlighted with an orange outline.](https://docs.github.com/assets/cb-13029/images/help/projects-v2/filter-example.png)
In board layout, you can click on item data to filter for items with that value. For example, click on an assignee to show only items for that assignee. To remove the filter, click the item data again.
Using multiple filters will act as a logical AND filter. For example, `label:bug status:"In progress"` will return items with the `bug` label and the "In progress" status. You can also provide multiple values for the same field to act as a logical OR filter. For example, `label:bug,support` will return items with either the `bug` or `support` labels. Projects does not currently support logical OR filters across multiple fields.
The same filters are available for charts you create using insights for Projects, allowing you to filter the data used to create your charts. For more information, see [About insights for Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/viewing-insights-from-your-project/about-insights-for-projects).
When you filter a view and then add an item, the filtered metadata will be applied to new item. For example, if you're filtering by `status:"In progress"` and you add an item, the new item will have its status set to "In progress."
You can use filters to produce views for very specific purposes. For example, you could use `assignee:@me status:todo last-updated:5days` to create a view of all work assigned to the current user, with the "todo" status, that hasn't been updated in the last five days. You could create a triage view by using a negative filter, such as `no:label no:assignee repo:octocat/game`, which would show items without a label and without an assignee that are located in the `octocat/game` repository.
## [Filtering for fields](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects#filtering-for-fields)
Qualifier | Example  
---|---  
`assignee:_USERNAME_`|  **assignee:octocat** will show items assigned to @octocat.  
`label:_LABEL_`|  **label:bug** will show items with the "bug" label applied.  
`field:_VALUE_`|  **status:done** will show items with the "status" field set to "done."  
`reviewers:_USERNAME_`|  **reviewers:octocat** will show items that have been reviewed by @octocat.  
`milestone:"_MILESTONE_"`|  **milestone:"QA release"** will show items assigned to the "QA release" milestone.  
## [Combining filters](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects#combining-filters)
You can create filters for multiple fields. Your view will show items that match all filters.
Qualifier | Example  
---|---  
`assignee:_USERNAME_ field:_VALUE_`|  **assignee:octocat priority:1** will show items assigned to @octocat that have a priority of **1**.  
You can also filter for multiple values from the same field. If you separate the values with commas, your view will show items that match any of the provided values.
Qualifier | Example  
---|---  
`assignee:_USERNAME_,_USERNAME_`|  **assignee:octocat,stevecat** will show items assigned to either @octocat or @stevecat.  
To filter for multiple values from the same field but show items that match all of the provided values, you can repeat the qualifier for each value.
Qualifier | Example  
---|---  
`assignee:_USERNAME_ assignee:_USERNAME_`|  **assignee:octocat assignee:stevecat** will show items that are assigned to both @octocat and @stevecat.  
You can also combine filters that match some and match all items.
Qualifier | Example  
---|---  
`field:_VALUE_,_VALUE_ assignee:_USER_ assignee:_USER_`|  **label:bug,onboarding assignee:octocat assignee:stevecat** will show items that have either the bug or onboarding labels but are assigned to both @octocat and @stevecat.  
## [Negating a filter](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects#negating-a-filter)
You can invert any filter, including combinations, by prefixing with a hyphen.
Qualifier | Example  
---|---  
`-assignee:_USERNAME_`|  **-assignee:octocat** will not show any items assigned to @octocat.  
`-field:_VALUE_`|  **-status:done** will not show any items with a status of "done."  
`-field:_VALUE,VALUE_`|  **-priority:1,2** will not show any items with a priority of either 1 or 2.  
## [Filtering for items that have a value](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects#filtering-for-items-that-have-a-value)
You can use `has:` to filter for items that have a value
Qualifier | Example  
---|---  
`has:assignee` |  **has:assignee** will show items with an assignee.  
`has:label` |  **has:label** will show items with a label.  
`has:_FIELD_`|  **has:priority** will show items with a priority field value.  
## [Filtering for items that are missing a value](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects#filtering-for-items-that-are-missing-a-value)
You can use `no:` to filter for items that are missing a value
Qualifier | Example  
---|---  
`no:assignee` |  **no:assignee** will show any unassigned items.  
`no:reviewers` |  **no:reviewers** will show pull requests that do not have a reviewer.  
`no:_FIELD_`|  **no:priority** will show items with an empty priority field.  
You can also prefix a hyphen to negate this behavior and only return items that have a value.
Qualifier | Example  
---|---  
`-no:assignee` |  **-no:assignee** will only show items that are assigned.  
`-no:_FIELD_`|  **-no:priority** will only show items that have a value in the priority field.  
## [Filtering by item location](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects#filtering-by-item-location)
Use the `repo` qualifier to filter for items in a particular repository.
Qualifier | Example  
---|---  
`repo:_OWNER/REPO_`|  **repo:octocat/game** will items in the "octocat/game" repository.  
## [Filtering for item state or item type](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects#filtering-for-item-state-or-item-type)
You can use the `is` qualifier to filter for particular types of item or items in particular states.
Qualifier | Example  
---|---  
`is:_STATE_`|  **is:open** will show open issues and pull requests.  
|  **is:closed** will show closed issues and pull requests.  
|  **is:merged** will show any merged pull requests.  
`is:_TYPE_`|  **is:issue** will show only issues.  
|  **is:pr** will show only pull requests.  
|  **is:draft** will show draft issues and draft pull requests.  
|  **is:issue is:open** will show open issues.  
## [Filtering by close reason](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects#filtering-by-close-reason)
You can filter closed items by their close reason.
Qualifier | Example  
---|---  
`reason:_CLOSE REASON_`|  **reason:completed** will show items closed because they were completed.  
|  **reason:"not planned"** will show closed items with the "not planned" reason.  
|  **reason:reopened** will show items that have been reopened after previously being closed.  
## [Filtering for when an item was last updated](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects#filtering-for-when-an-item-was-last-updated)
The `updated` filter field provides a more powerful and flexible way to filter items based on their last modification date.
Qualifier | Example  
---|---  
`updated:_NUMBER_days`|  **updated:@today** will show items updated today.  
|  **updated:@today-1d** will show items updated 1 day ago.  
|  **updated: >@today-1w** will show items last updated seven or more days ago.  
|  **updated: >@today-30d** will show items last updated thirty or more days ago.  
|  **-updated:@today** excludes items updated today.  
GitHub marks an issue or pull request as updated when it is:
  * Created
  * Reopened
  * Edited
  * Commented
  * Labeled
  * Assignees are updated
  * Milestones are updated
  * Transferred to another repository


## [Filtering number, date, and iteration fields](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects#filtering-number-date-and-iteration-fields)
You can use `>`, `>=`, `<`, and `<=` to compare number, date, and iteration fields. Dates should be provided in the `YYYY-MM-DD` format.
Qualifier | Example  
---|---  
`field:>_VALUE_`|  **priority: >1** will show items with a priority greater than 1.  
`field:>=_VALUE_`|  **date: >=2022-06-01** will show items with a date of "2022-06-01" or later.  
`field:<_VALUE_`|  **iteration: <"Iteration 5"** will show items with an iteration before "Iteration 5."  
`field:<=_VALUE_`|  **points: <=10** will show items with 10 or less points.  
You can also use `..` to filter for an inclusive range. When working with a range, `*` can be supplied as a wildcard operator.
Qualifier | Example  
---|---  
`field:_VALUE_.._VALUE_`|  **priority:1..3** will show items with a priority of 1, 2, or 3.  
|  **date:2022-01-01..2022-12-31** will show items from the year 2022.  
|  **points:*..10** will show items with an points value of anything up to and including 10.  
|  **iteration:"Iteration 1..Iteration 4"** will show items in "Iteration 1", "Iteration 2", "Iteration 3", and "Iteration 4."  
## [Filtering assignees and reviewers using keywords](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects#filtering-assignees-and-reviewers-using-keywords)
You can use the `@me` keyword to represent yourself in a filter.
Qualifier | Example  
---|---  
`field:_@me_`|  **assignee:@me** will show items assigned to the signed-in user.  
|  **-reviewers:@me** will show items that have not been reviewed by the signed-in user.  
## [Filtering iteration and date fields using keywords](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects#filtering-iteration-and-date-fields-using-keywords)
You can use the `@previous`, `@current`, and `@next` keywords to filter for iterations relative to the current iteration. You can also use `@today` to filter for the current day.
Qualifier | Example  
---|---  
`field:_@keyword_`|  **iteration:@current** will show items assigned to the current iteration.  
|  **iteration:@next** will show items assigned to the next iteration.  
`field:_@today_`|  **date:@today** will show items with their date set to the current day.  
You can also use `>`, `>=`, `<`, `<=`, `+`, `-`, and `..` ranges with keywords.
Qualifier | Example  
---|---  
`field:_@keyword_.._@keyword_+_n_`|  **iteration:@current..@current+3** will show items assigned to the current iteration and the next three iterations.  
|  **date:@today..@today+7** will show items with a date set to today or the next seven days.  
`field:<_@keyword_`|  **iteration: <@current** will show items assigned to any iteration before the current iteration.  
`field:>=_@keyword_`|  **date: >=@today** will show items with a date set to today or later.  
## [Filtering by text fields](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects#filtering-by-text-fields)
You can filter by specific text fields or use a general text filter across all text fields and titles. When filtering with text that contains spaces or special characters, enclose your text in `"` or `'` quotation marks.
Qualifier | Example  
---|---  
`field:"_TEXT_"`|  **title:"Bug fix"** will show items with titles that exactly match "Bug fix".  
`field:_TEXT_`|  **note:complete** will show items with a note text field that exactly match "complete".  
`_TEXT_`|  **API** will show items with "API" in the title or any other text field.  
`field:_TEXT_ TEXT`|  **label:bug rendering** will show items with the "bug" label and with "rendering" in the title or any other text field.  
For general text search across all text fields and titles, matches are based only on the beginning of a word, not any part of it. For example, if the issue title is **"Document full-text search"** :
  * **Matches** : "Doc", "full", "search"
  * **Doesn't match** : "cument", "ext", "arch"


This approach helps keep general text search more precise and relevant.
You can also use a `*` as a wildcard.
Qualifier | Example  
---|---  
`field:*_TEXT_*`|  **label:*bug*** will show items with a label that contains the word "bug."  
`field:_TEXT_*`|  **title:API*** will show items with a title that begins with "API."  
`field:*_TEXT_`|  **label:*support** will show items with a label that ends with "support."  
## [Filtering by issue type](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects#filtering-by-issue-type)
If your organization uses issue types, you can filter for particular types.
Qualifier | Example  
---|---  
`type:"_ISSUE TYPE_"`|  **type:"bug"** will show issues with the "bug" type.  
## [Filtering by parent issue](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects#filtering-by-parent-issue)
You can filter your sub-issues by their parent issue.
Qualifier | Example  
---|---  
`parent-issue:_OWNER/REPO#ISSUE NUMBER_`|  **parent-issue:octocat/game#4** will show issues with issue #4 in octocat/game as their parent issue.
