  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners "Self-hosted runners")/
  * [Manage self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners "Manage self-hosted runners")/
  * [Label runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/using-labels-with-self-hosted-runners "Label runners")


# Using labels with self-hosted runners
You can use labels to organize your self-hosted runners based on their characteristics.
## In this article
  * [Creating a custom label](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/using-labels-with-self-hosted-runners#creating-a-custom-label)
  * [Assigning a label to a self-hosted runner](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/using-labels-with-self-hosted-runners#assigning-a-label-to-a-self-hosted-runner)
  * [Removing a custom label from a self-hosted runner](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/using-labels-with-self-hosted-runners#removing-a-custom-label-from-a-self-hosted-runner)
  * [Programmatically assign labels](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/using-labels-with-self-hosted-runners#programmatically-assign-labels)


For information on how to use labels to route jobs to specific types of self-hosted runners, see [Using self-hosted runners in a workflow](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/using-self-hosted-runners-in-a-workflow). You can also route jobs to runners in a specific group. For more information, see [Choosing the runner for a job](https://docs.github.com/en/actions/using-jobs/choosing-the-runner-for-a-job#targeting-runners-in-a-group).
A self-hosted runner can be located in either your repository, organization, or enterprise account settings on GitHub. To manage a self-hosted runner, you must have the following permissions, depending on where the self-hosted runner was added:
  * **User repository:** You must be the repository owner.
  * **Organization:** You must be an organization owner.
  * **Organization repository:** You must be an organization owner, or have admin access to the repository.


Actions Runner Controller does not support multiple labels, to find out more please read our [Actions Runner Controller documentation](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/about-actions-runner-controller#using-arc-runners-in-a-workflow)
## [Creating a custom label](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/using-labels-with-self-hosted-runners#creating-a-custom-label)
You can create custom labels for runners at the repository and organization levels.
  * [Creating a custom label for a repository runner](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/using-labels-with-self-hosted-runners#creating-a-custom-label-for-a-repository-runner)
  * [Creating a custom label for an organization runner](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/using-labels-with-self-hosted-runners#creating-a-custom-label-for-an-organization-runner)


Labels are case-insensitive.
### [Creating a custom label for a repository runner](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/using-labels-with-self-hosted-runners#creating-a-custom-label-for-a-repository-runner)
  1. Navigate to the main page of the repository where your self-hosted runner group is registered.
  2. Click 
  3. In the left sidebar, click **Runners**.
  4. In the list of runners, click on the name of the runner you'd like to configure.
  5. In the "Labels" section, click 
  6. In the "Find or create a label" field, type the name of your new label and click **Create new label**. The custom label is created and assigned to the self-hosted runner. Custom labels can be removed from self-hosted runners, but they currently can't be manually deleted. Any unused labels that are not assigned to a runner will be automatically deleted within 24 hours.


### [Creating a custom label for an organization runner](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/using-labels-with-self-hosted-runners#creating-a-custom-label-for-an-organization-runner)
  1. Navigate to the main page of the organization where your self-hosted runner group is registered.
  2. Click 
  3. In the left sidebar, click **Runners**.
  4. In the list of runners, click on the name of the runner you'd like to configure.
  5. In the "Labels" section, click 
  6. In the "Find or create a label" field, type the name of your new label and click **Create new label**. The custom label is created and assigned to the self-hosted runner. Custom labels can be removed from self-hosted runners, but they currently can't be manually deleted. Any unused labels that are not assigned to a runner will be automatically deleted within 24 hours.


## [Assigning a label to a self-hosted runner](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/using-labels-with-self-hosted-runners#assigning-a-label-to-a-self-hosted-runner)
You can assign labels to self-hosted runners at the repository and organization levels.
  * [Assigning a label to a repository runner](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/using-labels-with-self-hosted-runners#assigning-a-label-to-a-repository-runner)
  * [Assigning a label to an organization runner](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/using-labels-with-self-hosted-runners#assigning-a-label-to-an-organization-runner)


### [Assigning a label to a repository runner](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/using-labels-with-self-hosted-runners#assigning-a-label-to-a-repository-runner)
  1. Navigate to the main page of the repository where your self-hosted runner group is registered.
  2. Click 
  3. In the left sidebar, click **Runners**.
  4. In the "Labels" section, click 
  5. To assign a label to your self-hosted runner, in the "Find or create a label" field, click the label.


### [Assigning a label to an organization runner](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/using-labels-with-self-hosted-runners#assigning-a-label-to-an-organization-runner)
  1. Navigate to the main page of the organization where your self-hosted runner group is registered.
  2. Click 
  3. In the left sidebar, click **Runners**.
  4. In the "Labels" section, click 
  5. To assign a label to your self-hosted runner, in the "Find or create a label" field, click the label.


## [Removing a custom label from a self-hosted runner](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/using-labels-with-self-hosted-runners#removing-a-custom-label-from-a-self-hosted-runner)
You can remove custom labels from self-hosted runners at the repository and organization levels.
  * [Removing a custom label from a repository runner](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/using-labels-with-self-hosted-runners#removing-a-custom-label-from-a-repository-runner)
  * [Removing a custom label from an organization runner](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/using-labels-with-self-hosted-runners#removing-a-custom-label-from-an-organization-runner)


### [Removing a custom label from a repository runner](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/using-labels-with-self-hosted-runners#removing-a-custom-label-from-a-repository-runner)
  1. Navigate to the main page of the repository where your self-hosted runner group is registered.
  2. Click 
  3. In the left sidebar, click **Runners**.
  4. In the "Labels" section, click 
  5. In the "Find or create a label" field, assigned labels are marked with the 


### [Removing a custom label from an organization runner](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/using-labels-with-self-hosted-runners#removing-a-custom-label-from-an-organization-runner)
  1. Navigate to the main page of the organization where your self-hosted runner group is registered.
  2. Click 
  3. In the left sidebar, click **Runners**.
  4. In the "Labels" section, click 
  5. In the "Find or create a label" field, assigned labels are marked with the 


## [Programmatically assign labels](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/using-labels-with-self-hosted-runners#programmatically-assign-labels)
You can programmatically assign labels to a self-hosted runner after the runner is created, or during its initial configuration.
  * To programmatically assign labels to an existing self-hosted runner, you must use the REST API. For more information, see [REST API endpoints for self-hosted runners](https://docs.github.com/en/rest/actions/self-hosted-runners).
  * To programmatically assign labels to a self-hosted runner during the initial runner configuration, you can pass label names to the `config` script using the `labels` parameter.
You cannot use the `config` script to assign labels to an existing self-hosted runner.
For example, this command assigns a label named `gpu` when configuring a new self-hosted runner:
```
./config.sh --url <REPOSITORY_URL> --token <REGISTRATION_TOKEN> --labels gpu

```

The label is created if it does not already exist. You can also use this approach to assign the default labels to runners, such as `x64` or `linux`. When default labels are assigned using the configuration script, GitHub Actions accepts them as given and does not validate that the runner is actually using that operating system or architecture.
You can use comma separation to assign multiple labels. For example:
```
./config.sh --url <REPOSITORY_URL> --token <REGISTRATION_TOKEN> --labels gpu,x64,linux

```

If you replace an existing runner, then you must reassign any custom labels.


