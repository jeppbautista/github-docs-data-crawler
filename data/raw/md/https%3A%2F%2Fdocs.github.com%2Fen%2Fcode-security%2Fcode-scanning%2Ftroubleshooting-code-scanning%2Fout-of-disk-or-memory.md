  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Troubleshooting code scanning](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning "Troubleshooting code scanning")/
  * [Out of disk or memory](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/out-of-disk-or-memory "Out of disk or memory")


# Error: "Out of disk" or Error: "Out of memory"
If you see one of these errors with GitHub Actions, you can try alternative runners.
## In this article
  * [About these errors](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/out-of-disk-or-memory#about-these-errors)
  * [Confirming the cause of the problem](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/out-of-disk-or-memory#confirming-the-cause-of-the-problem)
  * [Fixing the problem](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/out-of-disk-or-memory#fixing-the-problem)


## [About these errors](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/out-of-disk-or-memory#about-these-errors)
```
Out of disk

```
```
Out of memory

```

You may see these errors when running code scanning.
## [Confirming the cause of the problem](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/out-of-disk-or-memory#confirming-the-cause-of-the-problem)
You can review the recommended hardware resources for running CodeQL to make sure the runners that you use for code scanning meet those requirements. For more information, see [Recommended hardware resources for running CodeQL](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/recommended-hardware-resources-for-running-codeql).
## [Fixing the problem](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/out-of-disk-or-memory#fixing-the-problem)
If the runners you're using don't meet the recommended hardware requirements, consider using either larger runners or self-hosted runners.
Larger runners are GitHub-hosted runners with more RAM, CPU, and disk space than standard runners. These runners have the runner application and other tools preinstalled. For more information about larger runners and code scanning, see [Using larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-larger-runners) and [Configuring larger runners for default setup](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/configuring-larger-runners-for-default-setup).
Self-hosted runners offer more control of hardware, operating system, and software tools than GitHub-hosted runners can provide. For more information, see [About self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners).
