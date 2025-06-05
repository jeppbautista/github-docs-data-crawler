  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [test extract](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-extract "test extract")


# test extract
[Plumbing] Build a dataset for a test directory.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-extract#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-extract#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-extract#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-extract#synopsis)
Shell```
codeql test extract [--source-root=<dir>] <options>... -- <testDirectory>

```
```
codeql test extract [--source-root=<dir>] <options>... -- <testDirectory>

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-extract#description)
[Plumbing] Build a dataset for a test directory.
Build a database for a specified test directory, without actually running any test queries. Outputs the path to the raw QL dataset to execute test queries against.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-extract#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-extract#primary-options)
#### [`<testDirectory>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-extract#testdirectory)
[Mandatory] The path to the test directory.
#### [`--database=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-extract#--databasedir)
Override the location of the database being created. By default it will be a subdirectory whose name is derived from the name of the test directory itself with '.testproj' appended.
#### [`-s, --source-root=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-extract#-s---source-rootdir)
[Advanced] The root source code directory, if different from the test directory.
#### [`--search-path=<dir>[:<dir>...]`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-extract#--search-pathdirdir)
A list of directories under which extractor packs may be found. The directories can either be the extractor packs themselves or directories that contain extractors as immediate subdirectories.
If the path contains multiple directory trees, their order defines precedence between them: if the target language is matched in more than one of the directory trees, the one given first wins.
The extractors bundled with the CodeQL toolchain itself will always be found, but if you need to use separately distributed extractors you need to give this option (or, better yet, set up `--search-path` in a per-user configuration file).
(Note: On Windows the path separator is `;`).
#### [`--cleanup`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-extract#--cleanup)
Remove the test database instead of creating it.
#### [`--[no-]show-extractor-output`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-extract#--no-show-extractor-output)
[Advanced] Show the output from extractor scripts that create test databases. This can be useful while developing or editing test cases. Beware that it can cause duplicated or malformed output if you use this with multiple threads!
#### [`--[no-]check-undefined-labels`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-extract#--no-check-undefined-labels)
[Advanced] Report errors for undefined labels.
#### [`--[no-]check-unused-labels`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-extract#--no-check-unused-labels)
[Advanced] Report errors for unused labels.
#### [`--[no-]check-repeated-labels`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-extract#--no-check-repeated-labels)
[Advanced] Report errors for repeated labels.
#### [`--[no-]check-redefined-labels`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-extract#--no-check-redefined-labels)
[Advanced] Report errors for redefined labels.
#### [`--[no-]check-use-before-definition`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-extract#--no-check-use-before-definition)
[Advanced] Report errors for labels used before they're defined.
#### [`--[no-]fail-on-trap-errors`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-extract#--no-fail-on-trap-errors)
[Advanced] Exit non-zero if an error occurs during trap import.
#### [`--[no-]include-location-in-star`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-extract#--no-include-location-in-star)
[Advanced] Construct entity IDs that encode the location in the TRAP file they came from. Can be useful for debugging of TRAP generators, but takes up a lot of space in the dataset.
#### [`--[no-]linkage-aware-import`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-extract#--no-linkage-aware-import)
[Advanced] Controls whether [codeql dataset import](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import) is linkage-aware _(default)_ or not. On projects where this part of database creation consumes too much memory, disabling this option may help them progress at the expense of database completeness.
Available since `v2.15.3`.
#### [`--format=<fmt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-extract#--formatfmt)
Select output format, either `text` _(default)_ or `json`.
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-extract#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-extract#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-extract#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-extract#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-extract#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-extract#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-extract#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/test-extract#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
