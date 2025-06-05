  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [bqrs interpret](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret "bqrs interpret")


# bqrs interpret
[Plumbing] Interpret data in a single BQRS.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#synopsis)
Shell```
codeql bqrs interpret --format=<format> --output=<output> -t=<String=String> [--threads=<num>] [--source-archive=<sourceArchive>] [--source-location-prefix=<sourceLocationPrefix>] <options>... -- <bqrs-file>

```
```
codeql bqrs interpret --format=<format> --output=<output> -t=<String=String> [--threads=<num>] [--source-archive=<sourceArchive>] [--source-location-prefix=<sourceLocationPrefix>] <options>... -- <bqrs-file>

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#description)
[Plumbing] Interpret data in a single BQRS.
A command that interprets a single BQRS file according to the provided metadata and generates output in the specified format.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#primary-options)
#### [`<bqrs-file>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#bqrs-file)
[Mandatory] The BQRS file to interpret.
#### [`--format=<format>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#--formatformat)
[Mandatory] The format in which to write the results. One of:
`csv`: Formatted comma-separated values, including columns with both rule and alert metadata.
`sarif-latest`: Static Analysis Results Interchange Format (SARIF), a JSON-based format for describing static analysis results. This format option uses the most recent supported version (v2.1.0). This option is not suitable for use in automation as it will produce different versions of SARIF between different CodeQL versions.
`sarifv2.1.0`: SARIF v2.1.0.
`graphtext`: A textual format representing a graph. Only compatible with queries with @kind graph.
`dgml`: Directed Graph Markup Language, an XML-based format for describing graphs. Only compatible with queries with @kind graph.
`dot`: Graphviz DOT language, a text-based format for describing graphs. Only compatible with queries with @kind graph.
#### [`-o, --output=<output>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#-o---outputoutput)
[Mandatory] The output path to write results to. For graph formats this should be a directory, and the result (or results if this command supports interpreting more than one query) will be written within that directory.
#### [`-t=<String=String>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#-tstringstring)
[Mandatory] A query metadata key value pair. Repeat for each piece of metadata. At least the keys 'kind' and 'id' must be specified. Keys do not need to be prefixed with @.
#### [`--max-paths=<maxPaths>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#--max-pathsmaxpaths)
The maximum number of paths to produce for each alert with paths. (Default: 4)
#### [`--[no-]sarif-add-file-contents`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#--no-sarif-add-file-contents)
[SARIF formats only] Include the full file contents for all files referenced in at least one result.
#### [`--[no-]sarif-add-snippets`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#--no-sarif-add-snippets)
[SARIF formats only] Include code snippets for each location mentioned in the results, with two lines of context before and after the reported location.
#### [`--[no-]sarif-add-query-help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#--no-sarif-add-query-help)
[SARIF formats only] [Deprecated] Include Markdown query help for all queries. It loads query help for /path/to/query.ql from the /path/to/query.md file. If this flag is not supplied the default behavior is to include help only for custom queries i.e. those in query packs which are not of the form `codeql/<lang&rt;-queries`. This option has no effect when passed to [codeql bqrs interpret](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret).
#### [`--sarif-include-query-help=<mode>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#--sarif-include-query-helpmode)
[SARIF formats only] Specify whether to include query help in the SARIF output. One of:
`always`: Include query help for all queries.
`custom_queries_only` _(default)_ : Include query help only for custom queries i.e. those in query packs which are not of the form `codeql/<lang&rt;-queries`.
`never`: Do not include query help for any queries.
This option has no effect when passed to [codeql bqrs interpret](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret).
Available since `v2.15.2`.
#### [`--no-sarif-include-alert-provenance`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#--no-sarif-include-alert-provenance)
[Advanced] [SARIF formats only] Do not include alert provenance information in the SARIF output.
Available since `v2.18.1`.
#### [`--[no-]sarif-group-rules-by-pack`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#--no-sarif-group-rules-by-pack)
[SARIF formats only] Place the rule object for each query under its corresponding QL pack in the `<run>.tool.extensions` property. This option has no effect when passed to [codeql bqrs interpret](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret).
#### [`--[no-]sarif-multicause-markdown`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#--no-sarif-multicause-markdown)
[SARIF formats only] For alerts that have multiple causes, include them as a Markdown-formatted itemized list in the output in addition to as a plain string.
#### [`--no-sarif-minify`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#--no-sarif-minify)
[SARIF formats only] Produce pretty-printed SARIF output. By default, SARIF output is minified to reduce the size of the output file.
#### [`--sarif-run-property=<String=String>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#--sarif-run-propertystringstring)
[SARIF formats only] A key value pair to add to the generated SARIF 'run' property bag. Can be repeated.
#### [`--no-group-results`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#--no-group-results)
[SARIF formats only] Produce one result per message, rather than one result per unique location.
#### [`--csv-location-format=<csvLocationFormat>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#--csv-location-formatcsvlocationformat)
The format in which to produce locations in CSV output. One of: uri, line-column, offset-length. (Default: line-column)
#### [`--dot-location-url-format=<dotLocationUrlFormat>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#--dot-location-url-formatdotlocationurlformat)
A format string defining the format in which to produce file location URLs in DOT output. The following place holders can be used {path} {start:line} {start:column} {end:line} {end:column}, {offset}, {length}
#### [`--[no-]sublanguage-file-coverage`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#--no-sublanguage-file-coverage)
[GitHub.com and GitHub Enterprise Server v3.12.0+ only] Use sub-language file coverage information. This calculates, displays, and exports separate file coverage information for languages which share a CodeQL extractor like C and C++, Java and Kotlin, and JavaScript and TypeScript.
Available since `v2.15.2`.
#### [`--sarif-category=<category>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#--sarif-categorycategory)
[SARIF formats only] [Recommended] Specify a category for this analysis to include in the SARIF output. A category can be used to distinguish multiple analyses performed on the same commit and repository, but on different languages or different parts of the code.
If you analyze the same version of a code base in several different ways (e.g., for different languages) and upload the results to GitHub for presentation in Code Scanning, this value should differ between each of the analyses, which tells Code Scanning that the analyses _supplement_ rather than _supersede_ each other. (The values should be consistent between runs of the same analysis for _different_ versions of the code base.)
This value will appear (with a trailing slash appended if not already present) as the `<run>.automationDetails.id` property.
#### [`-j, --threads=<num>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#-j---threadsnum)
The number of threads used for computing paths.
Defaults to 1. You can pass 0 to use one thread per core on the machine, or -_N_ to leave _N_ cores unused (except still use at least one thread).
#### [`--column-kind=<columnKind>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#--column-kindcolumnkind)
[SARIF only] The column kind used to interpret location columns. One of: utf8, utf16, utf32, bytes.
#### [`--[no-]unicode-new-lines`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#--no-unicode-new-lines)
[SARIF only] Whether the unicode newline characters LS (Line Separator, U+2028) and PS (Paragraph Separator, U+2029) are considered as new lines when interpreting location line numbers.
### [Source archive options - must be given together or not at all](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#source-archive-options---must-be-given-together-or-not-at-all)
#### [`-s, --source-archive=<sourceArchive>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#-s---source-archivesourcearchive)
The directory or zip file containing the source archive.
#### [`-p, --source-location-prefix=<sourceLocationPrefix>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#-p---source-location-prefixsourcelocationprefix)
The file path on the original file system where the source code was stored.
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-interpret#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
