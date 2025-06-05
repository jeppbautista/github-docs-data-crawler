  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [pack add](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-add "pack add")


# pack add
Adds a list of QL library packs with optional version ranges as dependencies of the current package, and then installs them.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-add#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-add#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-add#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-add#synopsis)
Shell```
codeql pack add <options>... -- <scope/name[@range]>...

```
```
codeql pack add <options>... -- <scope/name[@range]>...

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-add#description)
Adds a list of QL library packs with optional version ranges as dependencies of the current package, and then installs them.
This command modifies the qlpack.yml file of the current package. Formatting and comments will be removed.
Available since `v2.6.0`.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-add#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-add#primary-options)
#### [`<scope/name[@range]>...`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-add#scopenamerange)
[Mandatory] The scope, name, and optional version range of the pack to add to the dependency list.
If no version range is specified, or if the version range is specified as 'latest', the latest version of the pack is downloaded, and a dependency is added to qlpack.yml that allows any version that is compatible with the downloaded version.
If a single version is specified, that version of the pack is downloaded, and a dependency is added to qlpack.yml that allows any version that is compatible with the specified version.
If a version range is specified, the latest version of the pack that satisfies the specified range is downloaded, and a dependency is added to qlpack.yml with the specified version range.
#### [`--dir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-add#--dirdir)
The root directory of the package.
#### [`--registries-auth-stdin`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-add#--registries-auth-stdin)
Authenticate to GitHub Enterprise Server Container registries by passing a comma-separated list of <registry_url>=<token> pairs.
For example, you can pass `https://containers.GHEHOSTNAME1/v2/=TOKEN1,https://containers.GHEHOSTNAME2/v2/=TOKEN2` to authenticate to two GitHub Enterprise Server instances.
This overrides the CODEQL_REGISTRIES_AUTH and GITHUB_TOKEN environment variables. If you only need to authenticate to the github.com Container registry, you can instead authenticate using the simpler `--github-auth-stdin` option.
#### [`--github-auth-stdin`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-add#--github-auth-stdin)
Authenticate to the github.com Container registry by passing a github.com GitHub Apps token or personal access token via standard input.
To authenticate to GitHub Enterprise Server Container registries, pass `--registries-auth-stdin` or use the CODEQL_REGISTRIES_AUTH environment variable.
This overrides the GITHUB_TOKEN environment variable.
#### [`--[no-]allow-prerelease`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-add#--no-allow-prerelease)
Allow packs with pre-release version qualifiers (e.g., `X.Y.Z-qualifier`) to be used. Without this flag, pre-release packs will be ignored.
Available since `v2.11.3`.
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-add#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-add#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-add#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-add#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-add#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-add#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-add#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-add#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
