  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Use cases and examples](https://docs.github.com/en/actions/use-cases-and-examples "Use cases and examples")/
  * [Build and test](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing "Build and test")/
  * [Build & test .NET](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-net "Build & test .NET")


# Building and testing .NET
You can create a continuous integration (CI) workflow to build and test your .NET project.
## In this article
  * [Introduction](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-net#introduction)
  * [Prerequisites](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-net#prerequisites)
  * [Using a .NET workflow template](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-net#using-a-net-workflow-template)
  * [Specifying a .NET version](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-net#specifying-a-net-version)
  * [Installing dependencies](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-net#installing-dependencies)
  * [Building and testing your code](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-net#building-and-testing-your-code)
  * [Packaging workflow data as artifacts](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-net#packaging-workflow-data-as-artifacts)
  * [Publishing to package registries](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-net#publishing-to-package-registries)


## [Introduction](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-net#introduction)
This guide shows you how to build, test, and publish a .NET package.
GitHub-hosted runners have a tools cache with preinstalled software, which includes the .NET Core SDK. For a full list of up-to-date software and the preinstalled versions of .NET Core SDK, see [software installed on GitHub-hosted runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners).
## [Prerequisites](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-net#prerequisites)
You should already be familiar with YAML syntax and how it's used with GitHub Actions. For more information, see [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions).
We recommend that you have a basic understanding of the .NET Core SDK. For more information, see [Getting started with .NET](https://dotnet.microsoft.com/learn).
## [Using a .NET workflow template](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-net#using-a-net-workflow-template)
To get started quickly, add a workflow template to the `.github/workflows` directory of your repository.
GitHub provides a workflow template for .NET that should work for most .NET projects. The subsequent sections of this guide give examples of how you can customize this workflow template.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the tabs for the "github/docs" repository. The "Actions" tab is highlighted with an orange outline.](https://docs.github.com/assets/cb-12958/images/help/repository/actions-tab-global-nav-update.png)
  3. If you already have a workflow in your repository, click **New workflow**.
  4. The "Choose a workflow" page shows a selection of recommended workflow templates. Search for "dotnet".
  5. On the ".NET" workflow, click **Configure**.
  6. Edit the workflow as required. For example, change the .NET version.
  7. Click **Commit changes**.
The `dotnet.yml` workflow file is added to the `.github/workflows` directory of your repository.


## [Specifying a .NET version](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-net#specifying-a-net-version)
To use a preinstalled version of the .NET Core SDK on a GitHub-hosted runner, use the `setup-dotnet` action. This action finds a specific version of .NET from the tools cache on each runner, and adds the necessary binaries to `PATH`. These changes will persist for the remainder of the job.
The `setup-dotnet` action is the recommended way of using .NET with GitHub Actions, because it ensures consistent behavior across different runners and different versions of .NET. If you are using a self-hosted runner, you must install .NET and add it to `PATH`. For more information, see the [`setup-dotnet`](https://github.com/marketplace/actions/setup-net-core-sdk) action.
### [Using multiple .NET versions](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-net#using-multiple-net-versions)
```
name: dotnet package

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest
    strategy:
      matrix:
        dotnet-version: [ '3.1.x', '6.0.x' ]

    steps:
      - uses: actions/checkout@v4
      - name: Setup dotnet ${{ matrix.dotnet-version }}
        uses: actions/setup-dotnet@v4
        with:
          dotnet-version: ${{ matrix.dotnet-version }}
      # You can test your matrix by printing the current dotnet version
      - name: Display dotnet version
        run: dotnet --version

```

### [Using a specific .NET version](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-net#using-a-specific-net-version)
You can configure your job to use a specific version of .NET, such as `6.0.22`. Alternatively, you can use semantic version syntax to get the latest minor release. This example uses the latest minor release of .NET 6.
```
    - name: Setup .NET 6.x
      uses: actions/setup-dotnet@v4
      with:
        # Semantic version range syntax or exact version of a dotnet version
        dotnet-version: '6.x'

```

## [Installing dependencies](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-net#installing-dependencies)
GitHub-hosted runners have the NuGet package manager installed. You can use the dotnet CLI to install dependencies from the NuGet package registry before building and testing your code. For example, the YAML below installs the `Newtonsoft` package.
```
steps:
- uses: actions/checkout@v4
- name: Setup dotnet
  uses: actions/setup-dotnet@v4
  with:
    dotnet-version: '6.0.x'
- name: Install dependencies
  run: dotnet add package Newtonsoft.Json --version 12.0.1

```

### [Caching dependencies](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-net#caching-dependencies)
You can cache NuGet dependencies for future workflows using the optional `cache` input. For example, the YAML below caches the NuGet `global-packages` folder, and then installs the `Newtonsoft` package. A second optional input, `cache-dependency-path`, can be used to specify the path to a dependency file: `packages.lock.json`.
For more information, see [Caching dependencies to speed up workflows](https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows).
```
steps:
- uses: actions/checkout@v4
- name: Setup dotnet
  uses: actions/setup-dotnet@v4
  with:
    dotnet-version: '6.x'
    cache: true
- name: Install dependencies
  run: dotnet add package Newtonsoft.Json --version 12.0.1

```

Depending on the number of dependencies, it may be faster to use the dependency cache. Projects with many large dependencies should see a performance increase as it cuts down the time required for downloading. Projects with fewer dependencies may not see a significant performance increase and may even see a slight decrease due to how NuGet installs cached dependencies. The performance varies from project to project.
## [Building and testing your code](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-net#building-and-testing-your-code)
You can use the same commands that you use locally to build and test your code. This example demonstrates how to use `dotnet build` and `dotnet test` in a job:
```
steps:
- uses: actions/checkout@v4
- name: Setup dotnet
  uses: actions/setup-dotnet@v4
  with:
    dotnet-version: '6.0.x'
- name: Install dependencies
  run: dotnet restore
- name: Build
  run: dotnet build --no-restore
- name: Test with the dotnet CLI
  run: dotnet test --no-build

```

## [Packaging workflow data as artifacts](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-net#packaging-workflow-data-as-artifacts)
After a workflow completes, you can upload the resulting artifacts for analysis. For example, you may need to save log files, core dumps, test results, or screenshots. The following example demonstrates how you can use the `upload-artifact` action to upload test results.
For more information, see [Storing and sharing data from a workflow](https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts).
```
name: dotnet package

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest
    strategy:
      matrix:
        dotnet-version: [ '3.1.x', '6.0.x' ]

      steps:
        - uses: actions/checkout@v4
        - name: Setup dotnet
          uses: actions/setup-dotnet@v4
          with:
            dotnet-version: ${{ matrix.dotnet-version }}
        - name: Install dependencies
          run: dotnet restore
        - name: Test with dotnet
          run: dotnet test --no-restore --logger trx --results-directory "TestResults-${{ matrix.dotnet-version }}"
        - name: Upload dotnet test results
          uses: actions/upload-artifact@v4
          with:
            name: dotnet-results-${{ matrix.dotnet-version }}
            path: TestResults-${{ matrix.dotnet-version }}
          # Use always() to always run this step to publish test results when there are test failures
          if: ${{ always() }}

```

## [Publishing to package registries](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-net#publishing-to-package-registries)
You can configure your workflow to publish your .NET package to a package registry when your CI tests pass. You can use repository secrets to store any tokens or credentials needed to publish your binary. The following example creates and publishes a package to GitHub Packages using `dotnet core cli`.
```
name: Upload dotnet package

on:
  release:
    types: [created]

jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      packages: write
      contents: read
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-dotnet@v4
        with:
          dotnet-version: '6.0.x' # SDK Version to use.
          source-url: https://nuget.pkg.github.com/<owner>/index.json
        env:
          NUGET_AUTH_TOKEN: ${{secrets.GITHUB_TOKEN}}
      - run: dotnet build --configuration Release <my project>
      - name: Create the package
        run: dotnet pack --configuration Release <my project>
      - name: Publish the package to GPR
        run: dotnet nuget push <my project>/bin/Release/*.nupkg

```

