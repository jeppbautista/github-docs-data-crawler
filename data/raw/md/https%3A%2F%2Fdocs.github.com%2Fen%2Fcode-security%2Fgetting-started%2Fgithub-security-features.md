  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Getting started](https://docs.github.com/en/code-security/getting-started "Getting started")/
  * [GitHub security features](https://docs.github.com/en/code-security/getting-started/github-security-features "GitHub security features")


# GitHub security features
An overview of GitHub's security features.
## In this article
  * [About GitHub's security features](https://docs.github.com/en/code-security/getting-started/github-security-features#about-githubs-security-features)
  * [Available for all GitHub plans](https://docs.github.com/en/code-security/getting-started/github-security-features#available-for-all-github-plans)
  * [Available with GitHub Secret Protection](https://docs.github.com/en/code-security/getting-started/github-security-features#available-with-github-secret-protection)
  * [Available with GitHub Code Security](https://docs.github.com/en/code-security/getting-started/github-security-features#available-with-github-code-security)
  * [Further reading](https://docs.github.com/en/code-security/getting-started/github-security-features#further-reading)


## [About GitHub's security features](https://docs.github.com/en/code-security/getting-started/github-security-features#about-githubs-security-features)
GitHub's security features help keep your code and secrets secure in repositories and across organizations.
  * Some features are available for all GitHub plans.
  * Additional features are available to organizations on GitHub Team and GitHub Enterprise Cloud that purchase a GitHub Advanced Security product: 
    * [GitHub Secret Protection](https://docs.github.com/en/code-security/getting-started/github-security-features#available-with-github-secret-protection)
    * [GitHub Code Security](https://docs.github.com/en/code-security/getting-started/github-security-features#available-with-github-code-security)
  * In addition, a number of GitHub Secret Protection and GitHub Code Security features can be run on public repositories for free.


## [Available for all GitHub plans](https://docs.github.com/en/code-security/getting-started/github-security-features#available-for-all-github-plans)
The following security features are available for you to use, regardless of the GitHub plan you are on. You don't need to purchase GitHub Secret Protection or GitHub Code Security to use these features.
Most of these features are available for public and private repositories. Some features are _only_ available for public repositories.
### [Security policy](https://docs.github.com/en/code-security/getting-started/github-security-features#security-policy)
Make it easy for your users to confidentially report security vulnerabilities they've found in your repository. For more information, see [Adding a security policy to your repository](https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository).
### [Dependency graph](https://docs.github.com/en/code-security/getting-started/github-security-features#dependency-graph)
The dependency graph allows you to explore the ecosystems and packages that your repository depends on and the repositories and packages that depend on your repository.
You can find the dependency graph on the **Insights** tab for your repository. For more information, see [About the dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph).
### [Software Bill of Materials (SBOM)](https://docs.github.com/en/code-security/getting-started/github-security-features#software-bill-of-materials-sbom)
You can export the dependency graph of your repository as an SPDX-compatible, Software Bill of Materials (SBOM). For more information, see [Exporting a software bill of materials for your repository](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exporting-a-software-bill-of-materials-for-your-repository).
### [GitHub Advisory Database](https://docs.github.com/en/code-security/getting-started/github-security-features#github-advisory-database)
The GitHub Advisory Database contains a curated list of security vulnerabilities that you can view, search, and filter. For more information, see [Browsing security advisories in the GitHub Advisory Database](https://docs.github.com/en/code-security/security-advisories/working-with-global-security-advisories-from-the-github-advisory-database/browsing-security-advisories-in-the-github-advisory-database).
### [Dependabot alerts and security updates](https://docs.github.com/en/code-security/getting-started/github-security-features#dependabot-alerts-and-security-updates)
View alerts about dependencies that are known to contain security vulnerabilities, and choose whether to have pull requests generated automatically to update these dependencies. For more information, see [About Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts) and [About Dependabot security updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates).
You can also use default Dependabot auto-triage rules curated by GitHub to automatically filter out a substantial amount of false positives.
For an overview of the different features offered by Dependabot and instructions on how to get started, see [Dependabot quickstart guide](https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide).
### [Dependabot version updates](https://docs.github.com/en/code-security/getting-started/github-security-features#dependabot-version-updates)
Use Dependabot to automatically raise pull requests to keep your dependencies up-to-date. This helps reduce your exposure to older versions of dependencies. Using newer versions makes it easier to apply patches if security vulnerabilities are discovered, and also makes it easier for Dependabot security updates to successfully raise pull requests to upgrade vulnerable dependencies. You can also customize Dependabot version updates to streamline their integration into your repositories. For more information, see [About Dependabot version updates](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/about-dependabot-version-updates).
### [Security advisories](https://docs.github.com/en/code-security/getting-started/github-security-features#security-advisories)
Privately discuss and fix security vulnerabilities in your public repository's code. You can then publish a security advisory to alert your community to the vulnerability and encourage community members to upgrade. For more information, see [About repository security advisories](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/about-repository-security-advisories).
### [Repository rulesets](https://docs.github.com/en/code-security/getting-started/github-security-features#repository-rulesets)
Enforce consistent code standards, security, and compliance across branches and tags. For more information, see [About rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets).
### [Artifact attestations](https://docs.github.com/en/code-security/getting-started/github-security-features#artifact-attestations)
Create unfalsifiable provenance and integrity guarantees for the software you build. For more information, see [Using artifact attestations to establish provenance for builds](https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds).
If you are on a GitHub Free, GitHub Pro, or GitHub Team plan, artifact attestations are only available for public repositories. To use artifact attestations in private or internal repositories, you must be on a GitHub Enterprise Cloud plan.
### [Secret scanning alerts for partners](https://docs.github.com/en/code-security/getting-started/github-security-features#secret-scanning-alerts-for-partners)
When GitHub detects a leaked secret in a public repository, or a public npm packages, GitHub informs the relevant service provider that the secret may be compromised. For details of the supported secrets and service providers, see [Supported secret scanning patterns](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#supported-secrets).
### [Push protection for users](https://docs.github.com/en/code-security/getting-started/github-security-features#push-protection-for-users)
Push protection for users automatically protects you from accidentally committing secrets to public repositories, regardless of whether the repository itself has secret scanning enabled. Push protection for users is on by default, but you can disable the feature at any time through your personal account settings. For more information, see [Push protection for users](https://docs.github.com/en/code-security/secret-scanning/working-with-secret-scanning-and-push-protection/push-protection-for-users).
## [Available with GitHub Secret Protection](https://docs.github.com/en/code-security/getting-started/github-security-features#available-with-github-secret-protection)
For accounts on GitHub Team and GitHub Enterprise Cloud, you can access additional security features when you purchase **GitHub Secret Protection**.
GitHub Secret Protection includes features that help you detect and prevent secret leaks, such as secret scanning and push protection.
These features are available for all repository types. Some of these features are available for public repositories free of charge, meaning that you don't need to purchase GitHub Secret Protection to enable the feature on a public repository.
### [Secret scanning alerts for users](https://docs.github.com/en/code-security/getting-started/github-security-features#secret-scanning-alerts-for-users)
Automatically detect tokens or credentials that have been checked into a repository. You can view alerts for any secrets that GitHub finds in your code, in the **Security** tab of the repository, so that you know which tokens or credentials to treat as compromised. For more information, see [About secret scanning alerts](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/about-alerts#about-user-alerts).
Available for public repositories by default.
### [Copilot secret scanning](https://docs.github.com/en/code-security/getting-started/github-security-features#copilot-secret-scanning)
Copilot secret scanning's generic secret detection is an AI-powered expansion of secret scanning that identifies unstructured secrets (passwords) in your source code and then generates an alert. For more information, see [Responsible detection of generic secrets with Copilot secret scanning](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-generic-secrets).
### [Push protection](https://docs.github.com/en/code-security/getting-started/github-security-features#push-protection)
Push protection proactively scans your code, and any repository contributors' code, for secrets during the push process and blocks the push if any secrets are detected. If a contributor bypasses the block, GitHub creates an alert. For more information, see [About push protection](https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection).
Available for public repositories by default.
### [Delegated bypass for push protection](https://docs.github.com/en/code-security/getting-started/github-security-features#delegated-bypass-for-push-protection)
Delegated bypass for push protection lets you control which individuals, roles and teams can bypass push protection, and implements a review and approval cycle for pushes containing secrets. For more information, see [About delegated bypass for push protection](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/about-delegated-bypass-for-push-protection).
### [Custom patterns](https://docs.github.com/en/code-security/getting-started/github-security-features#custom-patterns)
You can define custom patterns to identify secrets that are not detected by the default patterns supported by secret scanning, such as patterns that are internal to your organization. For more information, see [Defining custom patterns for secret scanning](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/defining-custom-patterns-for-secret-scanning).
### [Security overview](https://docs.github.com/en/code-security/getting-started/github-security-features#security-overview)
Security overview allows you to review the overall security landscape of your organization, view trends and other insights, and manage security configurations, making it easy to monitor your organization's security status and identify the repositories and organizations at greatest risk. For more information, see [About security overview](https://docs.github.com/en/code-security/security-overview/about-security-overview).
## [Available with GitHub Code Security](https://docs.github.com/en/code-security/getting-started/github-security-features#available-with-github-code-security)
For accounts on GitHub Team and GitHub Enterprise Cloud, you can access additional security features when you purchase **GitHub Code Security**.
GitHub Code Security includes features that help you find and fix vulnerabilities, like code scanning, premium Dependabot features, and dependency review.
These features are available for all repository types. Some of these features are available for public repositories free of charge, meaning that you don't need to purchase GitHub Code Security to enable the feature on a public repository.
### [Code scanning](https://docs.github.com/en/code-security/getting-started/github-security-features#code-scanning)
Automatically detect security vulnerabilities and coding errors in new or modified code. Potential problems are highlighted, with detailed information, allowing you to fix the code before it's merged into your default branch. For more information, see [About code scanning](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning).
Available for public repositories by default.
### [CodeQL CLI](https://docs.github.com/en/code-security/getting-started/github-security-features#codeql-cli)
Run CodeQL processes locally on software projects or to generate code scanning results for upload to GitHub. For more information, see [About the CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/about-the-codeql-cli).
Available for public repositories by default.
### [Copilot Autofix](https://docs.github.com/en/code-security/getting-started/github-security-features#copilot-autofix)
Get automatically generated fixes for code scanning alerts. For more information, see [Responsible use of Copilot Autofix for code scanning](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/responsible-use-autofix-code-scanning).
Available for public repositories by default.
### [Custom auto-triage rules for Dependabot](https://docs.github.com/en/code-security/getting-started/github-security-features#custom-auto-triage-rules-for-dependabot)
Help you manage your Dependabot alerts at scale. With custom auto-triage rules you have control over the alerts you want to ignore, snooze, or trigger a Dependabot security update for. For more information, see [About Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts) and [Customizing auto-triage rules to prioritize Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/customizing-auto-triage-rules-to-prioritize-dependabot-alerts).
### [Dependency review](https://docs.github.com/en/code-security/getting-started/github-security-features#dependency-review)
Show the full impact of changes to dependencies and see details of any vulnerable versions before you merge a pull request. For more information, see [About dependency review](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review).
Available for public repositories by default.
### [Security campaigns](https://docs.github.com/en/code-security/getting-started/github-security-features#security-campaigns)
Fix security alerts at scale by creating security campaigns and collaborating with developers to reduce your security backlog. For more information, see [About security campaigns](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/about-security-campaigns).
### [Security overview](https://docs.github.com/en/code-security/getting-started/github-security-features#security-overview-1)
Security overview allows you to review the overall security landscape of your organization, view trends and other insights, and manage security configurations, making it easy to monitor your organization's security status and identify the repositories and organizations at greatest risk. For more information, see [About security overview](https://docs.github.com/en/code-security/security-overview/about-security-overview).
## [Further reading](https://docs.github.com/en/code-security/getting-started/github-security-features#further-reading)
  * [GitHub’s plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans)
  * [About GitHub Advanced Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security)
  * [GitHub language support](https://docs.github.com/en/get-started/learning-about-github/github-language-support)


