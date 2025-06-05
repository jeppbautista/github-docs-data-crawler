  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [resolve ram](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ram "resolve ram")


# resolve ram
[Deep plumbing] Prepare RAM options.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ram#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ram#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ram#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ram#synopsis)
Shell```
codeql resolve ram [--ram=<MB>] <options>...

```
```
codeql resolve ram [--ram=<MB>] <options>...

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ram#description)
[Deep plumbing] Prepare RAM options.
This deep plumbing command prepares appropriate command-line options to start a subcommand that will execute a QL query evaluator. It knows appropriate heuristics for deciding whether to keep some of the configured memory outside the Java heap.
In particular, this should be used to find appropriate `-J-Xmx` and `--off-heap-ram` options before starting a query server based on a desired _total_ RAM amount.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ram#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ram#primary-options)
#### [`--format=<fmt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ram#--formatfmt)
Select output format. Choices include:
`lines` _(default)_ : Print command-line arguments on one line each.
`json`: Print them as a JSON array.
### [Options from the invoking command's command line](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ram#options-from-the-invoking-commands-command-line)
#### [`-M, --ram=<MB>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ram#-m---rammb)
The query evaluator will try hard to keep its total memory footprint below this value. (However, for large databases it is possible that the threshold may be broken by file-backed memory maps, which can be swapped to disk in case of memory pressure).
The value should be at least 2048 MB; smaller values will be transparently rounded up.
#### [`--dataset=<directory>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ram#--datasetdirectory)
[Advanced] Tune the RAM settings appropriately for querying the given dataset, taking into account components of RAM usage that scale with the size of the database. If this is not given, a generic default size will be assumed.
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ram#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ram#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ram#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ram#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ram#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ram#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ram#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ram#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
