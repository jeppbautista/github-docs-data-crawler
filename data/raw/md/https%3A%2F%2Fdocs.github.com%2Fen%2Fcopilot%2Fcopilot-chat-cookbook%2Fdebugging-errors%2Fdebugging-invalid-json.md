  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Copilot Chat Cookbook](https://docs.github.com/en/copilot/copilot-chat-cookbook "Copilot Chat Cookbook")/
  * [Debugging errors](https://docs.github.com/en/copilot/copilot-chat-cookbook/debugging-errors "Debugging errors")/
  * [Debug invalid JSON](https://docs.github.com/en/copilot/copilot-chat-cookbook/debugging-errors/debugging-invalid-json "Debug invalid JSON")


# Debugging invalid JSON
Copilot Chat can identify and resolve syntax errors or structural issues in JSON data.
## In this article
  * [Example scenario](https://docs.github.com/en/copilot/copilot-chat-cookbook/debugging-errors/debugging-invalid-json#example-scenario)
  * [Example prompt](https://docs.github.com/en/copilot/copilot-chat-cookbook/debugging-errors/debugging-invalid-json#example-prompt)
  * [Example response](https://docs.github.com/en/copilot/copilot-chat-cookbook/debugging-errors/debugging-invalid-json#example-response)
  * [Further reading](https://docs.github.com/en/copilot/copilot-chat-cookbook/debugging-errors/debugging-invalid-json#further-reading)


When working with JSON data, you may encounter issues such as trailing commas, mismatched braces, or incorrect data types that make the JSON invalid. GitHub Copilot Chat can help you debug and fix these errors by suggesting corrections to fix invalid JSON.
## [Example scenario](https://docs.github.com/en/copilot/copilot-chat-cookbook/debugging-errors/debugging-invalid-json#example-scenario)
Consider a scenario where an application consumes JSON data from an API, but the response fails to parse due to invalid formatting. You receive the error message:
```
Error: Parse error
----------------------^
Expecting 'STRING', 'NUMBER', 'NULL', 'TRUE', 'FALSE', '{', '[', got 'undefined'

```

Below is the JSON data that caused the error:
```
{
  "location": "San Francisco",
  "current_weather": {
    "temperature": 18,
    "unit": "Celsius",
    "conditions": "Cloudy
  },
  "forecast": {
    "day": "Monday",
    "high": 22,
    "low": 15,
    "precipitation": 10
  }
}

```

## [Example prompt](https://docs.github.com/en/copilot/copilot-chat-cookbook/debugging-errors/debugging-invalid-json#example-prompt)
`Why is my JSON object invalid and how can I fix it?`
## [Example response](https://docs.github.com/en/copilot/copilot-chat-cookbook/debugging-errors/debugging-invalid-json#example-response)
The following response is an example. Copilot Chat responses are non-deterministic, so you may get a different response from the one shown here.
Copilot might suggest that your JSON is invalid because it's missing a closing quote for the `conditions` value. Here is the corrected JSON:
```
{
  "location": "San Francisco",
  "current_weather": {
    "temperature": 18,
    "unit": "Celsius",
    "conditions": "Cloudy"
  },
  "forecast": {
    "day": "Monday",
    "high": 22,
    "low": 15,
    "precipitation": 10
  }
}

```

In this example response, Copilot's suggestions include fixing the closing quote for the `conditions` value, which resolves the JSON parsing error.
## [Further reading](https://docs.github.com/en/copilot/copilot-chat-cookbook/debugging-errors/debugging-invalid-json#further-reading)
  * [Prompt engineering for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)
  * [Best practices for using GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)


