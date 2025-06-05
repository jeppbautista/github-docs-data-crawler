  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Create advanced setup](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning "Create advanced setup")/
  * [CodeQL for compiled languages](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages "CodeQL for compiled languages")


# CodeQL code scanning for compiled languages
Understand how CodeQL analyzes compiled languages, the build options available, and learn how you can customize the database generation process if you need to.
## Who can use this feature?
Users with **write** access if [advanced setup](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning) is already enabled
Code scanning is available for the following repository types:
  * Public repositories on GitHub.com
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [About the CodeQL analysis workflow and compiled languages](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#about-the-codeql-analysis-workflow-and-compiled-languages)
  * [CodeQL build modes](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#codeql-build-modes)
  * [About dependency caching for CodeQL](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#about-dependency-caching-for-codeql)
  * [About build mode None for CodeQL](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#about-build-mode-none-for-codeql)
  * [About Autobuild for CodeQL](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#about-autobuild-for-codeql)
  * [About specifying build steps manually](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#about-specifying-build-steps-manually)
  * [Autobuild steps for compiled languages](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#autobuild-steps-for-compiled-languages)
  * [Building C/C++](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#building-cc)
  * [Building C#](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#building-c)
  * [Building Go](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#building-go)
  * [Building Java and Kotlin](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#building-java-and-kotlin)
  * [Building Swift](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#building-swift)


## [About the CodeQL analysis workflow and compiled languages](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#about-the-codeql-analysis-workflow-and-compiled-languages)
Code scanning works by running queries against one or more CodeQL databases. Each database contains a representation of the code in a single language in your repository. For the compiled languages C/C++, C#, Go, Java, Kotlin, and Swift, the process of populating this database often involves building the code and extracting data.
When you enable code scanning, both default and advanced setup generate a CodeQL database for analysis using the simplest method available. For C# and Java, the CodeQL database is generated directly from the codebase without requiring a build (`none` build mode). For other compiled languages, CodeQL builds the codebase using the `autobuild` build mode. Alternatively, you can use the `manual` build mode to specify explicit build commands to analyze only the files that are built by these custom commands.
You can use dependency caching with CodeQL to store dependencies as a GitHub Actions cache instead of downloading them from registries. For more information, see [About dependency caching for CodeQL](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#about-dependency-caching-for-codeql) later in this article.
## [CodeQL build modes](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#codeql-build-modes)
The CodeQL action supports three different build modes for compiled languages:
  * `none` - the CodeQL database is created directly from the codebase without building the codebase (supported for all interpreted languages, and additionally supported for C# and Java).
  * `autobuild` - CodeQL detects the most likely build method and uses this to attempt to build the codebase and create a database for analysis (supported for all compiled languages).
  * `manual` - you define the build steps to use for the codebase in the workflow (supported for all compiled languages).


### [Comparison of the build modes](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#comparison-of-the-build-modes)
Build mode characteristic | None | Autobuild | Manual  
---|---|---|---  
Used by default setup and for organization-level enablement | Yes (C# and Java) | Yes, where `none` is not supported | No  
Analysis succeeds without user configuration | Yes | Variable | No  
Completeness of analysis | Generated code not analyzed | Variable | User controlled  
Accuracy of analysis | Good | Good | Best  
### [Recommendations](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#recommendations)
When you are setting up code scanning for the first time, or across multiple repositories, it's best to use default setup. Default setup uses the simplest method available to generate a CodeQL database and analyze your code, so that you can start fixing alerts as soon as possible. Once you have resolved the initial alerts, you may want to switch to advanced setup with a manual build process for high risk repositories.
### [Using multiple build modes in a multi-language repository](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#using-multiple-build-modes-in-a-multi-language-repository)
For repositories with multiple compiled languages, you can use different build modes for different languages. For example, if your repository contains C/C++, C# and Java, you might want to provide manual build steps for one language (here C/C++). This workflow specifies a different build mode for each language.
```
strategy:
  matrix:
    include:
      # Analyzes C and C++ code using the commands in `Build C and C++ code`
      - language: c-cpp
        build-mode: manual
      # Analyzes C# code by automatically detecting a build
      - language: csharp
        build-mode: autobuild
      # Analyzes Java code directly from the codebase without a build
      - language: java-kotlin
        build-mode: none # analyzes Java only
steps:
- name: Checkout repository
  uses: actions/checkout@v4

# Initializes CodeQL tools and creates a codebase for analysis.
- name: Initialize CodeQL
  uses: github/codeql-action/init@v3
  with:
    languages: ${{ matrix.language }}
- if: ${{ matrix.build-mode == 'manual' }}
  name: Build C and C++ code
  run: |
    echo 'If you are using a "manual" build mode for one or more of the' \
      'languages you are analyzing, replace this with the commands to build' \
      'your code, for example:'
    echo ' make bootstrap'
    echo ' make release'
    exit 1

```

For information about the languages, libraries, and frameworks that are supported in the latest version of CodeQL, see [Supported languages and frameworks](https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks) in the CodeQL documentation. For information about the system requirements for running the latest version of CodeQL, see [System requirements](https://codeql.github.com/docs/codeql-overview/system-requirements/#additional-software-requirements) in the CodeQL documentation.
## [About dependency caching for CodeQL](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#about-dependency-caching-for-codeql)
You can use dependency caching with CodeQL to store dependencies as a GitHub Actions cache instead of downloading them from registries. This reduces the risk of losing alerts when third party registries don't work well, and may result in a performance improvement for projects that have a large number of dependencies or work with slow registries. To read more about how caching dependencies can speed up workflows, see [Caching dependencies to speed up workflows](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/caching-dependencies-to-speed-up-workflows).
Dependency caching works with all build modes, and is supported by Java, Go, and C#.
Using dependency caching will store CodeQL-specific caches that will be subject to cache quotas for a repository. See [Caching dependencies to speed up workflows](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/caching-dependencies-to-speed-up-workflows#usage-limits-and-eviction-policy).
### [Enabling dependency caching for CodeQL](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#enabling-dependency-caching-for-codeql)
For default setup workflows, dependency caching is enabled only for GitHub-hosted runners in public and private repositories.
For advanced setup workflows, dependency caching is disabled by default. To enable dependency caching for CodeQL, use the `dependency-caching` setting for the CodeQL action in your advanced setup workflow. This setting accepts the following values:
  * `false`/`none`/`off`: Dependency caching is disabled (default)
  * `restore`: Only restore existing caches, do not store new caches
  * `store`: Only store new caches, do not restore existing caches
  * `true`/`full`/`on`: Restore existing caches, and store new caches


For example, the following settings would enable dependency caching for the CodeQL action:
```
    # Initializes CodeQL with dependency caching enabled
    - name: Initialize CodeQL
      uses: github/codeql-action/init@v3
      with:
        languages: java
        dependency-caching: true

```

## [About build mode None for CodeQL](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#about-build-mode-none-for-codeql)
For C# and Java, CodeQL creates a database without requiring a build when you enable default setup for code scanning unless the repository also includes Kotlin code. If a repository contains Kotlin code in addition to Java code, default setup is enabled with the autobuild process because Kotlin analysis requires a build.
Creating a CodeQL database without a build may produce less accurate results than using `autobuild` or manual build steps if:
  * The build scripts cannot be queried for dependency information, and dependency guesses are inaccurate.
  * The repository normally generates code during the build process.


To use `autobuild` or manual build steps, you can use advanced setup.
For Java analysis, if `build-mode` is set to `none` and Kotlin code is found in the repository, the Kotlin code will not be analyzed and a warning will be produced. See [Building Java and Kotlin](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#building-java-and-kotlin).
## [About Autobuild for CodeQL](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#about-autobuild-for-codeql)
The CodeQL action uses `autobuild` to analyze compiled languages in the following cases.
  * Default setup is enabled and the language does not support `none` build (supported for C# and Java).
  * Advanced setup is enabled and the workflow specifies `build-mode: autobuild`.
  * Advanced setup is enabled and the workflow has an Autobuild step for the language using the `autobuild` action (`github/codeql-action/autobuild@v3`).


### [Example using the `build-mode` option](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#example-using-the-build-mode-option)
```
# Initializes the CodeQL tools for scanning.
name: Analyze
strategy:
  matrix:
    include:
      # Analyze C and C++ code
      - language: c-cpp
        build-mode: autobuild
      # Analyze Go code
      - language: go
        build-mode: autobuild

steps:
  - uses: github/codeql-action/init@v3
    with:
      languages: ${{ matrix.language }}
      build-mode: ${{ matrix.build-mode }}

```

### [Example using the Autobuild step](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#example-using-the-autobuild-step)
```
    # Initializes the CodeQL tools for scanning.
    - name: Initialize CodeQL
      uses: github/codeql-action/init@v3
      with:
        languages: ${{ matrix.language }}

    - name: Autobuild
      uses: github/codeql-action/autobuild@v3

```

## [About specifying build steps manually](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#about-specifying-build-steps-manually)
You can only specify manual build steps if you have enabled advanced setup, see [Configuring advanced setup for code scanning](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning#configuring-advanced-setup-for-a-repository).
If `autobuild` fails, or you want to analyze a different set of source files from those built by the `autobuild` process, you'll need to do the following:
  * If your workflow specifies a build mode for the language, change the build mode to `manual`.
  * If your workflow contains an `autobuild` step, remove or comment out the `autobuild` step in the workflow.


Then uncomment the `run` step and manually specify the build process to use. For C/C++, C#, Go, Java, Kotlin, and Swift, CodeQL will analyze whatever source code is built by your specified build steps. For information on how to edit the workflow file, see [Customizing your advanced setup for code scanning](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/customizing-your-advanced-setup-for-code-scanning#editing-a-code-scanning-workflow).
Update your workflow to define the `build-mode` as `manual`.
```
# Initializes the CodeQL tools for scanning.
- name: Initialize CodeQL
- uses: github/codeql-action/init@v3
  with:
    languages: ${{ matrix.language }}
    build-mode: manual
- uses: github/codeql-action/analyze@v3
  with:
    category: "/language:${{ matrix.language }}"

```

Alternatively, update your workflow to comment out the "Autobuild" step.
```
    # Autobuild attempts to build any compiled languages.
    # - name: Autobuild
    #  uses: github/codeql-action/autobuild@v3

```

### [Specifying build commands](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#specifying-build-commands)
When manual building is enabled, uncomment the `run` step in the workflow and add build commands that are suitable for your repository. The `run` step runs command-line programs using the operating system's shell. You can modify these commands and add more commands to customize the build process.
```
- run: |
    make bootstrap
    make release

```

For more information about the `run` keyword, see [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstepsrun).
If you added manual build steps for compiled languages and code scanning is still not working on your repository, contact us through the [GitHub Support portal](https://support.github.com).
## [Autobuild steps for compiled languages](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#autobuild-steps-for-compiled-languages)
GitHub-hosted runners are always run with the software required by `autobuild`. If you use self-hosted runners for GitHub Actions, you may need to install additional software to use the `autobuild` process. Additionally, if your repository requires a specific version of a build tool, you may need to install it manually.
  * [Building C/C++](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#building-cc)
  * [Building C#](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#building-c)
  * [Building Go](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#building-go)
  * [Building Java and Kotlin](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#building-java-and-kotlin)
  * [Building Swift](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#building-swift)


If your workflow uses a `language` matrix, `autobuild` attempts to build each of the compiled languages listed in the matrix. Without a matrix `autobuild` attempts to build the supported compiled language that has the most source files in the repository. With the exception of Go, analysis of other compiled languages in your repository will fail unless you supply explicit build commands.
## [Building C/C++](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#building-cc)
CodeQL supports build modes `autobuild` or `manual` for C/C++ code.
### [Autobuild summary for C/C++](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#autobuild-summary-for-cc)
Supported system type | System name  
---|---  
Operating system | Windows, macOS, and Linux  
Build system | Windows: MSbuild and build scripts  
Linux and macOS: Autoconf, Make, CMake, qmake, Meson, Waf, SCons, Linux Kbuild, and build scripts  
The behavior of the `autobuild` step varies according to the operating system that the extraction runs on.
### [Windows autodetection](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#windows-autodetection)
On Windows, the `autobuild` step attempts to autodetect a suitable build method for C/C++ using the following approach:
  1. Invoke `MSBuild.exe` on the solution (`.sln`) or project (`.vcxproj`) file closest to the root. If `autobuild` detects multiple solution or project files at the same (shortest) depth from the top level directory, it will attempt to build all of them.
  2. Invoke a script that looks like a build script— _build.bat_ , _build.cmd_ , _and build.exe_ (in that order).


### [Linux and macOS autodetection](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#linux-and-macos-autodetection)
On Linux and macOS, the `autobuild` step reviews the files present in the repository to determine the build system used:
  1. Look for a build system in the root directory.
  2. If none are found, search subdirectories for a unique directory with a build system for C/C++.
  3. Run an appropriate command to configure the system.


#### [Runner requirements for C/C++](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#runner-requirements-for-cc)
On Ubuntu Linux runners, `autobuild` may try to automatically install dependencies required by the detected configuration and build steps. By default, this behavior is enabled on GitHub-hosted runners and disabled on self-hosted runners. You can enable or disable this feature explicitly by setting `CODEQL_EXTRACTOR_CPP_AUTOINSTALL_DEPENDENCIES` to `true` or `false` in the environment. For more information about defining environment variables, see [Store information in variables](https://docs.github.com/en/actions/learn-github-actions/variables#defining-environment-variables-for-a-single-workflow).
For self-hosted runners, unless automatic installation of dependencies is enabled, you will likely need to install the `gcc` compiler, and specific projects may also require access to `clang` or `msvc` executables. You will also need to install the build system (for example `msbuild`, `make`, `cmake`, `bazel`) and utilities (such as `python`, `perl`, `lex`, and `yacc`) that your projects depend on. If you enable automatic installation of dependencies, you must ensure that the runner is using Ubuntu and that it can run `sudo apt-get` without requiring a password.
Windows runners require `powershell.exe` to be on the `PATH`.
## [Building C#](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#building-c)
CodeQL supports build modes `none`, `autobuild` or `manual` for C# code.
When you enable default setup for a repository that contains C# code, the build mode is set to `none` automatically.
### [No build for C#](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#no-build-for-c)
CodeQL restores dependencies and generates a few additional source files, to give more accurate results, before creating a database from all the source files and dependencies.
Dependencies are restored using multiple heuristics and strategies. The following files are the primary source of information: `*.csproj`, `*.sln`, `nuget.config`, `packages.config`, `global.json`, and `project.assets.json`. If a private NuGet feed is defined for the organization, this is also used, see [Code scanning default setup access to private registries](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/giving-org-access-private-registries#code-scanning-default-setup-access-to-private-registries) and [Determining whether code scanning default setup used any private registries](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/viewing-code-scanning-logs#determining-whether-code-scanning-default-setup-used-any-private-registries).
The following generated source files are optional, but significantly increase the correctness of the CodeQL database:
  * `global` generated `using` directives to handle the implicit `using` feature of MSbuild.
  * ASP.NET core view files, `.cshtml` files are converted to `.cs` files.


The information from the dependency assembly names, generated source files, dependencies stored in private feeds, and the source files in the repository is compiled and used to create a CodeQL database.
#### [Accuracy of no build analysis for C#](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#accuracy-of-no-build-analysis-for-c)
Creating a CodeQL database without building the full code relies on being able to restore dependencies and being able to compile together the source files in the repository. When there are problems restoring dependencies or compiling the source code, this can affect the accuracy of the CodeQL database and code scanning analysis results.
You can ensure a more accurate analysis by taking the following steps:
  * Provide access to the public internet or ensure that access to a private NuGet feed is available, see [Code scanning default setup access to private registries](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/giving-org-access-private-registries#code-scanning-default-setup-access-to-private-registries).
  * Check whether the repository requires multiple versions of the same NuGet dependency. CodeQL can use only one version and usually chooses the newer version where there are multiple versions. This approach may not work for all repositories.
  * Check whether multiple versions of .NET are referenced, for example, `net48`, `net5.0`, and `netstandard1.6`. CodeQL can use only one version and this may affect accuracy.
  * Avoid colliding class names, otherwise this may cause missing method call targets, which has an impact on dataflow analysis.


### [Autobuild summary for C#](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#autobuild-summary-for-c)
Supported system type | System name  
---|---  
Operating system | Windows, macOS, and Linux  
Build system | .NET and MSbuild, as well as build scripts  
#### [Windows autodetection](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#windows-autodetection-1)
The `autobuild` process attempts to autodetect a suitable build method for C# using the following approach:
  1. Invoke `dotnet build` on the solution (`.sln`) or project (`.csproj`) file closest to the root.
  2. Invoke `MSBuild.exe` on the solution or project file closest to the root. If `autobuild` detects multiple solution or project files at the same (shortest) depth from the top level directory, it will attempt to build all of them.
  3. Invoke a script that looks like a build script—`build.bat`, `build.cmd`, and `build.exe` (in that order).


#### [Runner requirements for C# on Windows](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#runner-requirements-for-c-on-windows)
For .NET Core application development on self-hosted runners, the .NET SDK is required (for `dotnet`).
For .NET Framework application development, you will need Microsoft Build Tools (for `msbuild`) and NuGet CLI (for `nuget`).
Windows runners require `powershell.exe` to be on the `PATH`.
If you plan to create CodeQL databases using `build-mode: none`, you also need to provide access to the public internet, or you must ensure that access to a private NuGet feed is available.
#### [Linux and macOS autodetection](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#linux-and-macos-autodetection-1)
  1. Invoke `dotnet build` on the solution (`.sln`) or project (`.csproj`) file closest to the root.
  2. Invoke `MSbuild` on the solution or project file closest to the root. If `autobuild` detects multiple solution or project files at the same (shortest) depth from the top level directory, it will attempt to build all of them.
  3. Invoke a script that looks like a build script—`build` and `build.sh` (in that order).


#### [Runner requirements for C# on Linux and macOS](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#runner-requirements-for-c-on-linux-and-macos)
For .NET Core application development on self-hosted runners, the .NET SDK is required (for `dotnet`).
For .NET Framework application development, you will require Mono Runtime (to run `mono`, `msbuild`, or `nuget`).
If you plan to create CodeQL databases using `build-mode: none`, you also need to provide access to the public internet, or you must ensure that access to a private NuGet feed is available.
### [C# compiler flags injected by CodeQL for manual builds](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#c-compiler-flags-injected-by-codeql-for-manual-builds)
The CodeQL tracer enables the extraction of all compiled languages by intercepting build processes and forwarding information to the relevant CodeQL language extractors. The tracer injects certain flags into the C# compiler invocation to ensure every component is built and included in the CodeQL database, which may cause your C# code to build in a different way to what you expect during CodeQL analysis.
#### [`/p:MvcBuildViews=true`](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#pmvcbuildviewstrue)
When this option is set to `true`, the views in ASP.NET model-view-controller (MVC) projects are precompiled as part of the build process, which can help to catch errors and improve performance. The tracer injects this flag to make sure CodeQL finds and highlights security issues that may involve dataflow through the code generated from these views. For more information, see [Adding a View to an MVC Application](https://learn.microsoft.com/en-us/aspnet/mvc/overview/getting-started/introduction/adding-a-view) in Microsoft Learn.
#### [`/p:UseSharedCompilation=false`](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#pusesharedcompilationfalse)
Setting this option to `false` disables the use of the shared compilation feature, which may result in slower build times. When `/p:UseSharedCompilation=false` is **not** specified, `msbuild` starts a compiler server process, and all the compilation will be done by that single process. However, the CodeQL tracer depends on inspecting the arguments of newly created processes.
#### [`/p:EmitCompilerGeneratedFiles=true`](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#pemitcompilergeneratedfilestrue)
Setting this option to `true` will emit compiler-generated files during the build process. This option causes the compiler to generate additional source files that are used to support features such as improved regular expression support, serialization, and web application view generation. These generated artifacts are typically not written to disk by the compiler, but setting the option to `true` forces writing the files to disk, and so the extractor can process the files.
For some legacy projects, and projects that use `.sqlproj` files, you may see that the injected `/p:EmitCompilerGeneratedFiles=true` property causes unexpected issues with `msbuild`. For information about troubleshooting this, see [C# compiler unexpectedly failing](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/c-sharp-compiler-unexpectedly-failing).
## [Building Go](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#building-go)
CodeQL supports build modes `autobuild` or `manual` for Go code.
### [Autobuild summary for Go](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#autobuild-summary-for-go)
Supported system type | System name  
---|---  
Operating system | Windows, macOS, and Linux  
Build system | Go modules, `dep` and Glide, as well as build scripts including Makefiles and Ninja scripts  
### [Autodetection for Go](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#autodetection-for-go)
The `autobuild` process attempts to autodetect a suitable way to install the dependencies needed by a Go repository before extracting all `.go` files:
  1. Invoke `make`, `ninja`, `./build` or `./build.sh` (in that order) until one of these commands succeeds and a subsequent `go list ./...` also succeeds, indicating that the needed dependencies have been installed.
  2. If none of those commands succeeded, look for `go.mod`, `Gopkg.toml` or `glide.yaml`, and run `go get` (unless vendoring is in use), `dep ensure -v` or `glide install` respectively to try to install dependencies.
  3. Finally, if configurations files for these dependency managers are not found, rearrange the repository directory structure suitable for addition to `GOPATH`, and use `go get` to install dependencies. The directory structure reverts to normal after extraction completes.
  4. Extract all Go code in the repository, similar to running `go build ./...`.


If you use default setup, it will look for a `go.mod` file to automatically install a compatible version of the Go language.
### [Extractor options for Go](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#extractor-options-for-go)
By default, test code (code in files ending in `_test.go`) is not analyzed. You can override this with the option `--extractor-option extract_tests=true` when using the CodeQL CLI, or by setting the environment variable `CODEQL_EXTRACTOR_GO_OPTION_EXTRACT_TESTS` to `true`.
Additionally, `vendor` directories are excluded from CodeQL Go analysis by default. You can override this by passing the `--extractor-option extract_vendor_dirs=true` option when using the CodeQL CLI, or by setting the environment variable `CODEQL_EXTRACTOR_GO_OPTION_EXTRACT_VENDOR_DIRS` to `true`.
## [Building Java and Kotlin](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#building-java-and-kotlin)
CodeQL supports the following build modes.
  * Java: `none`, `autobuild`, or `manual`
  * Kotlin: `autobuild` or `manual`


When you first enable default setup for a repository, if only Java code is detected then the build mode is set to `none`. If Kotlin or a combination of Java and Kotlin code is detected, then the build mode is set to `autobuild`.
If you later add Kotlin code to a repository that uses the `none` build mode, CodeQL analysis reports a warning message explaining that Kotlin is not supported. You will need to disable default setup and re-enable it. When you re-enable default setup, the build mode will change to `autobuild` so that both languages can be analyzed. Alternatively, you can change to an advanced setup. For more information, see [Warning: Detected X Kotlin files in your project that could not be processed without a build](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/kotlin-detected-in-no-build).
### [No build for Java](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#no-build-for-java)
CodeQL will attempt to run Gradle or Maven to extract accurate dependency information (but not to invoke a build), before creating a database from all Java files present. Every root Maven or Gradle project file (a build script without any build script present in an ancestor directory) is queried for dependency information, and more recent dependency versions are preferred if there is a clash. For information about the runner requirements to run Maven or Gradle, see [Runner requirements for Java](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#runner-requirements-for-java).
If a private Maven registry is defined for the organization, this is also used, see [Code scanning default setup access to private registries](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/giving-org-access-private-registries#code-scanning-default-setup-access-to-private-registries) and [Determining whether code scanning default setup used any private registries](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/viewing-code-scanning-logs#determining-whether-code-scanning-default-setup-used-any-private-registries).
#### [Accuracy of no build analysis for Java](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#accuracy-of-no-build-analysis-for-java)
Creating a CodeQL Java database without a build may produce less accurate results than using `autobuild` or manual build steps if:
  * Gradle or Maven build scripts cannot be queried for dependency information, and dependency guesses (based on Java package names) are inaccurate.
  * The repository normally generates code during the build process. This would be analyzed if you created the CodeQL database using a different mode.


You can ensure a more accurate analysis by taking the following steps:
  * Provide access to the public internet or ensure that access to a private artifact repository is available, see [Code scanning default setup access to private registries](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/giving-org-access-private-registries#code-scanning-default-setup-access-to-private-registries).
  * Check whether the repository requires multiple versions of the same dependency. CodeQL can use only one version and usually chooses the newer version where there are multiple versions. This approach may not work for all repositories.
  * Check whether more than one version of the JDK API is required by different source Java files. When multiple versions are seen, CodeQL will use the highest version required by any build script. This may mean that some files that require a lower version of the JDK will be partially analyzed. For example, if some files require JDK 8 but a JDK 17 requirement is found in one or more build scripts, CodeQL will use JDK 17. Any files that require JDK 8 and could not be built using JDK 17 will be partially analyzed.
  * Avoid colliding class names (for example, multiple files defining `org.myproject.Test`), otherwise this may cause missing method call targets, which has an impact on dataflow analysis.


### [Autobuild summary for Java](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#autobuild-summary-for-java)
Supported system type | System name  
---|---  
Operating system | Windows, macOS, and Linux (no restriction)  
Build system | Gradle, Maven and Ant  
### [Autodetection for Java](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#autodetection-for-java)
The `autobuild` process tries to determine the build system for Java codebases by applying this strategy:
  1. Search for a build file in the root directory. Check for Gradle then Maven then Ant build files.
  2. Run the first build file found. If both Gradle and Maven files are present, the Gradle file is used.
  3. Otherwise, search for build files in direct subdirectories of the root directory. If only one subdirectory contains build files, run the first file identified in that subdirectory (using the same preference as for 1). If more than one subdirectory contains build files, report an error.


### [Runner requirements for Java](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#runner-requirements-for-java)
If you're using self-hosted runners, the required version(s) of Java should be present:
  * If the runner will be used for analyzing repositories that need a single version of Java, then the appropriate JDK version needs to be installed, and needs to be present in the PATH variable (so that `java` and `javac` can be found).
  * If the runner will be used for analyzing repositories that need multiple versions of Java, then the appropriate JDK versions need to be installed, and can be specified via the `toolchains.xml` file. This is a configuration file, typically used by Apache Maven, that allows you to specify the location of the tools, the version of the tools, and any additional configuration that is required to use the tools. For more information, see [Guide to Using Toolchains](https://maven.apache.org/guides/mini/guide-using-toolchains.html) in the Apache Maven documentation.


The following executables will likely be required for a range of Java projects, and should be present in the PATH variable, but they will not be essential in all cases:
  * `mvn` (Apache Maven)
  * `gradle` (Gradle)
  * `ant` (Apache Ant)


You will also need to install the build system (for example `make`, `cmake`, `bazel`) and utilities (such as `python`, `perl`, `lex`, and `yacc`) that your projects depend on.
Windows runners require `powershell.exe` to be on the `PATH`.
## [Building Swift](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#building-swift)
CodeQL supports build modes `autobuild` or `manual` for Swift code.
### [Autobuild summary for Swift](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#autobuild-summary-for-swift)
Supported system type | System name  
---|---  
Operating system | macOS  
Build system | Xcode  
The `autobuild` process tries to build the biggest target from an Xcode project or workspace.
Code scanning of Swift code uses macOS runners by default. Since GitHub-hosted macOS runners are more expensive than Linux and Windows runners, we recommend that you build only the code that you want to analyze. For more information about pricing for GitHub-hosted runners, see [About billing for GitHub Actions](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions).
Code scanning of Swift code is not supported for runners that are part of an Actions Runner Controller (ARC), because ARC runners only use Linux and Swift requires macOS runners. However, you can have a mixture of both ARC runners and self-hosted macOS runners. For more information, see [About Actions Runner Controller](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/about-actions-runner-controller).
### [Customizing Swift compilation in a CodeQL analysis workflow](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#customizing-swift-compilation-in-a-codeql-analysis-workflow)
`xcodebuild` and `swift build` are both supported for Swift builds. We recommend only targeting one architecture during the build. For example, `ARCH=arm64` for `xcodebuild`, or `--arch arm64` for `swift build`.
You can pass the `archive` and `test` options to `xcodebuild`. However, the standard `xcodebuild` command is recommended as it should be the fastest, and should be all that CodeQL requires for a successful scan.
For Swift analysis, you must always explicitly install dependencies managed via CocoaPods or Carthage before generating the CodeQL database.
