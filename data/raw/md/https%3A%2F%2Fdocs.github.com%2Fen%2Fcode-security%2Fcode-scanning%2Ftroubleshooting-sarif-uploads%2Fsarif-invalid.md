  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Troubleshooting SARIF uploads](https://docs.github.com/en/code-security/code-scanning/troubleshooting-sarif-uploads "Troubleshooting SARIF uploads")/
  * [SARIF file invalid](https://docs.github.com/en/code-security/code-scanning/troubleshooting-sarif-uploads/sarif-invalid "SARIF file invalid")


# SARIF file is invalid
Code scanning can only process syntactically valid SARIF files. Invalid files are rejected.
## In this article
  * [About this error](https://docs.github.com/en/code-security/code-scanning/troubleshooting-sarif-uploads/sarif-invalid#about-this-error)
  * [Confirming the cause of the error](https://docs.github.com/en/code-security/code-scanning/troubleshooting-sarif-uploads/sarif-invalid#confirming-the-cause-of-the-error)
  * [Fixing the problem](https://docs.github.com/en/code-security/code-scanning/troubleshooting-sarif-uploads/sarif-invalid#fixing-the-problem)


## [About this error](https://docs.github.com/en/code-security/code-scanning/troubleshooting-sarif-uploads/sarif-invalid#about-this-error)
```
Invalid SARIF
SARIF file invalid
SARIF ZIP upload is invalid
400: Bad Request if the sarif field is invalid

```

One of these errors is reported if code scanning cannot parse the SARIF file.
You are unlikely to see this error when using CodeQL analysis.
## [Confirming the cause of the error](https://docs.github.com/en/code-security/code-scanning/troubleshooting-sarif-uploads/sarif-invalid#confirming-the-cause-of-the-error)
You can investigate the underlying cause of the error by looking at the log for the workflow run that uploaded the analysis and by checking the SARIF file in a validator. For more information, see [Using workflow run logs](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/using-workflow-run-logs) and visit the [Microsoft SARIF validator](https://sarifweb.azurewebsites.net/).
## [Fixing the problem](https://docs.github.com/en/code-security/code-scanning/troubleshooting-sarif-uploads/sarif-invalid#fixing-the-problem)
After you identify the invalid parts of the SARIF file, you may be able to resolve smaller issues manually, but you may need to talk to the maintainers of the tool. For information about validation and the format supported by code scanning, see [SARIF support for code scanning](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/sarif-support-for-code-scanning).
