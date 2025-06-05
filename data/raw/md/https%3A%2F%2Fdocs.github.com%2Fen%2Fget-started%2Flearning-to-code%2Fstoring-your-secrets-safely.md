  * [Get started](https://docs.github.com/en/get-started "Get started")/
  * [Learn to code](https://docs.github.com/en/get-started/learning-to-code "Learn to code")/
  * [Storing secrets safely](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely "Storing secrets safely")


# Storing your secrets safely
Learn about secrets in software development and how you can manage them safely.
## In this article
  * [What is a secret?](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely#what-is-a-secret)
  * [Best practices for managing your secrets](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely#best-practices-for-managing-your-secrets)
  * [How GitHub helps keep your secrets secure](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely#how-github-helps-keep-your-secrets-secure)
  * [Practicing safely storing a secret](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely#practicing-safely-storing-a-secret)
  * [Next steps](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely#next-steps)


## [What is a secret?](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely#what-is-a-secret)
In software development, a secret is a piece of sensitive information that is used to authenticate or authorize access to systems, services, data, and APIs. Examples include:
  * **API keys** and **access tokens** that allow you to interact with external services such as GitHub's REST API. Access tokens also allow services, such as GitHub Actions, to perform tasks that need authentication, as we will experiment with later.
  * **Database credentials** that grant access to local and external databases and storage.
  * **Private keys** , such as private SSH and PGP keys, that can be used to access other servers and encrypt data.


Since secrets provide so much access, including to critical systems, we can understand why it's so important to keep your **secrets secure**.
### [What can happen when a secret is exposed?](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely#what-can-happen-when-a-secret-is-exposed)
  * Attackers can gain **unauthorized access** to everything the secret allows access to.
  * Hackers can **steal data** , including sensitive user data. This may have privacy and legal ramifications and harm trust in you and your application.
  * Exposed secrets can **cost you money** if hackers run unauthorized workloads on your cloud provider accounts.
  * Hackers can use an exposed secret to delete, modify, and disrupt servers which can cause **downtime and data loss**.


Consider all the access and abilities a secret grants you and what a hacker could do with it. For example, if a personal access token for your GitHub account was exposed, a hacker could post and make changes on GitHub as you.
## [Best practices for managing your secrets](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely#best-practices-for-managing-your-secrets)
To avoid these types of issues, follow best practices to prevent leaks and limit damage if a secret is ever exposed.
### [Follow the **Principle of Least Privilege (PoLP)**](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely#follow-the-principle-of-least-privilege-polp)
Whenever possible, restrict what a secret can do and can access to only what is necessary. For example:
  * If a secret will only be used to read data and not make changes to data, opt to make it **read only**.
  * If the API you're using allows you to limit a secret to only particular scopes or permissions, only select **the ones that you need**. For example, if you only need to create issues with a GitHub secret, there's no reason for the secret to have access to repository contents or anything else.
  * If a secret will give an attacker full access to the user account that owns it, **consider creating service accounts** that can take ownership of the secret.


### [Protect secrets in your application](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely#protect-secrets-in-your-application)
  * **Never hardcode a secret**. Always use **environment variables** or your platform's secret management tools (such as GitHub's repository secrets).
  * If you have to share a secret with someone, use a dedicated tool like a **password manager**. Never send secrets via email or instant message.
  * If possible, set **expiration dates** and **rotate your secrets** regularly; this reduces the risk of old secrets being exploited.
  * If your application produces a log, ensure that **secrets are redacted before being logged**. Otherwise, active secrets could be saved to plaintext files.


### [Limit damage if a secret is exposed](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely#limit-damage-if-a-secret-is-exposed)
  * Consider the secret compromised, even if only exposed for a second, and **revoke the secret immediately**. Then, generate a new secret and store it safely.
  * Check any **activity logs** that might show any suspicious activity performed with the compromised secret.
  * Consider how the secret was exposed and make changes to your processes so this can't happen again.


## [How GitHub helps keep your secrets secure](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely#how-github-helps-keep-your-secrets-secure)
There's a lot that you can do to keep your secrets safe, but there's also a lot that GitHub does to help keep your secrets secret. Everyone makes mistakes, and we're here to help with features that will catch any secrets you accidentally expose:
  * **Push protection** , which we'll experiment with later, blocks pushing secrets to your repositories on GitHub.
  * **Secret scanning** scans repositories and creates alerts when it discovers a secret. For some secrets, we also notify the provider so they can take action, such as revoking the secret automatically.


## [Practicing safely storing a secret](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely#practicing-safely-storing-a-secret)
In this exercise, we'll create a personal access token and store it safely so we can use it with GitHub Actions. The action we'll create is a straightforward workflow that responds to an issue.
### [1. Creating a practice repository](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely#1-creating-a-practice-repository)
We'll start by creating a repository to work from. The `new2code` account has a template repository we can use to quickly get started.
  1. Navigate to the [new repository page](https://github.com/new?template_owner=new2code&template_name=secret-action). Following this link will pre-select the template on the `new2code` account.
  2. Under "Owner", make sure your user account is selected.
  3. In the "Repository name" field, type `secret-action`.
  4. Beneath the description field, select **Public** to set the repository visibility.
  5. Click **Create repository**.


### [2. Committing a dummy token](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely#2-committing-a-dummy-token)
Everyone makes mistakes, and it's possible that you'll accidentally commit a secret at some point in your coding journey. In this exercise, we'll intentionally commit a **fake token** so that we can become familiar and comfortable with the alert that gets triggered.
  1. Navigate to the repository you just created.
  2. Navigate to the YAML workflow file by clicking `.github/workflows` in the list of files.
  3. Open the workflow file by clicking `comment.yml` in the list of files.
  4. To edit the workflow file, at the top-right, click 
  5. On line 13, `GH_TOKEN: ""`, insert this dummy token between the quotes:
```
secret_scanning_ab85fc6f8d7638cf1c11da812da308d43_abcde

```

The end result should look like this:
```
GH_TOKEN: "secret_scanning_ab85fc6f8d7638cf1c11da812da308d43_abcde"

```

  6. To attempt to commit the change, at the top right, click **Commit changes...** and then click **Commit changes** again in the dialog.
  7. You should now see the push protection alert, telling you that "Secret scanning found a GitHub Secret Scanning secret on line 13".
![Screenshot of a push protection alert for Line 13 of the file we attempted to commit. The "Cancel" button is highlighted in an orange outline.](https://docs.github.com/assets/cb-89243/images/help/security/push-protection-example.png)
If we weren't experimenting with a dummy token, this would alert us that we were one step away from exposing a token. Review the options you can select on the alert.
  8. To stop your commit and avoid exposing the secret, click **Cancel**. In the top right, click **Cancel changes** , then discard your unsaved changes if prompted.


### [3. Creating a real token](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely#3-creating-a-real-token)
Now, let's try following our best practices. First, we'll create a personal access token which will allow the action to act on your behalf (the comment it creates will appear to come from your user account).
Notice how we follow the Principle of Least Privilege for each configuration step. Your token will have the shortest expiration necessary, only have access to the repository it needs, and have the minimum permissions needed to work.
  1. Navigate to the [new personal access token page](https://github.com/settings/personal-access-tokens/new).
  2. Under "Token name", give your new token a name. You can use something like "Action token".
  3. Under "Expiration", select "7 days".
  4. Under "Repository access", select **Only select repositories**.
  5. In the "Select repositories" dropdown, select **just** the practice repository you created earlier.
  6. To the right of "Repository permissions" in the "Permissions" section, click 
  7. Scroll down to "Issues" and, in the dropdown on the right, select "Read and write".
  8. At the bottom of the page, click **Generate token**. If prompted, confirm by clicking **Generate token** again.


It's crucial to handle the resulting token securely from this moment forward. As we'll be using the token shortly, you can copy it to your clipboard briefly.
### [4. Storing the token safely](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely#4-storing-the-token-safely)
We can now store our new token safely in our repository.
  1. Navigate to the repository you created at the beginning of the exercise.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Security" section of the sidebar, select **Actions**.
  4. Under "Repository secrets," click **New repository secret**.
  5. In the **Name** field, type the name for your secret. For this exercise, we'll use `MY_TOKEN`.
  6. In the **Secret** field, paste the personal access token you generated previously.
  7. Click **Add secret**.


Your secret is now safely encrypted and ready to use!
### [5. Referencing the token in our action](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely#5-referencing-the-token-in-our-action)
Now we can update the YAML workflow file to use the token and test it works.
  1. Navigate back to your repository. If you're in your repository's settings, you can click 
  2. Navigate to the YAML workflow file by clicking `.github/workflows` in the list of files.
  3. Open the workflow file by clicking `comment.yml` in the list of files.
  4. To start editing the workflow file, at the top-right, click 
  5. On line 13, `GH_TOKEN: ""`, replace the empty quotes with `${{ secrets.MY_TOKEN }}`. This will reference the repository secret we added previously.
```
GH_TOKEN: ${{ secrets.MY_TOKEN }}

```

  6. To commit the change, at the top-right, click **Commit changes...**
  7. In the "Commit changes" dialog, edit "Commit message" to reflect the change we're making. For example, you could enter "Updating workflow to use repository secret".
  8. Make sure "Commit directly to the `main` branch" is selected.
  9. Click **Commit changes**.


### [6. Testing out the token and workflow](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely#6-testing-out-the-token-and-workflow)
We should be all set now! Let's go ahead and test the workflow.
  1. Under your repository name, click 
![Screenshot of the main page of a repository. In the horizontal navigation bar, a tab, labeled "Issues," is outlined in dark orange.](https://docs.github.com/assets/cb-51267/images/help/repository/repo-tabs-issues-global-nav-update.png)
  2. Click **New issue**.
  3. Under "Add a title", you can type any title you like.
  4. Under "Add a description", in the text area, type `Hello`.
  5. Beneath the text area, click **Create**.


Once the workflow has had time to complete, you should see a new comment appear. The comment will be authored by yourself, as we're using your token, and contain a greeting in return.
## [Next steps](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely#next-steps)
For a more in-depth dive into secret scanning and push protection, you can complete the [Introduction to secret scanning](https://github.com/skills/introduction-to-secret-scanning/tree/main) course in GitHub Skills.
Another important part of code security is learning how to identify and patch code vulnerabilities in your projects. See [Finding and fixing your first code vulnerability](https://docs.github.com/en/get-started/learning-to-code/finding-and-fixing-your-first-code-vulnerability).
