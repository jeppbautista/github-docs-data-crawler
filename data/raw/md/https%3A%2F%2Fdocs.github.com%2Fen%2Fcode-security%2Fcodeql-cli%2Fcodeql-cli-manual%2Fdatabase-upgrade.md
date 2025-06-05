  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [database upgrade](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade "database upgrade")


# database upgrade
Upgrade a database so it is usable by the current tools.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#synopsis)
Shell```
codeql database upgrade [--threads=<num>] [--ram=<MB>] <options>... -- <database>

```
```
codeql database upgrade [--threads=<num>] [--ram=<MB>] <options>... -- <database>

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#description)
Upgrade a database so it is usable by the current tools.
This rewrites a CodeQL database to be compatible with the QL libraries that are found on the QL pack search path, if necessary.
If an upgrade is necessary, it is irreversible. The database will subsequently be unusable with the libraries that were current when it was created.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#primary-options)
#### [`<database>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#database)
[Mandatory] Path to the CodeQL database to upgrade.
#### [`--search-path=<dir>[:<dir>...]`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#--search-pathdirdir)
A list of directories under which QL packs containing upgrade recipes may be found. Each directory can either be a QL pack (or bundle of packs containing a `.codeqlmanifest.json` file at the root) or the immediate parent of one or more such directories.
If the path contains directories trees, their order defines precedence between them: if a pack name that must be resolved is matched in more than one of the directory trees, the one given first wins.
Pointing this at a checkout of the open-source CodeQL repository ought to work when querying one of the languages that live there.
(Note: On Windows the path separator is `;`).
#### [`--additional-packs=<dir>[:<dir>...]`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#--additional-packsdirdir)
[Advanced] If this list of directories is given, they will be searched for upgrades before the ones in `--search-path`. The order between these doesn't matter; it is an error if a pack name is found in two different places through this list.
This is useful if you're temporarily developing a new version of a pack that also appears in the default path. On the other hand it is _not recommended_ to override this option in a config file; some internal actions will add this option on the fly, overriding any configured value.
(Note: On Windows the path separator is `;`).
#### [`--target-dbscheme=<file>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#--target-dbschemefile)
The _target_ dbscheme we want to upgrade to. If this is not given, a maximal upgrade path will be constructed
#### [`--target-sha=<sha>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#--target-shasha)
[Advanced] An alternative to `--target-dbscheme` that gives the internal hash of the target dbscheme instead of the dbscheme file.
#### [`--[no-]allow-downgrades`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#--no-allow-downgrades)
Include any relevant downgrades if there are no upgrades
### [Options to control evaluation of upgrade queries](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#options-to-control-evaluation-of-upgrade-queries)
#### [`--[no-]tuple-counting`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#--no-tuple-counting)
[Advanced] Display tuple counts for each evaluation step in the query evaluator logs. If the `--evaluator-log` option is provided, tuple counts will be included in both the text-based and structured JSON logs produced by the command. (This can be useful for performance optimization of complex QL code).
#### [`--timeout=<seconds>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#--timeoutseconds)
[Advanced] Set the timeout length for query evaluation, in seconds.
The timeout feature is intended to catch cases where a complex query would take "forever" to evaluate. It is not an effective way to limit the total amount of time the query evaluation can take. The evaluation will be allowed to continue as long as each separately timed part of the computation completes within the timeout. Currently these separately timed parts are "RA layers" of the optimized query, but that might change in the future.
If no timeout is specified, or is given as 0, no timeout will be set (except for [codeql test run](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-run), where the default timeout is 5 minutes).
#### [`-j, --threads=<num>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#-j---threadsnum)
Use this many threads to evaluate queries.
Defaults to 1. You can pass 0 to use one thread per core on the machine, or -_N_ to leave _N_ cores unused (except still use at least one thread).
#### [`--[no-]save-cache`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#--no-save-cache)
[Advanced] Aggressively write intermediate results to the disk cache. This takes more time and uses (much) more disk space, but may speed up the subsequent execution of similar queries.
#### [`--[no-]expect-discarded-cache`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#--no-expect-discarded-cache)
[Advanced] Make decisions about which predicates to evaluate, and what to write to the disk cache, based on the assumption that the cache will be discarded after the queries have been executed.
#### [`--[no-]keep-full-cache`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#--no-keep-full-cache)
[Advanced] Don't clean up the disk cache after evaluation completes. This may save time if you're going to do [codeql dataset cleanup](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-cleanup) or [codeql database cleanup](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-cleanup) afterwards anyway.
#### [`--max-disk-cache=<MB>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#--max-disk-cachemb)
Set the maximum amount of space that the disk cache for intermediate query results can use.
If this size is not configured explicitly, the evaluator will try to use a "reasonable" amount of cache space, based on the size of the dataset and the complexity of the queries. Explicitly setting a higher limit than this default usage will enable additional caching which can speed up later queries.
#### [`--min-disk-free=<MB>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#--min-disk-freemb)
[Advanced] Set target amount of free space on file system.
If `--max-disk-cache` is not given, the evaluator will try hard to curtail disk cache usage if the free space on the file system drops below this value.
#### [`--min-disk-free-pct=<pct>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#--min-disk-free-pctpct)
[Advanced] Set target fraction of free space on file system.
If `--max-disk-cache` is not given, the evaluator will try hard to curtail disk cache usage if the free space on the file system drops below this percentage.
#### [`--external=<pred>=<file.csv>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#--externalpredfilecsv)
A CSV file that contains rows for external predicate _< pred>_. Multiple `--external` options can be supplied.
#### [`--xterm-progress=<mode>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#--xterm-progressmode)
[Advanced] Controls whether to show progress tracking during QL evaluation using xterm control sequences. Possible values are:
`no`: Never produce fancy progress; assume a dumb terminal.
`auto` _(default)_ : Autodetect whether the command is running in an appropriate terminal.
`yes`: Assume the terminal can understand xterm control sequences. The feature still depends on being able to autodetect the _size_ of the terminal, and will also be disabled if `-q` is given.
`25x80` (or similar): Like `yes`, and also explicitly give the size of the terminal.
`25x80:/dev/pts/17` (or similar): show fancy progress on a _different_ terminal than stderr. Mostly useful for internal testing.
### [Options for controlling outputting of structured evaluator logs](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#options-for-controlling-outputting-of-structured-evaluator-logs)
#### [`--evaluator-log=<file>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#--evaluator-logfile)
[Advanced] Output structured logs about evaluator performance to the given file. The format of this log file is subject to change with no notice, but will be a stream of JSON objects separated by either two newline characters (by default) or one if the `--evaluator-log-minify` option is passed. Please use `codeql generate log-summary <file>` to produce a more stable summary of this file, and avoid parsing the file directly. The file will be overwritten if it already exists.
#### [`--evaluator-log-minify`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#--evaluator-log-minify)
[Advanced] If the `--evaluator-log` option is passed, also passing this option will minimize the size of the JSON log produced, at the expense of making it much less human readable.
### [Options to control RAM usage of the upgrade process](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#options-to-control-ram-usage-of-the-upgrade-process)
#### [`-M, --ram=<MB>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#-m---rammb)
The query evaluator will try hard to keep its total memory footprint below this value. (However, for large databases it is possible that the threshold may be broken by file-backed memory maps, which can be swapped to disk in case of memory pressure).
The value should be at least 2048 MB; smaller values will be transparently rounded up.
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-upgrade#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
