  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Build Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions "Build Copilot Extensions")/
  * [Debug Copilot Extension](https://docs.github.com/en/copilot/building-copilot-extensions/debugging-your-github-copilot-extension "Debug Copilot Extension")


# Debugging your GitHub Copilot Extension
Learn how to debug your GitHub Copilot Extension from the command line before you publish it.
## In this article
  * [Prerequisites](https://docs.github.com/en/copilot/building-copilot-extensions/debugging-your-github-copilot-extension#prerequisites)
  * [Debugging your Copilot Extension with the CLI](https://docs.github.com/en/copilot/building-copilot-extensions/debugging-your-github-copilot-extension#debugging-your-copilot-extension-with-the-cli)


With the debug tool for Copilot Extensions, you can chat with your Copilot agent from the command line, then view detailed logs as your agent generates a response. You can pass several flags to the tool, with the most important flags being:
  * The `url` flag, which contains the URL to access your Copilot agent. This is the only required flag to start the tool.
  * The `log-level` flag, which determines the level of visibility you have into your Copilot agent's process for generating a response. The available log levels are `DEBUG`, `NONE`, and `TRACE`, and the tool uses `DEBUG` by default.
  * The `token` flag, which must contain a fine-grained personal access token with read access to Copilot Chat if your Copilot agent calls the Copilot LLM. If your agent calls a different LLM, you don't need to use this flag.


## [Prerequisites](https://docs.github.com/en/copilot/building-copilot-extensions/debugging-your-github-copilot-extension#prerequisites)
To use the debug tool, you need to have the GitHub CLI installed on your machine. You can install the GitHub CLI in one of two ways:
  * From the command line using a package manager. For example, to install the GitHub CLI with Homebrew, paste the following command to the command line, then follow the prompts:
Bash```
brew install gh

```
```
brew install gh

```

  * From the [GitHub CLI releases page](https://github.com/cli/cli/releases/tag/v2.56.0)


## [Debugging your Copilot Extension with the CLI](https://docs.github.com/en/copilot/building-copilot-extensions/debugging-your-github-copilot-extension#debugging-your-copilot-extension-with-the-cli)
  1. Optionally, to prepare to debug a specific server-sent event (SSE), add some code to your Copilot agent that sends an SSE when a prompt contains a certain keyword.
The debug tool does not handle the payload verification process. To validate your SSEs, you need to temporarily disable payload verification for local testing, then re-enable it after you have successfully tested your extension.
  2. On the command line, start your Copilot agent.
  3. To authenticate with the GitHub CLI OAuth app, in a new window of your command line application, paste the following command and follow the prompts:
Bash```
gh auth login --web -h github.com

```
```
gh auth login --web -h github.com

```

  4. In the same window, to install the debug tool, paste the following command:
Bash```
gh extension install github.com/copilot-extensions/gh-debug-cli

```
```
gh extension install github.com/copilot-extensions/gh-debug-cli

```

  5. Optionally, for a list of available flags and their descriptions, paste the following command to the command line:
Bash```
gh debug-cli -h

```
```
gh debug-cli -h

```

  6. Optionally, set environment variables for each flag you want to use. Environment variables allow you to set a constant value for a flag rather than passing a value in each time you run the debug tool. For example, if you are using the Blackbeard extension to test the debug tool, you can create an environment variable for the agent URL as follows:
Bash```
export URL="http://localhost:3000"

```
```
export URL="http://localhost:3000"

```

To set an environment variable for a flag, you must use the name of the flag in all caps.
  7. To start the debug tool, paste the following command to the command line, adding any flags you want to use:
Bash```
gh debug-cli

```
```
gh debug-cli

```

The only required flag is the `url` flag, but you will likely want to use additional flags like `log-level` and `token`.
Once the debug tool is running, you should see a message that reads "Start typing to chat with your assistant...".
  8. To interact with your agent, enter a prompt on the command line. The output will vary based on the log level you chose in the previous step, with the `DEBUG` and `TRACE` log levels providing more detailed information.
If you are debugging an SSE, send a prompt containing the keyword you specified in your Copilot agent to trigger the SSE, then analyze the output in your command line application.


