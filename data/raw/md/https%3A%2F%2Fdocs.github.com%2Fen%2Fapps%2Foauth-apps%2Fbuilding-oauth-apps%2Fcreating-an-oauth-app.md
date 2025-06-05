  * [Apps](https://docs.github.com/en/apps "Apps")/
  * [OAuth apps](https://docs.github.com/en/apps/oauth-apps "OAuth apps")/
  * [Building OAuth apps](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps "Building OAuth apps")/
  * [Creating an OAuth app](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app "Creating an OAuth app")


# Creating an OAuth app
You can create and register an OAuth app under your personal account or under any organization you have administrative access to. While creating your OAuth app, remember to protect your privacy by only using information you consider public.
Consider building a GitHub App instead of an OAuth app.
Both OAuth apps and GitHub Apps use OAuth 2.0.
OAuth apps can only act on behalf of a user while GitHub Apps can either act on behalf of a user or independently of a user.
GitHub Apps use fine-grained permissions, give the user more control over which repositories the app can access, and use short-lived tokens.
For more information, see [Differences between GitHub Apps and OAuth apps](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/differences-between-github-apps-and-oauth-apps) and [About creating GitHub Apps](https://docs.github.com/en/apps/creating-github-apps/setting-up-a-github-app/about-creating-github-apps).
A user or organization can own up to 100 OAuth apps.
  1. In the upper-right corner of any page on GitHub, click your profile photo, then click 
  2. In the left sidebar, click 
  3. In the left sidebar, click **OAuth apps**.
  4. Click **New OAuth App**.
If you haven't created an app before, this button will say, **Register a new application**.
  5. In "Application name", type the name of your app.
Only use information in your OAuth app that you consider public. Avoid using sensitive data, such as internal URLs, when creating an OAuth app.
  6. In "Homepage URL", type the full URL to your app's website.
  7. Optionally, in "Application description", type a description of your app that users will see.
  8. In "Authorization callback URL", type the callback URL of your app.
OAuth apps cannot have multiple callback URLs, unlike GitHub Apps.
  9. If your OAuth app will use the device flow to identify and authorize users, click **Enable Device Flow**. For more information about the device flow, see [Authorizing OAuth apps](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps#device-flow).
  10. Click **Register application**.


## [Further reading](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app#further-reading)
  * [Modifying an OAuth app](https://docs.github.com/en/apps/oauth-apps/maintaining-oauth-apps/modifying-an-oauth-app)


