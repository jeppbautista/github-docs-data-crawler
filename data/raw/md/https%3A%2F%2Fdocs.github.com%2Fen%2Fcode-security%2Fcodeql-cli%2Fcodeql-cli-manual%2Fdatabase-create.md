  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [database create](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create "database create")


# database create
Create a CodeQL database for a source tree that can be analyzed using one of the CodeQL products.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#synopsis)
Shell```
codeql database create [--language=<lang>[,<lang>...]] [--github-auth-stdin] [--github-url=<url>] [--source-root=<dir>] [--threads=<num>] [--ram=<MB>] [--command=<command>] [--extractor-option=<extractor-option-name=value>] <options>... -- <database>

```
```
codeql database create [--language=<lang>[,<lang>...]] [--github-auth-stdin] [--github-url=<url>] [--source-root=<dir>] [--threads=<num>] [--ram=<MB>] [--command=<command>] [--extractor-option=<extractor-option-name=value>] <options>... -- <database>

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#description)
Create a CodeQL database for a source tree that can be analyzed using one of the CodeQL products.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#primary-options)
#### [`<database>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#database)
[Mandatory] Path to the CodeQL database to create. This directory will be created, and _must not_ already exist (but its parent must).
If the `--db-cluster` option is given, this will not be a database itself, but a directory that will _contain_ databases for several languages built from the same source root.
It is important that this directory is not in a location that the build process will interfere with. For instance, the `target` directory of a Maven project would not be a suitable choice.
#### [`--[no-]overwrite`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#--no-overwrite)
[Advanced] If the database already exists, delete it and proceed with this command instead of failing. If the directory exists, but it does not look like a database, an error will be thrown.
#### [`--[no-]force-overwrite`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#--no-force-overwrite)
[Advanced] If the database already exists, delete it even if it does not look like a database and proceed with this command instead of failing. This option should be used with caution as it may recursively delete the entire database directory.
#### [`--codescanning-config=<file>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#--codescanning-configfile)
[Advanced] Read a Code Scanning configuration file specifying options on how to create the CodeQL databases and what queries to run in later steps. For more details on the format of this configuration file, refer to [Customizing your advanced setup for code scanning](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/customizing-your-advanced-setup-for-code-scanning). To run queries from this file in a later step, invoke [codeql database analyze](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-analyze) without any other queries specified.
#### [`--[no-]db-cluster`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#--no-db-cluster)
Instead of creating a single database, create a "cluster" of databases for different languages, each of which is a subdirectory of the directory given on the command line.
#### [`-l, --language=<lang>[,<lang>...]`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#-l---languagelanglang)
The language that the new database will be used to analyze.
Use [codeql resolve languages](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-languages) to get a list of the pluggable language extractors found on the search path.
When the `--db-cluster` option is given, this can appear multiple times, or the value can be a comma-separated list of languages.
If this option is omitted, and the source root being analysed is a checkout of a GitHub repository, the CodeQL CLI will make a call to the GitHub API to attempt to automatically determine what languages to analyse. Note that to be able to do this, a GitHub PAT token must be supplied either in the environment variable GITHUB_TOKEN or via standard input using the `--github-auth-stdin` option.
#### [`--build-mode=<mode>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#--build-modemode)
The build mode that will be used to create the database.
Choose your build mode based on the language you are analyzing:
`none`: The database will be created without building the source root. Available for C#, Java, JavaScript/TypeScript, Python, and Ruby.
`autobuild`: The database will be created by attempting to automatically build the source root. Available for C/C++, C#, Go, Java/Kotlin, and Swift.
`manual`: The database will be created by building the source root using a manually specified build command. Available for C/C++, C#, Go, Java/Kotlin, and Swift.
When creating a database with `--command`, there is no need to additionally specify '--build-mode manual'.
Available since `v2.16.4`.
#### [`-s, --source-root=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#-s---source-rootdir)
[Default: .] The root source code directory. In many cases, this will be the checkout root. Files within it are considered to be the primary source files for this database. In some output formats, files will be referred to by their relative path from this directory.
#### [`-j, --threads=<num>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#-j---threadsnum)
Use this many threads for the import operation, and pass it as a hint to any invoked build commands.
Defaults to 1. You can pass 0 to use one thread per core on the machine, or -_N_ to leave _N_ cores unused (except still use at least one thread).
#### [`-M, --ram=<MB>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#-m---rammb)
Use this much memory for the import operation, and pass it as a hint to any invoked build commands.
#### [`-c, --command=<command>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#-c---commandcommand)
For compiled languages, build commands that will cause the compiler to be invoked on the source code to analyze. These commands will be executed under an instrumentation environment that allows analysis of generated code and (in some cases) standard libraries.
If no build command is specified, the command attempts to figure out automatically how to build the source tree, based on heuristics from the selected language pack.
Beware that some combinations of multiple languages _require_ an explicit build command to be specified.
#### [`--no-cleanup`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#--no-cleanup)
[Advanced] Suppress all database cleanup after finalization. Useful for debugging purposes.
#### [`--no-pre-finalize`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#--no-pre-finalize)
[Advanced] Skip any pre-finalize script specified by the active CodeQL extractor.
#### [`--[no-]skip-empty`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#--no-skip-empty)
[Advanced] Output a warning instead of failing if a database is empty because no source code was seen during the build. The empty database will be left unfinalized.
#### [`--[no-]linkage-aware-import`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#--no-linkage-aware-import)
[Advanced] Controls whether [codeql dataset import](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/dataset-import) is linkage-aware _(default)_ or not. On projects where this part of database creation consumes too much memory, disabling this option may help them progress at the expense of database completeness.
Available since `v2.15.3`.
### [Baseline calculation options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#baseline-calculation-options)
#### [`--[no-]calculate-baseline`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#--no-calculate-baseline)
[Advanced] Calculate baseline information about the code being analyzed and add it to the database. By default, this is enabled unless the source root is the root of a filesystem. This flag can be used to either disable, or force the behavior to be enabled even in the root of the filesystem.
#### [`--[no-]sublanguage-file-coverage`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#--no-sublanguage-file-coverage)
[GitHub.com and GitHub Enterprise Server v3.12.0+ only] Use sub-language file coverage information. This calculates, displays, and exports separate file coverage information for languages which share a CodeQL extractor like C and C++, Java and Kotlin, and JavaScript and TypeScript.
Available since `v2.15.2`.
### [Extractor selection options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#extractor-selection-options)
#### [`--search-path=<dir>[:<dir>...]`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#--search-pathdirdir)
A list of directories under which extractor packs may be found. The directories can either be the extractor packs themselves or directories that contain extractors as immediate subdirectories.
If the path contains multiple directory trees, their order defines precedence between them: if the target language is matched in more than one of the directory trees, the one given first wins.
The extractors bundled with the CodeQL toolchain itself will always be found, but if you need to use separately distributed extractors you need to give this option (or, better yet, set up `--search-path` in a per-user configuration file).
(Note: On Windows the path separator is `;`).
### [Options to configure how to call the GitHub API to auto-detect languages.](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#options-to-configure-how-to-call-the-github-api-to-auto-detect-languages)
#### [`-a, --github-auth-stdin`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#-a---github-auth-stdin)
Accept a GitHub Apps token or personal access token via standard input.
This overrides the GITHUB_TOKEN environment variable.
#### [`-g, --github-url=<url>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#-g---github-urlurl)
URL of the GitHub instance to use. If omitted, the CLI will attempt to autodetect this from the checkout path and if this is not possible default to <https://github.com/>
### [Options to configure the package manager.](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#options-to-configure-the-package-manager)
#### [`--registries-auth-stdin`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#--registries-auth-stdin)
Authenticate to GitHub Enterprise Server Container registries by passing a comma-separated list of <registry_url>=<token> pairs.
For example, you can pass `https://containers.GHEHOSTNAME1/v2/=TOKEN1,https://containers.GHEHOSTNAME2/v2/=TOKEN2` to authenticate to two GitHub Enterprise Server instances.
This overrides the CODEQL_REGISTRIES_AUTH and GITHUB_TOKEN environment variables. If you only need to authenticate to the github.com Container registry, you can instead authenticate using the simpler `--github-auth-stdin` option.
### [Low-level dataset cleanup options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#low-level-dataset-cleanup-options)
#### [`--max-disk-cache=<MB>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#--max-disk-cachemb)
Set the maximum amount of space that the disk cache for intermediate query results can use.
If this size is not configured explicitly, the evaluator will try to use a "reasonable" amount of cache space, based on the size of the dataset and the complexity of the queries. Explicitly setting a higher limit than this default usage will enable additional caching which can speed up later queries.
#### [`--min-disk-free=<MB>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#--min-disk-freemb)
[Advanced] Set target amount of free space on file system.
If `--max-disk-cache` is not given, the evaluator will try hard to curtail disk cache usage if the free space on the file system drops below this value.
#### [`--min-disk-free-pct=<pct>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#--min-disk-free-pctpct)
[Advanced] Set target fraction of free space on file system.
If `--max-disk-cache` is not given, the evaluator will try hard to curtail disk cache usage if the free space on the file system drops below this percentage.
#### [`--cache-cleanup=<mode>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#--cache-cleanupmode)
Select how aggressively to trim the cache. Choices include:
`clear`: Remove the entire cache, trimming down to the state of a freshly extracted dataset
`trim` _(default)_ : Trim everything except explicitly "cached" predicates.
`fit`: Simply make sure the defined size limits for the disk cache are observed, deleting as many intermediates as necessary.
#### [`--cleanup-upgrade-backups`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#--cleanup-upgrade-backups)
Delete any backup directories resulting from database upgrades.
### [Tracing options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#tracing-options)
#### [`--no-tracing`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#--no-tracing)
[Advanced] Do not trace the specified command, instead rely on it to produce all necessary data directly.
#### [`--extra-tracing-config=<tracing-config.lua>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#--extra-tracing-configtracing-configlua)
[Advanced] The path to a tracer configuration file. It may be used to modify the behavior of the build tracer. It may be used to pick out compiler processes that run as part of the build command, and trigger the execution of other tools. The extractors will provide default tracer configuration files that should work in most situations.
### [Build command customization options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#build-command-customization-options)
#### [`--working-dir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#--working-dirdir)
[Advanced] The directory in which the specified command should be executed. If this argument is not provided, the command is executed in the value of `--source-root` passed to [codeql database create](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create), if one exists. If no `--source-root` argument is provided, the command is executed in the current working directory.
#### [`--no-run-unnecessary-builds`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#--no-run-unnecessary-builds)
[Advanced] Only run the specified build command(s) if a database under construction uses an extractor that depends on tracing a build process. If this option is not given, the command will be executed even when CodeQL doesn't need it, on the assumption that you need its side effects for other reasons.
### [Options to control extractor behavior](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#options-to-control-extractor-behavior)
#### [`-O, --extractor-option=<extractor-option-name=value>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#-o---extractor-optionextractor-option-namevalue)
Set options for CodeQL extractors. `extractor-option-name` should be of the form extractor_name.group1.group2.option_name or group1.group2.option_name. If `extractor_option_name` starts with an extractor name, the indicated extractor must declare the option group1.group2.option_name. Otherwise, any extractor that declares the option group1.group2.option_name will have the option set. `value` can be any string that does not contain a newline.
You can use this command-line option repeatedly to set multiple extractor options. If you provide multiple values for the same extractor option, the behavior depends on the type that the extractor option expects. String options will use the last value provided. Array options will use all the values provided, in order. Extractor options specified using this command-line option are processed after extractor options given via `--extractor-options-file`.
When passed to [codeql database init](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-init) or `codeql database begin-tracing`, the options will only be applied to the indirect tracing environment. If your workflow also makes calls to [codeql database trace-command](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command) then the options also need to be passed there if desired.
See <https://codeql.github.com/docs/codeql-cli/extractor-options> for more information on CodeQL extractor options, including how to list the options declared by each extractor.
#### [`--extractor-options-file=<extractor-options-bundle-file>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#--extractor-options-fileextractor-options-bundle-file)
Specify extractor option bundle files. An extractor option bundle file is a JSON file (extension `.json`) or YAML file (extension `.yaml` or `.yml`) that sets extractor options. The file must have the top-level map key 'extractor' and, under it, extractor names as second-level map keys. Further levels of maps represent nested extractor groups, and string and array options are map entries with string and array values.
Extractor option bundle files are read in the order they are specified. If different extractor option bundle files specify the same extractor option, the behavior depends on the type that the extractor option expects. String options will use the last value provided. Array options will use all the values provided, in order. Extractor options specified using this command-line option are processed before extractor options given via `--extractor-option`.
When passed to [codeql database init](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-init) or `codeql database begin-tracing`, the options will only be applied to the indirect tracing environment. If your workflow also makes calls to [codeql database trace-command](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command) then the options also need to be passed there if desired.
See <https://codeql.github.com/docs/codeql-cli/extractor-options> for more information on CodeQL extractor options, including how to list the options declared by each extractor.
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
