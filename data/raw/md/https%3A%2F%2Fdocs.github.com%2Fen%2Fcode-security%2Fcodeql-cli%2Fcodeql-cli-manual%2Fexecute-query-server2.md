  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [execute query-server2](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-query-server2 "execute query-server2")


# execute query-server2
[Plumbing] Support for running queries from IDEs.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-query-server2#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-query-server2#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-query-server2#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-query-server2#synopsis)
Shell```
codeql execute query-server2 [--threads=<num>] <options>...

```
```
codeql execute query-server2 [--threads=<num>] <options>...

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-query-server2#description)
[Plumbing] Support for running queries from IDEs.
This command is only relevant for authors of QL language extensions for IDEs. It is started by the IDE plugin in the background and communicates with it through a special protocol on its standard input and output streams.
Available since `v2.10.11`.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-query-server2#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-query-server2#primary-options)
#### [`--[no-]tuple-counting`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-query-server2#--no-tuple-counting)
[Advanced] Display tuple counts for each evaluation step in the query evaluator logs. If the `--evaluator-log` option is provided, tuple counts will be included in both the text-based and structured JSON logs produced by the command. (This can be useful for performance optimization of complex QL code).
#### [`--timeout=<seconds>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-query-server2#--timeoutseconds)
[Advanced] Set the timeout length for query evaluation, in seconds.
The timeout feature is intended to catch cases where a complex query would take "forever" to evaluate. It is not an effective way to limit the total amount of time the query evaluation can take. The evaluation will be allowed to continue as long as each separately timed part of the computation completes within the timeout. Currently these separately timed parts are "RA layers" of the optimized query, but that might change in the future.
If no timeout is specified, or is given as 0, no timeout will be set (except for [codeql test run](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-run), where the default timeout is 5 minutes).
#### [`-j, --threads=<num>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-query-server2#-j---threadsnum)
Use this many threads to evaluate queries.
Defaults to 1. You can pass 0 to use one thread per core on the machine, or -_N_ to leave _N_ cores unused (except still use at least one thread).
#### [`--[no-]save-cache`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-query-server2#--no-save-cache)
[Advanced] Aggressively write intermediate results to the disk cache. This takes more time and uses (much) more disk space, but may speed up the subsequent execution of similar queries.
#### [`--[no-]expect-discarded-cache`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-query-server2#--no-expect-discarded-cache)
[Advanced] Make decisions about which predicates to evaluate, and what to write to the disk cache, based on the assumption that the cache will be discarded after the queries have been executed.
#### [`--[no-]keep-full-cache`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-query-server2#--no-keep-full-cache)
[Advanced] Don't clean up the disk cache after evaluation completes. This may save time if you're going to do [codeql dataset cleanup](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-cleanup) or [codeql database cleanup](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-cleanup) afterwards anyway.
#### [`--max-disk-cache=<MB>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-query-server2#--max-disk-cachemb)
Set the maximum amount of space that the disk cache for intermediate query results can use.
If this size is not configured explicitly, the evaluator will try to use a "reasonable" amount of cache space, based on the size of the dataset and the complexity of the queries. Explicitly setting a higher limit than this default usage will enable additional caching which can speed up later queries.
#### [`--min-disk-free=<MB>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-query-server2#--min-disk-freemb)
[Advanced] Set target amount of free space on file system.
If `--max-disk-cache` is not given, the evaluator will try hard to curtail disk cache usage if the free space on the file system drops below this value.
#### [`--min-disk-free-pct=<pct>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-query-server2#--min-disk-free-pctpct)
[Advanced] Set target fraction of free space on file system.
If `--max-disk-cache` is not given, the evaluator will try hard to curtail disk cache usage if the free space on the file system drops below this percentage.
#### [`--external=<pred>=<file.csv>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-query-server2#--externalpredfilecsv)
A CSV file that contains rows for external predicate _< pred>_. Multiple `--external` options can be supplied.
#### [`--xterm-progress=<mode>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-query-server2#--xterm-progressmode)
[Advanced] Controls whether to show progress tracking during QL evaluation using xterm control sequences. Possible values are:
`no`: Never produce fancy progress; assume a dumb terminal.
`auto` _(default)_ : Autodetect whether the command is running in an appropriate terminal.
`yes`: Assume the terminal can understand xterm control sequences. The feature still depends on being able to autodetect the _size_ of the terminal, and will also be disabled if `-q` is given.
`25x80` (or similar): Like `yes`, and also explicitly give the size of the terminal.
`25x80:/dev/pts/17` (or similar): show fancy progress on a _different_ terminal than stderr. Mostly useful for internal testing.
#### [`--search-path=<dir>[:<dir>...]`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-query-server2#--search-pathdirdir)
This works like the similar option to [codeql query compile](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-compile) (q.v.).
There are no `--additional-packs` or `--library-path` options, as the corresponding values are provided per query
(Note: On Windows the path separator is `;`).
### [Options for controlling outputting of structured evaluator logs](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-query-server2#options-for-controlling-outputting-of-structured-evaluator-logs)
#### [`--evaluator-log=<file>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-query-server2#--evaluator-logfile)
[Advanced] Output structured logs about evaluator performance to the given file. The format of this log file is subject to change with no notice, but will be a stream of JSON objects separated by either two newline characters (by default) or one if the `--evaluator-log-minify` option is passed. Please use `codeql generate log-summary <file>` to produce a more stable summary of this file, and avoid parsing the file directly. The file will be overwritten if it already exists.
#### [`--evaluator-log-minify`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-query-server2#--evaluator-log-minify)
[Advanced] If the `--evaluator-log` option is passed, also passing this option will minimize the size of the JSON log produced, at the expense of making it much less human readable.
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-query-server2#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-query-server2#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-query-server2#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-query-server2#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-query-server2#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-query-server2#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-query-server2#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-query-server2#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
