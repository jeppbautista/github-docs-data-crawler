  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [resolve ml-models](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ml-models "resolve ml-models")


# resolve ml-models
[Deprecated] [Experimental] [Deep plumbing] Determine accessible machine learning models.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ml-models#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ml-models#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ml-models#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ml-models#synopsis)
Shell```
codeql resolve ml-models <options>... -- <query|dir|suite|pack>...

```
```
codeql resolve ml-models <options>... -- <query|dir|suite|pack>...

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ml-models#description)
[Deprecated] [Deep plumbing] Determine accessible machine learning models.
This plumbing command is deprecated. Previously it resolved the set of GitHub-created machine learning models that were available to the query specifiers passed in as command line arguments.
It now returns an empty list of machine learning models.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ml-models#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ml-models#primary-options)
#### [`<query|dir|suite|pack>...`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ml-models#querydirsuitepack)
[Mandatory] Queries to execute. Each argument is in the form `scope/name@range:path` where:
  * `scope/name` is the qualified name of a CodeQL pack.
  * `range` is a semver range.
  * `path` is a file system path.


If a `scope/name` is specified, the `range` and `path` are optional. A missing `range` implies the latest version of the specified pack. A missing `path` implies the default query suite of the specified pack.
The `path` can be one of a `*.ql` query file, a directory containing one or more queries, or a `.qls` query suite file. If there is no pack name specified, then a `path` must be provided, and will be interpreted relative to the current working directory of the current process.
To specify a `path` that contains a literal `@` or `:`, use `path:` as a prefix to the argument, like this: `path:directory/with:and@/chars`.
If a `scope/name` and `path` are specified, then the `path` cannot be absolute. It is considered relative to the root of the CodeQL pack.
#### [`--search-path=<dir>[:<dir>...]`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ml-models#--search-pathdirdir)
A list of directories under which QL packs may be found. Each directory can either be a QL pack (or bundle of packs containing a `.codeqlmanifest.json` file at the root) or the immediate parent of one or more such directories.
If the path contains more than one directory, their order defines precedence between them: when a pack name that must be resolved is matched in more than one of the directory trees, the one given first wins.
Pointing this at a checkout of the open-source CodeQL repository ought to work when querying one of the languages that live there.
If you have checked out the CodeQL repository as a sibling of the unpacked CodeQL toolchain, you don't need to give this option; such sibling directories will always be searched for QL packs that cannot be found otherwise. (If this default does not work, it is strongly recommended to set up `--search-path` once and for all in a per-user configuration file).
(Note: On Windows the path separator is `;`).
#### [`--additional-packs=<dir>[:<dir>...]`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ml-models#--additional-packsdirdir)
If this list of directories is given, they will be searched for packs before the ones in `--search-path`. The order between these doesn't matter; it is an error if a pack name is found in two different places through this list.
This is useful if you're temporarily developing a new version of a pack that also appears in the default path. On the other hand, it is _not recommended_ to override this option in a config file; some internal actions will add this option on the fly, overriding any configured value.
(Note: On Windows the path separator is `;`).
### [Options for configuring the CodeQL package manager](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ml-models#options-for-configuring-the-codeql-package-manager)
#### [`--registries-auth-stdin`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ml-models#--registries-auth-stdin)
Authenticate to GitHub Enterprise Server Container registries by passing a comma-separated list of <registry_url>=<token> pairs.
For example, you can pass `https://containers.GHEHOSTNAME1/v2/=TOKEN1,https://containers.GHEHOSTNAME2/v2/=TOKEN2` to authenticate to two GitHub Enterprise Server instances.
This overrides the CODEQL_REGISTRIES_AUTH and GITHUB_TOKEN environment variables. If you only need to authenticate to the github.com Container registry, you can instead authenticate using the simpler `--github-auth-stdin` option.
#### [`--github-auth-stdin`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ml-models#--github-auth-stdin)
Authenticate to the github.com Container registry by passing a github.com GitHub Apps token or personal access token via standard input.
To authenticate to GitHub Enterprise Server Container registries, pass `--registries-auth-stdin` or use the CODEQL_REGISTRIES_AUTH environment variable.
This overrides the GITHUB_TOKEN environment variable.
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ml-models#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ml-models#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ml-models#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ml-models#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ml-models#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ml-models#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ml-models#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-ml-models#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
