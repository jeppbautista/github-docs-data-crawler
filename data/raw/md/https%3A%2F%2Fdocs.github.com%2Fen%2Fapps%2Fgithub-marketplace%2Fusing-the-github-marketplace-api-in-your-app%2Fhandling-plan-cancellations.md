  * [Apps](https://docs.github.com/en/apps "Apps")/
  * [GitHub Marketplace](https://docs.github.com/en/apps/github-marketplace "GitHub Marketplace")/
  * [Marketplace API usage](https://docs.github.com/en/apps/github-marketplace/using-the-github-marketplace-api-in-your-app "Marketplace API usage")/
  * [Plan cancellations](https://docs.github.com/en/apps/github-marketplace/using-the-github-marketplace-api-in-your-app/handling-plan-cancellations "Plan cancellations")


# Handling plan cancellations
Cancelling a GitHub Marketplace app triggers the [`marketplace_purchase` event](https://docs.github.com/en/marketplace/integrating-with-the-github-marketplace-api/github-marketplace-webhook-events) webhook with the `cancelled` action, which kicks off the cancellation flow.
## In this article
  * [Step 1. Cancellation event](https://docs.github.com/en/apps/github-marketplace/using-the-github-marketplace-api-in-your-app/handling-plan-cancellations#step-1-cancellation-event)
  * [Step 2. Deactivating customer accounts](https://docs.github.com/en/apps/github-marketplace/using-the-github-marketplace-api-in-your-app/handling-plan-cancellations#step-2-deactivating-customer-accounts)


This article applies to publishing apps in GitHub Marketplace only. For more information about publishing GitHub Actions in GitHub Marketplace, see [Publishing actions in GitHub Marketplace](https://docs.github.com/en/actions/creating-actions/publishing-actions-in-github-marketplace).
For more information about cancelling as it relates to billing, see [Billing customers](https://docs.github.com/en/apps/github-marketplace/selling-your-app-on-github-marketplace/billing-customers).
## [Step 1. Cancellation event](https://docs.github.com/en/apps/github-marketplace/using-the-github-marketplace-api-in-your-app/handling-plan-cancellations#step-1-cancellation-event)
If a customer chooses to cancel a GitHub Marketplace order, GitHub sends a [`marketplace_purchase`](https://docs.github.com/en/apps/github-marketplace/using-the-github-marketplace-api-in-your-app/webhook-events-for-the-github-marketplace-api) webhook with the action `cancelled` to your app when the cancellation takes effect. If the customer cancels during a free trial, your app will receive the event immediately. When a customer cancels a paid plan, the cancellation will occur at the end of the customer's billing cycle.
## [Step 2. Deactivating customer accounts](https://docs.github.com/en/apps/github-marketplace/using-the-github-marketplace-api-in-your-app/handling-plan-cancellations#step-2-deactivating-customer-accounts)
When a customer cancels a free or paid plan, your app must perform these steps to complete cancellation:
  1. Deactivate the account of the customer who canceled their plan.
  2. Revoke the OAuth token your app received for the customer.
  3. If your app is an OAuth app, remove all webhooks your app created for repositories.
  4. Remove all customer data within 30 days of receiving the `cancelled` event.


We recommend using the [`marketplace_purchase`](https://docs.github.com/en/apps/github-marketplace/using-the-github-marketplace-api-in-your-app/webhook-events-for-the-github-marketplace-api) webhook's `effective_date` to determine when a plan change will occur and periodically synchronizing the [List accounts for a plan](https://docs.github.com/en/rest/apps/marketplace#list-accounts-for-a-plan). For more information on webhooks, see [Webhook events for the GitHub Marketplace API](https://docs.github.com/en/apps/github-marketplace/using-the-github-marketplace-api-in-your-app/webhook-events-for-the-github-marketplace-api).
