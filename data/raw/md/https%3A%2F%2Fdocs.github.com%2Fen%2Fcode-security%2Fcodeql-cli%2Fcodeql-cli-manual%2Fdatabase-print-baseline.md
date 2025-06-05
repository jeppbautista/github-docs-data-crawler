  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [database print-baseline](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-print-baseline "database print-baseline")


# database print-baseline
[Plumbing] Print a summary of the baseline lines of code seen.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-print-baseline#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-print-baseline#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-print-baseline#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-print-baseline#synopsis)
Shell```
codeql database print-baseline <options>... -- <database>

```
```
codeql database print-baseline <options>... -- <database>

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-print-baseline#description)
[Plumbing] Print a summary of the baseline lines of code seen.
This command will print to standard out the baseline lines of code seen within the source root specified at [codeql database init](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-init) time for each language present in the database.
The baseline is an estimate of the non-empty, non-comment lines of code in a database. This count is different from the lines of code counted by CodeQL metrics queries, which only counts code that is passed to the CodeQL evaluator. In some cases, the baseline count may be lower than the count in metrics queries since metrics queries may include external files that are passed to the evaluator, but are not included in the source root.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-print-baseline#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-print-baseline#primary-options)
#### [`<database>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-print-baseline#database)
[Mandatory] Path to the CodeQL database under construction. This must have been prepared for extraction with [codeql database init](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-init).
If the `--db-cluster` option is given, this is not a database itself, but a directory that _contains_ databases, and all of those databases will be processed together.
#### [`--[no-]db-cluster`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-print-baseline#--no-db-cluster)
Indicates that the directory given on the command line is not a database itself, but a directory that _contains_ one or more databases under construction. Those databases will be processed together.
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-print-baseline#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-print-baseline#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-print-baseline#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-print-baseline#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-print-baseline#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-print-baseline#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-print-baseline#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-print-baseline#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
