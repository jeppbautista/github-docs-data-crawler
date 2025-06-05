  * [Apps](https://docs.github.com/en/apps "Apps")/
  * [Using GitHub Apps](https://docs.github.com/en/apps/using-github-apps "Using GitHub Apps")/
  * [Install from Marketplace for org](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-github-marketplace-for-your-organizations "Install from Marketplace for org")


# Installing a GitHub App from GitHub Marketplace for your organizations
You can install GitHub Apps from GitHub Marketplace to use on your organizations.
## In this article
  * [About GitHub Marketplace](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-github-marketplace-for-your-organizations#about-github-marketplace)
  * [About installing GitHub Apps](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-github-marketplace-for-your-organizations#about-installing-github-apps)
  * [Requirements to install a GitHub App on an organization](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-github-marketplace-for-your-organizations#requirements-to-install-a-github-app-on-an-organization)
  * [Installing a GitHub App in your organization](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-github-marketplace-for-your-organizations#installing-a-github-app-in-your-organization)
  * [Further reading](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-github-marketplace-for-your-organizations#further-reading)


## [About GitHub Marketplace](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-github-marketplace-for-your-organizations#about-github-marketplace)
This article applies to installing and purchasing GitHub Apps from GitHub Marketplace. For more information on installing GitHub Apps from a source other than GitHub Marketplace, see [Installing a GitHub App from a third party](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-a-third-party).
If you install a GitHub App on your organization account and you choose a paid plan, you will pay for your app subscription on your organization's current billing date using your organization's existing payment method.
If you choose a paid plan with a free trial, you can cancel at any time during your trial period without being charged, but you will automatically lose access to the app. Your paid subscription will start at the end of the 14-day trial. For more information, see [About billing for GitHub Marketplace](https://docs.github.com/en/billing/managing-billing-for-github-marketplace-apps/about-billing-for-github-marketplace).
For more information about installing an OAuth app instead of a GitHub App from GitHub Marketplace, see [Installing an OAuth app in your organization](https://docs.github.com/en/apps/oauth-apps/using-oauth-apps/installing-an-oauth-app-in-your-organization).
## [About installing GitHub Apps](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-github-marketplace-for-your-organizations#about-installing-github-apps)
In order to use a GitHub App on your repositories or organization, you must install the app on your organization or personal account. You can install the same GitHub App on multiple accounts. For example, if you install the app on your personal account and on a few organizations that you own, you'll be able to use the app on your personal repositories, on the organizations where you installed the app, and on repositories owned by those organizations.
When you install an app, you grant the app permission to access the organization and repository resources that it requested. During the installation process, GitHub will tell you which permissions the GitHub App requested. For more information about the REST API requests the GitHub App can make with those permissions, see [Permissions required for GitHub Apps](https://docs.github.com/en/rest/overview/permissions-required-for-github-apps).
When you install an app, you will also choose which repositories to grant the GitHub App access to.
Before installing a GitHub App, you should ensure you trust the owner of the GitHub App. You should also review the permissions that the GitHub App is requesting and make sure you are comfortable granting those permissions. For more information about the REST API requests the GitHub App can make with those permissions, see [Permissions required for GitHub Apps](https://docs.github.com/en/rest/overview/permissions-required-for-github-apps).
There is no limit to how many apps you can install.
### [Difference between installation and authorization](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-github-marketplace-for-your-organizations#difference-between-installation-and-authorization)
After you install a GitHub App, you may also be asked to authorize the app.
When you **install** a GitHub App on your account or organization, you grant the app permission to access the organization and repository resources that it requested. You also specify which repositories the app can access. During the installation process, the GitHub App will indicate which repository and organization permissions you are granting. For more information about what different permissions enable a GitHub App to do, see [Choosing permissions for a GitHub App](https://docs.github.com/en/apps/creating-github-apps/setting-up-a-github-app/choosing-permissions-for-a-github-app).
For example, you might grant the GitHub App permission to read repository metadata and write issues, and you might grant the GitHub App access to all of your repositories.
![Screenshot of the page to install a GitHub App. The app requests read access to metadata and write access to issues.](https://docs.github.com/assets/cb-118277/images/github-apps/install-app.png)
When you **authorize** a GitHub App, you grant the app access to your GitHub account, based on the account permissions the app requested. During the authorization process, the app will indicate which resources the app can access on your account. When you authorize a GitHub App, you also grant the app permission to act on your behalf.
For example, you might grant the GitHub App permission to read your email addresses and write gists.
![Screenshot of the page to authorize a GitHub App. The app is requesting read access to email and write access to gists.](https://docs.github.com/assets/cb-106378/images/github-apps/authorize-app.png)
You can install a GitHub App without authorizing the app. Similarly, you can authorize the app without installing the app.
For more information about authorizing GitHub Apps, see [Authorizing GitHub Apps](https://docs.github.com/en/apps/using-github-apps/authorizing-github-apps).
## [Requirements to install a GitHub App on an organization](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-github-marketplace-for-your-organizations#requirements-to-install-a-github-app-on-an-organization)
Organization owners can install GitHub Apps on their organization.
For enterprises that pay by credit card, enterprise owners who are also organization owners can install GitHub Apps on organizations within their enterprise.
Admins of repositories that are owned by an organization can also install GitHub Apps on the organization if they only grant the app access to repositories that they are an admin of and if the app does not request any organization permissions or the "repository administration" permission. Organization owners can prevent outside collaborators who are repository admins from installing GitHub Apps.
The "app manager" role in an organization does not give a person the ability to install a GitHub App in the organization. For more information, see [About GitHub App managers](https://docs.github.com/en/apps/maintaining-github-apps/about-github-app-managers).
## [Installing a GitHub App in your organization](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-github-marketplace-for-your-organizations#installing-a-github-app-in-your-organization)
  1. To open GitHub Marketplace, in the top-left corner of GitHub, select 
![Screenshot of the navigation bar on GitHub. The "Open global navigation menu" icon is outlined in dark orange.](https://docs.github.com/assets/cb-2683/images/help/navigation/global-navigation-menu-icon.png)
  2. Browse to the app you'd like to install, then click on the app's name.
  3. On the app's page, under "Pricing and setup," click the pricing plan you'd like to use.
  4. Click **Install it for free** , **Buy with GitHub** , or **Try free for 14 days**.
  5. Choose an installation organization for the app. Depending on your organization's terms of service, this process will be slightly different.
     * If you have given GitHub permission to collect name and address information for your organization, in the "Billing information" section, select the **Switch billing account**
![Screenshot of the GitHub Marketplace app purchase screen. A collapsed blue dropdown menu labeled "Switch billing account" is outlined in dark orange.](https://docs.github.com/assets/cb-58957/images/help/marketplace/marketplace-confirm-org.png)
     * Otherwise, under "Review your order," select the **Account** dropdown menu, then click the organization in which you'd like to install the app.
![Screenshot of the GitHub Marketplace app purchase screen. A collapsed gray dropdown menu labeled "Account" is outlined in dark orange.](https://docs.github.com/assets/cb-12210/images/help/marketplace/marketplace-confirm-org-no-org-details.png)
  6. If you chose a paid plan, review your payment method.
     * To change the existing payment method on file for the organization, click **Edit** , then complete the form to add a new payment method.
     * If there isn't a payment method on file for the organization, click **Add a Payment Method** , then complete the form to add a credit card or PayPal account.
  7. Click **Complete order and begin installation**.
  8. If the app requires access to repositories, select **All repositories** or **Only select repositories**.
If the app creates any repositories, the app will automatically be granted access to those repositories as well.
  9. If you chose to give the app access to limited repositories instead of all of your repositories, type the name of each repository you'd like to give the app access to, then click on the repository name to select it.
  10. Review the app's access permissions, then click **Install**.


## [Further reading](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-github-marketplace-for-your-organizations#further-reading)
  * [Managing your payment and billing information](https://docs.github.com/en/billing/managing-your-billing/managing-your-payment-and-billing-information)
  * [Installing a GitHub App from GitHub Marketplace for your personal account](https://docs.github.com/en/apps/using-github-apps/installing-an-app-in-your-personal-account)


