  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [dataset check](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-check "dataset check")


# dataset check
[Plumbing] Check a particular dataset for internal consistency.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-check#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-check#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-check#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-check#synopsis)
Shell```
codeql dataset check <options>... -- <dataset>

```
```
codeql dataset check <options>... -- <dataset>

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-check#description)
[Plumbing] Check a particular dataset for internal consistency.
This command is most commonly useful to developers of CodeQL extractors, as it validates the data produced by the extractor. It may also be useful if queries against a database are giving inconsistent results, to rule out issues in the underlying data as the cause.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-check#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-check#primary-options)
#### [`<dataset>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-check#dataset)
[Mandatory] Path to the raw QL dataset to check.
#### [`--failing-exitcode=<code>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-check#--failing-exitcodecode)
[Advanced] Set the exit code to produce if any failures are encountered. Usually 1, but tooling that parses the output may find it useful to set it to 0.
#### [`--format=<fmt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-check#--formatfmt)
Select output format. Possible choices:
`text` _(default)_ : A human-readable textual rendering.
`json`: A streamed JSON array of objects.
`jsonz`: A stream of zero-terminated JSON objects.
#### [`--[no-]precise-locations`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-check#--no-precise-locations)
[Advanced] Expend extra effort to compute precise locations for inconsistencies. This will take more time, but may make it easier to debug extractor behaviour.
#### [`--max-resolve-depth=<n>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-check#--max-resolve-depthn)
[Advanced] The maximum depth to which IDs should be resolved to explain inconsistencies. (Default: 3)
#### [`--max-errors-per-checker=<n>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-check#--max-errors-per-checkern)
The maximum number of inconsistency errors of each kind that should be reported explicitly. (Default: 5)
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-check#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-check#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-check#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-check#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-check#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-check#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-check#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-check#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
