  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Use GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot "Use GitHub Copilot")/
  * [Copilot Spaces](https://docs.github.com/en/copilot/using-github-copilot/copilot-spaces "Copilot Spaces")/
  * [Create and use Copilot Spaces](https://docs.github.com/en/copilot/using-github-copilot/copilot-spaces/creating-and-using-copilot-spaces "Create and use Copilot Spaces")


# Creating and using Copilot Spaces
Create spaces to organize and centralize relevant content that grounds Copilot’s responses in the right context for a specific task.
## Who can use this feature?
Anyone with a Copilot license can use Spaces.
## In this article
  * [Adding context to Spaces](https://docs.github.com/en/copilot/using-github-copilot/copilot-spaces/creating-and-using-copilot-spaces#adding-context-to-spaces)
  * [Using Spaces](https://docs.github.com/en/copilot/using-github-copilot/copilot-spaces/creating-and-using-copilot-spaces#using-spaces)
  * [Next steps](https://docs.github.com/en/copilot/using-github-copilot/copilot-spaces/creating-and-using-copilot-spaces#next-steps)


Copilot Spaces is in public preview and subject to change.
  1. To create a space, go to <https://github.com/copilot/spaces>, and click **Create space**.
  2. Give your space a name.
  3. Choose whether the space is owned by you or by an organization you belong to. Organization-owned Spaces can be shared using GitHub’s built-in permission model.
  4. Optionally, add a description to help others understand the purpose of the space.
  5. Click **Create**.


## [Adding context to Spaces](https://docs.github.com/en/copilot/using-github-copilot/copilot-spaces/creating-and-using-copilot-spaces#adding-context-to-spaces)
You can add two types of context to your space:
  * **Instructions** : Free text that describes what Copilot should focus on within this space. Include its areas of expertise, what kinds of tasks it should help with, and what it should avoid. This helps Copilot give more relevant responses based on your intent.
For example:
> You are a SQL generator. Your job is to take the sample queries and data schemas defined in the attached files and and generate SQL queries based on the user's goals.
  * **References** : You can add any code hosted in GitHub repositories, including public and private repositories. You can also add free-text content, such as transcripts or notes.
You don’t need formal docs to get value from Spaces. Try pasting in a Slack thread, a video call summary, or even bullet-point notes.


This context will be used to provide more relevant answers to your questions. Additionally, Spaces will always refer to the latest version of the code on the `main` branch of the repository.
## [Using Spaces](https://docs.github.com/en/copilot/using-github-copilot/copilot-spaces/creating-and-using-copilot-spaces#using-spaces)
Once you've added context to your space, you can ask Copilot questions in the chat interface. Your chat will be grounded in the context you've added.
You can also change the large language model (LLM) used for your space by selecting the **CURRENT-MODEL** [Choosing the right AI model for your task](https://docs.github.com/en/copilot/using-github-copilot/ai-models/choosing-the-right-ai-model-for-your-task).
## [Next steps](https://docs.github.com/en/copilot/using-github-copilot/copilot-spaces/creating-and-using-copilot-spaces#next-steps)
  * To learn more about how to use Spaces to help you with development work, see [Speeding up development work with Copilot Spaces](https://docs.github.com/en/copilot/using-github-copilot/copilot-spaces/speeding-up-development-work-with-copilot-spaces).
  * To learn how to share your space with your team, see [Collaborating with your team using Copilot Spaces](https://docs.github.com/en/copilot/using-github-copilot/copilot-spaces/collaborating-with-your-team-using-copilot-spaces).


