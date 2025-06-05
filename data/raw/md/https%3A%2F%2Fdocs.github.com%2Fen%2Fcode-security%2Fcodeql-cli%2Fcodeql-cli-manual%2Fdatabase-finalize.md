  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [database finalize](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize "database finalize")


# database finalize
[Plumbing] Final steps in database creation.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#synopsis)
Shell```
codeql database finalize [--dbscheme=<file>] [--threads=<num>] [--ram=<MB>] <options>... -- <database>

```
```
codeql database finalize [--dbscheme=<file>] [--threads=<num>] [--ram=<MB>] <options>... -- <database>

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#description)
[Plumbing] Final steps in database creation.
Finalize a database that was created with [codeql database init](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-init) and subsequently seeded with analysis data using [codeql database trace-command](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command). This needs to happen before the new database can be queried.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#primary-options)
#### [`<database>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#database)
[Mandatory] Path to the CodeQL database under construction. This must have been prepared for extraction with [codeql database init](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-init).
If the `--db-cluster` option is given, this is not a database itself, but a directory that _contains_ databases, and all of those databases will be processed together.
#### [`--[no-]db-cluster`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#--no-db-cluster)
Indicates that the directory given on the command line is not a database itself, but a directory that _contains_ one or more databases under construction. Those databases will be processed together.
#### [`--additional-dbs=<database>[:<database>...]`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#--additional-dbsdatabasedatabase)
[Advanced] Path to additional CodeQL databases under construction. These will not themselves be finalized, but the data from them will be included in the finalized database being created. This is an advanced option that may not have the desired effect in all cases. For more information, please refer to the documentation of [codeql database import](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import).
If the `--db-cluster` option is given, it is expected that these will be database clusters rather than individual CodeQL databases.
(Note: On Windows the path separator is `;`).
#### [`--no-cleanup`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#--no-cleanup)
[Advanced] Suppress all database cleanup after finalization. Useful for debugging purposes.
#### [`--no-pre-finalize`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#--no-pre-finalize)
[Advanced] Skip any pre-finalize script specified by the active CodeQL extractor.
#### [`--[no-]skip-empty`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#--no-skip-empty)
[Advanced] Output a warning instead of failing if a database is empty because no source code was seen during the build. The empty database will be left unfinalized.
### [Options for controlling the TRAP import operation](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#options-for-controlling-the-trap-import-operation)
#### [`-S, --dbscheme=<file>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#-s---dbschemefile)
[Advanced] Override the auto-detected dbscheme definition that the TRAP files are assumed to adhere to. Normally, this is taken from the database's extractor.
#### [`-j, --threads=<num>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#-j---threadsnum)
Use this many threads for the import operation.
Defaults to 1. You can pass 0 to use one thread per core on the machine, or -_N_ to leave _N_ cores unused (except still use at least one thread).
#### [`-M, --ram=<MB>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#-m---rammb)
Use this much memory for the import operation.
### [Low-level dataset cleanup options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#low-level-dataset-cleanup-options)
#### [`--max-disk-cache=<MB>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#--max-disk-cachemb)
Set the maximum amount of space that the disk cache for intermediate query results can use.
If this size is not configured explicitly, the evaluator will try to use a "reasonable" amount of cache space, based on the size of the dataset and the complexity of the queries. Explicitly setting a higher limit than this default usage will enable additional caching which can speed up later queries.
#### [`--min-disk-free=<MB>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#--min-disk-freemb)
[Advanced] Set target amount of free space on file system.
If `--max-disk-cache` is not given, the evaluator will try hard to curtail disk cache usage if the free space on the file system drops below this value.
#### [`--min-disk-free-pct=<pct>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#--min-disk-free-pctpct)
[Advanced] Set target fraction of free space on file system.
If `--max-disk-cache` is not given, the evaluator will try hard to curtail disk cache usage if the free space on the file system drops below this percentage.
#### [`--cache-cleanup=<mode>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#--cache-cleanupmode)
Select how aggressively to trim the cache. Choices include:
`clear`: Remove the entire cache, trimming down to the state of a freshly extracted dataset
`trim` _(default)_ : Trim everything except explicitly "cached" predicates.
`fit`: Simply make sure the defined size limits for the disk cache are observed, deleting as many intermediates as necessary.
#### [`--cleanup-upgrade-backups`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#--cleanup-upgrade-backups)
Delete any backup directories resulting from database upgrades.
### [Options for checking imported TRAP](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#options-for-checking-imported-trap)
#### [`--[no-]check-undefined-labels`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#--no-check-undefined-labels)
[Advanced] Report errors for undefined labels.
#### [`--[no-]check-unused-labels`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#--no-check-unused-labels)
[Advanced] Report errors for unused labels.
#### [`--[no-]check-repeated-labels`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#--no-check-repeated-labels)
[Advanced] Report errors for repeated labels.
#### [`--[no-]check-redefined-labels`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#--no-check-redefined-labels)
[Advanced] Report errors for redefined labels.
#### [`--[no-]check-use-before-definition`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#--no-check-use-before-definition)
[Advanced] Report errors for labels used before they're defined.
#### [`--[no-]fail-on-trap-errors`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#--no-fail-on-trap-errors)
[Advanced] Exit non-zero if an error occurs during trap import.
#### [`--[no-]include-location-in-star`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#--no-include-location-in-star)
[Advanced] Construct entity IDs that encode the location in the TRAP file they came from. Can be useful for debugging of TRAP generators, but takes up a lot of space in the dataset.
#### [`--[no-]linkage-aware-import`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#--no-linkage-aware-import)
[Advanced] Controls whether [codeql dataset import](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import) is linkage-aware _(default)_ or not. On projects where this part of database creation consumes too much memory, disabling this option may help them progress at the expense of database completeness.
Available since `v2.15.3`.
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-finalize#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
