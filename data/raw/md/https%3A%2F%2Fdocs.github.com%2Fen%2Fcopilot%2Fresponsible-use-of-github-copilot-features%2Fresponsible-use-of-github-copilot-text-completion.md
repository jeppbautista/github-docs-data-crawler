  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Responsible use](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features "Responsible use")/
  * [Copilot text completion](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-text-completion "Copilot text completion")


# Responsible use of GitHub Copilot text completion
Learn how to use Copilot text completion responsibly by understanding its purposes, capabilities, and limitations.
## Who can use this feature?
Members of an enterprise with a subscription to GitHub Copilot Enterprise
## In this article
  * [About Copilot text completion](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-text-completion#about-copilot-text-completion)
  * [Use case for pull request text complete](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-text-completion#use-case-for-pull-request-text-complete)
  * [Improving the performance of pull request text complete](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-text-completion#improving-the-performance-of-pull-request-text-complete)
  * [Limitations of pull request text complete](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-text-completion#limitations-of-pull-request-text-complete)
  * [Further reading](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-text-completion#further-reading)


You are currently viewing the documentation for Free, Pro, and Team plans. GitHub Copilot Enterprise is only available to customers on the GitHub Enterprise Cloud plan. For full documentation of Copilot Enterprise, see [What is GitHub Copilot?](https://docs.github.com/en/enterprise-cloud@latest/copilot/github-copilot-enterprise) in the GitHub Enterprise Cloud documentation.
## [About Copilot text completion](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-text-completion#about-copilot-text-completion)
Copilot text completion is an AI-powered feature that allows users to more easily write pull request descriptions by suggesting text as you type.
When you pause briefly while typing a summary, Copilot scans through the pull request and provides suggested prose, attempting to finish your thought.
The only supported language for Copilot text completion is English.
Copilot text completion uses a simple-prompt flow leveraging the Copilot API, utilizing the generic large language model, with no additional trained models.
When you pause during typing the pull request description, a call is generated to the Copilot API to generate suggested text to insert into the description at the current cursor position. The text complete request includes information from the pull request, including the pull request title, any text already in the description, the pull request commit titles, partial raw diffs, and recently viewed pull request and issue titles in a prompt that requests Copilot to generate a suggestion for the next words you are likely to type. The response is then displayed as grayed out text following the cursor. You can accept the suggested text by pressing the tab key, or reject the suggestion by simply continuing to type, or moving the cursor focus out of the description field.
## [Use case for pull request text complete](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-text-completion#use-case-for-pull-request-text-complete)
The goal of Copilot text completion is to help the pull request author to quickly provide context to the human reviewers of the pull request. When reviewing a pull request it is valuable to understand context such as why changes are being requested and how the pull request makes those changes. It may help increase developer productivity by reducing the time taken to open a pull request.
## [Improving the performance of pull request text complete](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-text-completion#improving-the-performance-of-pull-request-text-complete)
The feature is intended to supplement rather than replace a human's work adding context to pull requests. The quality of the text complete suggestions will depend on the quality of the title, the commit messages, and the text already added to the description. We encourage you to continue adding useful context and let Copilot suggest as you go. It remains your responsibility to review and assess the accuracy of information in the pull requests you create.
## [Limitations of pull request text complete](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-text-completion#limitations-of-pull-request-text-complete)
Currently, our team is aware that there are limitations to this feature. Many of them are expected in leveraging our Copilot API; however, there are a few that are specific to Copilot text completion which pertain to limited scope for very large pull requests, and potentially inaccurate responses. We also note that users should expect terms used in their pull request to appear in the AI-generated suggestions.
This feature has been subject to RAI Red Teaming and we will continue to monitor the efficacy and safety of the feature over time. For more information, see [Microsoft AI Red Team building future of safer AI](https://www.microsoft.com/en-us/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/) on the Microsoft security blog.
### [Limited scope](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-text-completion#limited-scope)
It is possible for very large pull requests, that some of the pull request content that the Copilot API relies upon for automatically suggesting text will not fit into the API call, and so for very large pull requests, some of the suggestions you might expect may not occur.
### [Inaccurate responses](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-text-completion#inaccurate-responses)
The more inputs and context that Copilot has to work from, the better the text complete suggestions will be. However, since the feature is quite new, it will take time to reach exact precision with the text complete suggestions that are generated. In the meantime, there may be cases where a generated text complete is less accurate and requires the user to make modifications before saving and publishing their pull request with this description. In addition, there is a risk of "hallucination," where Copilot generates statements that are inaccurate. For these reasons, reviewing is a requirement, and careful review of the output is highly recommended.
### [Replication of pull request content](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-text-completion#replication-of-pull-request-content)
Because a text complete suggestion is drawn from changes that were made in a pull request, if harmful or offensive terms are within the content of the pull request, there is potential for the suggestion to also include those terms.
## [Further reading](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-text-completion#further-reading)
  * [GitHub Copilot Trust Center](https://copilot.github.trust.page/)


