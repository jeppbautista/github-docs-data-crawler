  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [pack packlist](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-packlist "pack packlist")


# pack packlist
[Plumbing] Compute the set of files to be included in a QL query pack or library pack.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-packlist#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-packlist#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-packlist#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-packlist#synopsis)
Shell```
codeql pack packlist <options>... -- <dir>

```
```
codeql pack packlist <options>... -- <dir>

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-packlist#description)
[Plumbing] Compute the set of files to be included in a QL query pack or library pack.
This command determines the set of files to be included in the pack based on the patterns specified in any `.gitignore` files present in the pack or in an ancestor directory.
Available since `v2.6.0`.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-packlist#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-packlist#primary-options)
#### [`<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-packlist#dir)
The root directory of the package.
#### [`--format=<fmt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-packlist#--formatfmt)
Select output format, either `text` _(default)_ or `json`.
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-packlist#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-packlist#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-packlist#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-packlist#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-packlist#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-packlist#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-packlist#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-packlist#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
