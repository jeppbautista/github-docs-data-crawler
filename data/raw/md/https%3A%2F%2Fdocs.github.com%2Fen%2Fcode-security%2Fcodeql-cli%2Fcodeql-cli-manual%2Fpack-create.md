  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [pack create](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create "pack create")


# pack create
[Plumbing] Builds the contents of a QL package from source code.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#synopsis)
Shell```
codeql pack create [--output=<output>] [--threads=<num>] [--ram=<MB>] <options>... -- <dir>

```
```
codeql pack create [--output=<output>] [--threads=<num>] [--ram=<MB>] <options>... -- <dir>

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#description)
[Plumbing] Builds the contents of a QL package from source code.
This command builds the complete contents of a QL package, including the original source code, library dependencies, compiled queries, and package metadata.
Available since `v2.6.0`.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#primary-options)
#### [`<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#dir)
The root directory of the package.
#### [`-o, --output=<output>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#-o---outputoutput)
The output directory to write the built package to.
Defaults to `./.codeql/pack`.
#### [`--format=<fmt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#--formatfmt)
Select output format, either `text` _(default)_ or `json`.
#### [`-j, --threads=<num>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#-j---threadsnum)
Use this many threads to compile queries.
Defaults to 1. You can pass 0 to use one thread per core on the machine, or -_N_ to leave _N_ cores unused (except still use at least one thread).
#### [`-M, --ram=<MB>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#-m---rammb)
Set total amount of RAM that the compiler should be allowed to use.
#### [`--no-precompile`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#--no-precompile)
[Advanced] Avoid precompiling the compilation cache in the pack output directory. This will reduce the size of the pack and the time it takes to create it, but will require compilation before the pack can be run. Only meaningful for query packs.
#### [`--no-validate-extensions`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#--no-validate-extensions)
[Advanced] Avoid validating data extensions as part of the compile step.
Available since `v2.13.3`.
#### [`--no-overwrite`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#--no-overwrite)
[Advanced] Avoid recompiling and overwriting any existing compiled output from a previous invocation of this command.
### [Options to set up compilation environment](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#options-to-set-up-compilation-environment)
#### [`--search-path=<dir>[:<dir>...]`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#--search-pathdirdir)
A list of directories under which QL packs may be found. Each directory can either be a QL pack (or bundle of packs containing a `.codeqlmanifest.json` file at the root) or the immediate parent of one or more such directories.
If the path contains more than one directory, their order defines precedence between them: when a pack name that must be resolved is matched in more than one of the directory trees, the one given first wins.
Pointing this at a checkout of the open-source CodeQL repository ought to work when querying one of the languages that live there.
If you have checked out the CodeQL repository as a sibling of the unpacked CodeQL toolchain, you don't need to give this option; such sibling directories will always be searched for QL packs that cannot be found otherwise. (If this default does not work, it is strongly recommended to set up `--search-path` once and for all in a per-user configuration file).
(Note: On Windows the path separator is `;`).
#### [`--additional-packs=<dir>[:<dir>...]`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#--additional-packsdirdir)
If this list of directories is given, they will be searched for packs before the ones in `--search-path`. The order between these doesn't matter; it is an error if a pack name is found in two different places through this list.
This is useful if you're temporarily developing a new version of a pack that also appears in the default path. On the other hand, it is _not recommended_ to override this option in a config file; some internal actions will add this option on the fly, overriding any configured value.
(Note: On Windows the path separator is `;`).
#### [`--library-path=<dir>[:<dir>...]`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#--library-pathdirdir)
[Advanced] An optional list of directories that will be added to the raw import search path for QL libraries. This should only be used if you're using QL libraries that have not been packaged as QL packs.
(Note: On Windows the path separator is `;`).
#### [`--dbscheme=<file>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#--dbschemefile)
[Advanced] Explicitly define which dbscheme queries should be compiled against. This should only be given by callers that are extremely sure what they're doing.
#### [`--compilation-cache=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#--compilation-cachedir)
[Advanced] Specify an additional directory to use as a compilation cache.
#### [`--no-default-compilation-cache`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#--no-default-compilation-cache)
[Advanced] Don't use compilation caches in standard locations such as in the QL pack containing the query or in the CodeQL toolchain directory.
### [Options for configuring the CodeQL package manager](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#options-for-configuring-the-codeql-package-manager)
#### [`--registries-auth-stdin`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#--registries-auth-stdin)
Authenticate to GitHub Enterprise Server Container registries by passing a comma-separated list of <registry_url>=<token> pairs.
For example, you can pass `https://containers.GHEHOSTNAME1/v2/=TOKEN1,https://containers.GHEHOSTNAME2/v2/=TOKEN2` to authenticate to two GitHub Enterprise Server instances.
This overrides the CODEQL_REGISTRIES_AUTH and GITHUB_TOKEN environment variables. If you only need to authenticate to the github.com Container registry, you can instead authenticate using the simpler `--github-auth-stdin` option.
#### [`--github-auth-stdin`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#--github-auth-stdin)
Authenticate to the github.com Container registry by passing a github.com GitHub Apps token or personal access token via standard input.
To authenticate to GitHub Enterprise Server Container registries, pass `--registries-auth-stdin` or use the CODEQL_REGISTRIES_AUTH environment variable.
This overrides the GITHUB_TOKEN environment variable.
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/pack-create#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
