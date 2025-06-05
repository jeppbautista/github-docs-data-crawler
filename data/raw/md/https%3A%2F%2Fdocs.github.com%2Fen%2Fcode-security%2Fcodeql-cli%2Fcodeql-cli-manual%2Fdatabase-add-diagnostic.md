  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [database add-diagnostic](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic "database add-diagnostic")


# database add-diagnostic
[Experimental] Add a piece of diagnostic information to a database.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#synopsis)
Shell```
codeql database add-diagnostic --source-id=<id> --source-name=<name> <options>... -- <database>

```
```
codeql database add-diagnostic --source-id=<id> --source-name=<name> <options>... -- <database>

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#description)
[Experimental] Add a piece of diagnostic information to a database.
Available since `v2.12.6`.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#primary-options)
#### [`<database>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#database)
[Mandatory] Path to the CodeQL database to bundle.
#### [`--markdown-message=<markdownMessage>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#--markdown-messagemarkdownmessage)
Message for the diagnostic, in GitHub-flavored Markdown format.
#### [`--plaintext-message=<plaintextMessage>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#--plaintext-messageplaintextmessage)
Message for the diagnostic, in plain text. This option should only be used when populating a Markdown message with --markdown-message is not practical.
#### [`--severity=<severity>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#--severityseverity)
Severity of the diagnostic. Can be "error", "warning", or "note".
#### [`--help-link=<helpLinks>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#--help-linkhelplinks)
Help links relevant to the diagnostic.
#### [`--attributes-json=<attributesJson>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#--attributes-jsonattributesjson)
Structured metadata relevant to the diagnostic.
### [Options that indicate where the diagnostic message can be displayed](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#options-that-indicate-where-the-diagnostic-message-can-be-displayed)
#### [`--ready-for-status-page`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#--ready-for-status-page)
Indicate that the diagnostic is suitable for display on the status page.
#### [`--ready-for-cli-summary-table`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#--ready-for-cli-summary-table)
Indicate that the diagnostic is suitable for display in the diagnostics summary table printed by commands like `database analyze`.
### [Options describing the source of the diagnostic](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#options-describing-the-source-of-the-diagnostic)
#### [`--source-id=<id>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#--source-idid)
[Mandatory] An identifier for the source of this diagnostic.
#### [`--source-name=<name>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#--source-namename)
[Mandatory] A human-readable description of the source of this diagnostic.
#### [`--extractor-name=<extractorName>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#--extractor-nameextractorname)
The name of the CodeQL extractor, if this diagnostic was produced by a CodeQL extractor.
### [Options describing the diagnostic's location](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#options-describing-the-diagnostics-location)
#### [`--file-path=<file>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#--file-pathfile)
The path of the file to which the diagnostic applies, relative to the source root.
#### [`--start-line=<startLine>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#--start-linestartline)
The 1-based line number (inclusive) where the diagnostic's location starts.
#### [`--start-column=<startColumn>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#--start-columnstartcolumn)
The 1-based column number (inclusive) where the diagnostic's location starts.
#### [`--end-line=<endLine>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#--end-lineendline)
The 1-based line number (inclusive) where the diagnostic's location ends.
#### [`--end-column=<endColumn>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#--end-columnendcolumn)
The 1-based column number (inclusive) where the diagnostic's location ends.
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-add-diagnostic#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
