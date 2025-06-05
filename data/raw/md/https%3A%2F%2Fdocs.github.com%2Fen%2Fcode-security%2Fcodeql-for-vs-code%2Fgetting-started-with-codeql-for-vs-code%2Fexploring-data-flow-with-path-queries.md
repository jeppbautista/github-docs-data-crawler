  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL for VS Code](https://docs.github.com/en/code-security/codeql-for-vs-code "CodeQL for VS Code")/
  * [Getting started](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code "Getting started")/
  * [Explore data flow](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/exploring-data-flow-with-path-queries "Explore data flow")


# Exploring data flow with path queries
You can run CodeQL queries in Visual Studio Code to help you track the flow of data through a program, highlighting areas that are potential security vulnerabilities.
## In this article
  * [About path queries](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/exploring-data-flow-with-path-queries#about-path-queries)
  * [Running path queries in VS Code locally](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/exploring-data-flow-with-path-queries#running-path-queries-in-vs-code-locally)
  * [Next steps](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/exploring-data-flow-with-path-queries#next-steps)


## [About path queries](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/exploring-data-flow-with-path-queries#about-path-queries)
A path query is a CodeQL query with the property `@kind path-problem`. You can find a number of these in the standard CodeQL libraries.
You can run the standard CodeQL path queries to identify security vulnerabilities and manually look through the results. For more information about how CodeQL tracks data flow, see [About data flow analysis](https://codeql.github.com/docs/writing-codeql-queries/about-data-flow-analysis/) in the CodeQL documentation.
Once you're familiar with data flow analysis and existing queries, you can write your own path queries in CodeQL. For more information, see [Next steps](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/exploring-data-flow-with-path-queries#next-steps).
## [Running path queries in VS Code locally](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/exploring-data-flow-with-path-queries#running-path-queries-in-vs-code-locally)
  1. Open a path query in VS Code.
  2. Right-click in the window with the query open, and select **CodeQL: Run Query on Selected Database**. Alternatively, you can also run this from the VS Code Command Palette.
  3. Once the query has finished running, you can see the results in the "Results" view (under `alerts` in the dropdown menu). Each query result describes the flow of information between a source and a sink.
  4. Expand the result to see the individual steps that the data follows.
  5. Click each step to jump to it in the source code and investigate the problem further.


## [Next steps](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/exploring-data-flow-with-path-queries#next-steps)
When you are ready to run a path query at scale, you can use the "Variant Analysis Repositories" view to run the query against up to 1,000 repositories on GitHub.com. For more information, see [Running CodeQL queries at scale with multi-repository variant analysis](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/running-codeql-queries-at-scale-with-multi-repository-variant-analysis).
For information about how to use the correct format and metadata for your own path queries, see [Creating path queries](https://codeql.github.com/docs/writing-codeql-queries/creating-path-queries/#creating-path-queries) in the CodeQL documentation. The CodeQL documentation also contains detailed information about how to define new sources and sinks, as well as templates and examples of how to extend the standard CodeQL libraries to suit your analysis.
