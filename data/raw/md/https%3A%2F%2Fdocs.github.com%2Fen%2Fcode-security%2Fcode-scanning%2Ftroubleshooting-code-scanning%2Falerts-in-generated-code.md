  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Troubleshooting code scanning](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning "Troubleshooting code scanning")/
  * [Alerts in generated code](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/alerts-in-generated-code "Alerts in generated code")


# Alerts found in generated code
When analyzing your code with code scanning, you may wish to build only the code which you wish to analyze.
For compiled languages like Java, Kotlin, Go, C, C++, and C#, CodeQL analyzes all of the code which was built during the workflow run. To limit the amount of code being analyzed, build only the code which you wish to analyze by specifying your own build steps in a `run` block. You can combine specifying your own build steps with using the `paths` or `paths-ignore` filters on the `pull_request` and `push` events to ensure that your workflow only runs when specific code is changed. For more information, see [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onpushpull_requestpull_request_targetpathspaths-ignore).
For languages like JavaScript, Python, and TypeScript, that CodeQL analyzes without compiling the source code, you can specify additional configuration options to limit the amount of code to analyze. For more information, see [Customizing your advanced setup for code scanning](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/customizing-your-advanced-setup-for-code-scanning#specifying-directories-to-scan).
