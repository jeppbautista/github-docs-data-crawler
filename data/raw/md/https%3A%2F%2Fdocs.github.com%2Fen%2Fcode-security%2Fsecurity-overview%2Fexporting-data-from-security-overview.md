  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Security overview](https://docs.github.com/en/code-security/security-overview "Security overview")/
  * [Export data](https://docs.github.com/en/code-security/security-overview/exporting-data-from-security-overview "Export data")


# Exporting data from security overview
From security overview, you can export CSV files of the data used for your organization or enterprise's overview, risk, coverage, and CodeQL pull request alerts pages.
## Who can use this feature?
Access requires:
  * Organization views: **write** access to repositories in the organization
  * Enterprise views: organization owners and security managers


Organizations owned by a GitHub Team account with GitHub Secret Protection or GitHub Code Security, or owned by a GitHub Enterprise account
## In this article
  * [About exporting your security overview data](https://docs.github.com/en/code-security/security-overview/exporting-data-from-security-overview#about-exporting-your-security-overview-data)
  * [Exporting overview, coverage, and risk data from your organization's security overview](https://docs.github.com/en/code-security/security-overview/exporting-data-from-security-overview#exporting-overview-coverage-and-risk-data-from-your-organizations-security-overview)
  * [Exporting overview, coverage, and risk data from your enterprise's security overview](https://docs.github.com/en/code-security/security-overview/exporting-data-from-security-overview#exporting-overview-coverage-and-risk-data-from-your-enterprises-security-overview)


## [About exporting your security overview data](https://docs.github.com/en/code-security/security-overview/exporting-data-from-security-overview#about-exporting-your-security-overview-data)
From security overview, you can download comma-separated values (CSV) files containing data from several pages of your organization or enterprise's security overview. These files can be used for efforts like security research and in-depth data analysis, and can integrate easily with external datasets.
The overview page contains data about security alerts across your organization or enterprise, while the risk and coverage pages contain data about repositories and how they are affected by security alerts or covered by security features. The CodeQL pull request alerts page contains data about CodeQL alerts that were caught in pull requests merged to the default branch.
The CSV file you download will contain data corresponding to the filters you have applied to security overview. For example, if you add the filter `dependabot-alerts:enabled`, your file will only contain data for repositories that have enabled Dependabot alerts.
In the "Teams" column of the CSV file, each repository will list a maximum of 20 teams with write access to that repository. If more than 20 teams have write access to a repository, the data will be truncated.
## [Exporting overview, coverage, and risk data from your organization's security overview](https://docs.github.com/en/code-security/security-overview/exporting-data-from-security-overview#exporting-overview-coverage-and-risk-data-from-your-organizations-security-overview)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. In the "Organizations" section, select the organization for which you would like to download security overview data.
  3. Under your organization name, click 
![Screenshot of the horizontal navigation bar for an organization. A tab, labeled with a shield icon and "Security," is outlined in dark orange.](https://docs.github.com/assets/cb-22170/images/help/organizations/organization-security-tab.png)
  4. In the "Security" sidebar, choose the page that you want to export data from by clicking on 
  5. Next to the search bar, click 
It may take a moment for GitHub to generate the CSV file of your data. Once the CSV file generates, the file will automatically start downloading, and a banner will appear confirming your report is ready. If you are downloading the CSV from the overview page, you will also receive an email when your report is ready, containing a link to download the CSV.


The summary views ("Overview", "Coverage" and "Risk") show data only for default alerts. Code scanning alerts from third-party tools, and secret scanning alerts for non-provider patterns or for ignored directories are all omitted from these views. Consequently, files exported from the summary views do not contain data for these types of alert.
## [Exporting overview, coverage, and risk data from your enterprise's security overview](https://docs.github.com/en/code-security/security-overview/exporting-data-from-security-overview#exporting-overview-coverage-and-risk-data-from-your-enterprises-security-overview)
  1. Navigate to GitHub Enterprise Cloud.
  2. In the top-right corner of GitHub, click your profile photo, then click **Your enterprises**.
  3. In the list of enterprises, click the enterprise you want to view.
  4. On the left side of the page, in the enterprise account sidebar, click 
  5. Choose the page that you want to export data from by clicking on **Overview** , **Risk** , or **Coverage**.
  6. Next to the search bar, click **Export CSV**.
It may take a moment for GitHub to generate the CSV file of your data. Once the CSV file generates, the file will automatically start downloading, and a banner will appear confirming your report is ready. If you are downloading the CSV from the overview page, you will also receive an email when your report is ready, containing a link to download the CSV.


