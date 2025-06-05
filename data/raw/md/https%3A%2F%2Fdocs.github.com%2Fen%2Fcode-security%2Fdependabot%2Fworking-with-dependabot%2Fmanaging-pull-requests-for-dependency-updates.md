  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Dependabot](https://docs.github.com/en/code-security/dependabot "Dependabot")/
  * [Work with Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot "Work with Dependabot")/
  * [Manage Dependabot PRs](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/managing-pull-requests-for-dependency-updates "Manage Dependabot PRs")


# Managing pull requests for dependency updates
You manage pull requests raised by Dependabot in much the same way as other pull requests, but there are some extra options.
## Who can use this feature?
Users with **write** access
## In this article
  * [About Dependabot pull requests](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/managing-pull-requests-for-dependency-updates#about-dependabot-pull-requests)
  * [Viewing Dependabot pull requests](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/managing-pull-requests-for-dependency-updates#viewing-dependabot-pull-requests)
  * [Changing the rebase strategy for Dependabot pull requests](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/managing-pull-requests-for-dependency-updates#changing-the-rebase-strategy-for-dependabot-pull-requests)
  * [Allowing Dependabot to rebase and force push over extra commits](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/managing-pull-requests-for-dependency-updates#allowing-dependabot-to-rebase-and-force-push-over-extra-commits)
  * [Managing Dependabot pull requests with comment commands](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/managing-pull-requests-for-dependency-updates#managing-dependabot-pull-requests-with-comment-commands)


## [About Dependabot pull requests](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/managing-pull-requests-for-dependency-updates#about-dependabot-pull-requests)
Dependabot raises pull requests to update dependencies. Depending on how your repository is configured, Dependabot may raise pull requests for version updates and/or for security updates. You manage these pull requests in the same way as any other pull request, but there are also some extra commands available. For information about enabling Dependabot dependency updates, see [Configuring Dependabot security updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates) and [Configuring Dependabot version updates](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuring-dependabot-version-updates).
When Dependabot raises a pull request, you're notified by your chosen method for the repository. Each pull request contains detailed information about the proposed change, taken from the package manager. These pull requests follow the normal checks and tests defined in your repository. In addition, where enough information is available, you'll see a compatibility score. This may also help you decide whether or not to merge the change. For information about this score, see [About Dependabot security updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates).
If you have many dependencies to manage, you may want to customize the configuration for each package manager so that pull requests have specific reviewers, assignees, and labels. You may also want to group sets of dependencies together, so that multiple dependencies are updated in a single pull request. For more information, see [Customizing Dependabot pull requests to fit your processes](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/customizing-dependabot-prs) and [Configuring Dependabot security updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates#grouping-dependabot-updates-into-a-single-pull-request).
If you don't interact with Dependabot pull requests for a repository during a 90-day time period, Dependabot considers your repository as inactive, and will automatically pause Dependabot updates. For more information about inactivity criteria, see [About Dependabot version updates](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/about-dependabot-version-updates#about-automatic-deactivation-of-dependabot-updates) and [About Dependabot security updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates#about-automatic-deactivation-of-dependabot-updates).
## [Viewing Dependabot pull requests](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/managing-pull-requests-for-dependency-updates#viewing-dependabot-pull-requests)
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the main page of a repository. In the horizontal navigation bar, a tab, labeled "Pull requests," is outlined in dark orange.](https://docs.github.com/assets/cb-51156/images/help/repository/repo-tabs-pull-requests-global-nav-update.png)
  3. Any pull requests for security or version updates are easy to identify.
     * The author is [dependabot](https://github.com/dependabot), the bot account used by Dependabot.
     * By default, they have the `dependencies` label.


## [Changing the rebase strategy for Dependabot pull requests](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/managing-pull-requests-for-dependency-updates#changing-the-rebase-strategy-for-dependabot-pull-requests)
By default, Dependabot automatically rebases pull requests to resolve any conflicts. If a pull request has not been merged for 30 days, Dependabot will stop rebasing the pull request. You can still manually rebase and merge the pull request. If you'd prefer to handle merge conflicts manually, you can disable this using the `rebase-strategy` option. For details, see [Dependabot options reference](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference#rebase-strategy).
## [Allowing Dependabot to rebase and force push over extra commits](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/managing-pull-requests-for-dependency-updates#allowing-dependabot-to-rebase-and-force-push-over-extra-commits)
By default, Dependabot will stop rebasing a pull request once extra commits have been pushed to it. To allow Dependabot to force push over commits added to its branches, include any of the following strings: `[dependabot skip]` , `[skip dependabot]`, `[dependabot-skip]`, or `[skip-dependabot]`, in either lower or uppercase, to the commit message.
## [Managing Dependabot pull requests with comment commands](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/managing-pull-requests-for-dependency-updates#managing-dependabot-pull-requests-with-comment-commands)
Dependabot responds to simple commands in comments. Each pull request contains details of the commands you can use to process the pull request (for example: to merge, squash, reopen, close, or rebase the pull request) under the "Dependabot commands and options" section. The aim is to make it as easy as possible for you to triage these automatically generated pull requests.
You can use any of the following commands on a Dependabot pull request.
  * `@dependabot cancel merge` cancels a previously requested merge.
  * `@dependabot close` closes the pull request and prevents Dependabot from recreating that pull request. You can achieve the same result by closing the pull request manually.
  * `@dependabot ignore this dependency` closes the pull request and prevents Dependabot from creating any more pull requests for this dependency (unless you reopen the pull request or upgrade to the suggested version of the dependency yourself).
  * `@dependabot ignore this major version` closes the pull request and prevents Dependabot from creating any more pull requests for this major version (unless you reopen the pull request or upgrade to this major version yourself).
  * `@dependabot ignore this minor version` closes the pull request and prevents Dependabot from creating any more pull requests for this minor version (unless you reopen the pull request or upgrade to this minor version yourself).
  * `@dependabot ignore this patch version` closes the pull request and prevents Dependabot from creating any more pull requests for this patch version (unless you reopen the pull request or upgrade to this patch version yourself).
  * `@dependabot merge` merges the pull request once your CI tests have passed.
  * `@dependabot rebase` rebases the pull request.
  * `@dependabot recreate` recreates the pull request, overwriting any edits that have been made to the pull request.
  * `@dependabot reopen` reopens the pull request if the pull request is closed.
  * `@dependabot show DEPENDENCY_NAME ignore conditions` retrieves information on the ignore conditions for the specified dependency, and comments on the pull request with a table that displays all ignore conditions for the dependency. For example, `@dependabot show express ignore conditions` would find all `ignore` conditions stored for the Express dependency, and comment on the pull request with that information.
  * `@dependabot squash and merge` squashes and merges the pull request once your CI tests have passed.


Dependabot will react with a "thumbs up" emoji to acknowledge the command, and may respond with a comment on the pull request. While Dependabot usually responds quickly, some commands may take several minutes to complete if Dependabot is busy processing other updates or commands.
If you run any of the commands for ignoring dependencies or versions, Dependabot stores the preferences for the repository centrally. While this is a quick solution, for repositories with more than one contributor it is better to explicitly define the dependencies and versions to ignore in the configuration file. This makes it easy for all contributors to see why a particular dependency isn't being updated automatically.
For more information, see [Dependabot options reference](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference#ignore).
### [Managing Dependabot pull requests for grouped updates with comment commands](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/managing-pull-requests-for-dependency-updates#managing-dependabot-pull-requests-for-grouped-updates-with-comment-commands)
In Dependabot pull requests for grouped version updates and security updates, you can use comment commands to ignore and un-ignore updates for specific dependencies and versions. You can use any of the following commands to manage ignore conditions for grouped updates.
  * `@dependabot ignore DEPENDENCY_NAME` closes the pull request and prevents Dependabot from updating this dependency.
  * `@dependabot ignore DEPENDENCY_NAME major version` closes the pull request and prevents Dependabot from updating this dependency's major version.
  * `@dependabot ignore DEPENDENCY_NAME minor version` closes the pull request and prevents Dependabot from updating this dependency's minor version.
  * `@dependabot ignore DEPENDENCY_NAME patch version` closes the pull request and prevents Dependabot from updating this dependency's patch version.
  * `@dependabot unignore *` closes the current pull request, clears all `ignore` conditions stored for all dependencies in the group, then opens a new pull request.
  * `@dependabot unignore DEPENDENCY_NAME` closes the current pull request, clears all `ignore` conditions stored for the dependency, then opens a new pull request that includes available updates for the specified dependency. For example, `@dependabot unignore lodash` would open a new pull request that includes updates for the Lodash dependency.
  * `@dependabot unignore DEPENDENCY_NAME IGNORE_CONDITION` closes the current pull request, clears the stored `ignore` condition, then opens a new pull request that includes available updates for the specified ignore condition. For example, `@dependabot unignore express [< 1.9, > 1.8.0]` would open a new pull request that includes updates for Express between versions 1.8.0 and 1.9.0.


When you want to un-ignore a specific ignore condition, use the `@dependabot show DEPENDENCY_NAME ignore conditions` command to quickly check what ignore conditions a dependency currently has.
