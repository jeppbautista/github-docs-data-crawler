  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Security overview](https://docs.github.com/en/code-security/security-overview "Security overview")/
  * [Review bypass requests](https://docs.github.com/en/code-security/security-overview/reviewing-requests-to-bypass-push-protection "Review bypass requests")


# Reviewing requests to bypass push protection
You can use security overview to review requests to bypass push protection from contributors pushing to repositories across your organization.
## Who can use this feature?
Access requires:
  * Organization views: **write** access to repositories in the organization
  * Enterprise views: organization owners and security managers


Organizations owned by a GitHub Team account with GitHub Secret Protection, or owned by a GitHub Enterprise account
## In this article
  * [About bypass requests](https://docs.github.com/en/code-security/security-overview/reviewing-requests-to-bypass-push-protection#about-bypass-requests)
  * [Reviewing bypass requests for an organization](https://docs.github.com/en/code-security/security-overview/reviewing-requests-to-bypass-push-protection#reviewing-bypass-requests-for-an-organization)
  * [Filtering requests](https://docs.github.com/en/code-security/security-overview/reviewing-requests-to-bypass-push-protection#filtering-requests)
  * [Further reading](https://docs.github.com/en/code-security/security-overview/reviewing-requests-to-bypass-push-protection#further-reading)


## [About bypass requests](https://docs.github.com/en/code-security/security-overview/reviewing-requests-to-bypass-push-protection#about-bypass-requests)
If your organization has configured delegated bypass for push protection, a designated team of reviewers controls which organization members can push secrets to repositories in your organization, and which members must first make a "bypass request" in order to push the secret.
On the "Push protection bypass" page in security overview, reviewers can find, review (approve or deny) and manage these requests.
For more information, see [Managing requests to bypass push protection](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/managing-requests-to-bypass-push-protection).
## [Reviewing bypass requests for an organization](https://docs.github.com/en/code-security/security-overview/reviewing-requests-to-bypass-push-protection#reviewing-bypass-requests-for-an-organization)
  1. On GitHub, navigate to the main page of the organization.
  2. Under your organization name, click 
![Screenshot of the horizontal navigation bar for an organization. A tab, labeled with a shield icon and "Security," is outlined in dark orange.](https://docs.github.com/assets/cb-22170/images/help/organizations/organization-security-tab.png)
  3. In the sidebar, under "Requests", click 
  4. Select the **All statuses** dropdown menu, then click **Open** to view requests that are awaiting review, or that have been approved but for which the commits haven't been pushed to the repository yet.
  5. Click the request that you want to review.
  6. Review the details of the request.
  7. Optionally, add a review comment. The comment will be added to the review request timeline and the secret scanning alert timeline. For example, you may wish to explain the reason for the approval or denial of the request for auditing and reporting reasons, and suggest next steps for the contributor to take.
  8. To allow the contributor to push the commit containing the secret, click **Approve bypass request**. Or, to require the contributor to remove the secret from the commit, click **Deny bypass request**.


## [Filtering requests](https://docs.github.com/en/code-security/security-overview/reviewing-requests-to-bypass-push-protection#filtering-requests)
You can filter requests by repository, approver (member who has reviewed the request), requester (contributor making the request), timeframe, and status.
### [Filtering by status](https://docs.github.com/en/code-security/security-overview/reviewing-requests-to-bypass-push-protection#filtering-by-status)
The following statuses are assigned to a request:
Status | Description  
---|---  
`Cancelled` | The request has been cancelled by the contributor.  
`Completed` | The request has been approved and the commit(s) have been pushed to the repository.  
`Denied` | The request has been reviewed and denied.  
`Expired` | The request has expired. Requests are valid for 7 days.  
`Open` | The request has either not yet been reviewed, or has been approved but the commit(s) have not been pushed to the repository.  
## [Further reading](https://docs.github.com/en/code-security/security-overview/reviewing-requests-to-bypass-push-protection#further-reading)
  * [About delegated bypass for push protection](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/about-delegated-bypass-for-push-protection)
  * [Enabling delegated bypass for push protection](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/enabling-delegated-bypass-for-push-protection)


