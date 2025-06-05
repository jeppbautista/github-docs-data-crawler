  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secret scanning](https://docs.github.com/en/code-security/secret-scanning "Secret scanning")/
  * [Advanced features](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features "Advanced features")/
  * [Delegated bypass](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection "Delegated bypass")/
  * [Manage bypass requests](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/managing-requests-to-bypass-push-protection "Manage bypass requests")


# Managing requests to bypass push protection
As a member of the bypass list for an organization or repository, you can review bypass requests from other members of the organization or repository.
## Who can use this feature?
  * Organization owners
  * Security managers
  * Users in teams, default roles, or custom roles that have been added to the bypass list.
  * Users who are assigned a custom role with the "review and manage secret scanning bypass requests" fine-grained permission.


## In this article
  * [Managing requests to bypass push protection](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/managing-requests-to-bypass-push-protection#managing-requests-to-bypass-push-protection)
  * [Further reading](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/managing-requests-to-bypass-push-protection#further-reading)


## [Managing requests to bypass push protection](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/managing-requests-to-bypass-push-protection#managing-requests-to-bypass-push-protection)
When enabling delegated bypass for push protection, organization owners or repository administrators decide which individuals, roles or teams can review (approve or deny) requests to bypass push protection.
When a contributor requests bypass privileges to push a commit containing a secret, this designated group of reviewers:
  * Receives an email notification containing a link to the request.
  * Reviews the request in the "Bypass requests" page of the repository, or in the organization's security overview.
  * Has 7 days to either approve or deny the request before the request expires.


To help reviewers efficiently triage secrets for which there is a bypass request, GitHub displays the following information in the request:
  * Name of the user who attempted the push.
  * Repository where the push was attempted.
  * Commit hash of the push.
  * Timestamp of the push.
  * File path and branch information. The branch information is only available for pushes to single branches.


The contributor is notified of the decision by email and must take the required action:
  * If the request is approved, the contributor can push the commit containing the secret to the repository.
  * If the request is denied, the contributor must remove the secret from the commit in order to successfully push the commit to the repository.


### [Managing requests for a repository](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/managing-requests-to-bypass-push-protection#managing-requests-for-a-repository)
  1. On GitHub, navigate to the main page of the repository.
  2. Under the repository name, click **Security**. 
![Screenshot of a repository header showing the tabs. The "Security" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-17801/images/help/repository/security-tab.png)
  3. In the left sidebar, under "Requests," click **Push protection bypass**.
  4. Select the **All statuses** dropdown menu, then click **Open** to view requests that are awaiting review, and those that have been approved but for which the commits haven't been pushed to the repository yet.
  5. Click the request that you want to review.
  6. Review the details of the request.
  7. Optionally, add a review comment. The comment will be added to the review request timeline and the secret scanning alert timeline. For example, you may wish to explain the reason for the approval or denial of the request for auditing and reporting reasons, and suggest next steps for the contributor to take.
  8. To allow the contributor to push the commit containing the secret, click **Approve bypass request**. Or, to require the contributor to remove the secret from the commit, click **Deny bypass request**.


### [Managing requests for an organization](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/managing-requests-to-bypass-push-protection#managing-requests-for-an-organization)
Organization owners, security managers and organization members with the relevant fine-grained permission (via a custom role) can review and manage bypass requests for all repositories in the organization using security overview. See [Reviewing requests to bypass push protection](https://docs.github.com/en/code-security/security-overview/reviewing-requests-to-bypass-push-protection).
### [Filtering requests](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/managing-requests-to-bypass-push-protection#filtering-requests)
You can filter requests by:
  * Approver (member of the bypass list)
  * Requester (contributor making the request)
  * Timeframe
  * Status


#### [Filtering by status](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/managing-requests-to-bypass-push-protection#filtering-by-status)
The following statuses are assigned to a request:
Status | Description  
---|---  
`Cancelled` | The request has been canceled by the contributor.  
`Completed` | The request has been approved and the commit(s) have been pushed to the repository.  
`Denied` | The request has been reviewed and denied.  
`Expired` | The request has expired. Requests are valid for 7 days.  
`Open` | The request has either not yet been reviewed, or has been approved but the commit(s) have not been pushed to the repository.  
## [Further reading](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/managing-requests-to-bypass-push-protection#further-reading)
  * [About delegated bypass for push protection](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/about-delegated-bypass-for-push-protection)
  * [Enabling delegated bypass for push protection](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/enabling-delegated-bypass-for-push-protection)
  * [Reviewing requests to bypass push protection](https://docs.github.com/en/code-security/security-overview/reviewing-requests-to-bypass-push-protection)


