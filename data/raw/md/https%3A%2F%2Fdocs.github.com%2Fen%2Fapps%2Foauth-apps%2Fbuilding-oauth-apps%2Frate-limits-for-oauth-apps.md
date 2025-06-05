  * [Apps](https://docs.github.com/en/apps "Apps")/
  * [OAuth apps](https://docs.github.com/en/apps/oauth-apps "OAuth apps")/
  * [Building OAuth apps](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps "Building OAuth apps")/
  * [Rate limits](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/rate-limits-for-oauth-apps "Rate limits")


# Rate limits for OAuth apps
Rate limits restrict the rate of traffic to GitHub.com, to help ensure consistent access for all users.
## In this article
  * [About rate limits for OAuth apps](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/rate-limits-for-oauth-apps#about-rate-limits-for-oauth-apps)
  * [Rate limits for signing in users](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/rate-limits-for-oauth-apps#rate-limits-for-signing-in-users)
  * [Rate limits for the API](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/rate-limits-for-oauth-apps#rate-limits-for-the-api)
  * [Further reading](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/rate-limits-for-oauth-apps#further-reading)


Consider building a GitHub App instead of an OAuth app. The rate limit for GitHub Apps using an installation access token scales with the number of repositories and number of organization users. Conversely, OAuth apps have lower rate limits and do not scale. For more information, see [Differences between GitHub Apps and OAuth apps](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/differences-between-github-apps-and-oauth-apps) and [About creating GitHub Apps](https://docs.github.com/en/apps/creating-github-apps/setting-up-a-github-app/about-creating-github-apps).
## [About rate limits for OAuth apps](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/rate-limits-for-oauth-apps#about-rate-limits-for-oauth-apps)
OAuth apps act on behalf of a user, by making requests with a user access token after the user authorizes the app. For more information, see [Authorizing OAuth apps](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps).
The generation of these user access tokens is subject to a rate limit. Additionally, API requests made with these user access tokens are subject to rate limits.
## [Rate limits for signing in users](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/rate-limits-for-oauth-apps#rate-limits-for-signing-in-users)
OAuth apps should always cache their tokens, and only rarely need to sign in a user. Repeatedly signing in a user can indicate a bug, most frequently seen as an infinite loop between the app and GitHub. If an app signs the user in ten times within one hour, the next sign in within the same hour will require re-authorization of the application. This ensures the user is aware that the app is minting so many tokens, and provides a break in what may be an infinite loop otherwise. This ten _sign in_ rate limit is distinct from the ten _token_ limit also enforced for OAuth apps. For information about the ten token limit, see [Authorizing OAuth apps](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps#creating-multiple-tokens-for-oauth-apps).
## [Rate limits for the API](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/rate-limits-for-oauth-apps#rate-limits-for-the-api)
GitHub sets a limit on the number of requests a OAuth app can make to the REST API within a specific time period. It also sets a limit on the point value of queries that a OAuth app can make to the GraphQL API within a specific time period. In addition to these primary rate limits, GitHub may also apply secondary rate limits. These limits help to prevent abuse and denial-of-service attacks, and ensure that the system remains available for all users.
For more information, see [Rate limits for the REST API](https://docs.github.com/en/rest/overview/rate-limits-for-the-rest-api) and [Rate limits and node limits for the GraphQL API](https://docs.github.com/en/graphql/overview/resource-limitations).
## [Further reading](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/rate-limits-for-oauth-apps#further-reading)
  * [Rate limits for the REST API](https://docs.github.com/en/rest/overview/rate-limits-for-the-rest-api)
  * [Rate limits and node limits for the GraphQL API](https://docs.github.com/en/graphql/overview/resource-limitations)
  * [Rate limits for GitHub Apps](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/rate-limits-for-github-apps)


