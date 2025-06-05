  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Troubleshooting code scanning](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning "Troubleshooting code scanning")/
  * [Kotlin detected in no build](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/kotlin-detected-in-no-build "Kotlin detected in no build")


# Warning: Detected X Kotlin files in your project that could not be processed without a build
CodeQL databases can be created for Java without building the code, but Kotlin files are excluded unless the code is built.
## In this article
  * [About this warning](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/kotlin-detected-in-no-build#about-this-warning)
  * [Confirming the cause of the warning](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/kotlin-detected-in-no-build#confirming-the-cause-of-the-warning)
  * [Fixing the problem](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/kotlin-detected-in-no-build#fixing-the-problem)
  * [Further reading](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/kotlin-detected-in-no-build#further-reading)


## [About this warning](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/kotlin-detected-in-no-build#about-this-warning)
```
Warning: Detected X Kotlin files in your project that could not be processed without a build. To process these files...

```

This warning is reported when Kotlin files are detected in a repository that ran CodeQL code scanning for Java using the build mode of `none` (default setup), or if you run the CodeQL CLI using `--build-mode none` for a repository containing Java and Kotlin files.
## [Confirming the cause of the warning](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/kotlin-detected-in-no-build#confirming-the-cause-of-the-warning)
This warning is only displayed when the build mode of `none` is used for a repository with both Java and Kotlin files.
The CodeQL action and CodeQL CLI support a build mode of `none` for Java. This provides an easy way to enable analysis for Java code without building the codebase. However, Kotlin files are not included in the resulting CodeQL database.
You can verify the presence of Kotlin files by looking at the repository or pull request that triggered the warning. The `none` build mode is used only in the following circumstances:
  * Code scanning was enabled for the repository before Kotlin code was added and after the new mode was introduced (previously it would have used the `autobuild` mode).
  * The CodeQL workflow specifies a build mode of `none` for the repository (check for `build-mode: none`).
  * The CodeQL CLI is called without a `--command` and with `--build-mode none`.


## [Fixing the problem](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/kotlin-detected-in-no-build#fixing-the-problem)
You may not want to analyze the Kotlin files, in which case you can ignore the warning message.
If you want to update the analysis to also include Kotlin files, then CodeQL will need to build the Java and Kotlin code.
### [Code scanning default setup](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/kotlin-detected-in-no-build#code-scanning-default-setup)
  1. Wait until the Kotlin code is merged into the default branch for the repository.
  2. Disable and then re-enable default setup on the "Settings" page for your repository.


This will trigger a new analysis using automatic build detection. See [Configuring default setup for code scanning](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning) and [Building Java and Kotlin](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#building-java-and-kotlin).
If the automatic build detection fails, you will need to use advanced setup with the correct build commands for the project to analyze both languages.
### [Code scanning advanced setup](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/kotlin-detected-in-no-build#code-scanning-advanced-setup)
If you already use advanced setup, you can edit the CodeQL workflow and change the build mode for `java-kotlin` from `none` to either `autobuild` to automatically build your project, or `manual` to specify your own build steps. [Building Java and Kotlin](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#building-java-and-kotlin).
If you need to convert from default setup to advanced setup, you need enable advanced setup on the on the "Settings" page for your repository and create a CodeQL workflow. Then you can define a `manual` build mode for `java-kotlin` and define the build commands for the project.
### [Running the CodeQL CLI directly](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/kotlin-detected-in-no-build#running-the-codeql-cli-directly)
Update your calls to run the CodeQL CLI for the repository and pull requests to replace `--build-mode none` by `--build-mode autobuild` to try the automatic build detection. If automatic build detection is unsuccessful, remove the `--build-mode` option and include one or more `--command` options detailing the build script or steps required to build the project.
## [Further reading](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/kotlin-detected-in-no-build#further-reading)
  * [Creating an advanced setup for code scanning](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning)
  * [Building Java and Kotlin](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#building-java-and-kotlin)
  * [CodeQL build modes](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#codeql-build-modes)


