  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Use GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot "Use GitHub Copilot")/
  * [AI models](https://docs.github.com/en/copilot/using-github-copilot/ai-models "AI models")/
  * [Examples for AI model comparison](https://docs.github.com/en/copilot/using-github-copilot/ai-models/comparing-ai-models-using-different-tasks "Examples for AI model comparison")


# Comparing AI models using different tasks
Explore real-world examples of common developer tasks along with sample prompts, responses, and guidance to help you choose the right AI model for your workflow.
## In this article
  * [Overview](https://docs.github.com/en/copilot/using-github-copilot/ai-models/comparing-ai-models-using-different-tasks#overview)
  * [GPT-4o](https://docs.github.com/en/copilot/using-github-copilot/ai-models/comparing-ai-models-using-different-tasks#gpt-4o)
  * [o3-mini](https://docs.github.com/en/copilot/using-github-copilot/ai-models/comparing-ai-models-using-different-tasks#o3-mini)
  * [Gemini 2.0 Flash](https://docs.github.com/en/copilot/using-github-copilot/ai-models/comparing-ai-models-using-different-tasks#gemini-20-flash)
  * [Claude 3.5 Sonnet](https://docs.github.com/en/copilot/using-github-copilot/ai-models/comparing-ai-models-using-different-tasks#claude-35-sonnet)
  * [Claude 3.7 Sonnet](https://docs.github.com/en/copilot/using-github-copilot/ai-models/comparing-ai-models-using-different-tasks#claude-37-sonnet)
  * [Further reading](https://docs.github.com/en/copilot/using-github-copilot/ai-models/comparing-ai-models-using-different-tasks#further-reading)


## [Overview](https://docs.github.com/en/copilot/using-github-copilot/ai-models/comparing-ai-models-using-different-tasks#overview)
Each AI model supported in Copilot Chat has different strengths. To help you decide which model to use, this article provides real-world examples of common developer tasks along with sample prompts, responses, and guidance on why a particular model is a good fit.
These examples show how models vary in their reasoning style, response depth, and ability to handle visual input. Use them to compare output quality and choose the right model for your specific workflow.
For a full list of supported models and side-by-side feature comparisons, see [Choosing the right AI model for your task](https://docs.github.com/en/copilot/using-github-copilot/ai-models/choosing-the-right-ai-model-for-your-task).
## [GPT-4o](https://docs.github.com/en/copilot/using-github-copilot/ai-models/comparing-ai-models-using-different-tasks#gpt-4o)
GPT-4o is a good choice for common development tasks that benefit from speed, responsiveness, and general-purpose reasoning. If you're working on tasks that require broad knowledge, fast iteration, or basic code understanding, GPT-4o is likely the model to use.
### [Example scenario](https://docs.github.com/en/copilot/using-github-copilot/ai-models/comparing-ai-models-using-different-tasks#example-scenario)
Consider a scenario where you are writing helper functions for access control in a Python service. You want to add docstrings to clarify the purpose of the function.
Below is the helper function that grants editor access to a document:
```
def grant_editor_access(user_id, doc_id):
    access = AccessManager()
    access.assign_role(
        resource_type="document",
        resource_id=doc_id,
        role="editor",
        user_id=user_id
    )

```

### [Example prompt](https://docs.github.com/en/copilot/using-github-copilot/ai-models/comparing-ai-models-using-different-tasks#example-prompt)
`Add a docstring to the function that explains what it does.`
### [Example response](https://docs.github.com/en/copilot/using-github-copilot/ai-models/comparing-ai-models-using-different-tasks#example-response)
The following response is an example. Copilot Chat responses are non-deterministic, so you may get a different response from the one shown here.
```
def grant_editor_access(user_id, doc_id):
    """
    Grants editor access to a specific document for a given user.

    This function uses the AccessManager to assign the "editor" role
    to the specified user for the provided document ID.

    Args:
        user_id (str): The ID of the user to grant access to.
        doc_id (str): The ID of the document to which access is being granted.
    """
    access = AccessManager()
    access.assign_role(
        resource_type="document",
        resource_id=doc_id,
        role="editor",
        user_id=user_id
    )

```

### [Why GPT-4o is a good fit](https://docs.github.com/en/copilot/using-github-copilot/ai-models/comparing-ai-models-using-different-tasks#why-gpt-4o-is-a-good-fit)
  * The function is short and self-contained, making it ideal for quick docstring generation.
  * GPT-4o can recognize the pattern and provide a clear, concise explanation.
  * The task doesn't require deep reasoning or complex logic.


## [o3-mini](https://docs.github.com/en/copilot/using-github-copilot/ai-models/comparing-ai-models-using-different-tasks#o3-mini)
OpenAI o3-mini is a fast, cost-effective reasoning model designed to deliver coding performance while maintaining lower latency and resource usage. o3-mini outperforms o1 on coding benchmarks with response times that are comparable to o1-mini. Copilot is configured to use OpenAI's "medium" reasoning effort.
### [Example scenario](https://docs.github.com/en/copilot/using-github-copilot/ai-models/comparing-ai-models-using-different-tasks#example-scenario-1)
Consider a scenario where you are working on a software licensing system. You have a list of user records, each stored as a dictionary with fields like `name`, `active`, and `signup_date`. You want to find only the active users, sorted by their signup date, so that the newest users appear last.
Below is list of users you are working with:
```
users = [
    {"name": "Alice", "active": True, "signup_date": "2023-12-10"},
    {"name": "Bob", "active": False, "signup_date": "2023-11-05"},
    {"name": "Charlie", "active": True, "signup_date": "2024-01-15"}
]

```

### [Example prompt](https://docs.github.com/en/copilot/using-github-copilot/ai-models/comparing-ai-models-using-different-tasks#example-prompt-1)
`Filter the list of users to only include active users, and sort them by signup_date.`
### [Example response](https://docs.github.com/en/copilot/using-github-copilot/ai-models/comparing-ai-models-using-different-tasks#example-response-1)
The following response is an example. Copilot Chat responses are non-deterministic, so you may get a different response from the one shown here.
```
# Filter to only include active users
active_users = [user for user in users if user["active"]]

# Sort active users by signup_date
active_users_sorted = sorted(active_users, key=lambda user: user["signup_date"])

print(active_users_sorted)

```

### [Why o3-mini is a good fit](https://docs.github.com/en/copilot/using-github-copilot/ai-models/comparing-ai-models-using-different-tasks#why-o3-mini-is-a-good-fit)
  * The task involves simple filtering and sorting, which doesn’t require deep reasoning.
  * Its fast responses make it ideal for quick iteration during development.


## [Gemini 2.0 Flash](https://docs.github.com/en/copilot/using-github-copilot/ai-models/comparing-ai-models-using-different-tasks#gemini-20-flash)
Gemini 2.0 Flash supports image input so that developers can bring visual context into tasks like UI inspection, diagram analysis, or layout debugging. This makes Gemini 2.0 Flash particularly useful for scenarios where image-based input enhances problem-solving, such as asking Copilot to analyze a UI screenshot for accessibility issues or to help understand a visual bug in a layout.
### [Example scenario](https://docs.github.com/en/copilot/using-github-copilot/ai-models/comparing-ai-models-using-different-tasks#example-scenario-2)
You’re designing a shopping cart system and have a UML class diagram that outlines the relationships between `Cart`, `Product`, `User`, and `Order`. Instead of writing out the system from scratch, you want to upload the image of the diagram and ask Copilot to generate the classes.
![Screenshot of a shopping cart UML diagram, showing the class details for Cart, Product, User, and Order.](https://docs.github.com/assets/cb-14364/images/help/copilot/shopping-cart-uml.png)
### [Example prompt](https://docs.github.com/en/copilot/using-github-copilot/ai-models/comparing-ai-models-using-different-tasks#example-prompt-2)
`Use this UML diagram to generate the classes for a shopping cart system.`
### [Example response](https://docs.github.com/en/copilot/using-github-copilot/ai-models/comparing-ai-models-using-different-tasks#example-response-2)
The following response is an example. Copilot Chat responses are non-deterministic, so you may get a different response from the one shown here.
Copilot will generate a class for each of the classes in the diagram, including the relationships between them. Here’s the example code generated for the `Cart` class:
```
from cart_item import CartItem
from order import Order

class Cart:
    def __init__(self, cart_id, user_id):
        self.cart_id = cart_id
        self.user_id = user_id
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items = [i for i in self.items if i != item]

    def calculate_total(self):
        return sum(item.quantity * item.product.price for item in self.items)

    def place_order(self):
        # Implementation for placing an order
        return Order("", None, 0)

```

### [Why Gemini 2.0 Flash is a good fit](https://docs.github.com/en/copilot/using-github-copilot/ai-models/comparing-ai-models-using-different-tasks#why-gemini-20-flash-is-a-good-fit)
  * It can interpret visual assets, such as UML diagrams, wireframes, or flowcharts, to generate code scaffolding or suggest architecture.
  * It can be useful for reviewing screenshots of UI layouts or form designs and generating.


## [Claude 3.5 Sonnet](https://docs.github.com/en/copilot/using-github-copilot/ai-models/comparing-ai-models-using-different-tasks#claude-35-sonnet)
Claude 3.5 Sonnet is a good choice for everyday coding support—including writing documentation, answering language-specific questions, or generating boilerplate code. It offers helpful, direct answers without over-complicating the task. If you're working within cost constraints, Claude 3.5 Sonnet is recommended as it delivers solid performance on many of the same tasks as Claude 3.7 Sonnet, but with significantly lower resource usage.
### [Example scenario](https://docs.github.com/en/copilot/using-github-copilot/ai-models/comparing-ai-models-using-different-tasks#example-scenario-3)
Consider a scenario where you are implementing both unit tests and integration tests for an application. You want to ensure that the tests are comprehensive and cover any edge cases that you may and may not have thought of.
For a complete walkthrough of the scenario, see [Writing tests with GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot/writing-tests-with-github-copilot).
### [Why Claude 3.5 Sonnet is a good fit](https://docs.github.com/en/copilot/using-github-copilot/ai-models/comparing-ai-models-using-different-tasks#why-claude-35-sonnet-is-a-good-fit)
  * It performs well on everyday coding tasks like test generation, boilerplate scaffolding, and validation logic.
  * The task leans into multi-step reasoning, but still stays within the confidence zone of a less advanced model because the logic isn’t too deep.


## [Claude 3.7 Sonnet](https://docs.github.com/en/copilot/using-github-copilot/ai-models/comparing-ai-models-using-different-tasks#claude-37-sonnet)
Claude 3.7 Sonnet excels across the software development lifecycle, from initial design to bug fixes, maintenance to optimizations. It is particularly well-suited for multi-file refactoring or architectural planning, where understanding context across components is important.
### [Example scenario](https://docs.github.com/en/copilot/using-github-copilot/ai-models/comparing-ai-models-using-different-tasks#example-scenario-4)
Consider a scenario where you're modernizing a legacy COBOL application by rewriting it in Node.js. The project involves understanding unfamiliar source code, converting logic across languages, iteratively building the replacement, and verifying correctness through a test suite.
For a complete walkthrough of the scenario, see [Modernizing legacy code with GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot/modernizing-legacy-code-with-github-copilot).
### [Why Claude 3.7 Sonnet is a good fit](https://docs.github.com/en/copilot/using-github-copilot/ai-models/comparing-ai-models-using-different-tasks#why-claude-37-sonnet-is-a-good-fit)
  * Claude 3.7 Sonnet handles complex context well, making it suited for workflows that span multiple files or languages.
  * Its hybrid reasoning architecture allows it to switch between quick answers and deeper, step-by-step problem-solving.


## [Further reading](https://docs.github.com/en/copilot/using-github-copilot/ai-models/comparing-ai-models-using-different-tasks#further-reading)
  * [Choosing the right AI model for your task](https://docs.github.com/en/copilot/using-github-copilot/ai-models/choosing-the-right-ai-model-for-your-task)
  * [Copilot Chat Cookbook](https://docs.github.com/en/copilot/copilot-chat-cookbook)


