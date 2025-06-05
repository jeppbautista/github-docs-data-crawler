  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Dependabot](https://docs.github.com/en/code-security/dependabot "Dependabot")/
  * [Dependabot ecosystems](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot "Dependabot ecosystems")/
  * [Optimize Java packages](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/optimizing-java-packages-dependabot "Optimize Java packages")


# Optimizing Java packages for Dependabot updates
By including metadata in your `pom.xml` file, you can enhance the information available to users in Dependabot pull requests to update your Java packages.
## In this article
  * [Including the metadata Dependabot needs in pom.xml files](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/optimizing-java-packages-dependabot#including-the-metadata-dependabot-needs-in-pomxml-files)
  * [Impact of omitting project metadata from pom.xml files](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/optimizing-java-packages-dependabot#impact-of-omitting-project-metadata-from-pomxml-files)
  * [Further reading](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/optimizing-java-packages-dependabot#further-reading)


Dependabot uses the information defined in `pom.xml` files to create pull requests to update Java dependencies for the Gradle and Maven ecosystems. When you include the project metadata that Dependabot expects, pull requests contain links to the release notes for the suggested package update and a link where users can report any issues. This information means that users can update their packages with confidence after reviewing all the release information.
## [Including the metadata Dependabot needs in pom.xml files](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/optimizing-java-packages-dependabot#including-the-metadata-dependabot-needs-in-pomxml-files)
Dependabot uses the URLs for the project, the source code management system, and the issue management system to build the summary for update pull requests.
  * `url` the home page for the project, see [More Project Information](https://maven.apache.org/pom.html#More_Project_Information) in the POM reference
  * `scm` the URL of the source code management system used by the project, see [SCM](https://maven.apache.org/pom.html#scm) in the POM Reference
  * `issueManagement` the URL of the issue management system used by the project, see [Issue Management](https://maven.apache.org/pom.html#issue-management) in the POM Reference


### [Example for a project hosted on GitHub](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/optimizing-java-packages-dependabot#example-for-a-project-hosted-on-github)
```
<project>
  <url>https://github.com/OWNER/REPOSITORY</url>
  <scm>
    <url>https://github.com/OWNER/REPOSITORY</url>
  </scm>
  <issueManagement>
    <url>https://github.com/OWNER/REPOSITORY/issues</url>
  </issueManagement>
</project>

```

Replace `OWNER` and `REPOSITORY` with the detailed for your project.
## [Impact of omitting project metadata from pom.xml files](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/optimizing-java-packages-dependabot#impact-of-omitting-project-metadata-from-pomxml-files)
If you forget to include the URLs that Dependabot checks for, then pull requests to update Java packages are still created. However, the information available to users in the pull request summary will be limited.
  * **Project repository or Source code management URL undefined:** no links to release notes in Dependabot pull requests
  * **Issue management URL undefined:** no link to the issues page for reporting problems.


Adding this information helps Dependabot provide better, more accurate updates for your project, complete with helpful links to release notes and issue trackers.
## [Further reading](https://docs.github.com/en/code-security/dependabot/ecosystems-supported-by-dependabot/optimizing-java-packages-dependabot#further-reading)
  * [Maven SCM Plugin](https://maven.apache.org/scm/maven-scm-plugin/)


