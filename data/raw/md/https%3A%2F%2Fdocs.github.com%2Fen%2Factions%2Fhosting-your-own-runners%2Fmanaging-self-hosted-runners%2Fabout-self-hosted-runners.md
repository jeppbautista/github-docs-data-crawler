  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners "Self-hosted runners")/
  * [Manage self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners "Manage self-hosted runners")/
  * [About self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners "About self-hosted runners")


# About self-hosted runners
You can host your own runners and customize the environment used to run jobs in your GitHub Actions workflows.
## In this article
  * [About self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners#about-self-hosted-runners)
  * [Further reading](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners#further-reading)


## [About self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners#about-self-hosted-runners)
A self-hosted runner is a system that you deploy and manage to execute jobs from GitHub Actions on GitHub.
Self-hosted runners:
  * Give you more control of hardware, operating system, and software tools than GitHub-hosted runners provide.
  * Are free to use with GitHub Actions, but you are responsible for the cost of maintaining your runner machines.
  * Let you create custom hardware configurations that meet your needs with processing power or memory to run larger jobs, install software available on your local network.
  * Receive automatic updates for the self-hosted runner application only, though you may disable automatic updates of the runner.
  * Can use cloud services or local machines that you already pay for.
  * Don't need to have a clean instance for every job execution.
  * Can be physical, virtual, in a container, on-premises, or in a cloud.


You can use self-hosted runners anywhere in the management hierarchy. Repository-level runners are dedicated to a single repository, while organization-level runners can process jobs for multiple repositories in an organization. Organization owners can choose which repositories are allowed to create repository-level self-hosted runners. See [Disabling or limiting GitHub Actions for your organization](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#limiting-the-use-of-self-hosted-runners). Finally, enterprise-level runners can be assigned to multiple organizations in an enterprise account.
### [Requirements for self-hosted runner machines](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners#requirements-for-self-hosted-runner-machines)
You can use any machine as a self-hosted runner as long at it meets these requirements:
  * You can install and run the self-hosted runner application on the machine.
  * The machine can communicate with GitHub Actions.
  * The machine has enough hardware resources for the type of workflows you plan to run. The self-hosted runner application itself only requires minimal resources.
  * If you want to run workflows that use Docker container actions or service containers, you must use a Linux machine and Docker must be installed.


## [Further reading](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners#further-reading)
  * [Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions)
  * [Adding self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/adding-self-hosted-runners)
  * [Using self-hosted runners in a workflow](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/using-self-hosted-runners-in-a-workflow)
  * [Autoscaling with self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/autoscaling-with-self-hosted-runners)
  * [Supported architectures and operating systems for self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/supported-architectures-and-operating-systems-for-self-hosted-runners)
  * [Communicating with self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/communicating-with-self-hosted-runners)


