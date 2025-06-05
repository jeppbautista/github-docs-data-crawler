  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Dependabot](https://docs.github.com/en/code-security/dependabot "Dependabot")/
  * [Dependabot version updates](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates "Dependabot version updates")/
  * [Optimize PR creation](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/optimizing-pr-creation-version-updates "Optimize PR creation")


# Optimizing the creation of pull requests for Dependabot version updates
Learn how to streamline and efficiently manage your Dependabot pull requests.
## Who can use this feature?
Users with **write** access
## In this article
  * [Controlling the frequency and timings of dependency updates](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/optimizing-pr-creation-version-updates#controlling-the-frequency-and-timings-of-dependency-updates)
  * [Prioritizing meaningful updates](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/optimizing-pr-creation-version-updates#prioritizing-meaningful-updates)


By default, Dependabot opens a new pull request to update each dependency. When you enable security updates, new pull requests are opened when a vulnerable dependency is found. When you configure version updates for one or more ecosystems, new pull requests are opened when new versions of dependencies are available, with the frequency defined in the `dependabot.yml` file.
If your project has many dependencies, you might find that you have a very large number of Dependabot pull requests to review and merge, which can quickly become difficult to manage.
There are a couple of customization options you can implement to optimize Dependabot update pull requests to align with your processes, such as:
  * **Controlling the frequency** with which Dependabot checks for newer versions of your dependencies with `schedule`.
  * **Prioritize meaningful updates** with `groups`.


## [Controlling the frequency and timings of dependency updates](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/optimizing-pr-creation-version-updates#controlling-the-frequency-and-timings-of-dependency-updates)
Dependabot runs its checks for version updates at a frequency set by you in the configuration file, where the required field, `schedule.interval`, must be set to `daily`, `weekly`, `monthly`, `quarterly`, `semiannually`, `yearly`, or `cron` (see [cronjob](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference#cronjob)).
By default, Dependabot balances its workload by assigning a random time to check and raise pull requests for dependency updates.
However, to reduce distraction, or to better organize time and resources for reviewing and addressing version updates, you might find it useful to modify the frequency and timings. For example, you may prefer Dependabot to run weekly rather than daily checks for updates, and at a time that ensures pull requests are raised before for your team's triage session.
You can use `schedule` with a combination of options to modify the frequency and timings of when Dependabot checks for version updates
The example `dependabot.yml` file below changes the npm configuration to specify that Dependabot should check for version updates to npm dependencies every Tuesday at 02:00 Japanese Standard Time (UTC +09:00).
YAML```
# `dependabot.yml` file with
# customized schedule for version updates

version: 2
updates:
  # Keep npm dependencies up to date
  - package-ecosystem: "npm"
    directory: "/"
    # Check the npm registry every week on Tuesday at 02:00 Japan Standard Time (UTC +09:00)
    schedule:
      interval: "weekly"
      day: "tuesday"
      time: "02:00"
      timezone: "Asia/Tokyo"

```
```
# `dependabot.yml` file with
# customized schedule for version updates

version: 2
updates:
  # Keep npm dependencies up to date
  - package-ecosystem: "npm"
    directory: "/"
    # Check the npm registry every week on Tuesday at 02:00 Japan Standard Time (UTC +09:00)
    schedule:
      interval: "weekly"
      day: "tuesday"
      time: "02:00"
      timezone: "Asia/Tokyo"

```

See also [schedule](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference#schedule-).
## [Prioritizing meaningful updates](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/optimizing-pr-creation-version-updates#prioritizing-meaningful-updates)
You can use `groups` to consolidate updates for multiple dependencies into a single pull request. This helps you focus your review time on higher risk updates, and minimize the time spent reviewing minor version updates. For example, you can combine updates for minor or patch updates for development dependencies into a single pull request, and have a dedicated group for security or version updates that impact a key area of your codebase.
You must configure groups per individual package ecosystem, then you can create multiple groups per package ecosystem using a combination of criteria:
  * Dependabot update type: `applies-to`
  * Type of dependency: `dependency-type`.
  * Dependency name: `patterns` and `exclude-patterns`
  * Semantic versioning levels: `update-types`


To see all supported values for each criterion, see [`groups`](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference#groups--).
The below examples present several different methods to create groups of dependencies using the criteria.
### [Example 1: Three version update groups](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/optimizing-pr-creation-version-updates#example-1-three-version-update-groups)
In this example, the `dependabot.yml` file:
  * Creates three groups, called "`production-dependencies`", "`development-dependencies`", and "`rubocop`".
  * Uses `patterns` and `dependency-type` to include dependencies in the group.
  * Uses `exclude-patterns` to exclude a dependency (or multiple dependencies) from the group.

```
version: 2
updates:
  # Keep bundler dependencies up to date
  - package-ecosystem: "bundler"
    directory: "/"
    schedule:
      interval: "weekly"
    groups:
      production-dependencies:
        dependency-type: "production"
      development-dependencies:
        dependency-type: "development"
        exclude-patterns:
          - "rubocop*"
      rubocop:
        patterns:
          - "rubocop*"

```

As a result:
  * Version updates are grouped by dependency type.
  * Development dependencies matching the pattern `rubocop*` are excluded from the `development-dependencies` group.
  * Instead, development dependencies matching `rubocop*` will be included in the `rubocop` group. Due to the ordering, production dependencies matching `rubocop*` will be included in the `production-dependencies` group.
  * In addition, all groups default to applying to version updates only, since the `applies-to` key is absent.


### [Example 2: Grouped updates with excluded dependencies](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/optimizing-pr-creation-version-updates#example-2-grouped-updates-with-excluded-dependencies)
In this example, the `dependabot.yml` file:
  * Creates a group called "`support-dependencies`", as part of a customized Bundler configuration.
  * Uses `patterns` that match with the name of a dependency (or multiple dependencies) to include dependencies in the group.
  * Uses `exclude-patterns` that match with the name of a dependency (or multiple dependencies) to exclude dependencies from the group.
  * Applies the grouping to version updates only, since `applies-to: version-updates` is used.

```
version: 2
updates:
  # Keep bundler dependencies up to date
  - package-ecosystem: "bundler"
    directories:
      - "/frontend"
      - "/backend"
      - "/admin"
    schedule:
      interval: "weekly"
    # Create a group of dependencies to be updated together in one pull request
    groups:
      # Specify a name for the group, which will be used in pull request titles
      # and branch names
      support-dependencies:
        # Define patterns to include dependencies in the group (based on
        # dependency name)
        applies-to: version-updates # Applies the group rule to version updates
        patterns:
          - "rubocop" # A single dependency name
          - "rspec*"  # A wildcard string that matches multiple dependency names
          - "*"       # A wildcard that matches all dependencies in the package
                      # ecosystem. Note: using "*" may open a large pull request
        # Define patterns to exclude dependencies from the group (based on
        # dependency name)
        exclude-patterns:
          - "gc_ruboconfig"
          - "gocardless-*"

```

As a result:
  * The majority of dependencies for bundler are consolidated into the `support-dependencies` group due to the wildcard ("*") pattern, apart from
  * Dependencies that match `gc_ruboconfig` and `gocardless-*` are excluded from the group, and Dependabot continues to raise single pull requests for these dependencies. This can be helpful if updates for these dependencies need to be reviewed with closer scrutiny.
  * For `support-dependencies`, Dependabot will only raise pull requests for version updates.


### [Example 3: Individual pull requests for major updates and grouped for minor/patch updates](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/optimizing-pr-creation-version-updates#example-3-individual-pull-requests-for-major-updates-and-grouped-for-minorpatch-updates)
In this example, the `dependabot.yml` file:
  * Creates a group called "`angular`".
  * Uses `patterns` that match with the name of a dependency to include dependencies in the group.
  * Uses `update-type` to only include `minor` or `patch` updates in the group.
  * Applies the grouping to version updates only, since `applies-to: version-updates` is used.

```
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    groups:
      # Specify a name for the group, which will be used in pull request titles
      # and branch names
      angular:
        applies-to: version-updates
        patterns:
          - "@angular*"
        update-types:
          - "minor"
          - "patch"

```

As a result:
  * Dependabot will create a grouped pull request for all Angular dependencies that have a minor or patch update.
  * All major updates will continue to be raised as individual pull requests.


### [Example 4: Grouped pull requests for minor/patch updates and no pull requests for major updates](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/optimizing-pr-creation-version-updates#example-4-grouped-pull-requests-for-minorpatch-updates-and-no-pull-requests-for-major-updates)
In this example, the `dependabot.yml` file:
  * Creates two groups called "`angular`" and "`minor-and-patch`".
  * Uses `applies-to` so that the first group applies to version updates only, and the second group applies to security updates only.
  * Uses `update-type` to only include `minor` or `patch` updates for both groups.
  * Uses an `ignore` condition to exclude updates to `major` versions of `@angular*` packages.

```
version: 2
updates:
  # Keep npm dependencies up to date
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    groups:
      angular:
        applies-to: version-updates
        patterns:
          - "@angular*"
        update-types:
          - "minor"
          - "patch"
      minor-and-patch:
        applies-to: security-updates
        patterns:
          - "@angular*"
        update-types:
          - "patch"
          - "minor"
    ignore:
      - dependency-name: "@angular*"
        update-types: ["version-update:semver-major"]

```

As a result:
  * Minor and patch version updates for Angular dependencies are grouped into a single pull request.
  * Minor and patch security updates for Angular dependencies are also grouped together into a single pull request.
  * Dependabot won't automatically open pull requests for major updates for Angular.


