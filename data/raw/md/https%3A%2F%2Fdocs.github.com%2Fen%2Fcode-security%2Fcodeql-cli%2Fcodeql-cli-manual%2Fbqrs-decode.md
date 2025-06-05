  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [bqrs decode](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-decode "bqrs decode")


# bqrs decode
Convert result data from BQRS into other forms.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-decode#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-decode#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-decode#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-decode#synopsis)
Shell```
codeql bqrs decode [--output=<file>] [--result-set=<name>] [--sort-key=<col>[,<col>...]] <options>... -- <file>

```
```
codeql bqrs decode [--output=<file>] [--result-set=<name>] [--sort-key=<col>[,<col>...]] <options>... -- <file>

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-decode#description)
Convert result data from BQRS into other forms.
The decoded output will be written to standard output, unless the `--output` option is specified.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-decode#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-decode#primary-options)
#### [`<file>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-decode#file)
[Mandatory] BQRS file to decode.
#### [`-o, --output=<file>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-decode#-o---outputfile)
The file to write the desired output to.
#### [`-r, --result-set=<name>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-decode#-r---result-setname)
Select a particular result set from the BQRS file to decode. The available results sets can be listed by [codeql bqrs info](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-info).
If no result set is selected, all result sets will be decoded, provided the selected output format and processing options support that. Otherwise an error results.
#### [`-k, --sort-key=<col>[,<col>...]`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-decode#-k---sort-keycolcol)
Sort the selected result set by the indicated columns.
#### [`--sort-direction=<direction>[,<direction>...]`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-decode#--sort-directiondirectiondirection)
Sort the selected result set using the indicated sort directions.
If sort directions are not specified, then ascending order will be used for all columns.
### [Output format options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-decode#output-format-options)
#### [`--format=<fmt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-decode#--formatfmt)
Select output format. Choices include:
`text` _(default)_ : A human-readable plain text table.
`csv`: Comma-separated values.
`json`: Streaming JSON.
`bqrs`: BQRS. This must be used with `--output`. Most useful together with `--sort-key`.
#### [`--no-titles`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-decode#--no-titles)
Omit column titles for `text` and `csv` formats
#### [`--entities=<fmt>[,<fmt>...]`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-decode#--entitiesfmtfmt)
[Advanced] Control how result columns of entity type are shown. A comma-separated list of the following choices:
`url`: A URL referring to a source location, if the query was compiled to produce such URLs for entity types.
`string`: A string computed by the toString() method in QL, if the query was compiled to produce such strings for the column.
`id`: The internal ID of the entity, which may not be informative.
`all`: Show columns with all the information the BQRS file provides.
All the selected options are shown, if possible.
### [Options for pagination (for use by interactive front-ends)](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-decode#options-for-pagination-for-use-by-interactive-front-ends)
#### [`--rows=<num>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-decode#--rowsnum)
[Advanced] Output this many rows from the selected resultset, starting at the top, or at the location given by `--start-at`.
#### [`--start-at=<offset>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-decode#--start-atoffset)
[Advanced] Start printing the row defined at a particular byte offset in the BQRS file. The offset must be gotten from [codeql bqrs info](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-info), or from the "next" pointer found in JSON output from a previous invocation with `--rows` set. Other offsets are likely to produce nonsense output and/or explicit errors.
Must always be used together with `--rows`, and is incompatible with `--sort-key`.
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-decode#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-decode#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-decode#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-decode#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-decode#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-decode#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-decode#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/bqrs-decode#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
