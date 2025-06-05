  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [execute language-server](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-language-server "execute language-server")


# execute language-server
[Plumbing] On-line support for the QL language in IDEs.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-language-server#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-language-server#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-language-server#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-language-server#synopsis)
Shell```
codeql execute language-server --check-errors=<checkErrors> <options>...

```
```
codeql execute language-server --check-errors=<checkErrors> <options>...

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-language-server#description)
[Plumbing] On-line support for the QL language in IDEs.
This command is only relevant for authors of QL language extensions for IDEs. It is started by the IDE extension in the background and communicates with it through a special protocol on its standard input and output streams.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-language-server#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-language-server#primary-options)
#### [`--check-errors=<checkErrors>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-language-server#--check-errorscheckerrors)
[Mandatory] How to check errors. One of: ON_CHANGE, EXPLICIT.
#### [`--search-path=<dir>[:<dir>...]`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-language-server#--search-pathdirdir)
This works like the similar option to [codeql query compile](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/query-compile) (q.v.).
There are no `--additional-packs` or `--library-path` options, as the corresponding values are provided online by the IDE extension through the language server protocol.
(Note: On Windows the path separator is `;`).
#### [`--synchronous`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-language-server#--synchronous)
Carry out actions a single main thread rather than in a threaded executor.
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-language-server#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-language-server#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-language-server#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-language-server#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-language-server#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-language-server#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-language-server#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/execute-language-server#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
