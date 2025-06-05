  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Code scanning](https://docs.github.com/en/code-security/code-scanning "Code scanning")/
  * [Troubleshooting code scanning](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning "Troubleshooting code scanning")/
  * [Unnecessary step found](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/unnecessary-step-found "Unnecessary step found")


# Warning: "1 issue was detected with this workflow: git checkout HEAD^2 is no longer necessary"
If you see this warning, you should update your workflow to follow current best practice.
## In this article
  * [About this warning](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/unnecessary-step-found#about-this-warning)
  * [Confirm the cause of the problem](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/unnecessary-step-found#confirm-the-cause-of-the-problem)
  * [Fixing the problem](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/unnecessary-step-found#fixing-the-problem)


## [About this warning](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/unnecessary-step-found#about-this-warning)
```
Warning: 1 issue was detected with this workflow: git checkout HEAD^2 is no longer
necessary. Please remove this step as Code Scanning recommends analyzing the merge
commit for best results.

```

If you're using an old CodeQL workflow you may receive this warning from the "Initialize CodeQL" action.
## [Confirm the cause of the problem](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/unnecessary-step-found#confirm-the-cause-of-the-problem)
Check for the following lines from the CodeQL workflow. These lines were included in the `steps` section of the `Analyze` job in initial versions of the CodeQL workflow.
```
        with:
          # We must fetch at least the immediate parents so that if this is
          # a pull request then we can checkout the head.
          fetch-depth: 2

      # If this run was triggered by a pull request event, then checkout
      # the head of the pull request instead of the merge commit.
      - run: git checkout HEAD^2
        if: ${{ github.event_name == 'pull_request' }}

```

## [Fixing the problem](https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/unnecessary-step-found#fixing-the-problem)
Remove the lines from the CodeQL workflow. The revised `steps` section of the workflow should now look like this:
```
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      # Initializes the CodeQL tools for scanning.
      - name: Initialize CodeQL
        uses: github/codeql-action/init@v3

      # ...

```

For more information about editing the CodeQL workflow file, see [Customizing your advanced setup for code scanning](https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/customizing-your-advanced-setup-for-code-scanning#editing-a-code-scanning-workflow).
