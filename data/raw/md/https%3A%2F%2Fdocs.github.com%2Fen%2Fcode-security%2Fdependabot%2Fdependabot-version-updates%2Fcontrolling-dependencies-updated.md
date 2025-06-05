  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Dependabot](https://docs.github.com/en/code-security/dependabot "Dependabot")/
  * [Dependabot version updates](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates "Dependabot version updates")/
  * [Control dependency update](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/controlling-dependencies-updated "Control dependency update")


# Controlling which dependencies are updated by Dependabot
Learn how to configure your `dependabot.yml` file so that Dependabot automatically updates the packages you specify, in the way you define.
## Who can use this feature?
Users with **write** access
## In this article
  * [Defining multiple locations for manifest files](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/controlling-dependencies-updated#defining-multiple-locations-for-manifest-files)
  * [Ignoring specific dependencies](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/controlling-dependencies-updated#ignoring-specific-dependencies)
  * [Allowing specific dependencies to be updated](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/controlling-dependencies-updated#allowing-specific-dependencies-to-be-updated)
  * [Ignoring specific versions or ranges of versions](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/controlling-dependencies-updated#ignoring-specific-versions-or-ranges-of-versions)
  * [Specifying the semantic versioning level to ignore](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/controlling-dependencies-updated#specifying-the-semantic-versioning-level-to-ignore)
  * [Defining a versioning strategy](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/controlling-dependencies-updated#defining-a-versioning-strategy)
  * [Updating vendored dependencies](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/controlling-dependencies-updated#updating-vendored-dependencies)


You can customize your Dependabot configuration to suit your needs, by adding options to your `dependabot.yml` file. For example, you can make sure that Dependabot uses the correct package manifest files, and updates only the dependencies you want maintained.
This article collates customization options you may find useful.
## [Defining multiple locations for manifest files](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/controlling-dependencies-updated#defining-multiple-locations-for-manifest-files)
If you want to enable Dependabot version updates for manifest files stored in more than one location, you can use `directories` in place of `directory`. For example, this configuration sets two different update schedules for manifest files stored in different directories.
YAML```
# Specify the locations of the manifest files to update for each package manager
# using both `directories` and `directory`

version: 2
updates:
  - package-ecosystem: "bundler"
    # Update manifest files stored in these directories weekly
    directories:
      - "/frontend"
      - "/backend"
      - "/admin"
    schedule:
      interval: "weekly"
  - package-ecosystem: "bundler"
    # Update manifest files stored in the root directory daily
    directory: "/"
    schedule:
      interval: "daily"

```
```
# Specify the locations of the manifest files to update for each package manager
# using both `directories` and `directory`

version: 2
updates:
  - package-ecosystem: "bundler"
    # Update manifest files stored in these directories weekly
    directories:
      - "/frontend"
      - "/backend"
      - "/admin"
    schedule:
      interval: "weekly"
  - package-ecosystem: "bundler"
    # Update manifest files stored in the root directory daily
    directory: "/"
    schedule:
      interval: "daily"

```

  * To specify a range of directories using a pattern
YAML```
# Specify the root directory and directories that start with "lib-",
# using globbing, for locations of manifest files

version: 2
updates:
  - package-ecosystem: "composer"
    directories:
      - "/"
      - "/lib-*"
    schedule:
      interval: "weekly"

```
```
# Specify the root directory and directories that start with "lib-",
# using globbing, for locations of manifest files

version: 2
updates:
  - package-ecosystem: "composer"
    directories:
      - "/"
      - "/lib-*"
    schedule:
      interval: "weekly"

```

  * To specify manifests in the current directory and recursive subdirectories
YAML```
# Specify all directories from the current layer and below recursively,
# using globstar, for locations of manifest files

version: 2
updates:
  - package-ecosystem: "composer"
    directories:
      - "**/*"
    schedule:
      interval: "weekly"

```
```
# Specify all directories from the current layer and below recursively,
# using globstar, for locations of manifest files

version: 2
updates:
  - package-ecosystem: "composer"
    directories:
      - "**/*"
    schedule:
      interval: "weekly"

```



## [Ignoring specific dependencies](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/controlling-dependencies-updated#ignoring-specific-dependencies)
If you are not ready to adopt changes from certain dependencies in your project, you can configure Dependabot to ignore those dependencies when it opens pull requests for version updates and security updates. You can do this using one of the following methods.
  * Configure the `ignore` option for the dependency in your `dependabot.yml` file. 
    * **You can use this to ignore updates for specific dependencies, versions, and types of updates.**
    * For more information, see `ignore` in [Dependabot options reference](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference#ignore--).
  * Use `@dependabot ignore` comment commands on a Dependabot pull request for version updates and security updates. 
    * **You can use comment commands to ignore updates for specific dependencies and versions.**
    * For more information, see [Managing pull requests for dependency updates](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/managing-pull-requests-for-dependency-updates#managing-dependabot-pull-requests-with-comment-commands).


Here are some examples showing how `ignore` can be used to customize which dependencies are updated.
  * To ignore updates beyond a specific version
YAML```
ignore:
  - dependency-name: "lodash:*"
    # Ignore versions of Lodash that are equal to or greater than 1.0.0
    versions: [ ">=1.0.0" ]

```
```
ignore:
  - dependency-name: "lodash:*"
    # Ignore versions of Lodash that are equal to or greater than 1.0.0
    versions: [ ">=1.0.0" ]

```

YAML```
ignore:
  - dependency-name: "sphinx"
    versions: [ "[1.1,)" ]

```
```
ignore:
  - dependency-name: "sphinx"
    versions: [ "[1.1,)" ]

```

  * To ignore patch updates
YAML```
ignore:
  - dependency-name: "@types/node"
    # Ignore patch updates for Node
    update-types: ["version-update:semver-patch"]

```
```
ignore:
  - dependency-name: "@types/node"
    # Ignore patch updates for Node
    update-types: ["version-update:semver-patch"]

```

  * To ignore specific versions or version ranges, see [Ignoring specific versions or ranges of versions](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/controlling-dependencies-updated#ignoring-specific-versions-or-ranges-of-versions).


If you want to un-ignore a dependency or ignore condition, you can delete the ignore conditions from the `dependabot.yml` file or reopen the pull request.
For pull requests for grouped updates, you can also use `@dependabot unignore` comment commands. The `@dependabot unignore` comment commands enable you to do the following by commenting on a Dependabot pull request:
  * Un-ignore a specific ignore condition
  * Un-ignore a specific dependency
  * Un-ignore all ignore conditions for all dependencies in a Dependabot pull request


For more information, see [Managing pull requests for dependency updates](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/managing-pull-requests-for-dependency-updates#managing-dependabot-pull-requests-for-grouped-updates-with-comment-commands).
## [Allowing specific dependencies to be updated](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/controlling-dependencies-updated#allowing-specific-dependencies-to-be-updated)
You can use `allow` to tell Dependabot about the dependencies you want to maintain. `allow` is usually used in conjunction with `ignore`.
For more information, see `allow` in [Dependabot options reference](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference#allow--).
By default, Dependabot creates version update pull requests only for the dependencies that are explicitly defined in a manifest (`direct` dependencies). This configuration uses `allow` to tell Dependabot that we want it to maintain `all` types of dependency. That is, both the `direct` dependencies and their dependencies (also known as indirect dependencies, sub-dependencies, or transient dependencies). In addition, the configuration tells Dependabot to ignore all dependencies with a name matching the pattern `org.xwiki.*` because we have a different process for maintaining them.
Dependabot checks for all **allowed** dependencies, then filters out any **ignored** dependencies. If a dependency is matched by an **allow** and an **ignore** statement, then it is ignored.
YAML```
version: 2
registries:
  # Helps find updates for non Maven Central dependencies
  maven-xwiki-public:
    type: maven-repository
    url: https://nexus.xwiki.org/nexus/content/groups/public/
    username: ""
    password: ""
  # Required to resolve xwiki-common SNAPSHOT parent pom
  maven-xwiki-snapshots:
    type: maven-repository
    url: https://maven.xwiki.org/snapshots
    username: ""
    password: ""
updates:
  - package-ecosystem: "maven"
    directory: "/"
    registries:
      - maven-xwiki-public
      - maven-xwiki-snapshots
    schedule:
      interval: "weekly"
    allow:
      # Allow both direct and indirect updates for all packages.
      - dependency-type: "all"
    ignore:
      # Ignore XWiki dependencies. We have a separate process for updating them
      - dependency-name: "org.xwiki.*"
    open-pull-requests-limit: 15

```
```
version: 2
registries:
  # Helps find updates for non Maven Central dependencies
  maven-xwiki-public:
    type: maven-repository
    url: https://nexus.xwiki.org/nexus/content/groups/public/
    username: ""
    password: ""
  # Required to resolve xwiki-common SNAPSHOT parent pom
  maven-xwiki-snapshots:
    type: maven-repository
    url: https://maven.xwiki.org/snapshots
    username: ""
    password: ""
updates:
  - package-ecosystem: "maven"
    directory: "/"
    registries:
      - maven-xwiki-public
      - maven-xwiki-snapshots
    schedule:
      interval: "weekly"
    allow:
      # Allow both direct and indirect updates for all packages.
      - dependency-type: "all"
    ignore:
      # Ignore XWiki dependencies. We have a separate process for updating them
      - dependency-name: "org.xwiki.*"
    open-pull-requests-limit: 15

```

## [Ignoring specific versions or ranges of versions](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/controlling-dependencies-updated#ignoring-specific-versions-or-ranges-of-versions)
You can use `versions` in conjunction with `ignore` to ignore specific versions or ranges of versions.
For more information, see `versions` in [Dependabot options reference](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference#versions-ignore).
  * To ignore a specific version
YAML```
ignore:
  - dependency-name: "django*"
    # Ignore version 11
    versions: [ "11" ]

```
```
ignore:
  - dependency-name: "django*"
    # Ignore version 11
    versions: [ "11" ]

```

  * To ignore a range of versions
YAML```
    ignore:
      - dependency-name: "@types/node"
        versions: ["15.x", "14.x", "13.x"]
      - dependency-name: "xdg-basedir"
        # 5.0.0 has breaking changes as they switch to named exports
        # and convert the module to ESM
        # We can't use it until we switch to ESM across the project
        versions: ["5.x"]
      - dependency-name: "limiter"
        # 2.0.0 has breaking changes
        # so we want to delay updating.
        versions: ["2.x"]

```
```
    ignore:
      - dependency-name: "@types/node"
        versions: ["15.x", "14.x", "13.x"]
      - dependency-name: "xdg-basedir"
        # 5.0.0 has breaking changes as they switch to named exports
        # and convert the module to ESM
        # We can't use it until we switch to ESM across the project
        versions: ["5.x"]
      - dependency-name: "limiter"
        # 2.0.0 has breaking changes
        # so we want to delay updating.
        versions: ["2.x"]

```



## [Specifying the semantic versioning level to ignore](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/controlling-dependencies-updated#specifying-the-semantic-versioning-level-to-ignore)
You can specify one or more semantic versioning (SemVer) levels to ignore using `update-types`.
For more information, see `update-types` in [Dependabot options reference](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference#update-types-ignore).
In this example, Dependabot will ignore patch versions for Node.
YAML```
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "daily"
    ignore:
      - dependency-name: "express"
        # For Express, ignore all updates for version 4 and 5
        versions: ["4.x", "5.x"]
        # For Lodash, ignore all updates
      - dependency-name: "lodash"
      - dependency-name: "@types/node"
        # For Node types, ignore any patch versions
        update-types: ["version-update:semver-patch"]

```
```
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "daily"
    ignore:
      - dependency-name: "express"
        # For Express, ignore all updates for version 4 and 5
        versions: ["4.x", "5.x"]
        # For Lodash, ignore all updates
      - dependency-name: "lodash"
      - dependency-name: "@types/node"
        # For Node types, ignore any patch versions
        update-types: ["version-update:semver-patch"]

```

## [Defining a versioning strategy](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/controlling-dependencies-updated#defining-a-versioning-strategy)
By default, Dependabot tries to increase the minimum version requirement for dependencies it identifies as apps, and widens the allowed version requirements to include both the new and old versions for dependencies it identifies as libraries.
You can change this default strategy. For more information, see `versioning-strategy` in [Dependabot options reference](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference#versioning-strategy--).
In this example, Dependabot will increase the minimum version requirement to match the new version for both apps and libraries.
YAML```
version: 2
updates:
  - package-ecosystem: npm
    directory: "/"
    schedule:
      interval: daily
    # Increase the minimum version for all npm dependencies
    versioning-strategy: increase

```
```
version: 2
updates:
  - package-ecosystem: npm
    directory: "/"
    schedule:
      interval: daily
    # Increase the minimum version for all npm dependencies
    versioning-strategy: increase

```

In this example, Dependabot will **only** increase the minimum version requirement if the original constraint does not allow the new version.
YAML```
version: 2
updates:
- package-ecosystem: pip
  directory: "/"
  schedule:
    interval: daily
  open-pull-requests-limit: 20
  rebase-strategy: "disabled"
  # Increase the version requirements for npm
  # only when required
  versioning-strategy: increase-if-necessary

```
```
version: 2
updates:
- package-ecosystem: pip
  directory: "/"
  schedule:
    interval: daily
  open-pull-requests-limit: 20
  rebase-strategy: "disabled"
  # Increase the version requirements for npm
  # only when required
  versioning-strategy: increase-if-necessary

```

## [Updating vendored dependencies](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/controlling-dependencies-updated#updating-vendored-dependencies)
You can instruct Dependabot to vendor specific dependencies when updating them.
Dependabot automatically maintains vendored dependencies for Go modules, and you can configure Bundler to also update vendored dependencies.
For more information, see `vendor` in [Dependabot options reference](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference#vendor--).
In this example, `vendor` is set to `true` for Bundler, which means that Dependabot will also maintain dependencies for Bundler that are stored in the _vendor/cache_ directory in the repository.
YAML```
version: 2
updates:
- package-ecosystem: bundler
  directory: "/"
  # Vendoring Bundler
  vendor: true
  schedule:
    interval: weekly
    day: saturday
  open-pull-requests-limit: 10

```
```
version: 2
updates:
- package-ecosystem: bundler
  directory: "/"
  # Vendoring Bundler
  vendor: true
  schedule:
    interval: weekly
    day: saturday
  open-pull-requests-limit: 10

```

