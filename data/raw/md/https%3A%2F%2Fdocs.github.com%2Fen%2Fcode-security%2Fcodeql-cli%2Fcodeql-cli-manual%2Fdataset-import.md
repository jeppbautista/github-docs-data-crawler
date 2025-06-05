  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [dataset import](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import "dataset import")


# dataset import
[Plumbing] Import a set of TRAP files to a raw dataset.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import#synopsis)
Shell```
codeql dataset import --dbscheme=<file> [--threads=<num>] <options>... -- <dataset> <trap>...

```
```
codeql dataset import --dbscheme=<file> [--threads=<num>] <options>... -- <dataset> <trap>...

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import#description)
[Plumbing] Import a set of TRAP files to a raw dataset.
Create a dataset by populating it with TRAP files, or add data from TRAP files to an existing dataset. Updating a dataset is only possible if it has the correct dbscheme _and_ its ID pool has been preserved from the initial import.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import#primary-options)
#### [`<dataset>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import#dataset)
[Mandatory] Path to the raw QL dataset to create or update. The directory will be created if it doesn't already exist.
#### [`<trap>...`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import#trap)
Paths to .trap(.gz) files to import, or to directories that will be recursively scanned for .trap(.gz) files. If no files are given, an empty dataset will be created.
#### [`-S, --dbscheme=<file>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import#-s---dbschemefile)
[Mandatory] The dbscheme definition that describes the TRAP files you want to import.
#### [`-j, --threads=<num>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import#-j---threadsnum)
Use this many threads for the import operation.
Defaults to 1. You can pass 0 to use one thread per core on the machine, or -_N_ to leave _N_ cores unused (except still use at least one thread).
#### [`--[no-]check-undefined-labels`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import#--no-check-undefined-labels)
[Advanced] Report errors for undefined labels.
#### [`--[no-]check-unused-labels`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import#--no-check-unused-labels)
[Advanced] Report errors for unused labels.
#### [`--[no-]check-repeated-labels`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import#--no-check-repeated-labels)
[Advanced] Report errors for repeated labels.
#### [`--[no-]check-redefined-labels`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import#--no-check-redefined-labels)
[Advanced] Report errors for redefined labels.
#### [`--[no-]check-use-before-definition`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import#--no-check-use-before-definition)
[Advanced] Report errors for labels used before they're defined.
#### [`--[no-]fail-on-trap-errors`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import#--no-fail-on-trap-errors)
[Advanced] Exit non-zero if an error occurs during trap import.
#### [`--[no-]include-location-in-star`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import#--no-include-location-in-star)
[Advanced] Construct entity IDs that encode the location in the TRAP file they came from. Can be useful for debugging of TRAP generators, but takes up a lot of space in the dataset.
#### [`--[no-]linkage-aware-import`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import#--no-linkage-aware-import)
[Advanced] Controls whether [codeql dataset import](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import) is linkage-aware _(default)_ or not. On projects where this part of database creation consumes too much memory, disabling this option may help them progress at the expense of database completeness.
Available since `v2.15.3`.
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
