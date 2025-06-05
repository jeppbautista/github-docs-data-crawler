  * [Codespaces](https://docs.github.com/en/codespaces "Codespaces")/
  * [Managing your organization](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization "Managing your organization")/
  * [List organization codespaces](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/listing-the-codespaces-in-your-organization "List organization codespaces")


# Listing the codespaces in your organization
You can list all of the currently active or stopped codespaces for your organization.
## Who can use this feature?
To list all of the current codespaces for your organization, you must be an organization owner.
Organizations on GitHub Team and GitHub Enterprise plans can pay for members' and collaborators' use of GitHub Codespaces. These organizations can then access settings and policies to manage codespaces paid for by the organization. For more information, see [Choosing who owns and pays for codespaces in your organization](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/choosing-who-owns-and-pays-for-codespaces-in-your-organization#about-ownership-of-codespaces) and [GitHub’s plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans).
## [Overview](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/listing-the-codespaces-in-your-organization#overview)
As an organization owner, you can list all of the currently active and stopped codespaces for your organization. You might want to do this to check how many codespaces users are creating, to make sure they aren't incurring unnecessary costs. For information about pricing, see [About billing for GitHub Codespaces](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-codespaces/about-billing-for-github-codespaces).
The easiest way to list the codespaces for an organization is by using GitHub CLI. You can also use the REST API, which provides more information about each codespace.
For information on how to see the current total Codespaces usage for your organization or enterprise, and generate a detailed report, see [Viewing your GitHub Codespaces usage](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-codespaces/viewing-your-github-codespaces-usage).
### [Using GitHub CLI to list codespaces](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/listing-the-codespaces-in-your-organization#using-github-cli-to-list-codespaces)
To list all of the current codespaces for a specified organization, use the following command.
Shell```
gh codespace list --org ORGANIZATION

```
```
gh codespace list --org ORGANIZATION

```

This command returns a list that includes the following information for each codespace:
  * The name and display name
  * The user who created the codespace
  * The repository and branch
  * The current state of the codespace


To list all of the current codespaces for an organization that were created by a specific user, use the following command.
Shell```
gh codespace list --org ORGANIZATION --user USER

```
```
gh codespace list --org ORGANIZATION --user USER

```

In the above commands, replace `ORGANIZATION` with the name of the organization you are querying. You must be an owner of the organization.
### [Using the REST API to list codespaces](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/listing-the-codespaces-in-your-organization#using-the-rest-api-to-list-codespaces)
You can use the `/orgs/{org}/codespaces` API endpoint as an alternative method of listing the current codespaces for an organization. This returns more information than GitHub CLI; for example, the machine type details.
For more information about this endpoint, see [REST API endpoints for Codespaces organizations](https://docs.github.com/en/rest/codespaces/organizations#list-codespaces-for-the-organization).
