  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [Getting started](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli "Getting started")/
  * [Setting up the CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/setting-up-the-codeql-cli "Setting up the CodeQL CLI")


# Setting up the CodeQL CLI
To get started with the CodeQL CLI, you need to download and set up the CLI so that it can access the tools and libraries required to create and analyze databases.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [Setting up the CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/setting-up-the-codeql-cli#setting-up-the-codeql-cli)
  * [Testing the CodeQL CLI configuration](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/setting-up-the-codeql-cli#testing-the-codeql-cli-configuration)
  * [Next steps](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/setting-up-the-codeql-cli#next-steps)


## [Setting up the CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/setting-up-the-codeql-cli#setting-up-the-codeql-cli)
To run CodeQL commands, you need to set up the CLI so that it can access the tools, queries, and libraries required to create and analyze databases.
The CodeQL CLI can be set up to support many different use cases and directory structures. To get started quickly, we recommend adopting a relatively simple setup, as outlined in the steps below.
If you plan to use the CodeQL CLI for security research or to test or contribute queries, you may want a more advanced setup of CodeQL CLI. For more information, see [Advanced setup of the CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/advanced-setup-of-the-codeql-cli).
If you are setting up the CodeQL CLI in your CI system, you need to make the full contents of the CodeQL CLI bundle available to every CI server that you want to run CodeQL code scanning analysis on. For example, you might configure each server to copy the bundle from a central, internal location and extract it. Alternatively, you could use the REST API to get the bundle directly from GitHub, ensuring that you benefit from the latest improvements to queries. For more information, see [REST API endpoints for releases and release assets](https://docs.github.com/en/rest/releases) in the REST API documentation.
If you are using macOS on Apple Silicon (for example, Apple M1), ensure that the [Xcode command-line developer tools](https://developer.apple.com/downloads/index.action) and [Rosetta 2](https://support.apple.com/en-us/HT211861) are installed.
The CodeQL CLI is currently not compatible with non-glibc Linux distributions such as (muslc-based) Alpine Linux.
### [1. Download the CodeQL CLI tar archive](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/setting-up-the-codeql-cli#1-download-the-codeql-cli-tar-archive)
The CodeQL CLI download package is a tar archive containing tools, scripts, and various CodeQL-specific files. If you don’t have a GitHub Enterprise license then, by downloading this archive, you are agreeing to the [GitHub CodeQL Terms and Conditions](https://securitylab.github.com/tools/codeql/license).
You should download the CodeQL bundle from <https://github.com/github/codeql-action/releases>. The bundle contains:
  * CodeQL CLI product
  * A compatible version of the queries and libraries from <https://github.com/github/codeql>
  * Precompiled versions of all the queries included in the bundle


You should always use the CodeQL bundle. This ensures compatibility and gives much better performance than a separate download of the CodeQL CLI and checkout of the CodeQL queries. If you will only be running the CLI on one specific platform, download the appropriate `codeql-bundle-PLATFORM.tar.zst` file. Alternatively, you can download `codeql-bundle.tar.zst`, which contains the CLI for all supported platforms.
There are also `tar.gz` variants of the bundle, which are identical to the `tar.zst` variants except compressed using the less efficient gzip algorithm. The only reason to download the `tar.gz` variants is if you are using older decompression tools that do not support the Zstandard compression algorithm.
### [2. Extract the CodeQL CLI tar archive](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/setting-up-the-codeql-cli#2-extract-the-codeql-cli-tar-archive)
Extract the CodeQL CLI tar archive to a directory of your choosing.
### [3. Launch `codeql`](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/setting-up-the-codeql-cli#3-launch-codeql)
Once extracted, you can run CodeQL processes by running the `codeql` executable in a couple of ways:
  * By executing `<extraction-root>/codeql/codeql`, where `<extraction-root>` is the folder where you extracted the CodeQL CLI package.
  * By adding `<extraction-root>/codeql` to your `PATH`, so that you can run the executable as just `codeql`.


At this point, you can execute CodeQL commands. For a full list of the CodeQL CLI commands, see [CodeQL CLI commands manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual).
If you add `codeql` to your `PATH`, it can be accessed by CodeQL for Visual Studio Code to compile and run queries. For more information about configuring VS Code to access the CodeQL CLI, see [Configuring access to the CodeQL CLI](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/configuring-access-to-the-codeql-cli).
## [Testing the CodeQL CLI configuration](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/setting-up-the-codeql-cli#testing-the-codeql-cli-configuration)
After you extract the CodeQL CLI bundle, you can run the following command to verify that the CLI is correctly configured to create and analyze databases:
  * `codeql resolve packs` if `/<extraction root>/codeql` is on the `PATH`.
  * `/<extraction root>/codeql/codeql resolve packs` otherwise.


If successful, you should see output similar to the extract below:
```
Searching directories specified by `--additional-packs`. All directories have equal priority.
  Searching in:
    No packs were found at this location.
Searching directories specified by `--search-path`. Directories are searched in order.
Searching the root of the CodeQL distribution.
  Searching in:
      <extraction root>
    The following packs were found:
      codeql/java-all@<version>: (library) <extraction root>/qlpacks/codeql/javat-all/<version>/qlpack.yml
      codeql/java-queries@<version>: (query) <extraction root>/qlpacks/codeql/java-queries/<version>/qlpack.yml
      codeql/javascript-all@<version>: (library) <extraction root>/qlpacks/codeql/javascript-all/<version>/qlpack.yml
      codeql/javascript-queries@<version>: (query) <extraction root>/qlpacks/codeql/javascript-queries/<version>/qlpack.yml
      codeql/swift-all@<version>: (library) <extraction root>/qlpacks/codeql/swift-all/<version>/qlpack.yml
      codeql/swift-queries@<version>: (query) <extraction root>/qlpacks/codeql/swift-queries/<version>/qlpack.yml
...

```

The results have been truncated for brevity. The actual results will be longer and more detailed.
You should check that the output contains the expected languages and also that the directory location for the qlpack files is correct. The location should be within the extracted CodeQL CLI bundle, shown in the earlier example as `<extraction root>`. If the CodeQL CLI is unable to locate the qlpacks for the expected languages, check that you downloaded the CodeQL bundle and not a standalone copy of the CodeQL CLI.
You can also run `codeql resolve languages` to show which languages are available for database creation. This will list the languages supported by default in your CodeQL CLI package.
Optionally, you can download some CodeQL packs containing pre-compiled queries you would like to run. For more information, see [Customizing analysis with CodeQL packs](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/customizing-analysis-with-codeql-packs).
The `codeql resolve packs` command is useful for diagnosing problems when the CodeQL CLI is unable to locate query packs that you expect to be available for analysis.
The `codeql resolve packs` command is available in the CodeQL CLI versions 2.19.0 and later. For earlier versions of the CLI, you should run the `codeql resolve qlpacks` command, which produces similar, but less detailed output.
## [Next steps](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/setting-up-the-codeql-cli#next-steps)
To learn how to prepare your code to be analyzed by the CodeQL CLI, see [Preparing your code for CodeQL analysis](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/preparing-your-code-for-codeql-analysis).
