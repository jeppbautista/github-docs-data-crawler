  * [Apps](https://docs.github.com/en/apps "Apps")/
  * [GitHub Marketplace](https://docs.github.com/en/apps/github-marketplace "GitHub Marketplace")/
  * [Create Marketplace apps](https://docs.github.com/en/apps/github-marketplace/creating-apps-for-github-marketplace "Create Marketplace apps")/
  * [View listing transactions](https://docs.github.com/en/apps/github-marketplace/creating-apps-for-github-marketplace/viewing-transactions-for-your-listing "View listing transactions")


# Viewing transactions for your listing
The GitHub Marketplace transactions page allows you to download and view all transactions for your GitHub Marketplace listing. You can view transactions for the past day (24 hours), week, month, or for the entire duration of time that your GitHub App has been listed.
## In this article
  * [Transaction data fields](https://docs.github.com/en/apps/github-marketplace/creating-apps-for-github-marketplace/viewing-transactions-for-your-listing#transaction-data-fields)
  * [Accessing GitHub Marketplace transactions](https://docs.github.com/en/apps/github-marketplace/creating-apps-for-github-marketplace/viewing-transactions-for-your-listing#accessing-github-marketplace-transactions)


This article applies to publishing apps in GitHub Marketplace only. For more information about publishing GitHub Actions in GitHub Marketplace, see [Publishing actions in GitHub Marketplace](https://docs.github.com/en/actions/creating-actions/publishing-actions-in-github-marketplace).
Because it takes time to aggregate data, you'll notice a slight delay in the dates shown. When you select a time period, you can see exact dates for the metrics at the top of the page.
You can view or download the transaction data to keep track of your subscription activity. Click the **Export CSV** button to download a `.csv` file. You can also select a period of time to view and search within the transaction page.
## [Transaction data fields](https://docs.github.com/en/apps/github-marketplace/creating-apps-for-github-marketplace/viewing-transactions-for-your-listing#transaction-data-fields)
  * **date:** The date of the transaction in `yyyy-mm-dd` format.
  * **app_name:** The app name.
  * **user_login:** The login of the user with the subscription.
  * **user_id:** The id of the user with the subscription.
  * **user_type:** The type of GitHub account, either `User` or `Organization`.
  * **country:** The three letter country code.
  * **amount_in_cents:** The amount of the transaction in cents. When a value is less the plan amount, the user upgraded and the new plan is prorated. A value of zero indicates the user canceled their plan.
  * **renewal_frequency:** The subscription renewal frequency, either `Monthly` or `Yearly`.
  * **marketplace_listing_plan_id:** The `id` of the subscription plan.
  * **region:** The name of the region present in billing address.
  * **postal_code:** The postal code value present in billing address.


![Screenshot of the "Transactions" tab in an app listing. Transactions from the past week are listed in a table with a search field.](https://docs.github.com/assets/cb-82701/images/marketplace/marketplace-transactions.png)
## [Accessing GitHub Marketplace transactions](https://docs.github.com/en/apps/github-marketplace/creating-apps-for-github-marketplace/viewing-transactions-for-your-listing#accessing-github-marketplace-transactions)
To access GitHub Marketplace transactions:
  1. In the upper-right corner of any page on GitHub, click your profile photo, then click 
  2. In the left sidebar, click 
  3. In the left sidebar, click either **OAuth Apps** or **GitHub Apps** depending on the GitHub Marketplace listing you'd like to manage.
You can also manage your listing by navigating to <https://github.com/marketplace/manage>.
![Screenshot of the sidebar on the "Developer Settings" page of GitHub. Options labeled "GitHub Apps" and "OAuth apps" are outlined in dark orange.](https://docs.github.com/assets/cb-38606/images/settings/apps-choose-app.png)
  4. Select the GitHub App that you'd like to view transactions for.
  5. On the app settings landing page, scroll down to the Marketplace section and click **List in Marketplace**. If you already have a Marketplace draft listing, click **Edit Marketplace listing**. The Marketplace section is only visible if you allowed your app to be installed by any user or organization when registering the app. For more information, see the list of [Marketplace requirements](https://docs.github.com/en/apps/publishing-apps-to-github-marketplace/creating-apps-for-github-marketplace/requirements-for-listing-an-app).
  6. Click the **Transactions** tab.
  7. Optionally, select a different time period by clicking the Period dropdown in the upper-right corner of the Transactions page.


