  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [bqrs diff](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-diff "bqrs diff")


# bqrs diff
Compute the difference between two result sets.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-diff#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-diff#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-diff#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-diff#synopsis)
Shell```
codeql bqrs diff <options>... -- <file1> <file2>

```
```
codeql bqrs diff <options>... -- <file1> <file2>

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-diff#description)
Compute the difference between two result sets.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-diff#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-diff#primary-options)
#### [`<file1>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-diff#file1)
[Mandatory] First BQRS file to compare.
#### [`<file2>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-diff#file2)
[Mandatory] Second BQRS file to compare.
#### [`--left=<file>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-diff#--leftfile)
Write rows only present in `file1` to this file.
#### [`--right=<file>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-diff#--rightfile)
Write rows only present in `file2` to this file.
#### [`--both=<file>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-diff#--bothfile)
Write rows present in both `file1` and `file2` to this file.
#### [`--retain-result-sets=<result-set>[,<result-set>...]`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-diff#--retain-result-setsresult-setresult-set)
Comma-separated list of result set names to copy directly to the corresponding output instead of comparing. If --both is given, that output is taken from `file1`. Defaults to 'nodes,edges,subpaths' to simplify handling of path-problem results.
#### [`--[no-]compare-internal-ids`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-diff#--no-compare-internal-ids)
[Advanced] Include internal entity IDs in the comparison. Entity IDs are not comparable across databases, but for result sets that originate from the same database this can help distinguish entities with the same location and label.
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-diff#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-diff#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-diff#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-diff#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-diff#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-diff#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-diff#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-diff#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
