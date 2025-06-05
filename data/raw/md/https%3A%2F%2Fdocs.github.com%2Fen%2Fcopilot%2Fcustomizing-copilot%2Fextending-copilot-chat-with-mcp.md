  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Customize Copilot](https://docs.github.com/en/copilot/customizing-copilot "Customize Copilot")/
  * [Extend Copilot Chat with MCP](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp "Extend Copilot Chat with MCP")


# Extending Copilot Chat with the Model Context Protocol (MCP)
Learn how to use the Model Context Protocol (MCP) to extend Copilot Chat.
## Tool navigation
  * [Eclipse](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp?tool=eclipse)
  * [JetBrains IDEs](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp?tool=jetbrains)
  * [Visual Studio Code](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp?tool=vscode)
  * [Xcode](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp?tool=xcode)


## In this article
  * [Overview](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp#overview)
  * [Prerequisites](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp#prerequisites)
  * [Configuring MCP servers in Visual Studio Code](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp#configuring-mcp-servers-in-visual-studio-code)
  * [Using MCP servers in Copilot Chat](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp#using-mcp-servers-in-copilot-chat)
  * [Using existing MCP configurations](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp#using-existing-mcp-configurations)
  * [Overview](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp#overview-1)
  * [Prerequisites](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp#prerequisites-1)
  * [Configuring MCP servers in JetBrains IDEs](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp#configuring-mcp-servers-in-jetbrains-ides)
  * [Overview](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp#overview-2)
  * [Prerequisites](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp#prerequisites-2)
  * [Configuring MCP servers in Xcode](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp#configuring-mcp-servers-in-xcode)
  * [Overview](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp#overview-3)
  * [Prerequisites](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp#prerequisites-3)
  * [Configuring MCP servers in Eclipse](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp#configuring-mcp-servers-in-eclipse)
  * [Creating a new MCP server](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp#creating-a-new-mcp-server)
  * [Further reading](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp#further-reading)


  * MCP support is currently in public preview and subject to change.
  * MCP support is available in Copilot Chat for Visual Studio Code, JetBrains, Eclipse, and Xcode.
  * The [GitHub Pre-release License Terms](https://docs.github.com/en/site-policy/github-terms/github-pre-release-license-terms) apply to your use of this product.


## [Overview](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp#overview)
The Model Context Protocol (MCP) is an open standard that defines how applications share context with large language models (LLMs). MCP provides a standardized way to connect AI models to different data sources and tools, enabling them to work together more effectively.
You can use MCP to extend the capabilities of Copilot Chat by integrating it with a wide range of existing tools and services. For example, the GitHub MCP server allows you to use Copilot Chat in Visual Studio Code to perform tasks on GitHub. You can also use MCP to create new tools and services that work with Copilot Chat, allowing you to customize and enhance your experience.
For more information on MCP, see [the official MCP documentation](https://modelcontextprotocol.io/introduction).
For information on some of the other currently available MCP servers, see [the MCP servers repository](https://github.com/modelcontextprotocol/servers/tree/main).
## [Prerequisites](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp#prerequisites)
  * **Access to Copilot**. For information about how to get access to Copilot, see [What is GitHub Copilot?](https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot#getting-access-to-copilot).
  * **Visual Studio Code version 1.99 or later**. For information on installing Visual Studio Code, see the [Visual Studio Code download page](https://code.visualstudio.com/Download).


## [Configuring MCP servers in Visual Studio Code](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp#configuring-mcp-servers-in-visual-studio-code)
To configure MCP servers in Visual Studio Code, you need to set up a configuration script that specifies the details of the MCP servers you want to use. You can configure MCP servers for either:
  * **A specific repository**. This will share MCP servers with anyone who opens the project in Visual Studio Code. To do this, create a `.vscode/mcp.json` file in the root of your repository.
  * **Your personal instance of Visual Studio Code**. You will be the only person who has access to configured MCP servers. To do this, add the configuration to your `settings.json` file in Visual Studio Code.
We recommend you use only one location per server. Adding the same server to both locations may cause conflicts and unexpected behavior.


The steps below show how to configure the Fetch MCP server in your `.vscode/mcp.json` file. The Fetch MCP server is a simple MCP server that provides web content fetching capabilities. For more information on the Fetch MCP server, see [the Fetch directory](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) in the MCP Server repository.
You can use the same steps to configure MCP servers in your personal Visual Studio Code settings. Details on how to configure other MCP servers are available in the [MCP servers repository](https://github.com/modelcontextprotocol/servers/tree/main).
  1. Add the following configuration to your `.vscode/mcp.json` file:
JSON```
{
"inputs": [
  // The "inputs" section defines the inputs required for the MCP server configuration.
  {
    "type": "promptString"
  }
],
"servers": {
  // The "servers" section defines the MCP servers you want to use.
  "fetch": {
    "command": "uvx",
    "args": ["mcp-server-fetch"]
  }
 }
}

```
```
{
"inputs": [
  // The "inputs" section defines the inputs required for the MCP server configuration.
  {
    "type": "promptString"
  }
],
"servers": {
  // The "servers" section defines the MCP servers you want to use.
  "fetch": {
    "command": "uvx",
    "args": ["mcp-server-fetch"]
  }
 }
}

```

  2. Save the `.vscode/mcp.json` file.
  3. A "Start" button will appear in your `.vscode/mcp.json` file, at the top of the list of servers. Click the "Start" button to start the MCP servers. This will trigger the input dialog and discover the server tools, which are then stored for later sessions.
![Screenshot of MCP server configuration in Visual Studio Code. The "Start" button is outlined in dark orange. ](https://docs.github.com/assets/cb-51859/images/help/copilot/mcp-start-server-button.png)
  4. Open Copilot Chat by clicking the 
  5. In the Copilot Chat box, select **Agent** from the popup menu.
![Screenshot of the Copilot Chat box in Visual Studio Code. The "Agent" option is outlined in dark orange.](https://docs.github.com/assets/cb-38150/images/help/copilot/copilot-chat-agent-option.png)
  6. To view your list of available MCP servers, click the tools icon in the top left corner of the chat box. This will open the MCP server list, where you can see all the MCP servers and associated tools that are currently available in your Visual Studio Code instance.


For more information on configuring MCP servers in Visual Studio Code, see [Use MCP servers in Visual Studio Code (Preview)](https://aka.ms/vscode-add-mcp) in the Visual Studio Code documentation.
Beginning April 4, 2025, the GitHub MCP server, and installation instructions, will be publicly available in the [github-mcp-server](https://github.com/github/github-mcp-server) repository.
## [Using MCP servers in Copilot Chat](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp#using-mcp-servers-in-copilot-chat)
Once you have configured your MCP servers, you can use them in Copilot Chat to access a wide range of tools and services. In the example below, we will use the Fetch MCP server to fetch details about a web page.
  1. Open Copilot Chat by clicking the 
  2. In the Copilot Chat box, select **Agent** from the popup menu.
  3. In the file with the MCP configuration, check that the MCP server is running. If it is not running, click the "Start" button to start the MCP server.
![Screenshot of the MCP server configuration in Visual Studio Code. The "Running" status is outlined in dark orange.](https://docs.github.com/assets/cb-68101/images/help/copilot/vsc-mcp-server-running.png)
  4. Ask Copilot Chat to fetch the details of a URL. For example:
`Fetch https://github.com/github/docs.`
  5. If Copilot asks you to confirm that you want to proceed, click **Continue**.
  6. Copilot will fetch the details of the URL and display them in the chat box.


For more information on using MCP servers in Visual Studio Code, see [Use MCP servers in Visual Studio Code (Preview)](https://aka.ms/vscode-add-mcp) in the Visual Studio Code documentation.
## [Using existing MCP configurations](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp#using-existing-mcp-configurations)
If you already have an MCP configuration in Claude Desktop, you can use that configuration in Visual Studio Code to access the same MCP servers. To do this, add the following configuration to your `settings.json` file in Visual Studio Code:
JSON```
"chat.mcp.discovery.enabled": true

```
```
"chat.mcp.discovery.enabled": true

```

Visual Studio Code will automatically find your existing configuration and use it in your Visual Studio Code instance.
## [Overview](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp#overview-1)
The Model Context Protocol (MCP) is an open standard that defines how applications share context with large language models (LLMs). MCP provides a standardized way to connect AI models to different data sources and tools, enabling them to work together more effectively.
You can use MCP to extend the capabilities of Copilot Chat by integrating it with a wide range of existing tools and services. You can also use MCP to create new tools and services that work with Copilot Chat, allowing you to customize and enhance your experience.
For more information on MCP, see [the official MCP documentation](https://modelcontextprotocol.io/introduction).
For information on other currently available MCP servers, see [the MCP servers repository](https://github.com/modelcontextprotocol/servers/tree/main).
## [Prerequisites](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp#prerequisites-1)
  * **Access to Copilot**. For information about how to get access to Copilot, see [What is GitHub Copilot?](https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot#getting-access-to-copilot).
  * **A compatible JetBrains IDE**. GitHub Copilot is compatible with the following IDEs:
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


## [Configuring MCP servers in JetBrains IDEs](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp#configuring-mcp-servers-in-jetbrains-ides)
  1. In the lower right corner, click 
  2. From the menu, select "Edit settings".
  3. Under the MCP section, click "Edit in `mcp.json`".
  4. Define your MCP servers. You can use the following configuration as an example:
JSON```
{
  "servers": {
    "memory": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-memory"
      ]
    }
  }
}

```
```
{
  "servers": {
    "memory": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-memory"
      ]
    }
  }
}

```



Alternatively, to access the MCP settings, once you're in "Agent Mode", click the tools icon, then click **Add more tools**.
## [Overview](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp#overview-2)
The Model Context Protocol (MCP) is an open standard that defines how applications share context with large language models (LLMs). MCP provides a standardized way to connect AI models to different data sources and tools, enabling them to work together more effectively.
You can use MCP to extend the capabilities of Copilot Chat by integrating it with a wide range of existing tools and services. You can also use MCP to create new tools and services that work with Copilot Chat, allowing you to customize and enhance your experience.
For more information on MCP, see [the official MCP documentation](https://modelcontextprotocol.io/introduction).
For information on other currently available MCP servers, see [the MCP servers repository](https://github.com/modelcontextprotocol/servers/tree/main).
## [Prerequisites](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp#prerequisites-2)
  * **Access to Copilot**. For information about how to get access to Copilot, see [What is GitHub Copilot?](https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot#getting-access-to-copilot).
  * **GitHub Copilot for Xcode extension**. See [Installing the GitHub Copilot extension in your environment](https://docs.github.com/en/copilot/configuring-github-copilot/installing-the-github-copilot-extension-in-your-environment).


## [Configuring MCP servers in Xcode](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp#configuring-mcp-servers-in-xcode)
  1. Open the GitHub Copilot for Xcode extension.
  2. In agent mode, click the tools icon.
  3. Select "Edit config".
  4. Define your MCP servers, editing `mcp.json`. You can use the following configuration as an example:
JSON```
{
  "servers": {
    "memory": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-memory"
      ]
    }
  }
}

```
```
{
  "servers": {
    "memory": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-memory"
      ]
    }
  }
}

```



## [Overview](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp#overview-3)
The Model Context Protocol (MCP) is an open standard that defines how applications share context with large language models (LLMs). MCP provides a standardized way to connect AI models to different data sources and tools, enabling them to work together more effectively.
You can use MCP to extend the capabilities of Copilot Chat by integrating it with a wide range of existing tools and services. You can also use MCP to create new tools and services that work with Copilot Chat, allowing you to customize and enhance your experience.
For more information on MCP, see [the official MCP documentation](https://modelcontextprotocol.io/introduction).
For information on other currently available MCP servers, see [the MCP servers repository](https://github.com/modelcontextprotocol/servers/tree/main).
## [Prerequisites](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp#prerequisites-3)
  * **Access to Copilot**. To use GitHub Copilot in Eclipse, you must have an active GitHub Copilot subscription. For information about how to get access to Copilot, see [What is GitHub Copilot?](https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot#getting-access-to-copilot).
  * **Compatible version of Eclipse**. To use the GitHub Copilot extension, you must have Eclipse version 2024-09 or above. See the [Eclipse download page](https://www.eclipse.org/downloads/packages/).
  * **Latest version of the GitHub Copilot extension**. Download this from the [Eclipse Marketplace](https://aka.ms/copiloteclipse). For more information, see [Installing the GitHub Copilot extension in your environment](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/installing-the-github-copilot-extension-in-your-environment?tool=eclipse).
  * **Sign in to GitHub from Eclipse**.


## [Configuring MCP servers in Eclipse](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp#configuring-mcp-servers-in-eclipse)
  1. To open the Copilot Chat panel, click the Copilot icon (
  2. From the menu, select "Edit preferences".
  3. In the left pane, expand Copilot Chat and click **MCP**.
  4. Define your MCP servers. You can use the following configuration as an example:
JSON```
{
  "servers": {
    "memory": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-memory"
      ]
    }
  }
}

```
```
{
  "servers": {
    "memory": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-memory"
      ]
    }
  }
}

```



## [Creating a new MCP server](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp#creating-a-new-mcp-server)
You can create a new MCP server to fulfill your specific needs, and then integrate it with Copilot Chat. For example, you can create an MCP server that connects to a database or a web service, and then use that server in Copilot Chat to perform tasks on that database or web service.
For more information on creating and configuring your own MCP servers, see [the official MCP documentation](https://modelcontextprotocol.io/quickstart/server).
## [Further reading](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp#further-reading)
  * [Extending Copilot coding agent with the Model Context Protocol (MCP)](https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-coding-agent-with-mcp)


