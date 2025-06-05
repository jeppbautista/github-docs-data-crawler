  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Build Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions "Build Copilot Extensions")/
  * [Manage Extension availability](https://docs.github.com/en/copilot/building-copilot-extensions/managing-the-availability-of-your-copilot-extension "Manage Extension availability")


# Managing the availability of your Copilot Extension
After you build your Copilot Extension, you can change it's visibility or publish it on the GitHub Marketplace.
## In this article
  * [Changing the visibility of your Copilot Extension](https://docs.github.com/en/copilot/building-copilot-extensions/managing-the-availability-of-your-copilot-extension#changing-the-visibility-of-your-copilot-extension)
  * [Listing your Copilot Extension on the GitHub Marketplace](https://docs.github.com/en/copilot/building-copilot-extensions/managing-the-availability-of-your-copilot-extension#listing-your-copilot-extension-on-the-github-marketplace)


When you build a Copilot Extension, you have two options for the visibility of your GitHub App:
  * **Public:** Any user or organization account with the link to your app's installation page can install it. Making your app public automatically creates a public installation page, but does not list the app on the GitHub Marketplace.
  * **Private:** Any user, organization, or enterprise can create an extension. Any user or organization, and any organization in an enterprise can install an enterprise-created extension. Private extensions are not available to all users outside your organization or enterprise based on the level at which it was created.


If you make your app public, you can choose to publish it on the GitHub Marketplace.
## [Changing the visibility of your Copilot Extension](https://docs.github.com/en/copilot/building-copilot-extensions/managing-the-availability-of-your-copilot-extension#changing-the-visibility-of-your-copilot-extension)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Under "Organizations", next to the name of your organization, click **Settings**.
  3. At the bottom of the sidebar, select **GitHub Apps**.
  4. In the "GitHub Apps" section, next to the name of your Copilot Extension, click **Edit**.
  5. In the sidebar, click **Advanced**. At the bottom of the "Danger Zone" section, you will see one of two options: 
     * **Make public:** If you see the **Make public** option, your GitHub App is currently private, and can only be installed by the organization or user that created the app. You can click **Make public** to allow any other account with the link to your app's installation page to install your Copilot extension. Leave the settings unchanged to keep your app private.
     * **Make private:** If you see the **Make private** option, your GitHub App is currently public, and can be installed by any account with the link to your app's installation page. You can click **Make private** to only allow installations by the organization or user that created the app, or organizations that are part of the enterprise that created the extension. Leave the settings unchanged to keep your app public.
  6. Optionally, if your GitHub App is public, you can share the link to the installation page for your Copilot Extension. In the sidebar, click **Public page** in the sidebar, then copy the link for your listing.


You can set a published marketplace extension to private, and it will remain accessible on the GitHub Marketplace. However, it won't be accessible from the direct installation page.
## [Listing your Copilot Extension on the GitHub Marketplace](https://docs.github.com/en/copilot/building-copilot-extensions/managing-the-availability-of-your-copilot-extension#listing-your-copilot-extension-on-the-github-marketplace)
To list your Copilot Extension on the GitHub Marketplace, you must meet the following requirements:
  * You must publish your app from an organization that is a verified publisher on the GitHub Marketplace. 
    * If your organization is not yet verified, see [Applying for publisher verification for your organization](https://docs.github.com/en/apps/github-marketplace/github-marketplace-overview/applying-for-publisher-verification-for-your-organization).
    * If you need to transfer ownership of your app from your personal account to your organization account, see [Transferring ownership of a GitHub App](https://docs.github.com/en/apps/maintaining-github-apps/transferring-ownership-of-a-github-app).
  * Your app must meet the requirements for all Copilot Extension listings on the GitHub Marketplace. See [Requirements for listing an app](https://docs.github.com/en/apps/github-marketplace/creating-apps-for-github-marketplace/requirements-for-listing-an-app#requirements-for-github-copilot-extensions).


App managers cannot create, edit, or publish extensions on the GitHub Marketplace. To manage a listing, you should be an organization owner for the publishing organization.
Paid plans are not supported for Copilot Extensions during public preview. Any requests to publish with a paid plan attached will not be approved.
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Under "Organizations", next to the name of your organization, click **Settings**.
  3. At the bottom of the sidebar, select **GitHub Apps**.
  4. Select the app you'd like to publish to the GitHub Marketplace.
  5. On the app settings landing page, scroll down to the Marketplace section, then click **List in Marketplace**. The Marketplace section is only visible if your app is public.
  6. In the "Listing name" text box, type a name for your listing. This name is displayed on the GitHub Marketplace page and in search results, and can be changed later. GitHub recommends using any of the following naming conventions:
     * `YOUR-PRODUCT-NAME` (example: "Copilot"): We recommend this convention if your extension stays within the scope of a single product and there are no other well-known products with the same name.
     * `YOUR-COMPANY-NAME` (example "GitHub"): We recommend this convention if your extension spans multiple products.
     * `YOUR-COMPANY-PRODUCT-NAME` (example: "GitHub Copilot"): We recommend this convention if your extension stays within the scope of one product, but there are other well-known products with the same name.
The listing name is not the same as your GitHub App's name or your Copilot Extension's slug. Changing the listing name will not affect the app name or slug.
  7. In the "Primary category" section, select the dropdown menu, then click a category. You can change your selection or add a secondary category later.
  8. To create a draft listing for your Copilot Extension, click **Save and add more details**.
  9. After you create a new draft listing, you'll see a view where you can manage your listing. Before you can submit your listing for review, you need to:
     * Fill out each of the required sections
     * Verify the organization account that owns the GitHub App
     * Accept the GitHub Marketplace Developer Agreement
  10. To submit your listing, click **Submit for review**. After your listing is reviewed, an onboarding expert will let you know if your submission was approved or denied.


GitHub reviews all submissions to ensure they meet our standards for quality, performance, reliability, and security. GitHub may deny submissions at its own discretion, and will provide reasons for denials. You are welcome to address any issues and resubmit your extension for review. You may also go through the [GitHub Appeal and Reinstatement Process](https://docs.github.com/en/site-policy/acceptable-use-policies/github-appeal-and-reinstatement).
