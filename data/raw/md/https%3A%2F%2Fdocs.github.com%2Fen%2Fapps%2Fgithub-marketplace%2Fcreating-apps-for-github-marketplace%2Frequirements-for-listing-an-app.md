  * [Apps](https://docs.github.com/en/apps "Apps")/
  * [GitHub Marketplace](https://docs.github.com/en/apps/github-marketplace "GitHub Marketplace")/
  * [Create Marketplace apps](https://docs.github.com/en/apps/github-marketplace/creating-apps-for-github-marketplace "Create Marketplace apps")/
  * [Listing requirements](https://docs.github.com/en/apps/github-marketplace/creating-apps-for-github-marketplace/requirements-for-listing-an-app "Listing requirements")


# Requirements for listing an app
Apps on GitHub Marketplace must meet the requirements outlined on this page before the listing can be published.
## In this article
  * [Requirements for all GitHub Marketplace listings](https://docs.github.com/en/apps/github-marketplace/creating-apps-for-github-marketplace/requirements-for-listing-an-app#requirements-for-all-github-marketplace-listings)
  * [Considerations for free apps](https://docs.github.com/en/apps/github-marketplace/creating-apps-for-github-marketplace/requirements-for-listing-an-app#considerations-for-free-apps)
  * [Requirements for GitHub Copilot Extensions](https://docs.github.com/en/apps/github-marketplace/creating-apps-for-github-marketplace/requirements-for-listing-an-app#requirements-for-github-copilot-extensions)
  * [Requirements for paid apps](https://docs.github.com/en/apps/github-marketplace/creating-apps-for-github-marketplace/requirements-for-listing-an-app#requirements-for-paid-apps)
  * [Billing requirements for paid apps](https://docs.github.com/en/apps/github-marketplace/creating-apps-for-github-marketplace/requirements-for-listing-an-app#billing-requirements-for-paid-apps)


This article applies to publishing apps in GitHub Marketplace only. For more information about publishing GitHub Actions in GitHub Marketplace, see [Publishing actions in GitHub Marketplace](https://docs.github.com/en/actions/creating-actions/publishing-actions-in-github-marketplace).
The requirements for listing an app on GitHub Marketplace vary according to whether you want to offer a free or a paid app.
## [Requirements for all GitHub Marketplace listings](https://docs.github.com/en/apps/github-marketplace/creating-apps-for-github-marketplace/requirements-for-listing-an-app#requirements-for-all-github-marketplace-listings)
All listings on GitHub Marketplace should be for tools that provide value to the GitHub community. When you submit your listing for publication, you must read and accept the terms of the [GitHub Marketplace Developer Agreement](https://docs.github.com/en/site-policy/github-terms/github-marketplace-developer-agreement).
### [User experience requirements for all apps](https://docs.github.com/en/apps/github-marketplace/creating-apps-for-github-marketplace/requirements-for-listing-an-app#user-experience-requirements-for-all-apps)
All listings should meet the following requirements, regardless of whether they are for a free or paid app.
  * Listings must not actively persuade users away from GitHub.
  * Listings must include valid contact information for the publisher.
  * Listings must have a relevant description of the application.
  * Listings must specify a pricing plan.
  * Apps must provide value to customers and integrate with the platform in some way beyond authentication.
  * Apps must be publicly available in GitHub Marketplace and cannot be in public preview or available by invite only, with the exception of Copilot Extensions.
  * Apps must have webhook events set up to notify the publisher of any plan changes or cancellations using the GitHub Marketplace API. For more information, see [Using the GitHub Marketplace API in your app](https://docs.github.com/en/apps/github-marketplace/using-the-github-marketplace-api-in-your-app).


For more information on providing a good customer experience, see [Customer experience best practices for apps](https://docs.github.com/en/apps/github-marketplace/creating-apps-for-github-marketplace/customer-experience-best-practices-for-apps).
### [Brand and listing requirements for all apps](https://docs.github.com/en/apps/github-marketplace/creating-apps-for-github-marketplace/requirements-for-listing-an-app#brand-and-listing-requirements-for-all-apps)
  * Apps that use GitHub logos must follow the GitHub guidelines. For more information, see [GitHub Logos and Usage](https://github.com/logos).
  * Apps must have a logo, feature card, and screenshots images that meet the recommendations provided in [Writing a listing description for your app](https://docs.github.com/en/apps/github-marketplace/listing-an-app-on-github-marketplace/writing-a-listing-description-for-your-app).
  * Listings must include descriptions that are well written and free of grammatical errors. For guidance in writing your listing, see [Writing a listing description for your app](https://docs.github.com/en/apps/github-marketplace/listing-an-app-on-github-marketplace/writing-a-listing-description-for-your-app).


To protect your customers, we recommend that you also follow security best practices. For more information, see [Security best practices for apps on GitHub Marketplace](https://docs.github.com/en/apps/github-marketplace/creating-apps-for-github-marketplace/security-best-practices-for-apps-on-github-marketplace).
## [Considerations for free apps](https://docs.github.com/en/apps/github-marketplace/creating-apps-for-github-marketplace/requirements-for-listing-an-app#considerations-for-free-apps)
Free apps are encouraged in GitHub Marketplace and are a great way to offer open source services. If you list a paid version of your app outside of GitHub Marketplace then, after a free listing of your app in the marketplace meets the [requirements for paid apps](https://docs.github.com/en/apps/github-marketplace/creating-apps-for-github-marketplace/requirements-for-listing-an-app#requirements-for-paid-apps), you must offer at least one paid plan for the app in GitHub Marketplace.
## [Requirements for GitHub Copilot Extensions](https://docs.github.com/en/apps/github-marketplace/creating-apps-for-github-marketplace/requirements-for-listing-an-app#requirements-for-github-copilot-extensions)
Copilot Extensions are essentially GitHub Apps with additional read access to Copilot Chat, integration with the Copilot API, and optional integration into other LLMs.
To publish an extension, it must be owned by an organization account with Verified Creator status. For more information about the verification process or transferring ownership of your app, see [Applying for publisher verification for your organization](https://docs.github.com/en/apps/github-marketplace/github-marketplace-overview/applying-for-publisher-verification-for-your-organization).
The requirements to publish a Copilot Extension are the same as the requirements for free apps, with the following exceptions:
  * Your extension must provide a clear and descriptive response to a prompt like "What can you do?" or "List your capabilities".
  * Your extension can be in public preview as long as that is clearly communicated in the listing description. If you are using a waitlist, you must also include a link to sign up at the top of the description. Someone from the GitHub review team will join the waitlist and email your technical lead requesting access for testing.
  * You must include links to two videos that demonstrate the following:
    * A few example prompts and responses from your extension
    * A net new user installing, authenticating, and sending their first prompt to your extension
These videos are private to GitHub and are used solely for reviewing your listing submission. The videos can be brief, and you don't need to edit them.
  * Your extension must provide a stable and reliable user experience, and be able to perform the capabilities listed in the description.
  * You must provide a pathway for new users to install, set up, and authorize your extension with minimal friction. If the GitHub review team is not able to successfully test your extension, it will not be approved for publishing.


## [Requirements for paid apps](https://docs.github.com/en/apps/github-marketplace/creating-apps-for-github-marketplace/requirements-for-listing-an-app#requirements-for-paid-apps)
To publish a paid plan for your app on the GitHub Marketplace, your app must be owned by an organization that is a verified publisher. For more information about the verification process or transferring ownership of your app, see [Applying for publisher verification for your organization](https://docs.github.com/en/apps/github-marketplace/github-marketplace-overview/applying-for-publisher-verification-for-your-organization).
If your app is already published and you're a verified publisher, then you can publish a new paid plan from the pricing plan editor. For more information, see [Setting pricing plans for your listing](https://docs.github.com/en/apps/github-marketplace/listing-an-app-on-github-marketplace/setting-pricing-plans-for-your-listing).
To publish a paid app (or an app that offers a paid plan), you must also meet the following requirements:
  * GitHub Apps should have a minimum of 100 installations.
  * OAuth apps should have a minimum of 200 users.
  * All paid apps must handle GitHub Marketplace purchase events for new purchases, upgrades, downgrades, cancellations, and free trials. For more information, see [Billing requirements for paid apps](https://docs.github.com/en/apps/github-marketplace/creating-apps-for-github-marketplace/requirements-for-listing-an-app#billing-requirements-for-paid-apps) below.


When you are ready to publish the app on GitHub Marketplace you must request verification for the app listing.
If you want to sell an app that's owned by your personal account, first you'll need to transfer the app to an organization, and then request verification for a listing created by the organization. For information on how to transfer an app to an organization, see: [Submitting your listing for publication](https://docs.github.com/en/apps/github-marketplace/listing-an-app-on-github-marketplace/submitting-your-listing-for-publication#transferring-an-app-to-an-organization-before-you-submit).
## [Billing requirements for paid apps](https://docs.github.com/en/apps/github-marketplace/creating-apps-for-github-marketplace/requirements-for-listing-an-app#billing-requirements-for-paid-apps)
Your app does not need to handle payments but does need to use GitHub Marketplace purchase events to manage new purchases, upgrades, downgrades, cancellations, and free trials. For information about how to integrate these events into your app, see [Using the GitHub Marketplace API in your app](https://docs.github.com/en/apps/github-marketplace/using-the-github-marketplace-api-in-your-app).
Using GitHub's billing API allows customers to purchase an app without leaving GitHub and to pay for the service with the payment method already attached to their account on GitHub.
  * Apps must support both monthly and annual billing for paid subscriptions purchases.
  * Listings may offer any combination of free and paid plans. Free plans are optional but encouraged. For more information, see [Setting pricing plans for your listing](https://docs.github.com/en/apps/github-marketplace/listing-an-app-on-github-marketplace/setting-pricing-plans-for-your-listing).


