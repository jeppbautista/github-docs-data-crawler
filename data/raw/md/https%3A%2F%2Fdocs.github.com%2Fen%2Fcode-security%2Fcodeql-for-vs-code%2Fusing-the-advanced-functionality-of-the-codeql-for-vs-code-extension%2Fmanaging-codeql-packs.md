  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL for VS Code](https://docs.github.com/en/code-security/codeql-for-vs-code "CodeQL for VS Code")/
  * [Advanced functionality](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension "Advanced functionality")/
  * [Manage CodeQL packs](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/managing-codeql-packs "Manage CodeQL packs")


# Managing CodeQL query packs and library packs
You can view, write, and edit CodeQL query and library packs in Visual Studio Code using the CodeQL extension.
## In this article
  * [Benefits of using the CodeQL extension for Visual Studio Code to work with packs](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/managing-codeql-packs#benefits-of-using-the-codeql-extension-for-visual-studio-code-to-work-with-packs)
  * [Installing dependencies for CodeQL query packs](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/managing-codeql-packs#installing-dependencies-for-codeql-query-packs)
  * [Downloading CodeQL query packs](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/managing-codeql-packs#downloading-codeql-query-packs)
  * [Viewing a CodeQL query pack and its dependencies](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/managing-codeql-packs#viewing-a-codeql-query-pack-and-its-dependencies)
  * [Working with CodeQL model packs](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/managing-codeql-packs#working-with-codeql-model-packs)


## [Benefits of using the CodeQL extension for Visual Studio Code to work with packs](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/managing-codeql-packs#benefits-of-using-the-codeql-extension-for-visual-studio-code-to-work-with-packs)
With the CodeQL for Visual Studio Code extension, you can:
  * Write CodeQL query packs without needing to check out the standard libraries in your workspace.
  * Install dependencies for CodeQL query packs inside your VS Code workspace.
  * Download CodeQL query packs.
  * View a CodeQL query pack and all of its dependencies.


For more information about creating and editing CodeQL query and library packs, see [Creating and working with CodeQL packs](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/creating-and-working-with-codeql-packs).
## [Installing dependencies for CodeQL query packs](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/managing-codeql-packs#installing-dependencies-for-codeql-query-packs)
  1. In VS Code, open the VS Code Command Palette and run **CodeQL: Install Pack Dependencies**.
  2. Select the packs that you want to install dependencies for.


## [Downloading CodeQL query packs](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/managing-codeql-packs#downloading-codeql-query-packs)
  1. In VS Code, open the VS Code Command Palette and run **CodeQL: Download Packs**.
  2. You can download all the core query packs, or enter the full name of a specific pack to download. You can download query packs created by other users.


## [Viewing a CodeQL query pack and its dependencies](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/managing-codeql-packs#viewing-a-codeql-query-pack-and-its-dependencies)
  1. In VS Code, open the `qlpack.yml` file in the root of any CodeQL pack directory.
  2. In the `dependencies` section of the `qlpack.yml` file, you'll see what libraries the pack depends on.
  3. Optionally, you can use VS Code's Intellisense features. For example, if you hover over an element from a library depended on by the pack, Visual Studio Code will resolve it so you can see documentation about the element.
  4. To view the full definition of an element of a query, you can right-click and select **Go to Definition**.
     * If the library pack is present within the same Visual Studio Code workspace, this will take you to the definition within the workspace.
     * Otherwise, you will see the definition stored in your package cache, where downloaded dependencies are saved. The package cache is a shared location that is stored in your home directory by default.


## [Working with CodeQL model packs](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/managing-codeql-packs#working-with-codeql-model-packs)
CodeQL model packs are currently in public preview and subject to change. Model packs are supported for C/C++, C#, Java/Kotlin, Python, and Ruby analysis.
The CodeQL model editor in the CodeQL extension for Visual Studio Code supports modeling dependencies for C#, Java/Kotlin, Python, and Ruby.
CodeQL model packs can be used to expand code scanning analysis to include dependencies that are not supported by default. The CodeQL extension for Visual Studio Code includes a dedicated editor for creating and editing model packs. For information on using the model editor, see [Using the CodeQL model editor](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/using-the-codeql-model-editor).
