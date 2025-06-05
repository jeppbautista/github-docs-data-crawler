  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [CodeQL CLI manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual "CodeQL CLI manual")/
  * [database trace-command](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command "database trace-command")


# database trace-command
[Plumbing] Run a single command as part of a traced build.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command#synopsis)
  * [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command#description)
  * [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command#options)


This content describes the most recent release of the CodeQL CLI. For more information about this release, see <https://github.com/github/codeql-cli-binaries/releases>.
To see details of the options available for this command in an earlier release, run the command with the `--help` option in your terminal.
## [Synopsis](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command#synopsis)
Shell```
codeql database trace-command [--threads=<num>] [--ram=<MB>] [--extractor-option=<extractor-option-name=value>] <options>... -- <database> <command>...

```
```
codeql database trace-command [--threads=<num>] [--ram=<MB>] [--extractor-option=<extractor-option-name=value>] <options>... -- <database> <command>...

```

## [Description](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command#description)
[Plumbing] Run a single command as part of a traced build.
This runs a single given command line under a tracer, thus possibly performing some extraction, but does not finalize the resulting CodeQL database.
## [Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command#options)
### [Primary Options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command#primary-options)
#### [`<database>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command#database)
[Mandatory] Path to the CodeQL database under construction. This must have been prepared for extraction with [codeql database init](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-init).
If the `--db-cluster` option is given, this is not a database itself, but a directory that _contains_ databases, and all of those databases will be processed together.
#### [`<command>...`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command#command)
The command to run. This may consist of one or more arguments, which are used to create the process. It is recommended to pass the '--' argument before listing the command's arguments, in order to avoid confusion between its arguments and ours.
The command is expected to exit with a status code of 0. Any other exit code is interpreted as a failure.
The command may be omitted when `--index-traceless-dbs` is given.
#### [`-j, --threads=<num>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command#-j---threadsnum)
Ask the extractor to use this many threads. This option is passed to the extractor as a suggestion. If the CODEQL_THREADS environment variable is set, the environment variable value takes precedence over this option.
You can pass 0 to use one thread per core on the machine, or -_N_ to leave _N_ cores unused (except still use at least one thread).
#### [`-M, --ram=<MB>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command#-m---rammb)
Ask the extractor to use this much memory. This option is passed to the extractor as a suggestion. If the CODEQL_RAM environment variable is set, the environment variable value takes precedence over this option.
#### [`--[no-]db-cluster`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command#--no-db-cluster)
Indicates that the directory given on the command line is not a database itself, but a directory that _contains_ one or more databases under construction. Those databases will be processed together.
#### [`--no-tracing`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command#--no-tracing)
[Advanced] Do not trace the specified command, instead rely on it to produce all necessary data directly.
#### [`--extra-tracing-config=<tracing-config.lua>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command#--extra-tracing-configtracing-configlua)
[Advanced] The path to a tracer configuration file. It may be used to modify the behavior of the build tracer. It may be used to pick out compiler processes that run as part of the build command, and trigger the execution of other tools. The extractors will provide default tracer configuration files that should work in most situations.
#### [`--[no-]index-traceless-dbs`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command#--no-index-traceless-dbs)
In addition to the specified command, run the main script for extractors that don't depend on tracing a build process. If you're constructing databases for several languages with `--db-cluster`, this option should be given to exactly one invocation of [codeql database trace-command](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command).
#### [`--[no-]use-build-mode`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command#--no-use-build-mode)
Determine what to run based on the database's build mode. This option cannot be used in conjunction with `--index-traceless-dbs`.
#### [`--working-dir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command#--working-dirdir)
[Advanced] The directory in which the specified command should be executed. If this argument is not provided, the command is executed in the value of `--source-root` passed to [codeql database create](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-create), if one exists. If no `--source-root` argument is provided, the command is executed in the current working directory.
#### [`--no-run-unnecessary-builds`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command#--no-run-unnecessary-builds)
[Advanced] Only run the specified build command(s) if a database under construction uses an extractor that depends on tracing a build process. If this option is not given, the command will be executed even when CodeQL doesn't need it, on the assumption that you need its side effects for other reasons.
### [Options to control extractor behavior](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command#options-to-control-extractor-behavior)
#### [`-O, --extractor-option=<extractor-option-name=value>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command#-o---extractor-optionextractor-option-namevalue)
Set options for CodeQL extractors. `extractor-option-name` should be of the form extractor_name.group1.group2.option_name or group1.group2.option_name. If `extractor_option_name` starts with an extractor name, the indicated extractor must declare the option group1.group2.option_name. Otherwise, any extractor that declares the option group1.group2.option_name will have the option set. `value` can be any string that does not contain a newline.
You can use this command-line option repeatedly to set multiple extractor options. If you provide multiple values for the same extractor option, the behavior depends on the type that the extractor option expects. String options will use the last value provided. Array options will use all the values provided, in order. Extractor options specified using this command-line option are processed after extractor options given via `--extractor-options-file`.
When passed to [codeql database init](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-init) or `codeql database begin-tracing`, the options will only be applied to the indirect tracing environment. If your workflow also makes calls to [codeql database trace-command](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command) then the options also need to be passed there if desired.
See <https://codeql.github.com/docs/codeql-cli/extractor-options> for more information on CodeQL extractor options, including how to list the options declared by each extractor.
#### [`--extractor-options-file=<extractor-options-bundle-file>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command#--extractor-options-fileextractor-options-bundle-file)
Specify extractor option bundle files. An extractor option bundle file is a JSON file (extension `.json`) or YAML file (extension `.yaml` or `.yml`) that sets extractor options. The file must have the top-level map key 'extractor' and, under it, extractor names as second-level map keys. Further levels of maps represent nested extractor groups, and string and array options are map entries with string and array values.
Extractor option bundle files are read in the order they are specified. If different extractor option bundle files specify the same extractor option, the behavior depends on the type that the extractor option expects. String options will use the last value provided. Array options will use all the values provided, in order. Extractor options specified using this command-line option are processed before extractor options given via `--extractor-option`.
When passed to [codeql database init](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-init) or `codeql database begin-tracing`, the options will only be applied to the indirect tracing environment. If your workflow also makes calls to [codeql database trace-command](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command) then the options also need to be passed there if desired.
See <https://codeql.github.com/docs/codeql-cli/extractor-options> for more information on CodeQL extractor options, including how to list the options declared by each extractor.
### [Common options](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command#common-options)
#### [`-h, --help`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command#-h---help)
Show this help text.
#### [`-J=<opt>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command#-jopt)
[Advanced] Give option to the JVM running the command.
(Beware that options containing spaces will not be handled correctly.)
#### [`-v, --verbose`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command#-v---verbose)
Incrementally increase the number of progress messages printed.
#### [`-q, --quiet`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command#-q---quiet)
Incrementally decrease the number of progress messages printed.
#### [`--verbosity=<level>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command#--verbositylevel)
[Advanced] Explicitly set the verbosity level to one of errors, warnings, progress, progress+, progress++, progress+++. Overrides `-v` and `-q`.
#### [`--logdir=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command#--logdirdir)
[Advanced] Write detailed logs to one or more files in the given directory, with generated names that include timestamps and the name of the running subcommand.
(To write a log file with a name you have full control over, instead give `--log-to-stderr` and redirect stderr as desired.)
#### [`--common-caches=<dir>`](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-trace-command#--common-cachesdir)
[Advanced] Controls the location of cached data on disk that will persist between several runs of the CLI, such as downloaded QL packs and compiled query plans. If not set explicitly, this defaults to a directory named `.codeql` in the user's home directory; it will be created if it doesn't already exist.
Available since `v2.15.2`.
