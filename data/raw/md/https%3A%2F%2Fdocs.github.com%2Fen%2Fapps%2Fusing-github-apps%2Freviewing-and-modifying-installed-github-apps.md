  * [Apps](https://docs.github.com/en/apps "Apps")/
  * [Using GitHub Apps](https://docs.github.com/en/apps/using-github-apps "Using GitHub Apps")/
  * [Review installations](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps "Review installations")


# Reviewing and modifying installed GitHub Apps
You can review the permissions and change the repository access for GitHub Apps that you have installed. You can also temporarily or permanently prevent a GitHub App from accessing resources owned by your account or organization.
## In this article
  * [About installed GitHub Apps](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps#about-installed-github-apps)
  * [Navigating to the GitHub App you want to review or modify](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps#navigating-to-the-github-app-you-want-to-review-or-modify)
  * [Reviewing permissions](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps#reviewing-permissions)
  * [Modifying repository access](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps#modifying-repository-access)
  * [Blocking access](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps#blocking-access)
  * [Further reading](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps#further-reading)


## [About installed GitHub Apps](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps#about-installed-github-apps)
GitHub users can install GitHub Apps on their personal account or organizations. When you install a GitHub App, you grant the app the organization-level and repository-level permissions that it requested. You also specify which repositories the GitHub App can access.
You should periodically review the GitHub Apps that you have installed. You can review the permissions that you granted and change the repositories that the GitHub App can access. If you no longer use an app, consider suspending or deleting the GitHub App to block its access to resources owned by the account where it is installed.
In addition to reviewing GitHub Apps that you have installed, you can review GitHub Apps that you have authorized to act on your behalf. For more information, see [Reviewing and revoking authorization of GitHub Apps](https://docs.github.com/en/apps/using-github-apps/reviewing-and-revoking-authorization-of-github-apps).
## [Navigating to the GitHub App you want to review or modify](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps#navigating-to-the-github-app-you-want-to-review-or-modify)
  * For a GitHub App installed on an organization:
    1. In the top right corner of GitHub, click your profile photo, then click **Your organizations**.
    2. Next to your organization name, click **Settings**.
    3. In the side bar, under "Third-party Access," click **GitHub Apps**. A list of the GitHub Apps installed on your organization will be displayed.
    4. Next to the GitHub App you want to review or modify, click **Configure**.
  * For a GitHub App installed on your personal account:
    1. In the upper-right corner of any page, click your profile photo, then click **Settings**.
    2. Under "Integrations," click **Applications**.
    3. Click **Installed GitHub Apps**. A list of the GitHub Apps installed on your personal account will be displayed.
    4. Next to the GitHub App you want to review or modify, click **Configure**.
  * For a repository where a GitHub App was granted access:
In the following steps, you will be taken to the account settings for the organization or personal account where the GitHub App is installed. The settings will affect all repositories where the app is installed under that account, not just the repository where you navigated from.
    1. Navigate to the main page of the organization or repository.
    2. Click 
    3. Under "Integrations," click **GitHub Apps**. A list of the GitHub Apps that have been granted access to your repository will be displayed.
    4. Next to the GitHub App you want to review or modify, click **Configure**.


## [Reviewing permissions](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps#reviewing-permissions)
  1. Navigate to the GitHub App you want to modify. For more information, see [Navigating to the GitHub App you want to review or modify](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps#navigating-to-the-github-app-you-want-to-review-or-modify).
  2. Under "Permissions," review the permissions that the GitHub App has. For more information about what different permissions enable a GitHub App to do, see [Choosing permissions for a GitHub App](https://docs.github.com/en/apps/creating-github-apps/setting-up-a-github-app/choosing-permissions-for-a-github-app).


## [Modifying repository access](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps#modifying-repository-access)
  1. Navigate to the GitHub App you want to modify. For more information, see [Navigating to the GitHub App you want to review or modify](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps#navigating-to-the-github-app-you-want-to-review-or-modify).
  2. Under "Repository access," select **All repositories** or **Only select repositories**.
  3. If you selected **Only select repositories** in the previous step, under the **Select repositories** dropdown, select the repositories that you want the GitHub App to access.
If the GitHub App creates any repositories later, the app will automatically be granted access to those repositories as well.
  4. Click **Save**.


## [Blocking access](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps#blocking-access)
  1. Navigate to the GitHub App you want to modify. For more information, see [Navigating to the GitHub App you want to review or modify](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps#navigating-to-the-github-app-you-want-to-review-or-modify).
  2. To keep the GitHub App installed for future use but temporarily block it from accessing resources owned by your account, click **Suspend**.
When you suspend a GitHub App, your authorization of the app (if the app is installed on your personal account) or the authorization of the app by members of your organization (if the app is installed on an organization) will not be affected. For more information, see [Authorizing GitHub Apps](https://docs.github.com/en/apps/using-github-apps/authorizing-github-apps).
If the GitHub App was previously suspended, you can unsuspend the app by clicking **Unsuspend**. If the GitHub App was suspended by the GitHub App owner, then you cannot unsuspend the app.
  3. To uninstall a GitHub App and block it from accessing resources owned by your account, click **Uninstall**.
When you uninstall a GitHub App from an account, the app will lose access to the resources in that account. The app might still be authorized to access organizations on your behalf, if it has installations in those organizations.
If you want to stop an app from acting on your behalf anywhere on GitHub, also de-authorize the app in the "Authorized GitHub Apps" tab of your user account. This will fully deactivate any tokens issued to the app on your behalf. For more information, see [Authorizing GitHub Apps](https://docs.github.com/en/apps/using-github-apps/authorizing-github-apps).


## [Further reading](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps#further-reading)
  * [Reviewing and revoking authorization of GitHub Apps](https://docs.github.com/en/apps/using-github-apps/reviewing-and-revoking-authorization-of-github-apps)
  * [Privileged GitHub Apps](https://docs.github.com/en/apps/using-github-apps/privileged-github-apps)


