  * [Apps](https://docs.github.com/en/apps "Apps")/
  * [Creating GitHub Apps](https://docs.github.com/en/apps/creating-github-apps "Creating GitHub Apps")/
  * [Authenticate with a GitHub App](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app "Authenticate with a GitHub App")/
  * [Authenticate as an app](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app "Authenticate as an app")


# Authenticating as a GitHub App
You can authenticate as a GitHub App in order to generate an installation access token or manage your app.
## In this article
  * [About authentication as a GitHub App](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app#about-authentication-as-a-github-app)
  * [Using a JSON Web Token (JWT) to authenticate as a GitHub App](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app#using-a-json-web-token-jwt-to-authenticate-as-a-github-app)
  * [Using the Octokit.js SDK to authenticate as a GitHub App](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app#using-the-octokitjs-sdk-to-authenticate-as-a-github-app)


## [About authentication as a GitHub App](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app#about-authentication-as-a-github-app)
You must authenticate as a GitHub App in order to make REST API requests as the application. For example, if you want to use the API to generate an installation access token for accessing organization resources, list installations across organizations for your app, or suspend an app installation, you must authenticate as an app.
If a REST API endpoint requires you to authenticate as an app, the documentation for that endpoint will indicate that you must use a JWT to access the endpoint. The GraphQL API does not support any queries or mutations that require you to authenticate as an app.
## [Using a JSON Web Token (JWT) to authenticate as a GitHub App](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app#using-a-json-web-token-jwt-to-authenticate-as-a-github-app)
  1. Generate a JSON Web Token (JWT) for your app. For more information, see [Generating a JSON Web Token (JWT) for a GitHub App](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-json-web-token-jwt-for-a-github-app).
  2. Include the JWT in the `Authorization` header of your request. In the following example, replace `YOUR_JWT` with your JWT.
```
curl --request GET \
--url "https://api.github.com/app/installations" \
--header "Accept: application/vnd.github+json" \
--header "Authorization: Bearer YOUR_JWT" \
--header "X-GitHub-Api-Version: 2022-11-28"

```



## [Using the Octokit.js SDK to authenticate as a GitHub App](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app#using-the-octokitjs-sdk-to-authenticate-as-a-github-app)
You can use GitHub's Octokit.js SDK to authenticate as a GitHub App. One advantage of using the SDK to authenticate is that you do not need to generate a JSON web token (JWT) yourself. Additionally, the SDK will take care of regenerating the JWT when it expires.
You must install and import `octokit` in order to use the Octokit.js library. The following example uses import statements in accordance with ES6. For more information about different installation and import methods, see [Usage](https://github.com/octokit/octokit.js/#usage) in the octokit/octokit repository.
  1. Get the ID of your app. You can find your app's ID on the settings page for your GitHub App. For more information about navigating to the settings page for your GitHub App, see [Modifying a GitHub App registration](https://docs.github.com/en/apps/maintaining-github-apps/modifying-a-github-app-registration#navigating-to-your-github-app-settings).
  2. Generate a private key. For more information, see [Managing private keys for GitHub Apps](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/managing-private-keys-for-github-apps).
  3. Import `App` from `octokit`.
JavaScript```
import { App } from "octokit";

```
```
import { App } from "octokit";

```

  4. Create a new instance of `App`. In the following example, replace `APP_ID` with a reference to your app's ID. Replace `PRIVATE_KEY` with a reference to the value of your app's private key.
JavaScript```
 const app = new App({
  appId: APP_ID,
  privateKey: PRIVATE_KEY,
});

```
```
 const app = new App({
  appId: APP_ID,
  privateKey: PRIVATE_KEY,
});

```

  5. Use an `octokit` method to make a request to a REST API endpoint that requires a JWT. For example:
JavaScript```
await app.octokit.request("/app")

```
```
await app.octokit.request("/app")

```



