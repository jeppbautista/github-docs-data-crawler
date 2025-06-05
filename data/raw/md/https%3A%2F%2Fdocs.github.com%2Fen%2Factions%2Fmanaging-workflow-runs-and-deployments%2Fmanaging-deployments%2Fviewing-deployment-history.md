  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Manage workflows and deployments](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments "Manage workflows and deployments")/
  * [Manage deployments](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments "Manage deployments")/
  * [Deployment history](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/viewing-deployment-history "Deployment history")


# Viewing deployment history
View current and previous deployments for your repository.
## In this article
  * [About deployment history](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/viewing-deployment-history#about-deployment-history)
  * [Viewing your repository's deployment history](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/viewing-deployment-history#viewing-your-repositorys-deployment-history)


## [About deployment history](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/viewing-deployment-history#about-deployment-history)
You can deliver deployments through GitHub Actions and environments or with the REST API and third party apps. For more information about using environments to deploy with GitHub Actions, see [Managing environments for deployment](https://docs.github.com/en/actions/deployment/targeting-different-environments/managing-environments-for-deployment). For more information about deployments with the REST API, see [REST API endpoints for repositories](https://docs.github.com/en/rest/repos#deployments).
On the deployments page of your repository, you can view the following aspects of your deployments.
  * Currently active deployments across various environments
  * Deployments filtered by environment
  * Your repository's full deployment history
  * Associated commits that triggered the deployment
  * Connected GitHub Actions workflow logs
  * The deployment URL (if one exists)
  * The source pull request and branch related to each deployment
  * Deployment statuses. For more information about deployment statuses, see [REST API endpoints for deployments](https://docs.github.com/en/rest/deployments/deployments#about-deployments).


By default, the deployments page shows currently active deployments from select environments and a timeline of the latest deployments for all environments.
## [Viewing your repository's deployment history](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/viewing-deployment-history#viewing-your-repositorys-deployment-history)
  1. In the right-hand sidebar of the home page of your repository, click **Deployments**.
  2. Once you are on the "Deployments" page, you can view the following information about your deployment history. 
     * **To view recent deployments for a specific environment** , in the "Environments" section of the left sidebar, click an environment.
     * **To pin an environment to the top of the deployment history list** , repository administrators can click 
     * **To view the commit that triggered a deployment** , in the deployment history list, click the commit message for the deployment you want to view. 
Deployments from commits that originate from a fork outside of the repository will not show links to the source pull request and branch related to each deployment. For more information about forks, see [About forks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks).
     * **To view the URL for a deployment** , to the right of the commit message in the deployment history list, click 
     * **To navigate to the workflow run logs associated with a deployment** , to the right of the commit message in the deployment history list, click **View logs**.
  3. Optionally, to filter the deployment history list, create a filter. 
    1. Click on the 
    2. Click 
    3. Choose a qualifier you would like to filter the deployment history by.
    4. Depending on the qualifier you chose, fill out information in the "Operator" and "Value" columns.
    5. Optionally, click 
    6. Click **Apply**.


