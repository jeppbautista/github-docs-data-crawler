  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Migrate to GitHub Actions](https://docs.github.com/en/actions/migrating-to-github-actions "Migrate to GitHub Actions")/
  * [Automated migrations](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations "Automated migrations")/
  * [CircleCI migration](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer "CircleCI migration")


# Migrating from CircleCI with GitHub Actions Importer
Learn how to use GitHub Actions Importer to automate the migration of your CircleCI pipelines to GitHub Actions.
## In this article
  * [About migrating from CircleCI with GitHub Actions Importer](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#about-migrating-from-circleci-with-github-actions-importer)
  * [Installing the GitHub Actions Importer CLI extension](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#installing-the-github-actions-importer-cli-extension)
  * [Configuring credentials](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#configuring-credentials)
  * [Perform an audit of CircleCI](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#perform-an-audit-of-circleci)
  * [Forecast potential GitHub Actions usage](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#forecast-potential-github-actions-usage)
  * [Perform a dry-run migration of a CircleCI pipeline](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#perform-a-dry-run-migration-of-a-circleci-pipeline)
  * [Perform a production migration of a CircleCI pipeline](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#perform-a-production-migration-of-a-circleci-pipeline)
  * [Reference](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#reference)
  * [Legal notice](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#legal-notice)


[Legal notice](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#legal-notice)
## [About migrating from CircleCI with GitHub Actions Importer](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#about-migrating-from-circleci-with-github-actions-importer)
The instructions below will guide you through configuring your environment to use GitHub Actions Importer to migrate CircleCI pipelines to GitHub Actions.
### [Prerequisites](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#prerequisites)
  * A CircleCI account or organization with projects and pipelines that you want to convert to GitHub Actions workflows.
  * Access to create a CircleCI personal API token for your account or organization.
  * An environment where you can run Linux-based containers, and can install the necessary tools. 
    * Docker is [installed](https://docs.docker.com/get-docker/) and running.
    * [GitHub CLI](https://cli.github.com) is installed.
The GitHub Actions Importer container and CLI do not need to be installed on the same server as your CI platform.


### [Limitations](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#limitations)
There are some limitations when migrating from CircleCI to GitHub Actions with GitHub Actions Importer:
  * Automatic caching in between jobs of different workflows is not supported.
  * The `audit` command is only supported when you use a CircleCI organization account. The `dry-run` and `migrate` commands can be used with a CircleCI organization or user account.


#### [Manual tasks](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#manual-tasks)
Certain CircleCI constructs must be migrated manually. These include:
  * Contexts
  * Project-level environment variables
  * Unknown job properties
  * Unknown orbs


## [Installing the GitHub Actions Importer CLI extension](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#installing-the-github-actions-importer-cli-extension)
  1. Install the GitHub Actions Importer CLI extension:
Bash```
gh extension install github/gh-actions-importer

```
```
gh extension install github/gh-actions-importer

```

  2. Verify that the extension is installed:
```
$ gh actions-importer -h
Options:
  -?, -h, --help  Show help and usage information

Commands:
  update     Update to the latest version of GitHub Actions Importer.
  version    Display the version of GitHub Actions Importer.
  configure  Start an interactive prompt to configure credentials used to authenticate with your CI server(s).
  audit      Plan your CI/CD migration by analyzing your current CI/CD footprint.
  forecast   Forecast GitHub Actions usage from historical pipeline utilization.
  dry-run    Convert a pipeline to a GitHub Actions workflow and output its yaml file.
  migrate    Convert a pipeline to a GitHub Actions workflow and open a pull request with the changes.

```



## [Configuring credentials](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#configuring-credentials)
The `configure` CLI command is used to set required credentials and options for GitHub Actions Importer when working with CircleCI and GitHub.
  1. Create a GitHub personal access token (classic). For more information, see [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic).
Your token must have the `workflow` scope.
After creating the token, copy it and save it in a safe location for later use.
  2. Create a CircleCI personal API token. For more information, see [Managing API Tokens](https://circleci.com/docs/managing-api-tokens/#creating-a-personal-api-token) in the CircleCI documentation.
After creating the token, copy it and save it in a safe location for later use.
  3. In your terminal, run the GitHub Actions Importer `configure` CLI command:
```
gh actions-importer configure

```

The `configure` command will prompt you for the following information:
     * For "Which CI providers are you configuring?", use the arrow keys to select `CircleCI`, press `Space` to select it, then press `Enter`.
     * For "Personal access token for GitHub", enter the value of the personal access token (classic) that you created earlier, and press `Enter`.
     * For "Base url of the GitHub instance", press `Enter` to accept the default value (`https://github.com`).
     * For "Personal access token for CircleCI", enter the value for the CircleCI personal API token that you created earlier, and press `Enter`.
     * For "Base url of the CircleCI instance", press `Enter` to accept the default value (`https://circleci.com`).
     * For "CircleCI organization name", enter the name for your CircleCI organization, and press `Enter`.
An example of the `configure` command is shown below:
```
$ gh actions-importer configure
✔ Which CI providers are you configuring?: CircleCI
Enter the following values (leave empty to omit):
✔ Personal access token for GitHub: ***************
✔ Base url of the GitHub instance: https://github.com
✔ Personal access token for CircleCI: ********************
✔ Base url of the CircleCI instance: https://circleci.com
✔ CircleCI organization name: mycircleciorganization
Environment variables successfully updated.

```

  4. In your terminal, run the GitHub Actions Importer `update` CLI command to connect to GitHub Packages Container registry and ensure that the container image is updated to the latest version:
```
gh actions-importer update

```

The output of the command should be similar to below:
```
Updating ghcr.io/actions-importer/cli:latest...
ghcr.io/actions-importer/cli:latest up-to-date

```



## [Perform an audit of CircleCI](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#perform-an-audit-of-circleci)
You can use the `audit` command to get a high-level view of all projects in a CircleCI organization.
The `audit` command performs the following steps:
  1. Fetches all of the projects defined in a CircleCI organization.
  2. Converts each pipeline to its equivalent GitHub Actions workflow.
  3. Generates a report that summarizes how complete and complex of a migration is possible with GitHub Actions Importer.


### [Running the audit command](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#running-the-audit-command)
To perform an audit of a CircleCI organization, run the following command in your terminal:
```
gh actions-importer audit circle-ci --output-dir tmp/audit

```

### [Inspecting the audit results](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#inspecting-the-audit-results)
The files in the specified output directory contain the results of the audit. See the `audit_summary.md` file for a summary of the audit results.
The audit summary has the following sections.
#### [Pipelines](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#pipelines)
The "Pipelines" section contains a high-level statistics regarding the conversion rate done by GitHub Actions Importer.
Listed below are some key terms that can appear in the "Pipelines" section:
  * **Successful** pipelines had 100% of the pipeline constructs and individual items converted automatically to their GitHub Actions equivalent.
  * **Partially successful** pipelines had all of the pipeline constructs converted, however, there were some individual items that were not converted automatically to their GitHub Actions equivalent.
  * **Unsupported** pipelines are definition types that are not supported by GitHub Actions Importer.
  * **Failed** pipelines encountered a fatal error when being converted. This can occur for one of three reasons: 
    * The pipeline was originally misconfigured and not valid.
    * GitHub Actions Importer encountered an internal error when converting it.
    * There was an unsuccessful network response that caused the pipeline to be inaccessible, which is often due to invalid credentials.


#### [Build steps](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#build-steps)
The "Build steps" section contains an overview of individual build steps that are used across all pipelines, and how many were automatically converted by GitHub Actions Importer.
Listed below are some key terms that can appear in the "Build steps" section:
  * A **known** build step is a step that was automatically converted to an equivalent action.
  * An **unknown** build step is a step that was not automatically converted to an equivalent action.
  * An **unsupported** build step is a step that is either: 
    * Fundamentally not supported by GitHub Actions.
    * Configured in a way that is incompatible with GitHub Actions.
  * An **action** is a list of the actions that were used in the converted workflows. This can be important for: 
    * If you use GitHub Enterprise Server, gathering the list of actions to sync to your instance.
    * Defining an organization-level allowlist of actions that are used. This list of actions is a comprehensive list of actions that your security or compliance teams may need to review.


#### [Manual tasks](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#manual-tasks-1)
The "Manual tasks" section contains an overview of tasks that GitHub Actions Importer is not able to complete automatically, and that you must complete manually.
Listed below are some key terms that can appear in the "Manual tasks" section:
  * A **secret** is a repository or organization-level secret that is used in the converted pipelines. These secrets must be created manually in GitHub Actions for these pipelines to function properly. For more information, see [Using secrets in GitHub Actions](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions).
  * A **self-hosted runner** refers to a label of a runner that is referenced in a converted pipeline that is not a GitHub-hosted runner. You will need to manually define these runners for these pipelines to function properly.


#### [Files](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#files)
The final section of the audit report provides a manifest of all the files that were written to disk during the audit.
Each pipeline file has a variety of files included in the audit, including:
  * The original pipeline as it was defined in GitHub.
  * Any network responses used to convert the pipeline.
  * The converted workflow file.
  * Stack traces that can be used to troubleshoot a failed pipeline conversion.


Additionally, the `workflow_usage.csv` file contains a comma-separated list of all actions, secrets, and runners that are used by each successfully converted pipeline. This can be useful for determining which workflows use which actions, secrets, or runners, and can be useful for performing security reviews.
## [Forecast potential GitHub Actions usage](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#forecast-potential-github-actions-usage)
You can use the `forecast` command to forecast potential GitHub Actions usage by computing metrics from completed pipeline runs in CircleCI.
### [Running the forecast command](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#running-the-forecast-command)
To perform a forecast of potential GitHub Actions usage, run the following command in your terminal. By default, GitHub Actions Importer includes the previous seven days in the forecast report.
```
gh actions-importer forecast circle-ci --output-dir tmp/forecast_reports

```

### [Inspecting the forecast report](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#inspecting-the-forecast-report)
The `forecast_report.md` file in the specified output directory contains the results of the forecast.
Listed below are some key terms that can appear in the forecast report:
  * The **job count** is the total number of completed jobs.
  * The **pipeline count** is the number of unique pipelines used.
  * **Execution time** describes the amount of time a runner spent on a job. This metric can be used to help plan for the cost of GitHub-hosted runners.
This metric is correlated to how much you should expect to spend in GitHub Actions. This will vary depending on the hardware used for these minutes. You can use the [GitHub Actions pricing calculator](https://github.com/pricing/calculator) to estimate the costs.
  * **Queue time** metrics describe the amount of time a job spent waiting for a runner to be available to execute it.
  * **Concurrent jobs** metrics describe the amount of jobs running at any given time. This metric can be used to define the number of runners you should configure.


Additionally, these metrics are defined for each queue of runners in CircleCI. This is especially useful if there is a mix of hosted or self-hosted runners, or high or low spec machines, so you can see metrics specific to different types of runners.
## [Perform a dry-run migration of a CircleCI pipeline](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#perform-a-dry-run-migration-of-a-circleci-pipeline)
You can use the `dry-run` command to convert a CircleCI pipeline to an equivalent GitHub Actions workflow. A dry-run creates the output files in a specified directory, but does not open a pull request to migrate the pipeline.
To perform a dry run of migrating your CircleCI project to GitHub Actions, run the following command in your terminal, replacing `my-circle-ci-project` with the name of your CircleCI project.
```
gh actions-importer dry-run circle-ci --output-dir tmp/dry-run --circle-ci-project my-circle-ci-project

```

You can view the logs of the dry run and the converted workflow files in the specified output directory.
If there is anything that GitHub Actions Importer was not able to convert automatically, such as unknown build steps or a partially successful pipeline, you might want to create custom transformers to further customize the conversion process. For more information, see [Extending GitHub Actions Importer with custom transformers](https://docs.github.com/en/actions/migrating-to-github-actions/automated-migrations/extending-github-actions-importer-with-custom-transformers).
## [Perform a production migration of a CircleCI pipeline](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#perform-a-production-migration-of-a-circleci-pipeline)
You can use the `migrate` command to convert a CircleCI pipeline and open a pull request with the equivalent GitHub Actions workflow.
### [Running the migrate command](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#running-the-migrate-command)
To migrate a CircleCI pipeline to GitHub Actions, run the following command in your terminal, replacing the `target-url` value with the URL for your GitHub repository, and `my-circle-ci-project` with the name of your CircleCI project.
```
gh actions-importer migrate circle-ci --target-url https://github.com/octo-org/octo-repo --output-dir tmp/migrate --circle-ci-project my-circle-ci-project

```

The command's output includes the URL to the pull request that adds the converted workflow to your repository. An example of a successful output is similar to the following:
```
$ gh actions-importer migrate circle-ci --target-url https://github.com/octo-org/octo-repo --output-dir tmp/migrate --circle-ci-project my-circle-ci-project
[2022-08-20 22:08:20] Logs: 'tmp/migrate/log/actions-importer-20220916-014033.log'
[2022-08-20 22:08:20] Pull request: 'https://github.com/octo-org/octo-repo/pull/1'

```

### [Inspecting the pull request](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#inspecting-the-pull-request)
The output from a successful run of the `migrate` command contains a link to the new pull request that adds the converted workflow to your repository.
Some important elements of the pull request include:
  * In the pull request description, a section called **Manual steps** , which lists steps that you must manually complete before you can finish migrating your pipelines to GitHub Actions. For example, this section might tell you to create any secrets used in your workflows.
  * The converted workflows file. Select the **Files changed** tab in the pull request to view the workflow file that will be added to your GitHub repository.


When you are finished inspecting the pull request, you can merge it to add the workflow to your GitHub repository.
## [Reference](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#reference)
This section contains reference information on environment variables, optional arguments, and supported syntax when using GitHub Actions Importer to migrate from CircleCI.
### [Using environment variables](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#using-environment-variables)
GitHub Actions Importer uses environment variables for its authentication configuration. These variables are set when following the configuration process using the `configure` command. For more information, see the [Configuring credentials](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#configuring-credentials) section.
GitHub Actions Importer uses the following environment variables to connect to your CircleCI instance:
  * `GITHUB_ACCESS_TOKEN`: The personal access token (classic) used to create pull requests with a converted workflow (requires `repo` and `workflow` scopes).
  * `GITHUB_INSTANCE_URL`: The URL to the target GitHub instance (for example, `https://github.com`).
  * `CIRCLE_CI_ACCESS_TOKEN`: The CircleCI personal API token used to authenticate with your CircleCI instance.
  * `CIRCLE_CI_INSTANCE_URL`: The URL to the CircleCI instance (for example, `https://circleci.com`). If the variable is left unset, `https://circleci.com` is used as the default value.
  * `CIRCLE_CI_ORGANIZATION`: The organization name of your CircleCI instance.
  * `CIRCLE_CI_PROVIDER`: The location where your pipeline's source file is stored (such as `github`). Currently, only GitHub is supported.
  * `CIRCLE_CI_SOURCE_GITHUB_ACCESS_TOKEN` (Optional): The personal access token (classic) used to authenticate with your source GitHub instance (requires `repo` scope). If not provided, the value of `GITHUB_ACCESS_TOKEN` is used instead.
  * `CIRCLE_CI_SOURCE_GITHUB_INSTANCE_URL` (Optional): The URL to the source GitHub instance. If not provided, the value of `GITHUB_INSTANCE_URL` is used instead.


These environment variables can be specified in a `.env.local` file that is loaded by GitHub Actions Importer when it is run.
### [Optional arguments](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#optional-arguments)
There are optional arguments you can use with the GitHub Actions Importer subcommands to customize your migration.
#### [`--source-file-path`](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#--source-file-path)
You can use the `--source-file-path` argument with the `forecast`, `dry-run`, or `migrate` subcommands.
By default, GitHub Actions Importer fetches pipeline contents from source control. The `--source-file-path` argument tells GitHub Actions Importer to use the specified source file path instead.
For example:
```
gh actions-importer dry-run circle-ci --output-dir ./output/ --source-file-path ./path/to/.circleci/config.yml

```

If you would like to supply multiple source files when running the `forecast` subcommand, you can use pattern matching in the file path value. For example, `gh forecast --source-file-path ./tmp/previous_forecast/jobs/*.json` supplies GitHub Actions Importer with any source files that match the `./tmp/previous_forecast/jobs/*.json` file path.
#### [`--config-file-path`](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#--config-file-path)
You can use the `--config-file-path` argument with the `audit`, `dry-run`, and `migrate` subcommands.
By default, GitHub Actions Importer fetches pipeline contents from source control. The `--config-file-path` argument tells GitHub Actions Importer to use the specified source files instead.
The `--config-file-path` argument can also be used to specify which repository a converted composite action should be migrated to.
##### [Audit example](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#audit-example)
In this example, GitHub Actions Importer uses the specified YAML configuration file to perform an audit.
```
gh actions-importer audit circle-ci --output-dir ./output/ --config-file-path ./path/to/circle-ci/config.yml

```

To audit a CircleCI instance using a config file, the config file must be in the following format, and each `repository_slug` must be unique:
```
source_files:
  - repository_slug: circle-org-name/circle-project-name
    path: path/to/.circleci/config.yml
  - repository_slug: circle-org-name/some-other-circle-project-name
    path: path/to/.circleci/config.yml

```

##### [Dry run example](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#dry-run-example)
In this example, GitHub Actions Importer uses the specified YAML configuration file as the source file to perform a dry run.
The pipeline is selected by matching the `repository_slug` in the config file to the value of the `--circle-ci-organization` and `--circle-ci-project` options. The `path` is then used to pull the specified source file.
```
gh actions-importer dry-run circle-ci --circle-ci-project circle-org-name/circle-project-name --output-dir ./output/ --config-file-path ./path/to/circle-ci/config.yml

```

##### [Specify the repository of converted composite actions](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#specify-the-repository-of-converted-composite-actions)
GitHub Actions Importer uses the YAML file provided to the `--config-file-path` argument to determine the repository that converted composite actions are migrated to.
To begin, you should run an audit without the `--config-file-path` argument:
```
gh actions-importer audit circle-ci --output-dir ./output/

```

The output of this command will contain a file named `config.yml` that contains a list of all the composite actions that were converted by GitHub Actions Importer. For example, the `config.yml` file may have the following contents:
```
composite_actions:
  - name: my-composite-action.yml
    target_url: https://github.com/octo-org/octo-repo
    ref: main

```

You can use this file to specify which repository and ref a reusable workflow or composite action should be added to. You can then use the `--config-file-path` argument to provide the `config.yml` file to GitHub Actions Importer. For example, you can use this file when running a `migrate` command to open a pull request for each unique repository defined in the config file:
```
gh actions-importer migrate circle-ci --circle-ci-project my-project-name --output-dir output/ --config-file-path config.yml --target-url https://github.com/my-org/my-repo

```

#### [`--include-from`](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#--include-from)
You can use the `--include-from` argument with the `audit` subcommand.
The `--include-from` argument specifies a file that contains a line-delimited list of repositories to include in the audit of a CircleCI organization. Any repositories that are not included in the file are excluded from the audit.
For example:
```
gh actions-importer audit circle-ci --output-dir ./output/ --include-from repositories.txt

```

The file supplied for this parameter must be a line-delimited list of repositories, for example:
```
repository_one
repository_two
repository_three

```

### [Supported syntax for CircleCI pipelines](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#supported-syntax-for-circleci-pipelines)
The following table shows the type of properties that GitHub Actions Importer is currently able to convert.
CircleCI Pipelines | GitHub Actions | Status  
---|---|---  
cron triggers | 
  * `on.schedule`

| Supported  
environment | 
  * `env`
  * `jobs.<job_id>.env`
  * `jobs.<job_id>.steps.env`

| Supported  
executors | 
  * `runs-on`

| Supported  
jobs | 
  * `jobs`

| Supported  
job | 
  * `jobs.<job_id>`
  * `jobs.<job_id>.name`

| Supported  
matrix | 
  * `jobs.<job_id>.strategy`
  * `jobs.<job_id>.strategy.matrix`

| Supported  
parameters | 
  * `env`
  * `workflow-dispatch.inputs`

| Supported  
steps | 
  * `jobs.<job_id>.steps`

| Supported  
when, unless | 
  * `jobs.<job_id>.if`

| Supported  
triggers | 
  * `on`

| Supported  
executors | 
  * `container`
  * `services`

| Partially Supported  
orbs | 
  * `actions`

| Partially Supported  
executors | 
  * `self hosted runners`

| Unsupported  
setup | Not applicable | Unsupported  
version | Not applicable | Unsupported  
For more information about supported CircleCI concept and orb mappings, see the [`github/gh-actions-importer` repository](https://github.com/github/gh-actions-importer/blob/main/docs/circle_ci/index.md).
### [Environment variable mapping](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#environment-variable-mapping)
GitHub Actions Importer uses the mapping in the table below to convert default CircleCI environment variables to the closest equivalent in GitHub Actions.
CircleCI | GitHub Actions  
---|---  
`CI` | `$CI`  
`CIRCLE_BRANCH` | `${{ github.ref }}`  
`CIRCLE_JOB` | `${{ github.job }}`  
`CIRCLE_PR_NUMBER` | `${{ github.event.number }}`  
`CIRCLE_PR_REPONAME` | `${{ github.repository }}`  
`CIRCLE_PROJECT_REPONAME` | `${{ github.repository }}`  
`CIRCLE_SHA1` | `${{ github.sha }}`  
`CIRCLE_TAG` | `${{ github.ref }}`  
`CIRCLE_USERNAME` | `${{ github.actor }}`  
`CIRCLE_WORKFLOW_ID` | `${{ github.run_number }}`  
`CIRCLE_WORKING_DIRECTORY` | `${{ github.workspace }}`  
`<< pipeline.id >>` | `${{ github.workflow }}`  
`<< pipeline.number >>` | `${{ github.run_number }}`  
`<< pipeline.project.git_url >>` | `$GITHUB_SERVER_URL/$GITHUB_REPOSITORY`  
`<< pipeline.project.type >>` | `github`  
`<< pipeline.git.tag >>` | `${{ github.ref }}`  
`<< pipeline.git.branch >>` | `${{ github.ref }}`  
`<< pipeline.git.revision >>` | `${{ github.event.pull_request.head.sha }}`  
`<< pipeline.git.base_revision >>` | `${{ github.event.pull_request.base.sha }}`  
## [Legal notice](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer#legal-notice)
Portions have been adapted from <https://github.com/github/gh-actions-importer/> under the MIT license:
```
MIT License

Copyright (c) 2022 GitHub

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

