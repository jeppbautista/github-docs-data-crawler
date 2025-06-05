  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Troubleshooting code scanning](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning "Troubleshooting code scanning")/
  * [Not recognized](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/not-recognized "Not recognized")


# Error: "is not a .ql file, .qls file, a directory, or a query pack specification"
CodeQL was unable to locate one of the queries or sets of queries that are specified for analysis.
## In this article
  * [About this error](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/not-recognized#about-this-error)
  * [Confirming the cause of the error](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/not-recognized#confirming-the-cause-of-the-error)
  * [Fixing the problem](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/not-recognized#fixing-the-problem)


## [About this error](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/not-recognized#about-this-error)
```
Is not a .ql file, .qls file, a directory, or a query pack specification.

```

You will see this error if CodeQL is unable to find the named query, query suite, or query pack at the location requested in the workflow.
## [Confirming the cause of the error](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/not-recognized#confirming-the-cause-of-the-error)
There are two common reasons for this error:
  * There is a typo in the workflow.
  * A resource the workflow refers to by path was renamed, deleted, or moved to a new location.


## [Fixing the problem](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/not-recognized#fixing-the-problem)
After verifying the location of the resource, you can update the workflow to specify the correct location.
