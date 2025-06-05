  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Share automations](https://docs.github.com/en/actions/sharing-automations "Share automations")/
  * [Create actions](https://docs.github.com/en/actions/sharing-automations/creating-actions "Create actions")/
  * [Set exit codes](https://docs.github.com/en/actions/sharing-automations/creating-actions/setting-exit-codes-for-actions "Set exit codes")


# Setting exit codes for actions
You can use exit codes to set the status of an action. GitHub displays statuses to indicate passing or failing actions.
## In this article
  * [About exit codes](https://docs.github.com/en/actions/sharing-automations/creating-actions/setting-exit-codes-for-actions#about-exit-codes)
  * [Setting a failure exit code in a JavaScript action](https://docs.github.com/en/actions/sharing-automations/creating-actions/setting-exit-codes-for-actions#setting-a-failure-exit-code-in-a-javascript-action)
  * [Setting a failure exit code in a Docker container action](https://docs.github.com/en/actions/sharing-automations/creating-actions/setting-exit-codes-for-actions#setting-a-failure-exit-code-in-a-docker-container-action)


## [About exit codes](https://docs.github.com/en/actions/sharing-automations/creating-actions/setting-exit-codes-for-actions#about-exit-codes)
GitHub uses the exit code to set the action's check run status, which can be `success` or `failure`.
Exit status | Check run status | Description  
---|---|---  
`0` | `success` | The action completed successfully and other tasks that depend on it can begin.  
Nonzero value (any integer but 0) | `failure` | Any other exit code indicates the action failed. When an action fails, all concurrent actions are canceled and future actions are skipped. The check run and check suite both get a `failure` status.  
## [Setting a failure exit code in a JavaScript action](https://docs.github.com/en/actions/sharing-automations/creating-actions/setting-exit-codes-for-actions#setting-a-failure-exit-code-in-a-javascript-action)
If you are creating a JavaScript action, you can use the actions toolkit [`@actions/core`](https://github.com/actions/toolkit/tree/main/packages/core) package to log a message and set a failure exit code. For example:
```
try {
  // something
} catch (error) {
  core.setFailed(error.message);
}

```

For more information, see [Creating a JavaScript action](https://docs.github.com/en/actions/creating-actions/creating-a-javascript-action).
## [Setting a failure exit code in a Docker container action](https://docs.github.com/en/actions/sharing-automations/creating-actions/setting-exit-codes-for-actions#setting-a-failure-exit-code-in-a-docker-container-action)
If you are creating a Docker container action, you can set a failure exit code in your `entrypoint.sh` script. For example:
```
if <condition> ; then
  echo "Game over!"
  exit 1
fi

```

For more information, see [Creating a Docker container action](https://docs.github.com/en/actions/creating-actions/creating-a-docker-container-action).
