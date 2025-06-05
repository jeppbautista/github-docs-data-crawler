  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [database unbundle](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-unbundle "database unbundle")


# database unbundle
Extracts a CodeQL database archive.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-unbundle#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-unbundle#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-unbundle#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-unbundle#synopsis)
Shell```
codeql database unbundle <options>... -- <archive>

```
```
codeql database unbundle <options>... -- <archive>

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-unbundle#description)
Extracts a CodeQL database archive.
This command extracts a CodeQL database archive created by [codeql database bundle](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-bundle). It is similar to using unzip to extract the database, but performs better in certain scenarios (for instance, unzip is very slow on Windows) and supports additional options such as setting the name of the database extracted.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-unbundle#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-unbundle#primary-options)
#### [`<archive>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-unbundle#archive)
[Mandatory] Path to the CodeQL database archive to unzip.
#### [`--name=<name>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-unbundle#--namename)
The name to give the CodeQL database created. If not provided, this will match whatever name the database has in the archive.
#### [`--target=<target>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-unbundle#--targettarget)
The directory to unzip the CodeQL database in. If not provided, this will default to the current working directory.
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-unbundle#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-unbundle#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-unbundle#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-unbundle#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-unbundle#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-unbundle#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-unbundle#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-unbundle#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
