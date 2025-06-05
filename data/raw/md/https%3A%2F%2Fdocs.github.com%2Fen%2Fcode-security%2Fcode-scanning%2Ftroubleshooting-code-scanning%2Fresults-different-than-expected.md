  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Troubleshooting code scanning](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning "Troubleshooting code scanning")/
  * [Results different than expected](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/results-different-than-expected "Results different than expected")


# Results are different than expected
If your code scanning results are different than you expected, you can check which configurations are active.
If your code scanning results are different than you expected, you may have both default and advanced setup configured for your repository. When you enable default setup, this disables the existing CodeQL workflow file and blocks any CodeQL API analysis from uploading results.
To check if default setup is enabled, navigate to the main page of the repository, then click 
If you want to return to using advanced setup and get code scanning results from your custom workflow file, click [Disabling and enabling a workflow](https://docs.github.com/en/actions/managing-workflow-runs/disabling-and-enabling-a-workflow) and [Configuring advanced setup for code scanning](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning).
In some cases, your repository may use multiple code scanning configurations. These configurations can generate duplicate alerts. Additionally, stale configurations that no longer run will display outdated alert statuses, and the stale alerts will stay open indefinitely. To avoid outdated alerts, you should remove stale code scanning configurations from a branch. For more information on multiple configurations and deleting stale configurations, see [About code scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts#about-alerts-from-multiple-configurations) and [Resolving code scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/resolving-code-scanning-alerts#removing-stale-configurations-and-alerts-from-a-branch).
