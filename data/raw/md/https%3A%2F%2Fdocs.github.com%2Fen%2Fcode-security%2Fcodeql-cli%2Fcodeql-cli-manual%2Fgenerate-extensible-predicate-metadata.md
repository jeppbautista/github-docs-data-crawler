  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [generate extensible-predicate-metadata](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-extensible-predicate-metadata "generate extensible-predicate-metadata")


# generate extensible-predicate-metadata
[Experimental] [Deep plumbing] Report the extensible predicates found in the given pack.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-extensible-predicate-metadata#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-extensible-predicate-metadata#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-extensible-predicate-metadata#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-extensible-predicate-metadata#synopsis)
Shell```
codeql generate extensible-predicate-metadata <options>... -- <pack-root-dir>

```
```
codeql generate extensible-predicate-metadata <options>... -- <pack-root-dir>

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-extensible-predicate-metadata#description)
[Deep plumbing] Report the extensible predicates found in the given pack.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-extensible-predicate-metadata#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-extensible-predicate-metadata#primary-options)
#### [`<pack-root-dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-extensible-predicate-metadata#pack-root-dir)
[Mandatory] The pack root directory for which we are reporting extensible predicate metadata.
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-extensible-predicate-metadata#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-extensible-predicate-metadata#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-extensible-predicate-metadata#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-extensible-predicate-metadata#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-extensible-predicate-metadata#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-extensible-predicate-metadata#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-extensible-predicate-metadata#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-extensible-predicate-metadata#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
