  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Supply chain security](https://docs.github.com/en/code-security/supply-chain-security "Supply chain security")/
  * [Understand your supply chain](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain "Understand your supply chain")/
  * [Automatic dependency submission](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-automatic-dependency-submission-for-your-repository "Automatic dependency submission")


# Configuring automatic dependency submission for your repository
You can use automatic dependency submission to submit transitive dependency data in your repository. This enables you to analyze these transitive dependencies using the dependency graph.
## Who can use this feature?
Repository owners, organization owners, security managers, and users with the **admin** role
## In this article
  * [About automatic dependency submission](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-automatic-dependency-submission-for-your-repository#about-automatic-dependency-submission)
  * [Prerequisites](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-automatic-dependency-submission-for-your-repository#prerequisites)
  * [Enabling automatic dependency submission](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-automatic-dependency-submission-for-your-repository#enabling-automatic-dependency-submission)
  * [Using self-hosted runners for automatic dependency submission](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-automatic-dependency-submission-for-your-repository#using-self-hosted-runners-for-automatic-dependency-submission)
  * [Using GitHub-hosted larger runners for automatic dependency submission](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-automatic-dependency-submission-for-your-repository#using-github-hosted-larger-runners-for-automatic-dependency-submission)
  * [Troubleshooting automatic dependency submission](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-automatic-dependency-submission-for-your-repository#troubleshooting-automatic-dependency-submission)
  * [Further reading](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-automatic-dependency-submission-for-your-repository#further-reading)


## [About automatic dependency submission](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-automatic-dependency-submission-for-your-repository#about-automatic-dependency-submission)
Automatic dependency submission does not support all package ecosystems. For the current list of supported ecosystems, see [Dependency graph supported package ecosystems](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/dependency-graph-supported-package-ecosystems).
Dependency graph analyzes the manifest and lock files in a repository, in order to help users understand the upstream packages that their software project depends on. However, in some ecosystems, the resolution of transitive dependencies occurs at build-time and GitHub isn't able to automatically discover all dependencies based on the contents of the repository alone.
When you enable automatic dependency submission for a repository, GitHub automatically identifies the transitive dependencies in the repository and will submit these dependencies to GitHub using the dependency submission API. You can then explore these dependencies using the dependency graph. Dependabot will notify you about security updates for these dependencies by generating Dependabot alerts .
Using automatic dependency submission counts toward your GitHub Actions minutes. For more information, see [About billing for GitHub Actions](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions).
Optionally, you can choose to configure self-hosted runners or GitHub-hosted larger runners for automatic dependency submission. For more information, see [Using self-hosted runners for automatic dependency submission](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-automatic-dependency-submission-for-your-repository#using-self-hosted-runners-for-automatic-dependency-submission) and [Using GitHub-hosted larger runners for automatic dependency submission](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-automatic-dependency-submission-for-your-repository#using-github-hosted-larger-runners-for-automatic-dependency-submission).
## [Prerequisites](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-automatic-dependency-submission-for-your-repository#prerequisites)
Dependency graph must be enabled for the repository for you to enable automatic dependency submission.
You must also enable GitHub Actions for the repository in order to use automatic dependency submission. For more information, see [Managing GitHub Actions settings for a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository).
## [Enabling automatic dependency submission](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-automatic-dependency-submission-for-your-repository#enabling-automatic-dependency-submission)
Repository administrators can enable or disable automatic dependency submission for a repository by following the steps outlined in this procedure.
Organization owners can enable automatic dependency submission for multiple repositories using a security configuration. For more information, see [Creating a custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/creating-a-custom-security-configuration).
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Security" section of the sidebar, click 
  4. Under "Dependency graph", click the dropdown menu next to “Automatic dependency submission”, then select **Enabled**.


Once you've enabled automatic dependency submission for a repository, GitHub will:
  * Monitor for changes to manifest files in the root of the repository on all branches of the repository.
  * Run the dependency graph build action associated with the package ecosystem of each changed manifest.
  * Perform an automatic dependency submission with the results.


You can view details about the automatic workflows run by viewing the **Actions** tab of your repository.
After you enable automatic dependency submission, we'll automatically trigger a run of the action. Once enabled, it'll run each time a commit to the default branch updates a manifest.
## [Using self-hosted runners for automatic dependency submission](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-automatic-dependency-submission-for-your-repository#using-self-hosted-runners-for-automatic-dependency-submission)
You can configure self-hosted runners to run automatic dependency submission jobs, instead of using the GitHub Actions infrastructure.
  1. Provision one or more self-hosted runners, at the repository or organization level. For more information, see [About self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners) and [Adding self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/adding-self-hosted-runners). The self-hosted runners must be running on Linux or macOS, and must have Docker installed.
  2. Assign a `dependency-submission` label to each runner you want automatic dependency submission to use. For more information, see [Using labels with self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/using-labels-with-self-hosted-runners#assigning-a-label-to-a-self-hosted-runner).
  3. In the "Security" section of the sidebar, click 
  4. Under "Dependency graph", click the dropdown menu next to “Automatic dependency submission”, then select **Enabled for labeled runners**.


Once enabled, automatic dependency submission jobs will run on the self-hosted runners, unless:
  * The self-hosted runners are unavailable.
  * There aren't any runner groups tagged with a `dependency-submission` label.


For Maven or Gradle projects that use self-hosted runners with private Maven registries, you need to modify the Maven server settings file to allow the dependency submission workflows to connect to the registries. For more information about the Maven server settings file, see [Security and Deployment Settings](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html#transitive-dependencies) in the Maven documentation.
## [Using GitHub-hosted larger runners for automatic dependency submission](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-automatic-dependency-submission-for-your-repository#using-github-hosted-larger-runners-for-automatic-dependency-submission)
GitHub Team or GitHub Enterprise Cloud users can use larger runners to run automatic dependency submissions jobs.
  1. Provision a larger runner at the organization level with the name `dependency-submission`. For more information, see [Adding a larger runner to an organization](https://docs.github.com/en/actions/using-github-hosted-runners/about-larger-runners/managing-larger-runners#adding-a-larger-runner-to-an-organization).
  2. Give your repository access to the runner. For more information, see [Allowing repositories to access larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-larger-runners/managing-larger-runners#allowing-repositories-to-access-larger-runners).
  3. Under "Dependency graph", click the dropdown menu next to “Automatic dependency submission”, then select **Enabled for labeled runners**.


## [Troubleshooting automatic dependency submission](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-automatic-dependency-submission-for-your-repository#troubleshooting-automatic-dependency-submission)
Automatic dependency submission makes a best effort to cache package downloads between runs using the [Cache](https://github.com/marketplace/actions/cache) action to speed up workflows. For self-hosted runners, you may want to manage this cache within your own infrastructure. To do this, you can disable the built-in caching by setting an environment variable of `GH_DEPENDENCY_SUBMISSION_SKIP_CACHE` to `true`. For more information, see [Store information in variables](https://docs.github.com/en/actions/learn-github-actions/variables).
### [Manifest deduplication](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-automatic-dependency-submission-for-your-repository#manifest-deduplication)
Dependency graph can learn about dependencies in three different ways: static analysis, automatic submission, and manual submission. A repository can have multiple methods configured, which can cause the same package manifest to be scanned multiple times, potentially with different outputs from each scan. Dependency graph uses deduplication logic to parse the outputs, prioritizing the most accurate information for each manifest file.
Dependency graph displays only one instance of each manifest file using the following precedence rules.
  1. **User submissions** take the highest priority, because they are usually created during artifact builds they have the most complete information. 
     * If there are multiple manual snapshots from different detectors, they are sorted alphabetically by correlator and the first one used.
     * If there are two correlators with the same detector, the resolved dependencies are merged. For more information about correlators and detectors, see [REST API endpoints for dependency submission](https://docs.github.com/en/rest/dependency-graph/dependency-submission).
  2. **Automatic submissions** have the second-highest priority since they are also created during artifact builds, but are not submitted by users.
  3. **Static analysis results** are used when no other data is available.


### [Maven projects](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-automatic-dependency-submission-for-your-repository#maven-projects)
For Maven projects, automatic dependency submission runs an open source fork of the [Maven Dependency Tree Dependency Submission](https://github.com/marketplace/actions/maven-dependency-tree-dependency-submission). The fork allows GitHub to stay in sync with the upstream repository plus maintain some changes that are only applicable to automatic submission. The fork's source is available at [advanced-security/maven-dependency-submission-action](https://github.com/advanced-security/maven-dependency-submission-action).
If your repository's dependencies seem inaccurate, check that the timestamp of the last dependency graph build matches the last change to your `pom.xml` file. The timestamp is visible on the table of alerts in the repository's Dependabot alerts tab. Pushing a commit which updates `pom.xml` will trigger a new run of the Dependency Tree Submission action and force a rebuild of that repository's dependency graph.
### [Gradle projects](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-automatic-dependency-submission-for-your-repository#gradle-projects)
For Gradle projects, automatic dependency submission runs a fork of the open source Gradle actions from [gradle/actions](https://github.com/gradle/actions). The fork is available at [actions/gradle-build-tools-actions](https://github.com/actions/gradle-build-tools-actions). You can view the results of the autosubmission action under your repository's **Actions** tab. Each run will be labeled "Automatic Dependency Submission (Gradle)" and its output will contain the JSON payload which the action submitted to the API.
## [Further reading](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-automatic-dependency-submission-for-your-repository#further-reading)
  * [About supply chain security](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-supply-chain-security)
  * [Using the dependency submission API](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/using-the-dependency-submission-api)


