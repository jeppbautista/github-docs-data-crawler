  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secret scanning](https://docs.github.com/en/code-security/secret-scanning "Secret scanning")/
  * [Work with secret scanning](https://docs.github.com/en/code-security/secret-scanning/working-with-secret-scanning-and-push-protection "Work with secret scanning")/
  * [Push protection from the REST API](https://docs.github.com/en/code-security/secret-scanning/working-with-secret-scanning-and-push-protection/working-with-push-protection-from-the-rest-api "Push protection from the REST API")


# Working with push protection from the REST API
Learn your options for unblocking your push to GitHub using the REST API if secret scanning detects a secret in the content of your API request.
## Who can use this feature?
Users with **write** access
## In this article
  * [About push protection from the REST API](https://docs.github.com/en/code-security/secret-scanning/working-with-secret-scanning-and-push-protection/working-with-push-protection-from-the-rest-api#about-push-protection-from-the-rest-api)
  * [Further reading](https://docs.github.com/en/code-security/secret-scanning/working-with-secret-scanning-and-push-protection/working-with-push-protection-from-the-rest-api#further-reading)


## [About push protection from the REST API](https://docs.github.com/en/code-security/secret-scanning/working-with-secret-scanning-and-push-protection/working-with-push-protection-from-the-rest-api#about-push-protection-from-the-rest-api)
Push protection prevents you from accidentally committing secrets to a repository by blocking pushes containing supported secrets.
The "Create a blob" and "Create or update file contents" endpoints in the REST API include push protection. See [REST API endpoints for Git blobs](https://docs.github.com/en/rest/git/blobs?apiVersion=2022-11-28#create-a-blob) and [REST API endpoints for repository contents](https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28#create-or-update-file-contents).
If you make a request with these endpoints whose content includes a supported secret, the REST API will return a 409 error, indicating that a secret has been detected.
To resolve the error, you can either:
  * **Remove** the secret from the content of your API request before trying again.
  * **Create a push protection bypass:** You can bypass push protection using the "Create a push protection bypass" endpoint. For more information, see [REST API endpoints for secret scanning](https://docs.github.com/en/rest/secret-scanning/secret-scanning?apiVersion=2022-11-28#create-a-push-protection-bypass).


## [Further reading](https://docs.github.com/en/code-security/secret-scanning/working-with-secret-scanning-and-push-protection/working-with-push-protection-from-the-rest-api#further-reading)
  * [Working with push protection from the command line](https://docs.github.com/en/code-security/secret-scanning/working-with-secret-scanning-and-push-protection/working-with-push-protection-from-the-command-line)
  * [Working with push protection in the GitHub UI](https://docs.github.com/en/code-security/secret-scanning/working-with-secret-scanning-and-push-protection/working-with-push-protection-in-the-github-ui)


