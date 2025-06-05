  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Supply chain security](https://docs.github.com/en/code-security/supply-chain-security "Supply chain security")/
  * [Understand your supply chain](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain "Understand your supply chain")/
  * [Configure dependency review action](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-review-action "Configure dependency review action")


# Configuring the dependency review action
You can use the dependency review action to catch vulnerabilities before they are added to your project.
## Who can use this feature?
Repository owners, organization owners, security managers, and users with the **admin** role
## In this article
  * [About the dependency review action](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-review-action#about-the-dependency-review-action)
  * [Configuring the dependency review action](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-review-action#configuring-the-dependency-review-action)
  * [Further reading](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-review-action#further-reading)


## [About the dependency review action](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-review-action#about-the-dependency-review-action)
The "dependency review action" refers to the specific action that can report on differences in a pull request within the GitHub Actions context, and add enforcement mechanisms to the GitHub Actions workflow.
The dependency review action scans your pull requests for dependency changes and raises an error if any new dependencies have known vulnerabilities. The action is supported by an API endpoint that compares the dependencies between two revisions and reports any differences.
For more information about the action and the API endpoint, see the [`dependency-review-action`](https://github.com/actions/dependency-review-action) documentation, and [REST API endpoints for dependency review](https://docs.github.com/en/rest/dependency-graph/dependency-review).
Organization owners can roll out dependency review at scale by enforcing the use of the dependency review action across repositories in the organization. This involves the use of repository rulesets for which you'll set the dependency review action as a required workflow, which means that pull requests can only be merged once the workflow passes all the required checks. For more information, see [Enforcing dependency review across an organization](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/enforcing-dependency-review-across-an-organization).
Here is a list of common configuration options. For more information, and a full list of options, see [Dependency Review](https://github.com/marketplace/actions/dependency-review) on the GitHub Marketplace.
Option | Required | Usage  
---|---|---  
`fail-on-severity` |  | Defines the threshold for level of severity (`low`, `moderate`, `high`, `critical`).  
The action will fail on any pull requests that introduce vulnerabilities of the specified severity level or higher.  
`allow-licenses` |  | Contains a list of allowed licenses. You can find the possible values for this parameter in the [Licenses](https://docs.github.com/en/rest/licenses) page of the API documentation.  
The action will fail on pull requests that introduce dependencies with licenses that do not match the list.  
`deny-licenses` |  | Contains a list of prohibited licenses. You can find the possible values for this parameter in the [Licenses](https://docs.github.com/en/rest/licenses) page of the API documentation.  
The action will fail on pull requests that introduce dependencies with licenses that match the list.  
`fail-on-scopes` |  | Contains a list of strings representing the build environments you want to support (`development`, `runtime`, `unknown`).   
The action will fail on pull requests that introduce vulnerabilities in the scopes that match the list.  
`comment-summary-in-pr` |  | Enable or disable the reporting of the review summary as a comment in the pull request. If enabled, you must give the workflow or job the `pull-requests: write` permission. With each execution, a new comment will overwrite the existing one.  
`allow-ghsas` |  | Contains a list of GitHub Advisory Database IDs that can be skipped during detection. You can find the possible values for this parameter in the [GitHub Advisory Database](https://github.com/advisories).  
`config-file` |  | Specifies a path to a configuration file. The configuration file can be local to the repository or a file located in an external repository.  
`external-repo-token` |  | Specifies a token for fetching the configuration file, if the file resides in a private external repository. The token must have read access to the repository.  
The `allow-licenses` and `deny-licenses` options are mutually exclusive.
## [Configuring the dependency review action](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-review-action#configuring-the-dependency-review-action)
There are two methods of configuring the dependency review action:
  * Inlining the configuration options in your workflow file.
  * Referencing a configuration file in your workflow file.


Notice that all of the examples use a short version number for the action (`v3`) instead of a semver release number (for example, `v3.0.8`). This ensures that you use the most recent minor version of the action.
### [Using inline configuration to set up the dependency review action](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-review-action#using-inline-configuration-to-set-up-the-dependency-review-action)
  1. Add a new YAML workflow to your `.github/workflows` folder.
YAML```
name: 'Dependency Review'
on: [pull_request]

permissions:
  contents: read

jobs:
  dependency-review:
    runs-on: ubuntu-latest
    steps:
     - name: 'Checkout Repository'
       uses: actions/checkout@v4
     - name: Dependency Review
       uses: actions/dependency-review-action@v4

```
```
name: 'Dependency Review'
on: [pull_request]

permissions:
  contents: read

jobs:
  dependency-review:
    runs-on: ubuntu-latest
    steps:
     - name: 'Checkout Repository'
       uses: actions/checkout@v4
     - name: Dependency Review
       uses: actions/dependency-review-action@v4

```

  2. Specify your settings.
This dependency review action example file illustrates how you can use the available configuration options.
YAML```
name: 'Dependency Review'
on: [pull_request]

permissions:
  contents: read

jobs:
  dependency-review:
    runs-on: ubuntu-latest
    steps:
    - name: 'Checkout Repository'
      uses: actions/checkout@v4
    - name: Dependency Review
      uses: actions/dependency-review-action@v4
      with:
        # Possible values: "critical", "high", "moderate", "low"
        fail-on-severity: critical

        
        # You can only include one of these two options: `allow-licenses` and `deny-licenses`
        # ([String]). Only allow these licenses (optional)
        # Possible values: Any SPDX-compliant license identifiers or expressions from https://spdx.org/licenses/
        allow-licenses: GPL-3.0, BSD-3-Clause, MIT
        # ([String]). Block the pull request on these licenses (optional)
        # Possible values: Any SPDX-compliant license identifiers or expressions from https://spdx.org/licenses/
        deny-licenses: LGPL-2.0, BSD-2-Clause
        
        # ([String]). Skip these GitHub Advisory Database IDs during detection (optional)
        # Possible values: Any valid GitHub Advisory Database ID from https://github.com/advisories
        allow-ghsas: GHSA-abcd-1234-5679, GHSA-efgh-1234-5679
        # ([String]). Block pull requests that introduce vulnerabilities in the scopes that match this list (optional)
        # Possible values: "development", "runtime", "unknown"
        fail-on-scopes: development, runtime

```
```
name: 'Dependency Review'
on: [pull_request]

permissions:
  contents: read

jobs:
  dependency-review:
    runs-on: ubuntu-latest
    steps:
    - name: 'Checkout Repository'
      uses: actions/checkout@v4
    - name: Dependency Review
      uses: actions/dependency-review-action@v4
      with:
        # Possible values: "critical", "high", "moderate", "low"
        fail-on-severity: critical

        
        # You can only include one of these two options: `allow-licenses` and `deny-licenses`
        # ([String]). Only allow these licenses (optional)
        # Possible values: Any SPDX-compliant license identifiers or expressions from https://spdx.org/licenses/
        allow-licenses: GPL-3.0, BSD-3-Clause, MIT
        # ([String]). Block the pull request on these licenses (optional)
        # Possible values: Any SPDX-compliant license identifiers or expressions from https://spdx.org/licenses/
        deny-licenses: LGPL-2.0, BSD-2-Clause
        
        # ([String]). Skip these GitHub Advisory Database IDs during detection (optional)
        # Possible values: Any valid GitHub Advisory Database ID from https://github.com/advisories
        allow-ghsas: GHSA-abcd-1234-5679, GHSA-efgh-1234-5679
        # ([String]). Block pull requests that introduce vulnerabilities in the scopes that match this list (optional)
        # Possible values: "development", "runtime", "unknown"
        fail-on-scopes: development, runtime

```



### [Using a configuration file to set up dependency review action](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-review-action#using-a-configuration-file-to-set-up-dependency-review-action)
  1. Add a new YAML workflow to your `.github/workflows` folder and use `config-file` to specify that you are using a configuration file.
YAML```
name: 'Dependency Review'
on: [pull_request]

permissions:
 contents: read

jobs:
  dependency-review:
    runs-on: ubuntu-latest
    steps:
    - name: 'Checkout Repository'
      uses: actions/checkout@v4
    - name: Dependency Review
      uses: actions/dependency-review-action@v4
      with:
       # ([String]). Representing a path to a configuration file local to the repository or in an external repository.
       # Possible values: An absolute path to a local file or an external file.
       config-file: './.github/dependency-review-config.yml'
       # Optional alternative syntax for an external file: OWNER/REPOSITORY/FILENAME@BRANCH (uncomment if preferred)
       # config-file: 'github/octorepo/dependency-review-config.yml@main'

       # ([Token]) Use if your configuration file resides in a private external repository.
       # Possible values: Any GitHub token with read access to the private external repository.
       external-repo-token: 'ghp_123456789abcde'

```
```
name: 'Dependency Review'
on: [pull_request]

permissions:
 contents: read

jobs:
  dependency-review:
    runs-on: ubuntu-latest
    steps:
    - name: 'Checkout Repository'
      uses: actions/checkout@v4
    - name: Dependency Review
      uses: actions/dependency-review-action@v4
      with:
       # ([String]). Representing a path to a configuration file local to the repository or in an external repository.
       # Possible values: An absolute path to a local file or an external file.
       config-file: './.github/dependency-review-config.yml'
       # Optional alternative syntax for an external file: OWNER/REPOSITORY/FILENAME@BRANCH (uncomment if preferred)
       # config-file: 'github/octorepo/dependency-review-config.yml@main'

       # ([Token]) Use if your configuration file resides in a private external repository.
       # Possible values: Any GitHub token with read access to the private external repository.
       external-repo-token: 'ghp_123456789abcde'

```

  2. Create the configuration file in the path you have specified.
This YAML example file illustrates how you can use the available configuration options.
YAML```
  # Possible values: "critical", "high", "moderate", "low"
  fail-on-severity: critical

  # You can only include one of these two options: `allow-licenses` and `deny-licenses`
  # ([String]). Only allow these licenses (optional)
  # Possible values: Any SPDX-compliant license identifiers or expressions from https://spdx.org/licenses/
  allow-licenses:
    - GPL-3.0
    - BSD-3-Clause
    - MIT
   # ([String]). Block the pull request on these licenses (optional)
   # Possible values: Any SPDX-compliant license identifiers or expressions from https://spdx.org/licenses/
  deny-licenses:
    - LGPL-2.0
    - BSD-2-Clause

   # ([String]). Skip these GitHub Advisory Database IDs during detection (optional)
   # Possible values: Any valid GitHub Advisory Database ID from https://github.com/advisories
  allow-ghsas:
    - GHSA-abcd-1234-5679
    - GHSA-efgh-1234-5679
   # ([String]). Block pull requests that introduce vulnerabilities in the scopes that match this list (optional)
   # Possible values: "development", "runtime", "unknown"
  fail-on-scopes:
    - development
    - runtime

```
```
  # Possible values: "critical", "high", "moderate", "low"
  fail-on-severity: critical

  # You can only include one of these two options: `allow-licenses` and `deny-licenses`
  # ([String]). Only allow these licenses (optional)
  # Possible values: Any SPDX-compliant license identifiers or expressions from https://spdx.org/licenses/
  allow-licenses:
    - GPL-3.0
    - BSD-3-Clause
    - MIT
   # ([String]). Block the pull request on these licenses (optional)
   # Possible values: Any SPDX-compliant license identifiers or expressions from https://spdx.org/licenses/
  deny-licenses:
    - LGPL-2.0
    - BSD-2-Clause

   # ([String]). Skip these GitHub Advisory Database IDs during detection (optional)
   # Possible values: Any valid GitHub Advisory Database ID from https://github.com/advisories
  allow-ghsas:
    - GHSA-abcd-1234-5679
    - GHSA-efgh-1234-5679
   # ([String]). Block pull requests that introduce vulnerabilities in the scopes that match this list (optional)
   # Possible values: "development", "runtime", "unknown"
  fail-on-scopes:
    - development
    - runtime

```



For further details about the configuration options, see [`dependency-review-action`](https://github.com/actions/dependency-review-action#readme).
## [Further reading](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-review-action#further-reading)
  * [Customizing your dependency review action configuration](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/customizing-your-dependency-review-action-configuration)


