  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Build Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions "Build Copilot Extensions")/
  * [Build a Copilot skillset](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-skillset-for-your-copilot-extension "Build a Copilot skillset")/
  * [About Copilot skillsets](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-skillset-for-your-copilot-extension/about-copilot-skillsets "About Copilot skillsets")


# About Copilot skillsets
Learn what Github Copilot skillsets are and how they simplify integrating third-party tools and functions into your Copilot experience.
## In this article
  * [How skillsets and agents differ](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-skillset-for-your-copilot-extension/about-copilot-skillsets#how-skillsets-and-agents-differ)
  * [The extensibility platform](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-skillset-for-your-copilot-extension/about-copilot-skillsets#the-extensibility-platform)


A skill within GitHub Copilot is a tool that the model calls to perform a specific task in response to a user query. A skillset is a collection of these skills (up to five per skillset). Github Copilot skillsets provide a streamlined way to extend Copilot’s functionality, allowing builders to integrate external services or custom API endpoints into their Copilot workflow. With skillsets, builders can enable Copilot to perform tasks—such as retrieving data or executing actions in third-party services—without needing to manage complex workflows or architecture.
For a quickstart example of a skillset, see the [skillset-example](https://github.com/copilot-extensions/skillset-example) repository. For information on building a skillset, see [Building Copilot skillsets](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-skillset-for-your-copilot-extension/building-copilot-skillsets).
## [How skillsets and agents differ](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-skillset-for-your-copilot-extension/about-copilot-skillsets#how-skillsets-and-agents-differ)
Skillsets and agents are the two ways to extend Copilot's capabilities and context through the Copilot Extensibility Platform. They let you integrate external services and APIs into Copilot Chat, but each one serves different use cases and offers different levels of control and complexity:
  * **Skillsets** are lightweight and streamlined, designed for developers who need Copilot to perform specific tasks (e.g., data retrieval or simple operations) with minimal setup. They handle routing, prompt crafting, function evaluation, and response generation automatically, making them ideal for quick and straightforward integrations.
  * **Agents** are for complex integrations that need full control over how requests are processed and responses are generated. They let you implement custom logic, integrate with other LLMs and/or the Copilot API, manage conversation context, and handle all aspects of the user interaction. While Agents require more engineering and maintenance, they offer maximum flexibility for sophisticated workflows. For more information about agents, see [About Copilot agents](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/about-copilot-agents).


## [The extensibility platform](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-skillset-for-your-copilot-extension/about-copilot-skillsets#the-extensibility-platform)
Skillsets and agents both operate on the GitHub Copilot Extensibility Platform, which manages the flow of user requests and function evaluations. With Copilot skillsets, the platform handles routing, prompt crafting, function calls and prompt generation.
### [Workflow overview](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-skillset-for-your-copilot-extension/about-copilot-skillsets#workflow-overview)
The extensibility platform follows a structured workflow to process user requests and generate responses:
  1. **User request**  
A user issues a request in the Copilot Chat interface, such as asking for data or executing a specific action.
  2. **Routing**  
The request is routed to the appropriate extension. For skillsets, this means the platform agent identifies and invokes the corresponding skillset based on the user’s intent. Each skill’s inference description helps the platform determine which skill to call.
  3. **Dynamic Prompt Crafting**  
GitHub Copilot generates a prompt using:
     * The user’s query.
     * Relevant thread history.
     * Available functions within the skillset.
     * Results from any prior function calls.
  4. **LLM Completion**  
The language model (LLM) processes the prompt and determines:
     * Whether the user’s intent matches a skillset function.
     * Which function(s) to call and with what arguments.
     * If required, the LLM may send additional function calls to gather more context.
  5. **Function Evaluation**  
The extension invokes the selected function(s), which may involve:
     * Gathering relevant context, such as Copilot skillsets repository or user metadata.
     * Making an API call to an external service to retrieve data or execute an action.
  6. **Response generation** The platform iteratively refines the output, looping through prompt crafting, LLM completion, and function evaluation as needed. Once the process is complete, Copilot streams a final response back to the user in the chat interface.


