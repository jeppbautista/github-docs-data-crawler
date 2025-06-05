  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Use GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot "Use GitHub Copilot")/
  * [Guides](https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot "Guides")/
  * [Upgrade Java projects](https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot/upgrading-java-projects-with-github-copilot "Upgrade Java projects")


# Upgrading Java projects with GitHub Copilot
You can use GitHub Copilot to upgrade your Maven and Gradle Java applications.
## In this article
  * [Introduction](https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot/upgrading-java-projects-with-github-copilot#introduction)
  * [Prerequisites](https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot/upgrading-java-projects-with-github-copilot#prerequisites)
  * [Upgrading a Java project](https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot/upgrading-java-projects-with-github-copilot#upgrading-a-java-project)


GitHub Copilot app modernization – upgrade for Java is currently in public preview and subject to change.
## [Introduction](https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot/upgrading-java-projects-with-github-copilot#introduction)
GitHub Copilot can help streamline the process of upgrading Java applications. The "GitHub Copilot app modernization – upgrade for Java" Visual Studio Code extension assists with every step of upgrading your Java project's runtime and/or framework version.
  * Analyzing the project and dependencies to generate an upgrade plan.
  * Executing code transformations based on the plan.
  * Automatically fixing issues during the upgrade.
  * Providing detailed logs, commit history, and output.
  * Performing security scans (CVE) and behavioral consistency checks post-upgrade.
  * Summarizing key changes including updated dependencies and resolved issues.
  * Generating unit tests independently of the upgrade process.


This solution supports both Maven and Gradle build tools and facilitates upgrades between Java versions 8, 11, 17, and 21.
## [Prerequisites](https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot/upgrading-java-projects-with-github-copilot#prerequisites)
Before getting started you must have the following:
  * Either a **GitHub Copilot Business** or **GitHub Copilot Enterprise** [subscription plan](https://docs.github.com/en/copilot/about-github-copilot/subscription-plans-for-github-copilot).
  * The latest version of [Visual Studio Code](https://code.visualstudio.com/).
  * The "GitHub Copilot app modernization – upgrade for Java (preview)" extension installed in Visual Studio Code.
  * Installed versions of both the source and target JDKs.
  * A Git-based Java project using Maven or Gradle.
  * For Maven-based projects, access to the public Maven Central repository.


For Gradle projects, only wrapper-based builds (Gradle v5+) are supported. Projects using Kotlin DSL are not currently supported.
## [Upgrading a Java project](https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot/upgrading-java-projects-with-github-copilot#upgrading-a-java-project)
### [1. Install the required extension](https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot/upgrading-java-projects-with-github-copilot#1-install-the-required-extension)
To get started, you'll need to install the “GitHub Copilot app modernization – upgrade for Java (preview)” extension for Visual Studio Code.
  1. Open Visual Studio Code.
  2. Click on “Extensions”.
  3. Search for “GitHub Copilot app modernization – upgrade for Java (preview)” and click “Download”.
  4. Restart Visual Studio Code.


### [2. Use GitHub Copilot Chat in agent mode and generate the upgrade plan](https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot/upgrading-java-projects-with-github-copilot#2-use-github-copilot-chat-in-agent-mode-and-generate-the-upgrade-plan)
Now you have the extension, you can continue to use GitHub Copilot in agent mode and create a plan for your upgrade.
  1. In Visual Studio Code, open the GitHub Copilot Chat panel.
  2. At the bottom of the chat panel, select **Agent** from the mode dropdown.
  3. Enter a prompt describing the upgrade path you need. For example:
> "Upgrade project to Java 21 and Spring Boot 3.2"
  4. When prompted, click **Continue** to generate an upgrade plan


### [3. Review and edit the upgrade plan](https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot/upgrading-java-projects-with-github-copilot#3-review-and-edit-the-upgrade-plan)
GitHub Copilot will analyze your project's structure, JDK, dependencies, and build tool before generating a `plan.md` upgrade plan for your specific circumstances that outlines source and target JDK versions and upgrade paths for frameworks and libraries.
  1. Click on the new `plan.md` tab in Visual Studio Code.
  2. Review, and edit if necessary, the plan. Make sure the versions in the plan align with your goals and what you've already specified.
  3. When you're ready, click **Continue** to proceed.


### [4. Apply code changes and fix build issues](https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot/upgrading-java-projects-with-github-copilot#4-apply-code-changes-and-fix-build-issues)
Next, GitHub Copilot will begin transforming your project. This involves using OpenRewrite to apply code changes via predefined recipes and iteratively fixing remaining issues with Copilot through a build/fix loop.
  1. When prompted to "Run Upgrade Java code using OpenRewrite", click **Continue**. Note that this step may take some time.
  2. When prompted to "Run Build project and fix errors", click **Continue**.


You can track the progress of this phase by viewing the `progress.md` file in Visual Studio Code.
### [5. Check for security vulnerabilities (CVE) and code behavior changes](https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot/upgrading-java-projects-with-github-copilot#5-check-for-security-vulnerabilities-cve-and-code-behavior-changes)
To ensure reliability and security, GitHub Copilot performs additional checks.
  1. When prompted to "Run Validate if any modified dependencies have known CVEs", click **Continue**.
If CVEs are detected, Copilot will try to resolve them. You can review and accept or reject the changes.
  2. When prompted to "Run Validate code behavior consistency", click **Continue**.
If inconsistencies are found, Copilot will again attempt fixes and you can decide which to keep.


At the end of this process, the tool rebuilds the project and runs one final validation. The process concludes if only minor issues that don’t block the upgrade may remain. Otherwise, it loops back to address outstanding problems.
### [6. View the Upgrade Summary](https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot/upgrading-java-projects-with-github-copilot#6-view-the-upgrade-summary)
Once completed, Copilot generates a `summary.md` file in your project directory containing:
  * Project metadata.
  * Lines of code modified.
  * Updated dependencies.
  * Description of code changes.
  * CVEs and inconsistencies resolved.
  * Remaining minor CVE issues (if any).


