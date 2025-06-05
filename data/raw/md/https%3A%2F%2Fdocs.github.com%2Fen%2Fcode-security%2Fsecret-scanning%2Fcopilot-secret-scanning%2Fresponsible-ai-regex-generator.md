  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secret scanning](https://docs.github.com/en/code-security/secret-scanning "Secret scanning")/
  * [Copilot secret scanning](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning "Copilot secret scanning")/
  * [Generate regular expressions with AI](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-regex-generator "Generate regular expressions with AI")


# Responsible generation of regular expressions with Copilot secret scanning
Learn about the capabilities and limitations of the regular expression generator in helping you to define custom patterns to extend the capabilities of secret scanning.
## Who can use this feature?
Copilot secret scanning is available for the following repository types:
  * Organization-owned repositories on GitHub Team with [GitHub Secret Protection](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [About generating regular expressions with Copilot secret scanning](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-regex-generator#about-generating-regular-expressions-with-copilot-secret-scanning)
  * [Improving performance when generating regular expressions with AI](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-regex-generator#improving-performance-when-generating-regular-expressions-with-ai)
  * [Limitations of generating regular expressions with AI](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-regex-generator#limitations-of-generating-regular-expressions-with-ai)
  * [Next steps](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-regex-generator#next-steps)
  * [Further reading](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-regex-generator#further-reading)


## [About generating regular expressions with Copilot secret scanning](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-regex-generator#about-generating-regular-expressions-with-copilot-secret-scanning)
Secret scanning scans repositories for a predefined set of secrets from our partner program, as well as custom patterns that are user-defined. Custom patterns are formatted as regular expressions.
You do not need a subscription to GitHub Copilot to use Copilot secret scanning's regular expression generator. Copilot secret scanning features are available to repositories owned by organizations and enterprises that have a license for GitHub Secret Protection.
Regular expressions can be challenging for people to write. Copilot secret scanning's regular expression generator makes it possible for you to define your custom patterns without knowledge of regular expressions. Within the existing custom pattern page, you can launch a generative AI experience where you input a text description of what pattern you would like to detect, include optional example strings that should be detected, and get matching regular expressions in return.
### [Input processing](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-regex-generator#input-processing)
Users input a text description of what they would like to detect, and optional example strings that should be detected.
### [Response generation and output formatting](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-regex-generator#response-generation-and-output-formatting)
Copilot secret scanning's regular expression generator uses GPT-3.5-Turbo and the GitHub Copilot API to generate regular expressions that match your input.
The model returns up to three regular expressions for you to review. You can click on the regular expression to get an AI-generated plain language description of the regular expression.
Some results may be quite similar, and some results may not find every instance of the secret that the pattern is intended to detect. It is also possible that the regular expression generator may produce results which are invalid or inappropriate.
When you click **Use result** on a regular expression, the expression and any examples inputted will be copied over to the main custom pattern form. There, you can perform a dry run of the pattern to see how it performs across your repository or organization. For more information on how to define a custom pattern for your repository or organization, see [Defining custom patterns for secret scanning](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/defining-custom-patterns-for-secret-scanning).
## [Improving performance when generating regular expressions with AI](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-regex-generator#improving-performance-when-generating-regular-expressions-with-ai)
To enhance performance and address some of the limitations of Copilot secret scanning's regular expression generator, there are various measures that you can adopt. For more information on the limitations of the regular expression generator, see [Limitations of generating regular expressions with AI](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-regex-generator#limitations-of-generating-regular-expressions-with-ai).
### [Use Copilot secret scanning's regular expression generator as a tool, not a replacement](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-regex-generator#use-copilot-secret-scannings-regular-expression-generator-as-a-tool-not-a-replacement)
While the regular expression generator is a powerful tool to create custom patterns without you having to write regular expressions yourself, it is important to use it as a tool rather than a replacement for manual input. You should carefully validate the performance of the results by performing a dry run across your organization or repository. It's a good idea to run the pattern on a repository (or repositories) that are representative of the repositories in your organization. In some cases, it may be beneficial to modify a generated regular expression to more fully meet your needs. You remain ultimately responsible for any custom patterns you decide to use.
## [Limitations of generating regular expressions with AI](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-regex-generator#limitations-of-generating-regular-expressions-with-ai)
Depending on factors such as your input description and examples, you may experience different levels of performance when using Copilot secret scanning's regular expression generator. You need to be as specific as possible with your description, and provide different types of examples of tokens that match your pattern, to be sure that the regular expression encompasses all the patterns you want secret scanning to search for.
Also, the model used by the regular expression generator has been trained on natural language content written predominantly in English. As a result, you may notice differing performance when providing the generator with natural language input prompts in languages other than English.
Note that Copilot secret scanning's regular expression generator is only suitable for creating regular expressions to detect structured patterns.
## [Next steps](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-regex-generator#next-steps)
  * [Generating regular expressions for custom patterns with Copilot secret scanning](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/generating-regular-expressions-for-custom-patterns-with-copilot-secret-scanning)
  * [Managing alerts from secret scanning](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning)


## [Further reading](https://docs.github.com/en/code-security/secret-scanning/copilot-secret-scanning/responsible-ai-regex-generator#further-reading)
  * [About secret scanning](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning)
  * [Managing alerts from secret scanning](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning)
  * [Defining custom patterns for secret scanning](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/defining-custom-patterns-for-secret-scanning)
  * [About secret scanning](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning)


