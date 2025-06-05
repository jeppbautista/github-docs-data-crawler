  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Build Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions "Build Copilot Extensions")/
  * [Build a Copilot skillset](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-skillset-for-your-copilot-extension "Build a Copilot skillset")/
  * [Build Copilot skillsets](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-skillset-for-your-copilot-extension/building-copilot-skillsets "Build Copilot skillsets")


# Building Copilot skillsets
Learn the steps to build Github Copilot skillsets and integrate custom tools and functions into your Copilot environment.
## In this article
  * [Introduction](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-skillset-for-your-copilot-extension/building-copilot-skillsets#introduction)
  * [Prerequisites](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-skillset-for-your-copilot-extension/building-copilot-skillsets#prerequisites)
  * [Configuration requirements](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-skillset-for-your-copilot-extension/building-copilot-skillsets#configuration-requirements)
  * [Using your skillset](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-skillset-for-your-copilot-extension/building-copilot-skillsets#using-your-skillset)
  * [Setting up a skillset](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-skillset-for-your-copilot-extension/building-copilot-skillsets#setting-up-a-skillset)


## [Introduction](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-skillset-for-your-copilot-extension/building-copilot-skillsets#introduction)
Github Copilot skillsets are a streamlined way to extend GitHub Copilot's functionality by defining API endpoints that Copilot can call. When you create a skillset, Copilot handles all the AI interactions while your endpoints provide the data or functionality. This guide walks you through configuring and deploying a skillset within your GitHub App.
## [Prerequisites](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-skillset-for-your-copilot-extension/building-copilot-skillsets#prerequisites)
Before you begin, make sure you have the following:
  1. **A configured GitHub App:** You’ll need a GitHub App to act as the container for your skillset. If you haven’t already set one up, refer to [Creating a GitHub App for your Copilot Extension](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/creating-a-github-app-for-your-copilot-extension) and [Configuring your GitHub App for your Copilot extension](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/configuring-your-github-app-for-your-copilot-extension).
  2. **API endpoints:** You need one endpoint per skill. Each endpoint must: 
     * Accept POST requests with the `application/json` MIME type
     * Be able to verify the signature of requests from GitHub to authenticate their origin and prevent unauthorized access
     * Be publicly accessible via HTTPS


For more information about signature verification, see [Verifying that payloads are coming from GitHub](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension/configuring-your-copilot-agent-to-communicate-with-github#verifying-that-payloads-are-coming-from-github).
## [Configuration requirements](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-skillset-for-your-copilot-extension/building-copilot-skillsets#configuration-requirements)
Each skillset is defined within a GitHub App. A single GitHub App can contain up to five skills. Each individual skill needs:
  * **Name:** A clear and descriptive name (for example, "Get Issues").
  * **Inference description:** A detailed explanation of what the skill does and when to use it (for example, "Searches for external issues matching specific criteria like status and labels").
  * **API endpoint:** A POST endpoint that accepts JSON requests.
  * **JSON schema:** The structure of data your endpoint expects.


### [Example JSON schema](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-skillset-for-your-copilot-extension/building-copilot-skillsets#example-json-schema)
This example demonstrates a skill that requires two parameters: a status string and a label string. If no parameters are provided, an empty object with the type 'object' must be passed in as the request body.
```
{
 "type": "object",
 "properties": {
   "status": {
     "type": "string",
     "description": "filter issues by status (open, closed)",
     "enum": ["open", "closed"]
   },
   "label": {
     "type": "string",
     "description": "filter issues by label"
   }
 }
}

```

This format lets users make natural-language requests like `find open security issues` and Copilot will structure the appropriate API call.
## [Using your skillset](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-skillset-for-your-copilot-extension/building-copilot-skillsets#using-your-skillset)
To use your skillset:
  1. Type `@` followed by your extension's name.
  2. Type your prompt in natural language.
For example:
     * `@skillset-example generate a lorem ipsum`
     * `@skillset-example give me sample data with 100 words`


Copilot interprets your request and calls the appropriate skill with the right parameters. There's no need to specify which skill to use—Copilot determines this from your natural-language request and the inference descriptions provided.
## [Setting up a skillset](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-skillset-for-your-copilot-extension/building-copilot-skillsets#setting-up-a-skillset)
  1. In the upper-right corner of any page on GitHub, click your profile photo.
  2. Navigate to your account settings. 
     * For an app owned by a personal account, click **Settings**.
     * For an app owned by an organization: 
       1. Click **Your organizations**.
       2. To the right of the organization, click **Settings**.
  3. In the left sidebar, click 
  4. In the left sidebar, click **GitHub Apps**.
  5. In the list of GitHub Apps, click the GitHub App you want to configure for your skillset.
  6. In the navigation menu on the left, select **Copilot**.
  7. Under **App Type** , select **Skillset** from the dropdown menu.
  8. Optionally, in the **Pre-authorization URL** field, enter the URL where users will be redirected to start the authentication process. This step is necessary if your API requires users to connect their GitHub account to access certain features or data.
  9. For each skill you want to add (maximum 5): 
    1. Click **Add new skill**.
    2. Enter a clear **Name** for the skill (e.g., "Generate Lorem Ipsum Data").
    3. Write a detailed **Inference description** to help Copilot understand when to use this skill.
    4. Add your **API endpoint URL** that will receive the POST requests.
    5. In the **Parameter** field, add the JSON schema defining the expected request format.
    6. Click **Add Definition** to save your skill.
  10. Click **Save** to save your skillset.


