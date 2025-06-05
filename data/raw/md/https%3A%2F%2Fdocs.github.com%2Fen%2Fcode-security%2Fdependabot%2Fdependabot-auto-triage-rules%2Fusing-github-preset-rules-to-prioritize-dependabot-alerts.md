  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Dependabot](https://docs.github.com/en/code-security/dependabot "Dependabot")/
  * [Dependabot auto-triage rules](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules "Dependabot auto-triage rules")/
  * [GitHub preset rules](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/using-github-preset-rules-to-prioritize-dependabot-alerts "GitHub preset rules")


# Using GitHub preset rules to prioritize Dependabot alerts
You can use GitHub presets, which are rules curated by GitHub, to auto-dismiss low impact development alerts for npm dependencies.
## Who can use this feature?
  * Organization owners
  * Security managers
  * Users with **admin** access (can enable, disable, and view GitHub presets for the repository)


## In this article
  * [About GitHub presets](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/using-github-preset-rules-to-prioritize-dependabot-alerts#about-github-presets)
  * [Enabling the Dismiss low impact issues for development-scoped dependencies rule for your private repository](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/using-github-preset-rules-to-prioritize-dependabot-alerts#enabling-the-dismiss-low-impact-issues-for-development-scoped-dependencies-rule-for-your-private-repository)
  * [Publicly disclosed CWEs used by the Dismiss low impact issues for development-scoped dependencies rule](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/using-github-preset-rules-to-prioritize-dependabot-alerts#publicly-disclosed-cwes-used-by-the-dismiss-low-impact-issues-for-development-scoped-dependencies-rule)


## [About GitHub presets](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/using-github-preset-rules-to-prioritize-dependabot-alerts#about-github-presets)
The `Dismiss low impact issues for development-scoped dependencies` rule is a GitHub preset that auto-dismisses certain types of vulnerabilities that are found in npm dependencies used in development. These alerts cover cases that feel like false alarms to most developers as the associated vulnerabilities:
  * Are unlikely to be exploitable in a developer (non-production or runtime) environment.
  * May relate to resource management, programming and logic, and information disclosure issues.
  * At worst, have limited effects like slow builds or long-running tests.
  * Are not indicative of issues in production.


Automatic dismissal of low impact development alerts is currently only supported for npm.
The `Dismiss low impact issues for development-scoped dependencies` rule includes vulnerabilities relating to resource management, programming and logic, and information disclosure issues. For more information, see [Publicly disclosed CWEs used by the `Dismiss low impact issues for development-scoped dependencies` rule](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/using-github-preset-rules-to-prioritize-dependabot-alerts#publicly-disclosed-cwes-used-by-the-dismiss-low-impact-issues-for-development-scoped-dependencies-rule).
Filtering out these low impact alerts allows you to focus on alerts that matter to you, without having to worry about missing potentially high-risk development-scoped alerts.
The `Dismiss low impact issues for development-scoped dependencies` rule is enabled by default on public repositories and disabled for private repositories. Administrators of private repositories can opt in by enabling the rule for their repository.
## [Enabling the `Dismiss low impact issues for development-scoped dependencies` rule for your private repository](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/using-github-preset-rules-to-prioritize-dependabot-alerts#enabling-the-dismiss-low-impact-issues-for-development-scoped-dependencies-rule-for-your-private-repository)
You first need to enable Dependabot alerts for the repository. For more information, see [Configuring Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/configuring-dependabot-alerts#managing-dependabot-alerts-for-your-repository).
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Security" section of the sidebar, click 
  4. Under "Dependabot alerts", click 
![Screenshot of the "Advanced Security" page for a repository. The gear icon is highlighted with an orange outline.](https://docs.github.com/assets/cb-38693/images/help/repository/dependabot-rules-page.png)
  5. Under "GitHub presets", to the right of "Dismiss low impact issues for development-scoped dependencies", click 
  6. Under "State", select the dropdown menu, then click "Enabled".
  7. Click **Save rule**.


## [Publicly disclosed CWEs used by the `Dismiss low impact issues for development-scoped dependencies` rule](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/using-github-preset-rules-to-prioritize-dependabot-alerts#publicly-disclosed-cwes-used-by-the-dismiss-low-impact-issues-for-development-scoped-dependencies-rule)
Along with the `ecosystem:npm` and `scope:development` alert metadata, we use the following GitHub-curated Common Weakness Enumerations (CWEs) to filter out low impact alerts for the `Dismiss low impact issues for development-scoped dependencies` rule. We regularly improve this list and vulnerability patterns covered by built-in rules.
### [Resource Management Issues](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/using-github-preset-rules-to-prioritize-dependabot-alerts#resource-management-issues)
  * CWE-400 Uncontrolled Resource Consumption
  * CWE-770 Allocation of Resources Without Limits or Throttling
  * CWE-409 Improper Handling of Highly Compressed Data (Data Amplification)
  * CWE-908 Use of Uninitialized Resource
  * CWE-1333 Inefficient Regular Expression Complexity
  * CWE-835 Loop with Unreachable Exit Condition ('Infinite Loop')
  * CWE-674 Uncontrolled Recursion
  * CWE-1119 Excessive Use of Unconditional Branching


### [Programming and Logic Errors](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/using-github-preset-rules-to-prioritize-dependabot-alerts#programming-and-logic-errors)
  * CWE-185 Incorrect Regular Expression
  * CWE-754 Improper Check for Unusual or Exceptional Conditions
  * CWE-755 Improper Handling of Exceptional Conditions
  * CWE-248 Uncaught Exception
  * CWE-252 Unchecked Return Value
  * CWE-391 Unchecked Error Condition
  * CWE-696 Incorrect Behavior Order
  * CWE-1254 Incorrect Comparison Logic Granularity
  * CWE-665 Improper Initialization
  * CWE-703 Improper Check or Handling of Exceptional Conditions
  * CWE-178 Improper Handling of Case Sensitivity


### [Information Disclosure Issues](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/using-github-preset-rules-to-prioritize-dependabot-alerts#information-disclosure-issues)
  * CWE-544 Missing Standardized Error Handling Mechanism
  * CWE-377 Insecure Temporary File
  * CWE-451 User Interface (UI) Misrepresentation of Critical Information
  * CWE-668 Exposure of Resource to Wrong Sphere


