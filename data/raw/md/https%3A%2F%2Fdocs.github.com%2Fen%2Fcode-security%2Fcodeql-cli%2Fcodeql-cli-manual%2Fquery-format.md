  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [query format](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-format "query format")


# query format
Autoformat QL source code.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-format#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-format#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-format#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-format#synopsis)
Shell```
codeql query format [--output=<file>] [--in-place] [--backup=<ext>] <options>... -- <file>...

```
```
codeql query format [--output=<file>] [--in-place] [--backup=<ext>] <options>... -- <file>...

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-format#description)
Autoformat QL source code.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-format#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-format#primary-options)
#### [`<file>...`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-format#file)
One or more `.ql` or `.qll` source files to autoformat. A dash can be specified to read from standard input.
#### [`-o, --output=<file>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-format#-o---outputfile)
Write the formatted QL code to this file instead of the standard output stream. Must not be given if there is more than one input.
#### [`-i, --[no-]in-place`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-format#-i---no-in-place)
Overwrite each input file with a formatted version of its content.
#### [`--[no-]check-only`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-format#--no-check-only)
Instead of writing output, exit with status 1 if any input files _differ_ from their correct formatting. A message telling which files differed will be printed to standard error unless you also give `-qq`.
#### [`-b, --backup=<ext>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-format#-b---backupext)
When writing a file that already exists, rename the existing file to a backup by appending this extension to its name. If the backup file already exists, it will be silently deleted.
#### [`--no-syntax-errors`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-format#--no-syntax-errors)
If an input file is not syntactically correct QL, pretend that it is already correctly formatted. (Usually such a file causes the command to terminate with an error message).
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-format#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-format#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-format#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-format#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-format#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-format#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-format#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-format#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
