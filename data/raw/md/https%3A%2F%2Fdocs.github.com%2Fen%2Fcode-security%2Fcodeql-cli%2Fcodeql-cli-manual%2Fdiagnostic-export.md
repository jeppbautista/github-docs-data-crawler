  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [diagnostic export](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/diagnostic-export "diagnostic export")


# diagnostic export
[Experimental] Export diagnostic information for a failed analysis.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/diagnostic-export#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/diagnostic-export#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/diagnostic-export#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/diagnostic-export#synopsis)
Shell```
codeql diagnostic export --format=<format> [--output=<output>] <options>...

```
```
codeql diagnostic export --format=<format> [--output=<output>] <options>...

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/diagnostic-export#description)
[Experimental] Export diagnostic information for a failed analysis.
Available since `v2.12.6`.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/diagnostic-export#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/diagnostic-export#primary-options)
#### [`--format=<format>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/diagnostic-export#--formatformat)
[Mandatory] The format in which to write the results. One of:
`raw`: A list of raw, uninterpreted diagnostic messages as JSON objects.
`sarif-latest`: Static Analysis Results Interchange Format (SARIF), a JSON-based format for describing static analysis results. This format option uses the most recent supported version (v2.1.0). This option is not suitable for use in automation as it will produce different versions of SARIF between different CodeQL versions.
`sarifv2.1.0`: SARIF v2.1.0.
`text`: A bullet point list of diagnostic messages.
#### [`-o, --output=<output>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/diagnostic-export#-o---outputoutput)
The output path to write diagnostic information to.
#### [`--sarif-exit-code=<sarifExitCode>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/diagnostic-export#--sarif-exit-codesarifexitcode)
[SARIF formats only] Exit code of the failing process.
#### [`--sarif-exit-code-description=<sarifExitCodeDescription>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/diagnostic-export#--sarif-exit-code-descriptionsarifexitcodedescription)
[SARIF formats only] Reason that the failing process exited.
#### [`--sarif-category=<category>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/diagnostic-export#--sarif-categorycategory)
[SARIF formats only] [Recommended] Specify a category for this analysis to include in the SARIF output. A category can be used to distinguish multiple analyses performed on the same commit and repository, but on different languages or different parts of the code.
If you analyze the same version of a code base in several different ways (e.g., for different languages) and upload the results to GitHub for presentation in Code Scanning, this value should differ between each of the analyses, which tells Code Scanning that the analyses _supplement_ rather than _supersede_ each other. (The values should be consistent between runs of the same analysis for _different_ versions of the code base.)
This value will appear (with a trailing slash appended if not already present) as the `<run>.automationDetails.id` property.
#### [`--diagnostic-dir=<diagnosticDirs>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/diagnostic-export#--diagnostic-dirdiagnosticdirs)
Directory containing CodeQL diagnostic messages. You can pass this multiple times to include multiple directories.
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/diagnostic-export#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/diagnostic-export#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/diagnostic-export#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/diagnostic-export#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/diagnostic-export#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/diagnostic-export#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/diagnostic-export#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/diagnostic-export#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
