  * [Get started](https://docs.github.com/en/get-started "Get started")/
  * [Learn to code](https://docs.github.com/en/get-started/learning-to-code "Learn to code")/
  * [Set up Copilot for learning](https://docs.github.com/en/get-started/learning-to-code/setting-up-copilot-for-learning-to-code "Set up Copilot for learning")


# Setting up Copilot for learning to code
Configure Copilot to help you learn coding concepts and actively build your programming skills.
## In this article
  * [Can Copilot help me learn to code?](https://docs.github.com/en/get-started/learning-to-code/setting-up-copilot-for-learning-to-code#can-copilot-help-me-learn-to-code)
  * [Prerequisites](https://docs.github.com/en/get-started/learning-to-code/setting-up-copilot-for-learning-to-code#prerequisites)
  * [Step 1: Disable code completion](https://docs.github.com/en/get-started/learning-to-code/setting-up-copilot-for-learning-to-code#step-1-disable-code-completion)
  * [Step 2: Add learning instructions](https://docs.github.com/en/get-started/learning-to-code/setting-up-copilot-for-learning-to-code#step-2-add-learning-instructions)
  * [Step 3: Use Copilot Chat to learn](https://docs.github.com/en/get-started/learning-to-code/setting-up-copilot-for-learning-to-code#step-3-use-copilot-chat-to-learn)


## [Can Copilot help me learn to code?](https://docs.github.com/en/get-started/learning-to-code/setting-up-copilot-for-learning-to-code#can-copilot-help-me-learn-to-code)
Yes! Copilot can adapt to meet your changing needs throughout your coding journey. When you're an experienced developer, you'll use Copilot as a coding assistant. While you're learning to code, it's more beneficial as a **supportive companion**.
In this guide, you’ll learn how to set up Copilot to act as a **tutor** that will help you build a deep understanding of programming concepts, rather than relying on it to write your code for you. To optimize your learning, follow these steps for each repository you work on!
## [Prerequisites](https://docs.github.com/en/get-started/learning-to-code/setting-up-copilot-for-learning-to-code#prerequisites)
This guide assumes that you'll use Copilot in VS Code. To get set up, see [Set up Copilot in VS Code](https://code.visualstudio.com/docs/copilot/setup-simplified) in the Visual Studio Code documentation.
## [Step 1: Disable code completion](https://docs.github.com/en/get-started/learning-to-code/setting-up-copilot-for-learning-to-code#step-1-disable-code-completion)
First, let's disable code completion. This will give you the opportunity to deepen your understanding of programming concepts by writing more code yourself.
  1. In VS Code, open your project.
  2. Create a folder in the root directory called `.vscode`.
  3. Inside `.vscode`, create a file called `settings.json`.
  4. Add the following text to the file:
JSON```
{
    "github.copilot.enable": {
        "*": false
    }
}

```
```
{
    "github.copilot.enable": {
        "*": false
    }
}

```

  5. Save the file. Copilot code completion is now disabled for this project in VS Code.


## [Step 2: Add learning instructions](https://docs.github.com/en/get-started/learning-to-code/setting-up-copilot-for-learning-to-code#step-2-add-learning-instructions)
Now, let's provide Copilot Chat with instructions to act like a tutor that supports your learning.
  1. In the root folder of your project, create a file called `copilot-instructions.md`.
  2. Add the following text, or customize it for your personal learning goals:
Markdown```
I am learning to code. You are to act as a tutor; assume I am a beginning coder. Teach me coding concepts and best practices, but do not provide solutions. Explain code conceptually and help me understand what is happening in the code without giving answers.

Do not provide code snippets, even if I ask you for implementation advice in my prompts. Teach me all the basic coding concepts in your answers. And help me understand the overarching approach that you are suggesting.

Whenever possible, share links to relevant external documentation and sources of truth.

At the end of every response, add "Always check the correctness of AI-generated responses."

```
```
I am learning to code. You are to act as a tutor; assume I am a beginning coder. Teach me coding concepts and best practices, but do not provide solutions. Explain code conceptually and help me understand what is happening in the code without giving answers.

Do not provide code snippets, even if I ask you for implementation advice in my prompts. Teach me all the basic coding concepts in your answers. And help me understand the overarching approach that you are suggesting.

Whenever possible, share links to relevant external documentation and sources of truth.

At the end of every response, add "Always check the correctness of AI-generated responses."

```

  3. Save the file. Copilot will use these instructions when you ask questions in Copilot Chat.


## [Step 3: Use Copilot Chat to learn](https://docs.github.com/en/get-started/learning-to-code/setting-up-copilot-for-learning-to-code#step-3-use-copilot-chat-to-learn)
You're ready to start building real coding skills with Copilot's help!
Throughout your work on the project, engage in a long-running conversation with **Copilot Chat**. Treat it as your **personal tutor** , asking questions as they arise and using it to navigate challenges or clarify concepts.
[ Open Copilot Chat in VS Code ](vscode://GitHub.Copilot-Chat)  
  

Copilot Chat is especially helpful for debugging your code. For step-by-step guidance, see [Learning to debug with GitHub Copilot](https://docs.github.com/en/get-started/learning-to-code/learning-to-debug-with-github-copilot).
