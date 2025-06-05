  * [Get started](https://docs.github.com/en/get-started "Get started")/
  * [Learn to code](https://docs.github.com/en/get-started/learning-to-code "Learn to code")/
  * [Debug with Copilot](https://docs.github.com/en/get-started/learning-to-code/learning-to-debug-with-github-copilot "Debug with Copilot")


# Learning to debug with GitHub Copilot
Identify and fix errors in your code by asking GitHub Copilot for help.
## In this article
  * [Prerequisites](https://docs.github.com/en/get-started/learning-to-code/learning-to-debug-with-github-copilot#prerequisites)
  * [Learning to debug through examples](https://docs.github.com/en/get-started/learning-to-code/learning-to-debug-with-github-copilot#learning-to-debug-through-examples)
  * [Debugging your own project](https://docs.github.com/en/get-started/learning-to-code/learning-to-debug-with-github-copilot#debugging-your-own-project)
  * [Next steps](https://docs.github.com/en/get-started/learning-to-code/learning-to-debug-with-github-copilot#next-steps)


Finding and fixing bugs in code can be frustrating, especially when you're a new developer. Thankfully, tools like GitHub Copilot can quickly identify and squash bugs, letting you focus on more creative, interesting work.
## [Prerequisites](https://docs.github.com/en/get-started/learning-to-code/learning-to-debug-with-github-copilot#prerequisites)
The examples in this article assume you're using GitHub Copilot to debug a Python project in Visual Studio Code (VS Code). To follow the examples, you need to:
  * Complete [Set up Visual Studio Code with Copilot](https://code.visualstudio.com/docs/copilot/setup-simplified) in the Visual Studio Code documentation.
  * [Download Python](https://www.python.org/downloads/).
  * Install the [Python extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python).


## [Learning to debug through examples](https://docs.github.com/en/get-started/learning-to-code/learning-to-debug-with-github-copilot#learning-to-debug-through-examples)
There are two main situations you'll encounter when you try to run bugged code:
  * Your code exits before it finishes running, and you receive an error message.
  * Your code runs without errors, but the output is different from what you expected.


Thankfully, Copilot can help debug your code in both situations. To learn how, work through the following examples.
### [Debugging an error with GitHub Copilot](https://docs.github.com/en/get-started/learning-to-code/learning-to-debug-with-github-copilot#debugging-an-error-with-github-copilot)
When you run bugged code, you'll often receive an error message. The message tells you the file and line where the error occurred and briefly describes what went wrong. However, error messages can be confusing. To fully understand and fix the bug, we can ask Copilot for help.
Let's try this out with an example repository: [`new2code/debug-with-copilot`](https://github.com/new2code/debug-with-copilot).
#### [Cloning the example repository](https://docs.github.com/en/get-started/learning-to-code/learning-to-debug-with-github-copilot#cloning-the-example-repository)
First, we need to create a local copy of the repository:
  1. [Start cloning the new2code/debug-with-copilot repository](vscode://vscode.git/clone?url=https://github.com/new2code/debug-with-copilot) in VS Code. 
  2. Choose a location to save the repository on your computer, then click **Select as Repository Destination**.
  3. When prompted, open the repository.


#### [Running the bugged file](https://docs.github.com/en/get-started/learning-to-code/learning-to-debug-with-github-copilot#running-the-bugged-file)
Now, let's run the [`bugged_dice_battle.py`](https://github.com/new2code/debug-with-copilot/blob/main/bugged_dice_battle.py) file. This program simulates a dice battle between two players.
  1. In VS Code, open and review the `bugged_dice_battle.py` file.
  2. Open the Command Palette by pressing `Ctrl`+`Shift`+`P` (Windows/Linux) or `Cmd`+`Shift`+`P` (Mac).
  3. Type `Terminal: Create New Terminal` and press `Enter`.
  4. In the terminal tab, paste the following command.
Windows:
Shell```
py bugged_dice_battle.py

```
```
py bugged_dice_battle.py

```

Mac or Linux:
Shell```
python bugged_dice_battle.py

```
```
python bugged_dice_battle.py

```

  5. Press `Enter` to run the program.


Unfortunately, we get some error text in our terminal ending with the following message:
> TypeError: can only concatenate str (not "int") to str
#### [Debugging the file](https://docs.github.com/en/get-started/learning-to-code/learning-to-debug-with-github-copilot#debugging-the-file)
To understand what this error means, [open Copilot Chat in VS Code](vscode://GitHub.Copilot-Chat), then paste and send the following prompt: 
Text```
Explain in depth why my code produces the following error and how I can fix it:

TypeError: can only concatenate str (not "int") to str

```
```
Explain in depth why my code produces the following error and how I can fix it:

TypeError: can only concatenate str (not "int") to str

```

Copilot will respond that the error occurs because we are trying to concatenate the integers `die_1` and `die_2` to strings, and you can only concatenate strings to strings.
It will also provide an **updated version of our code** that fixes the bug by using the `str()` function to convert the integers to strings before concatenating them. Practice the final step of debugging by applying Copilot's suggestion to the file.
### [Debugging an incorrect output with GitHub Copilot](https://docs.github.com/en/get-started/learning-to-code/learning-to-debug-with-github-copilot#debugging-an-incorrect-output-with-github-copilot)
Sometimes, bugged code runs without throwing any errors, but the output is clearly incorrect. In this case, debugging can be more difficult because VS Code can't tell you the location or description of the bug.
For these "invisible" bugs, Copilot is particularly useful. Let's get some hands-on experience with the other file in our example repository: `bugged_factorial_finder.py`. It's a Python program that's supposed to calculate a factorial.
#### [Running the bugged file](https://docs.github.com/en/get-started/learning-to-code/learning-to-debug-with-github-copilot#running-the-bugged-file-1)
First, let's run the program to see the incorrect output:
  1. Open and review the `bugged_factorial_finder.py` file.
  2. In the terminal you created earlier, paste the following command. Windows:
Shell```
py bugged_factorial_finder.py

```
```
py bugged_factorial_finder.py

```

Mac or Linux:
Shell```
python bugged_factorial_finder.py

```
```
python bugged_factorial_finder.py

```

  3. Press `Enter` to run the program.


Unfortunately, the code isn't working as expected. We want it to return `720`, the correct value of 6 factorial, but the output is much higher than that.
#### [Debugging the file](https://docs.github.com/en/get-started/learning-to-code/learning-to-debug-with-github-copilot#debugging-the-file-1)
To understand what went wrong, [open Copilot Chat](vscode://GitHub.Copilot-Chat) and send the following prompt: 
Text```
Why is the output of this code so much higher than expected? Please explain in depth and suggest a solution.

```
```
Why is the output of this code so much higher than expected? Please explain in depth and suggest a solution.

```

Copilot will point out that, because we're using the `*=` operator, we're actually multiplying `factorial` by both `i` **and** `factorial`. In other words, we're multiplying by an extra `factorial` for each iteration of the loop.
To fix this error, Copilot will suggest code that removes the extra `factorial` from the equation, or that changes the `*=` operator to `=`. Make that change now!
## [Debugging your own project](https://docs.github.com/en/get-started/learning-to-code/learning-to-debug-with-github-copilot#debugging-your-own-project)
Now that you've practiced debugging some simple programs with Copilot, you can use the same methodologies to find and fix bugs hiding in your own work.
For example, to debug an error message generated by your code, send Copilot the following prompt:
Text```
Explain in depth why my code produces the following error and how I can fix it:

YOUR-ERROR-MESSAGE

```
```
Explain in depth why my code produces the following error and how I can fix it:

YOUR-ERROR-MESSAGE

```

Otherwise, if you're debugging an incorrect output, ask Copilot why the output is incorrect and how you can fix it. For the best results, provide as much context as possible on how the output differs from your expectations.
With these tactics, you're well equipped to start squashing bugs in your project!
## [Next steps](https://docs.github.com/en/get-started/learning-to-code/learning-to-debug-with-github-copilot#next-steps)
As you continue coding, you'll likely encounter specific problem scenarios and errors that are difficult to debug. For a list of potential issues and example Copilot Chat prompts to fix them, see [Debugging errors](https://docs.github.com/en/copilot/copilot-chat-cookbook/debugging-errors).
