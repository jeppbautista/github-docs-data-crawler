  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [dataset measure](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-measure "dataset measure")


# dataset measure
[Plumbing] Collect statistics about the relations in a particular dataset.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-measure#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-measure#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-measure#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-measure#synopsis)
Shell```
codeql dataset measure --output=<file> [--threads=<num>] <options>... -- <dataset>

```
```
codeql dataset measure --output=<file> [--threads=<num>] <options>... -- <dataset>

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-measure#description)
[Plumbing] Collect statistics about the relations in a particular dataset.
This command is typically only used when developing a CodeQL extractor, after a change that affects the database schema and which therefore needs to have an accompanying change to the statistics used by the query optimizer.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-measure#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-measure#primary-options)
#### [`<dataset>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-measure#dataset)
[Mandatory] Path to the raw QL dataset to measure.
#### [`-o, --output=<file>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-measure#-o---outputfile)
[Mandatory] The output file to which statistics should be written, typically with a '.dbscheme.stats' extension.
#### [`-j, --threads=<num>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-measure#-j---threadsnum)
The number of concurrent threads to use.
Defaults to 1. You can pass 0 to use one thread per core on the machine, or -_N_ to leave _N_ cores unused (except still use at least one thread).
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-measure#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-measure#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-measure#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-measure#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-measure#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-measure#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-measure#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-measure#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
