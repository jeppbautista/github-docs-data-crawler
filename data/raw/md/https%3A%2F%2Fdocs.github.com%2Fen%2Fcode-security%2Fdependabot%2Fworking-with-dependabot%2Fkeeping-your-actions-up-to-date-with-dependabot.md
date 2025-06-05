  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Dependabot](https://docs.github.com/en/code-security/dependabot "Dependabot")/
  * [Work with Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot "Work with Dependabot")/
  * [Auto-update actions](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/keeping-your-actions-up-to-date-with-dependabot "Auto-update actions")


# Keeping your actions up to date with Dependabot
You can use Dependabot to keep the actions you use updated to the latest versions.
## Who can use this feature?
Users with **write** access
## In this article
  * [About Dependabot version updates for actions](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/keeping-your-actions-up-to-date-with-dependabot#about-dependabot-version-updates-for-actions)
  * [Enabling Dependabot version updates for actions](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/keeping-your-actions-up-to-date-with-dependabot#enabling-dependabot-version-updates-for-actions)
  * [Configuring Dependabot version updates for actions](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/keeping-your-actions-up-to-date-with-dependabot#configuring-dependabot-version-updates-for-actions)
  * [Further reading](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/keeping-your-actions-up-to-date-with-dependabot#further-reading)


## [About Dependabot version updates for actions](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/keeping-your-actions-up-to-date-with-dependabot#about-dependabot-version-updates-for-actions)
Actions are often updated with bug fixes and new features to make automated processes more reliable, faster, and safer. When you enable Dependabot version updates for GitHub Actions, Dependabot will help ensure that references to actions in a repository's _workflow.yml_ file and reusable workflows used inside workflows are kept up to date.
For each action in the file, Dependabot checks the action's reference (typically a version number or commit identifier associated with the action) against the latest version. For information about how action creators version their actions, see [Using release management for your custom actions](https://docs.github.com/en/actions/learn-github-actions/finding-and-customizing-actions#using-release-management-for-your-custom-actions).
If a more recent version of the action is available, Dependabot will send you a pull request that updates the reference in the workflow file to the latest version. For more information about Dependabot version updates, see [About Dependabot version updates](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/about-dependabot-version-updates). For more information about configuring workflows for GitHub Actions, see [Writing workflows](https://docs.github.com/en/actions/learn-github-actions).
Dependabot also checks workflow files for uses of reusable workflows, and updates the git reference for these called reusable workflows. For more information about reusable workflows, see [Reusing workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows).
Workflow runs triggered by Dependabot pull requests run as if they are from a forked repository, and therefore use a read-only `GITHUB_TOKEN`. These workflow runs cannot access any secrets. For information about strategies to keep these workflows secure, see [Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions).
## [Enabling Dependabot version updates for actions](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/keeping-your-actions-up-to-date-with-dependabot#enabling-dependabot-version-updates-for-actions)
You can configure Dependabot version updates to maintain your actions as well as the libraries and packages you depend on.
  1. If you have already enabled Dependabot version updates for other ecosystems or package managers, simply open the existing `dependabot.yml` file. Otherwise, create a `dependabot.yml` configuration file in the `.github` directory of your repository. For more information, see [Configuring Dependabot version updates](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuring-dependabot-version-updates#enabling-dependabot-version-updates).
  2. Specify `"github-actions"` as a `package-ecosystem` to monitor.
  3. Set the `directory` to `"/"` to check for workflow files in `.github/workflows`.
  4. Set a `schedule.interval` to specify how often to check for new versions.
  5. Check the `dependabot.yml` configuration file in to the `.github` directory of the repository. If you have edited an existing file, save your changes.


You can also enable Dependabot version updates on forks. For more information, see [Configuring Dependabot version updates](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuring-dependabot-version-updates#enabling-version-updates-on-forks).
### [Example `dependabot.yml` file for GitHub Actions](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/keeping-your-actions-up-to-date-with-dependabot#example-dependabotyml-file-for-github-actions)
The example `dependabot.yml` file below configures version updates for GitHub Actions. The `directory` must be set to `"/"` to check for workflow files in `.github/workflows`. The `schedule.interval` is set to `"weekly"`. After this file has been checked in or updated, Dependabot checks for new versions of your actions. Dependabot will raise pull requests for version updates for any outdated actions that it finds. After the initial version updates, Dependabot will continue to check for outdated versions of actions once a week.
YAML```
# Set update schedule for GitHub Actions

version: 2
updates:

  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      # Check for updates to GitHub Actions every week
      interval: "weekly"

```
```
# Set update schedule for GitHub Actions

version: 2
updates:

  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      # Check for updates to GitHub Actions every week
      interval: "weekly"

```

## [Configuring Dependabot version updates for actions](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/keeping-your-actions-up-to-date-with-dependabot#configuring-dependabot-version-updates-for-actions)
When enabling Dependabot version updates for actions, you must specify values for `package-ecosystem`, `directory`, and `schedule.interval`. There are many more optional properties that you can set to further customize your version updates. For more information, see [Dependabot options reference](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference).
## [Further reading](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/keeping-your-actions-up-to-date-with-dependabot#further-reading)
  * [Writing workflows](https://docs.github.com/en/actions/learn-github-actions)


