  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Troubleshooting code scanning](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning "Troubleshooting code scanning")/
  * [Enabling default setup takes too long](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/enabling-default-setup-takes-too-long "Enabling default setup takes too long")


# Enabling default setup takes too long
If you think that enabling default setup has stalled, you can restart the process.
When you enable default setup, a workflow is triggered with the automatically generated configuration. This run is used to test whether default setup works for all CodeQL-supported languages in the repository.
You can check on the progress of the test run for default setup on the **Actions** tab. If the run is taking too long, try canceling the workflow run and restarting the configuration process.
To restart your configuration, navigate to the main page of your repository, then click **CodeQL** workflow run that's in progress, then click **Cancel workflow**. Once **Advanced Security** settings and re-enable default setup. If default setup continues to stall, please contact us through the [GitHub Support portal](https://support.github.com) or try enabling advanced setup. For more information, see [Configuring advanced setup for code scanning](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning).
