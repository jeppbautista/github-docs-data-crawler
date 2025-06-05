  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Getting started](https://docs.github.com/en/code-security/getting-started "Getting started")/
  * [Secure repository quickstart](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository "Secure repository quickstart")


# Quickstart for securing your repository
Manage access to your code. Find and fix vulnerable code and dependencies automatically.
## Who can use this feature?
Repository owners, organization owners, security managers, and users with the **admin** role
## In this article
  * [Introduction](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository#introduction)
  * [Managing access to your repository](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository#managing-access-to-your-repository)
  * [Managing the dependency graph](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository#managing-the-dependency-graph)
  * [Managing Dependabot alerts](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository#managing-dependabot-alerts)
  * [Managing dependency review](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository#managing-dependency-review)
  * [Managing Dependabot security updates](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository#managing-dependabot-security-updates)
  * [Managing Dependabot version updates](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository#managing-dependabot-version-updates)
  * [Configuring Code Security](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository#configuring-code-security)
  * [Configuring Secret Protection](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository#configuring-secret-protection)
  * [Setting a security policy](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository#setting-a-security-policy)
  * [Next steps](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository#next-steps)


## [Introduction](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository#introduction)
This guide shows you how to configure security features for a repository.
Your security needs are unique to your repository, so you may not need to enable every feature for your repository. For more information, see [GitHub security features](https://docs.github.com/en/code-security/getting-started/github-security-features).
Some features are available for repositories on all plans. Additional features are available to organizations and enterprises that use GitHub Secret Protection, GitHub Code Security, or GitHub Advanced Security. GitHub Advanced Security features are also enabled for all public repositories on GitHub. For more information, see [About GitHub Advanced Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security).
## [Managing access to your repository](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository#managing-access-to-your-repository)
The first step to securing a repository is to establish who can see and modify your code. For more information, see [Managing your repository’s settings and features](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features).
From the main page of your repository, click 
  * To change who can view your repository, click **Change visibility**. For more information, see [Setting repository visibility](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility).
  * To change who can access your repository and adjust permissions, click **Manage access**. For more information, see [Managing teams and people with access to your repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-teams-and-people-with-access-to-your-repository).


## [Managing the dependency graph](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository#managing-the-dependency-graph)
Repository administrators can enable or disable the dependency graph for repositories. The dependency graph interprets manifest and lock files in a repository to identify dependencies.
  1. From the main page of your repository, click 
  2. Click **Advanced Security**.
  3. Next to Dependency graph, click **Enable** or **Disable**.


For more information, see [Exploring the dependencies of a repository](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exploring-the-dependencies-of-a-repository#enabling-and-disabling-the-dependency-graph).
## [Managing Dependabot alerts](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository#managing-dependabot-alerts)
Dependabot alerts are generated when GitHub identifies a dependency in the dependency graph with a vulnerability. You can enable Dependabot alerts for any repository.
Additionally, you can use Dependabot auto-triage rules to manage your alerts at scale, so you can auto-dismiss or snooze alerts, and specify which alerts you want Dependabot to open pull requests for. For information about the different types of auto-triage rules, and whether your repositories are eligible, see [About Dependabot auto-triage rules](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/about-dependabot-auto-triage-rules).
For an overview of the different features offered by Dependabot and instructions on how to get started, see [Dependabot quickstart guide](https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide).
  1. Click your profile photo, then click **Settings**.
  2. Click **Advanced Security**.
  3. Click **Enable** next to Dependabot alerts.


For more information, see [About Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts) and [Managing security and analysis settings for your personal account](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-personal-account-settings/managing-security-and-analysis-settings-for-your-personal-account).
## [Managing dependency review](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository#managing-dependency-review)
Dependency review lets you visualize dependency changes in pull requests before they are merged into your repositories. For more information, see [About dependency review](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review).
Dependency review is a GitHub Code Security feature. Dependency review is enabled for all repositories with the dependency graph enabled. Organizations that use GitHub Team or GitHub Enterprise Cloud with GitHub Code Security can additionally enable dependency review for private and internal repositories.
To enable dependency review for a repository, ensure that the dependency graph is enabled and enable GitHub Code Security.
  1. From the main page of your repository, click 
  2. Click **Advanced Security**.
  3. To the right of Code Security, click **Enable**.
  4. Under Code Security, check that dependency graph is enabled for the repository.


## [Managing Dependabot security updates](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository#managing-dependabot-security-updates)
For any repository that uses Dependabot alerts, you can enable Dependabot security updates to raise pull requests with security updates when vulnerabilities are detected.
  1. From the main page of your repository, click 
  2. Click **Advanced Security**.
  3. Next to Dependabot security updates, click **Enable**.


For more information, see [About Dependabot security updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates) and [Configuring Dependabot security updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates).
## [Managing Dependabot version updates](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository#managing-dependabot-version-updates)
You can enable Dependabot to automatically raise pull requests to keep your dependencies up-to-date. For more information, see [About Dependabot version updates](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/about-dependabot-version-updates).
  1. From the main page of your repository, click 
  2. Click **Advanced Security**.
  3. Next to Dependabot version updates, click **Enable** to create a basic `dependabot.yml` configuration file.
  4. Specify the dependencies to update and any associated configuration options, then commit the file to the repository. For more information, see [Configuring Dependabot version updates](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuring-dependabot-version-updates#enabling-dependabot-version-updates).


## [Configuring Code Security](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository#configuring-code-security)
Code Security features are available for all public repositories, and for private repositories owned by organizations that are part of a team or an enterprise that uses GitHub Code Security or GitHub Advanced Security.
GitHub Code Security includes code scanning, CodeQL CLI and Copilot Autofix, as well as other features that find and fix vulnerabilities in your codebase.
You can configure code scanning to automatically identify vulnerabilities and errors in the code stored in your repository by using a CodeQL analysis workflow or third-party tool. Depending on the programming languages in your repository, you can configure code scanning with CodeQL using default setup, in which GitHub automatically determines the languages to scan, query suites to run, and events that will trigger a new scan. For more information, see [Configuring default setup for code scanning](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning).
  1. From the main page of your repository, click 
  2. In the "Security" section of the sidebar, click 
  3. If "Code Security" or "GitHub Advanced Security" is not already enabled, click **Enable**.
  4. To the right of "CodeQL analysis", select **Set up** **Default**.
  5. In the pop-up window that appears, review the default configuration settings for your repository, then click **Enable CodeQL**.
  6. Choose whether you want to enable addition features, such as Copilot Autofix.


As an alternative to default setup, you can use advanced setup, which generates a workflow file you can edit to customize your code scanning with CodeQL. For more information, see [Configuring advanced setup for code scanning](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning#configuring-advanced-setup-for-code-scanning-with-codeql).
## [Configuring Secret Protection](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository#configuring-secret-protection)
Secret Protection features are available for all public repositories, and for private repositories owned by organizations that are part of a team or an enterprise that uses GitHub Secret Protection or GitHub Advanced Security.
GitHub Secret Protection includes secret scanning and push protection, as well as other features that help you detect and prevent secret leaks in your repository.
  1. From the main page of your repository, click 
  2. Click **Advanced Security**.
  3. If "Secret Protection" or "GitHub Advanced Security" is not already enabled, click **Enable**.
  4. If the option "Secret scanning" is shown, click **Enable**.
  5. Choose whether you want to enable additional features, such as scanning for non-provider patterns and push protection.


## [Setting a security policy](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository#setting-a-security-policy)
If you are a repository maintainer, it's good practice to specify a security policy for your repository by creating a file named `SECURITY.md` in the repository. This file instructs users about how to best contact you and collaborate with you when they want to report security vulnerabilities in your repository. You can view the security policy of a repository from the repository’s **Security** tab.
  1. From the main page of your repository, click 
  2. In the left sidebar, under "Reporting", click 
  3. Click **Start setup**.
  4. Add information about supported versions of your project and how to report vulnerabilities.


For more information, see [Adding a security policy to your repository](https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository).
## [Next steps](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository#next-steps)
You can view and manage alerts from security features to address dependencies and vulnerabilities in your code. For more information, see [Viewing and updating Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/viewing-and-updating-dependabot-alerts), [Managing pull requests for dependency updates](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/managing-pull-requests-for-dependency-updates), [Assessing code scanning alerts for your repository](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository), and [Managing alerts from secret scanning](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning).
You can also use GitHub's tools to audit responses to security alerts. For more information, see [Auditing security alerts](https://docs.github.com/en/code-security/getting-started/auditing-security-alerts).
If you have a security vulnerability in a public repository, you can create a security advisory to privately discuss and fix the vulnerability. For more information, see [About repository security advisories](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/about-repository-security-advisories) and [Creating a repository security advisory](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/creating-a-repository-security-advisory).
If you use GitHub Actions, you can use GitHub's security features to increase the security of your workflows. For more information, see [Using GitHub's security features to secure your use of GitHub Actions](https://docs.github.com/en/actions/security-guides/using-githubs-security-features-to-secure-your-use-of-github-actions).
