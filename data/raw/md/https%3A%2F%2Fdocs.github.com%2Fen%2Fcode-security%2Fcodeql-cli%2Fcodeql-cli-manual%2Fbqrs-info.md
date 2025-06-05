  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [bqrs info](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-info "bqrs info")


# bqrs info
Display metadata for a BQRS file.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-info#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-info#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-info#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-info#synopsis)
Shell```
codeql bqrs info <options>... -- <file>

```
```
codeql bqrs info <options>... -- <file>

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-info#description)
Display metadata for a BQRS file.
This command displays an overview of the data contained in the compact binary BQRS file that is the result of executing a query. It shows the names and sizes of each result set (table) in the BQRS file, and the column types of each result set.
It can also optionally precompute offsets for using the pagination options of [codeql bqrs decode](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-decode). This is mainly useful for IDE plugins.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-info#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-info#primary-options)
#### [`<file>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-info#file)
[Mandatory] BQRS file to show information about.
#### [`--format=<fmt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-info#--formatfmt)
Select output format, either `text` _(default)_ or `json`.
### [Supporting pagination in codeql bqrs decode](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-info#supporting-pagination-in-codeql-bqrs-decode)
#### [`--paginate-rows=<num>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-info#--paginate-rowsnum)
[Advanced] When given together with `--format=json`, compute a table of byte offsets that can later be given to the `--start-at` option of [codeql bqrs decode](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-decode), to start streaming results at positions 0, _< num>_, 2*_< num>_, and so forth.
#### [`--paginate-result-set=<name>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-info#--paginate-result-setname)
[Advanced] Only process `--paginate-rows` for result sets with this name. (If the name does not match any result set, `--paginate-rows` is a no-op).
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-info#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-info#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-info#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-info#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-info#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-info#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-info#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-info#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
