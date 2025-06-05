  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli "CodeQL CLI")/
  * [Advanced functionality](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli "Advanced functionality")/
  * [CodeQL CLI CSV output](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/csv-output "CodeQL CLI CSV output")


# CodeQL CLI CSV output
You can output results from the CodeQL CLI in CSV format to share with other systems.
## Who can use this feature?
CodeQL is available for the following repository types:
  * Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)
  * Organization-owned repositories on GitHub Team with [GitHub Code Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## [About CSV output](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/csv-output#about-csv-output)
You can save analysis results from the CodeQL CLI in a number of different formats, including SARIF and CSV. We do generally recommend SARIF because it is a standard output for static analysis tools and easier to parse. You can also upload SARIF files to GitHub. However, CSV format may be useful if you need to further process the analysis results using your own tools. For more information on selecting a file format for your analysis results, see [database analyze](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-analyze).
For more information about the SARIF format, see [CodeQL CLI SARIF output](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/sarif-output).
If you choose to generate results in CSV format, then each line in the output file corresponds to an alert. Each line is a comma-separated list with the following information.
**Property** | **Description** | **Example**  
---|---|---  
Name | Name of the query that identified the result. | `Inefficient regular expression`  
Description | Description of the query. | `A regular expression that requires exponential time to match certain inputs can be a performance bottleneck, and may be vulnerable to denial-of-service attacks.`  
Severity | Severity of the query. | `error`  
Message | Alert message. | `This part of the regular expression may cause exponential backtracking on strings containing many repetitions of '\\\\'.`  
Path | Path of the file containing the alert. | `/vendor/codemirror/markdown.js`  
Start line | Line of the file where the code that triggered the alert begins. | `617`  
Start column | Column of the start line that marks the start of the alert code. Not included when equal to 1. | `32`  
End line | Line of the file where the code that triggered the alert ends. Not included when the same value as the start line. | `64`  
End column | Where available, the column of the end line that marks the end of the alert code. Otherwise the end line is repeated. | `617`
