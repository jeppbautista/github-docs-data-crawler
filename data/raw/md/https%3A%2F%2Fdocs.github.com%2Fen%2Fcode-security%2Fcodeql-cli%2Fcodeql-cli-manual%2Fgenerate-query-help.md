  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [generate query-help](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-query-help "generate query-help")


# generate query-help
Generate end-user query help from .qhelp files.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-query-help#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-query-help#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-query-help#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-query-help#synopsis)
Shell```
codeql generate query-help --format=<format> [--output=<dir|file>] <options>... -- <qhelp|mdhelp|query|dir|suite>...

```
```
codeql generate query-help --format=<format> [--output=<dir|file>] <options>... -- <qhelp|mdhelp|query|dir|suite>...

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-query-help#description)
Generate end-user query help from .qhelp files.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-query-help#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-query-help#primary-options)
#### [`<qhelp|mdhelp|query|dir|suite>...`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-query-help#qhelpmdhelpquerydirsuite)
[Mandatory] Query help files to render. Each argument is one of:
  * A .qhelp file to render.
  * A .md file to render.
  * A .ql file with a corresponding .qhelp or .md file to render.
  * A directory that will be searched recursively for .ql files with corresponding .qhelp or .md files.
  * A .qls file that defines a particular set of queries.
  * The basename of a "well-known" .qls file exported by one of the installed QL packs.


#### [`--format=<format>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-query-help#--formatformat)
[Mandatory] The format in which to render the documentation. One of:
`markdown`: GitHub flavored markdown.
`sarif-latest`: Static Analysis Results Interchange Format (SARIF), a JSON-based format for describing static analysis results. This format option uses the most recent supported version (v2.1.0). This option is not suitable for use in automation as it will produce different versions of SARIF between different CodeQL versions.
`sarifv2.1.0`: SARIF v2.1.0.
#### [`-o, --output=<dir|file>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-query-help#-o---outputdirfile)
A path to write the rendered documentation to. Usually this is a directory into which the rendered output will be written.
If only a single .qhelp or .ql file is provided, and no directory exists at the output path, the output will be written to a single file at that path.
If no output path is provided, only a single .qhelp or .ql file will be accepted, and the output will be written to stdout.
If an output directory is used, filenames _within_ the output directory will be derived from the .qhelp file names.
#### [`--warnings=<mode>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-query-help#--warningsmode)
How to handle warnings from the query help renderer. One of:
`hide`: Suppress warnings.
`show` _(default)_ : Print warnings but continue with rendering.
`error`: Treat warnings as errors.
#### [`--no-sarif-minify`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-query-help#--no-sarif-minify)
[SARIF formats only] Produce pretty-printed SARIF output. By default, SARIF output is minified to reduce the size of the output file.
### [Options for finding QL packs (which may be necessary to resolve query suites)](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-query-help#options-for-finding-ql-packs-which-may-be-necessary-to-resolve-query-suites)
#### [`--search-path=<dir>[:<dir>...]`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-query-help#--search-pathdirdir)
A list of directories under which QL packs may be found. Each directory can either be a QL pack (or bundle of packs containing a `.codeqlmanifest.json` file at the root) or the immediate parent of one or more such directories.
If the path contains more than one directory, their order defines precedence between them: when a pack name that must be resolved is matched in more than one of the directory trees, the one given first wins.
Pointing this at a checkout of the open-source CodeQL repository ought to work when querying one of the languages that live there.
If you have checked out the CodeQL repository as a sibling of the unpacked CodeQL toolchain, you don't need to give this option; such sibling directories will always be searched for QL packs that cannot be found otherwise. (If this default does not work, it is strongly recommended to set up `--search-path` once and for all in a per-user configuration file).
(Note: On Windows the path separator is `;`).
#### [`--additional-packs=<dir>[:<dir>...]`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-query-help#--additional-packsdirdir)
If this list of directories is given, they will be searched for packs before the ones in `--search-path`. The order between these doesn't matter; it is an error if a pack name is found in two different places through this list.
This is useful if you're temporarily developing a new version of a pack that also appears in the default path. On the other hand, it is _not recommended_ to override this option in a config file; some internal actions will add this option on the fly, overriding any configured value.
(Note: On Windows the path separator is `;`).
### [Options for configuring the CodeQL package manager](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-query-help#options-for-configuring-the-codeql-package-manager)
#### [`--registries-auth-stdin`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-query-help#--registries-auth-stdin)
Authenticate to GitHub Enterprise Server Container registries by passing a comma-separated list of <registry_url>=<token> pairs.
For example, you can pass `https://containers.GHEHOSTNAME1/v2/=TOKEN1,https://containers.GHEHOSTNAME2/v2/=TOKEN2` to authenticate to two GitHub Enterprise Server instances.
This overrides the CODEQL_REGISTRIES_AUTH and GITHUB_TOKEN environment variables. If you only need to authenticate to the github.com Container registry, you can instead authenticate using the simpler `--github-auth-stdin` option.
#### [`--github-auth-stdin`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-query-help#--github-auth-stdin)
Authenticate to the github.com Container registry by passing a github.com GitHub Apps token or personal access token via standard input.
To authenticate to GitHub Enterprise Server Container registries, pass `--registries-auth-stdin` or use the CODEQL_REGISTRIES_AUTH environment variable.
This overrides the GITHUB_TOKEN environment variable.
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-query-help#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-query-help#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-query-help#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-query-help#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-query-help#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-query-help#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-query-help#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-query-help#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
