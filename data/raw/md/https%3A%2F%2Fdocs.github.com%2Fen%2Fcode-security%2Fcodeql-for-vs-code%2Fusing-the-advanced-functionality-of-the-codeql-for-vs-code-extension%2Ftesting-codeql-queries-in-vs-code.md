  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL for VS Code](https://docs.github.com/en/code-security/codeql-for-vs-code "CodeQL for VS Code")/
  * [Advanced functionality](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension "Advanced functionality")/
  * [Test CodeQL queries](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/testing-codeql-queries-in-vs-code "Test CodeQL queries")


# Testing CodeQL queries in Visual Studio Code
You can run unit tests for CodeQL queries using the Visual Studio Code extension.
## In this article
  * [About testing queries in VS Code](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/testing-codeql-queries-in-vs-code#about-testing-queries-in-vs-code)
  * [Testing the results of your queries](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/testing-codeql-queries-in-vs-code#testing-the-results-of-your-queries)
  * [Monitoring the performance of your queries](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/testing-codeql-queries-in-vs-code#monitoring-the-performance-of-your-queries)
  * [Next steps](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/testing-codeql-queries-in-vs-code#next-steps)


## [About testing queries in VS Code](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/testing-codeql-queries-in-vs-code#about-testing-queries-in-vs-code)
To ensure that your CodeQL queries produce the expected results, you can run tests that compare the expected query results with the actual results.
The CodeQL extension automatically registers itself with the "Testing" view. This view displays all tests found in your current workspace and provides a UI for exploring and running tests in your workspace.
For more information about creating CodeQL tests, see [Testing custom queries](https://docs.github.com/en/code-security/codeql-cli/using-the-codeql-cli/testing-custom-queries).
To see more detailed output from running unit tests, open the CodeQL Tests log. For information, see [Accessing logs](https://docs.github.com/en/code-security/codeql-for-vs-code/troubleshooting-codeql-for-vs-code/accessing-logs).
## [Testing the results of your queries](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/testing-codeql-queries-in-vs-code#testing-the-results-of-your-queries)
  1. In Visual Studio Code, open the "Testing" view in the sidebar.
  2. To run a specific test, hover over the file or folder name and click the play button. To run all tests in your workspace, click the play button at the top of the view. If a test takes too long to run, you can click the stop button at the top of the view to cancel the test.
![Screenshot of the "Testing" view, with the "Run Test" button \(to run all tests\) outlined in dark orange.](https://docs.github.com/assets/cb-44333/images/help/security/codeql-for-vs-code-run-all-tests.png)
  3. The icons show whether a test passed or failed. If it failed, click the test in the "Test Results" to display the differences between the expected output and the actual output.
![Screenshot of the "Test Results" view displaying the differences between the expected output and actual output for a test.](https://docs.github.com/assets/cb-125782/images/help/security/codeql-for-vs-code-test-output.png)
  4. Compare the results. If you want to update the test with the actual output, right-click the test in the "Testing" view and click **Accept Test Output**.


## [Monitoring the performance of your queries](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/testing-codeql-queries-in-vs-code#monitoring-the-performance-of-your-queries)
Query performance is important when you want to run a query on large databases, or as part of your continuous integration system.
If you want to examine query performance, enable the "Running Queries: Debug" setting to include timing and tuple counts. This will then be shown in the logs in the CodeQL "Query Server" tab of the "Output" view. The tuple count is useful because it indicates the size of the [predicates](https://codeql.github.com/docs/ql-language-reference/predicates/#predicates) computed by the query. For more information about changing settings, see [Customizing settings](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/customizing-settings#configuring-settings-for-running-queries-locally).
When a query is evaluated, the query server caches the predicates that it calculates. So when you want to compare the performance of two evaluations, you should run **CodeQL: Clear Cache** to clear the query server's cache before each run. This ensures that you're comparing equivalent data.
For more information about monitoring the performance of your CodeQL queries, see [Troubleshooting query performance](https://codeql.github.com/docs/writing-codeql-queries/troubleshooting-query-performance/#troubleshooting-query-performance) and [Evaluation of QL programs](https://codeql.github.com/docs/ql-language-reference/evaluation-of-ql-programs/#evaluation-of-ql-programs) in the CodeQL documentation.
## [Next steps](https://docs.github.com/en/code-security/codeql-for-vs-code/using-the-advanced-functionality-of-the-codeql-for-vs-code-extension/testing-codeql-queries-in-vs-code#next-steps)
When you are sure that your query finds the results you want to identify, you can use variant analysis to run it at scale. For information on running analysis at scale across many CodeQLdatabases, see [Running CodeQL queries at scale with multi-repository variant analysis](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/running-codeql-queries-at-scale-with-multi-repository-variant-analysis).
