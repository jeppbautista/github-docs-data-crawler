  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Administer GitHub Actions](https://docs.github.com/en/actions/administering-github-actions "Administer GitHub Actions")/
  * [GitHub Actions metrics](https://docs.github.com/en/actions/administering-github-actions/viewing-github-actions-metrics "GitHub Actions metrics")


# Viewing GitHub Actions metrics
You can view metrics to monitor where your organization or repositories use GitHub Actions and how they are performing.
## Who can use this feature?
Organization owners and users with the "View organization Actions metrics" permission can view organization-level metrics.   
  
Users with the base repository role can view repository-level metrics.
## In this article
  * [About GitHub Actions metrics](https://docs.github.com/en/actions/administering-github-actions/viewing-github-actions-metrics#about-github-actions-metrics)
  * [Enabling access to GitHub Actions metrics](https://docs.github.com/en/actions/administering-github-actions/viewing-github-actions-metrics#enabling-access-to-github-actions-metrics)
  * [About GitHub Actions usage metrics](https://docs.github.com/en/actions/administering-github-actions/viewing-github-actions-metrics#about-github-actions-usage-metrics)
  * [About GitHub Actions performance metrics](https://docs.github.com/en/actions/administering-github-actions/viewing-github-actions-metrics#about-github-actions-performance-metrics)
  * [Understanding GitHub Actions metrics aggregation](https://docs.github.com/en/actions/administering-github-actions/viewing-github-actions-metrics#understanding-github-actions-metrics-aggregation)
  * [Viewing GitHub Actions metrics for your organization](https://docs.github.com/en/actions/administering-github-actions/viewing-github-actions-metrics#viewing-github-actions-metrics-for-your-organization)
  * [Viewing GitHub Actions metrics for your repository](https://docs.github.com/en/actions/administering-github-actions/viewing-github-actions-metrics#viewing-github-actions-metrics-for-your-repository)


## [About GitHub Actions metrics](https://docs.github.com/en/actions/administering-github-actions/viewing-github-actions-metrics#about-github-actions-metrics)
GitHub Actions metrics provide insights into how your workflows and jobs are performing at the organization and repository levels. There are two types of metrics to help you analyze different aspects of your workflows:
  * **GitHub Actions usage metrics:** Usage metrics help you track how many minutes your workflows and jobs consume. You can use this data to understand the cost of running Actions and ensure you're staying within your plan limits. This is especially useful for identifying high-usage workflows or repositories.
  * **GitHub Actions performance metrics:** Performance metrics focus on the efficiency and reliability of your workflows and jobs. With performance metrics, you can monitor key indicators like job run times, queue times, and failure rates to identify bottlenecks, slow-running jobs, or frequently failing workflows.


## [Enabling access to GitHub Actions metrics](https://docs.github.com/en/actions/administering-github-actions/viewing-github-actions-metrics#enabling-access-to-github-actions-metrics)
Organization owners can create custom organization roles to allow people to view GitHub Actions usage metrics for their organization. To provide users with access, select the "View organization Actions metrics" role when creating a custom organization role. For more information, see [About custom organization roles](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/about-custom-organization-roles).
## [About GitHub Actions usage metrics](https://docs.github.com/en/actions/administering-github-actions/viewing-github-actions-metrics#about-github-actions-usage-metrics)
GitHub Actions usage metrics enable you to analyze how your organization is using Actions minutes. You can view usage information related to:
  * **Workflows**. View usage data for each workflow in your organization, and use this information to identify opportunities for optimization, such as refactoring a workflow or using a larger runner.
  * **Jobs**. See which jobs are the most resource-intensive and where they are running.
  * **Repositories**. Get a high-level snapshot of each repository in your organization and their volume of Actions minutes usage.
  * **Runtime OS**. Understand how runners for each operating system are using Actions minutes and what types of operating systems your workflows are running on most often.
  * **Runner type**. Compare how your self-hosted runners and GitHub-hosted runners use Actions minutes and the volume of workflow runs for each type of runner.


## [About GitHub Actions performance metrics](https://docs.github.com/en/actions/administering-github-actions/viewing-github-actions-metrics#about-github-actions-performance-metrics)
GitHub Actions performance metrics enables you to analyze the efficiency and reliability of your workflows. You can view performance information such as average run times, average queue times, and failure rates, related to:
  * **Workflows**. View performance data for each workflow in your organization, including average run time and job failures. Use this information to identify inefficient workflows and run stability.
  * **Jobs**. View performance data for each individual job to, including average run time, average queue time, and job failures. Use this information to identify inefficient jobs.
  * **Repositories**. Get a high-level snapshot of each repository in your organization and their average performance metrics.
  * **Runtime OS**. Understand how runners for each operating system are performing.
  * **Runner type**. Compare the performance of self-hosted runners and GitHub-hosted runners, to make decisions about runner types.


## [Understanding GitHub Actions metrics aggregation](https://docs.github.com/en/actions/administering-github-actions/viewing-github-actions-metrics#understanding-github-actions-metrics-aggregation)
The time period selection feature allows you to view GitHub Actions metrics over predefined periods, as detailed in the following table. These metrics include skipped runs and those that use zero minutes. Data is presented using Coordinated Universal Time (UTC) days.
Period | Description  
---|---  
Current week (Mon-Sun) | Data from Monday through the current day when the page is viewed.  
Current month | Data from the first of the month to the current day when the page is viewed.  
Last month | Data from the first day to the last day of the previous month.  
Last 30 days | Data from the last 30 days to when the page is viewed.  
Last 90 days | Data from the last 90 days to when the page is viewed.  
Last year | Data aggregated for the last 12 months.  
Custom | Data from a custom date range. The range can be up to 100 days including the start and end dates and go back as far as one year.  
## [Viewing GitHub Actions metrics for your organization](https://docs.github.com/en/actions/administering-github-actions/viewing-github-actions-metrics#viewing-github-actions-metrics-for-your-organization)
There may be a discrepancy between the **Workflows** tab's job count and the **Jobs** tab's count due to differences in how unique jobs are identified. This does not affect the total minutes calculated.
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Click the name of your organization.
  3. Under your organization name, click 
![Screenshot of the horizontal navigation bar for an organization. A tab, labeled with a graph icon and "Insights," is outlined in dark orange.](https://docs.github.com/assets/cb-25805/images/help/organizations/org-nav-insights-tab.png)
  4. In the "Insights" navigation menu, click **Actions Usage Metrics** or click **Actions Performance Metrics**.
  5. Optionally, to select a time period to view usage metrics for, choose an option from the **Period** drop down menu at the top right of the page. For more information, see [Understanding GitHub Actions metrics aggregation](https://docs.github.com/en/actions/administering-github-actions/viewing-github-actions-metrics#understanding-github-actions-metrics-aggregation).
  6. Click on the tab that contains the metrics you would like to view. For more information, see [About GitHub Actions usage metrics](https://docs.github.com/en/actions/administering-github-actions/viewing-github-actions-metrics#about-github-actions-usage-metrics) or [About GitHub Actions performance metrics](https://docs.github.com/en/actions/administering-github-actions/viewing-github-actions-metrics#about-github-actions-performance-metrics).
  7. Optionally, to filter the data displayed in a tab, create a filter.
    1. Click on the 
    2. Click 
    3. Choose a metric you would like to filter results by.
    4. Depending on the metric you chose, fill out information in the "Qualifier," "Operator," and "Value" columns.
    5. Optionally, click 
    6. Click **Apply**.
  8. Optionally, to download usage metrics to a CSV file, click 


## [Viewing GitHub Actions metrics for your repository](https://docs.github.com/en/actions/administering-github-actions/viewing-github-actions-metrics#viewing-github-actions-metrics-for-your-repository)
There may be a discrepancy between the **Workflows** tab's job count and the **Jobs** tab's count due to differences in how unique jobs are identified. This does not affect the total minutes calculated.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click the 
  3. In the "Insights" navigation menu, click **Actions Usage Metrics** or click **Actions Performance Metrics**.
  4. Optionally, to select a time period to view usage metrics for, choose an option from the **Period** drop down menu at the top right of the page. For more information, see [Understanding GitHub Actions metrics aggregation](https://docs.github.com/en/actions/administering-github-actions/viewing-github-actions-metrics#understanding-github-actions-metrics-aggregation).
  5. Click on the tab that contains the metrics you would like to view. For more information, see [About GitHub Actions usage metrics](https://docs.github.com/en/actions/administering-github-actions/viewing-github-actions-metrics#about-github-actions-usage-metrics) or [About GitHub Actions performance metrics](https://docs.github.com/en/actions/administering-github-actions/viewing-github-actions-metrics#about-github-actions-performance-metrics).
  6. Optionally, to filter the data displayed in a tab, create a filter. 
    1. Click on the 
    2. Click 
    3. Choose a metric you would like to filter results by.
    4. Depending on the metric you chose, fill out information in the "Qualifier," "Operator," and "Value" columns.
    5. Optionally, click 
    6. Click **Apply**.
  7. Optionally, to download usage metrics to a CSV file, click 


