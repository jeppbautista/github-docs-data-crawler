  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners "Self-hosted runners")/
  * [Manage self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners "Manage self-hosted runners")/
  * [Self-hosted runner communication](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/communicating-with-self-hosted-runners "Self-hosted runner communication")


# Communicating with self-hosted runners
Your self-hosted runners can communicate with GitHub
A self-hosted runner connects to GitHub to receive job assignments and to download new versions of the runner application. The self-hosted runner uses an HTTPS long poll that opens a connection to GitHub for 50 seconds, and if no response is received, it then times out and creates a new long poll. The application must be running on the machine to accept and run GitHub Actions jobs.
The GitHub Actions runner application is open source. You can contribute and file issues in the [runner](https://github.com/actions/runner) repository. When a new version is released, the runner application automatically updates itself when a job is assigned to the runner, or within a week of release if the runner hasn't been assigned any jobs.
A self-hosted runner is automatically removed from GitHub if it has not connected to GitHub Actions for more than 14 days. An ephemeral self-hosted runner is automatically removed from GitHub if it has not connected to GitHub Actions for more than 1 day.
The connection between self-hosted runners and GitHub is over HTTPS (port 443).
Since the self-hosted runner opens a connection to GitHub, you do not need to allow GitHub to make inbound connections to your self-hosted runner.
You must ensure that the machine has the appropriate network access with at least 70 kilobits per second upload and download speed to communicate with the GitHub hosts listed below. Some hosts are required for essential runner operations, while other hosts are only required for certain functionality.
You can use the REST API to get meta information about GitHub, including the IP addresses and domain details for GitHub services. The `actions_inbound` section of the API supports both fully qualified and wildcard domains. Fully qualified domains specify a complete domain name (e.g., `example.github.com`), while wildcard domains use a `*` to represent multiple possible subdomains (e.g., `*.github.com`). An example of the self-hosted runner requirements using wildcard domains has been listed below. For more information, see [REST API endpoints for meta data](https://docs.github.com/en/rest/meta/meta).
Shell```
github.com
*.github.com
*.githubusercontent.com
ghcr.io

```
```
github.com
*.github.com
*.githubusercontent.com
ghcr.io

```

Some of the domains listed are configured using `CNAME` records. Some firewalls might require you to add rules recursively for all `CNAME` records. Note that the `CNAME` records might change in the future, and that only the domains listed will remain constant.
**Needed for essential operations:**
Shell```
github.com
api.github.com
*.actions.githubusercontent.com

```
```
github.com
api.github.com
*.actions.githubusercontent.com

```

**Needed for downloading actions:**
Shell```
codeload.github.com
pkg.actions.githubusercontent.com

```
```
codeload.github.com
pkg.actions.githubusercontent.com

```

**Needed for publishing immutable actions:**
Shell```
ghcr.io

```
```
ghcr.io

```

**Needed for uploading/downloading job summaries, logs, workflow artifacts, and caches:**
Shell```
results-receiver.actions.githubusercontent.com
*.blob.core.windows.net

```
```
results-receiver.actions.githubusercontent.com
*.blob.core.windows.net

```

**Needed for runner version updates:**
Shell```
objects.githubusercontent.com
objects-origin.githubusercontent.com
github-releases.githubusercontent.com
github-registry-files.githubusercontent.com

```
```
objects.githubusercontent.com
objects-origin.githubusercontent.com
github-releases.githubusercontent.com
github-registry-files.githubusercontent.com

```

**Needed for retrieving OIDC tokens:**
Shell```
*.actions.githubusercontent.com

```
```
*.actions.githubusercontent.com

```

**Needed for downloading or publishing packages or containers to GitHub Packages:**
Shell```
*.pkg.github.com
pkg-containers.githubusercontent.com
ghcr.io

```
```
*.pkg.github.com
pkg-containers.githubusercontent.com
ghcr.io

```

**Needed for Git Large File Storage**
Shell```
github-cloud.githubusercontent.com
github-cloud.s3.amazonaws.com

```
```
github-cloud.githubusercontent.com
github-cloud.s3.amazonaws.com

```

**Needed for jobs for Dependabot updates**
Shell```
dependabot-actions.githubapp.com

```
```
dependabot-actions.githubapp.com

```

In addition, your workflow may require access to other network resources.
If you use an IP address allow list for your GitHub organization or enterprise account, you must add your self-hosted runner's IP address to the allow list. See [Managing allowed IP addresses for your organization](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-allowed-ip-addresses-for-your-organization#using-github-actions-with-an-ip-allow-list) or [Enforcing policies for security settings in your enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-security-settings-in-your-enterprise) in the GitHub Enterprise Cloud documentation.
## [Further reading](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/communicating-with-self-hosted-runners#further-reading)
  * [Using a proxy server with self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/using-a-proxy-server-with-self-hosted-runners)
  * [Monitoring and troubleshooting self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/monitoring-and-troubleshooting-self-hosted-runners#troubleshooting-network-connectivity)


