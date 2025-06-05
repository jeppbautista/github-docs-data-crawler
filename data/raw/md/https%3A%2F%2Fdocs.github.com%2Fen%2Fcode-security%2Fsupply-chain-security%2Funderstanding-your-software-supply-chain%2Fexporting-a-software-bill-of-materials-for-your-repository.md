  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Supply chain security](https://docs.github.com/en/code-security/supply-chain-security "Supply chain security")/
  * [Understand your supply chain](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain "Understand your supply chain")/
  * [Export dependencies as SBOM](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exporting-a-software-bill-of-materials-for-your-repository "Export dependencies as SBOM")


# Exporting a software bill of materials for your repository
You can export a software bill of materials or SBOM for your repository from the dependency graph. SBOMs allow transparency into your open source usage and help expose supply chain vulnerabilities, reducing supply chain risks.
## Who can use this feature?
Anyone on GitHub
## In this article
  * [About the dependency graph and SBOM exports](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exporting-a-software-bill-of-materials-for-your-repository#about-the-dependency-graph-and-sbom-exports)
  * [Exporting a software bill of materials for your repository from the UI](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exporting-a-software-bill-of-materials-for-your-repository#exporting-a-software-bill-of-materials-for-your-repository-from-the-ui)
  * [Exporting a software bill of materials for your repository using the REST API](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exporting-a-software-bill-of-materials-for-your-repository#exporting-a-software-bill-of-materials-for-your-repository-using-the-rest-api)
  * [Generating a software bill of materials from GitHub Actions](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exporting-a-software-bill-of-materials-for-your-repository#generating-a-software-bill-of-materials-from-github-actions)


## [About the dependency graph and SBOM exports](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exporting-a-software-bill-of-materials-for-your-repository#about-the-dependency-graph-and-sbom-exports)
The dependency graph is a summary of the manifest and lock files stored in a repository and any dependencies that are submitted for the repository using the dependency submission API. For each repository, it shows:
  * Dependencies, the ecosystems and packages it depends on
  * Dependents, the repositories and packages that depend on it


For each dependency, you can see the version, license information, the manifest file which included it, and whether it has known vulnerabilities. For package ecosystems supporting transitive dependencies, the relationship status will be displayed and you can click "
You can also search for a specific dependency using the search bar. Dependencies are sorted automatically with vulnerable packages at the top.
You can export the current state of the dependency graph for your repository as a Software Bill of Materials (SBOM) using the industry standard [SPDX](https://spdx.github.io/spdx-spec/v2.3/) format:
  * Via the GitHub UI
  * Using the REST API


An SBOM is a formal, machine-readable inventory of a project's dependencies and associated information (such as versions, package identifiers, licenses, transitive paths for package ecosystems with support for transitive dependency labeling, and copyright information). SBOMs help reduce supply chain risks by:
  * Providing transparency about the dependencies used by your repository
  * Allowing vulnerabilities to be identified across your codebase
  * Providing insights in the license compliance, security, or quality issues that may exist in your codebase
  * Enabling you to better comply with various data protection standards


For more information about the ecosystems supporting transitive dependency labeling, see [Dependency graph supported package ecosystems](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/dependency-graph-supported-package-ecosystems).
If your company provides software to the US federal government per [Executive Order 14028](https://www.gsa.gov/technology/it-contract-vehicles-and-purchasing-programs/information-technology-category/it-security/executive-order-14028), you will need to provide an SBOM for your product. You can also use SBOMs as part of your audit process and use them to comply with regulatory and legal requirements.
Dependents are not included in SBOMs.
## [Exporting a software bill of materials for your repository from the UI](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exporting-a-software-bill-of-materials-for-your-repository#exporting-a-software-bill-of-materials-for-your-repository-from-the-ui)
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the main page of a repository. In the horizontal navigation bar, a tab, labeled with a graph icon and "Insights," is outlined in orange.](https://docs.github.com/assets/cb-52175/images/help/repository/repo-nav-insights-tab.png)
  3. In the left sidebar, click **Dependency graph**.
  4. On the top right side of the **Dependencies** tab, click **Export SBOM** to generate an SBOM file for download from your browser.


## [Exporting a software bill of materials for your repository using the REST API](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exporting-a-software-bill-of-materials-for-your-repository#exporting-a-software-bill-of-materials-for-your-repository-using-the-rest-api)
If you want to use the REST API to export an SBOM for your repository, see [REST API endpoints for software bill of materials (SBOM)](https://docs.github.com/en/rest/dependency-graph/sboms#export-a-software-bill-of-materials-sbom-for-a-repository).
## [Generating a software bill of materials from GitHub Actions](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exporting-a-software-bill-of-materials-for-your-repository#generating-a-software-bill-of-materials-from-github-actions)
The following actions will generate an SBOM for your repository and attach it as a workflow artifact which you can download and use in other applications. For more information about downloading workflow artifacts, see [Downloading workflow artifacts](https://docs.github.com/en/actions/managing-workflow-runs/downloading-workflow-artifacts).
Action | Details  
---|---  
[SPDX Dependency Submission Action](https://github.com/marketplace/actions/spdx-dependency-submission-action) | Uses [Microsoft's SBOM Tool](https://github.com/microsoft/sbom-tool) to create SPDX 2.2 compatible SBOMs with the [supported ecosystems](https://github.com/microsoft/component-detection/blob/main/docs/feature-overview.md)  
[Anchore SBOM Action](https://github.com/marketplace/actions/anchore-sbom-action) | Uses [Syft](https://github.com/anchore/syft) to create SPDX 2.2 compatible SBOMs with the [supported ecosystems](https://github.com/anchore/syft#supported-ecosystems)  
[SBOM Dependency Submission Action](https://github.com/marketplace/actions/sbom-submission-action) | Uploads a CycloneDX SBOM to the dependency submission API
