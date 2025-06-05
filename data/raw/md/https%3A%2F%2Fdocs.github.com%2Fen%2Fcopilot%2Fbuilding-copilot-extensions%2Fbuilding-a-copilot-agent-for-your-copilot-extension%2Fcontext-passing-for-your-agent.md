  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Build Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions "Build Copilot Extensions")/
  * [Build a Copilot agent](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension "Build a Copilot agent")/
  * [Context passing](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/context-passing-for-your-agent "Context passing")


# Context passing for your agent
Learn how to use context passing with your Copilot agent.
## In this article
  * [About context passing](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/context-passing-for-your-agent#about-context-passing)
  * [Prerequisites](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/context-passing-for-your-agent#prerequisites)
  * [Understanding context passing](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/context-passing-for-your-agent#understanding-context-passing)
  * [Example references](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/context-passing-for-your-agent#example-references)
  * [Setting up context passing](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/context-passing-for-your-agent#setting-up-context-passing)
  * [Privacy controls](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/context-passing-for-your-agent#privacy-controls)


## [About context passing](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/context-passing-for-your-agent#about-context-passing)
GitHub Copilot Extensions can access certain contextual information using context passing. Context passing allows agents to receive relevant details about a user’s current file, selected text, and repository. It happens automatically when you interact with an extension, but requires your explicit authorization through GitHub App permissions for use in any organization-owned repositories.
Different clients, such as GitHub Copilot Chat in Visual Studio Code, Visual Studio, and GitHub, provide context through different reference types. For example, IDEs send information such as file contents and selections, while Copilot Chat in GitHub includes the current URL for the page being viewed.
## [Prerequisites](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/context-passing-for-your-agent#prerequisites)
Before you configure your Copilot agent to communicate with GitHub, you should understand how your Copilot agent communicates with the Copilot platform. See [Configuring your Copilot agent to communicate with the Copilot platform](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/configuring-your-copilot-agent-to-communicate-with-the-copilot-platform).
## [Understanding context passing](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/context-passing-for-your-agent#understanding-context-passing)
Context passing enables agents to receive information about the user’s active workspace. Your agent receives server-sent events (SSEs) that contain a list of messages from the user as well as references to the user’s current environment. Depending on the client, different types of context are provided.
The following table shows the reference types that are passed to GitHub Copilot Extensions based on the client or IDE you are using.
Client or IDE | client.file | client.selection | github.repository | github.current-url | Additional contexts  
---|---|---|---|---|---  
Visual Studio Code | Yes | Yes | Yes | No | Repository owner and branch  
Visual Studio | Yes | Yes | Yes | No | Repository owner and branch  
GitHub.com | No | No | Yes | Yes | Repository information and other GitHub resources  
GitHub Mobile | No | No | No | Yes | Not applicable  
### [Reference types for Copilot Chat in IDEs](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/context-passing-for-your-agent#reference-types-for-copilot-chat-in-ides)
The following reference types can be passed to your agent from an IDE:
  * `client.file`: Represents the full content of the currently active file in the IDE.
  * `client.selection`: Represents the selected portion of text the user highlighted in the active file.
  * `github.repository`: Provides information about the active repository.


### [Reference types for Copilot Chat in GitHub](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/context-passing-for-your-agent#reference-types-for-copilot-chat-in-github)
The following reference types can be passed to your agent from GitHub:
  * `github.current-url`: Represents the URL of the current GitHub page the user is viewing.
  * `github.repository`: Provides information about the active repository.


## [Example references](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/context-passing-for-your-agent#example-references)
The following code shows an example object for `client.file`:
```
{
    // The reference type.
    "type": "client.file",
    "data": {
        // The full content of the active file. 
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
        "language": "plaintext"
    },
    "id": "relative-path/to/file",
    // `is_implicit` indicates whether the reference was automatically provided by the client (true) or manually attached by the user (false).
    "is_implicit": true,
    "metadata": {
        "display_name": "https://github.com/example-user/example-repository",
        "display_icon": "",
        "display_url": ""
    }
}

```

The following code shows an example object for `client.selection`:
```
{
    // The reference type.
    "type": "client.selection",
    "data": {
        // The currently selected portion of text.
        "content": "<current selection>",
        "end": {
            "col": 80,
            "line": 10
        },
        "start": {
            "col": 0,
            "line": 0
        }
    },
    "id": "relative-path/to/file",
    // `is_implicit` indicates whether the reference was automatically provided by the client (true) or manually attached by the user (false).
    "is_implicit": true,
    "metadata": {
        "display_name": "https://github.com/example-user/example-repository",
        "display_icon": "",
        "display_url": ""
    }
}

```

The following code shows an example object for `github.repository`:
```
{
    // The reference type.
    "type": "github.repository",
    "data": {
        "type": "repository",
        "id": "abc-123",
        "name": "example-repository",
        "ownerLogin": "example-user",
        "ownerType": "",
        "readmePath": "",
        "description": "",
        "commitOID": "",
        "ref": "",
        "refInfo": {
            "name": "",
            "type": ""
        },
        "visibility": "",
        "languages": null
    },
    "id": "example-user/example-repository",
    // `is_implicit` is always false for github.repository.
    "is_implicit": false,
    "metadata": {
        "display_name": "https://github.com/example-user/example-repository",
        "display_icon": "",
        "display_url": ""
    }
}

```

The following code shows an example object for `github.current-url`:
```
{
    // The reference type.
    "type": "github.current-url",
    "data": {
        // The GitHub URL the user was on while chatting with the agent.
        "url": "https://github.com/example-user/example-repository"
    },
    "id": "https://github.com/example-user/example-repository",
    // `is_implicit` is always true for github.current-url.
    "is_implicit": true,
    "metadata": {
        "display_name": "https://github.com/example-user/example-repository",
        "display_icon": "",
        "display_url": ""
    }
}

```

## [Setting up context passing](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/context-passing-for-your-agent#setting-up-context-passing)
To enable context passing through an IDE client, the **Copilot Editor Context** permission must be configured for your agent. This permission only controls access for the `client.file` and `client.selection` reference types. Users that install and use the agent will be clearly informed that the agent has read access to Copilot Editor Context which includes content such as active file and current selection.
`github.current-url` and `github.repository` are unaffected by the Copilot Editor Context. These reference types rely on authorization filtering to ensure third party agents only receive references they have access to. For information on managing the privacy of `github.current-url` and `github.repository`, see [Privacy controls](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/context-passing-for-your-agent#privacy-controls).
Follow these steps to set the necessary permissions for context passing from IDEs to your agent:
  1. In the upper-right corner of any page on GitHub, click your profile photo.
  2. Navigate to your account settings. 
     * For an app owned by a personal account, click **Settings**.
     * For an app owned by an organization: 
       1. Click **Your organizations**.
       2. To the right of the organization, click **Settings**.
  3. In the left sidebar, click 
  4. In the left sidebar, click **GitHub Apps**.
  5. In the list of GitHub Apps, click the GitHub App you want to configure for context passing.
  6. In the navigation menu on the left, select **Permissions & events**.
  7. Under **Account Permissions** , select **Read-only** access for **Copilot Editor Context**.


## [Privacy controls](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/context-passing-for-your-agent#privacy-controls)
In cases where you don't want to share certain context details with the agent, you can redact and remove reference types in multiple ways.
### [Chat in IDEs](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/context-passing-for-your-agent#chat-in-ides)
  * If an agent doesn't have the Copilot Editor Context read-access permission, all `client.*` references are removed.
  * If an agent doesn't have read access to a repository, all `client.*` references are removed and the `github.repository` reference is redacted.


Visual Studio and Visual Studio Code provides an option to exclude content from the current file. The `client.*` reference types are removed if the user has excluded content from the current file.
### [Chat in GitHub](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/context-passing-for-your-agent#chat-in-github)
  * If an agent doesn't have read access to the repository associated with the current GitHub URL, the `github.current-url` and `github.repository` references are redacted.
  * If repository information cannot be extracted from the current GitHub URL, `github.current-url` is redacted.


### [Redacted references](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/context-passing-for-your-agent#redacted-references)
When a reference is redacted due to insufficient permissions, it is replaced with a placeholder indicating the type of information that was excluded. In the following example, the `type` field indicates that the reference has been redacted and the `data.type` field reveals the original reference type.
```
{
    "role": "user",
    "content": "Current Date and Time (UTC): 2024-10-22 00:43:14\nCurrent User's Login: monalisa\n",
    "name": "_session",
    "copilot_references": [
        {
            "type": "github.redacted",
            "data": {
                "type": "github.current-url"
            },
            "id": "example-id",
            "is_implicit": true,
            "metadata": {
                "display_name": "",
                "display_icon": "",
                "display_url": ""
            }
        }
    ],
    "copilot_confirmations": null
}

```

### [Context Exclusions](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/context-passing-for-your-agent#context-exclusions)
To safeguard sensitive information, certain scenarios automatically prevent the passing of context to agents. If an organization has set content exclusion rules for Copilot, files that fall under these rules will not be included in the context passed to agents.
For more information on content exlusion rules, see [Excluding content from GitHub Copilot](https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion/excluding-content-from-github-copilot).
#### [Large Files](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/context-passing-for-your-agent#large-files)
Files exceeding the size limit set by the client will not be sent. The reference will include metadata indicating that the file was too large to process.
#### [Hidden Files](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/context-passing-for-your-agent#hidden-files)
Files beginning with a dot, such as `.env` and `.config`, are excluded by default to prevent unintentional sharing of sensitive configurations. In VS Code, you can specify files or directories in a `.copilotignore` file to prevent them from being sent to Copilot agents. This client-side mechanism offers granular control over which files are excluded.
