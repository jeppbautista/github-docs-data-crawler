  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Roll out Copilot at scale](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale "Roll out Copilot at scale")/
  * [Assigning licenses](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/assigning-licenses "Assigning licenses")/
  * [Manage spending](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/assigning-licenses/managing-your-companys-spending-on-github-copilot "Manage spending")


# Managing your company's spending on GitHub Copilot
Learn how to track spending, view usage, and optimize license distribution.
## Who can use this feature?
Enterprise owners and billing managers
GitHub Copilot Business or GitHub Copilot Enterprise
## In this article
  * [Understand who can grant licenses](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/assigning-licenses/managing-your-companys-spending-on-github-copilot#understand-who-can-grant-licenses)
  * [Managing charges for premium requests](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/assigning-licenses/managing-your-companys-spending-on-github-copilot#managing-charges-for-premium-requests)
  * [Map spending to groups of users](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/assigning-licenses/managing-your-companys-spending-on-github-copilot#map-spending-to-groups-of-users)
  * [Receive alerts for overspending](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/assigning-licenses/managing-your-companys-spending-on-github-copilot#receive-alerts-for-overspending)
  * [Visualize spending trends](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/assigning-licenses/managing-your-companys-spending-on-github-copilot#visualize-spending-trends)
  * [Optimize license usage](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/assigning-licenses/managing-your-companys-spending-on-github-copilot#optimize-license-usage)


When you're adopting GitHub Copilot in an enterprise, you will want to set budgets and track spending to ensure your rollout is sustainable. GitHub offers billing tools to help you visualize your spending patterns, receive alerts when you reach budget thresholds, and optimize your license usage.
Some of the tools recommended in this article are part of GitHub's new billing platform, which isn't available to all customers. If your enterprise has access, you will see a 
## [Understand who can grant licenses](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/assigning-licenses/managing-your-companys-spending-on-github-copilot#understand-who-can-grant-licenses)
To control spending, it's important to understand who can affect your bill by granting licenses to users. These are people with the **organization owner** role in organizations where you enable GitHub Copilot. Organization owners can receive requests for access from members through the GitHub UI.
We recommend that you identify the people with this role and communicate with them about your company's strategy for distributing licenses. For example, you may have a budget or limited pilot program, or you may distribute licenses through an internal website.
## [Managing charges for premium requests](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/assigning-licenses/managing-your-companys-spending-on-github-copilot#managing-charges-for-premium-requests)
Billing and budget setting for premium requests will start on **June 4, 2025** for all plans.
Certain requests may experience rate limits.
  * Rate limits restrict the number of requests that can be made within a specific time period.
  * High demand may result in rate limiting.


Each Copilot plan includes a per-user allowance for premium requests:
  * 300 requests per user per month for Copilot Business
  * 1000 requests per user per month for Copilot Enterprise


Copilot Chat, Copilot agent mode, Copilot coding agent, Copilot code review, and Copilot Extensions use premium requests, with usage varying by model.
Copilot coding agent uses GitHub Actions in addition to premium requests. For more information, see [Managing your spending limit for GitHub Actions](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-actions/managing-your-spending-limit-for-github-actions).
Premium requests over the allowance are rejected unless you have set a budget. Depending on the type of development tasks your developers use Copilot for, you may find developers need to make more premium requests than the allowance included in your plan.
Premium requests over the allowance are charged at a rate of $0.04 USD per request, with an additional multiplier applied to certain models. You can also increase your monthly allowance by upgrading to Copilot Enterprise.
For pricing details and a list of available models, see [Plans for GitHub Copilot](https://docs.github.com/en/copilot/about-github-copilot/subscription-plans-for-github-copilot#comparing-copilot-plans).
### [Managing budgets](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/assigning-licenses/managing-your-companys-spending-on-github-copilot#managing-budgets)
By default, a $0 budget for the GitHub Copilot Premium Request SKU is created for your enterprise. You can edit this budget from the "Budgets and alerts" page. See [Preventing overspending](https://docs.github.com/en/billing/using-the-new-billing-platform/preventing-overspending#editing-or-deleting-a-budget).
The default budget that is created applies to your whole enterprise. To set a new budget for a specific part of your enterprise, such as a cost center, you can create a new budget:
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. On the left side of the page, in the organization sidebar, click 
  4. Click **Budgets and alerts**.
  5. Click **New budget**.
  6. Under "Budget Type" select **SKU-level budget**.
  7. Select the "Product" dropdown and click **Copilot**.
  8. Select the "SKU" dropdown and click **Copilot Premium Request**
  9. Under "Budget scope", set the scope of spending for this budget.
  10. Under "Budget", set a budget amount. Optionally, choose to stop usage when the budget limit is reached.
  11. Click **Create budget**.


### [Tracking premium requests](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/assigning-licenses/managing-your-companys-spending-on-github-copilot#tracking-premium-requests)
You can view a CSV report that shows the cumulative number of premium requests per user over a time period. You can use this report to:
  * Understand if developers are frequently hitting the limit and would benefit from you enabling additional premium requests or upgrading your plan.
  * Identify users who are making a large number of premium requests over the limit, and follow up to the users to understand their use cases and requirements.
  * After enabling additional premium requests, track usage to determine if it would be more cost effective to upgrade to Copilot Enterprise.


You can download the report for an enterprise account, or for an organization that is not part of an enterprise.
  1. Go to your enterprise or organization account settings and click 
  2. In the left sidebar, click **Usage**.
  3. To download the usage report, select **Get usage report** in the upper-right corner of the page, and click **Copilot premium requests usage report**.


## [Map spending to groups of users](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/assigning-licenses/managing-your-companys-spending-on-github-copilot#map-spending-to-groups-of-users)
With GitHub's new billing platform, you can create cost centers to map spending to individual business units or groups of users. Cost centers allow you to track costs tied to different initiatives and charge the costs to specific areas of your business.
For example, if you were running a pilot program for GitHub Copilot Enterprise for a group of employees, you might want to create a cost center to track their spending and set a budget independently of the rest of the company.
### [Create a cost center](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/assigning-licenses/managing-your-companys-spending-on-github-copilot#create-a-cost-center)
  1. Go to your enterprise or organization account settings and click 
  2. In the left sidebar, click **Cost centers** , then click **New cost center**.
  3. Create the cost center. You don't need to add any repositories or organizations, because you will add users to the cost center directly in the next step.
As a priority, a cost center is charged for a Copilot license if the assigned **user** has been added to the cost center directly. As a fallback, a cost center is charged for the license if the **organization where the user receives access** has been added to the cost center.
  4. After creating the cost center, use the REST API to add the users whose usage you want to track. See [REST API endpoints for enterprise billing](https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin/billing#add-users-to-a-cost-center).


## [Receive alerts for overspending](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/assigning-licenses/managing-your-companys-spending-on-github-copilot#receive-alerts-for-overspending)
With GitHub's new billing platform, you can set a monthly budget on GitHub Copilot spending. Setting a budget for license-based products, such as Copilot, is for monitoring purposes only and will not prevent usage beyond the budgeted amount. However, you will receive notifications by email when spending exceeds certain percentages of the budget you've set. To prevent usage over the limit for the Copilot Premium Request SKU, update the default $0 SKU-level budget and select "Stop usage when budget limit is reached".
  1. Go to your enterprise or organization account settings and click 
  2. In the left sidebar, click **Budgets and alerts**.
  3. Click **New budget**.
  4. Select **Copilot** for the product, or **Copilot Premium Request** for the SKU, then configure the settings as required. You can choose who receives alerts when budget thresholds are reached.
  5. Click **Create budget**.


## [Visualize spending trends](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/assigning-licenses/managing-your-companys-spending-on-github-copilot#visualize-spending-trends)
With GitHub's new billing platform, you can understand your spending trends by viewing a graph for Copilot usage over a certain timeframe. For more detailed insights, you can filter the results by cost center and group usage by the type of Copilot plan.
  1. Go to your enterprise or organization account settings and click 
  2. In the left sidebar, click **Usage**.
  3. In the "Metered usage" section, in the search field, enter `product:copilot`. To filter by cost center, add a query like `cost_center:ce-pilot-group`.
  4. To understand spending differences between Copilot Business and Copilot Enterprise plans, select the **Group: None** dropdown menu and click **Group: SKU**.


![Screenshot of the "Usage" page. A line chart tracks Copilot spending over the current month, grouped by SKU.](https://docs.github.com/assets/cb-90151/images/help/copilot/track-spending.png)
## [Optimize license usage](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/assigning-licenses/managing-your-companys-spending-on-github-copilot#optimize-license-usage)
When you begin rolling out Copilot in a company, you may see low rates of adoption at first. An effective enablement process is essential to drive adoption of Copilot in your company. Tailor this process to your company's needs and goals, and design it to help your teams understand how to use Copilot effectively.
To ensure your licenses are being used effectively, you can use the API to identify inactive users. We recommend sending these users a message with advice and resources for getting started. If a user remains inactive, you can revoke their license and assign it to another user.
If you're not sure how best to distribute licenses, GitHub has found that many successful rollouts offer a fully self-service model where developers can claim a license without approval. This allows people to get started quickly and ensures you're giving licenses to people who plan to use them.
For detailed guidance, see:
  * [Driving Copilot adoption in your company](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/driving-copilot-adoption-in-your-company)
  * [Setting up a self-serve process for GitHub Copilot licenses](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/setting-up-a-self-serve-process-for-github-copilot-licenses)
  * [Reminding inactive users to use their GitHub Copilot license](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/reminding-inactive-users)


