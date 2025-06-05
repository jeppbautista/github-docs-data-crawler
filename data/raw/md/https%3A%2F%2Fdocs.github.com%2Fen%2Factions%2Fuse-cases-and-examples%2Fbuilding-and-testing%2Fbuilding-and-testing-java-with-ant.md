  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Use cases and examples](https://docs.github.com/en/actions/use-cases-and-examples "Use cases and examples")/
  * [Build and test](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing "Build and test")/
  * [Build & test Java & Ant](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-java-with-ant "Build & test Java & Ant")


# Building and testing Java with Ant
You can create a continuous integration (CI) workflow in GitHub Actions to build and test your Java project with Ant.
## In this article
  * [Introduction](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-java-with-ant#introduction)
  * [Prerequisites](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-java-with-ant#prerequisites)
  * [Using an Ant workflow template](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-java-with-ant#using-an-ant-workflow-template)
  * [Building and testing your code](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-java-with-ant#building-and-testing-your-code)
  * [Packaging workflow data as artifacts](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-java-with-ant#packaging-workflow-data-as-artifacts)


## [Introduction](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-java-with-ant#introduction)
This guide shows you how to create a workflow that performs continuous integration (CI) for your Java project using the Ant build system. The workflow you create will allow you to see when commits to a pull request cause build or test failures against your default branch; this approach can help ensure that your code is always healthy. You can extend your CI workflow to upload artifacts from a workflow run.
GitHub-hosted runners have a tools cache with pre-installed software, which includes Java Development Kits (JDKs) and Ant. For a list of software and the pre-installed versions for JDK and Ant, see [Using GitHub-hosted runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners#supported-software).
## [Prerequisites](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-java-with-ant#prerequisites)
You should be familiar with YAML and the syntax for GitHub Actions. For more information, see:
  * [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
  * [Writing workflows](https://docs.github.com/en/actions/learn-github-actions)


We recommend that you have a basic understanding of Java and the Ant framework. For more information, see the [Apache Ant Manual](https://ant.apache.org/manual/).
## [Using an Ant workflow template](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-java-with-ant#using-an-ant-workflow-template)
To get started quickly, add a workflow template to the `.github/workflows` directory of your repository.
GitHub provides a workflow template for Ant that should work for most Java with Ant projects. The subsequent sections of this guide give examples of how you can customize this workflow template.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the tabs for the "github/docs" repository. The "Actions" tab is highlighted with an orange outline.](https://docs.github.com/assets/cb-12958/images/help/repository/actions-tab-global-nav-update.png)
  3. If you already have a workflow in your repository, click **New workflow**.
  4. The "Choose a workflow" page shows a selection of recommended workflow templates. Search for "Java with Ant".
  5. On the "Java with Ant" workflow, click **Configure**.
  6. Edit the workflow as required. For example, change the Java version.
  7. Click **Commit changes**.
The `ant.yml` workflow file is added to the `.github/workflows` directory of your repository.


### [Specifying the Java version and architecture](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-java-with-ant#specifying-the-java-version-and-architecture)
The workflow template sets up the `PATH` to contain OpenJDK 8 for the x64 platform. If you want to use a different version of Java, or target a different architecture (`x64` or `x86`), you can use the `setup-java` action to choose a different Java runtime environment.
For example, to use version 11 of the JDK provided by Adoptium for the x64 platform, you can use the `setup-java` action and configure the `java-version`, `distribution` and `architecture` parameters to `'11'`, `'temurin'` and `x64`.
YAML```
steps:
  - uses: actions/checkout@v4
  - name: Set up JDK 11 for x64
    uses: actions/setup-java@v4
    with:
      java-version: '11'
      distribution: 'temurin'
      architecture: x64

```
```
steps:
  - uses: actions/checkout@v4
  - name: Set up JDK 11 for x64
    uses: actions/setup-java@v4
    with:
      java-version: '11'
      distribution: 'temurin'
      architecture: x64

```

For more information, see the [`setup-java`](https://github.com/actions/setup-java) action.
## [Building and testing your code](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-java-with-ant#building-and-testing-your-code)
You can use the same commands that you use locally to build and test your code.
The workflow template will run the default target specified in your `build.xml` file. Your default target will commonly be set to build classes, run tests and package classes into their distributable format, for example, a JAR file.
If you use different commands to build your project, or you want to run a different target, you can specify those. For example, you may want to run the `jar` target that's configured in your `build-ci.xml` file.
YAML```
steps:
  - uses: actions/checkout@v4
  - uses: actions/setup-java@v4
    with:
      java-version: '17'
      distribution: 'temurin'
  - name: Run the Ant jar target
    run: ant -noinput -buildfile build-ci.xml jar

```
```
steps:
  - uses: actions/checkout@v4
  - uses: actions/setup-java@v4
    with:
      java-version: '17'
      distribution: 'temurin'
  - name: Run the Ant jar target
    run: ant -noinput -buildfile build-ci.xml jar

```

## [Packaging workflow data as artifacts](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-java-with-ant#packaging-workflow-data-as-artifacts)
After your build has succeeded and your tests have passed, you may want to upload the resulting Java packages as a build artifact. This will store the built packages as part of the workflow run, and allow you to download them. Artifacts can help you test and debug pull requests in your local environment before they're merged. For more information, see [Storing and sharing data from a workflow](https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts).
Ant will usually create output files like JARs, EARs, or WARs in the `build/jar` directory. You can upload the contents of that directory using the `upload-artifact` action.
YAML```
steps:
  - uses: actions/checkout@v4
  - uses: actions/setup-java@v4
    with:
      java-version: '17'
      distribution: 'temurin'

  - run: ant -noinput -buildfile build.xml
  - uses: actions/upload-artifact@v4
    with:
      name: Package
      path: build/jar

```
```
steps:
  - uses: actions/checkout@v4
  - uses: actions/setup-java@v4
    with:
      java-version: '17'
      distribution: 'temurin'

  - run: ant -noinput -buildfile build.xml
  - uses: actions/upload-artifact@v4
    with:
      name: Package
      path: build/jar

```

