  * [Apps](https://docs.github.com/en/apps "Apps")/
  * [GitHub Marketplace](https://docs.github.com/en/apps/github-marketplace "GitHub Marketplace")/
  * [Marketplace API usage](https://docs.github.com/en/apps/github-marketplace/using-the-github-marketplace-api-in-your-app "Marketplace API usage")/
  * [Testing your app](https://docs.github.com/en/apps/github-marketplace/using-the-github-marketplace-api-in-your-app/testing-your-app "Testing your app")


# Testing your app
GitHub recommends testing your app with APIs and webhooks before submitting your listing to GitHub Marketplace so you can provide an ideal experience for customers. Before an onboarding expert approves your app, it must adequately handle the billing flows.
## In this article
  * [Testing apps](https://docs.github.com/en/apps/github-marketplace/using-the-github-marketplace-api-in-your-app/testing-your-app#testing-apps)
  * [Testing APIs](https://docs.github.com/en/apps/github-marketplace/using-the-github-marketplace-api-in-your-app/testing-your-app#testing-apis)
  * [Testing webhooks](https://docs.github.com/en/apps/github-marketplace/using-the-github-marketplace-api-in-your-app/testing-your-app#testing-webhooks)


This article applies to publishing apps in GitHub Marketplace only. For more information about publishing GitHub Actions in GitHub Marketplace, see [Publishing actions in GitHub Marketplace](https://docs.github.com/en/actions/creating-actions/publishing-actions-in-github-marketplace).
## [Testing apps](https://docs.github.com/en/apps/github-marketplace/using-the-github-marketplace-api-in-your-app/testing-your-app#testing-apps)
You can use a draft GitHub Marketplace listing to simulate each of the billing flows. A listing in the draft state means that it has not been submitted for approval. Any purchases you make using a draft GitHub Marketplace listing will _not_ create real transactions, and GitHub will not charge your credit card. Note that you can only simulate purchases for plans published in the draft listing and not for draft plans. For more information, see [Drafting a listing for your app](https://docs.github.com/en/apps/github-marketplace/listing-an-app-on-github-marketplace/drafting-a-listing-for-your-app) and [Using the GitHub Marketplace API in your app](https://docs.github.com/en/apps/github-marketplace/using-the-github-marketplace-api-in-your-app).
### [Using a development app with a draft listing to test changes](https://docs.github.com/en/apps/github-marketplace/using-the-github-marketplace-api-in-your-app/testing-your-app#using-a-development-app-with-a-draft-listing-to-test-changes)
A GitHub Marketplace listing can only be associated with a single app registration, and each app can only access its own GitHub Marketplace listing. For these reasons, we recommend configuring a separate development app, with the same configuration as your production app, and creating a draft GitHub Marketplace listing that you can use for testing. The draft GitHub Marketplace listing allows you to test changes without affecting the active users of your production app. You will never have to submit your development GitHub Marketplace listing, since you will only use it for testing.
Because you can only create draft GitHub Marketplace listings for public apps, you must make your development app public. Public apps are not discoverable outside of published GitHub Marketplace listings as long as you don't share the app's URL. A Marketplace listing in the draft state is only visible to the app's owner.
Once you have a development app with a draft listing, you can use it to test changes you make to your app while integrating with the GitHub Marketplace API and webhooks.
Do not make test purchases with an app that is live in GitHub Marketplace.
### [Simulating Marketplace purchase events](https://docs.github.com/en/apps/github-marketplace/using-the-github-marketplace-api-in-your-app/testing-your-app#simulating-marketplace-purchase-events)
Your testing scenarios may require setting up listing plans that offer free trials and switching between free and paid subscriptions. Because downgrades and cancellations don't take effect until the next billing cycle, GitHub provides a developer-only feature to "Apply Pending Change" to force `changed` and `cancelled` plan actions to take effect immediately. You can access **Apply Pending Change** for apps with draft Marketplace listings in <https://github.com/settings/billing#pending-cycle>:
## [Testing APIs](https://docs.github.com/en/apps/github-marketplace/using-the-github-marketplace-api-in-your-app/testing-your-app#testing-apis)
For most GitHub Marketplace API endpoints, we also provide stubbed API endpoints that return hard-coded, fake data you can use for testing. To receive stubbed data, you must specify stubbed URLs, which include `/stubbed` in the route (for example, `/user/marketplace_purchases/stubbed`). For a list of endpoints that support this stubbed-data approach, see [GitHub Marketplace endpoints](https://docs.github.com/en/rest/apps#github-marketplace).
## [Testing webhooks](https://docs.github.com/en/apps/github-marketplace/using-the-github-marketplace-api-in-your-app/testing-your-app#testing-webhooks)
GitHub provides tools for testing your deployed payloads. For more information, see [Testing webhooks](https://docs.github.com/en/webhooks/testing-and-troubleshooting-webhooks/testing-webhooks).
