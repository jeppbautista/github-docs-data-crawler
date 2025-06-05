  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [query run](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run "query run")


# query run
Run a single query.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#synopsis)
Shell```
codeql query run (--database=<database> | --dataset=<dataset>) [--output=<file.bqrs>] [--threads=<num>] [--ram=<MB>] <options>... -- <file.ql>

```
```
codeql query run (--database=<database> | --dataset=<dataset>) [--output=<file.bqrs>] [--threads=<num>] [--ram=<MB>] <options>... -- <file.ql>

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#description)
Run a single query.
This command runs single query against a CodeQL database or raw QL dataset.
By default the result of the query will be displayed on the terminal in a human-friendly rendering. If you want to do further processing of the results, we strongly recommend using the `--output` option to write the results to a file in an intermediate binary format, which can then be unpacked into various more machine-friendly representations by [codeql bqrs decode](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-decode).
If your query produces results in a form that can be interpreted as source-code alerts, you may find [codeql database analyze](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-analyze) a more convenient way to run it. In particular, [codeql database analyze](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-analyze) can produce output in the SARIF format, which can be used with an variety of alert viewers.
To run multiple queries in parallel, see [codeql database run-queries](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-run-queries).
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#primary-options)
#### [`<file.ql>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#fileql)
[Mandatory] QL source of the query to execute.
#### [`-o, --output=<file.bqrs>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#-o---outputfilebqrs)
A file where to output from the query will be written in BQRS format.
### [Options to select what to query](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#options-to-select-what-to-query)
Exactly one of these options must be given.
#### [`-d, --database=<database>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#-d---databasedatabase)
Path to a CodeQL database to query.
#### [`--dataset=<dataset>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--datasetdataset)
[Advanced] Path to a raw QL dataset to query.
### [Options to control the query evaluator](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#options-to-control-the-query-evaluator)
#### [`--[no-]tuple-counting`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--no-tuple-counting)
[Advanced] Display tuple counts for each evaluation step in the query evaluator logs. If the `--evaluator-log` option is provided, tuple counts will be included in both the text-based and structured JSON logs produced by the command. (This can be useful for performance optimization of complex QL code).
#### [`--timeout=<seconds>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--timeoutseconds)
[Advanced] Set the timeout length for query evaluation, in seconds.
The timeout feature is intended to catch cases where a complex query would take "forever" to evaluate. It is not an effective way to limit the total amount of time the query evaluation can take. The evaluation will be allowed to continue as long as each separately timed part of the computation completes within the timeout. Currently these separately timed parts are "RA layers" of the optimized query, but that might change in the future.
If no timeout is specified, or is given as 0, no timeout will be set (except for [codeql test run](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-run), where the default timeout is 5 minutes).
#### [`-j, --threads=<num>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#-j---threadsnum)
Use this many threads to evaluate queries.
Defaults to 1. You can pass 0 to use one thread per core on the machine, or -_N_ to leave _N_ cores unused (except still use at least one thread).
#### [`--[no-]save-cache`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--no-save-cache)
[Advanced] Aggressively write intermediate results to the disk cache. This takes more time and uses (much) more disk space, but may speed up the subsequent execution of similar queries.
#### [`--[no-]expect-discarded-cache`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--no-expect-discarded-cache)
[Advanced] Make decisions about which predicates to evaluate, and what to write to the disk cache, based on the assumption that the cache will be discarded after the queries have been executed.
#### [`--[no-]keep-full-cache`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--no-keep-full-cache)
[Advanced] Don't clean up the disk cache after evaluation completes. This may save time if you're going to do [codeql dataset cleanup](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-cleanup) or [codeql database cleanup](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-cleanup) afterwards anyway.
#### [`--max-disk-cache=<MB>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--max-disk-cachemb)
Set the maximum amount of space that the disk cache for intermediate query results can use.
If this size is not configured explicitly, the evaluator will try to use a "reasonable" amount of cache space, based on the size of the dataset and the complexity of the queries. Explicitly setting a higher limit than this default usage will enable additional caching which can speed up later queries.
#### [`--min-disk-free=<MB>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--min-disk-freemb)
[Advanced] Set target amount of free space on file system.
If `--max-disk-cache` is not given, the evaluator will try hard to curtail disk cache usage if the free space on the file system drops below this value.
#### [`--min-disk-free-pct=<pct>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--min-disk-free-pctpct)
[Advanced] Set target fraction of free space on file system.
If `--max-disk-cache` is not given, the evaluator will try hard to curtail disk cache usage if the free space on the file system drops below this percentage.
#### [`--external=<pred>=<file.csv>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--externalpredfilecsv)
A CSV file that contains rows for external predicate _< pred>_. Multiple `--external` options can be supplied.
#### [`--xterm-progress=<mode>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--xterm-progressmode)
[Advanced] Controls whether to show progress tracking during QL evaluation using xterm control sequences. Possible values are:
`no`: Never produce fancy progress; assume a dumb terminal.
`auto` _(default)_ : Autodetect whether the command is running in an appropriate terminal.
`yes`: Assume the terminal can understand xterm control sequences. The feature still depends on being able to autodetect the _size_ of the terminal, and will also be disabled if `-q` is given.
`25x80` (or similar): Like `yes`, and also explicitly give the size of the terminal.
`25x80:/dev/pts/17` (or similar): show fancy progress on a _different_ terminal than stderr. Mostly useful for internal testing.
### [Options for controlling outputting of structured evaluator logs](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#options-for-controlling-outputting-of-structured-evaluator-logs)
#### [`--evaluator-log=<file>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--evaluator-logfile)
[Advanced] Output structured logs about evaluator performance to the given file. The format of this log file is subject to change with no notice, but will be a stream of JSON objects separated by either two newline characters (by default) or one if the `--evaluator-log-minify` option is passed. Please use `codeql generate log-summary <file>` to produce a more stable summary of this file, and avoid parsing the file directly. The file will be overwritten if it already exists.
#### [`--evaluator-log-minify`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--evaluator-log-minify)
[Advanced] If the `--evaluator-log` option is passed, also passing this option will minimize the size of the JSON log produced, at the expense of making it much less human readable.
### [Options to control RAM usage](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#options-to-control-ram-usage)
#### [`-M, --ram=<MB>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#-m---rammb)
The query evaluator will try hard to keep its total memory footprint below this value. (However, for large databases it is possible that the threshold may be broken by file-backed memory maps, which can be swapped to disk in case of memory pressure).
The value should be at least 2048 MB; smaller values will be transparently rounded up.
### [Options to control QL compilation](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#options-to-control-ql-compilation)
#### [`--warnings=<mode>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--warningsmode)
How to handle warnings from the QL compiler. One of:
`hide`: Suppress warnings.
`show` _(default)_ : Print warnings but continue with compilation.
`error`: Treat warnings as errors.
#### [`--no-debug-info`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--no-debug-info)
Don't emit source location info in RA for debugging.
#### [`--[no-]fast-compilation`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--no-fast-compilation)
[Deprecated] [Advanced] Omit particularly slow optimization steps.
#### [`--no-release-compatibility`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--no-release-compatibility)
[Advanced] Use the newest compiler features, at the cost of portability.
From time to time, new QL language features and evaluator optimizations will be supported by the QL evaluator a few releases before they are enabled by default in the QL compiler. This helps ensure that the performance you experience when developing queries in the newest CodeQL release can be matched by slightly older releases that may still be in use for Code Scanning or CI integrations.
If you do not care about your queries being compatible with other (earlier or later) CodeQL releases, you can sometimes achieve a small amount of extra performance by using this flag to enable recent improvements in the compiler early.
In releases where there are no recent improvements to enable, this option silently does nothing. Thus it is safe to set it once and for all in your global CodeQL config file.
Available since `v2.11.1`.
#### [`--[no-]local-checking`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--no-local-checking)
Only perform initial checks on the part of the QL source that is used.
#### [`--no-metadata-verification`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--no-metadata-verification)
Don't check embedded query metadata in QLDoc comments for validity.
#### [`--compilation-cache-size=<MB>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--compilation-cache-sizemb)
[Advanced] Override the default maximum size for a compilation cache directory.
#### [`--fail-on-ambiguous-relation-name`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--fail-on-ambiguous-relation-name)
[Advanced] Fail compilation if an ambiguous relation name is generated during compilation.
### [Options to set up compilation environment](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#options-to-set-up-compilation-environment)
#### [`--search-path=<dir>[:<dir>...]`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--search-pathdirdir)
A list of directories under which QL packs may be found. Each directory can either be a QL pack (or bundle of packs containing a `.codeqlmanifest.json` file at the root) or the immediate parent of one or more such directories.
If the path contains more than one directory, their order defines precedence between them: when a pack name that must be resolved is matched in more than one of the directory trees, the one given first wins.
Pointing this at a checkout of the open-source CodeQL repository ought to work when querying one of the languages that live there.
If you have checked out the CodeQL repository as a sibling of the unpacked CodeQL toolchain, you don't need to give this option; such sibling directories will always be searched for QL packs that cannot be found otherwise. (If this default does not work, it is strongly recommended to set up `--search-path` once and for all in a per-user configuration file).
(Note: On Windows the path separator is `;`).
#### [`--additional-packs=<dir>[:<dir>...]`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--additional-packsdirdir)
If this list of directories is given, they will be searched for packs before the ones in `--search-path`. The order between these doesn't matter; it is an error if a pack name is found in two different places through this list.
This is useful if you're temporarily developing a new version of a pack that also appears in the default path. On the other hand, it is _not recommended_ to override this option in a config file; some internal actions will add this option on the fly, overriding any configured value.
(Note: On Windows the path separator is `;`).
#### [`--library-path=<dir>[:<dir>...]`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--library-pathdirdir)
[Advanced] An optional list of directories that will be added to the raw import search path for QL libraries. This should only be used if you're using QL libraries that have not been packaged as QL packs.
(Note: On Windows the path separator is `;`).
#### [`--dbscheme=<file>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--dbschemefile)
[Advanced] Explicitly define which dbscheme queries should be compiled against. This should only be given by callers that are extremely sure what they're doing.
#### [`--compilation-cache=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--compilation-cachedir)
[Advanced] Specify an additional directory to use as a compilation cache.
#### [`--no-default-compilation-cache`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--no-default-compilation-cache)
[Advanced] Don't use compilation caches in standard locations such as in the QL pack containing the query or in the CodeQL toolchain directory.
### [Options for configuring the CodeQL package manager](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#options-for-configuring-the-codeql-package-manager)
#### [`--registries-auth-stdin`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--registries-auth-stdin)
Authenticate to GitHub Enterprise Server Container registries by passing a comma-separated list of <registry_url>=<token> pairs.
For example, you can pass `https://containers.GHEHOSTNAME1/v2/=TOKEN1,https://containers.GHEHOSTNAME2/v2/=TOKEN2` to authenticate to two GitHub Enterprise Server instances.
This overrides the CODEQL_REGISTRIES_AUTH and GITHUB_TOKEN environment variables. If you only need to authenticate to the github.com Container registry, you can instead authenticate using the simpler `--github-auth-stdin` option.
#### [`--github-auth-stdin`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--github-auth-stdin)
Authenticate to the github.com Container registry by passing a github.com GitHub Apps token or personal access token via standard input.
To authenticate to GitHub Enterprise Server Container registries, pass `--registries-auth-stdin` or use the CODEQL_REGISTRIES_AUTH environment variable.
This overrides the GITHUB_TOKEN environment variable.
### [Options to control the extension packs](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#options-to-control-the-extension-packs)
####  [`--model-packs=<`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--model-packsnamerange)name@range>...
A list of CodeQL pack names, each with an optional version range, to be used as model packs to customize the queries that are about to be evaluated.
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-run#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
