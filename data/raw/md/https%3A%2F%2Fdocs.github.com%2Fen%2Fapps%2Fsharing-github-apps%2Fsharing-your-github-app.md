  * [Apps](https://docs.github.com/en/apps "Apps")/
  * [Sharing GitHub Apps](https://docs.github.com/en/apps/sharing-github-apps "Sharing GitHub Apps")/
  * [Share your app](https://docs.github.com/en/apps/sharing-github-apps/sharing-your-github-app "Share your app")


# Sharing your GitHub App
You can share your GitHub App with other users.
## In this article
  * [Sharing your GitHub App on GitHub Marketplace](https://docs.github.com/en/apps/sharing-github-apps/sharing-your-github-app#sharing-your-github-app-on-github-marketplace)
  * [Sharing your GitHub App via an install link](https://docs.github.com/en/apps/sharing-github-apps/sharing-your-github-app#sharing-your-github-app-via-an-install-link)
  * [Sharing your GitHub App with GitHub Enterprise Server instances](https://docs.github.com/en/apps/sharing-github-apps/sharing-your-github-app#sharing-your-github-app-with-github-enterprise-server-instances)


## [Sharing your GitHub App on GitHub Marketplace](https://docs.github.com/en/apps/sharing-github-apps/sharing-your-github-app#sharing-your-github-app-on-github-marketplace)
If your GitHub App is public, you can choose to publish it to GitHub Marketplace. For more information, see [About GitHub Marketplace for apps](https://docs.github.com/en/apps/publishing-apps-to-github-marketplace/github-marketplace-overview/about-github-marketplace).
For more information about how users can install your app from GitHub Marketplace, see [Installing a GitHub App from GitHub Marketplace for your organizations](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-github-marketplace-for-your-organizations) and [Installing a GitHub App from GitHub Marketplace for your personal account](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-github-marketplace-for-your-personal-account).
## [Sharing your GitHub App via an install link](https://docs.github.com/en/apps/sharing-github-apps/sharing-your-github-app#sharing-your-github-app-via-an-install-link)
If your GitHub App is public, other users and organizations can install your app. For more information about making your app public, see [Making a GitHub App public or private](https://docs.github.com/en/apps/creating-github-apps/setting-up-a-github-app/making-a-github-app-public-or-private).
  1. In the upper-right corner of any page on GitHub, click your profile photo.
  2. Navigate to your account settings.
     * For an app owned by a personal account, click **Settings**.
     * For an app owned by an organization: 
       1. Click **Your organizations**.
       2. To the right of the organization, click **Settings**.
  3. In the left sidebar, click 
  4. In the left sidebar, click **GitHub Apps**.
  5. Next to the GitHub App that you want to share, click **Edit**.
  6. Click **Public page**. GitHub will bring you to the public page for your GitHub App.
  7. Click **Install**. GitHub will bring you to the installation URL for your GitHub App. The URL will look something like `https://github.com/apps/APP-NAME/installations/new`, where `APP-NAME` is the name of the GitHub App.
  8. Share the installation URL with other users. For more information about how users can install your app from this URL, see [Installing a GitHub App from a third party](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-a-third-party).
When you share the URL, you can include a `state` query parameter in the installation URL to preserve the state of the application page and return people back to that state after they install, authenticate, or accept updates to your GitHub App. For example, you could use the `state` to correlate an installation to a user or account.
To preserve a state, add it to the installation URL: `https://github.com/apps/<app name>/installations/new?state=AB12t`


## [Sharing your GitHub App with GitHub Enterprise Server instances](https://docs.github.com/en/apps/sharing-github-apps/sharing-your-github-app#sharing-your-github-app-with-github-enterprise-server-instances)
If you want to share your GitHub App with GitHub Enterprise Server instances that you are not part of, you need to take additional steps. For more information, see [Making your GitHub App available for GitHub Enterprise Server](https://docs.github.com/en/apps/creating-github-apps/setting-up-a-github-app/making-your-github-app-available-for-github-enterprise-server).
