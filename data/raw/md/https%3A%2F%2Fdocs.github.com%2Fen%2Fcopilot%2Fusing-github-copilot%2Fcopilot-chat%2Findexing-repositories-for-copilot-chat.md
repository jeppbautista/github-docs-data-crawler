  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Use GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot "Use GitHub Copilot")/
  * [Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat "Copilot Chat")/
  * [Semantic indexing](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/indexing-repositories-for-copilot-chat "Semantic indexing")


# Indexing repositories for Copilot Chat
GitHub Copilot Chat improves responses to questions about code by indexing your repositories.
## In this article
  * [Benefit of indexing repositories](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/indexing-repositories-for-copilot-chat#benefit-of-indexing-repositories)
  * [About index creation and use](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/indexing-repositories-for-copilot-chat#about-index-creation-and-use)
  * [Excluding content from Copilot Chat answers](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/indexing-repositories-for-copilot-chat#excluding-content-from-copilot-chat-answers)


## [Benefit of indexing repositories](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/indexing-repositories-for-copilot-chat#benefit-of-indexing-repositories)
Copilot Chat's ability to answer natural language questions in a repository context is optimized when the semantic code search index for the repository is up to date.
When you start a conversation with Copilot Chat that has a repository context, the repository is automatically indexed to improve context-enriched answers to your questions about the code's structure and logic in GitHub and Visual Studio Code. For example, you can ask **“How does this repo manage HTTP requests and responses?”** and Copilot Chat will reference relevant sections of your code to deliver an informed answer.
**Copilot Chat will not use your indexed repository for model training.**
For more information on how to ask questions, see [Asking GitHub Copilot questions in GitHub](https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-github).
## [About index creation and use](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/indexing-repositories-for-copilot-chat#about-index-creation-and-use)
Indexing runs in the background and initial indexing can take up to 60 seconds for a large repository. Once a repository has been indexed for the first time, re-indexing is much quicker and the index will typically be automatically updated to include the latest changes within seconds of you starting a new conversation.
Once an index has been created for a repository, Copilot Chat uses it to answer questions asked by any Copilot user in GitHub and Visual Studio Code.
There is no limit to how many repositories you can index.
## [Excluding content from Copilot Chat answers](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/indexing-repositories-for-copilot-chat#excluding-content-from-copilot-chat-answers)
Enterprise or organization owners with a Copilot Enterprise or Copilot Business plan can define content exclusions to control the behavior of GitHub Copilot for the Copilot seats they manage. For more information, see [Excluding content from GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/setting-policies-for-copilot-in-your-organization/excluding-content-from-github-copilot).
If a semantic code search index is created for a repository that is included in a content exclusion policy, data is filtered according to the policy before being passed to Copilot Chat.
