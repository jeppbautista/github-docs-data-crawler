  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secret scanning](https://docs.github.com/en/code-security/secret-scanning "Secret scanning")/
  * [Advanced features](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features "Advanced features")/
  * [Delegated bypass](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection "Delegated bypass")/
  * [About delegated bypass](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/about-delegated-bypass-for-push-protection "About delegated bypass")


# About delegated bypass for push protection
You can control which teams or roles have the ability to bypass push protection in your organization or repository.
## Who can use this feature?
Delegated bypass for push protection is available for the following repository types:
  * Organization-owned repositories on GitHub Team with [GitHub Secret Protection](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [About delegated bypass for push protection](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/about-delegated-bypass-for-push-protection#about-delegated-bypass-for-push-protection)
  * [Next steps](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/about-delegated-bypass-for-push-protection#next-steps)


## [About delegated bypass for push protection](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/about-delegated-bypass-for-push-protection#about-delegated-bypass-for-push-protection)
By default, when push protection is enabled for a repository, anyone with write access can still push a secret to the repository, provided that they specify a reason for bypassing push protection.
With delegated bypass for push protection, you can:
  * **Choose** which individuals, roles, and teams can bypass push protection.
  * Introduce a **review and approval** cycle for pushes containing secrets from all other contributors.


Delegated bypass applies to files created, edited, and uploaded on GitHub.
To set up delegated bypass, organization owners or repository administrators create a list of users with bypass privileges. This designated list of users can then:
  * Bypass push protection, by specifying a reason for bypassing the block.
  * Manage (approve or deny) bypass requests coming from all other contributors. These requests are located in the "Push protection bypass" page in the **Security** tab of the repository.


The following types of users can always bypass push protection without having to request bypass privileges:
  * Organization owners
  * Security managers
  * Users in teams, default roles, or custom roles that have been added to the bypass list.
  * Users who are assigned (either directly or via a team) a custom role with the "review and manage secret scanning bypass requests" fine-grained permission.


## [Next steps](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/about-delegated-bypass-for-push-protection#next-steps)
  * [Enabling delegated bypass for push protection](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/enabling-delegated-bypass-for-push-protection)
  * [Managing requests to bypass push protection](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/managing-requests-to-bypass-push-protection)


