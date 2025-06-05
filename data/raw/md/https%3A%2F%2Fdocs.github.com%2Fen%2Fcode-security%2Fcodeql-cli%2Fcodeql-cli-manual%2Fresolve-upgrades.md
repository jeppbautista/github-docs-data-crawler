  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [resolve upgrades](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-upgrades "resolve upgrades")


# resolve upgrades
[Deep plumbing] Determine upgrades to run for a raw dataset.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-upgrades#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-upgrades#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-upgrades#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-upgrades#synopsis)
Shell```
codeql resolve upgrades --dbscheme=<file> <options>...

```
```
codeql resolve upgrades --dbscheme=<file> <options>...

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-upgrades#description)
[Deep plumbing] Determine upgrades to run for a raw dataset.
Determine which upgrades need to be performed on a particular raw QL dataset to bring it up to the state of the configured QL libraries. This computation is part of what happens during an ordinary database upgrade, and is exposed as a separate plumbing command in order to (a) help with troubleshooting, and (b) provide a starting point for modifying the path in extraordinary cases where exact control is needed.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-upgrades#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-upgrades#primary-options)
#### [`--dbscheme=<file>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-upgrades#--dbschemefile)
[Mandatory] The _current_ dbscheme of the dataset we want to upgrade.
#### [`--format=<fmt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-upgrades#--formatfmt)
Select output format. Choices include:
`lines` _(default)_ : Print upgrade scripts on one line each.
`json`: Print a JSON array of upgrade script paths.
#### [`--just-check`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-upgrades#--just-check)
Don't print any output, but exit with code 0 if there are upgrades to do, and code 1 if there are none.
### [Options from the invoking command's command line](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-upgrades#options-from-the-invoking-commands-command-line)
#### [`--search-path=<dir>[:<dir>...]`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-upgrades#--search-pathdirdir)
A list of directories under which QL packs containing upgrade recipes may be found. Each directory can either be a QL pack (or bundle of packs containing a `.codeqlmanifest.json` file at the root) or the immediate parent of one or more such directories.
If the path contains directories trees, their order defines precedence between them: if a pack name that must be resolved is matched in more than one of the directory trees, the one given first wins.
Pointing this at a checkout of the open-source CodeQL repository ought to work when querying one of the languages that live there.
(Note: On Windows the path separator is `;`).
#### [`--additional-packs=<dir>[:<dir>...]`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-upgrades#--additional-packsdirdir)
[Advanced] If this list of directories is given, they will be searched for upgrades before the ones in `--search-path`. The order between these doesn't matter; it is an error if a pack name is found in two different places through this list.
This is useful if you're temporarily developing a new version of a pack that also appears in the default path. On the other hand it is _not recommended_ to override this option in a config file; some internal actions will add this option on the fly, overriding any configured value.
(Note: On Windows the path separator is `;`).
#### [`--target-dbscheme=<file>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-upgrades#--target-dbschemefile)
The _target_ dbscheme we want to upgrade to. If this is not given, a maximal upgrade path will be constructed
#### [`--target-sha=<sha>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-upgrades#--target-shasha)
[Advanced] An alternative to `--target-dbscheme` that gives the internal hash of the target dbscheme instead of the dbscheme file.
#### [`--[no-]allow-downgrades`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-upgrades#--no-allow-downgrades)
Include any relevant downgrades if there are no upgrades
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-upgrades#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-upgrades#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-upgrades#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-upgrades#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-upgrades#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-upgrades#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-upgrades#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-upgrades#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
