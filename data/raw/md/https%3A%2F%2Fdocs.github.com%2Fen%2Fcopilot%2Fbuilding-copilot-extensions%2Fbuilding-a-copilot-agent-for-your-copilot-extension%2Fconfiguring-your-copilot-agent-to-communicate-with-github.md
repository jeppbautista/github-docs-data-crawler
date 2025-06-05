  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Build Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions "Build Copilot Extensions")/
  * [Build a Copilot agent](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension "Build a Copilot agent")/
  * [Communicate with GitHub](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/configuring-your-copilot-agent-to-communicate-with-github "Communicate with GitHub")


# Configuring your Copilot agent to communicate with GitHub
Learn how to verify payloads and get resources from GitHub with your Copilot agent.
## In this article
  * [Prerequisites](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/configuring-your-copilot-agent-to-communicate-with-github#prerequisites)
  * [Verifying that payloads are coming from GitHub](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/configuring-your-copilot-agent-to-communicate-with-github#verifying-that-payloads-are-coming-from-github)
  * [Fetching resources from the GitHub API](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/configuring-your-copilot-agent-to-communicate-with-github#fetching-resources-from-the-github-api)


## [Prerequisites](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/configuring-your-copilot-agent-to-communicate-with-github#prerequisites)
Before you configure your Copilot agent to communicate with GitHub, you should understand how your Copilot agent communicates with the Copilot platform. See [Configuring your Copilot agent to communicate with the Copilot platform](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/configuring-your-copilot-agent-to-communicate-with-the-copilot-platform).
## [Verifying that payloads are coming from GitHub](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/configuring-your-copilot-agent-to-communicate-with-github#verifying-that-payloads-are-coming-from-github)
Before your Copilot agent begins processing a request, you should verify that the request came from GitHub, and that it is intended for your agent. All agent requests contain the `X-GitHub-Public-Key-Identifier` and `X-GitHub-Public-Key-Signature` headers. To verify the signature for a particular request, compare the signature in the `X-GitHub-Public-Key-Signature` header with a signed copy of the request body using the current public key listed at <https://api.github.com/meta/public_keys/copilot_api>.
For more details and examples of signature verification in specific languages, see the [`github-technology-partners/signature-verification`](https://github.com/github-technology-partners/signature-verification) repository.
> ⚠️ **Note:** We currently send duplicate pairs of these headers. One set has the prefix `Github-Public-...`; the other has `X-GitHub-Public...`. The former will be closing down **by March 31st**. Please update your relevant checks to the correct prefix (`X-GitHub-Public...`) by then.
## [Fetching resources from the GitHub API](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/configuring-your-copilot-agent-to-communicate-with-github#fetching-resources-from-the-github-api)
Requests to your Copilot agent will receive an `X-GitHub-Token` header. This header contains an API token that can be used to fetch resources from the GitHub API on behalf of the user interacting with your agent. The permissions of this token are the overlap of the user's own permissions and the permissions granted to your GitHub App installation.
For an example of how you might use `X-GitHub-Token`, see the following code sample:
```
async function whoami(req) {
  const response = await fetch(
    // The GitHub API endpoint for the authenticated user
    "https://api.github.com/user",
    {
      headers: {
        "Authorization": `Bearer ${req.headers.get("x-github-token")}`
      }
    }
  )

  const user = await response.json()
  return user
}

```

To learn more about working with GitHub's API and explore official software development kits (SDKs), see the [`octokit`](https://github.com/octokit) organization.
