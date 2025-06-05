  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners "Self-hosted runners")/
  * [Actions Runner Controller](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller "Actions Runner Controller")/
  * [Using ARC in a workflow](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/using-actions-runner-controller-runners-in-a-workflow "Using ARC in a workflow")


# Using Actions Runner Controller runners in a workflow
You can use Actions Runner Controller runners in a workflow file.
## In this article
  * [About using ARC runners in a workflow file](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/using-actions-runner-controller-runners-in-a-workflow#about-using-arc-runners-in-a-workflow-file)
  * [Using runner scale set names](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/using-actions-runner-controller-runners-in-a-workflow#using-runner-scale-set-names)
  * [Legal notice](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/using-actions-runner-controller-runners-in-a-workflow#legal-notice)


[Legal notice](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/using-actions-runner-controller-runners-in-a-workflow#legal-notice)
## [About using ARC runners in a workflow file](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/using-actions-runner-controller-runners-in-a-workflow#about-using-arc-runners-in-a-workflow-file)
To assign jobs to run on a runner scale set, you can specify the name of the scale set as the value for the `runs-on` key in your GitHub Actions workflow file.
For example, the following configuration for a runner scale set has the `INSTALLATION_NAME` value set to `arc-runner-set`.
```
# Using a Personal Access Token (PAT)
INSTALLATION_NAME="arc-runner-set"
NAMESPACE="arc-runners"
GITHUB_CONFIG_URL="https://github.com/<your_enterprise/org/repo>"
GITHUB_PAT="<PAT>"
helm install "${INSTALLATION_NAME}" \
    --namespace "${NAMESPACE}" \
    --create-namespace \
    --set githubConfigUrl="${GITHUB_CONFIG_URL}" \
    --set githubConfigSecret.github_token="${GITHUB_PAT}" \
    oci://ghcr.io/actions/actions-runner-controller-charts/gha-runner-scale-set

```

To use this configuration in a workflow, set the value of the `runs-on` key in your workflow to `arc-runner-set`, similar to the following example.
```
jobs:
  job_name:
    runs-on: arc-runner-set

```

## [Using runner scale set names](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/using-actions-runner-controller-runners-in-a-workflow#using-runner-scale-set-names)
Runner scale set names are unique within the runner group they belong to. To deploy multiple runner scale sets with the same name, they must belong to different runner groups. For more information about specifying runner scale set names, see [Deploying runner scale sets with Actions Runner Controller](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/deploying-runner-scale-sets-with-actions-runner-controller).
You cannot use additional labels to target runners created by ARC. You can only use the installation name of the runner scale set that you specified during the installation or by defining the value of the `runnerScaleSetName` field in your [`values.yaml`](https://github.com/actions/actions-runner-controller/blob/master/charts/gha-runner-scale-set/values.yaml) file. These are used as the 'single label' to use as your `runs-on` target. For more information, see [Deploying runner scale sets with Actions Runner Controller](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/deploying-runner-scale-sets-with-actions-runner-controller#scaling-runners).
## [Legal notice](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/using-actions-runner-controller-runners-in-a-workflow#legal-notice)
Portions have been adapted from <https://github.com/actions/actions-runner-controller/> under the Apache-2.0 license:
```
Copyright 2019 Moto Ishizawa

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

```

