  * [Codespaces](https://docs.github.com/en/codespaces "Codespaces")/
  * [Quickstart](https://docs.github.com/en/codespaces/quickstart "Quickstart")


# Quickstart for GitHub Codespaces
Get started with GitHub Codespaces quickly.
## In this article
  * [Introduction](https://docs.github.com/en/codespaces/quickstart#introduction)
  * [Creating your codespace](https://docs.github.com/en/codespaces/quickstart#creating-your-codespace)
  * [Running the application](https://docs.github.com/en/codespaces/quickstart#running-the-application)
  * [Edit the application and view changes](https://docs.github.com/en/codespaces/quickstart#edit-the-application-and-view-changes)
  * [Committing and pushing your changes](https://docs.github.com/en/codespaces/quickstart#committing-and-pushing-your-changes)
  * [Personalizing with an extension](https://docs.github.com/en/codespaces/quickstart#personalizing-with-an-extension)
  * [Next steps](https://docs.github.com/en/codespaces/quickstart#next-steps)
  * [Further reading](https://docs.github.com/en/codespaces/quickstart#further-reading)


## [Introduction](https://docs.github.com/en/codespaces/quickstart#introduction)
In this guide, you'll create a codespace from a template repository and explore some of the essential features available to you within the codespace. You'll work in the browser version of Visual Studio Code, which is initially the default editor for GitHub Codespaces. After trying out this quickstart you can use Codespaces in other editors, and you can change the default editor. Links are provided at the end of this guide.
From this quickstart, you'll learn how to create a codespace, connect to a forwarded port to view your running application, publish your codespace to a new repository, and personalize your setup with extensions.
For more information on exactly how GitHub Codespaces works, see the companion guide [Deep dive into GitHub Codespaces](https://docs.github.com/en/codespaces/about-codespaces/deep-dive).
## [Creating your codespace](https://docs.github.com/en/codespaces/quickstart#creating-your-codespace)
  1. Navigate to the [github/haikus-for-codespaces](https://github.com/github/haikus-for-codespaces) template repository.
  2. Click **Use this template** , then click **Open in a codespace**.
![Screenshot of the "Use this template" button and the dropdown menu expanded to show the "Open in a codespace" option.](https://docs.github.com/assets/cb-76823/images/help/repository/use-this-template-button.png)


## [Running the application](https://docs.github.com/en/codespaces/quickstart#running-the-application)
Once your codespace is created, the template repository will be automatically cloned into it. Now you can run the application and launch it in a browser.
  1. When the terminal becomes available, enter the command `npm run dev`. This example uses a Node.js project, and this command runs the script labeled "dev" in the `package.json` file, which starts up the web application defined in the sample repository.
![Screenshot of the Terminal in VS Code with the "npm run dev" command entered.](https://docs.github.com/assets/cb-36170/images/help/codespaces/codespaces-npm-run-dev.png)
If you're following along with a different application type, enter the corresponding start command for that project.
  2. When your application starts, the codespace recognizes the port the application is running on and displays a pop-up message to let you know that the port has been forwarded.
![Screenshot of the pop-up message: "Your application running on port 3000 is available." Below this is a green button, labeled "Open in Browser."](https://docs.github.com/assets/cb-17218/images/help/codespaces/quickstart-port-toast.png)
  3. Click **Open in Browser** to view your running application in a new tab.


## [Edit the application and view changes](https://docs.github.com/en/codespaces/quickstart#edit-the-application-and-view-changes)
  1. Switch back to your codespace and open the `haikus.json` file by clicking it in the Explorer.
  2. Edit the `text` field of the first haiku to personalize the application with your own haiku.
  3. Go back to the running application tab in your browser and refresh to see your changes.
**Local Address** value for the running port, and click the **Open in Browser** icon.
![Screenshot of the "Ports" panel. The "Ports" tab and a globe icon, which opens the forwarded port in a browser, are highlighted with orange outlines.](https://docs.github.com/assets/cb-25086/images/help/codespaces/quickstart-forward-port.png)


## [Committing and pushing your changes](https://docs.github.com/en/codespaces/quickstart#committing-and-pushing-your-changes)
Now that you've made a few changes, you can use the integrated terminal or the source view to publish your work to a new repository.
  1. In the Activity Bar, click the **Source Control** view.
![Screenshot of the VS Code Activity Bar with the source control button highlighted with an orange outline.](https://docs.github.com/assets/cb-33788/images/help/codespaces/source-control-activity-bar-button.png)
  2. To stage your changes, click `haikus.json` file, or next to **Changes** if you've changed multiple files and you want to stage them all.
![Screenshot of the "Source control" side bar with the staging button \(a plus sign\), to the right of "Changes," highlighted with a dark orange outline.](https://docs.github.com/assets/cb-33843/images/help/codespaces/codespaces-commit-stage.png)
  3. To commit your staged changes, type a commit message describing the change you've made, then click **Commit**.
![Screenshot of the "Source control" side bar. The commit message, "Change haiku text and styles," and the "Commit" button are outlined in orange.](https://docs.github.com/assets/cb-38443/images/help/codespaces/vscode-commit-button.png)
  4. Click **Publish Branch**.
![Screenshot of the "Source control" side bar showing the "Publish Branch" button.](https://docs.github.com/assets/cb-15968/images/help/codespaces/vscode-publish-branch-button.png)
  5. In the "Repository Name" dropdown, type a name for your new repository, then select **Publish to GitHub private repository** or **Publish to GitHub public repository**.
![Screenshot of the repository name dropdown in VS Code. Two options are shown, for publishing to a private or a public repository.](https://docs.github.com/assets/cb-24667/images/help/codespaces/choose-new-repository.png)
The owner of the new repository will be the GitHub account with which you created the codespace.
  6. In the pop-up that appears in the lower right corner of the editor, click **Open on GitHub** to view the new repository on GitHub. In the new repository, view the `haikus.json` file and check that the change you made in your codespace has been successfully pushed to the repository.
![Screenshot of a confirmation message for a successfully published repository, showing the "Open on GitHub" button.](https://docs.github.com/assets/cb-33916/images/help/codespaces/open-on-github.png)


## [Personalizing with an extension](https://docs.github.com/en/codespaces/quickstart#personalizing-with-an-extension)
When you connect to a codespace using the browser, or the Visual Studio Code desktop application, you can access the Visual Studio Code Marketplace directly from the editor. For this example, you'll install a VS Code extension that alters the theme, but you can install any extension that's useful for your workflow.
  1. In the Activity Bar, click the Extensions icon.
![Screenshot of the Activity Bar. The Extensions icon is highlighted with an orange outline.](https://docs.github.com/assets/cb-2620/images/help/codespaces/extensions-activity-bar-icon.png)
  2. In the search bar, type `fairyfloss` and click **Install**.
![Screenshot of "Extensions: Marketplace". The search box shows "fairyfloss." The results show the "fairyfloss" extension with an "Install" button.](https://docs.github.com/assets/cb-25167/images/help/codespaces/add-extension.png)
  3. Select the `fairyfloss` theme by selecting it from the list.
![Screenshot of the "Select Color Theme" dropdown, with the "fairyfloss" theme selected.](https://docs.github.com/assets/cb-57096/images/help/codespaces/fairyfloss.png)


### [About Settings Sync](https://docs.github.com/en/codespaces/quickstart#about-settings-sync)
You can enable Settings Sync to sync extensions and other settings across devices and instances of VS Code. Your synced settings are cached in the cloud. If Settings Sync is turned on in a codespace, any updates you make to your settings in the codespace are pushed to the cloud, and any updates you push to the cloud from elsewhere are pulled into your codespace. For more information, see [Personalizing GitHub Codespaces for your account](https://docs.github.com/en/codespaces/setting-your-user-preferences/personalizing-github-codespaces-for-your-account#settings-sync).
## [Next steps](https://docs.github.com/en/codespaces/quickstart#next-steps)
You've successfully created, personalized, and run your first application within a codespace but there's so much more to explore! Here are some helpful resources for taking your next steps with GitHub Codespaces.
  * [Deep dive into GitHub Codespaces](https://docs.github.com/en/codespaces/about-codespaces/deep-dive): This quickstart presented some of the features of GitHub Codespaces. The deep dive looks at these areas from a technical standpoint.
  * [Adding a dev container configuration to your repository](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration): These guides provide information on setting up your repository to use GitHub Codespaces with specific languages.
  * [Introduction to dev containers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers): This guide provides details on creating a custom configuration for Codespaces for your project.


## [Further reading](https://docs.github.com/en/codespaces/quickstart#further-reading)
  * [Enabling or disabling GitHub Codespaces for your organization](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/enabling-or-disabling-github-codespaces-for-your-organization)
  * [Using GitHub Codespaces in Visual Studio Code](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-github-codespaces-in-visual-studio-code)
  * [Using GitHub Codespaces with GitHub CLI](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-github-codespaces-with-github-cli)
  * [Setting your default editor for GitHub Codespaces](https://docs.github.com/en/codespaces/setting-your-user-preferences/setting-your-default-editor-for-github-codespaces).
  * [Managing the cost of GitHub Codespaces in your organization](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/managing-the-cost-of-github-codespaces-in-your-organization)


