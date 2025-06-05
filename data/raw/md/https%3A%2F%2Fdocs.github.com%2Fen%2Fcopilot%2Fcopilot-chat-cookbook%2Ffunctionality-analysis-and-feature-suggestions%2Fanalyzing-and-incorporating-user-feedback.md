  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Copilot Chat Cookbook](https://docs.github.com/en/copilot/copilot-chat-cookbook "Copilot Chat Cookbook")/
  * [Functionality analysis and feature suggestions](https://docs.github.com/en/copilot/copilot-chat-cookbook/functionality-analysis-and-feature-suggestions "Functionality analysis and feature suggestions")/
  * [Incorporate feedback](https://docs.github.com/en/copilot/copilot-chat-cookbook/functionality-analysis-and-feature-suggestions/analyzing-and-incorporating-user-feedback "Incorporate feedback")


# Analyzing and incorporating user feedback
Copilot Chat can enhance the process of incorporating user feedback into your project.
## In this article
  * [Analyzing user feedback](https://docs.github.com/en/copilot/copilot-chat-cookbook/functionality-analysis-and-feature-suggestions/analyzing-and-incorporating-user-feedback#analyzing-user-feedback)
  * [Generating feature specifications](https://docs.github.com/en/copilot/copilot-chat-cookbook/functionality-analysis-and-feature-suggestions/analyzing-and-incorporating-user-feedback#generating-feature-specifications)
  * [Further reading](https://docs.github.com/en/copilot/copilot-chat-cookbook/functionality-analysis-and-feature-suggestions/analyzing-and-incorporating-user-feedback#further-reading)


Gathering and incorporating user feedback is crucial for product development, but it can be a challenging process. Developers and product teams often struggle to effectively analyze user feedback, prioritize it, and implement changes based on that feedback without disrupting existing workflows or introducing new issues.
## [Analyzing user feedback](https://docs.github.com/en/copilot/copilot-chat-cookbook/functionality-analysis-and-feature-suggestions/analyzing-and-incorporating-user-feedback#analyzing-user-feedback)
User feedback can be overwhelming and it may be difficult to identify what you should respond to.
### [Example scenario](https://docs.github.com/en/copilot/copilot-chat-cookbook/functionality-analysis-and-feature-suggestions/analyzing-and-incorporating-user-feedback#example-scenario)
Imagine you are a maintainer of a popular open source repository. Because the community is very invested in your project, they often open issues to provide feedback. They also frequently interact with open issues. You want to respond to this feedback, but you aren't sure where to start.
### [Example prompt](https://docs.github.com/en/copilot/copilot-chat-cookbook/functionality-analysis-and-feature-suggestions/analyzing-and-incorporating-user-feedback#example-prompt)
This example assumes that you use labels to track issues related to user feedback in your repository.
Navigate to the **Issues** tab in your repository, then type:
`Find the issues with the feedback label that have the most reactions, and categorize them based on sentiment.`
To try out this prompt, you can go to the [`microsoft/vscode`](https://github.com/microsoft/vscode/issues) repository, which uses labels to track feature requests, and type: `Find the issues with the feature-request label that have the most reactions, and categorize them based on sentiment.`
### [Example response](https://docs.github.com/en/copilot/copilot-chat-cookbook/functionality-analysis-and-feature-suggestions/analyzing-and-incorporating-user-feedback#example-response)
The following response is an example. Copilot Chat responses are non-deterministic, so you may get a different response from the one shown here.
Copilot lists the issues with the most reactions, and provides a sentiment analysis for each issue. You can use this list to make more informed decisions when you are prioritizing your work.
For example:
```
1. [Feedback] CLI error messages are difficult to understand
  * Issue URL: #321
  * Reactions: 543
  * Sentiment: Negative

1. [Feedback] Add API to enable third party integration
  * Issue URL: #210
  * Reactions: 482
  * Sentiment: Positive

1. [Feedback] Shortcut for --with-token CLI option
  * Issue URL: #426
  * Reactions: 187
  * Sentiment: Neutral to slightly positive

```

## [Generating feature specifications](https://docs.github.com/en/copilot/copilot-chat-cookbook/functionality-analysis-and-feature-suggestions/analyzing-and-incorporating-user-feedback#generating-feature-specifications)
Feature specifications provide a plan for development and are useful for communication and alignment prior to implementing a new feature.
### [Example scenario](https://docs.github.com/en/copilot/copilot-chat-cookbook/functionality-analysis-and-feature-suggestions/analyzing-and-incorporating-user-feedback#example-scenario-1)
In this scenario, you've chosen a piece of user feedback to address. Someone requested a shortcut to an existing CLI option. Now you want to create a plan for how you'll implement this.
### [Example prompt](https://docs.github.com/en/copilot/copilot-chat-cookbook/functionality-analysis-and-feature-suggestions/analyzing-and-incorporating-user-feedback#example-prompt-1)
This example assumes you are asking about an issue in the same repository where you are using Copilot Chat.
`Write a feature specification for Issue #426.`
### [Example response](https://docs.github.com/en/copilot/copilot-chat-cookbook/functionality-analysis-and-feature-suggestions/analyzing-and-incorporating-user-feedback#example-response-1)
The following response is an example. Copilot Chat responses are non-deterministic, so you may get a different response from the one shown here.
Copilot generates a feature specification, similar to the following.
```
# Feature Specification for Issue #426: Shortcut for --with-token CLI option

## Description:
Currently, the --with-token option is used to to pass in a token to commands. Typing --with-token each time is cumbersome. This feature proposes a new flag -wt as a shortcut to quickly specify the --with-token option when running various commands.

## Problem:
Typing --with-token repeatedly is time-consuming and inconvenient for users who frequently use this option.

## Solution:
Introduce a new flag -wt that serves as a shortcut for the --with-token option.

## Feature Details:

### 1. Flag Introduction:
-wt will be introduced as a shorthand for --with-token.
Usage: <command> -wt <token>

### 2. Commands Affected:
All commands that currently support the --with-token option.

### 3. Backward Compatibility:
- The existing --with-token option will continue to work as before.
- No existing functionality will be removed or altered.

### 4. Documentation:
- Update documentation to include the new -wt flag.
- Provide examples and usage scenarios for the new flag.

### 5. Testing:
- Ensure thorough testing of the -wt flag across various commands.
- Test cases should include:
  - Valid and invalid tokens.
  - Interaction with other options.
  - Ensuring no regression in current --with-token functionality.

## Benefits:
- Improved user experience by reducing the amount of typing required.
- Streamlined command execution for users who frequently use the --with-token option.

## Potential Risks:
Minimal risk as this feature is an addition and does not alter existing functionality.

```

## [Further reading](https://docs.github.com/en/copilot/copilot-chat-cookbook/functionality-analysis-and-feature-suggestions/analyzing-and-incorporating-user-feedback#further-reading)
  * [Prompt engineering for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)
  * [Best practices for using GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)


