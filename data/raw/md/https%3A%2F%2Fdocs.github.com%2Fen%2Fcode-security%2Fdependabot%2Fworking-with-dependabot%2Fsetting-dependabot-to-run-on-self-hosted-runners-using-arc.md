  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Dependabot](https://docs.github.com/en/code-security/dependabot "Dependabot")/
  * [Work with Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot "Work with Dependabot")/
  * [Configure ARC](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-self-hosted-runners-using-arc "Configure ARC")


# Setting up Dependabot to run on self-hosted action runners using the Actions Runner Controller
You can configure the Actions Runner Controller to run Dependabot on self-hosted runners.
## Who can use this feature?
Users with **write** access
## In this article
  * [Working with the Actions Runner Controller (ARC)](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-self-hosted-runners-using-arc#working-with-the-actions-runner-controller-arc)
  * [What is ARC?](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-self-hosted-runners-using-arc#what-is-arc)
  * [Dependabot on ARC](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-self-hosted-runners-using-arc#dependabot-on-arc)
  * [Setting up ARC for Dependabot on your Local environment](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-self-hosted-runners-using-arc#setting-up-arc-for-dependabot-on-your-local-environment)
  * [Triggering a Dependabot run](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-self-hosted-runners-using-arc#triggering-a-dependabot-run)
  * [Viewing the generated ARC runners](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-self-hosted-runners-using-arc#viewing-the-generated-arc-runners)


## [Working with the Actions Runner Controller (ARC)](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-self-hosted-runners-using-arc#working-with-the-actions-runner-controller-arc)
This article provides step-by-step instructions for setting up ARC on a Kubernetes cluster and configuring Dependabot to run on self-hosted action runners. The article:
  * Contains an overview of the ARC and Dependabot integration.
  * Provides detailed installation and configuration steps using helm scripts.


## [What is ARC?](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-self-hosted-runners-using-arc#what-is-arc)
The Actions Runner Controller is a Kubernetes controller that manages self-hosted GitHub Actions as Kubernetes pods. It allows you to dynamically scale and orchestrate runners based on your workflows, providing better resource utilization and integration with Kubernetes environments. See [About Actions Runner Controller](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/about-actions-runner-controller).
## [Dependabot on ARC](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-self-hosted-runners-using-arc#dependabot-on-arc)
You can run Dependabot on self-hosted GitHub Actions runners managed within a Kubernetes cluster via ARC. This enables auto-scaling, workload isolation, and better resource management for Dependabot jobs, ensuring that dependency updates can run efficiently within an organization's controlled infrastructure while integrating seamlessly with GitHub Actions.
## [Setting up ARC for Dependabot on your Local environment](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-self-hosted-runners-using-arc#setting-up-arc-for-dependabot-on-your-local-environment)
### [Prerequisites](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-self-hosted-runners-using-arc#prerequisites)
  * A Kubernetes cluster 
    * For a managed cloud environment, you can use Azure Kubernetes Service (AKS).
    * For a local setup, you can use minikube.
  * Helm 
    * A package manager for Kubernetes.


### [Setting up ARC](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-self-hosted-runners-using-arc#setting-up-arc)
  1. Install ARC. For more information, see [Quickstart for Actions Runner Controller](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/quickstart-for-actions-runner-controller).
  2. Create a work directory for the ARC setup and create a shell script file (for example, `helm_install_arc.sh`) to install the latest ARC version.
Bash```
    mkdir ARC
    touch helm_install_arc.sh
    chmod 755 helm_install_arc.sh

```
```
    mkdir ARC
    touch helm_install_arc.sh
    chmod 755 helm_install_arc.sh

```

  3. Edit `helm_install_arc.sh` with this bash script for installing ARC.
Text```
NAMESPACE="arc-systems"
helm install arc \
    --namespace "${NAMESPACE}" \
    --create-namespace \
    oci://ghcr.io/actions/actions-runner-controller-charts/gha-runner-scale-set-controller

```
```
NAMESPACE="arc-systems"
helm install arc \
    --namespace "${NAMESPACE}" \
    --create-namespace \
    oci://ghcr.io/actions/actions-runner-controller-charts/gha-runner-scale-set-controller

```

  4. Execute the `helm_install_arc.sh` script file.
```
./helm_install_arc.sh

```

  5. Now, you need to configure the runner scale set. For this, let's start by creating and editing a file with the following bash script.
Bash```
touch arc-runner-set.sh
chmod 755 arc-runner-set.sh

```
```
touch arc-runner-set.sh
chmod 755 arc-runner-set.sh

```

Text```
INSTALLATION_NAME="dependabot"
NAMESPACE="arc-runners"
GITHUB_CONFIG_URL=REPO_URL
GITHUB_PAT=PAT
helm install "${INSTALLATION_NAME}" \
    --namespace "${NAMESPACE}" \
    --create-namespace \
    --set githubConfigUrl="${GITHUB_CONFIG_URL}" \
    --set githubConfigSecret.github_token="${GITHUB_PAT}" \
    --set containerMode.type="dind" \
    oci://ghcr.io/actions/actions-runner-controller-charts/gha-runner-scale-set

```
```
INSTALLATION_NAME="dependabot"
NAMESPACE="arc-runners"
GITHUB_CONFIG_URL=REPO_URL
GITHUB_PAT=PAT
helm install "${INSTALLATION_NAME}" \
    --namespace "${NAMESPACE}" \
    --create-namespace \
    --set githubConfigUrl="${GITHUB_CONFIG_URL}" \
    --set githubConfigSecret.github_token="${GITHUB_PAT}" \
    --set containerMode.type="dind" \
    oci://ghcr.io/actions/actions-runner-controller-charts/gha-runner-scale-set

```

  6. Execute the `arc-runner-set.sh` script file.
Bash```
./arc-runner-set.sh

```
```
./arc-runner-set.sh

```



  * The installation name of the runner scale set has to be `dependabot` in order to target the dependabot job to the runner.
  * The `containerMode.type="dind"` configuration is required to allow the runner to connect to the Docker daemon.
  * If an organization-level or enterprise-level runner is created, then the appropriate scopes should be provided to the Personal Access Token (PAT).
  * A personal access token (classic) (PAT) can be created. The token should have the following scopes based on whether you are creating a repository, organization or enterprise level runner scale set. 
    * Repository level: **repo**
    * Organization level: **admin:org**
    * Enterprise level: **admin:enterprise**  
For information about creating a personal access token (classic), see [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic).


### [Adding runner groups](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-self-hosted-runners-using-arc#adding-runner-groups)
Runner groups are used to control which organizations or repositories have access to runner scale sets. To add a runner scale set to a runner group, you must already have a runner group created.
For information about creating runner groups, see [Managing access to self-hosted runners using groups](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups#creating-a-self-hosted-runner-group-for-an-organization).
Don't forget to add the following setting to the runner scale set configuration in the helm chart.
Text```
--set runnerGroup="<Runner group name>" \

```
```
--set runnerGroup="<Runner group name>" \

```

### [Checking your installation](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-self-hosted-runners-using-arc#checking-your-installation)
  1. Check your installation.
Bash```
helm list -A

```
```
helm list -A

```

Output:
```
➜  ARC git:(master) ✗ helm list -A
    NAME           NAMESPACE   REVISION UPDATED                              STATUS   CHART                                  APP VERSION
    arc            arc-systems 1        2025-04-11 14:41:53.70893 -0500 CDT  deployed gha-runner-scale-set-controller-0.11.0 0.11.0
    arc-runner-set arc-runners 1        2025-04-11 15:08:12.58119 -0500 CDT  deployed gha-runner-scale-set-0.11.0            0.11.0
    dependabot     arc-runners 1        2025-04-16 21:53:40.080772 -0500 CDT deployed gha-runner-scale-set-0.11.0

```

  2. Check the manager pod using this command.
Bash```
kubectl get pods -n arc-systems

```
```
kubectl get pods -n arc-systems

```

Output:
```
➜  ARC git:(master) ✗ kubectl get pods -n arc-systems

NAME                                    READY   STATUS    RESTARTS      AGE
arc-gha-rs-controller-57c67d4c7-zjmw2   1/1     Running   8 (36h ago)   6d9h
arc-runner-set-754b578d-listener        1/1     Running   0             11h
dependabot-754b578d-listener            1/1     Running   0             14h

```



### [Setting up Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-self-hosted-runners-using-arc#setting-up-dependabot)
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Security" section of the sidebar, click 
  4. Under "Dependabot", scroll to "Dependabot on Action Runners", and select **Enable** for "Dependabot on self-hosted runners".


## [Triggering a Dependabot run](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-self-hosted-runners-using-arc#triggering-a-dependabot-run)
Now that you've set up ARC, you can start a Dependabot run.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click the 
  3. In the left sidebar, click **Dependency graph**. 
![Screenshot of the "Dependency graph" tab. The tab is highlighted with an orange outline.](https://docs.github.com/assets/cb-3959/images/help/graphs/graphs-sidebar-dependency-graph.png)
  4. Under "Dependency graph", click **Dependabot**.
  5. To the right of the name of manifest file you're interested in, click **Recent update jobs**.
  6. If there are no recent update jobs for the manifest file, click **Check for updates** to re-run a Dependabot version updates'job and check for new updates to dependencies for that ecosystem.


## [Viewing the generated ARC runners](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/setting-dependabot-to-run-on-self-hosted-runners-using-arc#viewing-the-generated-arc-runners)
You can view the ARC runners that have been created for the Dependabot job.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click 
![Screenshot of the tabs for the "github/docs" repository. The "Actions" tab is highlighted with an orange outline.](https://docs.github.com/assets/cb-12958/images/help/repository/actions-tab-global-nav-update.png)
  3. On the left sidebar, click **Runners**.
  4. Under "Runners", click **Self-hosted runners** to view the list of all the runners available in the repository. You can see the ephemeral dependabot runner that has been created. 
![Screenshot showing a dependabot runner in the list of available runners. The runner is highlighted with an orange outline.](https://docs.github.com/assets/cb-71012/images/help/dependabot/dependabot-self-hosted-runner.png)
You can also view the same dependabot runner pod created in your kubernetes cluster from the terminal by executing this command.
Text```
➜  ARC git:(master) ✗ kubectl get pods -n arc-runners
    NAME                            READY   STATUS    RESTARTS   AGE
    dependabot-sw8zn-runner-4mbc7   2/2     Running   0          46s

```
```
➜  ARC git:(master) ✗ kubectl get pods -n arc-runners
    NAME                            READY   STATUS    RESTARTS   AGE
    dependabot-sw8zn-runner-4mbc7   2/2     Running   0          46s

```



Additionally, you can verify:
  * The logs, by checking the runner and machine name. See [Viewing Dependabot job logs](https://docs.github.com/en/code-security/dependabot/troubleshooting-dependabot/viewing-dependabot-job-logs).
![Example of log for a dependabot self hosted runner.](https://docs.github.com/assets/cb-1020027/images/help/dependabot/dependabot-self-hosted-runner-log.png)
  * The version update pull requests created by the dependabot job in the **Pull requests** tab of the repository.


