  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL for VS Code](https://docs.github.com/en/code-security/codeql-for-vs-code "CodeQL for VS Code")/
  * [Troubleshooting CodeQL for VS Code](https://docs.github.com/en/code-security/codeql-for-vs-code/troubleshooting-codeql-for-vs-code "Troubleshooting CodeQL for VS Code")/
  * [Problem with controller repository](https://docs.github.com/en/code-security/codeql-for-vs-code/troubleshooting-codeql-for-vs-code/warning-problem-with-controller-repository "Problem with controller repository")


# Problem with controller repository
If you see this warning, update your controller repository to a private repository.
## In this article
  * [About this warning](https://docs.github.com/en/code-security/codeql-for-vs-code/troubleshooting-codeql-for-vs-code/warning-problem-with-controller-repository#about-this-warning)
  * [Confirming the cause of the problem](https://docs.github.com/en/code-security/codeql-for-vs-code/troubleshooting-codeql-for-vs-code/warning-problem-with-controller-repository#confirming-the-cause-of-the-problem)
  * [Fixing the problem](https://docs.github.com/en/code-security/codeql-for-vs-code/troubleshooting-codeql-for-vs-code/warning-problem-with-controller-repository#fixing-the-problem)


## [About this warning](https://docs.github.com/en/code-security/codeql-for-vs-code/troubleshooting-codeql-for-vs-code/warning-problem-with-controller-repository#about-this-warning)
```
Publicly visible controller repository can't be used to analyze private repositories. NUMBER private repositories were not analyzed.

```

If you run variant analysis on a custom list of repositories, you may receive this warning as a banner in Visual Studio Code, where NUMBER is the number of private repositories that have not been analyzed.
## [Confirming the cause of the problem](https://docs.github.com/en/code-security/codeql-for-vs-code/troubleshooting-codeql-for-vs-code/warning-problem-with-controller-repository#confirming-the-cause-of-the-problem)
When you run variant analysis, you'll see any errors and warnings displayed in the "Variant Analysis Results" view.
## [Fixing the problem](https://docs.github.com/en/code-security/codeql-for-vs-code/troubleshooting-codeql-for-vs-code/warning-problem-with-controller-repository#fixing-the-problem)
To analyze private repositories, you should edit your settings to update your controller repository to a private repository. For information on how to edit the controller repository, see [Customizing settings](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/customizing-settings#configuring-settings-for-variant-analysis).
