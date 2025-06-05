  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Build Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions "Build Copilot Extensions")/
  * [Build a Copilot agent](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension "Build a Copilot agent")/
  * [Use Copilot's LLM](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/using-copilots-llm-for-your-agent "Use Copilot's LLM")


# Using Copilot's LLM for your agent
Learn how to use Copilot's LLM for your agent.
## In this article
  * [About Copilot's Large Language Model (LLM)](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/using-copilots-llm-for-your-agent#about-copilots-large-language-model-llm)
  * [Using Copilot's LLM for your agent](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/using-copilots-llm-for-your-agent#using-copilots-llm-for-your-agent)


## [About Copilot's Large Language Model (LLM)](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/using-copilots-llm-for-your-agent#about-copilots-large-language-model-llm)
Copilot's Large Language Model (LLM) is a powerful, large-scale language model that is trained on a diverse range of data sources, including code, documentation, and other text. Copilot's LLM underpins the functionality for GitHub Copilot, and is used to power all of Copilot's features, including code generation, documentation generation, and code completion.
You have the option to use Copilot's LLM to power your agent, which can be useful if you want your agent to be able to generate completions for user messages, but you don't want to manage your own LLM.
Third-party agents have strict rate limits for using Copilot's LLM. If your third-party agent will need to generate a large number of completions, you should consider using your own LLM or an API like OpenAI.
## [Using Copilot's LLM for your agent](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/using-copilots-llm-for-your-agent#using-copilots-llm-for-your-agent)
You can call Copilot's LLM deployment at `https://api.githubcopilot.com/chat/completions` with a POST request. Requests and responses should follow the format as the [OpenAI API](https://platform.openai.com/docs/api-reference/chat/create).
To authenticate, use the same `X-Github-Token` header sent to your agent. For more information, see [Configuring your Copilot agent to communicate with GitHub](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/configuring-your-copilot-agent-to-communicate-with-github#fetching-resources-from-the-github-api).
Here is an example of how Copilot's LLM deployment is used by the Blackbeard extension to generate completions for a user message:
```
  // Use Copilot's LLM to generate a response to the user's
  //  messages, with our extra system messages attached.
  const copilotLLMResponse = await fetch(
    "https://api.githubcopilot.com/chat/completions",
    {
      method: "POST",
      headers: {
        authorization: `Bearer ${tokenForUser}`,
        "content-type": "application/json",
      },
      body: JSON.stringify({
        messages,
        stream: true,
      }),
    }
  );

```

To see this example in its full context, see the [Blackbeard extension](https://github.com/copilot-extensions/blackbeard-extension).
