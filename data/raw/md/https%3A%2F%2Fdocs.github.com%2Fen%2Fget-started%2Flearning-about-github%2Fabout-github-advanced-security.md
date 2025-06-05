  * [Get started](https://docs.github.com/en/get-started "Get started")/
  * [Learning about GitHub](https://docs.github.com/en/get-started/learning-about-github "Learning about GitHub")/
  * [GitHub Advanced Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security "GitHub Advanced Security")


# About GitHub Advanced Security
GitHub makes extra security features available to customers who purchase GitHub Code Security or GitHub Secret Protection. Some features are enabled for public repositories by default.
## Who can use this feature?
GitHub Code Security and GitHub Secret Protection are available for accounts on GitHub Team and GitHub Enterprise Cloud.
Some features are also available for free for public repositories on GitHub.com. For more information, see [GitHub’s plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans).
For information about GitHub Advanced Security for Azure DevOps, see [Configure GitHub Advanced Security for Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features) in Microsoft Learn.
## In this article
  * [About GitHub Advanced Security products](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security#about-github-advanced-security-products)
  * [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security#github-code-security)
  * [GitHub Secret Protection](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security#github-secret-protection)
  * [Run an assessment of your organization's exposure to secret leaks](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security#run-an-assessment-of-your-organizations-exposure-to-secret-leaks)
  * [Deploying GitHub Code Security and GitHub Secret Protection](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security#deploying-github-code-security-and-github-secret-protection)
  * [Enabling features](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security#enabling-features)
  * [About GitHub Advanced Security Certification](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security#about-github-advanced-security-certification)
  * [About GitHub Advanced Security with Azure Repos](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security#about-github-advanced-security-with-azure-repos)
  * [Further reading](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security#further-reading)


## [About GitHub Advanced Security products](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security#about-github-advanced-security-products)
GitHub has many features that help you improve and maintain the quality of your code. Some of these are included in all plans, such as dependency graph and Dependabot alerts.
Other security features require you to purchase one of GitHub's Advanced Security products:
  * **GitHub Secret Protection** , which includes features that help you detect and prevent secret leaks, such as secret scanning and push protection.
  * **GitHub Code Security** , which includes features that help you find and fix vulnerabilities, like code scanning, premium Dependabot features, and dependency review.


Some of these features, such as code scanning and secret scanning, are enabled for public repositories by default. To run the feature on your private or internal repositories, you must purchase the relevant GitHub Advanced Security product.
You must be on a GitHub Team or GitHub Enterprise plan in order to purchase GitHub Code Security or GitHub Secret Protection. For more information, see [GitHub’s plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans) and [About billing for GitHub Advanced Security](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-advanced-security/about-billing-for-github-advanced-security).
## [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security#github-code-security)
You get the following features with GitHub Code Security:
  * **Code scanning** : Search for potential security vulnerabilities and coding errors in your code using CodeQL or a third-party tool.
  * **CodeQL CLI** : Run CodeQL processes locally on software projects or to generate code scanning results for upload to GitHub.
  * **Copilot Autofix** : Get automatically generated fixes for code scanning alerts.
  * **Security campaigns** : Reduce security debt at scale.
  * **Custom auto-triage rules for Dependabot** : Manage your Dependabot alerts at scale, by automating which alerts you want to ignore, snooze, or trigger a Dependabot security update for.
  * **Dependency review** : Show the full impact of changes to dependencies and see details of any vulnerable versions before you merge a pull request.
  * **Security overview** : Understand the distribution of risk across your organization.


The table below summarizes the availability of GitHub Code Security features for public and private repositories.
| Public repository   
without GitHub Code Security | Private repository   
without GitHub Code Security | Public or private repository   
with GitHub Code Security  
---|---|---|---  
Code scanning |  |  |   
CodeQL CLI |  |  |   
Copilot Autofix |  |  |   
Security campaigns |  |  |   
Custom auto-triage rules |  |  |   
Dependency review |  |  |   
Security overview |  |  |   
For more information about features, see [GitHub security features](https://docs.github.com/en/code-security/getting-started/github-security-features).
## [GitHub Secret Protection](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security#github-secret-protection)
You get the following features with GitHub Secret Protection:
  * **Secret scanning** : Detect secrets, for example keys and tokens, that have been checked into a repository and receive alerts.
  * **Push protection** : Prevent secret leaks before they happen by blocking commits containing secrets.
  * **Copilot secret scanning** : Leverage AI to detect unstructured credentials, such as passwords, that have been checked into a repository.
  * **Custom patterns** : Detect and prevent leaks for organization-specific secrets.
  * **Delegated bypass for push protection** and **Delegated alert dismissal** : Implement an approval process for better control over who in your enterprise can perform sensitive actions, supporting governance at scale.
  * **Security overview** : Understand the distribution of risk across your organization.


The table below summarizes the availability of GitHub Secret Protection features for public and private repositories.
| Public repository   
without GitHub Secret Protection | Private repository   
without GitHub Secret Protection | Public or private repository   
with GitHub Secret Protection  
---|---|---|---  
Secret scanning |  |  |   
Push protection |  |  |   
Copilot secret scanning |  |  |   
Custom patterns |  |  |   
Delegated bypass for push protection |  |  |   
Security overview |  |  |   
For more information about individual features, see [GitHub security features](https://docs.github.com/en/code-security/getting-started/github-security-features).
## [Run an assessment of your organization's exposure to secret leaks](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security#run-an-assessment-of-your-organizations-exposure-to-secret-leaks)
Organizations on GitHub Team and GitHub Enterprise can run a free report to scan the code in the organization for leaked secrets. This can help you understand the current exposure of repositories in your organization to leaked secrets, as well as help you see how many existing secret leaks could have been prevented by GitHub Secret Protection. See [About the secret risk assessment](https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/about-secret-risk-assessment).
## [Deploying GitHub Code Security and GitHub Secret Protection](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security#deploying-github-code-security-and-github-secret-protection)
To learn about what you need to know to plan your deployment of GitHub Code Security and GitHub Secret Protection at a high level and to review the rollout phases we recommended, see [Adopting GitHub Advanced Security at scale](https://docs.github.com/en/code-security/adopting-github-advanced-security-at-scale).
## [Enabling features](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security#enabling-features)
You can quickly enable security features at scale with the GitHub-recommended security configuration, a collection of security enablement settings you can apply to repositories in an organization. You can then further customize Advanced Security features at the organization level with global settings. See [About enabling security features at scale](https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/about-enabling-security-features-at-scale).
If you are on a GitHub Team or GitHub Enterprise plan, license use for the entire team or enterprise is shown on your license page. See [Viewing and downloading licensed use of Advanced Security](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-advanced-security/viewing-your-github-advanced-security-usage).
## [About GitHub Advanced Security Certification](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security#about-github-advanced-security-certification)
You can highlight your knowledge by earning a GitHub Advanced Security certificate with GitHub Certifications. The certification validates your expertise in vulnerability identification, workflow security, and robust security implementation. See [About GitHub Certifications](https://docs.github.com/en/get-started/showcase-your-expertise-with-github-certifications/about-github-certifications).
## [About GitHub Advanced Security with Azure Repos](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security#about-github-advanced-security-with-azure-repos)
If you want to use GitHub Advanced Security with Azure Repos, see [GitHub Advanced Security & Azure DevOps](https://resources.github.com/topics/github-advanced-security/) in our resources site. For documentation, see [Configure GitHub Advanced Security for Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features) in Microsoft Learn.
## [Further reading](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security#further-reading)
  * [GitHub security features](https://docs.github.com/en/code-security/getting-started/github-security-features)
  * [GitHub public roadmap](https://github.com/github/roadmap)


