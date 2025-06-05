  * [Codespaces](https://docs.github.com/en/codespaces "Codespaces")/
  * [Setting your user preferences](https://docs.github.com/en/codespaces/setting-your-user-preferences "Setting your user preferences")/
  * [Set the timeout](https://docs.github.com/en/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces "Set the timeout")


# Setting your timeout period for GitHub Codespaces
You can set your default timeout for GitHub Codespaces in your personal settings page.
## Tool navigation
  * [GitHub CLI](https://docs.github.com/en/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?tool=cli)
  * [Visual Studio Code](https://docs.github.com/en/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?tool=vscode)
  * [Web browser](https://docs.github.com/en/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?tool=webui)


## In this article
  * [About the idle timeout](https://docs.github.com/en/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces#about-the-idle-timeout)
  * [Setting your default timeout period](https://docs.github.com/en/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces#setting-your-default-timeout-period)
  * [Setting the timeout period for a codespace](https://docs.github.com/en/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces#setting-the-timeout-period-for-a-codespace)
  * [Setting a timeout period](https://docs.github.com/en/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces#setting-a-timeout-period)
  * [Further reading](https://docs.github.com/en/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces#further-reading)


## [About the idle timeout](https://docs.github.com/en/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces#about-the-idle-timeout)
A codespace will stop running after a period of inactivity. By default this period is 30 minutes, but you can specify a longer or shorter default timeout period in your personal settings on GitHub. The updated setting will apply to any new codespaces you create, or to existing codespaces the next time you start them. You can also specify a timeout when you use GitHub CLI to create a codespace.
Codespaces compute usage is billed for the duration for which a codespace is active. If you're not using a codespace but it remains running, and hasn't yet timed out, you are billed for the total time that the codespace was active, irrespective of whether you were using it. For more information, see [About billing for GitHub Codespaces](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#codespaces-pricing).
### [Inactivity defined](https://docs.github.com/en/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces#inactivity-defined)
In the context of the Codespaces idle timeout, inactivity is defined as the absence of activity indicative of a user's presence. Personal interaction with a codespace, such as typing or using the mouse, resets the idle timeout period. Terminal activity, either input or output, also resets the idle timeout period. For example, if you publish a web app on a port from a codespace and page requests generate output in a terminal on the codespace, then each time terminal output occurs the timeout will be reset. However, if you share a port, and then don't interact with the codespace, and no terminal output is generated, the codespace will time out after the configured period.
### [Timeout periods for organization-owned repositories](https://docs.github.com/en/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces#timeout-periods-for-organization-owned-repositories)
Organizations can set a maximum idle timeout policy for codespaces created from some or all of their repositories. If an organization policy sets a maximum timeout which is less than the default timeout you have set, the organization's timeout will be used instead of your setting. You will be notified of this after the codespace is created. For more information, see [Restricting the idle timeout period](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-idle-timeout-period).
## [Setting your default timeout period](https://docs.github.com/en/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces#setting-your-default-timeout-period)
  1. In the upper-right corner of any page on GitHub, click your profile photo, then click 
  2. In the "Code, planning, and automation" section of the sidebar, click 
  3. Under "Default idle timeout", enter the time that you want, then click **Save**. The time must be between 5 minutes and 240 minutes (4 hours).
![Screenshot of the "Default idle timeout" section of the Codespaces settings, with "90 minutes" entered.](https://docs.github.com/assets/cb-37553/images/help/codespaces/setting-default-timeout.png)


## [Setting the timeout period for a codespace](https://docs.github.com/en/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces#setting-the-timeout-period-for-a-codespace)
To learn more about GitHub CLI, see [About GitHub CLI](https://docs.github.com/en/github-cli/github-cli/about-github-cli).
To set the timeout period when you create a codespace, use the `idle-timeout` argument with the `codespace create` subcommand. Specify the time in minutes, followed by `m`. The time must be between 5 minutes and 240 minutes (4 hours).
```
gh codespace create --idle-timeout 90m

```

If you don't specify a timeout period when you create a codespace, then the default timeout period will be used. For information about setting a default timeout period, click the "Web browser" tab on this page. You can't currently specify a default timeout period through GitHub CLI.
## [Setting a timeout period](https://docs.github.com/en/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces#setting-a-timeout-period)
You can set your default timeout period in your web browser, on GitHub. Alternatively, if you use GitHub CLI to create a codespace you can set a timeout period for that particular codespace. For more information, click the appropriate tab above.
## [Further reading](https://docs.github.com/en/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces#further-reading)
  * [Customizing your codespace](https://docs.github.com/en/codespaces/customizing-your-codespace)
  * [Managing your codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces)


