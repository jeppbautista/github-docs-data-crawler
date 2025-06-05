  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Dependabot](https://docs.github.com/en/code-security/dependabot "Dependabot")/
  * [Maintain dependencies at scale](https://docs.github.com/en/code-security/dependabot/maintain-dependencies "Maintain dependencies at scale")/
  * [Remove access to public registries](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/removing-dependabot-access-to-public-registries "Remove access to public registries")


# Removing Dependabot access to public registries
Examples of how you can configure Dependabot to only access private registries by removing calls to public registries.
## Who can use this feature?
Users with **write** access
## In this article
  * [About configuring Dependabot to only access private registries](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/removing-dependabot-access-to-public-registries#about-configuring-dependabot-to-only-access-private-registries)
  * [Bundler](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/removing-dependabot-access-to-public-registries#bundler)
  * [Docker](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/removing-dependabot-access-to-public-registries#docker)
  * [Gradle](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/removing-dependabot-access-to-public-registries#gradle)
  * [Maven](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/removing-dependabot-access-to-public-registries#maven)
  * [Node](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/removing-dependabot-access-to-public-registries#node)
  * [NuGet](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/removing-dependabot-access-to-public-registries#nuget)
  * [Python](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/removing-dependabot-access-to-public-registries#python)


## [About configuring Dependabot to only access private registries](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/removing-dependabot-access-to-public-registries#about-configuring-dependabot-to-only-access-private-registries)
Dependabot can access public registries by default, and you can configure Dependabot to also access private registries. For more information about private registry support and configuration, see [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot). For in-depth information about available options, as well as recommendations and advice when configuring private registries, see [Guidance for the configuration of private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/guidance-for-the-configuration-of-private-registries-for-dependabot).
To have greater control over Dependabot's access to your private registries and internal network resources, you can configure Dependabot to run on GitHub Actions self-hosted runners. For more information, see [About Dependabot on GitHub Actions runners](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/about-dependabot-on-github-actions-runners) and [Managing Dependabot on self-hosted runners](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/managing-dependabot-on-self-hosted-runners).
You can configure Dependabot to access _only_ private registries by removing calls to public registries. This can only be configured for the ecosystems listed in this article.
## [Bundler](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/removing-dependabot-access-to-public-registries#bundler)
To configure the Bundler ecosystem to only access private registries, you can set `replaces-base: true` in the `dependabot.yml` file. For more information, see [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#rubygems-server).
The Bundler ecosystem additionally requires a `Gemfile` file with the private registry URL to be checked into the repository.
YAML```
# Example Gemfile

 source "https://private_registry_url"

```
```
# Example Gemfile

 source "https://private_registry_url"

```

## [Docker](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/removing-dependabot-access-to-public-registries#docker)
To configure the Docker ecosystem to only access private registries, you can use these configuration methods.
**Option 1**
Define the private registry configuration in a `dependabot.yml` file without `replaces-base`. For more information, see [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#docker-registry).
Remove `replaces-base: true` from the configuration file.
YAML```
version: 2
registries:
  azuretestregistry: # Define access for a private registry
    type: docker-registry
    url: firewallregistrydep.azurecr.io
    username: firewallregistrydep
    password: ${{ secrets.AZUREHUB_PASSWORD }}

```
```
version: 2
registries:
  azuretestregistry: # Define access for a private registry
    type: docker-registry
    url: firewallregistrydep.azurecr.io
    username: firewallregistrydep
    password: ${{ secrets.AZUREHUB_PASSWORD }}

```

In the `Dockerfile` file, add the image name in the format of `IMAGE[:TAG]`, where `IMAGE` consists of your username and the name of the repository.
YAML```
 FROM firewallregistrydep.azurecr.io/myreg/ubuntu:22.04

```
```
 FROM firewallregistrydep.azurecr.io/myreg/ubuntu:22.04

```

**Option 2**
Set `replaces-base: true` in the `dependabot.yml` file. For more information, see [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#docker-registry). The registry configured with the `replaces-base` can be used as a mirror or a pull through cache. For further details, see [Registry as a pull through cache](https://docs.docker.com/registry/recipes/mirror/) in the Docker documentation.
## [Gradle](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/removing-dependabot-access-to-public-registries#gradle)
To configure the Gradle ecosystem to only access private registries, you can use these configuration methods.
Define the private registry configuration in a `dependabot.yml` file. For more information, see [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#maven-repository).
Remove `replaces-base: true` from the configuration file.
Additionally, you also need to specify the private registry URL in the `repositories` section of the `build.gradle` file.
```
# Example build.gradle file

repositories {
    maven {
        url "https://private_registry_url"
    }
}

```

## [Maven](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/removing-dependabot-access-to-public-registries#maven)
To configure the Maven ecosystem to only access private registries, you can use these configuration methods.
**Option 1**
Set `replaces-base: true` in the `dependabot.yml` file. For more information, see [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#maven-repository).
**Option 2**
Use only the private registry URL in the `pom.xml` file.
```
<project>
...
 <repositories>
  <repository>
    <id>central</id>
    <name>your custom repo</name>
    <url>https://private_registry_url</url>
 </repository>
...
</project>

```

## [Node](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/removing-dependabot-access-to-public-registries#node)
### [npm](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/removing-dependabot-access-to-public-registries#npm)
To configure the npm ecosystem to only access private registries, you can use these configuration methods.
**Option 1**
Define the private registry configuration in a `dependabot.yml` file. For more information, see [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#npm-registry).
Remove `replaces-base: true` from the configuration file.
The npm ecosystem additionally requires a `.npmrc` file with the private registry URL to be checked into the repository.
YAML```
 registry=https://private_registry_url

```
```
 registry=https://private_registry_url

```

**Option 2**
If there is no global registry defined in an `.npmrc` file, you can set `replaces-base: true` in the `dependabot.yml` file. For more information, see [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#npm-registry).
For scoped dependencies (`@my-org/my-dep`), Dependabot requires that the private registry is defined in the project's `.npmrc` file. To define private registries for individual scopes, use `@myscope:registry=https://private_registry_url`.
### [Yarn](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/removing-dependabot-access-to-public-registries#yarn)
Yarn Classic and Yarn Berry private registries are both supported by Dependabot, but Dependabot requires a different configuration for each ecosystem to access only private registries.
#### [Yarn Classic](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/removing-dependabot-access-to-public-registries#yarn-classic)
To configure the Yarn Classic ecosystem to only access private registries, you can use these configuration methods.
**Option 1**
Define the private registry configuration in a `dependabot.yml` file. For more information, see [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#npm-registry).
Delete `replaces-base: true` from the configuration file.
To ensure the private registry is listed as the dependency source in the project's `yarn.lock` file, run `yarn install` on a machine with private registry access. Yarn should update the `resolved` field to include the private registry URL.
YAML```
encoding@^0.1.11:
  version "0.1.13"
  resolved "https://private_registry_url/encoding/-/encoding-0.1.13.tgz#56574afdd791f54a8e9b2785c0582a2d26210fa9"
  integrity sha512-ETBauow1T35Y/WZMkio9jiM0Z5xjHHmJ4XmjZOq1l/dXz3lr2sRn87nJy20RupqSh1F2m3HHPSp8ShIPQJrJ3A==
  dependencies:
    iconv-lite "^0.6.2"

```
```
encoding@^0.1.11:
  version "0.1.13"
  resolved "https://private_registry_url/encoding/-/encoding-0.1.13.tgz#56574afdd791f54a8e9b2785c0582a2d26210fa9"
  integrity sha512-ETBauow1T35Y/WZMkio9jiM0Z5xjHHmJ4XmjZOq1l/dXz3lr2sRn87nJy20RupqSh1F2m3HHPSp8ShIPQJrJ3A==
  dependencies:
    iconv-lite "^0.6.2"

```

**Option 2**
If the `yarn.lock` file doesn't list the private registry as the dependency source, you can set up Yarn Classic according to the normal package manager instructions:
  1. Define the private registry configuration in a `dependabot.yml` file
  2. Add the registry to a `.yarnrc` file in the project root with the key registry. Alternatively run `yarn config set registry <private registry URL>`.
YAML```
registry https://private_registry_url

```
```
registry https://private_registry_url

```



**Option 3**
If there is no global registry defined in a `.yarnrc` file, you can set `replaces-base: true` in the `dependabot.yml` file. For more information, see [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#npm-registry).
For scoped dependencies (`@my-org/my-dep`), Dependabot requires that the private registry is defined in the project's `.npmrc` file. To define private registries for individual scopes, use `@myscope:registry=https://private_registry_url`.
#### [Yarn Berry](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/removing-dependabot-access-to-public-registries#yarn-berry)
To configure the Yarn Berry ecosystem to only access private registries, you can use these configuration methods.
**Option 1**
Define the private registry configuration in a `dependabot.yml` file. For more information, see [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#npm-registry).
Delete `replaces-base: true` from the configuration file.
To ensure the private registry is listed as the dependency source in the project's `yarn.lock` file, run `yarn install` on a machine with private registry access. Yarn should update the `resolved` field to include the private registry URL.
YAML```
encoding@^0.1.11:
  version "0.1.13"
  resolved "https://private_registry_url/encoding/-/encoding-0.1.13.tgz#56574afdd791f54a8e9b2785c0582a2d26210fa9"
  integrity sha512-ETBauow1T35Y/WZMkio9jiM0Z5xjHHmJ4XmjZOq1l/dXz3lr2sRn87nJy20RupqSh1F2m3HHPSp8ShIPQJrJ3A==
  dependencies:
    iconv-lite "^0.6.2"

```
```
encoding@^0.1.11:
  version "0.1.13"
  resolved "https://private_registry_url/encoding/-/encoding-0.1.13.tgz#56574afdd791f54a8e9b2785c0582a2d26210fa9"
  integrity sha512-ETBauow1T35Y/WZMkio9jiM0Z5xjHHmJ4XmjZOq1l/dXz3lr2sRn87nJy20RupqSh1F2m3HHPSp8ShIPQJrJ3A==
  dependencies:
    iconv-lite "^0.6.2"

```

**Option 2**
If the `yarn.lock` file doesn't list the private registry as the dependency source, you can set up Yarn Berry according to the normal package manager instructions:
  1. Define the private registry configuration in a `dependabot.yml` file
  2. Add the registry to a `.yarnrc.yml` file in the project root with the key `npmRegistryServer`. Alternatively run `yarn config set npmRegistryServer <private registry URL>`. `    npmRegistryServer: "https://private_registry_url"    `


For scoped dependencies (`@my-org/my-dep`), Dependabot requires that the private registry is defined in the project's `.yarnrc` file. To define private registries for individual scopes, use `"@myscope:registry" "https://private_registry_url"`.
## [NuGet](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/removing-dependabot-access-to-public-registries#nuget)
To allow the NuGet ecosystem to only access private registries, you can configure the `dependabot.yml` file. For more information, see [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#nuget-feed).
The NuGet ecosystem additionally requires a `nuget.config` file to be checked into the repository, with either a `< clear />` tag in `<packageSources>` section or a key `nuget.org` as true in the `disabledPackageSources` section of the `nuget.config` file.
This is an example of a `< clear />` tag in the `packageSources` section of the `nuget.config`.
```
<?xml version="1.0" encoding="utf-8"?>
<configuration>
 <packageSources>
   < clear />
   <add key="example-nuget" value="https://private_registry_url/nuget/example-nuget/index.json" />
 </packageSources>
</configuration>

```

This is an example of adding key `nuget.org` as true to the `disabledPackageSources` section of the `nuget.config`
```
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <packageSources>
    <add key="example-nuget" value="https://private_registry_url/nuget/example-nuget/index.json" />
  </packageSources>
  <disabledPackageSources>
    <add key="nuget.org" value="true" />
  </disabledPackageSources>
</configuration>

```

To configure Dependabot to access both private _and_ public feeds, view the following `dependabot.yml` example which includes the configured `public` feed under `registries`:
YAML```
version: 2
registries:
  nuget-example:
    type: nuget-feed
    url: https://nuget.example.com/v3/index.json
    username: $
    password: $
  public:
    type: nuget-feed
    url: https://api.nuget.org/v3/index.json
updates:
  - package-ecosystem: nuget
    directory: "/"
    registries: "*"
    schedule:
      interval: daily

```
```
version: 2
registries:
  nuget-example:
    type: nuget-feed
    url: https://nuget.example.com/v3/index.json
    username: $
    password: $
  public:
    type: nuget-feed
    url: https://api.nuget.org/v3/index.json
updates:
  - package-ecosystem: nuget
    directory: "/"
    registries: "*"
    schedule:
      interval: daily

```

## [Python](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/removing-dependabot-access-to-public-registries#python)
Pip, Pip-compile, Pipenv, and Poetry are the four package managers that the Python ecosystem currently supports.
### [Pip](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/removing-dependabot-access-to-public-registries#pip)
To configure the Pip ecosystem to only access private registries, you can use these configuration methods.
**Option 1**
Define the private registry configuration in a `dependabot.yml` file. For more information, see [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#npm-registry).
Delete `replaces-base: true` from the configuration file.
Add the private registry URL to the `[global]` section of the `pip.conf` file and check the file into the repository.
YAML```
[global]
timeout = 60
index-url = https://private_registry_url

```
```
[global]
timeout = 60
index-url = https://private_registry_url

```

**Option 2**
Set `replaces-base: true` in the `dependabot.yml` file. For more information, see [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#python-index).
### [Pip-compile](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/removing-dependabot-access-to-public-registries#pip-compile)
To configure the Pip-compile ecosystem to only access private registries, you can use these configuration methods.
**Option 1**
Set `replaces-base: true` in the `dependabot.yml` file. For more information, see [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#python-index).
**Option 2**
Define the private registry configuration in a `dependabot.yml` file. For more information, see [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#npm-registry).
Delete `replaces-base: true` from the configuration file.
Add the private registry URL to the `requirements.txt` file and check the file into the repository.
YAML```
--index-url https://private_registry_url

```
```
--index-url https://private_registry_url

```

### [Pipenv](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/removing-dependabot-access-to-public-registries#pipenv)
To configure Pipenv to only access private registries, remove `replaces-base` from the `dependabot.yml` file. For more information, see [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#python-index).
Delete `replaces-base: true` from the configuration file.
Add the private registry URL to the `[[source]]` section of the `Pipfile` file and check the file into the repository.
YAML```
[[source]]
url = "https://private_registry_url"
verify_ssl = true
name = "pypi"

```
```
[[source]]
url = "https://private_registry_url"
verify_ssl = true
name = "pypi"

```

### [Poetry](https://docs.github.com/en/code-security/dependabot/maintain-dependencies/removing-dependabot-access-to-public-registries#poetry)
To configure Poetry to only access private registries, set `replaces-base: true` in the `dependabot.yml` file. For more information, see [Configuring access to private registries for Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#python-index).
Add the private registry url to the `[[tool.poetry.source]]` section of the `pyproject.toml` file and checked it in the repository.
YAML```
[[tool.poetry.source]]
name = "private"
url = "https://private_registry_url"
default = true

```
```
[[tool.poetry.source]]
name = "private"
url = "https://private_registry_url"
default = true

```

