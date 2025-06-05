  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Build Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions "Build Copilot Extensions")/
  * [Use OIDC](https://docs.github.com/en/copilot/building-copilot-extensions/using-oidc-with-github-copilot-extensions "Use OIDC")


# Using OIDC with GitHub Copilot Extensions
Learn how to use OpenID Connect (OIDC) with your Copilot Extension to enhance security.
## In this article
  * [About OpenID Connect (OIDC) for Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions/using-oidc-with-github-copilot-extensions#about-openid-connect-oidc-for-copilot-extensions)
  * [Overview of OIDC](https://docs.github.com/en/copilot/building-copilot-extensions/using-oidc-with-github-copilot-extensions#overview-of-oidc)
  * [Benefits of using OIDC](https://docs.github.com/en/copilot/building-copilot-extensions/using-oidc-with-github-copilot-extensions#benefits-of-using-oidc)
  * [Token exchange flow](https://docs.github.com/en/copilot/building-copilot-extensions/using-oidc-with-github-copilot-extensions#token-exchange-flow)
  * [Understanding OIDC tokens](https://docs.github.com/en/copilot/building-copilot-extensions/using-oidc-with-github-copilot-extensions#understanding-oidc-tokens)
  * [Setting up OIDC for your extension](https://docs.github.com/en/copilot/building-copilot-extensions/using-oidc-with-github-copilot-extensions#setting-up-oidc-for-your-extension)
  * [Troubleshooting](https://docs.github.com/en/copilot/building-copilot-extensions/using-oidc-with-github-copilot-extensions#troubleshooting)


## [About OpenID Connect (OIDC) for Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions/using-oidc-with-github-copilot-extensions#about-openid-connect-oidc-for-copilot-extensions)
OpenID Connect (OIDC) allows Copilot Extensions to exchange short-lived tokens directly from their cloud provider instead of storing long-lived GitHub credentials. This feature enables both Copilot agents and skillsets to more securely authenticate users and access cloud resources.
## [Overview of OIDC](https://docs.github.com/en/copilot/building-copilot-extensions/using-oidc-with-github-copilot-extensions#overview-of-oidc)
Copilot Extensions often need to access third-party resources or APIs on behalf of users. Traditionally, this required storing GitHub tokens as secrets and making additional API calls to map these tokens to user identities in your system. With OIDC, your extension can request short-lived access tokens directly from your authentication service by exchanging GitHub identity information.
When enabled, GitHub's OIDC provider automatically generates a token containing claims about the user and the request context. Your authentication service can validate these claims and exchange them for an access token scoped specifically for your service.
Using OIDC is especially valuable for Copilot skillsets development because it allows you to leverage your existing API endpoints without maintaining separate GitHub-specific endpoints. Instead of duplicating endpoints to accept GitHub tokens, you can use OIDC to translate GitHub identities into your service’s native authentication tokens.
## [Benefits of using OIDC](https://docs.github.com/en/copilot/building-copilot-extensions/using-oidc-with-github-copilot-extensions#benefits-of-using-oidc)
By implementing OIDC token exchange in your Copilot Extension, you can:
  * Avoid storing long-lived GitHub tokens or maintain a mapping between GitHub and your service's identities.
  * Use short-lived tokens that automatically expire and can be scoped specifically to your service's needs.
  * Avoid making additional calls to GitHub's API to validate tokens and fetch user information.
  * Enable direct integration for Copilot Skills with your existing APIs without maintaining separate endpoints for GitHub.
  * Reuse existing API endpoints by translating GitHub authentication into your service's native tokens.


## [Token exchange flow](https://docs.github.com/en/copilot/building-copilot-extensions/using-oidc-with-github-copilot-extensions#token-exchange-flow)
The following outlines how the Copilot Extensibility Platform exchanges an OIDC token for an access token to authenticate requests to your extension.
### [Initial request](https://docs.github.com/en/copilot/building-copilot-extensions/using-oidc-with-github-copilot-extensions#initial-request)
  1. The user sends a message to your Copilot Extension.
  2. GitHub generates an OIDC token containing user identity information.
  3. GitHub calls your token exchange endpoint with the OIDC token.
  4. Your service validates the token and returns an access token.
  5. GitHub includes your access token in the request to your extension.

```
# HTTP header
Authorization: Bearer <your-service-token>
X-GitHub-Token: <github-token>

```

### [Subsequent requests](https://docs.github.com/en/copilot/building-copilot-extensions/using-oidc-with-github-copilot-extensions#subsequent-requests)
  1. GitHub caches your access token for up to 10 minutes.
  2. The cached token is reused for subsequent requests.
  3. If the token expires or becomes invalid, GitHub requests a new one.


## [Understanding OIDC tokens](https://docs.github.com/en/copilot/building-copilot-extensions/using-oidc-with-github-copilot-extensions#understanding-oidc-tokens)
The OIDC token from GitHub is a JWT containing claims about the user and request context:
```
{
  "jti": "<unique-token-id>",
  "sub": "<github-user-id>",
  "aud": "<your-client-id>",
  "iss": "https://github.com/login/oauth",
  "nbf": 1632492967,
  "exp": 1632493867,
  "iat": 1632493567,
  "act": {
    "sub": "api.copilotchat.com"
  }
}

```

## [Setting up OIDC for your extension](https://docs.github.com/en/copilot/building-copilot-extensions/using-oidc-with-github-copilot-extensions#setting-up-oidc-for-your-extension)
There are three steps to setting up OIDC for your extension.
  1. [Configure your token exchange endpoint](https://docs.github.com/en/copilot/building-copilot-extensions/using-oidc-with-github-copilot-extensions#configure-your-token-exchange-endpoint).
  2. [Enable OIDC in your Copilot extensions settings](https://docs.github.com/en/copilot/building-copilot-extensions/using-oidc-with-github-copilot-extensions#enable-oidc-in-your-copilot-extensions-settings).
  3. [Validate OIDC tokens](https://docs.github.com/en/copilot/building-copilot-extensions/using-oidc-with-github-copilot-extensions#validate-oidc-tokens).


### [Configure your token exchange endpoint](https://docs.github.com/en/copilot/building-copilot-extensions/using-oidc-with-github-copilot-extensions#configure-your-token-exchange-endpoint)
Create an endpoint in your service that conforms to the [RFC 8693 OAuth 2.0 Token Exchange](https://www.rfc-editor.org/rfc/rfc8693.html). This endpoint should:
  * Accept `POST` requests with the following form-encoded parameters:
```
grant_type=urn:ietf:params:oauth:grant-type:token-exchange
&resource=<https://your-service.com/resource>
&subject_token=<github-jwt-token>
&subject_token_type=urn:ietf:params:oauth:token-type:id_token

```

  * Return a JSON response with your service's access token:
```
{
  "access_token": <"your-service-token">,
  "issued_token_type":"urn:ietf:params:oauth:token-type:access_token",
  "token_type": "Bearer",
  "expires_in": 3600
}

```

  * Return an error response when validation fails:
```
{
  "error": "invalid_request"
}

```



### [Enable OIDC in your Copilot Extension's settings](https://docs.github.com/en/copilot/building-copilot-extensions/using-oidc-with-github-copilot-extensions#enable-oidc-in-your-copilot-extensions-settings)
In your Copilot Extension's configuration, enable OIDC:
  1. In the upper-right corner of any page on GitHub, click your profile photo.
  2. Navigate to your account settings.
     * For an app owned by a personal account, click **Settings**.
     * For an app owned by an organization: 
       1. Click **Your organizations**.
       2. To the right of the organization, click **Settings**.
  3. In the left sidebar, click 
  4. In the left sidebar, click **GitHub Apps**.
  5. To the right of the GitHub App you want to configure for your Copilot Extension, click **Edit**.
  6. In the left sidebar, click **Copilot**.
  7. Under **OpenID Connect Token Exchange** , check **Enabled**.
  8. In the **Token exchange endpoint** field, input your token exchange URL.
  9. In the **Request header key** field, input the header key for your service's token. The default is `Authorization`.
  10. In the **Request header value** field, input the header value format. The default is `Bearer ${token}`.


### [Validate OIDC tokens](https://docs.github.com/en/copilot/building-copilot-extensions/using-oidc-with-github-copilot-extensions#validate-oidc-tokens)
Your token exchange endpoint should validate the GitHub OIDC token by following the steps below:
  1. Fetch the JSON Web Key Set (JWKS) from <https://github.com/login/oauth/.well-known/openid-configuration>.
  2. Verify the token signature.
  3. Validate required claims. 
     * `aud`: Audience. Your Copilot Extension's client ID.
     * `sub`: Subject. The GitHub user ID making the request. The response is limited to data that the user has permissions to access. If the user has no permissions `400 Bad Request` is shown.
     * `iat`: Issued At. The timestamp when the token was issued. It is typically a timestamp in the past but represents the exact moment the token was created.
     * `nbf`: Not Before. The timestamp before which the token is not valid. This should be a timestamp in the past.
     * `exp`: Expiration Time. The timestamp when the token expires. This should be a timestamp in the future.
     * `act`: Actor. The acting entity in delegated access. This should be a constant string.


## [Troubleshooting](https://docs.github.com/en/copilot/building-copilot-extensions/using-oidc-with-github-copilot-extensions#troubleshooting)
The following sections outline common problems and best practices for implementing OIDC for your Copilot Extension.
### [Token validation errors](https://docs.github.com/en/copilot/building-copilot-extensions/using-oidc-with-github-copilot-extensions#token-validation-errors)
  * Ensure you're using the correct JWKS endpoint.
  * Verify that all the required claims are present and valid.
  * Check that timestamps (`iat`, `nbf`, and `exp`) are within valid ranges.


### [Token exchange failures](https://docs.github.com/en/copilot/building-copilot-extensions/using-oidc-with-github-copilot-extensions#token-exchange-failures)
  * Return `HTTP 400` for invalid tokens.
  * Return `HTTP 403` if the user lacks the necessary permissions.
  * If GitHub receives a 403 response, it will retry the request with a new token.


### [Performance issues](https://docs.github.com/en/copilot/building-copilot-extensions/using-oidc-with-github-copilot-extensions#performance-issues)
  * Implement efficient token validation to minimize latency.
  * Use appropriate token expiration times (recommended: 10 minutes or less).
  * Consider caching implications for high-traffic extensions.


### [Best practices](https://docs.github.com/en/copilot/building-copilot-extensions/using-oidc-with-github-copilot-extensions#best-practices)
  * Scope tokens to the minimum required permissions.
  * Implement proper error handling and logging.
  * Monitor token exchange patterns for security anomalies.
  * Keep tokens short-lived to minimize security risks.
  * Validate all claims before issuing access tokens.
  * Consider implementing rate limiting on your token exchange endpoint.
  * Use HTTPS for all token exchange communications.


