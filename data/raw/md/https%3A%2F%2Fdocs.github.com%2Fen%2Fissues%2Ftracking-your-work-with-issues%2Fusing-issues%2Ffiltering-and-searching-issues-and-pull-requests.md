  * [GitHub Issues](https://docs.github.com/en/issues "GitHub Issues")/
  * [Issues](https://docs.github.com/en/issues/tracking-your-work-with-issues "Issues")/
  * [Using issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues "Using issues")/
  * [Filter and search](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests "Filter and search")


# Filtering and searching issues and pull requests
To find detailed information about a repository on GitHub, you can filter, sort, and search issues and pull requests that are relevant to the repository.
## Tool navigation
  * [GitHub CLI](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests?tool=cli)
  * [Web browser](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests?tool=webui)


## In this article
  * [Filtering issues and pull requests](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests#filtering-issues-and-pull-requests)
  * [Building advanced filters for issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests#building-advanced-filters-for-issues)
  * [Filtering issues and pull requests by assignees](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests#filtering-issues-and-pull-requests-by-assignees)
  * [Filtering issues and pull requests by labels](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests#filtering-issues-and-pull-requests-by-labels)
  * [Filtering by issue type](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests#filtering-by-issue-type)
  * [Filtering pull requests by review status](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests#filtering-pull-requests-by-review-status)
  * [Using search to filter issues and pull requests](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests#using-search-to-filter-issues-and-pull-requests)
  * [Sorting issues and pull requests](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests#sorting-issues-and-pull-requests)
  * [Sharing filters](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests#sharing-filters)
  * [Further reading](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests#further-reading)


You can also filter issues or pull requests using the GitHub CLI. For more information, see [`gh issue list`](https://cli.github.com/manual/gh_issue_list) or [`gh pr list`](https://cli.github.com/manual/gh_pr_list) in the GitHub CLI documentation.
## [Filtering issues and pull requests](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests#filtering-issues-and-pull-requests)
Issues and pull requests come with a set of default filters you can apply to organize your listings.
You can filter issues and pull requests to find:
  * All open issues and pull requests
  * Issues and pull requests that you've created
  * Issues and pull requests that are assigned to you
  * Issues and pull requests where you're [**@mentioned**](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#mentioning-people-and-teams)


You can also filter issues or pull requests using the GitHub CLI. For more information, see [`gh issue list`](https://cli.github.com/manual/gh_issue_list) or [`gh pr list`](https://cli.github.com/manual/gh_pr_list) in the GitHub CLI documentation.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the main page of a repository. In the horizontal navigation bar, the "Issues" and "Pull requests" tabs are outlined in orange.](https://docs.github.com/assets/cb-51787/images/help/repository/repo-settings-issues-pull-requests-global-nav-update.png)
  3. Above the list, select the **Filters** dropdown menu, then click the type of filter you're interested in.
![Screenshot of the list of issues for a repository. Above the list, a dropdown menu, labeled "Filters", is outlined in dark orange.](https://docs.github.com/assets/cb-49430/images/help/issues/issues-filter-dropdown.png)


## [Building advanced filters for issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests#building-advanced-filters-for-issues)
You can build advanced filters using boolean and nested queries on your repository's issues page and the issues dashboard. As you type your filter, GitHub will show available qualifiers, suggest values, and warn when there is a problem with your filter.
### [Using boolean operators](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests#using-boolean-operators)
You can use `AND` and `OR` operators to refine your filters.
Use `AND` when you need results where both statements are true. In the example filter below, the results will be comprised of issues with the "question" label that are assigned to the @octocat user.
```
label:"question" AND assignee:octocat

```

To return results where either statement is true, use `OR`. In the example below, the results will contain issues assigned to either @octocat or @hubot.
```
assignee:octocat OR assignee:hubot

```

If you choose not to use `AND` and `OR` operators, GitHub will treat a space between statements as an `AND` operator.
### [Using parentheses for more complicated filters](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests#using-parentheses-for-more-complicated-filters)
You can also use parentheses to nest filters and group qualifiers. In the example below, the results will contain issues that are either assigned to @octocat with the "bug" issue type or assigned to @hubot with the "Feature" issue type.
```
(type:"Bug" AND assignee:octocat) OR (type:"Feature" AND assignee:hubot)

```

You can nest filters using parentheses up to five levels deep.
## [Filtering issues and pull requests by assignees](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests#filtering-issues-and-pull-requests-by-assignees)
Once you've [assigned an issue or pull request to someone](https://docs.github.com/en/issues/tracking-your-work-with-issues/assigning-issues-and-pull-requests-to-other-github-users), you can find items based on who's working on them.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the main page of a repository. In the horizontal navigation bar, the "Issues" and "Pull requests" tabs are outlined in orange.](https://docs.github.com/assets/cb-51787/images/help/repository/repo-settings-issues-pull-requests-global-nav-update.png)
  3. Above the list of issues or pull requests, select the **Assignee** dropdown menu.
![Screenshot of a list of issues. In the header above the list, a dropdown menu, labeled "Assignees", is outlined in dark orange.](https://docs.github.com/assets/cb-49381/images/help/issues/issues-assignee-dropdown.png)
  4. The Assignee drop-down menu lists everyone who has write access to your repository. Click the name of the person whose assigned items you want to see, or click **Assigned to nobody** to see which issues are unassigned.


To clear your filter selection, click **Clear current search query, filters, and sorts**.
## [Filtering issues and pull requests by labels](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests#filtering-issues-and-pull-requests-by-labels)
Once you've [applied labels to an issue or pull request](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels), you can find items based on their labels.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the main page of a repository. In the horizontal navigation bar, the "Issues" and "Pull requests" tabs are outlined in orange.](https://docs.github.com/assets/cb-51787/images/help/repository/repo-settings-issues-pull-requests-global-nav-update.png)
  3. Above the list of issues or pull requests, click **Labels**.
![Screenshot of the list of issues for a repository. Above the list, a button, labeled with a label icon and "Labels", is outlined in dark orange.](https://docs.github.com/assets/cb-49625/images/help/issues/issues-labels-button.png)
  4. In the list of labels, click a label.


To clear your filter selection, click **Clear current search query, filters, and sorts**.
## [Filtering by issue type](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests#filtering-by-issue-type)
If your organization uses issue types, you can filter issues for a particular type. You can also type the `type:` qualifier directly into your filter.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the main page of a repository. In the horizontal navigation bar, a tab, labeled "Issues," is outlined in dark orange.](https://docs.github.com/assets/cb-51267/images/help/repository/repo-tabs-issues-global-nav-update.png)
  3. Above the list of issues, select the **Types** dropdown menu.
![Screenshot of a list of issues. In the list header, the "Types" filter is outlined in orange and expanded.](https://docs.github.com/assets/cb-32818/images/help/issues/issue-type-dropdown.png)
  4. In the list of type, click an issue type.


## [Filtering pull requests by review status](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests#filtering-pull-requests-by-review-status)
You can use filters to list pull requests by review status and to find pull requests that you've reviewed or other people have asked you to review.
You can filter a repository's list of pull requests to find:
  * Pull requests that haven't been [reviewed](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews) yet
  * Pull requests that [require a review](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches#require-pull-request-reviews-before-merging) before they can be merged
  * Pull requests that a reviewer has approved
  * Pull requests in which a reviewer has asked for changes
  * Pull requests that you have reviewed
  * Pull requests that someone has asked you directly to review
  * Pull requests that [someone has asked you, or a team you're a member of, to review](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/requesting-a-pull-request-review)


  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the main page of a repository. In the horizontal navigation bar, a tab, labeled "Pull requests," is outlined in dark orange.](https://docs.github.com/assets/cb-51156/images/help/repository/repo-tabs-pull-requests-global-nav-update.png)
  3. In the upper-right corner, select the **Reviews** dropdown menu.
![Screenshot of the filter menu above the list of pull requests. The "Reviews" dropdown is outlined in dark orange.](https://docs.github.com/assets/cb-46801/images/help/pull_requests/reviews-filter-dropdown.png)
  4. Choose a filter to find all of the pull requests with that filter's status.


## [Using search to filter issues and pull requests](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests#using-search-to-filter-issues-and-pull-requests)
You can use filters to search for issues and pull requests that meet specific criteria.
### [Searching for issues and pull requests](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests#searching-for-issues-and-pull-requests)
The issues and pull requests search bar allows you to define your own custom filters and sort by a wide variety of criteria. You can find the search bar on each repository's **Issues** and **Pull requests** tabs and on your [Issues and Pull requests dashboards](https://docs.github.com/en/issues/tracking-your-work-with-issues/viewing-all-of-your-issues-and-pull-requests).
![Screenshot of the list of issues for a repository. Above the list, a search field, containing the query "is:issue is:open", is outlined in orange.](https://docs.github.com/assets/cb-50768/images/help/issues/issues-search-bar.png)
You can focus your cursor on the search bar above the issue or pull request list with a keyboard shortcut. For more information, see [Keyboard shortcuts](https://docs.github.com/en/get-started/accessibility/keyboard-shortcuts#issue-and-pull-request-lists).
To learn more about GitHub CLI, see [About GitHub CLI](https://docs.github.com/en/github-cli/github-cli/about-github-cli).
You can use the GitHub CLI to search for issues or pull requests. Use the `gh issue list` or `gh pr list` subcommand along with the `--search` argument and a search query.
For example, you can list, in order of date created, all issues that have no assignee and that have the label `help wanted` or `bug`.
```
gh issue list --search 'no:assignee label:"help wanted",bug sort:created-asc'

```

You can also list all pull requests that mention the `octo-org/octo-team` team.
```
gh pr list --search "team:octo-org/octo-team"

```

### [About search terms](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests#about-search-terms)
With issue and pull request search terms, you can:
  * Filter issues and pull requests by author: `state:open type:issue author:octocat`
  * Filter issues and pull requests that involve, but don't necessarily [**@mention**](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#mentioning-people-and-teams), certain people: `state:open type:issue involves:octocat`
  * Filter issues and pull requests by assignee: `state:open type:issue assignee:octocat`
  * Filter issues and pull requests by label: `state:open type:issue label:"bug"`
  * Filter out search terms by using `-` before the term: `state:open type:issue -author:octocat`


You can filter issues and pull requests by label using logical OR or using logical AND.
  * To filter issues using logical OR, use the comma syntax: `label:"bug","wip"`.
  * To filter issues using logical AND, use separate label filters: `label:"bug" label:"wip"`.


For issues, you can also use search to:
  * Filter for issues that are linked to a pull request by a closing reference: `linked:pr`
  * Filter issues by the reason they were closed: `is:closed reason:completed` or `is:closed reason:"not planned"`
  * Filter for issues with a particular type: `is:open type:"Bug"`
  * Filter for issues from repositories [**owned**](https://docs.github.com/en/search-github/searching-on-github/searching-issues-and-pull-requests#search-within-a-users-or-organizations-repositories) by a certain user or organization, limited to up to 16 `user` and `org` qualifiers with no limit on `repo` qualifiers: `state:open type:issue org:github OR user:octocat`


For pull requests, you can also use search to:
  * Filter [draft](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests#draft-pull-requests) pull requests: `is:draft`
  * Filter pull requests that haven't been [reviewed](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews) yet: `state:open type:pr review:none`
  * Filter pull requests that [require a review](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches#require-pull-request-reviews-before-merging) before they can be merged: `state:open type:pr review:required`
  * Filter pull requests that a reviewer has approved: `state:open type:pr review:approved`
  * Filter pull requests in which a reviewer has asked for changes: `state:open type:pr review:changes_requested`
  * Filter pull requests by [reviewer](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews): `state:open type:pr reviewed-by:octocat`
  * Filter pull requests by the specific user [requested for review](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/requesting-a-pull-request-review): `state:open type:pr review-requested:octocat`
  * Filter pull requests that someone has asked you directly to review: `state:open type:pr user-review-requested:@me`
  * Filter pull requests by the team requested for review: `state:open type:pr team-review-requested:github/docs`
  * Filter for pull requests that are linked to an issue that the pull request may close: `linked:issue`
  * Filter pull requests by state of [merging](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges): `is:merged` or `is:unmerged`


## [Sorting issues and pull requests](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests#sorting-issues-and-pull-requests)
Filters can be sorted to provide better information during a specific time period.
You can sort any filtered view by:
  * The newest created issues or pull requests
  * The oldest created issues or pull requests
  * The most commented issues or pull requests
  * The least commented issues or pull requests
  * The newest updated issues or pull requests
  * The oldest updated issues or pull requests
  * The most added reaction on issues or pull requests


  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the main page of a repository. In the horizontal navigation bar, the "Issues" and "Pull requests" tabs are outlined in orange.](https://docs.github.com/assets/cb-51787/images/help/repository/repo-settings-issues-pull-requests-global-nav-update.png)
  3. Above the list of issues or pull requests, select the **Sort** dropdown menu, then click a sort method.
![Screenshot of the list of issues for a repository. Above the list, a dropdown menu, labeled "Sort," is outlined in dark orange.](https://docs.github.com/assets/cb-49361/images/help/issues/issues-sort-dropdown.png)


To clear your sort selection, click **Sort** > **Newest**.
## [Sharing filters](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests#sharing-filters)
When you filter or sort issues and pull requests, your browser's URL is automatically updated to match the new view.
You can send the URL that issues generates to any user, and they'll be able to see the same filter view that you see.
For example, if you filter on issues assigned to Hubot, and sort on the oldest open issues, your URL would update to something like the following:
```
/issues?q=state:open+type:issue+assignee:hubot+sort:created-asc

```

## [Further reading](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests#further-reading)
  * [Searching issues and pull requests](https://docs.github.com/en/search-github/searching-on-github/searching-issues-and-pull-requests)


