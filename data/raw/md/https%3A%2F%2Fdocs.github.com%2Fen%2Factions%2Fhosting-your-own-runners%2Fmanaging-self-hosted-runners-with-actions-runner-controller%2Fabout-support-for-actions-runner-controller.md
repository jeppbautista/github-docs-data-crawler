  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners "Self-hosted runners")/
  * [Actions Runner Controller](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller "Actions Runner Controller")/
  * [About Support for ARC](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/about-support-for-actions-runner-controller "About Support for ARC")


# About support for Actions Runner Controller
What to know before you [contact GitHub Support](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/support/contacting-github-support) for assistance with Actions Runner Controller.
## In this article
  * [About support for Actions Runner Controller Versions](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/about-support-for-actions-runner-controller#about-support-for-actions-runner-controller-versions)
  * [Scope of support for Actions Runner Controller](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/about-support-for-actions-runner-controller#scope-of-support-for-actions-runner-controller)
  * [Working with GitHub Support for Actions Runner Controller](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/about-support-for-actions-runner-controller#working-with-github-support-for-actions-runner-controller)


You can [contact GitHub Support](https://docs.github.com/en/support/contacting-github-support) for assistance with Actions Runner Controller.
## [About support for Actions Runner Controller Versions](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/about-support-for-actions-runner-controller#about-support-for-actions-runner-controller-versions)
The Actions Runner Controller (ARC) project [was adopted by GitHub](https://github.com/actions/actions-runner-controller/discussions/2072) to release as a new GitHub product. As a result, there are currently two ARC releases: the legacy community-maintained ARC and GitHub's Autoscaling Runner Sets.
GitHub only supports the latest Autoscaling Runner Sets version of ARC. Support for the legacy ARC is provided by the community in the [Actions Runner Controller](https://github.com/actions/actions-runner-controller) repository only.
## [Scope of support for Actions Runner Controller](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/about-support-for-actions-runner-controller#scope-of-support-for-actions-runner-controller)
If your support request is outside of the scope of what our team can help you with, we may recommend next steps to resolve your issue outside of GitHub Support. Your support request is possibly out of GitHub Support's scope if the request is primarily about:
  * The legacy community-maintained version of ARC
  * Installing, configuring, or maintaining dependencies
  * Template spec customization
  * Container orchestration, such as Kubernetes setup, networking, building images in ARC (DinD), etc.
  * Applying Kubernetes policies
  * Managed Kubernetes providers or provider-specific configurations
  * [Runner Container Hooks](https://github.com/actions/runner-container-hooks) in conjunction with ARC's `kubernetes` mode
  * Installation tooling other than Helm
  * Storage provisioners and PersistentVolumeClaims (PVCs)
  * Best practices, such as configuring metrics servers, image caching, etc.


While ARC may be deployed successfully with different tooling and configurations, your support request is possibly out of GitHub Support's scope if ARC has been deployed with:
  * Installation tooling other than Helm
  * Service account and/or template spec customization


If you're uncertain if the issue is out of scope, open a ticket and we're happy to help you determine the best way to proceed.
For more information about contacting GitHub Support, see [Contacting GitHub Support](https://docs.github.com/en/support/contacting-github-support).
  * OpenShift clusters are currently unsupported.
  * ARC is only supported on GitHub Enterprise Server versions 3.9 and greater.


## [Working with GitHub Support for Actions Runner Controller](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/about-support-for-actions-runner-controller#working-with-github-support-for-actions-runner-controller)
GitHub Support may ask questions about your Actions Runner Controller deployment and request that you collect and attach the [controller, listener](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/troubleshooting-actions-runner-controller-errors#checking-the-logs-of-the-controller-and-runner-set-listener), and runner logs to the support ticket.
