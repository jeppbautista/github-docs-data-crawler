  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [database interpret-results](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results "database interpret-results")


# database interpret-results
[Plumbing] Interpret computed query results into meaningful formats such as SARIF or CSV.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#synopsis)
Shell```
codeql database interpret-results --format=<format> --output=<output> [--threads=<num>] <options>... -- <database> <file|dir|suite>...

```
```
codeql database interpret-results --format=<format> --output=<output> [--threads=<num>] <options>... -- <database> <file|dir|suite>...

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#description)
[Plumbing] Interpret computed query results into meaningful formats such as SARIF or CSV.
The results should have been computed and stored in a CodeQL database directory using [codeql database run-queries](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-run-queries). (Usually you'd want to do these steps together, by using [codeql database analyze](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-analyze)).
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#primary-options)
#### [`<database>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#database)
[Mandatory] Path to the CodeQL database that has been queried.
#### [`<file|dir|suite>...`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#filedirsuite)
Repeat the specification of which queries were executed here.
If omitted, the CLI will determine a suitable set of queries using the same logic as [codeql database run-queries](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-run-queries).
(In a future version it ought to be possible to omit this and instead interpret all results that are found in the database. That glorious future is not yet. Sorry.)
#### [`--format=<format>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#--formatformat)
[Mandatory] The format in which to write the results. One of:
`csv`: Formatted comma-separated values, including columns with both rule and alert metadata.
`sarif-latest`: Static Analysis Results Interchange Format (SARIF), a JSON-based format for describing static analysis results. This format option uses the most recent supported version (v2.1.0). This option is not suitable for use in automation as it will produce different versions of SARIF between different CodeQL versions.
`sarifv2.1.0`: SARIF v2.1.0.
`graphtext`: A textual format representing a graph. Only compatible with queries with @kind graph.
`dgml`: Directed Graph Markup Language, an XML-based format for describing graphs. Only compatible with queries with @kind graph.
`dot`: Graphviz DOT language, a text-based format for describing graphs. Only compatible with queries with @kind graph.
#### [`-o, --output=<output>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#-o---outputoutput)
[Mandatory] The output path to write results to. For graph formats this should be a directory, and the result (or results if this command supports interpreting more than one query) will be written within that directory.
#### [`--max-paths=<maxPaths>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#--max-pathsmaxpaths)
The maximum number of paths to produce for each alert with paths. (Default: 4)
#### [`--[no-]sarif-add-file-contents`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#--no-sarif-add-file-contents)
[SARIF formats only] Include the full file contents for all files referenced in at least one result.
#### [`--[no-]sarif-add-snippets`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#--no-sarif-add-snippets)
[SARIF formats only] Include code snippets for each location mentioned in the results, with two lines of context before and after the reported location.
#### [`--[no-]sarif-add-query-help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#--no-sarif-add-query-help)
[SARIF formats only] [Deprecated] Include Markdown query help for all queries. It loads query help for /path/to/query.ql from the /path/to/query.md file. If this flag is not supplied the default behavior is to include help only for custom queries i.e. those in query packs which are not of the form `codeql/<lang&rt;-queries`. This option has no effect when passed to [codeql bqrs interpret](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret).
#### [`--sarif-include-query-help=<mode>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#--sarif-include-query-helpmode)
[SARIF formats only] Specify whether to include query help in the SARIF output. One of:
`always`: Include query help for all queries.
`custom_queries_only` _(default)_ : Include query help only for custom queries i.e. those in query packs which are not of the form `codeql/<lang&rt;-queries`.
`never`: Do not include query help for any queries.
This option has no effect when passed to [codeql bqrs interpret](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret).
Available since `v2.15.2`.
#### [`--no-sarif-include-alert-provenance`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#--no-sarif-include-alert-provenance)
[Advanced] [SARIF formats only] Do not include alert provenance information in the SARIF output.
Available since `v2.18.1`.
#### [`--[no-]sarif-group-rules-by-pack`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#--no-sarif-group-rules-by-pack)
[SARIF formats only] Place the rule object for each query under its corresponding QL pack in the `<run>.tool.extensions` property. This option has no effect when passed to [codeql bqrs interpret](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret).
#### [`--[no-]sarif-multicause-markdown`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#--no-sarif-multicause-markdown)
[SARIF formats only] For alerts that have multiple causes, include them as a Markdown-formatted itemized list in the output in addition to as a plain string.
#### [`--no-sarif-minify`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#--no-sarif-minify)
[SARIF formats only] Produce pretty-printed SARIF output. By default, SARIF output is minified to reduce the size of the output file.
#### [`--sarif-run-property=<String=String>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#--sarif-run-propertystringstring)
[SARIF formats only] A key value pair to add to the generated SARIF 'run' property bag. Can be repeated.
#### [`--no-group-results`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#--no-group-results)
[SARIF formats only] Produce one result per message, rather than one result per unique location.
#### [`--csv-location-format=<csvLocationFormat>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#--csv-location-formatcsvlocationformat)
The format in which to produce locations in CSV output. One of: uri, line-column, offset-length. (Default: line-column)
#### [`--dot-location-url-format=<dotLocationUrlFormat>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#--dot-location-url-formatdotlocationurlformat)
A format string defining the format in which to produce file location URLs in DOT output. The following place holders can be used {path} {start:line} {start:column} {end:line} {end:column}, {offset}, {length}
#### [`--[no-]sublanguage-file-coverage`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#--no-sublanguage-file-coverage)
[GitHub.com and GitHub Enterprise Server v3.12.0+ only] Use sub-language file coverage information. This calculates, displays, and exports separate file coverage information for languages which share a CodeQL extractor like C and C++, Java and Kotlin, and JavaScript and TypeScript.
Available since `v2.15.2`.
#### [`--sarif-category=<category>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#--sarif-categorycategory)
[SARIF formats only] [Recommended] Specify a category for this analysis to include in the SARIF output. A category can be used to distinguish multiple analyses performed on the same commit and repository, but on different languages or different parts of the code.
If you analyze the same version of a code base in several different ways (e.g., for different languages) and upload the results to GitHub for presentation in Code Scanning, this value should differ between each of the analyses, which tells Code Scanning that the analyses _supplement_ rather than _supersede_ each other. (The values should be consistent between runs of the same analysis for _different_ versions of the code base.)
This value will appear (with a trailing slash appended if not already present) as the `<run>.automationDetails.id` property.
#### [`-j, --threads=<num>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#-j---threadsnum)
The number of threads used for computing paths.
Defaults to 1. You can pass 0 to use one thread per core on the machine, or -_N_ to leave _N_ cores unused (except still use at least one thread).
#### [`--no-database-extension-packs`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#--no-database-extension-packs)
[Advanced] Omit extension packs stored in the database during database creation, either from a Code Scanning configuration file or from extension files stored in the 'extensions' directory of the analyzed codebase.
#### [`--[no-]print-diagnostics-summary`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#--no-print-diagnostics-summary)
Print a summary of the analyzed diagnostics to standard output.
#### [`--[no-]print-metrics-summary`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#--no-print-metrics-summary)
Print a summary of the analyzed metrics to standard output.
#### [`--[no-]print-baseline-loc`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#--no-print-baseline-loc)
Print the baseline lines of code counted to standard output.
### [Options for configuring the CodeQL package manager](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#options-for-configuring-the-codeql-package-manager)
#### [`--registries-auth-stdin`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#--registries-auth-stdin)
Authenticate to GitHub Enterprise Server Container registries by passing a comma-separated list of <registry_url>=<token> pairs.
For example, you can pass `https://containers.GHEHOSTNAME1/v2/=TOKEN1,https://containers.GHEHOSTNAME2/v2/=TOKEN2` to authenticate to two GitHub Enterprise Server instances.
This overrides the CODEQL_REGISTRIES_AUTH and GITHUB_TOKEN environment variables. If you only need to authenticate to the github.com Container registry, you can instead authenticate using the simpler `--github-auth-stdin` option.
#### [`--github-auth-stdin`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#--github-auth-stdin)
Authenticate to the github.com Container registry by passing a github.com GitHub Apps token or personal access token via standard input.
To authenticate to GitHub Enterprise Server Container registries, pass `--registries-auth-stdin` or use the CODEQL_REGISTRIES_AUTH environment variable.
This overrides the GITHUB_TOKEN environment variable.
### [Options to specify which extensions to use when interpreting the results](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#options-to-specify-which-extensions-to-use-when-interpreting-the-results)
####  [`--model-packs=<`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#--model-packsnamerange)name@range>...
A list of CodeQL pack names, each with an optional version range, to be used as model packs to customize the queries that are about to be evaluated.
### [Options for finding QL packs (which may be necessary to interpret query suites)](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#options-for-finding-ql-packs-which-may-be-necessary-to-interpret-query-suites)
#### [`--search-path=<dir>[:<dir>...]`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#--search-pathdirdir)
A list of directories under which QL packs may be found. Each directory can either be a QL pack (or bundle of packs containing a `.codeqlmanifest.json` file at the root) or the immediate parent of one or more such directories.
If the path contains more than one directory, their order defines precedence between them: when a pack name that must be resolved is matched in more than one of the directory trees, the one given first wins.
Pointing this at a checkout of the open-source CodeQL repository ought to work when querying one of the languages that live there.
If you have checked out the CodeQL repository as a sibling of the unpacked CodeQL toolchain, you don't need to give this option; such sibling directories will always be searched for QL packs that cannot be found otherwise. (If this default does not work, it is strongly recommended to set up `--search-path` once and for all in a per-user configuration file).
(Note: On Windows the path separator is `;`).
#### [`--additional-packs=<dir>[:<dir>...]`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#--additional-packsdirdir)
If this list of directories is given, they will be searched for packs before the ones in `--search-path`. The order between these doesn't matter; it is an error if a pack name is found in two different places through this list.
This is useful if you're temporarily developing a new version of a pack that also appears in the default path. On the other hand, it is _not recommended_ to override this option in a config file; some internal actions will add this option on the fly, overriding any configured value.
(Note: On Windows the path separator is `;`).
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
