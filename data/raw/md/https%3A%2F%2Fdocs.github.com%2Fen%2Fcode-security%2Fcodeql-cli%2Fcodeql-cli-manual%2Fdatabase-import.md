  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [database import](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import "database import")


# database import
[Advanced] [Plumbing] Import unfinalized database(s) into another unfinalized database.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import#synopsis)
Shell```
codeql database import [--dbscheme=<file>] [--threads=<num>] [--ram=<MB>] <options>... -- <database> <additionalDbs>...

```
```
codeql database import [--dbscheme=<file>] [--threads=<num>] [--ram=<MB>] <options>... -- <database> <additionalDbs>...

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import#description)
[Advanced] [Plumbing] Import unfinalized database(s) into another unfinalized database.
The result of this command is that the target database (the one in the _first_ argument) will be augmented with the data from all the other databases passed. In particular, TRAP files from the other databases will be imported and sources in them will be copied.
Note that this command will probably not have the desired effect in most cases. In particular, the resulting database may not correctly track dataflow between the partial databases that were combined. It is only intended to be used in certain advanced scenarios involving distributed build systems where special care has been taken in how the build was separated in order to ensure that the resulting final database is meaningful.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import#primary-options)
#### [`<database>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import#database)
[Mandatory] Path to the CodeQL database under construction. This must have been prepared for extraction with [codeql database init](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-init).
If the `--db-cluster` option is given, this is not a database itself, but a directory that _contains_ databases, and all of those databases will be processed together.
#### [`<additionalDbs>...`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import#additionaldbs)
[Mandatory] Paths to the unfinished database(s) that should imported into the first database.
If the `--db-cluster` option is given, it is expected that these will be database clusters rather than individual CodeQL databases.
#### [`--[no-]db-cluster`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import#--no-db-cluster)
Indicates that the directory given on the command line is not a database itself, but a directory that _contains_ one or more databases under construction. Those databases will be processed together.
### [Options for controlling the TRAP import operation](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import#options-for-controlling-the-trap-import-operation)
#### [`-S, --dbscheme=<file>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import#-s---dbschemefile)
[Advanced] Override the auto-detected dbscheme definition that the TRAP files are assumed to adhere to. Normally, this is taken from the database's extractor.
#### [`-j, --threads=<num>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import#-j---threadsnum)
Use this many threads for the import operation.
Defaults to 1. You can pass 0 to use one thread per core on the machine, or -_N_ to leave _N_ cores unused (except still use at least one thread).
#### [`-M, --ram=<MB>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import#-m---rammb)
Use this much memory for the import operation.
### [Options for checking imported TRAP](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import#options-for-checking-imported-trap)
#### [`--[no-]check-undefined-labels`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import#--no-check-undefined-labels)
[Advanced] Report errors for undefined labels.
#### [`--[no-]check-unused-labels`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import#--no-check-unused-labels)
[Advanced] Report errors for unused labels.
#### [`--[no-]check-repeated-labels`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import#--no-check-repeated-labels)
[Advanced] Report errors for repeated labels.
#### [`--[no-]check-redefined-labels`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import#--no-check-redefined-labels)
[Advanced] Report errors for redefined labels.
#### [`--[no-]check-use-before-definition`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import#--no-check-use-before-definition)
[Advanced] Report errors for labels used before they're defined.
#### [`--[no-]fail-on-trap-errors`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import#--no-fail-on-trap-errors)
[Advanced] Exit non-zero if an error occurs during trap import.
#### [`--[no-]include-location-in-star`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import#--no-include-location-in-star)
[Advanced] Construct entity IDs that encode the location in the TRAP file they came from. Can be useful for debugging of TRAP generators, but takes up a lot of space in the dataset.
#### [`--[no-]linkage-aware-import`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import#--no-linkage-aware-import)
[Advanced] Controls whether [codeql dataset import](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import) is linkage-aware _(default)_ or not. On projects where this part of database creation consumes too much memory, disabling this option may help them progress at the expense of database completeness.
Available since `v2.15.3`.
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-import#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
