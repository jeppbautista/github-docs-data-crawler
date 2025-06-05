  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Create advanced setup](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning "Create advanced setup")/
  * [Hardware resources for CodeQL](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/recommended-hardware-resources-for-running-codeql "Hardware resources for CodeQL")


# Recommended hardware resources for running CodeQL
Recommended specifications (RAM, CPU cores, and disk) for running CodeQL analysis on self-hosted machines, based on the size of your codebase.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


You can configure CodeQL on GitHub Actions or on an external CI system. CodeQL is fully compatible with GitHub-hosted runners on GitHub Actions.
If you're using an external CI system, or self-hosted runners on GitHub Actions for private repositories, you're responsible for configuring your own hardware. The optimal hardware configuration for running CodeQL may vary based on the size and complexity of your codebase, the programming languages and build systems being used, and your CI workflow configuration.
The table below provides recommended hardware specifications for running CodeQL analysis, based on the size of your codebase. Use these as a starting point for determining your choice of hardware or virtual machine. A machine with greater resources may improve analysis performance, but may also be more expensive to maintain.
Codebase size | RAM | CPU  
---|---|---  
Small (<100 K lines of code) | 8 GB or higher | 2 cores  
Medium (100 K to 1 M lines of code) | 16 GB or higher | 4 or 8 cores  
Large (>1 M lines of code) | 64 GB or higher | 8 cores  
For all codebase sizes, we recommend using an SSD with 14 GB or more of disk space. There must be enough disk space to check out and build your code, plus additional space for data produced by CodeQL.
