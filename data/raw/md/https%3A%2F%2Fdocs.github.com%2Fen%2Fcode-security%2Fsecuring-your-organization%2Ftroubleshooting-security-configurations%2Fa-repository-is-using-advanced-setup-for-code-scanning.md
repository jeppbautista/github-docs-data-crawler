  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secure your organization](https://docs.github.com/en/code-security/securing-your-organization "Secure your organization")/
  * [Troubleshooting configurations](https://docs.github.com/en/code-security/securing-your-organization/troubleshooting-security-configurations "Troubleshooting configurations")/
  * [Active advanced setup](https://docs.github.com/en/code-security/securing-your-organization/troubleshooting-security-configurations/a-repository-is-using-advanced-setup-for-code-scanning "Active advanced setup")


# A repository is using advanced setup for code scanning
You cannot attach a security configuration with code scanning enabled to repositories that are using advanced setup for code scanning.
## Who can use this feature?
Organization owners, security managers, and organization members with the **admin** role
## In this article
  * [About the problem](https://docs.github.com/en/code-security/securing-your-organization/troubleshooting-security-configurations/a-repository-is-using-advanced-setup-for-code-scanning#about-the-problem)
  * [Solving the problem](https://docs.github.com/en/code-security/securing-your-organization/troubleshooting-security-configurations/a-repository-is-using-advanced-setup-for-code-scanning#solving-the-problem)


## [About the problem](https://docs.github.com/en/code-security/securing-your-organization/troubleshooting-security-configurations/a-repository-is-using-advanced-setup-for-code-scanning#about-the-problem)
You cannot successfully apply a security configuration with code scanning default setup enabled to a target repository that uses advanced setup for code scanning. Advanced setups are tailored to the specific security needs of their repositories, so they are not intended to be overridden at scale.
If you try to attach a security configuration with code scanning enabled to a repository already using advanced setup, security settings will be applied as follows:
  * **Code scanning default setup will not be enabled** , and advanced setup will continue to run as normal.
  * **All other security features enabled in the configuration will be enabled.**
  * **The security configuration will not be attached** to the repository, since only some features from the configuration are enabled.


For all repositories without an active advanced setup, the security configuration will be applied as expected, and code scanning default setup will be enabled.
If advanced setup is considered inactive for a repository, default setup _will_ still be enabled for that repository. Advanced setup is considered inactive for a repository if the repository meets any of the following criteria:
  * The latest CodeQL analysis is more than 90 days old
  * All CodeQL configurations have been deleted
  * The workflow file has been deleted or disabled (exclusively for YAML-based advanced setup)


## [Solving the problem](https://docs.github.com/en/code-security/securing-your-organization/troubleshooting-security-configurations/a-repository-is-using-advanced-setup-for-code-scanning#solving-the-problem)
There are two ways you can solve this problem:
  1. **Update the affected repositories to use default setup** for code scanning at the repository level and then reapply your security configuration to the repositories. For more information, see [Configuring default setup for code scanning](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning).
  2. **Create a new custom security configuration** that does not include a setting for code scanning and apply this security configuration to repositories that use advanced setup. For more information, see [Creating a custom security configuration](https://docs.github.com/en/code-security/securing-your-organization/enabling-security-features-in-your-organization/creating-a-custom-security-configuration).


