  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Dependabot](https://docs.github.com/en/code-security/dependabot "Dependabot")/
  * [Dependabot auto-triage rules](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules "Dependabot auto-triage rules")/
  * [Manage auto-dismissed alerts](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/managing-automatically-dismissed-alerts "Manage auto-dismissed alerts")


# Managing alerts that have been automatically dismissed by a Dependabot auto-triage rule
You can filter to see which alerts have been auto-dismissed by a rule, and you can reopen dismissed alerts.
## Who can use this feature?
  * Organization owners
  * Security managers
  * Users with **admin** access (can enable, disable, and view auto-triage rules for the repository, as well as create custom auto-triage rules)


## [Managing automatically dismissed alerts](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/managing-automatically-dismissed-alerts#managing-automatically-dismissed-alerts)
The Dependabot alerts page defaults to showing open alerts. To filter and view auto-dismissed alerts, you must first clear the `is:open` default filter from the view.
  1. On GitHub, navigate to the main page of the repository.
  2. Under the repository name, click **Security**. 
![Screenshot of a repository header showing the tabs. The "Security" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-17801/images/help/repository/security-tab.png)
  3. To filter to see all closed alerts, click `is:closed` filter query in the search bar.
![Screenshot of the "Dependabot Alerts" page. A button, labelled "Closed" is highlighted with an orange outline.](https://docs.github.com/assets/cb-32784/images/help/repository/dependabot-alerts-closed-tab.png)
  4. To see all auto-dismissed alerts, select **Closed as** , then in the dropdown menu, click **Auto-dismissed**.
![Screenshot of the "Dependabot Alerts" page. A button, labelled "Closed as" is highlighted with an orange outline.](https://docs.github.com/assets/cb-60043/images/help/repository/dependabot-alerts-closed-as.png)
  5. To reopen an auto-dismissed alert, to the left of the alert title, click the checkbox adjacent to the alert, then click **Reopen**.
![Screenshot of an alert title on the "Dependabot Alerts" page. To the left of the alert, a checkbox is highlighted in an orange outline.](https://docs.github.com/assets/cb-29409/images/help/repository/dependabot-reopen-closed-alert.png)


