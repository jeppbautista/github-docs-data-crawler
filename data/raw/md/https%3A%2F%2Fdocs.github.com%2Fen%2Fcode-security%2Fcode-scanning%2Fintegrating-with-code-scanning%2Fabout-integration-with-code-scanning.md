  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Integrate with code scanning](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning "Integrate with code scanning")/
  * [About integration](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/about-integration-with-code-scanning "About integration")


# About integration with code scanning
You can perform code scanning externally and then display the results in GitHub, or configure webhooks that listen to code scanning activity in your repository.
## Who can use this feature?
Code scanning is available for the following repository types:
  * Public repositories on GitHub.com
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [About integration with code scanning](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/about-integration-with-code-scanning#about-integration-with-code-scanning)
  * [Integrations with webhooks](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/about-integration-with-code-scanning#integrations-with-webhooks)
  * [Further reading](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/about-integration-with-code-scanning#further-reading)


## [About integration with code scanning](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/about-integration-with-code-scanning#about-integration-with-code-scanning)
As an alternative to running code scanning within GitHub, you can perform analysis elsewhere, using the CodeQL CLI or another static analysis tool, and then upload the results. For more information, see [Using code scanning with your existing CI system](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/using-code-scanning-with-your-existing-ci-system).
If you run code scanning using multiple configurations, an alert will sometimes have multiple analysis origins. If an alert has multiple analysis origins, you can view the status of the alert for each analysis origin on the alert page. For more information, see [About code scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts#about-analysis-origins).
## [Integrations with webhooks](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/about-integration-with-code-scanning#integrations-with-webhooks)
You can use code scanning webhooks to build or configure integrations, such as [GitHub Apps](https://docs.github.com/en/apps/creating-github-apps/setting-up-a-github-app) or [OAuth apps](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps), that subscribe to code scanning events in your repository. For example, you could build an integration that creates an issue on GitHub or sends you a Slack notification when a new code scanning alert is added in your repository. For more information, see [Webhooks documentation](https://docs.github.com/en/webhooks) and [Webhook events and payloads](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#code_scanning_alert).
## [Further reading](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/about-integration-with-code-scanning#further-reading)
  * [About code scanning](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning)
  * [Using code scanning with your existing CI system](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/using-code-scanning-with-your-existing-ci-system)
  * [SARIF support for code scanning](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/sarif-support-for-code-scanning)


