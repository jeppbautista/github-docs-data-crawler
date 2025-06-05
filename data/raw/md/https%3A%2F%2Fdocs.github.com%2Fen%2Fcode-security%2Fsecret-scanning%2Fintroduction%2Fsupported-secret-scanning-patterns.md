  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Secret scanning](https://docs.github.com/en/code-security/secret-scanning "Secret scanning")/
  * [Introduction](https://docs.github.com/en/code-security/secret-scanning/introduction "Introduction")/
  * [Supported patterns](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns "Supported patterns")


# Supported secret scanning patterns
Lists of supported secrets and the partners that GitHub works with to prevent fraudulent use of secrets that were committed accidentally.
## Who can use this feature?
Secret scanning is available for the following repository types:
  * Public repositories on GitHub.com
  * Organization-owned repositories on GitHub Team with [GitHub Secret Protection](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) enabled


## In this article
  * [About secret scanning patterns](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#about-secret-scanning-patterns)
  * [Supported secrets](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#supported-secrets)
  * [Further reading](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#further-reading)


## [About secret scanning patterns](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#about-secret-scanning-patterns)
There are three types of secret scanning alerts:
  * **User alerts:** Reported to users in the **Security** tab of the repository, when a supported secret is detected in the repository.
  * **Push protection alerts:** Reported to users in the **Security** tab of the repository, when a contributor bypasses push protection.
  * **Partner alerts:** Reported directly to secret providers that are part of secret scanning's partner program. These alerts are not reported in the **Security** tab of the repository.


For in-depth information about each alert type, see [About secret scanning alerts](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/about-alerts).
For details about all the supported patterns, see the [Supported secrets](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#supported-secrets) section below.
If you use the REST API for secret scanning, you can use the `Secret type` to report on secrets from specific issuers. For more information, see [REST API endpoints for secret scanning](https://docs.github.com/en/enterprise-cloud@latest/rest/secret-scanning).
If you believe that secret scanning should have detected a secret committed to your repository, and it has not, you first need to check that GitHub supports your secret. For more information, refer to the following sections. For more advanced troubleshooting information, see [Troubleshooting secret scanning](https://docs.github.com/en/code-security/secret-scanning/troubleshooting-secret-scanning-and-push-protection/troubleshooting-secret-scanning).
## [Supported secrets](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#supported-secrets)
This table lists the secrets supported by secret scanning. You can see the types of alert that get generated for each token, as well as whether a validity check is performed on the token.
  * **Provider:** Name of the token provider.
  * **Partner:** Token for which leaks are reported to the relevant token partner. Applies to public repositories only.
  * **User:** Token for which leaks are reported to users on GitHub.
    * Applies to public repositories, and to private repositories where GitHub Secret Protection and secret scanning are enabled.
    * Includes default tokens, which relate to supported patterns and specified custom patterns, as well as non-provider tokens such as private keys, which usually have a higher ratio of false positives.
    * For secret scanning to scan for non-provider patterns, the detection of non-provider patterns must be enabled for the repository or the organization. For more information, see [Enabling secret scanning for your repository](https://docs.github.com/en/code-security/secret-scanning/enabling-secret-scanning-features/enabling-secret-scanning-for-your-repository).
  * **Push protection:** Token for which leaks are reported to users on GitHub. Applies to repositories with secret scanning and push protection enabled.
  * **Validity check:** Token for which a validity check is implemented. For partner tokens, GitHub sends the token to the relevant partner. Note that not all partners are based in the United States. For more information, see [Advanced Security](https://docs.github.com/en/site-policy/github-terms/github-terms-for-additional-products-and-features#advanced-security) in the Site Policy documentation.


### [Non-provider patterns](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#non-provider-patterns)
Provider | Token  
---|---  
Generic | password  
Generic | http_basic_authentication_header  
Generic | http_bearer_authentication_header  
Generic | mongodb_connection_string  
Generic | mysql_connection_string  
Generic | openssh_private_key  
Generic | pgp_private_key  
Generic | postgres_connection_string  
Generic | rsa_private_key  
Push protection and validity checks are not supported for non-provider patterns.
### [Default patterns](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#default-patterns)
Validity checks are only available to users with GitHub Team or GitHub Enterprise who enable the feature as part of GitHub Secret Protection.
Provider | Token | Partner | User | Push protection | Validity check  
---|---|---|---|---|---  
Adafruit | adafruit_io_key |  |  |  |   
Adobe | adobe_client_secret |  |  |  |   
Adobe | adobe_device_token |  |  |  |   
Adobe | adobe_pac_token |  |  |  |   
Adobe | adobe_refresh_token |  |  |  |   
Adobe | adobe_service_token |  |  |  |   
Adobe | adobe_short_lived_access_token |  |  |  |   
Aiven | aiven_auth_token |  |  |  |   
Aiven | aiven_service_password |  |  |  |   
Alibaba | alibaba_cloud_access_key_id   
alibaba_cloud_access_key_secret |  |  |  |   
Amazon AWS | aws_access_key_id   
aws_secret_access_key |  |  |  |   
Amazon AWS | aws_secret_access_key   
aws_session_token   
aws_temporary_access_key_id |  |  |  |   
Anthropic | anthropic_admin_api_key |  |  |  |   
Anthropic | anthropic_api_key |  |  |  |   
Anthropic | anthropic_session_id |  |  |  |   
Asaas | asaas_api_token |  |  |  |   
Asana | asana_legacy_format_personal_access_token |  |  |  |   
Asana | asana_personal_access_token |  |  |  |   
Atlassian | atlassian_api_token   
[Token versions](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#token-versions) |  |  |  |   
Atlassian | atlassian_jwt |  |  |  |   
Authress | authress_service_client_access_key |  |  |  |   
Azure | azure_active_directory_application_secret   
[Token versions](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#token-versions) |  |  |  |   
Azure | azure_active_directory_user_credential |  |  |  |   
Azure | azure_apim_direct_management_key |  |  |  |   
Azure | azure_apim_gateway_key |  |  |  |   
Azure | azure_apim_repository_key |  |  |  |   
Azure | azure_apim_subscription_key |  |  |  |   
Azure | azure_app_configuration_connection_string |  |  |  |   
Azure | azure_batch_key_identifiable |  |  |  |   
Azure | azure_cache_for_redis_access_key |  |  |  |   
Azure | azure_communication_services_connection_string |  |  |  |   
Azure | azure_container_registry_key_identifiable |  |  |  |   
Azure | azure_cosmosdb_key_identifiable |  |  |  |   
Azure | azure_devops_personal_access_token |  |  |  |   
Azure | azure_event_hub_key_identifiable |  |  |  |   
Azure | azure_function_key |  |  |  |   
Azure | azure_iot_device_connection_string |  |  |  |   
Azure | azure_iot_device_key |  |  |  |   
Azure | azure_iot_device_provisioning_key |  |  |  |   
Azure | azure_iot_hub_connection_string |  |  |  |   
Azure | azure_iot_hub_key |  |  |  |   
Azure | azure_iot_provisioning_connection_string |  |  |  |   
Azure | azure_management_certificate |  |  |  |   
Azure | azure_ml_web_service_classic_identifiable_key |  |  |  |   
Azure | azure_openai_key |  |  |  |   
Azure | azure_relay_key_identifiable |  |  |  |   
Azure | azure_sas_token |  |  |  |   
Azure | azure_search_admin_key |  |  |  |   
Azure | azure_search_query_key |  |  |  |   
Azure | azure_service_bus_identifiable |  |  |  |   
Azure | azure_signalr_connection_string |  |  |  |   
Azure | azure_sql_connection_string |  |  |  |   
Azure | azure_sql_password |  |  |  |   
Azure | azure_storage_account_key   
[Token versions](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#token-versions) |  |  |  |   
Azure | azure_web_pub_sub_connection_string |  |  |  |   
Azure | microsoft_azure_entra_id_token |  |  |  |   
Azure | microsoft_corporate_network_user_credential |  |  |  |   
Baidu | baiducloud_api_accesskey |  |  |  |   
Beamer | beamer_api_key |  |  |  |   
Bitbucket | bitbucket_server_personal_access_token |  |  |  |   
Bitrise | bitrise_personal_access_token |  |  |  |   
Bitrise | bitrise_workspace_api_token |  |  |  |   
Block Protocol | block_protocol_api_key |  |  |  |   
Brevo | sendinblue_api_key |  |  |  |   
Brevo | sendinblue_smtp_key |  |  |  |   
Buildkite | buildkite_user_access_token |  |  |  |   
Canadian Digital Service | cds_canada_notify_api_key |  |  |  |   
Canva | canva_app_secret |  |  |  |   
Canva | canva_connect_api_secret |  |  |  |   
Canva | canva_secret |  |  |  |   
Cashfree | cashfree_api_key |  |  |  |   
Cfx.re | cfxre_server_key |  |  |  |   
Checkout.com | checkout_production_secret_key   
[Token versions](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#token-versions) |  |  |  |   
Checkout.com | checkout_test_secret_key   
[Token versions](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#token-versions) |  |  |  |   
Chief Tools | chief_tools_token |  |  |  |   
CircleCI | circleci_bot_access_token |  |  |  |   
CircleCI | circleci_personal_access_token |  |  |  |   
CircleCI | circleci_project_access_token |  |  |  |   
CircleCI | circleci_release_integration_token |  |  |  |   
Clojars | clojars_deploy_token |  |  |  |   
CloudBees | codeship_credential |  |  |  |   
Cockroach Labs | ccdb_api_key |  |  |  |   
Contentful | contentful_personal_access_token |  |  |  |   
Contributed Systems | contributed_systems_credentials |  |  |  |   
Coveo | coveo_access_token |  |  |  |   
Coveo | coveo_api_key |  |  |  |   
crates.io | cratesio_api_token |  |  |  |   
Databento | databento_api_key |  |  |  |   
Databricks | databricks_access_token |  |  |  |   
Datadog | datadog_api_key |  |  |  |   
Datadog | datadog_app_key |  |  |  |   
Datadog | datadog_rcm |  |  |  |   
Datastax | datastax_astracs_token |  |  |  |   
Defined Networking | defined_networking_nebula_api_key |  |  |  |   
DevCycle | devcycle_client_api_key |  |  |  |   
DevCycle | devcycle_mobile_api_key |  |  |  |   
DevCycle | devcycle_server_api_key |  |  |  |   
DigitalOcean | digitalocean_oauth_token |  |  |  |   
DigitalOcean | digitalocean_personal_access_token |  |  |  |   
DigitalOcean | digitalocean_refresh_token |  |  |  |   
DigitalOcean | digitalocean_system_token |  |  |  |   
Discord | discord_bot_token   
[Token versions](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#token-versions) |  |  |  |   
Docker | docker_organization_access_token |  |  |  |   
Docker | docker_personal_access_token |  |  |  |   
Docker | docker_swarm_join_token |  |  |  |   
Docker | docker_swarm_unlock_key |  |  |  |   
Doppler | doppler_audit_token |  |  |  |   
Doppler | doppler_cli_token |  |  |  |   
Doppler | doppler_personal_token |  |  |  |   
Doppler | doppler_scim_token |  |  |  |   
Doppler | doppler_service_account_token |  |  |  |   
Doppler | doppler_service_token |  |  |  |   
Dropbox | dropbox_access_token |  |  |  |   
Dropbox | dropbox_short_lived_access_token |  |  |  |   
Duffel | duffel_live_access_token |  |  |  |   
Duffel | duffel_test_access_token |  |  |  |   
Dynatrace | dynatrace_api_token |  |  |  |   
Dynatrace | dynatrace_internal_token |  |  |  |   
EasyPost | easypost_production_api_key |  |  |  |   
EasyPost | easypost_test_api_key |  |  |  |   
eBay | ebay_production_client_id   
ebay_production_client_secret |  |  |  |   
eBay | ebay_sandbox_client_id   
ebay_sandbox_client_secret |  |  |  |   
Facebook | facebook_access_token |  |  |  |   
Fastly | fastly_api_token   
[Token versions](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#token-versions) |  |  |  |   
Figma | figma_pat |  |  |  |   
Finicity | finicity_app_key |  |  |  |   
Firebase | firebase_cloud_messaging_server_key |  |  |  |   
Flutterwave | flutterwave_live_api_secret_key |  |  |  |   
Flutterwave | flutterwave_test_api_secret_key |  |  |  |   
Frame.io | frameio_developer_token |  |  |  |   
Frame.io | frameio_jwt |  |  |  |   
FullStory | fullstory_api_key   
[Token versions](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#token-versions) |  |  |  |   
GitHub | github_app_installation_access_token   
[Token versions](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#token-versions) |  |  |  |   
GitHub | github_oauth_access_token   
[Token versions](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#token-versions) |  |  |  |   
GitHub | github_personal_access_token   
[Token versions](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#token-versions) |  |  |  |   
GitHub | github_refresh_token   
[Token versions](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#token-versions) |  |  |  |   
GitHub | github_ssh_private_key |  |  |  |   
GitHub | github_test_token |  |  |  |   
GitHub Secret Scanning | secret_scanning_sample_token |  |  |  |   
GitLab | gitlab_access_token |  |  |  |   
GoCardless | gocardless_live_access_token |  |  |  |   
GoCardless | gocardless_sandbox_access_token |  |  |  |   
Google | google_api_key |  |  |  |   
Google | google_cloud_service_account_credentials |  |  |  |   
Google | google_cloud_storage_access_key_secret   
google_cloud_storage_service_account_access_key_id |  |  |  |   
Google | google_cloud_storage_access_key_secret   
google_cloud_storage_user_access_key_id |  |  |  |   
Google | google_gcp_api_key_bound_service_account |  |  |  |   
Google | google_oauth_access_token |  |  |  |   
Google | google_oauth_client_id   
google_oauth_client_secret |  |  |  |   
Google | google_oauth_refresh_token |  |  |  |   
Grafana | grafana_cloud_api_key |  |  |  |   
Grafana | grafana_cloud_api_token |  |  |  |   
Grafana | grafana_project_api_key |  |  |  |   
Grafana | grafana_project_service_account_token |  |  |  |   
Groq | groq_api_key |  |  |  |   
HashiCorp | hashicorp_vault_batch_token   
[Token versions](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#token-versions) |  |  |  |   
HashiCorp | hashicorp_vault_root_service_token |  |  |  |   
HashiCorp | hashicorp_vault_service_token   
[Token versions](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#token-versions) |  |  |  |   
HashiCorp | terraform_api_token |  |  |  |   
Heroku | heroku_platform_api_oauth2_token |  |  |  |   
Heroku | heroku_postgres_connection_url |  |  |  |   
Highnote | highnote_rk_live_key |  |  |  |   
Highnote | highnote_rk_test_key |  |  |  |   
Highnote | highnote_sk_live_key |  |  |  |   
Highnote | highnote_sk_test_key |  |  |  |   
HOP | hop_bearer |  |  |  |   
HOP | hop_pat |  |  |  |   
HOP | hop_ptk |  |  |  |   
Hubspot | hubspot_api_key   
[Token versions](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#token-versions) |  |  |  |   
Hubspot | hubspot_personal_access_key |  |  |  |   
Hubspot | hubspot_private_apps_user_token |  |  |  |   
Hubspot | hubspot_smtp_credential   
[Token versions](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#token-versions) |  |  |  |   
Hugging Face | hf_org_api_key |  |  |  |   
Hugging Face | hf_user_access_token |  |  |  |   
IBM | ibm_cloud_iam_key |  |  |  |   
IBM | ibm_softlayer_api_key |  |  |  |   
Intercom | intercom_access_token |  |  |  |   
Ionic | ionic_personal_access_token   
[Token versions](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#token-versions) |  |  |  |   
Ionic | ionic_refresh_token   
[Token versions](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#token-versions) |  |  |  |   
Iterative | iterative_dvc_studio_access_token |  |  |  |   
JFrog | jfrog_platform_access_token |  |  |  |   
JFrog | jfrog_platform_api_key |  |  |  |   
JFrog | jfrog_platform_reference_token |  |  |  |   
LaunchDarkly | launchdarkly_access_token |  |  |  |   
Lichess | lichess_oauth_access_token |  |  |  |   
Lichess | lichess_personal_access_token |  |  |  |   
Lightspeed | lightspeed_xs_pat |  |  |  |   
Linear | linear_api_key |  |  |  |   
Linear | linear_oauth_access_token |  |  |  |   
LinkedIn | linkedin_client_secret |  |  |  |   
Lob | lob_live_api_key |  |  |  |   
Lob | lob_test_api_key |  |  |  |   
Localstack | localstack_api_key |  |  |  |   
LogicMonitor | logicmonitor_bearer_token |  |  |  |   
LogicMonitor | logicmonitor_lmv1_access_key |  |  |  |   
Login with Amazon | amazon_oauth_client_id   
amazon_oauth_client_secret   
amazon_oauth_client_secret |  |  |  |   
Mailchimp | mailchimp_api_key |  |  |  |   
Mailchimp | mandrill_api_key |  |  |  |   
Mailersend | mailersend_api_token |  |  |  |   
Mailersend | mailersend_smtp_password |  |  |  |   
Mailersend | mailersend_smtp_username |  |  |  |   
Mailgun | mailgun_api_key   
[Token versions](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#token-versions) |  |  |  |   
Mailgun | mailgun_smtp_credential |  |  |  |   
Mapbox | mapbox_secret_access_token |  |  |  |   
MaxMind | maxmind_license_key |  |  |  |   
Mercury | mercury_non_production_api_token |  |  |  |   
Mercury | mercury_production_api_token |  |  |  |   
Mergify | mergify_application_key |  |  |  |   
MessageBird | messagebird_api_key |  |  |  |   
Midtrans | midtrans_production_server_key |  |  |  |   
Midtrans | midtrans_sandbox_server_key |  |  |  |   
MongoDB | mongodb_atlas_db_uri_with_credentials |  |  |  |   
MongoDB | mongodb_atlas_service_account_secret |  |  |  |   
Naver Cloud | navercloud_gov_access_key |  |  |  |   
Naver Cloud | navercloud_gov_access_key_secret |  |  |  |   
Naver Cloud | navercloud_gov_sts |  |  |  |   
Naver Cloud | navercloud_gov_sts_secret |  |  |  |   
Naver Cloud | navercloud_pub_access_key |  |  |  |   
Naver Cloud | navercloud_pub_access_key_secret |  |  |  |   
Naver Cloud | navercloud_pub_sts |  |  |  |   
Naver Cloud | navercloud_pub_sts_secret |  |  |  |   
Neon | neon_api_key |  |  |  |   
Neon | neon_connection_uri |  |  |  |   
Netflix | netflix_netkey |  |  |  |   
New Relic | new_relic_insights_query_key |  |  |  |   
New Relic | new_relic_license_key |  |  |  |   
New Relic | new_relic_personal_api_key |  |  |  |   
New Relic | new_relic_rest_api_key |  |  |  |   
Notion | notion_integration_token |  |  |  |   
Notion | notion_oauth_client_secret |  |  |  |   
npm | npm_access_token   
[Token versions](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#token-versions) |  |  |  |   
NuGet | nuget_api_key |  |  |  |   
Octopus Deploy | octopus_deploy_api_key |  |  |  |   
Oculus | oculus_access_token |  |  |  |   
OneChronos | onechronos_api_key |  |  |  |   
OneChronos | onechronos_eb_api_key |  |  |  |   
OneChronos | onechronos_eb_encryption_key |  |  |  |   
OneChronos | onechronos_oauth_token |  |  |  |   
OneChronos | onechronos_refresh_token |  |  |  |   
Onfido | onfido_live_api_token |  |  |  |   
Onfido | onfido_sandbox_api_token |  |  |  |   
OpenAI | openai_api_key   
[Token versions](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#token-versions) |  |  |  |   
OpenRouter | openrouter_api_key |  |  |  |   
Oracle | oracle_api_key |  |  |  |   
Orbit | orbit_api_token |  |  |  |   
PagerDuty | pagerduty_oauth_secret |  |  |  |   
PagerDuty | pagerduty_oauth_token |  |  |  |   
Palantir | palantir_jwt |  |  |  |   
Pangea | pangea_token |  |  |  |   
Persona Identities | persona_production_api_key |  |  |  |   
Persona Identities | persona_sandbox_api_key |  |  |  |   
Pinterest | pinterest_access_token |  |  |  |   
Pinterest | pinterest_refresh_token |  |  |  |   
PlanetScale | planetscale_database_password |  |  |  |   
PlanetScale | planetscale_oauth_token |  |  |  |   
PlanetScale | planetscale_service_token |  |  |  |   
Planning Center | planning_center_oauth_access_token |  |  |  |   
Planning Center | planning_center_oauth_app_secret |  |  |  |   
Planning Center | planning_center_personal_access_token |  |  |  |   
Plivo | plivo_auth_id   
plivo_auth_token |  |  |  |   
Polar | polar_access_token |  |  |  |   
Polar | polar_authorization_code |  |  |  |   
Polar | polar_client_registration_token |  |  |  |   
Polar | polar_client_secret |  |  |  |   
Polar | polar_personal_access_token |  |  |  |   
Polar | polar_refresh_token |  |  |  |   
Postman | postman_api_key |  |  |  |   
Postman | postman_collection_key |  |  |  |   
Prefect | prefect_server_api_key |  |  |  |   
Prefect | prefect_user_api_key |  |  |  |   
Proctorio | proctorio_consumer_key |  |  |  |   
Proctorio | proctorio_linkage_key |  |  |  |   
Proctorio | proctorio_registration_key |  |  |  |   
Proctorio | proctorio_secret_key   
[Token versions](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#token-versions) |  |  |  |   
Pulumi | pulumi_access_token |  |  |  |   
PyPI | pypi_api_token |  |  |  |   
Ramp | ramp_client_id |  |  |  |   
Ramp | ramp_client_secret |  |  |  |   
Ramp | ramp_oauth_token |  |  |  |   
ReadMe | readmeio_api_access_token |  |  |  |   
redirect.pizza | redirect_pizza_api_token |  |  |  |   
Replicate | replicate_api_token |  |  |  |   
Rootly | rootly_api_key |  |  |  |   
RubyGems | rubygems_api_key |  |  |  |   
RunPod | runpod_api_key |  |  |  |   
Salesforce | salesforce_oauth2_consumer_key   
salesforce_oauth2_consumer_secret |  |  |  |   
Salesforce | salesforce_refresh_token |  |  |  |   
Samsara | samsara_api_token |  |  |  |   
Samsara | samsara_oauth_access_token |  |  |  |   
Scalr | scalr_api_token |  |  |  |   
Segment | segment_public_api_token |  |  |  |   
SendGrid | sendgrid_api_key |  |  |  |   
Sentry | sentry_integration_token |  |  |  |   
Sentry | sentry_org_auth_token |  |  |  |   
Sentry | sentry_user_app_auth_token |  |  |  |   
Sentry | sentry_user_auth_token |  |  |  |   
Shippo | shippo_live_api_token |  |  |  |   
Shippo | shippo_test_api_token |  |  |  |   
Shopee | shopee_open_platform_partner_key |  |  |  |   
Shopify | shopify_access_token |  |  |  |   
Shopify | shopify_app_client_credentials |  |  |  |   
Shopify | shopify_app_client_secret |  |  |  |   
Shopify | shopify_app_shared_secret |  |  |  |   
Shopify | shopify_custom_app_access_token |  |  |  |   
Shopify | shopify_marketplace_token |  |  |  |   
Shopify | shopify_merchant_token |  |  |  |   
Shopify | shopify_partner_api_token |  |  |  |   
Shopify | shopify_private_app_password |  |  |  |   
Siemens | siemens_api_token |  |  |  |   
Siemens | siemens_code_token |  |  |  |   
Sindri | sindri_api_key   
[Token versions](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#token-versions) |  |  |  |   
Slack | slack_api_token   
[Token versions](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#token-versions) |  |  |  |   
Slack | slack_incoming_webhook_url |  |  |  |   
Slack | slack_workflow_webhook_url |  |  |  |   
Sourcegraph | sourcegraph_access_token |  |  |  |   
Sourcegraph | sourcegraph_dotcom_user_gateway |  |  |  |   
Sourcegraph | sourcegraph_instance_identifier_access_token |  |  |  |   
Sourcegraph | sourcegraph_license_key_token |  |  |  |   
Sourcegraph | sourcegraph_product_subscription_token |  |  |  |   
Square | square_access_token   
[Token versions](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#token-versions) |  |  |  |   
Square | square_production_application_secret |  |  |  |   
Square | square_sandbox_application_secret |  |  |  |   
SSLMate | sslmate_api_key   
[Token versions](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#token-versions) |  |  |  |   
SSLMate | sslmate_cluster_secret |  |  |  |   
Stripe | stripe_api_key |  |  |  |   
Stripe | stripe_legacy_api_key |  |  |  |   
Stripe | stripe_live_restricted_key |  |  |  |   
Stripe | stripe_test_restricted_key |  |  |  |   
Stripe | stripe_test_secret_key |  |  |  |   
Stripe | stripe_webhook_signing_secret |  |  |  |   
Supabase | supabase_service_key   
[Token versions](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#token-versions) |  |  |  |   
Tableau | tableau_personal_access_token |  |  |  |   
Tailscale | tailscale_api_key |  |  |  |   
Telegram | telegram_bot_token |  |  |  |   
Telnyx | telnyx_api_v2_key |  |  |  |   
Tencent | tencent_cloud_secret_id |  |  |  |   
Tencent | tencent_wechat_api_app_id |  |  |  |   
Thunderstore | thunderstore_io_api_token |  |  |  |   
Twilio | twilio_access_token |  |  |  |   
Twilio | twilio_account_sid |  |  |  |   
Twilio | twilio_api_key |  |  |  |   
Typeform | typeform_personal_access_token |  |  |  |   
Uniwise | wiseflow_api_key |  |  |  |   
Unkey | unkey_root_key |  |  |  |   
VolcEngine | volcengine_access_key_id |  |  |  |   
Wakatime | wakatime_api_key |  |  |  |   
Wakatime | wakatime_app_secret |  |  |  |   
Wakatime | wakatime_oauth_access_token |  |  |  |   
Wakatime | wakatime_oauth_refresh_token |  |  |  |   
Workato | workato_developer_api_token   
[Token versions](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#token-versions) |  |  |  |   
WorkOS | workos_production_api_key   
[Token versions](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#token-versions) |  |  |  |   
WorkOS | workos_staging_api_key   
[Token versions](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#token-versions) |  |  |  |   
xAI | xai_api_key |  |  |  |   
Yandex | yandex_cloud_api_key |  |  |  |   
Yandex | yandex_cloud_iam_access_secret |  |  |  |   
Yandex | yandex_cloud_iam_cookie |  |  |  |   
Yandex | yandex_cloud_iam_token |  |  |  |   
Yandex | yandex_cloud_smartcaptcha_server_key |  |  |  |   
Yandex | yandex_dictionary_api_key |  |  |  |   
Yandex | yandex_passport_oauth_token |  |  |  |   
Yandex | yandex_predictor_api_key |  |  |  |   
Yandex | yandex_translate_api_key |  |  |  |   
Zuplo | zuplo_consumer_api_key |  |  |  |   
#### [Token versions](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#token-versions)
Service providers update the patterns used to generate tokens periodically and may support more than one version of a token. Push protection only supports the most recent token versions that secret scanning can identify with confidence. This avoids push protection blocking commits unnecessarily when a result may be a false positive, which is more likely to happen with legacy tokens.
## [Further reading](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#further-reading)
  * [About secret scanning alerts](https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/about-alerts)
  * [Secret scanning partner program](https://docs.github.com/en/code-security/secret-scanning/secret-scanning-partnership-program/secret-scanning-partner-program)
  * [Quickstart for securing your repository](https://docs.github.com/en/code-security/getting-started/securing-your-repository)
  * [Keeping your account and data secure](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure)


