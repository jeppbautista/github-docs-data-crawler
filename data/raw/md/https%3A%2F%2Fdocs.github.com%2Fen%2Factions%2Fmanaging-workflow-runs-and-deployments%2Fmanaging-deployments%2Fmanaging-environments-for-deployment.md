  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Manage workflows and deployments](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments "Manage workflows and deployments")/
  * [Manage deployments](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments "Manage deployments")/
  * [Manage environments](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment "Manage environments")


# Managing environments for deployment
You can create environments and secure those environments with deployment protection rules. A job that references an environment must follow any protection rules for the environment before running or accessing the environment's secrets.
## Who can use this feature?
Repository owners
Environments, environment secrets, and deployment protection rules are available in public repositories for all current GitHub plans. They are not available on legacy plans, such as Bronze, Silver, or Gold. For access to environments, environment secrets, and deployment branches in private or internal repositories, you must use GitHub Pro, GitHub Team, or GitHub Enterprise. If you are on a GitHub Free, GitHub Pro, or GitHub Team plan, other deployment protection rules, such as a wait timer or required reviewers, are only available for public repositories.
## In this article
  * [About environments](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#about-environments)
  * [Deployment protection rules](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#deployment-protection-rules)
  * [Environment secrets](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#environment-secrets)
  * [Environment variables](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#environment-variables)
  * [Creating an environment](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#creating-an-environment)
  * [Deleting an environment](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#deleting-an-environment)
  * [How environments relate to deployments](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#how-environments-relate-to-deployments)
  * [Next steps](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#next-steps)


## [About environments](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#about-environments)
Environments are used to describe a general deployment target like `production`, `staging`, or `development`. When a GitHub Actions workflow deploys to an environment, the environment is displayed on the main page of the repository. For more information about viewing deployments to environments, see [Viewing deployment history](https://docs.github.com/en/actions/deployment/managing-your-deployments/viewing-deployment-history).
You can configure environments with protection rules and secrets. When a workflow job references an environment, the job won't start until all of the environment's protection rules pass. A job also cannot access secrets that are defined in an environment until all the deployment protection rules pass.
Optionally, you can bypass an environment's protection rules and force all pending jobs referencing the environment to proceed. For more information, see [Reviewing deployments](https://docs.github.com/en/actions/managing-workflow-runs/reviewing-deployments#bypassing-environment-protection-rules).
Users with GitHub Free plans can only configure environments for public repositories. If you convert a repository from public to private, any configured protection rules or environment secrets will be ignored, and you will not be able to configure any environments. If you convert your repository back to public, you will have access to any previously configured protection rules and environment secrets.
Organizations with GitHub Team and users with GitHub Pro can configure environments for private repositories. For more information, see [GitHub’s plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans).
## [Deployment protection rules](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#deployment-protection-rules)
Deployment protection rules require specific conditions to pass before a job referencing the environment can proceed. You can use deployment protection rules to require a manual approval, delay a job, or restrict the environment to certain branches. You can also create and implement custom protection rules powered by GitHub Apps to use third-party systems to control deployments referencing environments configured on GitHub.
Third-party systems can be observability systems, change management systems, code quality systems, or other manual configurations that you use to assess readiness before deployments are safely rolled out to environments.
Any number of GitHub Apps-based deployment protection rules can be installed on a repository. However, a maximum of 6 deployment protection rules can be enabled on any environment at the same time.
### [Required reviewers](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#required-reviewers)
Use required reviewers to require a specific person or team to approve workflow jobs that reference the environment. You can list up to six users or teams as reviewers. The reviewers must have at least read access to the repository. Only one of the required reviewers needs to approve the job for it to proceed.
You also have the option to prevent self-reviews for deployments to protected environments. If you enable this setting, users who initiate a deployment cannot approve the deployment job, even if they are a required reviewer. This ensures that deployments to protected environments are always reviewed by more than one person.
For more information on reviewing jobs that reference an environment with required reviewers, see [Reviewing deployments](https://docs.github.com/en/actions/managing-workflow-runs/reviewing-deployments).
If you are on a GitHub Free, GitHub Pro, or GitHub Team plan, required reviewers are only available for public repositories.
### [Wait timer](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#wait-timer)
Use a wait timer to delay a job for a specific amount of time after the job is initially triggered. The time (in minutes) must be an integer between 1 and 43,200 (30 days). Wait time will not count towards your billable time.
If you are on a GitHub Free, GitHub Pro, or GitHub Team plan, wait timers are only available for public repositories.
### [Deployment branches and tags](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#deployment-branches-and-tags)
Use deployment branches and tags to restrict which branches and tags can deploy to the environment. Below are the options for deployment branches and tags for an environment:
  * **No restriction:** No restriction on which branch or tag can deploy to the environment.
  * **Protected branches only:** Only branches with branch protection rules enabled can deploy to the environment. If no branch protection rules are defined for any branch in the repository, then all branches can deploy. For more information about branch protection rules, see [About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
Deployment workflow runs triggered by tags with the same name as a protected branch and forks with branches that match the protected branch name cannot deploy to the environment.
  * **Selected branches and tags:** Only branches and tags that match your specified name patterns can deploy to the environment.
If you specify `releases/*` as a deployment branch or tag rule, only a branch or tag whose name begins with `releases/` can deploy to the environment. (Wildcard characters will not match `/`. To match branches or tags that begin with `release/` and contain an additional single slash, use `release/*/*`.) If you add `main` as a branch rule, a branch named `main` can also deploy to the environment. For more information about syntax options for deployment branches, see the [Ruby `File.fnmatch` documentation](https://ruby-doc.org/core-2.5.1/File.html#method-c-fnmatch).
Name patterns must be configured for branches or tags individually.


Deployment branches and tags are available for all public repositories. For users on GitHub Pro or GitHub Team plans, deployment branches and tags are also available for private repositories.
### [Allow administrators to bypass configured protection rules](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#allow-administrators-to-bypass-configured-protection-rules)
By default, administrators can bypass the protection rules and force deployments to specific environments. For more information, see [Reviewing deployments](https://docs.github.com/en/actions/managing-workflow-runs/reviewing-deployments#bypassing-environment-protection-rules).
Alternatively, you can configure environments to disallow bypassing the protection rules for all deployments to the environment.
Allowing administrators to bypass protection rules is only available for public repositories for users on GitHub Free, GitHub Pro, and GitHub Team plans.
### [Custom deployment protection rules](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#custom-deployment-protection-rules)
Custom deployment protection rules are currently in public preview and subject to change.
You can enable your own custom protection rules to gate deployments with third-party services. For example, you can use services such as Datadog, Honeycomb, and ServiceNow to provide automated approvals for deployments to GitHub. For more information, see [Creating custom deployment protection rules](https://docs.github.com/en/actions/deployment/protecting-deployments/creating-custom-deployment-protection-rules).
Once custom deployment protection rules have been created and installed on a repository, you can enable the custom deployment protection rule for any environment in the repository. For more information about configuring and enabling custom deployment protection rules, see [Configuring custom deployment protection rules](https://docs.github.com/en/actions/deployment/protecting-deployments/configuring-custom-deployment-protection-rules).
Custom deployment protection rules are only available for public repositories for users on GitHub Free, GitHub Pro, and GitHub Team plans.
## [Environment secrets](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#environment-secrets)
Secrets stored in an environment are only available to workflow jobs that reference the environment. If the environment requires approval, a job cannot access environment secrets until one of the required reviewers approves it. For more information about secrets, see [About secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/about-secrets).
  * Workflows that run on self-hosted runners are not run in an isolated container, even if they use environments. Environment secrets should be treated with the same level of security as repository and organization secrets. For more information, see [Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions#hardening-for-self-hosted-runners).
  * If you are using GitHub Free, environment secrets are only available in public repositories. For access to environment secrets in private or internal repositories, you must use GitHub Pro, GitHub Team, or GitHub Enterprise. For more information on switching your plan, see [Upgrading your account's plan](https://docs.github.com/en/billing/managing-the-plan-for-your-github-account/upgrading-your-accounts-plan).


## [Environment variables](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#environment-variables)
Variables stored in an environment are only available to workflow jobs that reference the environment. These variables are only accessible using the [`vars`](https://docs.github.com/en/actions/learn-github-actions/contexts#vars-context) context. For more information, see [Store information in variables](https://docs.github.com/en/actions/learn-github-actions/variables).
Environment variables are available for all public repositories. For users on GitHub Pro or GitHub Team plans, environment variables are also available for private repositories.
## [Creating an environment](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#creating-an-environment)
To configure an environment in a personal account repository, you must be the repository owner. To configure an environment in an organization repository, you must have `admin` access.
  * Creation of an environment in a private repository is available to organizations with GitHub Team and users with GitHub Pro.
  * Some features for environments have no or limited availability for private repositories. If you are unable to access a feature described in the instructions below, please see the documentation linked in the related step for availability information.


  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the left sidebar, click **Environments**.
  4. Click **New environment**.
  5. Enter a name for the environment, then click **Configure environment**. Environment names are not case sensitive. An environment name may not exceed 255 characters and must be unique within the repository.
  6. Optionally, specify people or teams that must approve workflow jobs that use this environment. For more information, see [Required reviewers](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#required-reviewers).
    1. Select **Required reviewers**.
    2. Enter up to 6 people or teams. Only one of the required reviewers needs to approve the job for it to proceed.
    3. Optionally, to prevent users from approving workflows runs that they triggered, select **Prevent self-review**.
    4. Click **Save protection rules**.
  7. Optionally, specify the amount of time to wait before allowing workflow jobs that use this environment to proceed. For more information, see [Wait timer](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#wait-timer).
    1. Select **Wait timer**.
    2. Enter the number of minutes to wait.
    3. Click **Save protection rules**.
  8. Optionally, disallow bypassing configured protection rules. For more information, see [Allow administrators to bypass configured protection rules](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#allow-administrators-to-bypass-configured-protection-rules).
    1. Deselect **Allow administrators to bypass configured protection rules**.
    2. Click **Save protection rules**.
  9. Optionally, enable any custom deployment protection rules that have been created with GitHub Apps. For more information, see [Custom deployment protection rules](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#custom-deployment-protection-rules).
    1. Select the custom protection rule you want to enable.
    2. Click **Save protection rules**.
  10. Optionally, specify what branches and tags can deploy to this environment. For more information, see [Deployment branches and tags](https://docs.github.com/en/actions/deployment/targeting-different-environments/managing-environments-for-deployment#deployment-branches-and-tags).
    1. Select the desired option in the **Deployment branches** dropdown.
    2. If you chose **Selected branches and tags** , to add a new rule, click **Add deployment branch or tag rule**
    3. In the "Ref type" dropdown menu, depending on what rule you want to apply, click 
    4. Enter the name pattern for the branch or tag that you want to allow.
Name patterns must be configured for branches or tags individually.
    5. Click **Add rule**.
  11. Optionally, add environment secrets. These secrets are only available to workflow jobs that use the environment. Additionally, workflow jobs that use this environment can only access these secrets after any configured rules (for example, required reviewers) pass. For more information, see [Environment secrets](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#environment-secrets).
    1. Under **Environment secrets** , click **Add Secret**.
    2. Enter the secret name.
    3. Enter the secret value.
    4. Click **Add secret**.
  12. Optionally, add environment variables. These variables are only available to workflow jobs that use the environment, and are only accessible using the [`vars`](https://docs.github.com/en/actions/learn-github-actions/contexts#vars-context) context. For more information, see [Environment variables](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#environment-variables).
    1. Under **Environment variables** , click **Add Variable**.
    2. Enter the variable name.
    3. Enter the variable value.
    4. Click **Add variable**.


You can also create and configure environments through the REST API. For more information, see [REST API endpoints for deployment environments](https://docs.github.com/en/rest/deployments/environments), [REST API endpoints for GitHub Actions Secrets](https://docs.github.com/en/rest/actions/secrets), [REST API endpoints for GitHub Actions variables](https://docs.github.com/en/rest/actions/variables), and [REST API endpoints for deployment branch policies](https://docs.github.com/en/rest/deployments/branch-policies).
Running a workflow that references an environment that does not exist will create an environment with the referenced name. If the environment is created from running implicit page builds (for example, from a branch or folder source), the source branch will be added as a protection rule to the environment. Otherwise, the newly created environment will not have any protection rules or secrets configured. Anyone that can edit workflows in the repository can create environments via a workflow file, but only repository admins can configure the environment.
## [Deleting an environment](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#deleting-an-environment)
To configure an environment in a personal account repository, you must be the repository owner. To configure an environment in an organization repository, you must have `admin` access.
Deleting an environment will delete all secrets and protection rules associated with the environment. Any jobs currently waiting because of protection rules from the deleted environment will automatically fail.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the left sidebar, click **Environments**.
  4. Next to the environment that you want to delete, click 
  5. Click **I understand, delete this environment**.


You can also delete environments through the REST API. For more information, see [REST API endpoints for repositories](https://docs.github.com/en/rest/repos#environments).
## [How environments relate to deployments](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#how-environments-relate-to-deployments)
When a workflow job that references an environment runs, it creates a deployment object with the `environment` property set to the name of your environment. As the workflow progresses, it also creates deployment status objects with the `environment` property set to the name of your environment, the `environment_url` property set to the URL for environment (if specified in the workflow), and the `state` property set to the status of the job.
You can access these objects through the REST API or GraphQL API. You can also subscribe to these webhook events. For more information, see [REST API endpoints for repositories](https://docs.github.com/en/rest/repos#deployments), [Objects](https://docs.github.com/en/graphql/reference/objects#deployment) (GraphQL API), or [Webhook events and payloads](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#deployment).
## [Next steps](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#next-steps)
GitHub Actions provides several features for managing your deployments. For more information, see [Deploying with GitHub Actions](https://docs.github.com/en/actions/deployment/about-deployments/deploying-with-github-actions).
