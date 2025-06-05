  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Security](https://docs.github.com/en/actions/security-for-github-actions "Security")/
  * [Security guides](https://docs.github.com/en/actions/security-for-github-actions/security-guides "Security guides")/
  * [GitHub security features](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-githubs-security-features-to-secure-your-use-of-github-actions "GitHub security features")


# Using GitHub's security features to secure your use of GitHub Actions
GitHub has several security features that can enhance the security of the actions you consume and publish.
## In this article
  * [About GitHub's security features](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-githubs-security-features-to-secure-your-use-of-github-actions#about-githubs-security-features)
  * [Understanding dependencies in your workflows](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-githubs-security-features-to-secure-your-use-of-github-actions#understanding-dependencies-in-your-workflows)
  * [Being aware of security vulnerabilities in actions you use](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-githubs-security-features-to-secure-your-use-of-github-actions#being-aware-of-security-vulnerabilities-in-actions-you-use)
  * [Keeping the actions in your workflows secure and up to date](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-githubs-security-features-to-secure-your-use-of-github-actions#keeping-the-actions-in-your-workflows-secure-and-up-to-date)
  * [Protecting actions you've created](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-githubs-security-features-to-secure-your-use-of-github-actions#protecting-actions-youve-created)


## [About GitHub's security features](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-githubs-security-features-to-secure-your-use-of-github-actions#about-githubs-security-features)
GitHub provides many features to make your code more secure. You can use GitHub's built-in features to understand the actions your workflows depend on, ensure you are notified about vulnerabilities in the actions you consume, or automate the process of keeping the actions in your workflows up to date. If you publish and maintain actions, you can use GitHub to communicate with your community about vulnerabilities and how to fix them. For more information about security features that GitHub offers, see [GitHub security features](https://docs.github.com/en/code-security/getting-started/github-security-features#about-githubs-security-features).
This article will explain how you can use some of GitHub's security features to increase the security of your use of GitHub Actions.
## [Understanding dependencies in your workflows](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-githubs-security-features-to-secure-your-use-of-github-actions#understanding-dependencies-in-your-workflows)
You can use the dependency graph to explore the actions that the workflows in your repository use. The dependency graph is a summary of the manifest and lock files stored in a repository. It also recognizes files in `./github/workflows/` as manifests, which means that any actions or workflows referenced using the syntax `jobs[*].steps[*].uses` or `jobs.<job_id>.uses` will be parsed as dependencies.
The dependency graph shows the following information about actions used in workflows:
  * The account or organization that owns the action.
  * The workflow file that references the action.
  * The version or SHA the action is pinned to.


In the dependency graph, dependencies are automatically sorted by vulnerability severity. If any of the actions you use have security advisories, they will display at the top of the list. You can navigate to the advisory from the dependency graph and access instructions for resolving the vulnerability.
The dependency graph is enabled for public repositories, and you can choose to enable it on private repositories. For more information about using the dependency graph, see [Exploring the dependencies of a repository](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exploring-the-dependencies-of-a-repository).
## [Being aware of security vulnerabilities in actions you use](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-githubs-security-features-to-secure-your-use-of-github-actions#being-aware-of-security-vulnerabilities-in-actions-you-use)
For actions available on the marketplace, GitHub reviews related security advisories and then adds those advisories to the GitHub Advisory Database. You can search the database for actions that you use to find information about existing vulnerabilities and instructions for how to fix them. To streamline your search, use the GitHub Actions filter in the [GitHub Advisory Database](https://github.com/advisories?query=type%3Areviewed+ecosystem%3Aactions).
You can set up your repositories so that you:
  * Receive alerts when actions used in your workflows receive a vulnerability report. For more information, see [Monitoring the actions in your workflows](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-githubs-security-features-to-secure-your-use-of-github-actions#monitoring-the-actions-in-your-workflows).
  * Are warned about existing advisories when you add or update an action in a workflow. For more information, see [Screening actions for vulnerabilities in new or updated workflows](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-githubs-security-features-to-secure-your-use-of-github-actions#screening-actions-for-vulnerabilities-in-new-or-updated-workflows).


### [Monitoring the actions in your workflows](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-githubs-security-features-to-secure-your-use-of-github-actions#monitoring-the-actions-in-your-workflows)
You can use Dependabot to monitor the actions in your workflows and enable Dependabot alerts to notify you when an action you use has a reported vulnerability. Dependabot performs a scan of the default branch of the repositories where it is enabled to detect insecure dependencies. Dependabot generates Dependabot alerts when a new advisory is added to the GitHub Advisory Database or when an action you use is updated.
Dependabot only creates alerts for vulnerable actions that use semantic versioning and will not create alerts for actions pinned to SHA values.
You can enable Dependabot alerts for your personal account, for a repository, or for an organization. For more information, see [Configuring Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/configuring-dependabot-alerts).
You can view all open and closed Dependabot alerts and corresponding Dependabot security updates in your repository's Dependabot alerts tab. For more information, see [Viewing and updating Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/viewing-and-updating-dependabot-alerts).
### [Screening actions for vulnerabilities in new or updated workflows](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-githubs-security-features-to-secure-your-use-of-github-actions#screening-actions-for-vulnerabilities-in-new-or-updated-workflows)
When you open pull requests to update your workflows, it is good practice to use dependency review to understand the security impact of changes you've made to the actions you use. Dependency review helps you understand dependency changes and the security impact of these changes at every pull request. It provides an easily understandable visualization of dependency changes with a rich diff on the "Files Changed" tab of a pull request. Dependency review informs you of:
  * Which dependencies were added, removed, or updated, along with the release dates
  * How many projects use these components
  * Vulnerability data for these dependencies


If any of the changes you made to your workflows are flagged as vulnerable, you can avoid adding them to your project or update them to a secure version.
For more information about dependency review, see [About dependency review](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review).
The "dependency review action" refers to the specific action that can report on differences in a pull request within the GitHub Actions context. See [`dependency-review-action`](https://github.com/actions/dependency-review-action). You can use the dependency review action in your repository to enforce dependency reviews on your pull requests. The action scans for vulnerable versions of dependencies introduced by package version changes in pull requests, and warns you about the associated security vulnerabilities. This gives you better visibility of what's changing in a pull request, and helps prevent vulnerabilities being added to your repository. For more information, see [About dependency review](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review#about-the-dependency-review-action).
## [Keeping the actions in your workflows secure and up to date](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-githubs-security-features-to-secure-your-use-of-github-actions#keeping-the-actions-in-your-workflows-secure-and-up-to-date)
You can use Dependabot to ensure that references to actions and reusable workflows used in your repository are kept up to date. Actions are often updated with bug fixes and new features to make automated processes faster, safer, and more reliable. Dependabot takes the effort out of maintaining your dependencies as it does this automatically for you. For more information, see [Keeping your actions up to date with Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/keeping-your-actions-up-to-date-with-dependabot) and [About Dependabot security updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates).
The following features can automatically update the actions in your workflows.
  * **Dependabot version updates** open pull requests to update actions to the latest version when a new version is released.
  * **Dependabot security updates** open pull requests to update actions with reported vulnerabilities to the minimum patched version.


  * Dependabot only supports updates to GitHub Actions using the GitHub repository syntax, such as `actions/checkout@v4`. Dependabot will ignore actions or reusable workflows referenced locally (for example, `./.github/actions/foo.yml`).
  * Docker Hub and GitHub Packages Container registry URLs are currently not supported. For example, references to Docker container actions using `docker://` syntax aren't supported.
  * Dependabot supports both public and private repositories for GitHub Actions. For private registry configuration options, see "`git`" in [Dependabot options reference](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuration-options-for-the-dependabot.yml-file#git).


For information on how to configure Dependabot version updates, see [Configuring Dependabot version updates](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuring-dependabot-version-updates).
For information on how to configure Dependabot security updates, see [Configuring Dependabot security updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates).
## [Protecting actions you've created](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-githubs-security-features-to-secure-your-use-of-github-actions#protecting-actions-youve-created)
GitHub enables collaboration between people who publish and maintain actions and vulnerability reporters in order to promote secure coding. Repository security advisories allow maintainers of public repositories to privately discuss and fix a security vulnerability in a project. After collaborating on a fix, repository maintainers can publish the security advisory to publicly disclose the security vulnerability to the project's community. By publishing security advisories, repository maintainers make it easier for their community to update package dependencies and research the impact of the security vulnerabilities.
If you are someone who maintains an action that is used in other projects, you can use the following GitHub features to enhance the security of the actions you've published.
  * Use the dependants view in the Dependency graph to see which projects depend on your code. If you receive a vulnerability report, this will give you an idea of who you need to communicate with about the vulnerability and how to fix it. For more information, see [Exploring the dependencies of a repository](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exploring-the-dependencies-of-a-repository#dependents-view).
  * Use repository security advisories to create a security advisory, privately collaborate to fix the vulnerability in a temporary private fork, and publish a security advisory to alert your community of the vulnerability once a patch is released. For more information, see [Configuring private vulnerability reporting for a repository](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/configuring-private-vulnerability-reporting-for-a-repository) and [Creating a repository security advisory](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/creating-a-repository-security-advisory).


