  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [dataset cleanup](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-cleanup "dataset cleanup")


# dataset cleanup
[Plumbing] Clean up temporary files from a dataset.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-cleanup#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-cleanup#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-cleanup#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-cleanup#synopsis)
Shell```
codeql dataset cleanup <options>... -- <dataset>

```
```
codeql dataset cleanup <options>... -- <dataset>

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-cleanup#description)
[Plumbing] Clean up temporary files from a dataset.
This should not be used for datasets still under construction, as it will make it impossible to import further data into the dataset.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-cleanup#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-cleanup#primary-options)
#### [`<dataset>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-cleanup#dataset)
[Mandatory] Path to the raw QL dataset to clean up.
#### [`--max-disk-cache=<MB>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-cleanup#--max-disk-cachemb)
Set the maximum amount of space that the disk cache for intermediate query results can use.
If this size is not configured explicitly, the evaluator will try to use a "reasonable" amount of cache space, based on the size of the dataset and the complexity of the queries. Explicitly setting a higher limit than this default usage will enable additional caching which can speed up later queries.
#### [`--min-disk-free=<MB>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-cleanup#--min-disk-freemb)
[Advanced] Set target amount of free space on file system.
If `--max-disk-cache` is not given, the evaluator will try hard to curtail disk cache usage if the free space on the file system drops below this value.
#### [`--min-disk-free-pct=<pct>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-cleanup#--min-disk-free-pctpct)
[Advanced] Set target fraction of free space on file system.
If `--max-disk-cache` is not given, the evaluator will try hard to curtail disk cache usage if the free space on the file system drops below this percentage.
#### [`--cache-cleanup=<mode>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-cleanup#--cache-cleanupmode)
Select how aggressively to trim the cache. Choices include:
`clear`: Remove the entire cache, trimming down to the state of a freshly extracted dataset
`trim` _(default)_ : Trim everything except explicitly "cached" predicates.
`fit`: Simply make sure the defined size limits for the disk cache are observed, deleting as many intermediates as necessary.
#### [`--cleanup-upgrade-backups`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-cleanup#--cleanup-upgrade-backups)
Delete any backup directories resulting from database upgrades.
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-cleanup#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-cleanup#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-cleanup#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-cleanup#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-cleanup#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-cleanup#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-cleanup#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-cleanup#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
