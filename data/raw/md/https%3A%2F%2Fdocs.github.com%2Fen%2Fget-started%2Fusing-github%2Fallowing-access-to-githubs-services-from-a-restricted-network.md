  * [Get started](https://docs.github.com/en/get-started "Get started")/
  * [Using GitHub](https://docs.github.com/en/get-started/using-github "Using GitHub")/
  * [Allow network access](https://docs.github.com/en/get-started/using-github/allowing-access-to-githubs-services-from-a-restricted-network "Allow network access")


# Allowing access to GitHub's services from a restricted network
If your network restricts access to specific domains, a network administrator may be able to grant access to GitHub's services by creating exceptions for GitHub's domain names.
## In this article
  * [About access to GitHub from a restricted network](https://docs.github.com/en/get-started/using-github/allowing-access-to-githubs-services-from-a-restricted-network#about-access-to-github-from-a-restricted-network)
  * [Retrieving GitHub's domain names using the REST API](https://docs.github.com/en/get-started/using-github/allowing-access-to-githubs-services-from-a-restricted-network#retrieving-githubs-domain-names-using-the-rest-api)


## [About access to GitHub from a restricted network](https://docs.github.com/en/get-started/using-github/allowing-access-to-githubs-services-from-a-restricted-network#about-access-to-github-from-a-restricted-network)
In rare cases, an institution's network access policy may restrict access to specific domain names for end users. For example, the policy may use DNS filtering to deny access to sites like GitHub. If your institution requires this level of control, but you still want to permit access to services on GitHub, you can create exceptions in your policy to allow access to the necessary domains.
## [Retrieving GitHub's domain names using the REST API](https://docs.github.com/en/get-started/using-github/allowing-access-to-githubs-services-from-a-restricted-network#retrieving-githubs-domain-names-using-the-rest-api)
You can use the REST API to retrieve a list of GitHub's domain names.
The list of domains from the REST API is not intended to be comprehensive. If you block access to services using DNS, but selectively allow access to GitHub's domain names, any or all of GitHub and related services may not function properly or at all for your end users.
For more information, see [REST API endpoints for meta data](https://docs.github.com/en/rest/meta).
