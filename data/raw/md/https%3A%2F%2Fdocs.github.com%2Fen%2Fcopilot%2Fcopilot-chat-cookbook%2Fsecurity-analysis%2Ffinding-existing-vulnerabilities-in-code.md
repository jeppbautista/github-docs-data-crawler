  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Copilot Chat Cookbook](https://docs.github.com/en/copilot/copilot-chat-cookbook "Copilot Chat Cookbook")/
  * [Security analysis](https://docs.github.com/en/copilot/copilot-chat-cookbook/security-analysis "Security analysis")/
  * [Find vulnerabilities](https://docs.github.com/en/copilot/copilot-chat-cookbook/security-analysis/finding-existing-vulnerabilities-in-code "Find vulnerabilities")


# Finding existing vulnerabilities in code
Copilot Chat can help find common vulnerabilities in your code and suggest fixes.
## In this article
  * [Example scenario](https://docs.github.com/en/copilot/copilot-chat-cookbook/security-analysis/finding-existing-vulnerabilities-in-code#example-scenario)
  * [Example prompt](https://docs.github.com/en/copilot/copilot-chat-cookbook/security-analysis/finding-existing-vulnerabilities-in-code#example-prompt)
  * [Example response](https://docs.github.com/en/copilot/copilot-chat-cookbook/security-analysis/finding-existing-vulnerabilities-in-code#example-response)
  * [Further reading](https://docs.github.com/en/copilot/copilot-chat-cookbook/security-analysis/finding-existing-vulnerabilities-in-code#further-reading)


While they may be considered "common knowledge" by many developers, the vast majority of newly introduced security weaknesses are due to vulnerabilities like cross-site scripting (XSS), SQL injection, and cross-site request forgery (CSRF). These vulnerabilities can be mitigated by following secure coding practices, such as using parameterized queries, input validation, and avoiding hard-coded sensitive data. GitHub Copilot can help detect and resolve these issues.
While Copilot Chat can help find some common security vulnerabilities and help you fix them, you should not rely on Copilot for a comprehensive security analysis. Using code scanning will more thoroughly ensure your code is secure. For more information on setting up code scanning, see [Configuring default setup for code scanning](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning).
## [Example scenario](https://docs.github.com/en/copilot/copilot-chat-cookbook/security-analysis/finding-existing-vulnerabilities-in-code#example-scenario)
The JavaScript code below has a potential XSS vulnerability that could be exploited if the `name` parameter is not properly sanitized before being displayed on the page.
```
function displayName(name) {
  const nameElement = document.getElementById('name-display');
  nameElement.innerHTML = `Showing results for "${name}"`
}

```

## [Example prompt](https://docs.github.com/en/copilot/copilot-chat-cookbook/security-analysis/finding-existing-vulnerabilities-in-code#example-prompt)
You can ask Copilot Chat to analyze code for common security vulnerabilities and provide explanations and fixes for the issues it finds.
`Analyze this code for potential security vulnerabilities and suggest fixes.`
## [Example response](https://docs.github.com/en/copilot/copilot-chat-cookbook/security-analysis/finding-existing-vulnerabilities-in-code#example-response)
The following response is an example. Copilot Chat responses are non-deterministic, so you may get a different response from the one shown here.
Copilot responds with an explanation of the vulnerability, and suggested changes to the code to fix it.
```
function displayName(name) {
  const nameElement = document.getElementById('name-display');
  nameElement.textContent = `Showing results for "${name}"`;
}

```

## [Further reading](https://docs.github.com/en/copilot/copilot-chat-cookbook/security-analysis/finding-existing-vulnerabilities-in-code#further-reading)
  * [Prompt engineering for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)
  * [Best practices for using GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)
  * [About code scanning](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning)


