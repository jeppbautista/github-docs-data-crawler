  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Enable code scanning](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning "Enable code scanning")/
  * [Configure code scanning](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning "Configure code scanning")


# Configuring default setup for code scanning
Quickly set up code scanning to find and fix vulnerable code automatically.
## Who can use this feature?
Repository owners, organization owners, security managers, and users with the **admin** role
Code scanning is available for the following repository types:
  * Public repositories on GitHub.com
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [About default setup](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning#about-default-setup)
  * [Configuring default setup for a repository](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning#configuring-default-setup-for-a-repository)
  * [Assigning labels to runners](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning#assigning-labels-to-runners)
  * [Next steps](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning#next-steps)


## [About default setup](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning#about-default-setup)
Default setup for code scanning is the quickest, easiest, most low-maintenance way to enable code scanning for your repository. Based on the code in your repository, default setup will automatically create a custom code scanning configuration. After enabling default setup, the code written in CodeQL-supported languages in your repository will be scanned:
  * On each push to the repository's default branch, or any protected branch. For more information on protected branches, see [About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
  * When creating or committing to a pull request based against the repository's default branch, or any protected branch, excluding pull requests from forks.
  * On a weekly schedule.


If no pushes and pull requests have occurred in a repository with default setup enabled for 6 months, the weekly schedule will be disabled to save your GitHub Actions minutes.
You can also enable default setup for multiple or all repositories in an organization at the same time. For information on bulk enablement, see [Configuring default setup for code scanning at scale](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning-at-scale).
If you need more granular control over your code scanning configuration, you should instead configure advanced setup. For more information, see [Configuring advanced setup for code scanning](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning).
### [Requirements for using default setup](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning#requirements-for-using-default-setup)
Your repository is eligible for default setup for code scanning if:
  * GitHub Actions are enabled.
  * It is publicly visible, or GitHub Code Security is enabled.


We recommend enabling default setup for eligible repositories if there is any chance the repositories will include at least one CodeQL-supported language in the future. If you enable default setup on a repository that does not include any CodeQL-supported languages, default setup will not run any scans or use any GitHub Actions minutes. If CodeQL-supported languages are added to the repository's default branch, default setup will automatically begin scanning CodeQL-supported languages and using GitHub Actions minutes. For more information on CodeQL-supported languages, see [About code scanning with CodeQL](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql#about-codeql).
You can use default setup for all CodeQL-supported languages for self-hosted runners or GitHub-hosted runners. See [Assigning labels to runners](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning#assigning-labels-to-runners), later in this article.
Default setup uses the `none` build mode for C# and Java and uses the `autobuild` build mode for other compiled languages. You should configure your self-hosted runners to make sure they can run all the necessary commands for C/C++, C#, and Swift analysis. Analysis of JavaScript/TypeScript, Go, Ruby, Python, and Kotlin code does not currently require special configuration.
### [Customizing default setup](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning#customizing-default-setup)
We recommend that you start using code scanning with default setup. After you've initially configured default setup, you can evaluate code scanning to see how it's working for you. If you find that something isn't working as you expect, you can customize default setup to better meet your needs. For more information, see [Evaluating default setup for code scanning](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/evaluating-default-setup-for-code-scanning).
### [About adding non-compiled and compiled languages to your default setup](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning#about-adding-non-compiled-and-compiled-languages-to-your-default-setup)
If the code in a repository changes to include Go, JavaScript/TypeScript, Python, or Ruby, GitHub will automatically update the code scanning configuration to include the new language. If code scanning fails with the new configuration, GitHub will resume the previous configuration automatically so the repository does not lose code scanning coverage.
Compiled languages are not automatically included in default setup configuration because they often require more advanced configuration, but you can manually select any CodeQL-supported compiled language for analysis.
## [Configuring default setup for a repository](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning#configuring-default-setup-for-a-repository)
If the analyses fail for all CodeQL-supported languages in a repository, default setup will still be enabled, but it will not run any scans or use any GitHub Actions minutes until another CodeQL-supported language is added to the repository or default setup is manually reconfigured, and the analysis of a CodeQL-supported language succeeds.
  1. On GitHub, navigate to the main page of the repository.
If you are configuring default setup on a fork, you must first enable GitHub Actions. To enable GitHub Actions, under your repository name, click **I understand my workflows, go ahead and enable them**. Be aware that this will enable all existing workflows on your fork.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Security" section of the sidebar, click 
  4. To the right of "Code Security", click **Enable**.
  5. Under "Code Security", to the right of "CodeQL analysis", select **Set up** **Default**.
![Screenshot of the "Code Security" section of "Advanced Security" settings. The "Default setup" button is highlighted with an orange outline.](https://docs.github.com/assets/cb-92392/images/help/security/default-code-scanning-setup.png)
You will then see a "CodeQL default configuration" dialog summarizing the code scanning configuration automatically created by default setup.
If your repository contains _only_ compiled CodeQL-supported languages (for example, Java), you will be taken to the settings page to select the languages you want to add to your default setup configuration.
  6. Optionally, to customize your code scanning setup, click 
     * To add or remove a language from the analysis performed by default setup, select or deselect that language in the "Languages" section. If you would like to analyze a CodeQL-supported compiled language with default setup, select that language here.
     * To specify the CodeQL query suite you would like to use, select your preferred query suite in the "Query suites" section.
  7. Review the settings for default setup on your repository, then click **Enable CodeQL**. This will trigger a workflow that tests the new, automatically generated configuration.
If you are switching to default setup from advanced setup, you will see a warning informing you that default setup will override existing code scanning configurations. This warning means default setup will disable the existing workflow file and block any CodeQL analysis API uploads.
  8. Optionally, to view your default setup configuration after enablement, select 


## [Assigning labels to runners](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning#assigning-labels-to-runners)
Code scanning sees assigned runners when default setup is enabled. If a runner is assigned to a repository that is already running default setup, you must disable and re-enable default setup to start using the runner. If you add a runner and want to start using it, you can change the configuration manually without needing to disable and re-enable default setup.
You can also assign self-hosted runners with the default `code-scanning` label, or you can optionally give them custom labels so that individual repositories can use different runners. For information about assigning labels to self-hosted runners, see [Using labels with self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/using-labels-with-self-hosted-runners).
Specifying custom labels for self-hosted runners is optional. Unless you have a specific use case, we recommend that you only assign runners with the default `code-scanning` label. For example, you may want to:
  * Assign more powerful self-hosted runners to critical repositories for faster code scanning analysis.
  * Run your code scanning analyses on a particular platform (for example, macOS).
  * Have granular control over the workload for your GitHub-hosted runners and self-hosted runners.


Once you've assigned custom labels to self-hosted runners, your repositories can use those runners for code scanning default setup. For more information, see [Configuring default setup for a repository](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning#configuring-default-setup-for-a-repository), earlier in this article.
You can also use security configurations to assign labels to self-hosted runners for code scanning. See [Creating a custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/meeting-your-specific-security-needs-with-custom-security-configurations/creating-a-custom-security-configuration#creating-a-custom-security-configuration).
### [Assigning larger runners](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning#assigning-larger-runners)
To assign a larger runner, name the runner `code-scanning`. This will automatically add the `code-scanning` label to the larger runner. An organization can only have one larger runner with the `code-scanning` label, and that runner will handle all code scanning jobs from repositories within your organization with access to the runner's group. See [Configuring larger runners for default setup](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/configuring-larger-runners-for-default-setup#provisioning-organization-level-larger-runners-for-default-setup).
## [Next steps](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning#next-steps)
After your configuration runs successfully at least once, you can start examining and resolving code scanning alerts. For more information on code scanning alerts, see [About code scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts) and [Assessing code scanning alerts for your repository](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository).
After you've configured default setup for code scanning, you can read about evaluating how it's working for you and the next steps you can take to customize it. For more information, see [Evaluating default setup for code scanning](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/evaluating-default-setup-for-code-scanning).
You can find detailed information about your code scanning configuration, including timestamps for each scan and the percentage of files scanned, on the tool status page. For more information, see [About the tool status page for code scanning](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/about-the-tool-status-page).
When you configure default setup, you may encounter an error. For information on troubleshooting specific errors, see [Troubleshooting code scanning](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning).
