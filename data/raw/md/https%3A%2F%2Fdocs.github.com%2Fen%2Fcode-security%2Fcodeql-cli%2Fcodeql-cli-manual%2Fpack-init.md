  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [pack init](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-init "pack init")


# pack init
Initializes a qlpack in the specified directory.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-init#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-init#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-init#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-init#synopsis)
Shell```
codeql pack init [--dir=<dir>] [--extractor=<extractor>] <options>... -- <package-name>

```
```
codeql pack init [--dir=<dir>] [--extractor=<extractor>] <options>... -- <package-name>

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-init#description)
Initializes a qlpack in the specified directory.
The pack will be created in a child directory of the specified directory.
Available since `v2.6.0`.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-init#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-init#primary-options)
#### [`<package-name>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-init#package-name)
[Mandatory] The scope and name of the pack to create. Scope is only required if this pack is to be published.
#### [`--version=<semver>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-init#--versionsemver)
Initial version of the pack.
#### [`-d, --dir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-init#-d---dirdir)
The directory to create the pack in. Defaults to current working directory.
#### [`-e, --extractor=<extractor>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-init#-e---extractorextractor)
The extractor to use for this qlpack. Only useful if this pack contains tests.
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-init#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-init#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-init#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-init#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-init#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-init#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-init#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-init#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
