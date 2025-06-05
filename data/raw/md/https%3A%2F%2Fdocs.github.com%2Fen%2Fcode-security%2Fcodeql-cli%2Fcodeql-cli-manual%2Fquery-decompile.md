  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [query decompile](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-decompile "query decompile")


# query decompile
[Plumbing] Read an intermediate representation of a compiled query from a .qlo file.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-decompile#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-decompile#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-decompile#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-decompile#synopsis)
Shell```
codeql query decompile [--output=<file>] <options>... -- <file>

```
```
codeql query decompile [--output=<file>] <options>... -- <file>

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-decompile#description)
[Plumbing] Read an intermediate representation of a compiled query from a .qlo file.
The code will be written to standard output, unless the `--output` option is specified.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-decompile#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-decompile#primary-options)
#### [`<file>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-decompile#file)
[Mandatory] QLO file to read from.
#### [`-o, --output=<file>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-decompile#-o---outputfile)
The file to write the desired output to.
#### [`--kind=<kind>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-decompile#--kindkind)
The kind of the intermediate representation to read. The options are:
`dil`: A Datalog intermediate representation.
`ra`: A relational algebra intermediate representation. This is used by the query evaluation phase.
`bytecode`: Show the raw (uncompressed) bytecode from the .qlo file. Mostly useful for debugging the compiler/evaluator.
The default is `dil` if the query was compiled with `--include-dil-in-qlo` and `ra` otherwise
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-decompile#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-decompile#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-decompile#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-decompile#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-decompile#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-decompile#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-decompile#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-decompile#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
