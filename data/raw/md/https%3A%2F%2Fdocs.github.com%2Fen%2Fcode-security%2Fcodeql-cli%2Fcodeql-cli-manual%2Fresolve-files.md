  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [resolve files](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-files "resolve files")


# resolve files
[Deep plumbing] Expand a set of file inclusion/exclusion globs.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-files#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-files#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-files#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-files#synopsis)
Shell```
codeql resolve files <options>... -- <dir>

```
```
codeql resolve files <options>... -- <dir>

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-files#description)
[Deep plumbing] Expand a set of file inclusion/exclusion globs.
This plumbing command is responsible for expanding the command-line parameters of subcommands that operate on multiple files, identified by their paths. By default, all files are included, and so running this command without any filter arguments will collect all files in a directory.
The `--include`, `--exclude`, and `--prune` options all take glob patterns, which can use the following wildcard characters:
  * A single "?" matches any character other than a forward/backward slash;
  * A single "*" matches any number of characters other than a forward/backward slash;
  * The pattern "**" matches zero or more complete directory components.


## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-files#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-files#primary-options)
#### [`<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-files#dir)
The directory to be searched.
#### [`--format=<fmt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-files#--formatfmt)
Select output format, either `text` _(default)_ or `json`.
### [Options for limiting the set of collected files](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-files#options-for-limiting-the-set-of-collected-files)
#### [`--include-extension=<.ext>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-files#--include-extensionext)
Include all files in the search directory tree that have the given extension. Typically, you should include the dot before the extension. For example, passing `--include-extension .xml` will include all files with the ".xml" extension. This option is incompatible with negated `--include` options.
#### [`--include=<glob>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-files#--includeglob)
Include all files and directories in the search directory tree that match the given glob, using each file and directory's relative path from the search directory. If the glob begins with a `!` character, the matching files and directories would instead be excluded.
`--include` options are processed in order, with later options overriding earlier ones. For example, `--include ** --include !sub/*.ts --include sub/main.*` would include `sub/main.ts` (because it is included by `sub/main.*`), exclude `sub/index.ts` (because it is excluded by `!sub/*.ts`), and include `sub/test.js` (because it is included by `**` without being subsequently excluded.)
#### [`--also-match=<glob>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-files#--also-matchglob)
Require all results to also match the given glob, using each file and directory's relative path from the search directory. This option has the same structure and the same interpretation as `--include` but specifies a separate sequence of globs that are applied in conjunction with `--include`.
#### [`--exclude=<glob>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-files#--excludeglob)
Exclude all files and directories that match the given glob, using each file and directory's relative path from the search directory. This option overrides all include options. This option is incompatible with negated `--include` options.
#### [`--prune=<glob>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-files#--pruneglob)
Exclude all files and directories that match the given glob, using each file and directory's relative path from the search directory. This option overrides all include options. This option is incompatible with negated `--include` options.
#### [`--size-limit=<bytes>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-files#--size-limitbytes)
Exclude all files whose size exceeds the given limit. The size limit is in bytes, or in kibibytes (KiB) with the "k" suffix, in mebibytes (MiB) with the "m" suffix, and in gibibytes (GiB) with the "g" suffix. This option overrides all include options.
#### [`--total-size-limit=<bytes>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-files#--total-size-limitbytes)
Make the command exit with an error if the combined size of all resolved files would exceed the given limit. The size limit is in bytes, or in kibibytes (KiB) with the "k" suffix, in mebibytes (MiB) with the "m" suffix, and in gibibytes (GiB) with the "g" suffix.
#### [`--[no-]follow-symlinks`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-files#--no-follow-symlinks)
Follow any symbolic links to their targets.
#### [`--[no-]find-any`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-files#--no-find-any)
Find at most one match (as opposed to all matches).
Available since `v2.11.3`.
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-files#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-files#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-files#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-files#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-files#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-files#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-files#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-files#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
