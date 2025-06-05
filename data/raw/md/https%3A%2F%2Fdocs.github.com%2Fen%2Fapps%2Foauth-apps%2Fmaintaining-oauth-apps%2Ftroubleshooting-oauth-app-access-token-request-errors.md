  * [Apps](https://docs.github.com/en/apps "Apps")/
  * [OAuth apps](https://docs.github.com/en/apps/oauth-apps "OAuth apps")/
  * [Maintaining OAuth apps](https://docs.github.com/en/apps/oauth-apps/maintaining-oauth-apps "Maintaining OAuth apps")/
  * [Troubleshoot token request](https://docs.github.com/en/apps/oauth-apps/maintaining-oauth-apps/troubleshooting-oauth-app-access-token-request-errors "Troubleshoot token request")


# Troubleshooting OAuth app access token request errors
When exchanging a code for an access token, there are an additional set of errors that can occur. The format of these responses is determined by the accept header you pass.
## In this article
  * [Incorrect client credentials](https://docs.github.com/en/apps/oauth-apps/maintaining-oauth-apps/troubleshooting-oauth-app-access-token-request-errors#incorrect-client-credentials)
  * [Redirect URI mismatch](https://docs.github.com/en/apps/oauth-apps/maintaining-oauth-apps/troubleshooting-oauth-app-access-token-request-errors#redirect-uri-mismatch)
  * [Bad verification code](https://docs.github.com/en/apps/oauth-apps/maintaining-oauth-apps/troubleshooting-oauth-app-access-token-request-errors#bad-verification-code)
  * [Unverified user email](https://docs.github.com/en/apps/oauth-apps/maintaining-oauth-apps/troubleshooting-oauth-app-access-token-request-errors#unverified-user-email)


These examples only show JSON responses.
## [Incorrect client credentials](https://docs.github.com/en/apps/oauth-apps/maintaining-oauth-apps/troubleshooting-oauth-app-access-token-request-errors#incorrect-client-credentials)
If the client_id and or client_secret you pass are incorrect you will receive this error response.
```
{
  "error": "incorrect_client_credentials",
  "error_description": "The client_id and/or client_secret passed are incorrect.",
  "error_uri": "/apps/managing-oauth-apps/troubleshooting-oauth-app-access-token-request-errors/#incorrect-client-credentials"
}

```

To solve this error, make sure you have the correct credentials for your OAuth app. Double check the `client_id` and `client_secret` to make sure they are correct and being passed correctly to GitHub.
## [Redirect URI mismatch](https://docs.github.com/en/apps/oauth-apps/maintaining-oauth-apps/troubleshooting-oauth-app-access-token-request-errors#redirect-uri-mismatch)
If you provide a `redirect_uri` that doesn't match what you've registered with your OAuth app, you'll receive this error message:
```
{
  "error": "redirect_uri_mismatch",
  "error_description": "The redirect_uri MUST match the registered callback URL for this application.",
  "error_uri": "/apps/managing-oauth-apps/troubleshooting-authorization-request-errors/#redirect-uri-mismatch2"
}

```

To correct this error, either provide a `redirect_uri` that matches what you registered or leave out this parameter to use the default one registered with your application.
## [Bad verification code](https://docs.github.com/en/apps/oauth-apps/maintaining-oauth-apps/troubleshooting-oauth-app-access-token-request-errors#bad-verification-code)
If the verification code you pass is incorrect, expired, or doesn't match what you received in the first request for authorization you will receive this error.
```
{
  "error": "bad_verification_code",
  "error_description": "The code passed is incorrect or expired.",
  "error_uri": "/apps/managing-oauth-apps/troubleshooting-oauth-app-access-token-request-errors/#bad-verification-code"
}

```

To solve this error, start the [OAuth authorization process again](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps) and get a new code.
## [Unverified user email](https://docs.github.com/en/apps/oauth-apps/maintaining-oauth-apps/troubleshooting-oauth-app-access-token-request-errors#unverified-user-email)
If the user for whom you are trying to generate a user access token has not verified their primary email address with GitHub, you will receive this error.
```
{
  "error": "unverified_user_email",
  "error_description": "The user must have a verified primary email.",
  "error_uri": "/apps/managing-oauth-apps/troubleshooting-oauth-app-access-token-request-errors/#unverified_user_email"
}

```

To resolve this error, prompt the user to verify the primary email address on their GitHub account. For more information, see [Verifying your email address](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/verifying-your-email-address).
