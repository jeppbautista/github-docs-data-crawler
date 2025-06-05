  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [generate log-summary](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-log-summary "generate log-summary")


# generate log-summary
[Advanced] Create a summary of a structured log file.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-log-summary#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-log-summary#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-log-summary#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-log-summary#synopsis)
Shell```
codeql generate log-summary <options>... -- <input> <result>

```
```
codeql generate log-summary <options>... -- <input> <result>

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-log-summary#description)
[Advanced] Create a summary of a structured log file.
This command creates a summary of a structured JSON evaluator event log. The output of this command aims to be more stable across different versions of the CLI than the log files themselves. Thus, when implementing a script that uses output from the logs, it is strongly recommended to run this command and use its output rather than using the event logs directly.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-log-summary#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-log-summary#primary-options)
#### [`<input>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-log-summary#input)
[Mandatory] Path to the event log file to produce a summary of.
#### [`<result>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-log-summary#result)
Path to the location to output the summarised log file to. If this omitted, then the summary will be output to stdout.
#### [`--minify-output`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-log-summary#--minify-output)
Where applicable, omit whitespace in the outputted summary. The result will be less human-readable but take up less memory. This option only has an effect for some output formats.
#### [`--utc`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-log-summary#--utc)
[Advanced] Certain timestamps in the summaries produced by this command may use the local timezone of the machine they are running on. Enabling this flag forces all timestamps to be UTC.
#### [`--format=<format>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-log-summary#--formatformat)
Control the format of the output produced.
`predicates` _(default)_ : Produce a summary of the computation performed for each predicate. This will be a stream of JSON objects separated either by two newline characters (by default) or one if the `--minify-output` option is passed.
`text`: Produce a human-readable summary of the evaluation run.
`overall`: Produce a JSON file containing some overall information about the evaluation run, including some summary statistics and information about the most time-consuming evaluations that were performed.
#### [`--[no-]deduplicate-stage-summaries`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-log-summary#--no-deduplicate-stage-summaries)
[Advanced] This option only works in conjunction with the text format. If passed, this will result in the summary tables containing the most expensive predicates not being repeated for stages that are shared between queries. This has the side-effect of moving all the summary tables to the end of the log, rather than having the ones for each query appear at the point when that query finished.
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-log-summary#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-log-summary#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-log-summary#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-log-summary#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-log-summary#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-log-summary#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-log-summary#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-log-summary#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
