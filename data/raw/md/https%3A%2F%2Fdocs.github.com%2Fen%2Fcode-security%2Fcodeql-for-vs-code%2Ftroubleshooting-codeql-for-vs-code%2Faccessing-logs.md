  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL for VS Code](https://docs.github.com/en/code-security/codeql-for-vs-code "CodeQL for VS Code")/
  * [Troubleshooting CodeQL for VS Code](https://docs.github.com/en/code-security/codeql-for-vs-code/troubleshooting-codeql-for-vs-code "Troubleshooting CodeQL for VS Code")/
  * [Access logs](https://docs.github.com/en/code-security/codeql-for-vs-code/troubleshooting-codeql-for-vs-code/accessing-logs "Access logs")


# Accessing logs
If you need to troubleshoot problems with CodeQL for Visual Studio Code, there are several logs you can access.
## In this article
  * [About logs](https://docs.github.com/en/code-security/codeql-for-vs-code/troubleshooting-codeql-for-vs-code/accessing-logs#about-logs)
  * [Accessing logs](https://docs.github.com/en/code-security/codeql-for-vs-code/troubleshooting-codeql-for-vs-code/accessing-logs#accessing-logs)


## [About logs](https://docs.github.com/en/code-security/codeql-for-vs-code/troubleshooting-codeql-for-vs-code/accessing-logs#about-logs)
Progress and error messages are displayed as notifications in the bottom right corner of the Visual Studio Code workspace. These link to more detailed logs and error messages in the "Output" window.
You can access the following logs:
  * CodeQL Extension
  * CodeQL Language Server
  * CodeQL Query Server
  * CodeQL Tests


The CodeQL Language Server log contains more advanced debug logs for CodeQL language maintainers. You should only need these to provide details in a bug report.
## [Accessing logs](https://docs.github.com/en/code-security/codeql-for-vs-code/troubleshooting-codeql-for-vs-code/accessing-logs#accessing-logs)
  1. In Visual Studio Code, open the "Output" window.
  2. Use the dropdown to select the log view you need. For example, "CodeQL Extension Log".
![Screenshot of the "Output" window in VS Code \(as highlighted in dark orange\). The dropdown is also highlighted, with "CodeQL Extension Log" selected.](https://docs.github.com/assets/cb-45440/images/help/security/codeql-for-vs-code-access-logs.png)


