  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Dependabot](https://docs.github.com/en/code-security/dependabot "Dependabot")/
  * [Troubleshoot Dependabot](https://docs.github.com/en/code-security/dependabot/troubleshooting-dependabot "Troubleshoot Dependabot")/
  * [Viewing Dependabot logs](https://docs.github.com/en/code-security/dependabot/troubleshooting-dependabot/viewing-dependabot-job-logs "Viewing Dependabot logs")


# Viewing Dependabot job logs
To support debugging of Dependabot pull requests, GitHub provides logs of all Dependabot jobs.
## Who can use this feature?
Users with **write** access
## In this article
  * [About Dependabot job logs](https://docs.github.com/en/code-security/dependabot/troubleshooting-dependabot/viewing-dependabot-job-logs#about-dependabot-job-logs)
  * [Viewing Dependabot job logs](https://docs.github.com/en/code-security/dependabot/troubleshooting-dependabot/viewing-dependabot-job-logs#viewing-dependabot-job-logs)


## [About Dependabot job logs](https://docs.github.com/en/code-security/dependabot/troubleshooting-dependabot/viewing-dependabot-job-logs#about-dependabot-job-logs)
Job logs are only available if Dependabot version updates are enabled for the repository.
Whenever a Dependabot job runs, the details of the job are captured in the job logs list, which is accessible from the dependency graph.
For each manifest file, the job logs record the most recent runs of Dependabot, with each log entry displaying the job type, job ID, timestamp, and, where necessary, a link to the pull request(s) associated with the job.
You may find that the log entry contains a short error message, which can be useful for debugging issues with a particular pull request or run. If you need to troubleshoot further, you can click **view logs** to access the full log files for a specific run.
You will see the following job types recorded in the log list:
  * **Version update** - refers to a Dependabot version updates run.
  * **Security update** - refers to a Dependabot security updates run.
  * **Rebase update** - refers to a run where Dependabot has automatically rebased the pull request to resolve a conflict with the target branch. This update could apply to a pull request from a Dependabot version updates job, or a Dependabot security updates job.


## [Viewing Dependabot job logs](https://docs.github.com/en/code-security/dependabot/troubleshooting-dependabot/viewing-dependabot-job-logs#viewing-dependabot-job-logs)
The Dependabot job logs list is accessible from the dependency graph tab in your repository.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the main page of a repository. In the horizontal navigation bar, a tab, labeled with a graph icon and "Insights," is outlined in orange.](https://docs.github.com/assets/cb-52175/images/help/repository/repo-nav-insights-tab.png)
  3. In the left sidebar, click **Dependency graph**. 
![Screenshot of the "Dependency graph" tab. The tab is highlighted with an orange outline.](https://docs.github.com/assets/cb-3959/images/help/graphs/graphs-sidebar-dependency-graph.png)
  4. Under "Dependency graph", click **Dependabot**.
  5. To the right of the name of manifest file that you're interested in, click **Recent update jobs**.
  6. Optionally, to see the full logs files for a particular job, click **view logs**.
![Screenshot of a Dependabot job log entry for the Gemfile package manager. A button, called "View logs", is highlighted in a dark orange outline.](https://docs.github.com/assets/cb-64050/images/help/dependabot/dependabot-job-logs.png)


