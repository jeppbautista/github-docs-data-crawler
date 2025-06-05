  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Manage code scanning](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration "Manage code scanning")/
  * [Configure larger runners](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/configuring-larger-runners-for-default-setup "Configure larger runners")


# Configuring larger runners for default setup
You can run code scanning default setup more quickly on bigger codebases using larger runners.
## Who can use this feature?
Larger runners are only available for organizations and enterprises using the GitHub Team or GitHub Enterprise Cloud plans.
## In this article
  * [About larger runners for default setup](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/configuring-larger-runners-for-default-setup#about-larger-runners-for-default-setup)
  * [Provisioning organization-level larger runners for default setup](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/configuring-larger-runners-for-default-setup#provisioning-organization-level-larger-runners-for-default-setup)


Support for larger runners for code scanning default setup is currently in public preview and subject to change.
## [About larger runners for default setup](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/configuring-larger-runners-for-default-setup#about-larger-runners-for-default-setup)
Customers on GitHub Team and GitHub Enterprise Cloud plans can choose from a range of managed virtual machines that have more resources than the [standard GitHub-hosted runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners#supported-runners-and-hardware-resources). These machines are referred to as "larger runner." They offer the following advanced features:
  * More RAM, CPU, and disk space
  * Static IP addresses
  * Azure private networking
  * The ability to group runners
  * Autoscaling to support concurrent workflows
  * GPU-powered runners


These larger runners are hosted by GitHub and have the runner application and other tools preinstalled. For more information about larger runners, see [About larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-larger-runners/about-larger-runners).
Consider configuring larger runners for default setup if:
  * Your scans with standard GitHub-hosted runners are taking too long.
  * Your scans with standard GitHub-hosted runners are returning memory or disk errors.
  * You want to customize aspects of your code scanning runner like the runner size, runner image, and job concurrency without using self-hosted runners.


Currently, Swift analysis is not available on larger runners for default setup. Additionally, if your repository has access to a runner with the `code-scanning` label, such as a larger runner provisioned for default setup, default setup workflows will _only_ use runners labeled `code-scanning`. If you would like to configure default setup on larger runners _and_ analyze Swift, you have two options:
  * Provision a self-hosted macOS runner with the `code-scanning` label in addition to your larger runner. For more information, see [Adding self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/adding-self-hosted-runners#adding-a-self-hosted-runner-to-a-repository).
  * Ensure any repositories containing Swift _do not_ have access to runners with the label `code-scanning`. Default setup workflows for that repository will only use standard runners.


## [Provisioning organization-level larger runners for default setup](https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/configuring-larger-runners-for-default-setup#provisioning-organization-level-larger-runners-for-default-setup)
  1. Add a larger runner to your organization. See [Managing larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-larger-runners/managing-larger-runners#adding-a-larger-runner-to-an-organization). 
     * To add a custom label to your larger runner, give the runner a name that matches that label. You can use this custom label when you configure default setup with larger runners. For more information, see [Configuring default setup for code scanning](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning#assigning-labels-to-runners).
  2. By default, all repositories in your organization have access to organization-level runners, meaning every repository can use your larger runner. For information on granting only select repositories access to a larger runner, see [Managing larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-larger-runners/managing-larger-runners#allowing-repositories-to-access-larger-runners).
  3. You can now configure default setup for your organization and repositories, and your larger runner will automatically pick up code scanning jobs. For more information on configuring default setup, see [Configuring default setup for code scanning](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning) and [Configuring default setup for code scanning at scale](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning-at-scale).


