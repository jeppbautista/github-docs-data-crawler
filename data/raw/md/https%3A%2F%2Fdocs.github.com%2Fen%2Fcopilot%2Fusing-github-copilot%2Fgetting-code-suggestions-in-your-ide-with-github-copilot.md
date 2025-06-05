  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Use GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot "Use GitHub Copilot")/
  * [Get code suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot "Get code suggestions")


# Getting code suggestions in your IDE with GitHub Copilot
Use GitHub Copilot to get code suggestions in your editor.
## Tool navigation
  * [Azure Data Studio](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot?tool=azure_data_studio)
  * [Eclipse](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot?tool=eclipse)
  * [JetBrains IDEs](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot?tool=jetbrains)
  * [Visual Studio Code](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot?tool=vscode)
  * More Tool items
    * [Vim/Neovim](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot?tool=vimneovim)
    * [Visual Studio](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot?tool=visualstudio)
    * [Xcode](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot?tool=xcode)


## In this article
  * [About GitHub Copilot and JetBrains IDEs](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#about-github-copilot-and-jetbrains-ides)
  * [Prerequisites](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#prerequisites)
  * [Getting code suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#getting-code-suggestions)
  * [Showing alternative suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#showing-alternative-suggestions)
  * [Showing multiple suggestions in a new tab](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#showing-multiple-suggestions-in-a-new-tab)
  * [Accepting partial suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#accepting-partial-suggestions)
  * [About GitHub Copilot and Visual Studio](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#about-github-copilot-and-visual-studio)
  * [Prerequisites](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#prerequisites-1)
  * [Getting code suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#getting-code-suggestions-1)
  * [Showing alternative suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#showing-alternative-suggestions-1)
  * [Getting comment suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#getting-comment-suggestions)
  * [About next edit suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#about-next-edit-suggestions)
  * [About GitHub Copilot and Visual Studio Code](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#about-github-copilot-and-visual-studio-code)
  * [Prerequisites](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#prerequisites-2)
  * [Getting code suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#getting-code-suggestions-2)
  * [Showing alternative suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#showing-alternative-suggestions-2)
  * [Showing multiple suggestions in a new tab](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#showing-multiple-suggestions-in-a-new-tab-1)
  * [Accepting partial suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#accepting-partial-suggestions-1)
  * [About next edit suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#about-next-edit-suggestions-1)
  * [Changing the AI model](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#changing-the-ai-model)
  * [About GitHub Copilot and Vim/Neovim](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#about-github-copilot-and-vimneovim)
  * [Prerequisites](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#prerequisites-3)
  * [Learning to use GitHub Copilot in Vim/Neovim](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#learning-to-use-github-copilot-in-vimneovim)
  * [About GitHub Copilot and Azure Data Studio](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#about-github-copilot-and-azure-data-studio)
  * [Prerequisites](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#prerequisites-4)
  * [Getting code suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#getting-code-suggestions-3)
  * [Showing alternative suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#showing-alternative-suggestions-3)
  * [Accepting partial suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#accepting-partial-suggestions-2)
  * [About GitHub Copilot in Xcode](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#about-github-copilot-in-xcode)
  * [Prerequisites](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#prerequisites-5)
  * [Getting code suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#getting-code-suggestions-4)
  * [About GitHub Copilot and Eclipse](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#about-github-copilot-and-eclipse)
  * [Prerequisites](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#prerequisites-6)
  * [Getting code suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#getting-code-suggestions-5)
  * [Manually triggering code completion](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#manually-triggering-code-completion)
  * [Accepting partial suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#accepting-partial-suggestions-3)
  * [Next steps](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#next-steps)


[ Get started for free ](https://github.com/copilot?ref_cta=Copilot+free&ref_loc=getting+started+with+github+copilot&ref_page=docs)
[ Open in Visual Studio Code ](vscode://GitHub.Copilot-Chat)
## [About GitHub Copilot and JetBrains IDEs](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#about-github-copilot-and-jetbrains-ides)
This guide demonstrates how to get coding suggestions from GitHub Copilot in a JetBrains IDE. To see instructions for other popular coding environments, use the tool switcher at the top of the page.
The examples in this guide use Java, however other languages will work similarly. GitHub Copilot provides suggestions for numerous languages and a wide variety of frameworks, but works especially well for Python, JavaScript, TypeScript, Ruby, Go, C# and C++. GitHub Copilot can also assist in query generation for databases, generating suggestions for APIs and frameworks, and can help with infrastructure as code development.
## [Prerequisites](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#prerequisites)
  * **Access to Copilot**. To use GitHub Copilot in JetBrains, you need either limited access through Copilot Free or a paid Copilot plan for full access. For information about how to get access to Copilot, see [What is GitHub Copilot?](https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot#getting-access-to-copilot).
  * **Compatible JetBrains IDE**. To use GitHub Copilot in JetBrains, you must have a compatible JetBrains IDE installed. GitHub Copilot is compatible with the following IDEs:
    * IntelliJ IDEA (Ultimate, Community, Educational)
    * Android Studio
    * AppCode
    * CLion
    * Code With Me Guest
    * DataGrip
    * DataSpell
    * GoLand
    * JetBrains Client
    * MPS
    * PhpStorm
    * PyCharm (Professional, Community, Educational)
    * Rider
    * RubyMine
    * RustRover
    * WebStorm
    * Writerside
See the [JetBrains IDEs](https://www.jetbrains.com/products/) tool finder to download.
  * **GitHub Copilot plugin**. See the [GitHub Copilot plugin](https://plugins.jetbrains.com/plugin/17718-github-copilot) in the JetBrains Marketplace. For installation instructions, see [Installing the GitHub Copilot extension in your environment](https://docs.github.com/en/copilot/configuring-github-copilot/installing-the-github-copilot-extension-in-your-environment).
  * **Log in to GitHub in your JetBrains IDE**. For authentication instructions, see [Installing the GitHub Copilot extension in your environment](https://docs.github.com/en/copilot/configuring-github-copilot/installing-the-github-copilot-extension-in-your-environment?tool=jetbrains#installing-the-github-copilot-plugin-in-your-jetbrains-ide).


## [Getting code suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#getting-code-suggestions)
GitHub Copilot offers coding suggestions as you type. For example, in a Java file, create a class by typing `class Test`.
GitHub Copilot will automatically suggest a class body in grayed text. To accept the suggestion, press `Tab`.
You can also describe something you want to do using natural language within a comment, and Copilot will suggest the code to accomplish your goal. For example, type this comment in a Java file:
Java```
// find all images without alternate text
// and give them a red border
void process () {

```
```
// find all images without alternate text
// and give them a red border
void process () {

```

GitHub Copilot will automatically suggest code. To accept the suggestion, press `Tab`.
GitHub Copilot will attempt to match the context and style of your code. You can always edit the suggested code.
If you receive limited or no suggestions from Copilot, you may have duplication detection enabled. For more information about duplication detection, see [Managing Copilot policies as an individual subscriber](https://docs.github.com/en/copilot/configuring-github-copilot/configuring-your-personal-github-copilot-settings-on-githubcom#enabling-or-disabling-suggestions-matching-public-code).
## [Showing alternative suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#showing-alternative-suggestions)
For any given input, GitHub Copilot may offer multiple suggestions. You can select which suggestion to use, or reject all suggestions.
For example, type the following line in a Java file, and press `Enter`:
Java```
private int calculateDaysBetweenDates(Date date1,

```
```
private int calculateDaysBetweenDates(Date date1,

```

GitHub Copilot will show you a suggestion.
Now hover over the suggestion to show the GitHub Copilot control for choosing suggestions. To display next or previous suggestions, click the forward or back arrow button in the control.
You can also use keyboard shortcuts to show alternative suggestions:
OS | See next suggestion | See previous suggestion  
---|---|---  
macOS |  `Option`+`]` |  `Option`+`[`  
Windows or Linux |  `Alt`+`]` |  `Alt`+`[`  
To accept a suggestion, click "Accept" in the Copilot command palette, or press `Tab`. To reject all suggestions, press `Esc`.
## [Showing multiple suggestions in a new tab](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#showing-multiple-suggestions-in-a-new-tab)
If you don't want to use any of the initial suggestions GitHub Copilot offers, you can show multiple suggestions in a new tab.
For example, type the following line in a Java file:
Java```
private int calculateDaysBetweenDates(Date date1,

```
```
private int calculateDaysBetweenDates(Date date1,

```

GitHub Copilot will show you a suggestion.
To open a new tab with multiple additional suggestions, use the following keyboard shortcut, then click **Open GitHub Copilot** :
OS | Open multiple suggestions  
---|---  
macOS |  `Command`+`Shift`+`A`  
Windows or Linux |  `Ctrl`+`Enter`  
To accept a suggestion, below the suggestion, click **Accept suggestion NUMBER**. To reject all suggestions, close the tab.
## [Accepting partial suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#accepting-partial-suggestions)
If you don't want to accept an entire suggestion from GitHub Copilot, you can accept the next word or the next line of a suggestion.
For example, type the following line in a Java file:
Java```
private int calculateDaysBetweenDates(Date date1,

```
```
private int calculateDaysBetweenDates(Date date1,

```

GitHub Copilot will show a suggestion in grayed text. The exact suggestion may vary.
Now hover over the suggestion to show the GitHub Copilot control for choosing suggestions. To accept only the next word of the suggestion, click **Accept Word** in the control.
Alternatively, you can use a keyboard shortcut to accept the next word of a suggestion:
OS | Accept Next Word | Accept Next Line  
---|---|---  
macOS |  `Command`+`→` |  `Command`+`Control`+`→`  
Windows or Linux |  `Control`+`→` |  `Control`+`Alt`+`→`  
If you want to accept the next line of a suggestion, you will need to set a custom keyboard shortcut for the command `editor.action.inlineSuggest.acceptNextLine`. For more information on setting custom keyboard shortcuts, see [Configuring GitHub Copilot in your environment](https://docs.github.com/en/copilot/configuring-github-copilot/configuring-github-copilot-in-your-environment).
## [About GitHub Copilot and Visual Studio](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#about-github-copilot-and-visual-studio)
This guide demonstrates how to get coding suggestions from GitHub Copilot in Visual Studio for Windows. To see instructions for other popular coding environments, use the tool switcher at the top of the page.
The examples in this guide use C#, however other languages will work similarly. GitHub Copilot provides suggestions for numerous languages and a wide variety of frameworks, but works especially well for Python, JavaScript, TypeScript, Ruby, Go, C# and C++. GitHub Copilot can also assist in query generation for databases, generating suggestions for APIs and frameworks, and can help with infrastructure as code development.
## [Prerequisites](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#prerequisites-1)
  * **Access to Copilot**. To use GitHub Copilot in GitHub Copilot in Visual Studio, you need either limited access through Copilot Free or a paid Copilot plan for full access. For information about how to get access to Copilot, see [What is GitHub Copilot?](https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot#getting-access-to-copilot).
  * **Compatible version of Visual Studio**. To use GitHub Copilot in Visual Studio, you must have version 2022 17.8 or later of Visual Studio for Windows installed. For more information, see [Install Visual Studio](https://learn.microsoft.com/en-us/visualstudio/install/install-visual-studio) in the Microsoft documentation.
  * **GitHub Copilot extension for Visual Studio**. For instructions on how to install the Copilot extension, see [Install GitHub Copilot in Visual Studio](https://learn.microsoft.com/visualstudio/ide/visual-studio-github-copilot-install-and-states) in the Microsoft documentation.
  * **Add your GitHub account to Visual Studio**. See [Add your GitHub accounts to your Visual Studio keychain](https://learn.microsoft.com/en-us/visualstudio/ide/work-with-github-accounts) in the Microsoft documentation.


## [Getting code suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#getting-code-suggestions-1)
GitHub Copilot offers coding suggestions as you type. For example, type this function signature in a C# file:
C#```
int CalculateDaysBetweenDates(

```
```
int CalculateDaysBetweenDates(
```

GitHub Copilot will automatically suggest an entire function body in grayed text. To accept the suggestion, press `Tab`.
You can also describe something you want to do using natural language within a comment, and Copilot will suggest the code to accomplish your goal. For example, type this comment in the C# file:
C#```
using System.Xml.Linq;

var doc = XDocument.Load("index.xhml");

// find all images

```
```
using System.Xml.Linq;

var doc = XDocument.Load("index.xhml");

// find all images

```

GitHub Copilot will suggest an implementation of the function. To accept the suggestion, press `Tab`.
If you receive limited or no suggestions from Copilot, you may have duplication detection enabled. For more information about duplication detection, see [Managing Copilot policies as an individual subscriber](https://docs.github.com/en/copilot/configuring-github-copilot/configuring-your-personal-github-copilot-settings-on-githubcom#enabling-or-disabling-suggestions-matching-public-code).
## [Showing alternative suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#showing-alternative-suggestions-1)
For any given input, GitHub Copilot may offer multiple suggestions. You can select which suggestion to use, or reject all suggestions.
For example, type this function signature in a C# file:
C#```
int CalculateDaysBetweenDates(

```
```
int CalculateDaysBetweenDates(
```

GitHub Copilot will show you a suggestion.
Now hover over the suggestion to show the GitHub Copilot control for choosing suggestions. To display next or previous suggestions, click the forward or back arrow button in the control.
Alternatively, you can show alternate suggestions by pressing `Alt`+`.` (or `Alt`+`,`) on your keyboard.
To accept a suggestion, click "Accept" in the Copilot command palette, or press `Tab`. To reject all suggestions, press `Esc`.
## [Getting comment suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#getting-comment-suggestions)
  * Comment suggestions are currently in public preview and are subject to change.
  * Comment suggestions are available in Visual Studio 17.14 Preview 2 and later.


GitHub Copilot can suggest comments for your code, by analyzing the code you write and generating comments that describe what the code does. For Copilot Free users, comment suggestions count towards your monthly Copilot Chat usage, not your code suggestions usage.
Comment suggestions are available in the following languages:
  * C#
  * C++


### [Enabling comment suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#enabling-comment-suggestions)
To enable comment suggestions, you need to configure the comment style in Visual Studio.
#### [For C++](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#for-c)
  1. In Visual Studio, in the **Tools** menu, click **Options**.
  2. In the left-side panel, click **Text Editor**.
  3. Click **C++** , then **Code Style** , then **General**.
  4. Under "Comments", select **Xml Doc Comments** from the dropdown.
  5. Select **Insert existing comment style at the start of new lines when writing comments** and **Continue single line comments.**


#### [For C#](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#for-c-1)
  1. In Visual Studio, in the **Tools** menu, click **Options**.
  2. In the left-side panel, click **Text Editor**.
  3. Click **C#** , then **Advanced**.
  4. Under "Comments", select **Generate XML documentation comments for ///** , **Insert // at the start of new lines when writing // comments** , and **Insert * at the start of new lines when writing /* */ comments.**


### [Using comment suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#using-comment-suggestions)
To initiate comment suggestions, type the standard comment initiator for the language you are writing in (for example, `///`), before the code you want to comment, and wait for the suggestion to appear.
To accept the suggestion, press `Tab`. To modify the suggestion, press `Alt`+`/`. To reject the suggestion, press `Esc`.
## [About next edit suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#about-next-edit-suggestions)
Inline suggestions autocomplete code, but many development tasks involve editing existing code. Next edit suggestions assists with edits both at the cursor and in other relevant parts of the code, helping maintain consistency and streamline changes.
Next edit suggestions predicts where and what edits may be needed based on ongoing changes. Suggestions may span a single symbol, an entire line, or multiple lines, depending on the scope of the potential change.
To enable next edit suggestions, see [Configuring GitHub Copilot in your environment](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#enabling-next-edit-suggestions).
### [Navigating and accepting suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#navigating-and-accepting-suggestions)
You can navigate suggested code changes using `Tab`, making it easier to find the next relevant edit without manually searching through files or references. Press `Tab` again to accept a suggestion.
An arrow in the gutter indicates an available edit suggestion. Click the arrow to access the edit suggestion menu, which provides keyboard shortcuts. If an edit suggestion is outside the current editor view, the arrow will point up or down to indicate where the next suggestion is.
## [About GitHub Copilot and Visual Studio Code](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#about-github-copilot-and-visual-studio-code)
This guide demonstrates how to get coding suggestions from GitHub Copilot in Visual Studio Code. To see instructions for other popular coding environments, use the tool switcher at the top of the page.
Copilot in VS Code provides two kinds of suggestions:
  * **Code completion**. Copilot offers coding suggestions as you type. You can also describe something you want to do using natural language within a comment, and Copilot will suggest the code to accomplish your goal.
  * **Next edit suggestions (public preview)**. Based on the edits you are making, Copilot will predict the location of the next edit you are likely to make and suggest a completion for it.


The examples in this guide use JavaScript, however other languages will work similarly. GitHub Copilot provides suggestions for numerous languages and a wide variety of frameworks, but works especially well for Python, JavaScript, TypeScript, Ruby, Go, C# and C++. GitHub Copilot can also assist in query generation for databases, generating suggestions for APIs and frameworks, and can help with infrastructure as code development.
## [Prerequisites](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#prerequisites-2)
  * **Access to Copilot**. To use GitHub Copilot in Visual Studio Code, you need either limited access through Copilot Free or a paid Copilot plan for full access. For information about how to get access to Copilot, see [What is GitHub Copilot?](https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot#getting-access-to-copilot).
  * **Sign in to GitHub in Visual Studio Code**. See [Set up GitHub Copilot in Visual Studio Code](https://code.visualstudio.com/docs/copilot/setup) in the VS Code documentation..
  * **Visual Studio Code**. To use GitHub Copilot in Visual Studio Code, you must have Visual Studio Code installed. For more information, see the [Visual Studio Code download page](https://code.visualstudio.com/Download).
  * **Copilot in Visual Studio Code**. When you set up GitHub Copilot in Visual Studio Code for the first time, the required extensions are installed automatically. You don't need to download or install them manually. For detailed instructions, see [Set up GitHub Copilot in Visual Studio Code](https://code.visualstudio.com/docs/copilot/setup) in the Visual Studio Code documentation.


## [Getting code suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#getting-code-suggestions-2)
GitHub Copilot offers coding suggestions as you type. For example, type this function header in a JavaScript file:
JavaScript```
function calculateDaysBetweenDates(begin, end) {

```
```
function calculateDaysBetweenDates(begin, end) {

```

GitHub Copilot will automatically suggest the rest of the function. To accept the suggestion, press `Tab`.
You can also describe something you want to do using natural language within a comment, and Copilot will suggest the code to accomplish your goal. For example, type this comment in a JavaScript file:
JavaScript```
// write a function to
// find all images without alternate text
// and give them a red border

```
```
// write a function to
// find all images without alternate text
// and give them a red border

```

GitHub Copilot will automatically suggest code. To accept the suggestion, press `Tab`.
If you receive limited or no suggestions from Copilot, you may have duplication detection enabled. For more information about duplication detection, see [Managing Copilot policies as an individual subscriber](https://docs.github.com/en/copilot/configuring-github-copilot/configuring-your-personal-github-copilot-settings-on-githubcom#enabling-or-disabling-suggestions-matching-public-code).
## [Showing alternative suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#showing-alternative-suggestions-2)
For any given input, GitHub Copilot may offer multiple suggestions. You can select which suggestion to use, or reject all suggestions.
For example, type this function header in a JavaScript file, and press `Enter`:
JavaScript```
function calculateDaysBetweenDates(begin, end) {

```
```
function calculateDaysBetweenDates(begin, end) {

```

GitHub Copilot will show you a suggestion.
Now hover over the suggestion to show the GitHub Copilot control for choosing suggestions. To display next or previous suggestions, click the forward or back arrow button in the control.
You can also use keyboard shortcuts to show alternative suggestions:
OS | See next suggestion | See previous suggestion  
---|---|---  
macOS |  `Option (⌥) or Alt`+`]` |  `Option (⌥) or Alt`+`[`  
Windows or Linux |  `Alt`+`]` |  `Alt`+`[`  
To accept a suggestion, click "Accept" in the Copilot command palette, or press `Tab`. To reject all suggestions, press `Esc`.
## [Showing multiple suggestions in a new tab](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#showing-multiple-suggestions-in-a-new-tab-1)
If you don't want to use any of the initial suggestions GitHub Copilot offers, you can show multiple suggestions in a new tab.
For example, type this function header in a JavaScript file, and press `Enter`:
JavaScript```
function calculateDaysBetweenDates(begin, end) {

```
```
function calculateDaysBetweenDates(begin, end) {

```

GitHub Copilot will show you a suggestion. Now press `Ctrl`+`Enter` to open a new tab with multiple additional options.
To accept a suggestion, below the suggestion, click **Accept suggestion NUMBER**. To reject all suggestions, close the tab.
## [Accepting partial suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#accepting-partial-suggestions-1)
If you don't want to accept an entire suggestion from GitHub Copilot, you can accept the next word or the next line of a suggestion.
For example, type this function header in a JavaScript file, and press `Enter`:
JavaScript```
function calculateDaysBetweenDates(begin, end) {

```
```
function calculateDaysBetweenDates(begin, end) {

```

GitHub Copilot will automatically suggest an entire function body in grayed text. The exact suggestion may vary.
Now hover over the suggestion to show the GitHub Copilot control for choosing suggestions. To accept only the next word of the suggestion, click **Accept Word** in the control.
Alternatively, you can use a keyboard shortcut to accept the next word of a suggestion:
OS | Accept Next Word  
---|---  
macOS |  `Command`+`→`  
Windows or Linux |  `Control`+`→`  
If you want to accept the next line of a suggestion, you will need to set a custom keyboard shortcut for the command `editor.action.inlineSuggest.acceptNextLine`. For more information on setting custom keyboard shortcuts, see [Configuring GitHub Copilot in your environment](https://docs.github.com/en/copilot/configuring-github-copilot/configuring-github-copilot-in-your-environment).
## [About next edit suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#about-next-edit-suggestions-1)
Inline suggestions autocomplete code, but many development tasks involve editing existing code. Next edit suggestions assists with edits both at the cursor and in other relevant parts of the code, helping maintain consistency and streamline changes.
Next edit suggestions predicts where and what edits may be needed based on ongoing changes. Suggestions may span a single symbol, an entire line, or multiple lines, depending on the scope of the potential change.
To enable next edit suggestions, see [Configuring GitHub Copilot in your environment](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment#enabling-next-edit-suggestions).
### [Navigating and accepting suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#navigating-and-accepting-suggestions-1)
You can navigate suggested code changes using `Tab`, making it easier to find the next relevant edit without manually searching through files or references. Press `Tab` again to accept a suggestion.
An arrow in the gutter indicates an available edit suggestion. Hover over the arrow to access the edit suggestion menu, which provides keyboard shortcuts and settings options. If an edit suggestion is outside the current editor view, the arrow will point up or down to indicate where the next suggestion is.
![Screenshot of the gutter menu in Visual Studio Code. The arrow is outlined in dark orange.](https://docs.github.com/assets/cb-39261/images/help/copilot/vsc-advanced-code-completion-menu.png)
For more details and examples, see [Code completions with GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/ai-powered-suggestions) in the Visual Studio Code documentation.
## [Changing the AI model](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#changing-the-ai-model)
You can change the large language model that's used to generate code completion suggestions. For more information, see [Changing the AI model for Copilot code completion](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-code-completion).
## [About GitHub Copilot and Vim/Neovim](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#about-github-copilot-and-vimneovim)
This guide demonstrates how to get coding suggestions from GitHub Copilot in Vim/Neovim. To see instructions for other popular coding environments, use the tool switcher at the top of the page.
## [Prerequisites](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#prerequisites-3)
  * **Access to Copilot**. To use GitHub Copilot in Vim/Neovim, you need either limited access through Copilot Free or a paid Copilot plan for full access. For information about how to get access to Copilot, see [What is GitHub Copilot?](https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot#getting-access-to-copilot).
  * **Compatible version of Vim/Neovim**. To use GitHub Copilot in Vim/Neovim you must have Vim version 9.0.0185 / Neovim version 0.6 or above and Node.js version 18 or above installed. For more information, see the [Vim](https://vimhelp.org/) / [Neovim documentation](https://neovim.io/doc/) and the [Node.js website](https://nodejs.org/en/).
  * **GitHub Copilot extension for Vim/Neovim**. To use GitHub Copilot in Vim/Neovim, you must install the GitHub Copilot plugin. For more information, see [Installing the GitHub Copilot extension in your environment](https://docs.github.com/en/copilot/configuring-github-copilot/installing-the-github-copilot-extension-in-your-environment).


## [Learning to use GitHub Copilot in Vim/Neovim](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#learning-to-use-github-copilot-in-vimneovim)
GitHub Copilot provides suggestions inline as you type in Vim/Neovim. To accept a suggestion, press the `tab` key.
For more information and guidance on using GitHub Copilot in Vim/Neovim run the following command to view the plugin documentation:
Shell```
:help copilot

```
```
:help copilot

```

## [About GitHub Copilot and Azure Data Studio](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#about-github-copilot-and-azure-data-studio)
This guide demonstrates how to get coding suggestions from GitHub Copilot in Azure Data Studio. To see instructions for other popular coding environments, use the tool switcher at the top of the page.
## [Prerequisites](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#prerequisites-4)
  * **Access to Copilot**. To use GitHub Copilot in Azure Data Studio, you need either limited access through Copilot Free or a paid Copilot plan for full access. For information about how to get access to Copilot, see [What is GitHub Copilot?](https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot#getting-access-to-copilot).
  * **Compatible version of Azure Data Studio**. To use GitHub Copilot in Azure Data Studio, you must have Azure Data Studio version 1.44.0 or later installed. For more information, see the [Azure Data Studio download page](https://docs.microsoft.com/sql/azure-data-studio/download-azure-data-studio) in the Azure Data Studio documentation.
  * **GitHub Copilot extension for Azure Data Studio**. To use GitHub Copilot in Azure Data Studio, you must install the GitHub Copilot extension. For more information, see [Installing the GitHub Copilot extension in your environment](https://docs.github.com/en/copilot/configuring-github-copilot/installing-the-github-copilot-extension-in-your-environment).


## [Getting code suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#getting-code-suggestions-3)
GitHub Copilot can provide you with inline suggestions as you create SQL databases in Azure Data Studio. For example, if you're writing a query that joins two tables, Copilot may suggest the join condition from columns in the open editor, other files in the workspace, and common syntax patterns.
In a SQL file, type the following query:
SQL```
SELECT [UserId], [Red], [Orange], [Yellow], [Green], [Blue], [Purple], [Rainbow]
FROM [Tag].[Scoreboard]
INNER JOIN

```
```
SELECT [UserId], [Red], [Orange], [Yellow], [Green], [Blue], [Purple], [Rainbow]
FROM [Tag].[Scoreboard]
INNER JOIN

```

GitHub Copilot will automatically suggest a join condition in grayed text. The exact suggestion may vary. To accept the suggestion, press `Tab`.
You can also describe something you want to do using natural language within a comment, and Copilot will suggest the code to accomplish your goal. For example, type this comment in a SQL file:
SQL```
SELECT TokenColor, COUNT(UserID) AS UserCount
FROM Tag.Users
GROUP BY TokenColor
-- pivot that query on tokencolor for Purple, Blue, Green, Yellow, Orange, Red
-- and rename the columns to match the colors
SELECT [Purple], [Blue], [Green], [Yellow], [Orange], [Red]

```
```
SELECT TokenColor, COUNT(UserID) AS UserCount
FROM Tag.Users
GROUP BY TokenColor
-- pivot that query on tokencolor for Purple, Blue, Green, Yellow, Orange, Red
-- and rename the columns to match the colors
SELECT [Purple], [Blue], [Green], [Yellow], [Orange], [Red]

```

GitHub Copilot will automatically suggest code. To accept the suggestion, press `Tab`.
If you receive limited or no suggestions from Copilot, you may have duplication detection enabled. For more information on duplication detection, see [Managing Copilot policies as an individual subscriber](https://docs.github.com/en/copilot/configuring-github-copilot/configuring-your-personal-github-copilot-settings-on-githubcom#enabling-or-disabling-suggestions-matching-public-code).
## [Showing alternative suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#showing-alternative-suggestions-3)
For some suggestions, GitHub Copilot may provide multiple alternatives. You can select which suggestion you want to use, or reject all suggestions.
For example, type this query in a SQL file:
SQL```
SELECT [UserId], [Red], [Orange], [Yellow], [Green], [Blue], [Purple], [Rainbow]
FROM [Tag].[Scoreboard]
INNER JOIN

```
```
SELECT [UserId], [Red], [Orange], [Yellow], [Green], [Blue], [Purple], [Rainbow]
FROM [Tag].[Scoreboard]
INNER JOIN

```

GitHub Copilot will show you a suggestion.
Now hover over the suggestion to show the GitHub Copilot control for choosing suggestions. To display next or previous suggestions, click the forward or back arrow button in the control.
You can also use keyboard shortcuts to show alternative suggestions:
OS | See next suggestion | See previous suggestion  
---|---|---  
macOS |  `Option`+`[` |  `Option`+`]`  
Windows or Linux |  `Alt`+`[` |  `Alt`+`]`  
To accept a suggestion, click "Accept" in the Copilot control, or press `Tab`. To reject all suggestions, press `Esc`.
## [Accepting partial suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#accepting-partial-suggestions-2)
If you don't want to accept an entire suggestion from GitHub Copilot, you can accept the next word or the next line of a suggestion.
For example, type this query in a SQL file:
SQL```
SELECT [UserId], [Red], [Orange], [Yellow], [Green], [Blue], [Purple], [Rainbow]
FROM [Tag].[Scoreboard]
INNER JOIN

```
```
SELECT [UserId], [Red], [Orange], [Yellow], [Green], [Blue], [Purple], [Rainbow]
FROM [Tag].[Scoreboard]
INNER JOIN

```

GitHub Copilot will show you a suggestion in grayed text. The exact suggestion may vary.
Now hover over the suggestion to show the GitHub Copilot control for choosing suggestions. To accept only the next word of the suggestion, click **Accept Word** in the control.
Alternatively, you can use a keyboard shortcut to accept the next word of a suggestion:
OS | Accept Next Word  
---|---  
macOS |  `Command`+`→`  
Windows or Linux |  `Control`+`→`  
If you want to accept the next line of the suggestion, you will need to set a custom keyboard shortcut for the command `editor.action.inlineSuggest.acceptNextLine`. For more information on setting custom keyboard shortcuts, see [Keyboard shortcuts in Azure Data Studio](https://learn.microsoft.com/en-us/azure-data-studio/keyboard-shortcuts) in the Microsoft documentation.
## [About GitHub Copilot in Xcode](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#about-github-copilot-in-xcode)
This guide demonstrates how to get coding suggestions from GitHub Copilot in Xcode. To see instructions for other popular coding environments, use the tool switcher at the top of the page.
## [Prerequisites](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#prerequisites-5)
  * **Access to Copilot**. To use GitHub Copilot in Xcode, you need either limited access through Copilot Free or a paid Copilot plan for full access. For information about how to get access to Copilot, see [What is GitHub Copilot?](https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot#getting-access-to-copilot).
  * **GitHub Copilot extension for Xcode**. To use GitHub Copilot for Xcode, you must install the GitHub Copilot for Xcode extension. See [Installing the GitHub Copilot extension in your environment](https://docs.github.com/en/copilot/configuring-github-copilot/installing-the-github-copilot-extension-in-your-environment).


## [Getting code suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#getting-code-suggestions-4)
GitHub Copilot offers coding suggestions as you type. For example, type this function signature in a Swift file:
Swift```
func calculateDaysBetweenDates(

```
```
func calculateDaysBetweenDates(

```

GitHub Copilot will automatically suggest an entire function body in grayed text. To accept the first line of a suggestion, press `Tab`. To view the full suggestion, hold `Option`, and to accept the full suggestion, press `Option`+`Tab`.
### [Improving code suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#improving-code-suggestions)
If you encounter issues with code suggestions, such as conflicting or missing suggestions, you can try the following:
  * **Disable Xcode's native predictive text completion:** To avoid receiving two sets of code suggestions, you can disable Xcode's native predictive text completion. You can find this setting in the Xcode settings in the "Editing" tab under "Text Editing".
  * **Check for duplication detection in Copilot:** If you receive limited or no suggestions from Copilot, you may have duplication detection enabled. For more information on duplication detection, see [Managing Copilot policies as an individual subscriber](https://docs.github.com/en/copilot/configuring-github-copilot/configuring-your-personal-github-copilot-settings-on-githubcom#enabling-or-disabling-suggestions-matching-public-code).
  * **Check for updates and restart Xcode:** Ensure you have the latest version of Copilot for Xcode in the extension application and restart Xcode.


You can also open an issue in the [Copilot for Xcode repository](https://github.com/github/CopilotForXcode).
## [About GitHub Copilot and Eclipse](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#about-github-copilot-and-eclipse)
This guide demonstrates how to get coding suggestions from GitHub Copilot in Eclipse. To see instructions for other popular coding environments, use the tool switcher at the top of the page.
## [Prerequisites](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#prerequisites-6)
  * **Access to Copilot**. To use GitHub Copilot in Eclipse, you need either limited access through Copilot Free or a paid Copilot plan for full access. For information about how to get access to Copilot, see [What is GitHub Copilot?](https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot#getting-access-to-copilot).
  * **GitHub Copilot extension for Eclipse**.To use GitHub Copilot in Eclipse, you must install the GitHub Copilot extension. See [Installing the GitHub Copilot extension in your environment](https://docs.github.com/en/copilot/configuring-github-copilot/installing-the-github-copilot-extension-in-your-environment?tool=eclipse).


## [Getting code suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#getting-code-suggestions-5)
GitHub Copilot offers coding suggestions as you type. For example, type this function header in a Java file:
Java```
public int getDiff(int a, int b)

```
```
public int getDiff(int a, int b)

```

GitHub Copilot will automatically suggest the rest of the function. To accept the suggestion, press `Tab`. To discard the suggestion, press `Esc`.
You can also describe something you want to do using natural language within a comment, and Copilot will suggest the code to accomplish your goal. For example, type this comment in a Java file:
Java```
/*
 * Return the difference between two different integers.
 */

```
```
/*
 * Return the difference between two different integers.
 */

```

GitHub Copilot will automatically suggest code.
If you receive limited or no suggestions from Copilot, you may have duplication detection enabled. For more information about duplication detection, see [Managing Copilot policies as an individual subscriber](https://docs.github.com/en/copilot/configuring-github-copilot/configuring-your-personal-github-copilot-settings-on-githubcom#enabling-or-disabling-suggestions-matching-public-code).
## [Manually triggering code completion](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#manually-triggering-code-completion)
You can also use keyboard shortcuts to trigger code completion.
OS | Trigger code completion  
---|---  
macOS |  `Option`+`Command`+`/`  
Windows or Linux |  `Ctrl`+`Alt`+`/`  
## [Accepting partial suggestions](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#accepting-partial-suggestions-3)
If you don't want to accept an entire suggestion from Copilot, you can accept the next word of a suggestion.
OS | Accept next word  
---|---  
macOS |  `Command`+`→`  
Windows or Linux |  `Ctrl`+`→`  
## [Next steps](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot#next-steps)
  * **Learn how to write effective prompts** - See [Prompt engineering for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot).
  * **Configure Copilot in your editor** - You can enable or disable GitHub Copilot from within your editor, and create your own preferred keyboard shortcuts for Copilot. See [Configuring GitHub Copilot in your environment](https://docs.github.com/en/copilot/configuring-github-copilot/configuring-github-copilot-in-your-environment).
  * **Get started with GitHub Copilot Chat** - Learn how to ask Copilot for information and assistance, using GitHub Copilot Chat. See [Asking GitHub Copilot questions in your IDE](https://docs.github.com/en/copilot/github-copilot-chat/using-github-copilot-chat-in-your-ide).
  * **Troubleshoot issues** - Learn more about how to troubleshoot common issues with GitHub Copilot. See [Troubleshooting GitHub Copilot](https://docs.github.com/en/copilot/troubleshooting-github-copilot).


