  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [Advanced functionality](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli "Advanced functionality")/
  * [Creating CodeQL CLI database bundles](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/creating-database-bundle-for-troubleshooting "Creating CodeQL CLI database bundles")


# Creating CodeQL CLI database bundles
You can create a database bundle with CodeQL troubleshooting information.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [About creating CodeQL CLI database bundles](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/creating-database-bundle-for-troubleshooting#about-creating-codeql-cli-database-bundles)
  * [Increasing the verbosity for database create and database analyze](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/creating-database-bundle-for-troubleshooting#increasing-the-verbosity-for-database-create-and-database-analyze)


CodeQL CLI database bundles contain a copy of the source code being analyzed by CodeQL, therefore we suggest sharing these bundles only with people who are authorized to access that source code.
## [About creating CodeQL CLI database bundles](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/creating-database-bundle-for-troubleshooting#about-creating-codeql-cli-database-bundles)
The CodeQL CLI database bundle command can be used to create a relocatable archive of a CodeQL database.
A copy of a database bundle can be used to share troubleshooting information with your team members or with GitHub Support.
The following CodeQL CLI command syntax is suggested when creating a database bundle for troubleshooting purposes:
This sample `database bundle` command requires CodeQL CLI version 2.17.6 or higher.
```
codeql database bundle --output=codeql-debug-artifacts.zip --include-diagnostics --include-logs --include-results -- <dir>

```

For this command, `<dir>` must be the path to the directory where the CodeQL database was created.
The successful command execution creates a zip file called `codeql-debug-artifacts.zip` which contains CodeQL troubleshooting information. That file is the database bundle.
This command assumes that the `--log-dir` command line argument was not used for the `database create` and `database analyze` commands. When that command line argument is used, the log files created by those commands will not be included with the database bundle.
## [Increasing the verbosity for `database create` and `database analyze`](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/creating-database-bundle-for-troubleshooting#increasing-the-verbosity-for-database-create-and-database-analyze)
If the `database create` and `database analyze` commands are not detailed enough for troubleshooting purposes, you can increase their verbosity.
Both commands support the `--verbosity` command line argument which can be set to `progress++` prior to creating a database bundle.
