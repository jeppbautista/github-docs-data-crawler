  * [Get started](https://docs.github.com/en/get-started "Get started")/
  * [Learn to code](https://docs.github.com/en/get-started/learning-to-code "Learn to code")/
  * [Reuse people's code](https://docs.github.com/en/get-started/learning-to-code/reusing-other-peoples-code-in-your-projects "Reuse people's code")


# Reusing other people's code in your projects
Increase your coding efficiency and knowledge by integrating existing code into your projects.
## In this article
  * [Using other people's code snippets in your project](https://docs.github.com/en/get-started/learning-to-code/reusing-other-peoples-code-in-your-projects#using-other-peoples-code-snippets-in-your-project)
  * [Using code from libraries in your project](https://docs.github.com/en/get-started/learning-to-code/reusing-other-peoples-code-in-your-projects#using-code-from-libraries-in-your-project)
  * [Sharing your work](https://docs.github.com/en/get-started/learning-to-code/reusing-other-peoples-code-in-your-projects#sharing-your-work)
  * [Further reading](https://docs.github.com/en/get-started/learning-to-code/reusing-other-peoples-code-in-your-projects#further-reading)


One of the best things about open source software is the ability to reuse other people's code. Repurposing code helps you save time, discover new functionality, and learn other programming styles. There are two main ways to reuse code:
  * **Copying and pasting a code snippet directly into your project.** If you're new to coding, this is the quickest way to start reusing code.
  * **Importing a library into your project.** While this approach takes some time to learn, it's ultimately easier and more efficient. It's also a foundational skill for software development.


In this article, we'll learn both by working through an example: reusing Python code that calculates the factorial of a number.
## [Using other people's code snippets in your project](https://docs.github.com/en/get-started/learning-to-code/reusing-other-peoples-code-in-your-projects#using-other-peoples-code-snippets-in-your-project)
When you're first learning to code, you might start with reuse by copying and pasting other people's code snippets into your project. It's a great way to save time, but there are a few key steps you should always take before copying another developer's code.
### [1. Finding and understanding a code snippet](https://docs.github.com/en/get-started/learning-to-code/reusing-other-peoples-code-in-your-projects#1-finding-and-understanding-a-code-snippet)
First, you need to find and understand the code snippet you want to reuse. For this example, we'll choose the [`new2code/python-factorial`](https://github.com/new2code/python-factorial) repository.
First, **open** [`factorial_finder.py`](https://github.com/new2code/python-factorial/blob/main/factorial_finder.py), which implements the calculator using a loop:
```
# Initialize the factorial result to 1
factorial = 1

# Initialize the input number to 6
number = 6

# Loop from 1 to number (inclusive) and multiply factorial by each number
for i in range(1, number + 1):
    factorial *= i

print(f"The factorial of {number} is {factorial}")

```

Then, in the menu bar at the top of the file, click 
![Screenshot of the Copilot button, outlined in dark orange, at the top of the file view.](https://docs.github.com/assets/cb-37670/images/help/copilot/factorial-finder-copilot-button.png)
In the chat window, ask Copilot:
Text```
Explain this program.

```
```
Explain this program.

```

### [2. Understanding project licensing](https://docs.github.com/en/get-started/learning-to-code/reusing-other-peoples-code-in-your-projects#2-understanding-project-licensing)
Before you can reuse the code you've found, you need to understand its licensing. Licenses determine how you can use the code in a project, including your ability to copy, modify, and distribute that code.
To identify the license for [new2code/python-factorial](https://github.com/new2code/python-factorial), locate the "About" section on the repository's main page. There, you'll see that the repository is licensed under the MIT license. To read the license, click **MIT license**.
![Screenshot of the main page of the new2code/python-factorial repository. In the right sidebar, "MIT license" is outlined in dark orange.](https://docs.github.com/assets/cb-66620/images/help/repository/license-info-python-factorial.png)
We want to copy the entire `factorial_finder.py` file, so the MIT license indicates that we should include a copy of the license in our own project. At the top of your Python file, paste the license as a comment.
You can learn what's allowed by other common licenses with the [Choose a license](https://choosealicense.com/licenses/) tool.
### [3. Using and modifying code snippets](https://docs.github.com/en/get-started/learning-to-code/reusing-other-peoples-code-in-your-projects#3-using-and-modifying-code-snippets)
Now, you're ready to paste the code snippet into your project. While you'll sometimes to be able to use code snippets as they are, you will often want to **modify** them for your specific use case. Let's practice that now!
Let's say we want to quickly calculate the factorials of 5, 7, 9, and 10. Instead of copying and pasting the entire program for each number, we can move our calculator into a **function** that takes a number as an argument.
Use [Copilot Chat](https://github.com/copilot) to suggest and explain an implementation. Paste our current code into the chat window, followed by this prompt:
Text```
Wrap the Python code above in a function.

```
```
Wrap the Python code above in a function.

```

Copilot will generate code that looks something like this:
Python```
def calculate_factorial(number):
    # Initialize the factorial result to 1
    factorial = 1

    # Loop from 1 to number (inclusive) and multiply factorial by each number
    for i in range(1, number + 1):
        factorial *= i

    return factorial

```
```
def calculate_factorial(number):
    # Initialize the factorial result to 1
    factorial = 1

    # Loop from 1 to number (inclusive) and multiply factorial by each number
    for i in range(1, number + 1):
        factorial *= i

    return factorial

```

With our new function, we can easily find the factorials of our numbers by adding the following code to our project, then running the Python program:
Python```
print(calculate_factorial(5))
print(calculate_factorial(7))
print(calculate_factorial(9))
print(calculate_factorial(10))

```
```
print(calculate_factorial(5))
print(calculate_factorial(7))
print(calculate_factorial(9))
print(calculate_factorial(10))

```

Congratulations! You've successfully found, understood, and modified an example code snippet.
## [Using code from libraries in your project](https://docs.github.com/en/get-started/learning-to-code/reusing-other-peoples-code-in-your-projects#using-code-from-libraries-in-your-project)
Now, let's learn how to use libraries, which is **standard practice** for developers. Libraries are essentially collections of code written by other developers to perform specific tasks. You can import libraries into your project to use the pre-written code, saving you time and effort.
In this section, we'll continue working with the Python factorial calculator example from the previous section. For reference, here's our current code:
Python```
def calculate_factorial(number):
    # Initialize the factorial result to 1
    factorial = 1

    # Loop from 1 to number (inclusive) and multiply factorial by each number
    for i in range(1, number + 1):
        factorial *= i

    return factorial

print(calculate_factorial(5))
print(calculate_factorial(7))
print(calculate_factorial(9))
print(calculate_factorial(10))

```
```
def calculate_factorial(number):
    # Initialize the factorial result to 1
    factorial = 1

    # Loop from 1 to number (inclusive) and multiply factorial by each number
    for i in range(1, number + 1):
        factorial *= i

    return factorial

print(calculate_factorial(5))
print(calculate_factorial(7))
print(calculate_factorial(9))
print(calculate_factorial(10))

```

### [1. Finding a library](https://docs.github.com/en/get-started/learning-to-code/reusing-other-peoples-code-in-your-projects#1-finding-a-library)
Once you know what functionality you want to add to your project, you can search for a library with relevant code. Copilot Chat is an easy way to search for libraries, since you can use natural language to describe exactly what you're looking for.
Finding a factorial is a pretty common function, and there's a good chance someone included that function in an existing library. Open [Copilot Chat](https://github.com/copilot), then ask:
Text```
Is there a Python library with a function for calculating a factorial?

```
```
Is there a Python library with a function for calculating a factorial?

```

Copilot will tell us a factorial function is included in the [`math`](https://docs.python.org/3/library/math.html) module from the standard Python library.
### [2. Prioritizing security in your project](https://docs.github.com/en/get-started/learning-to-code/reusing-other-peoples-code-in-your-projects#2-prioritizing-security-in-your-project)
When you add a library or module to your project, you create what's called a **dependency**. Dependencies are pre-written code bundles that your project relies on to function correctly. If they aren't carefully written or maintained, they can introduce security vulnerabilities to your work.
Thankfully, there are some steps you can take to best protect your project. Let's practice them now.
#### [Using popular libraries](https://docs.github.com/en/get-started/learning-to-code/reusing-other-peoples-code-in-your-projects#using-popular-libraries)
Popular libraries are more likely to be secure, because they are actively maintained and used by many developers. One good marker of popularity is the number of **stars** a repository has. If you can't find the GitHub repository for a dependency, you can ask Copilot for help.
Open [Copilot Chat](https://github.com/copilot), then ask:
Text```
Find the GitHub repository containing the code for the math module in Python.

```
```
Find the GitHub repository containing the code for the math module in Python.

```

Copilot will tell you that the `math` module is defined in [`python/cpython`](https://github.com/python/cpython), which has over 64,000 stars.
#### [Enabling Dependabot alerts for your project](https://docs.github.com/en/get-started/learning-to-code/reusing-other-peoples-code-in-your-projects#enabling-dependabot-alerts-for-your-project)
When enabled, Dependabot alerts are automatically generated when Dependabot detects a security issue in your dependencies, helping you quickly fix vulnerabilities. Dependabot is available for **free** on all open source GitHub repositories.
Turn Dependabot alerts on for your repository now. Click the **Security** tab for your project's GitHub repository. Next to Dependabot alerts, click **Enable Dependabot alerts**. You can access Dependabot alerts from the **Dependabot** tab of the sidebar.
![Screenshot of the "Security" page of a repository. The "Security" tab, "Dependabot" tab, and "Enable Dependabot alerts" button are outlined in orange.](https://docs.github.com/assets/cb-123013/images/help/dependabot/learners-enable-dependabot.png)
### [3. Implementing code from a library](https://docs.github.com/en/get-started/learning-to-code/reusing-other-peoples-code-in-your-projects#3-implementing-code-from-a-library)
Now you're ready to import the library into your project, then use its contents in your code. You can read the documentation for the library to learn how to do it yourself, or you can ask Copilot to suggest and explain an implementation for you.
Open [Copilot Chat](https://github.com/copilot), then ask:
Text```
How do I use the factorial function of the math module in my Python project?

```
```
How do I use the factorial function of the math module in my Python project?

```

Copilot will then suggest a version of the following code:
Python```
import math

# Calculate the factorial of a number
number = 5
result = math.factorial(number)

print(f"The factorial of {number} is {result}")

```
```
import math

# Calculate the factorial of a number
number = 5
result = math.factorial(number)

print(f"The factorial of {number} is {result}")

```

After you replace the existing code in your project with the above implementation, you've successfully used code from a library in your example project!
## [Sharing your work](https://docs.github.com/en/get-started/learning-to-code/reusing-other-peoples-code-in-your-projects#sharing-your-work)
With this tutorial, you've learned how to safely reuse other people's code in your own work. To celebrate, share how you repurposed code and built on the example project in our [community discussion](https://github.com/orgs/community/discussions/153140).
## [Further reading](https://docs.github.com/en/get-started/learning-to-code/reusing-other-peoples-code-in-your-projects#further-reading)
  * [Finding and understanding example code](https://docs.github.com/en/get-started/learning-to-code/finding-and-understanding-example-code)


