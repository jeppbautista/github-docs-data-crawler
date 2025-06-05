  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [resolve tests](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-tests "resolve tests")


# resolve tests
[Deep plumbing] Find QL unit tests in given directories.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-tests#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-tests#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-tests#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-tests#synopsis)
Shell```
codeql resolve tests <options>... -- <test|dir>...

```
```
codeql resolve tests <options>... -- <test|dir>...

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-tests#description)
[Deep plumbing] Find QL unit tests in given directories.
This plumbing command is responsible for expanding the command-line parameters of subcommands that run QL unit tests, to an actual list of individual .ql and .qlref files to execute.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-tests#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-tests#primary-options)
#### [`<test|dir>...`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-tests#testdir)
Each argument is one of:
  * A `.ql` or `.qlref` file that defines a test to run.
  * A directory which will be searched recursively for tests to run.


#### [`--slice=<N/M>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-tests#--slicenm)
[Advanced] Divide the test cases into _M_ roughly equal-sized slices and process only the _N_ th of them. This can be used for manual parallelization of the testing process.
#### [`--[no-]strict-test-discovery`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-tests#--no-strict-test-discovery)
[Advanced] Only use queries that can be strongly identified as tests. This mode tries to distinguish between `.ql` files that define unit tests and `.ql` files that are meant to be useful queries. This option is used by tools, such as IDEs, that need to identify all unit tests in a directory tree without depending on previous knowledge of how the files in it are arranged.
Within a QL pack whose `qlpack.yml` declares a `tests` directory, all `.ql` files in that directory are considered tests, and `.ql` files outside it are ignored. In a QL pack that doesn't declare a `tests` directory, a `.ql` file is identified as a test only if it has a corresponding `.expected` file.
For consistency, `.qlref` files are limited by the same rules as `.ql` files even though a `.qlref` file cannot really be a non-test.
#### [`--format=<fmt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-tests#--formatfmt)
Select output format, either `text` _(default)_ or `json`.
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-tests#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-tests#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-tests#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-tests#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-tests#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-tests#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-tests#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-tests#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
