  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Create advanced setup](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning "Create advanced setup")/
  * [Code scanning in a container](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/running-codeql-code-scanning-in-a-container "Code scanning in a container")


# Running CodeQL code scanning in a container
You can run code scanning in a container by ensuring that all processes run in the same container.
## Who can use this feature?
Code scanning is available for the following repository types:
  * Public repositories on GitHub.com
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [About code scanning with a containerized build](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/running-codeql-code-scanning-in-a-container#about-code-scanning-with-a-containerized-build)
  * [Dependencies for CodeQL code scanning](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/running-codeql-code-scanning-in-a-container#dependencies-for-codeql-code-scanning)
  * [Example workflow](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/running-codeql-code-scanning-in-a-container#example-workflow)


## [About code scanning with a containerized build](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/running-codeql-code-scanning-in-a-container#about-code-scanning-with-a-containerized-build)
If you're configuring code scanning for a compiled language, and you're building the code in a containerized environment, the analysis may fail with the error message "No source code was seen during the build." This indicates that CodeQL was unable to monitor your code as it was compiled.
You must run CodeQL inside the container in which you build your code. This applies whether you are using the CodeQL CLI or GitHub Actions. For the CodeQL CLI, see [Using code scanning with your existing CI system](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/using-code-scanning-with-your-existing-ci-system) for more information. If you're using GitHub Actions, configure your workflow to run all the actions in the same container. For more information, see [Example workflow](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/running-codeql-code-scanning-in-a-container#example-workflow).
The CodeQL CLI is currently not compatible with non-glibc Linux distributions such as (musl-based) Alpine Linux.
## [Dependencies for CodeQL code scanning](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/running-codeql-code-scanning-in-a-container#dependencies-for-codeql-code-scanning)
You may have difficulty running code scanning if the container you're using is missing certain dependencies (for example, Git must be installed and added to the PATH variable). If you encounter dependency issues, review the list of software typically included on GitHub's runner images. For more information, see the version-specific `readme` files in these locations:
  * Linux: <https://github.com/actions/runner-images/tree/main/images/ubuntu>
  * macOS: <https://github.com/actions/runner-images/tree/main/images/macos>
  * Windows: <https://github.com/actions/runner-images/tree/main/images/windows>


## [Example workflow](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/running-codeql-code-scanning-in-a-container#example-workflow)
This sample workflow uses GitHub Actions to run CodeQL analysis in a containerized environment. The value of `container.image` identifies the container to use. In this example the image is named `codeql-container`, with a tag of `f0f91db`. For more information, see [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idcontainer).
```
name: "CodeQL"

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  schedule:
    - cron: '15 5 * * 3'

jobs:
  analyze:
    name: Analyze
    runs-on: ubuntu-latest
    permissions:
      security-events: write
      actions: read

    strategy:
      fail-fast: false
      matrix:
        language: [java-kotlin]

    # Specify the container in which actions will run
    container:
      image: codeql-container:f0f91db

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
      - name: Initialize CodeQL
        uses: github/codeql-action/init@v3
        with:
          languages: ${{ matrix.language }}
      - name: Build
        run: |
          ./configure
          make
      - name: Perform CodeQL Analysis
        uses: github/codeql-action/analyze@v3

```

