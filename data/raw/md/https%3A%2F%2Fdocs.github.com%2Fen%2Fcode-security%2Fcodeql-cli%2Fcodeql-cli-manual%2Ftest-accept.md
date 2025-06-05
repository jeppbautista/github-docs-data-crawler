  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [test accept](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-accept "test accept")


# test accept
Accept results of failing unit tests.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-accept#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-accept#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-accept#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-accept#synopsis)
Shell```
codeql test accept <options>... -- <test|dir>...

```
```
codeql test accept <options>... -- <test|dir>...

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-accept#description)
Accept results of failing unit tests.
This is a convenience command that renames the `.actual` files left by [codeql test run](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-run) for failing tests into `.expected`, such that future runs on the tests that give the same output will be considered to pass. What it does can also be achieved by ordinary file manipulation, but you may find its syntax more useful for this special case.
The command-line arguments specify one or more _tests_ -- that is, `.ql(ref)` files -- and the command automatically derives the names of the `.actual` files from them. Any test that doesn't have an `.actual` file will be silently ignored, which makes it easy to accept just the results of _failing_ tests from a previous run.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-accept#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-accept#primary-options)
#### [`<test|dir>...`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-accept#testdir)
Each argument is one of:
  * A `.ql` or `.qlref` file that defines a test to run.
  * A directory which will be searched recursively for tests to run.


#### [`--slice=<N/M>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-accept#--slicenm)
[Advanced] Divide the test cases into _M_ roughly equal-sized slices and process only the _N_ th of them. This can be used for manual parallelization of the testing process.
#### [`--[no-]strict-test-discovery`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-accept#--no-strict-test-discovery)
[Advanced] Only use queries that can be strongly identified as tests. This mode tries to distinguish between `.ql` files that define unit tests and `.ql` files that are meant to be useful queries. This option is used by tools, such as IDEs, that need to identify all unit tests in a directory tree without depending on previous knowledge of how the files in it are arranged.
Within a QL pack whose `qlpack.yml` declares a `tests` directory, all `.ql` files in that directory are considered tests, and `.ql` files outside it are ignored. In a QL pack that doesn't declare a `tests` directory, a `.ql` file is identified as a test only if it has a corresponding `.expected` file.
For consistency, `.qlref` files are limited by the same rules as `.ql` files even though a `.qlref` file cannot really be a non-test.
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-accept#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-accept#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-accept#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-accept#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-accept#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-accept#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-accept#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-accept#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
