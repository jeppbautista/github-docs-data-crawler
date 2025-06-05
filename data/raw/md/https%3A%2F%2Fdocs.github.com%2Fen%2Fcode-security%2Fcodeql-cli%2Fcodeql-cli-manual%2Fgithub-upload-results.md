  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [github upload-results](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-upload-results "github upload-results")


# github upload-results
Uploads a SARIF file to GitHub code scanning.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-upload-results#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-upload-results#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-upload-results#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-upload-results#synopsis)
Shell```
codeql github upload-results --sarif=<file> [--github-auth-stdin] [--github-url=<url>] [--repository=<repository-name>] [--ref=<ref>] [--commit=<commit>] [--checkout-path=<path>] <options>...

```
```
codeql github upload-results --sarif=<file> [--github-auth-stdin] [--github-url=<url>] [--repository=<repository-name>] [--ref=<ref>] [--commit=<commit>] [--checkout-path=<path>] <options>...

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-upload-results#description)
Uploads a SARIF file to GitHub code scanning.
See: [Uploading CodeQL analysis results to GitHub](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/uploading-codeql-analysis-results-to-github)
A GitHub Apps token or personal access token must be set. For best security practices, it is recommended to set the `--github-auth-stdin` flag and pass the token to the command through standard input. Alternatively, the `GITHUB_TOKEN` environment variable can be set.
This token must have the `security_events` scope.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-upload-results#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-upload-results#primary-options)
#### [`-s, --sarif=<file>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-upload-results#-s---sariffile)
[Mandatory] Path to the SARIF files to use. This should be the output of [codeql database analyze](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-analyze) (or [codeql database interpret-results](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-interpret-results)) with `--format sarif-latest` for upload to github.com or the appropriate supported format tag for GitHub Enterprise Server instances (see [SARIF support for code scanning](https://docs.github.com/en/enterprise-server@3.17/code-security/code-scanning/integrating-with-code-scanning/sarif-support-for-code-scanning) for SARIF versions supported by your release).
#### [`-r, --repository=<repository-name>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-upload-results#-r---repositoryrepository-name)
GitHub repository owner and name (e.g., _github/octocat_) to use as an endpoint for uploading. The CLI will attempt to autodetect this from the checkout path if it is omitted.
#### [`-f, --ref=<ref>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-upload-results#-f---refref)
Name of the ref that was analyzed. If this ref is a pull request merge commit, then use _refs/pull/1234/merge_ or _refs/pull/1234/head_ (depending on whether or not this commit corresponds to the HEAD or MERGE commit of the PR). Otherwise, this should be a branch: _refs/heads/branch-name_. If omitted, the CLI will attempt to automatically populate this from the current branch of the checkout path, if this exists.
#### [`-c, --commit=<commit>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-upload-results#-c---commitcommit)
SHA of commit that was analyzed. If this is omitted the CLI will attempt to autodetect this from the checkout path.
#### [`-p, --checkout-path=<path>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-upload-results#-p---checkout-pathpath)
Checkout path. Default is the current working directory.
#### [`--merge`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-upload-results#--merge)
[Advanced] Allow more than one SARIF file to be specified, and merge these into a single file before uploading. This is only recommended for backwards compatibility. For new analyses it is recommended to upload two separate SARIF files with different categories. This option only works in conjunction with SARIF files produced by CodeQL with SARIF version 2.1.0 (this is the default version of SARIF used by CodeQL).
#### [`--no-wait-for-processing`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-upload-results#--no-wait-for-processing)
By default, the CLI will wait for GitHub to process the SARIF file for a maximum of 2 minutes, returning a non-zero exit code if there were any errors during processing of the analysis results. You can customize how long the CLI will wait with `--wait-for-processing-timeout`, or disable the feature with `--no-wait-for-processing`.
#### [`--wait-for-processing-timeout=<waitForProcessingTimeout>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-upload-results#--wait-for-processing-timeoutwaitforprocessingtimeout)
The maximum time the CLI will wait for the uploaded SARIF file to be processed by GitHub, in seconds. The default is 120 seconds (2 minutes). This option is only valid when `--wait-for-processing` is enabled.
#### [`--format=<fmt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-upload-results#--formatfmt)
Select output format. Choices include:
`text` _(default)_ : Print the URL for tracking the status of the SARIF upload.
`json`: Print the response body of the SARIF upload API request.
See also: [REST API endpoints for code scanning](https://docs.github.com/en/rest/code-scanning/code-scanning)
### [Options to configure where to upload SARIF files.](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-upload-results#options-to-configure-where-to-upload-sarif-files)
#### [`-a, --github-auth-stdin`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-upload-results#-a---github-auth-stdin)
Accept a GitHub Apps token or personal access token via standard input.
This overrides the GITHUB_TOKEN environment variable.
#### [`-g, --github-url=<url>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-upload-results#-g---github-urlurl)
URL of the GitHub instance to use. If omitted, the CLI will attempt to autodetect this from the checkout path and if this is not possible default to <https://github.com/>
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-upload-results#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-upload-results#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-upload-results#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-upload-results#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-upload-results#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-upload-results#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-upload-results#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/github-upload-results#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
