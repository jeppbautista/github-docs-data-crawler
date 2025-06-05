  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Security](https://docs.github.com/en/actions/security-for-github-actions "Security")/
  * [Security guides](https://docs.github.com/en/actions/security-for-github-actions/security-guides "Security guides")/
  * [Using secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions "Using secrets")


# Using secrets in GitHub Actions
Secrets allow you to store sensitive information in your organization, repository, or repository environments.
## Tool navigation
  * [GitHub CLI](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions?tool=cli)
  * [Web browser](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions?tool=webui)


## In this article
  * [Creating secrets for a repository](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository)
  * [Creating secrets for an environment](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-an-environment)
  * [Creating secrets for an organization](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-an-organization)
  * [Reviewing access to organization-level secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#reviewing-access-to-organization-level-secrets)
  * [Using secrets in a workflow](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#using-secrets-in-a-workflow)
  * [Limits for secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#limits-for-secrets)
  * [Storing Base64 binary blobs as secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#storing-base64-binary-blobs-as-secrets)
  * [Redacting secrets from workflow run logs](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#redacting-secrets-from-workflow-run-logs)


For general information about secrets, see [About secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/about-secrets).
## [Creating secrets for a repository](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository)
To create secrets or variables on GitHub for a personal account repository, you must be the repository owner. To create secrets or variables on GitHub for an organization repository, you must have `admin` access. Lastly, to create secrets or variables for a personal account repository or an organization repository through the REST API, you must have collaborator access.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Security" section of the sidebar, select **Actions**.
  4. Click the **Secrets** tab. 
![Screenshot of the "Actions secrets and variables" page. The "Secrets" tab is outlined in dark orange.](https://docs.github.com/assets/cb-57155/images/help/repository/actions-secrets-tab.png)
  5. Click **New repository secret**.
  6. In the **Name** field, type a name for your secret.
  7. In the **Secret** field, enter the value for your secret.
  8. Click **Add secret**.


If your repository has environment secrets or can access secrets from the parent organization, then those secrets are also listed on this page.
To learn more about GitHub CLI, see [About GitHub CLI](https://docs.github.com/en/github-cli/github-cli/about-github-cli).
To add a repository secret, use the `gh secret set` subcommand. Replace `secret-name` with the name of your secret.
```
gh secret set SECRET_NAME

```

The CLI will prompt you to enter a secret value. Alternatively, you can read the value of the secret from a file.
```
gh secret set SECRET_NAME < secret.txt

```

To list all secrets for the repository, use the `gh secret list` subcommand.
## [Creating secrets for an environment](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-an-environment)
To create secrets or variables for an environment in a personal account repository, you must be the repository owner. To create secrets or variables for an environment in an organization repository, you must have `admin` access. For more information on environments, see [Managing environments for deployment](https://docs.github.com/en/actions/deployment/targeting-different-environments/managing-environments-for-deployment).
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the left sidebar, click **Environments**.
  4. Click on the environment that you want to add a secret to.
  5. Under **Environment secrets** , click **Add secret**.
  6. Type a name for your secret in the **Name** input box.
  7. Enter the value for your secret.
  8. Click **Add secret**.


To add a secret for an environment, use the `gh secret set` subcommand with the `--env` or `-e` flag followed by the environment name.
```
gh secret set --env ENV_NAME SECRET_NAME

```

To list all secrets for an environment, use the `gh secret list` subcommand with the `--env` or `-e` flag followed by the environment name.
```
gh secret list --env ENV_NAME

```

## [Creating secrets for an organization](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-an-organization)
Organization-level secrets and variables are not accessible by private repositories for GitHub Free. For more information about upgrading your GitHub subscription, see [Upgrading your account's plan](https://docs.github.com/en/billing/managing-billing-for-your-github-account/upgrading-your-github-subscription).
When creating a secret or variable in an organization, you can use a policy to limit access by repository. For example, you can grant access to all repositories, or limit access to only private repositories or a specified list of repositories.
Organization owners can create secrets or variables at the organization level.
  1. On GitHub, navigate to the main page of the organization.
  2. Under your organization name, click **Settings**.
![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](https://docs.github.com/assets/cb-49309/images/help/discussions/org-settings-global-nav-update.png)
  3. In the "Security" section of the sidebar, select **Actions**.
  4. Click the **Secrets** tab.
![Screenshot of the "Actions secrets and variables" page. The "Secrets" tab is outlined in dark orange.](https://docs.github.com/assets/cb-57155/images/help/repository/actions-secrets-tab.png)
  5. Click **New organization secret**.
  6. Type a name for your secret in the **Name** input box.
  7. Enter the **Value** for your secret.
  8. From the **Repository access** dropdown list, choose an access policy.
  9. Click **Add secret**.


By default, GitHub CLI authenticates with the `repo` and `read:org` scopes. To manage organization secrets, you must additionally authorize the `admin:org` scope.
```
gh auth login --scopes "admin:org"

```

To add a secret for an organization, use the `gh secret set` subcommand with the `--org` or `-o` flag followed by the organization name.
```
gh secret set --org ORG_NAME SECRET_NAME

```

By default, the secret is only available to private repositories. To specify that the secret should be available to all repositories within the organization, use the `--visibility` or `-v` flag.
```
gh secret set --org ORG_NAME SECRET_NAME --visibility all

```

To specify that the secret should be available to selected repositories within the organization, use the `--repos` or `-r` flag.
```
gh secret set --org ORG_NAME SECRET_NAME --repos REPO-NAME-1, REPO-NAME-2

```

To list all secrets for an organization, use the `gh secret list` subcommand with the `--org` or `-o` flag followed by the organization name.
```
gh secret list --org ORG_NAME

```

## [Reviewing access to organization-level secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#reviewing-access-to-organization-level-secrets)
You can check which access policies are being applied to a secret in your organization.
  1. On GitHub, navigate to the main page of the organization.
  2. Under your organization name, click **Settings**.
![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](https://docs.github.com/assets/cb-49309/images/help/discussions/org-settings-global-nav-update.png)
  3. In the "Security" section of the sidebar, select **Actions**.
  4. The list of secrets includes any configured permissions and policies. For more details about the configured permissions for each secret, click **Update**.


## [Using secrets in a workflow](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#using-secrets-in-a-workflow)
  * With the exception of `GITHUB_TOKEN`, secrets are not passed to the runner when a workflow is triggered from a forked repository.
  * Secrets are not automatically passed to reusable workflows. For more information, see [Reusing workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows#passing-inputs-and-secrets-to-a-reusable-workflow). If your GitHub Actions workflows need to access resources from a cloud provider that supports OpenID Connect (OIDC), you can configure your workflows to authenticate directly to the cloud provider. This will let you stop storing these credentials as long-lived secrets and provide other security benefits. For more information, see [About security hardening with OpenID Connect](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect).


To provide an action with a secret as an input or environment variable, you can use the `secrets` context to access secrets you've created in your repository. For more information, see [Accessing contextual information about workflow runs](https://docs.github.com/en/actions/learn-github-actions/contexts) and [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions).
```
steps:
  - name: Hello world action
    with: # Set the secret as an input
      super_secret: ${{ secrets.SuperSecret }}
    env: # Or as an environment variable
      super_secret: ${{ secrets.SuperSecret }}

```

Secrets cannot be directly referenced in `if:` conditionals. Instead, consider setting secrets as job-level environment variables, then referencing the environment variables to conditionally run steps in the job. For more information, see [Accessing contextual information about workflow runs](https://docs.github.com/en/actions/learn-github-actions/contexts#context-availability) and [`jobs.<job_id>.steps[*].if`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstepsif).
If a secret has not been set, the return value of an expression referencing the secret (such as `${{ secrets.SuperSecret }}` in the example) will be an empty string.
Avoid passing secrets between processes from the command line, whenever possible. Command-line processes may be visible to other users (using the `ps` command) or captured by [security audit events](https://docs.microsoft.com/windows-server/identity/ad-ds/manage/component-updates/command-line-process-auditing). To help protect secrets, consider using environment variables, `STDIN`, or other mechanisms supported by the target process.
If you must pass secrets within a command line, then enclose them within the proper quoting rules. Secrets often contain special characters that may unintentionally affect your shell. To escape these special characters, use quoting with your environment variables. For example:
### [Example using Bash](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#example-using-bash)
```
steps:
  - shell: bash
    env:
      SUPER_SECRET: ${{ secrets.SuperSecret }}
    run: |
      example-command "$SUPER_SECRET"

```

### [Example using PowerShell](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#example-using-powershell)
```
steps:
  - shell: pwsh
    env:
      SUPER_SECRET: ${{ secrets.SuperSecret }}
    run: |
      example-command "$env:SUPER_SECRET"

```

### [Example using Cmd.exe](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#example-using-cmdexe)
```
steps:
  - shell: cmd
    env:
      SUPER_SECRET: ${{ secrets.SuperSecret }}
    run: |
      example-command "%SUPER_SECRET%"

```

## [Limits for secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#limits-for-secrets)
You can store up to 1,000 organization secrets, 100 repository secrets, and 100 environment secrets.
A workflow created in a repository can access the following number of secrets:
  * All 100 repository secrets.
  * If the repository is assigned access to more than 100 organization secrets, the workflow can only use the first 100 organization secrets (sorted alphabetically by secret name).
  * All 100 environment secrets.


Secrets are limited to 48 KB in size. To store larger secrets, see the [Storing large secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#storing-large-secrets) workaround below.
### [Storing large secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#storing-large-secrets)
To use secrets that are larger than 48 KB, you can use a workaround to store secrets in your repository and save the decryption passphrase as a secret on GitHub. For example, you can use `gpg` to encrypt a file containing your secret locally before checking the encrypted file in to your repository on GitHub. For more information, see the [gpg manpage](https://www.gnupg.org/gph/de/manual/r1023.html).
Be careful that your secrets do not get printed when your workflow runs. When using this workaround, GitHub does not redact secrets that are printed in logs.
  1. Run the following command from your terminal to encrypt the file containing your secret using `gpg` and the AES256 cipher algorithm. In this example, `my_secret.json` is the file containing the secret.
```
gpg --symmetric --cipher-algo AES256 my_secret.json

```

  2. You will be prompted to enter a passphrase. Remember the passphrase, because you'll need to create a new secret on GitHub that uses the passphrase as the value.
  3. Create a new secret that contains the passphrase. For example, create a new secret with the name `LARGE_SECRET_PASSPHRASE` and set the value of the secret to the passphrase you used in the step above.
  4. Copy your encrypted file to a path in your repository and commit it. In this example, the encrypted file is `my_secret.json.gpg`.
Make sure to copy the encrypted `my_secret.json.gpg` file ending with the `.gpg` file extension, and **not** the unencrypted `my_secret.json` file.
```
git add my_secret.json.gpg
git commit -m "Add new secret JSON file"

```

  5. Create a shell script in your repository to decrypt the secret file. In this example, the script is named `decrypt_secret.sh`.
Shell```
#!/bin/sh

# Decrypt the file
mkdir $HOME/secrets
# --batch to prevent interactive command
# --yes to assume "yes" for questions
gpg --quiet --batch --yes --decrypt --passphrase="$LARGE_SECRET_PASSPHRASE" \
--output $HOME/secrets/my_secret.json my_secret.json.gpg

```
```
#!/bin/sh

# Decrypt the file
mkdir $HOME/secrets
# --batch to prevent interactive command
# --yes to assume "yes" for questions
gpg --quiet --batch --yes --decrypt --passphrase="$LARGE_SECRET_PASSPHRASE" \
--output $HOME/secrets/my_secret.json my_secret.json.gpg

```

  6. Ensure your shell script is executable before checking it in to your repository.
```
chmod +x decrypt_secret.sh
git add decrypt_secret.sh
git commit -m "Add new decryption script"
git push

```

  7. In your GitHub Actions workflow, use a `step` to call the shell script and decrypt the secret. To have a copy of your repository in the environment that your workflow runs in, you'll need to use the [`actions/checkout`](https://github.com/actions/checkout) action. Reference your shell script using the `run` command relative to the root of your repository.
```
name: Workflows with large secrets

on: push

jobs:
  my-job:
    name: My Job
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Decrypt large secret
        run: ./decrypt_secret.sh
        env:
          LARGE_SECRET_PASSPHRASE: ${{ secrets.LARGE_SECRET_PASSPHRASE }}
      # This command is just an example to show your secret being printed
      # Ensure you remove any print statements of your secrets. GitHub does
      # not hide secrets that use this workaround.
      - name: Test printing your secret (Remove this step in production)
        run: cat $HOME/secrets/my_secret.json

```



## [Storing Base64 binary blobs as secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#storing-base64-binary-blobs-as-secrets)
You can use Base64 encoding to store small binary blobs as secrets. You can then reference the secret in your workflow and decode it for use on the runner. For the size limits, see [Using secrets in GitHub Actions](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#limits-for-secrets).
Note that Base64 only converts binary to text, and is not a substitute for actual encryption.
  1. Use `base64` to encode your file into a Base64 string. For example:
On macOS, you could run:
```
base64 -i cert.der -o cert.base64

```

On Linux, you could run:
```
base64 -w 0 cert.der > cert.base64

```

  2. Create a secret that contains the Base64 string. For example:
```
$ gh secret set CERTIFICATE_BASE64 < cert.base64
✓ Set secret CERTIFICATE_BASE64 for octocat/octorepo

```

  3. To access the Base64 string from your runner, pipe the secret to `base64 --decode`. For example:
```
name: Retrieve Base64 secret
on:
  push:
    branches: [ octo-branch ]
jobs:
  decode-secret:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Retrieve the secret and decode it to a file
        env:
          CERTIFICATE_BASE64: ${{ secrets.CERTIFICATE_BASE64 }}
        run: |
          echo $CERTIFICATE_BASE64 | base64 --decode > cert.der
      - name: Show certificate information
        run: |
          openssl x509 -in cert.der -inform DER -text -noout

```



Using another shell might require different commands for decoding the secret to a file. On Windows runners, we recommend [using a bash shell](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstepsshell) with `shell: bash` to use the commands in the `run` step above.
## [Redacting secrets from workflow run logs](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#redacting-secrets-from-workflow-run-logs)
GitHub Actions automatically redacts the contents of all GitHub secrets that are printed to workflow logs.
GitHub Actions also redacts information that is recognized as sensitive, but is not stored as a secret. Currently GitHub supports the following:
  * 32-byte and 64-byte Azure keys
  * Azure AD client app passwords
  * Azure Cache keys
  * Azure Container Registry keys
  * Azure Function host keys
  * Azure Search keys
  * Database connection strings
  * HTTP Bearer token headers
  * JWTs
  * NPM author tokens
  * NuGet API keys
  * v1 GitHub installation tokens
  * v2 GitHub installation tokens (`ghp`, `gho`, `ghu`, `ghs`, `ghr`)
  * v2 GitHub PATs


If you would like other types of sensitive information to be automatically redacted, please reach out to us in our [community discussions](https://github.com/orgs/community/discussions?discussions_q=is%3Aopen+label%3AActions).
As a habit of best practice, you should mask all sensitive information that is not a GitHub secret by using `::add-mask::VALUE`. This causes the value to be treated as a secret and redacted from logs. For more information about masking data, see [Workflow commands for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#masking-a-value-in-a-log).
Redacting of secrets is performed by your workflow runners. This means a secret will only be redacted if it was used within a job and is accessible by the runner. If an unredacted secret is sent to a workflow run log, you should delete the log and rotate the secret. For information on deleting logs, see [Using workflow run logs](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/using-workflow-run-logs#deleting-logs).
