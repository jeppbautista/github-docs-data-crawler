  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [github merge-results](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-merge-results "github merge-results")


# github merge-results
[Deep plumbing] Merges multiple SARIF files into a single SARIF file.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-merge-results#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-merge-results#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-merge-results#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-merge-results#synopsis)
Shell```
codeql github merge-results --sarif=<file> --output=<file> <options>...

```
```
codeql github merge-results --sarif=<file> --output=<file> <options>...

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-merge-results#description)
[Deep plumbing] Merges multiple SARIF files into a single SARIF file.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-merge-results#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-merge-results#primary-options)
#### [`-s, --sarif=<file>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-merge-results#-s---sariffile)
[Mandatory] Path to the SARIF files to use. This should be the output of [codeql database analyze](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-analyze) (or [codeql database interpret-results](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results)) with `--format sarif-latest` for upload to github.com or the appropriate supported format tag for GitHub Enterprise Server instances (see [SARIF support for code scanning](https://docs.github.com/en/enterprise-server@3.17/code-security/code-scanning/integrating-with-code-scanning/sarif-support-for-code-scanning) for SARIF versions supported by your release).
#### [`-o, --output=<file>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-merge-results#-o---outputfile)
[Mandatory] Path where the merged SARIF file should be stored.
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-merge-results#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-merge-results#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-merge-results#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-merge-results#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-merge-results#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-merge-results#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-merge-results#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-merge-results#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
