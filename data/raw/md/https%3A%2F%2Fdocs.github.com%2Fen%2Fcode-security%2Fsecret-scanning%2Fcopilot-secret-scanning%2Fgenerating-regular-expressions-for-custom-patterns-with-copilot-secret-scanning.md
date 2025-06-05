  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secret scanning](https://docs.github.com/en/code-security/secret-scanning "Secret scanning")/
  * [Copilot secret scanning](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning "Copilot secret scanning")/
  * [Regular expression generator](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/generating-regular-expressions-for-custom-patterns-with-copilot-secret-scanning "Regular expression generator")


# Generating regular expressions for custom patterns with Copilot secret scanning
You can use Copilot secret scanning's regular expression generator to write regular expressions for custom patterns. The generator uses an AI model to generate expressions that match your input, and optionally example strings.
## Who can use this feature?
Repository owners, organization owners, security managers, and users with the **admin** role
## In this article
  * [Generating a regular expression for a repository with Copilot secret scanning](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/generating-regular-expressions-for-custom-patterns-with-copilot-secret-scanning#generating-a-regular-expression-for-a-repository-with-copilot-secret-scanning)
  * [Generating a regular expression for an organization with Copilot secret scanning](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/generating-regular-expressions-for-custom-patterns-with-copilot-secret-scanning#generating-a-regular-expression-for-an-organization-with-copilot-secret-scanning)
  * [Further reading](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/generating-regular-expressions-for-custom-patterns-with-copilot-secret-scanning#further-reading)


## [Generating a regular expression for a repository with Copilot secret scanning](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/generating-regular-expressions-for-custom-patterns-with-copilot-secret-scanning#generating-a-regular-expression-for-a-repository-with-copilot-secret-scanning)
You do not need a subscription to GitHub Copilot to use Copilot secret scanning's regular expression generator. Copilot secret scanning features are available to repositories owned by organizations and enterprises with GitHub Secret Protection enabled.
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Security" section of the sidebar, click 
  4. Under "Secret Protection", under "Custom patterns", click **New pattern**.
  5. In the "Pattern name" field, type a name for your pattern.
  6. On the top right, click **Generate with AI**.
You can enter a regular expression manually instead of using the generator, by typing a regular expression for the format of your secret pattern in the "Secret format" field. For more information, see [Defining a custom pattern for a repository](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/defining-custom-patterns-for-secret-scanning#defining-a-custom-pattern-for-a-repository) or [Defining a custom pattern for an organization](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/defining-custom-patterns-for-secret-scanning#defining-a-custom-pattern-for-an-organization).
  7. In the sliding panel that is displayed:
     * Complete the "I want a regular expression that" field, describing, ideally in plain English, what patterns you want your regular expression to capture. You can use other natural languages, but the performance may not be as good as with English.
     * Complete the "Examples of what I'm looking for" field, giving an example of a pattern you want to scan for.
     * Click **Generate suggestions**.
     * Optionally, click on a suggestion to view a description of the regular expression.
     * Click **Use results** in the Results section that appears, for the result you want to use.
![Screenshot of a filled custom secret scanning pattern form for the generator to use.](https://docs.github.com/assets/cb-81182/images/help/repository/secret-scanning-use-regular-expression-generator.png)
  8. You can click **More options** to provide other surrounding content or additional match requirements for the secret format. GitHub will add the examples you typed in the sliding panel to the **Test string** field.
  9. When you're ready to test your new custom pattern, to identify matches in the repository without creating alerts, click **Save and dry run**.
  10. When the dry run finishes, you'll see a sample of results (up to 1000). Review the results and identify any false positive results. 
![Screenshot showing results from dry run.](https://docs.github.com/assets/cb-29264/images/help/repository/secret-scanning-publish-pattern.png)
  11. Edit the new custom pattern to fix any problems with the results, then, to test your changes, click **Save and dry run**.
  12. When you're satisfied with your new custom pattern, click **Publish pattern**.


You can configure secret scanning to check pushes for custom patterns before commits are merged into the default branch. For more information, see [Enabling push protection for a custom pattern](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/managing-custom-patterns#enabling-push-protection-for-a-custom-pattern).
## [Generating a regular expression for an organization with Copilot secret scanning](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/generating-regular-expressions-for-custom-patterns-with-copilot-secret-scanning#generating-a-regular-expression-for-an-organization-with-copilot-secret-scanning)
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the "Security" section of the sidebar, click **Global settings**.
  4. Under "Custom patterns", click **New pattern**.
  5. In the "Pattern name" field, type a name for your pattern.
  6. On the top right, click **Generate with AI**.
You can enter a regular expression manually instead of using the generator, by typing a regular expression for the format of your secret pattern in the "Secret format" field. For more information, see [Defining a custom pattern for a repository](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/defining-custom-patterns-for-secret-scanning#defining-a-custom-pattern-for-a-repository) or [Defining a custom pattern for an organization](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/defining-custom-patterns-for-secret-scanning#defining-a-custom-pattern-for-an-organization).
  7. In the sliding panel that is displayed:
     * Complete the "I want a regular expression that" field, describing, ideally in plain English, what patterns you want your regular expression to capture. You can use other natural languages, but the performance may not be as good as with English.
     * Complete the "Examples of what I'm looking for" field, giving an example of a pattern you want to scan for.
     * Click **Generate suggestions**.
     * Optionally, click on a suggestion to view a description of the regular expression.
     * Click **Use results** in the Results section that appears, for the result you want to use.
![Screenshot of a filled custom secret scanning pattern form for the generator to use.](https://docs.github.com/assets/cb-81182/images/help/repository/secret-scanning-use-regular-expression-generator.png)
  8. You can click **More options** to provide other surrounding content or additional match requirements for the secret format. GitHub will add the examples you typed in the sliding panel to the **Test string** field.
  9. When you're ready to test your new custom pattern, to identify matches in selected repositories without creating alerts, click **Save and dry run**.
  10. Select the repositories where you want to perform the dry run.
     * To perform the dry run across the entire organization, select **All repositories in the organization**.
     * To specify the repositories where you want to perform the dry run, select **Selected repositories** , then search for and select up to 10 repositories.
  11. When you're ready to test your new custom pattern, click **Run**.
  12. When the dry run finishes, you'll see a sample of results (up to 1000). Review the results and identify any false positive results. 
![Screenshot showing results from dry run.](https://docs.github.com/assets/cb-29264/images/help/repository/secret-scanning-publish-pattern.png)
  13. Edit the new custom pattern to fix any problems with the results, then, to test your changes, click **Save and dry run**.
  14. When you're satisfied with your new custom pattern, click **Publish pattern**.


You can configure secret scanning to check pushes for custom patterns before commits are merged into the default branch. For more information, see [Enabling push protection for a custom pattern](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/managing-custom-patterns#enabling-push-protection-for-a-custom-pattern).
## [Further reading](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/generating-regular-expressions-for-custom-patterns-with-copilot-secret-scanning#further-reading)
  * [Responsible generation of regular expressions with Copilot secret scanning](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-regex-generator)


