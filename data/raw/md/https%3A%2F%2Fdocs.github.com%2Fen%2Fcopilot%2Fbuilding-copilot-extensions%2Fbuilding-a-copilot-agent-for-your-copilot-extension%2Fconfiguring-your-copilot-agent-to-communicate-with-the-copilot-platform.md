  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Build Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions "Build Copilot Extensions")/
  * [Build a Copilot agent](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension "Build a Copilot agent")/
  * [Communicate with Copilot platform](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/configuring-your-copilot-agent-to-communicate-with-the-copilot-platform "Communicate with Copilot platform")


# Configuring your Copilot agent to communicate with the Copilot platform
Learn how to interact with the Copilot platform by sending and receiving server-sent events with your Copilot agent.
## In this article
  * [Sending server-sent events](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/configuring-your-copilot-agent-to-communicate-with-the-copilot-platform#sending-server-sent-events)
  * [Receiving server-sent events](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/configuring-your-copilot-agent-to-communicate-with-the-copilot-platform#receiving-server-sent-events)
  * [Next steps](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/configuring-your-copilot-agent-to-communicate-with-the-copilot-platform#next-steps)


Copilot agents communicate with the Copilot platform in the form of server-sent events (SSEs). Rather than waiting for the Copilot platform to request an update from your agent, or vice versa, you can use SSEs to send and receive updates to and from the platform in real time.
To learn more about SSEs, see [Server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events) in the mdn documentation.
## [Sending server-sent events](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/configuring-your-copilot-agent-to-communicate-with-the-copilot-platform#sending-server-sent-events)
Your agent should only send one SSE for each interaction with the Copilot platform. There are four predefined SSEs your agent can send:
  * [`copilot_confirmation`](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/configuring-your-copilot-agent-to-communicate-with-the-copilot-platform#copilot_confirmation)
  * [`copilot_errors`](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/configuring-your-copilot-agent-to-communicate-with-the-copilot-platform#copilot_errors)
  * [`copilot_references`](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/configuring-your-copilot-agent-to-communicate-with-the-copilot-platform#copilot_references)
  * [Default SSE](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/configuring-your-copilot-agent-to-communicate-with-the-copilot-platform#default-sse)


### [`copilot_confirmation`](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/configuring-your-copilot-agent-to-communicate-with-the-copilot-platform#copilot_confirmation)
The `copilot_confirmation` SSE sends the user a prompt to confirm an action. This SSE is sent through an event type and data field. See the following code for an example of a `copilot_confirmation` SSE:
TypeScript
BesideInline
```
//
event: copilot_confirmation
data: {
    // Currently, `action` is the only supported value for `type` in `copilot_confirmation`.
    "type": "action",
    // Title of the confirmation dialog shown to the user.
    "title": "Turn off feature flag",
    // Confirmation message shown to the user.
    "message": "Are you sure you wish to turn off the `copilot` feature flag?",
    // Optional field for the agent to include any data needed to uniquely identify this confirmation and take action once the decision is received from the client.
    "confirmation": {
        "id": "id-123",
        "other": "identifier-as-needed",
    }
}

```

```
event: copilot_confirmation
data: {
```

```
    "type": "action",
```

Currently, `action` is the only supported value for `type` in `copilot_confirmation`.
```
    "title": "Turn off feature flag",
```

Title of the confirmation dialog shown to the user.
```
    "message": "Are you sure you wish to turn off the `copilot` feature flag?",
```

Confirmation message shown to the user.
```
    "confirmation": {
        "id": "id-123",
        "other": "identifier-as-needed",
    }
}
```

Optional field for the agent to include any data needed to uniquely identify this confirmation and take action once the decision is received from the client.
```
//
event: copilot_confirmation
data: {
    // Currently, `action` is the only supported value for `type` in `copilot_confirmation`.
    "type": "action",
    // Title of the confirmation dialog shown to the user.
    "title": "Turn off feature flag",
    // Confirmation message shown to the user.
    "message": "Are you sure you wish to turn off the `copilot` feature flag?",
    // Optional field for the agent to include any data needed to uniquely identify this confirmation and take action once the decision is received from the client.
    "confirmation": {
        "id": "id-123",
        "other": "identifier-as-needed",
    }
}

```

After the user accepts or dismisses the confirmation, the agent receives a message similar to the following example:
TypeScript
BesideInline
```
//
{
    "copilot_confirmations": [
        {
            // A string containing the state of the confirmation. This value is either `accepted` or `dismissed`.
            "state": "accepted",
            // An array of strings containing data identifying the relevant action.
            "confirmation": {
                "id": "id-123",
                "other": "identifier-as-needed",
            }
        }
    ]
}

```

```
{
    "copilot_confirmations": [
        {
```

```
            "state": "accepted",
```

A string containing the state of the confirmation. This value is either `accepted` or `dismissed`.
```
            "confirmation": {
                "id": "id-123",
                "other": "identifier-as-needed",
            }
        }
    ]
}
```

An array of strings containing data identifying the relevant action.
```
//
{
    "copilot_confirmations": [
        {
            // A string containing the state of the confirmation. This value is either `accepted` or `dismissed`.
            "state": "accepted",
            // An array of strings containing data identifying the relevant action.
            "confirmation": {
                "id": "id-123",
                "other": "identifier-as-needed",
            }
        }
    ]
}

```

Based on the values in this message, the agent can then complete or cancel the appropriate action.
### [`copilot_errors`](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/configuring-your-copilot-agent-to-communicate-with-the-copilot-platform#copilot_errors)
The `copilot_errors` SSE sends the Copilot platform a list of encountered errors. This SSE is sent through an event type and data field. See the following code for an example of a `copilot_errors` SSE:
TypeScript
BesideInline
```
//
event: copilot_errors
data: [{
    // A string that specifies the error's type. `type` can have a value of `reference`, `function` or `agent`.
    "type": "function",
    // A string controlled by the agent describing the nature of an error.
    "code": "recentchanges",
    // A string that specifies the error message shown to the user.
    "message": "The repository does not exist",
    // A string that serves as a unique identifier to link the error with other resources such as references or function calls.
    "identifier": "github/hello-world"
}]

```

```
event: copilot_errors
data: [{
```

```
    "type": "function",
```

A string that specifies the error's type. `type` can have a value of `reference`, `function` or `agent`.
```
    "code": "recentchanges",
```

A string controlled by the agent describing the nature of an error.
```
    "message": "The repository does not exist",
```

A string that specifies the error message shown to the user.
```
    "identifier": "github/hello-world"
}]
```

A string that serves as a unique identifier to link the error with other resources such as references or function calls.
```
//
event: copilot_errors
data: [{
    // A string that specifies the error's type. `type` can have a value of `reference`, `function` or `agent`.
    "type": "function",
    // A string controlled by the agent describing the nature of an error.
    "code": "recentchanges",
    // A string that specifies the error message shown to the user.
    "message": "The repository does not exist",
    // A string that serves as a unique identifier to link the error with other resources such as references or function calls.
    "identifier": "github/hello-world"
}]

```

### [`copilot_references`](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/configuring-your-copilot-agent-to-communicate-with-the-copilot-platform#copilot_references)
Rendering references is currently unsupported for Copilot Chat in GitHub Mobile. Extensions that depend on reference memory to generate responses will still work, but the references will not be displayed to the user.
The `copilot_references` SSE sends the user a list of references used to generate a response. This SSE is sent through an event type and data field. See the following code for an example of a `copilot_references` SSE:
TypeScript
BesideInline
```
//
event: copilot_references
data: [{
    // A string that specifies the type of the reference.
    "type": "blackbeard.story",
    // A string that specifies the ID of the reference.
    "id": "snippet",
    // An optional field where the agent can include any data needed to uniquely identify this reference.
    "data": {
        "file": "story.go",
        "start": "0",
        "end": "13",
        "content": "func main()...writeStory()..."
    },
    // An optional boolean that indicates if the reference was passed implicitly or explicitly.
    "is_implicit": false,
    // An optional field for the agent to include any metadata to display in the user's environment. If any of the below required fields are missing, then the reference will not be rendered in the UI.
    "metadata": {
        "display_name": "Lines 1-13 from story.go",
        "display_icon": "icon",
        "display_url": "http://blackbeard.com/story/1",

    }
}]

```

```
event: copilot_references
data: [{
```

```
    "type": "blackbeard.story",
```

A string that specifies the type of the reference.
```
    "id": "snippet",
```

A string that specifies the ID of the reference.
```
    "data": {
        "file": "story.go",
        "start": "0",
        "end": "13",
        "content": "func main()...writeStory()..."
    },
```

An optional field where the agent can include any data needed to uniquely identify this reference.
```
    "is_implicit": false,
```

An optional boolean that indicates if the reference was passed implicitly or explicitly.
```
    "metadata": {
        "display_name": "Lines 1-13 from story.go",
        "display_icon": "icon",
        "display_url": "http://blackbeard.com/story/1",
    }
}]
```

An optional field for the agent to include any metadata to display in the user's environment. If any of the below required fields are missing, then the reference will not be rendered in the UI.
```
//
event: copilot_references
data: [{
    // A string that specifies the type of the reference.
    "type": "blackbeard.story",
    // A string that specifies the ID of the reference.
    "id": "snippet",
    // An optional field where the agent can include any data needed to uniquely identify this reference.
    "data": {
        "file": "story.go",
        "start": "0",
        "end": "13",
        "content": "func main()...writeStory()..."
    },
    // An optional boolean that indicates if the reference was passed implicitly or explicitly.
    "is_implicit": false,
    // An optional field for the agent to include any metadata to display in the user's environment. If any of the below required fields are missing, then the reference will not be rendered in the UI.
    "metadata": {
        "display_name": "Lines 1-13 from story.go",
        "display_icon": "icon",
        "display_url": "http://blackbeard.com/story/1",

    }
}]

```

### [Default SSE](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/configuring-your-copilot-agent-to-communicate-with-the-copilot-platform#default-sse)
The default SSE sends the user a general chat message. This SSE is unnamed and sent solely through a data field. See the following code for an example of a default SSE:
```
data: {"id":"chatcmpl-123","object":"chat.completion.chunk","created":1694268190,"model":"gpt-3.5-turbo-0125", "system_fingerprint": "fp_44709d6fcb", "choices":[{"index":0,"delta":{"role":"assistant","content":""},"logprobs":null,"finish_reason":null}]}

```

## [Receiving server-sent events](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/configuring-your-copilot-agent-to-communicate-with-the-copilot-platform#receiving-server-sent-events)
Just as your agent sends SSEs to the Copilot platform, it also receives the `resp_message` SSE from the platform. This SSE contains a list of messages from the user, as well as optional data related to each of the SSE events the agent can send. See the following code sample for an example curl request to your agent containing a message:
```
curl --request POST \
    --url $AGENT_URL \
    --header 'Accept: application/json' \
    --header 'Content-Type: application/json' \
    --header "X-GitHub-Token: $RUNTIME_GENERATED_TOKEN" \
    --data '{
        "messages": [
            {
                "role": "user",
                "content": "What is a closure in javascript?",
                "copilot_references": []
            }
        ]
    }'

```

## [Next steps](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/configuring-your-copilot-agent-to-communicate-with-the-copilot-platform#next-steps)
Now that you understand how your Copilot agent communicates with the Copilot platform, you can learn how to integrate your agent with the GitHub API. See [Configuring your Copilot agent to communicate with GitHub](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/configuring-your-copilot-agent-to-communicate-with-github).
