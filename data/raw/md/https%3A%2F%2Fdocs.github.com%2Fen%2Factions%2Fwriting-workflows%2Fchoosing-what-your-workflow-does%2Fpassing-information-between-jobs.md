  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Write workflows](https://docs.github.com/en/actions/writing-workflows "Write workflows")/
  * [Choose what workflows do](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does "Choose what workflows do")/
  * [Pass information](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/passing-information-between-jobs "Pass information")


# Passing information between jobs
You can define outputs to pass information from one job to another.
## [Overview](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/passing-information-between-jobs#overview)
You can use `jobs.<job_id>.outputs` to create a `map` of outputs for a job. Job outputs are available to all downstream jobs that depend on this job. For more information on defining job dependencies, see [`jobs.<job_id>.needs`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idneeds).
Outputs can be a maximum of 1 MB per job. The total of all outputs in a workflow run can be a maximum of 50 MB. Size is approximated based on UTF-16 encoding.
Job outputs containing expressions are evaluated on the runner at the end of each job. Outputs containing secrets are redacted on the runner and not sent to GitHub Actions.
If an output is skipped because it may contain a secret, you will see the following warning message: "Skip output `{output.Key}` since it may contain secret." For more information on how to handle secrets, please refer to the [Example: Masking and passing a secret between jobs or workflows](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/workflow-commands-for-github-actions#example-masking-and-passing-a-secret-between-jobs-or-workflows).
To use job outputs in a dependent job, you can use the `needs` context. For more information, see [Accessing contextual information about workflow runs](https://docs.github.com/en/actions/learn-github-actions/contexts#needs-context).
### [Example: Defining outputs for a job](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/passing-information-between-jobs#example-defining-outputs-for-a-job)
```
jobs:
  job1:
    runs-on: ubuntu-latest
    # Map a step output to a job output
    outputs:
      output1: ${{ steps.step1.outputs.test }}
      output2: ${{ steps.step2.outputs.test }}
    steps:
      - id: step1
        run: echo "test=hello" >> "$GITHUB_OUTPUT"
      - id: step2
        run: echo "test=world" >> "$GITHUB_OUTPUT"
  job2:
    runs-on: ubuntu-latest
    needs: job1
    steps:
      - env:
          OUTPUT1: ${{needs.job1.outputs.output1}}
          OUTPUT2: ${{needs.job1.outputs.output2}}
        run: echo "$OUTPUT1 $OUTPUT2"

```

### [Using Job Outputs in a Matrix Job](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/passing-information-between-jobs#using-job-outputs-in-a-matrix-job)
Matrices can be used to generate multiple outputs of different names. When using a matrix, job outputs will be combined from all jobs inside the matrix.
```
jobs:
  job1:
    runs-on: ubuntu-latest
    outputs:
      output_1: ${{ steps.gen_output.outputs.output_1 }}
      output_2: ${{ steps.gen_output.outputs.output_2 }}
      output_3: ${{ steps.gen_output.outputs.output_3 }}
    strategy:
      matrix:
        version: [1, 2, 3]
    steps:
      - name: Generate output
        id: gen_output
        run: |
          version="${{ matrix.version }}"
          echo "output_${version}=${version}" >> "$GITHUB_OUTPUT"
  job2:
    runs-on: ubuntu-latest
    needs: [job1]
    steps:
      # Will show
      # {
      #   "output_1": "1",
      #   "output_2": "2",
      #   "output_3": "3"
      # }
      - run: echo '${{ toJSON(needs.job1.outputs) }}'

```

Actions does not guarantee the order that matrix jobs will run in. Ensure that the output name is unique, otherwise the last matrix job that runs will override the output value.
