  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [About GitHub Actions](https://docs.github.com/en/actions/about-github-actions "About GitHub Actions")/
  * [Continuous deployment](https://docs.github.com/en/actions/about-github-actions/about-continuous-deployment-with-github-actions "Continuous deployment")


# About continuous deployment with GitHub Actions
You can create custom continuous deployment (CD) workflows directly in your GitHub repository with GitHub Actions.
## In this article
  * [About continuous deployment](https://docs.github.com/en/actions/about-github-actions/about-continuous-deployment-with-github-actions#about-continuous-deployment)
  * [About continuous deployment using GitHub Actions](https://docs.github.com/en/actions/about-github-actions/about-continuous-deployment-with-github-actions#about-continuous-deployment-using-github-actions)
  * [Using OpenID Connect to access cloud resources](https://docs.github.com/en/actions/about-github-actions/about-continuous-deployment-with-github-actions#using-openid-connect-to-access-cloud-resources)
  * [Workflow templates and third party actions](https://docs.github.com/en/actions/about-github-actions/about-continuous-deployment-with-github-actions#workflow-templates-and-third-party-actions)
  * [Further reading](https://docs.github.com/en/actions/about-github-actions/about-continuous-deployment-with-github-actions#further-reading)


## [About continuous deployment](https://docs.github.com/en/actions/about-github-actions/about-continuous-deployment-with-github-actions#about-continuous-deployment)
_Continuous deployment_ (CD) is the practice of using automation to publish and deploy software updates. As part of the typical CD process, the code is automatically built and tested before deployment.
Continuous deployment is often coupled with continuous integration. For more information about continuous integration, see [About continuous integration with GitHub Actions](https://docs.github.com/en/actions/automating-builds-and-tests/about-continuous-integration).
## [About continuous deployment using GitHub Actions](https://docs.github.com/en/actions/about-github-actions/about-continuous-deployment-with-github-actions#about-continuous-deployment-using-github-actions)
You can set up a GitHub Actions workflow to deploy your software product. To verify that your product works as expected, your workflow can build the code in your repository and run your tests before deploying.
You can configure your CD workflow to run when an event occurs (for example, when new code is pushed to the default branch of your repository), on a set schedule, manually, or when an external event occurs using the repository dispatch webhook. For more information about when your workflow can run, see [Events that trigger workflows](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows).
GitHub Actions provides features that give you more control over deployments. For example, you can use environments to require approval for a job to proceed, restrict which branches can trigger a workflow, or limit access to secrets. You can use concurrency to limit your CD pipeline to a maximum of one in-progress deployment and one pending deployment. For more information about these features, see [Deploying with GitHub Actions](https://docs.github.com/en/actions/deployment/about-deployments/deploying-with-github-actions) and [Managing environments for deployment](https://docs.github.com/en/actions/deployment/targeting-different-environments/managing-environments-for-deployment).
## [Using OpenID Connect to access cloud resources](https://docs.github.com/en/actions/about-github-actions/about-continuous-deployment-with-github-actions#using-openid-connect-to-access-cloud-resources)
If your GitHub Actions workflows need to access resources from a cloud provider that supports OpenID Connect (OIDC), you can configure your workflows to authenticate directly to the cloud provider. This will let you stop storing these credentials as long-lived secrets and provide other security benefits. For more information, see [About security hardening with OpenID Connect](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect).
## [Workflow templates and third party actions](https://docs.github.com/en/actions/about-github-actions/about-continuous-deployment-with-github-actions#workflow-templates-and-third-party-actions)
GitHub offers deployment workflow templates for several popular services, such as Azure Web App. To learn how to get started using a workflow template, see [Using workflow templates](https://docs.github.com/en/actions/learn-github-actions/using-starter-workflows) or [browse the full list of deployment workflow templates](https://github.com/actions/starter-workflows/tree/main/deployments). You can also check out our more detailed guides for specific deployment workflows, such as [Deploying Node.js to Azure App Service](https://docs.github.com/en/actions/deployment/deploying-to-your-cloud-provider/deploying-to-azure/deploying-nodejs-to-azure-app-service).
Many service providers also offer actions on GitHub Marketplace for deploying to their service. For the full list, see [GitHub Marketplace](https://github.com/marketplace?category=deployment&type=actions).
## [Further reading](https://docs.github.com/en/actions/about-github-actions/about-continuous-deployment-with-github-actions#further-reading)
  * [Deploying](https://docs.github.com/en/actions/use-cases-and-examples/deploying)
  * [Deploying with GitHub Actions](https://docs.github.com/en/actions/deployment/about-deployments/deploying-with-github-actions)
  * [Managing environments for deployment](https://docs.github.com/en/actions/deployment/targeting-different-environments/managing-environments-for-deployment)
  * [Managing billing for GitHub Actions](https://docs.github.com/en/billing/managing-billing-for-github-actions)


