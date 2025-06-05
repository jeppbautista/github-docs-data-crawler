  * [GitHub Actions](https://docs.github.com/en/actions "GitHub Actions")/
  * [Security](https://docs.github.com/en/actions/security-for-github-actions "Security")/
  * [Artifact attestations](https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations "Artifact attestations")/
  * [Artifact attestations](https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds "Artifact attestations")


# Using artifact attestations to establish provenance for builds
Artifact attestations enable you to increase the supply chain security of your builds by establishing where and how your software was built.
## Who can use this feature?
Artifact attestations are available in public repositories for all current GitHub plans. They are not available on legacy plans, such as Bronze, Silver, or Gold. If you are on a GitHub Free, GitHub Pro, or GitHub Team plan, artifact attestations are only available for public repositories. To use artifact attestations in private or internal repositories, you must be on a GitHub Enterprise Cloud plan.
## In this article
  * [About artifact attestations](https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds#about-artifact-attestations)
  * [Generating artifact attestations for your builds](https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds#generating-artifact-attestations-for-your-builds)
  * [Generating an attestation for a software bill of materials (SBOM)](https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds#generating-an-attestation-for-a-software-bill-of-materials-sbom)
  * [Verifying artifact attestations with the GitHub CLI](https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds#verifying-artifact-attestations-with-the-github-cli)


## [About artifact attestations](https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds#about-artifact-attestations)
Artifact attestations enable you to create unfalsifiable provenance and integrity guarantees for the software you build. In turn, people who consume your software can verify where and how your software was built.
When you generate artifact attestations with your software, you create cryptographically signed claims that establish your build's provenance and include the following information:
  * A link to the workflow associated with the artifact.
  * The repository, organization, environment, commit SHA, and triggering event for the artifact.
  * Other information from the OIDC token used to establish provenance. For more information, see [About security hardening with OpenID Connect](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect).


You can also generate artifact attestations that include an associated software bill of materials (SBOM). Associating your builds with a list of the open source dependencies used in them provides transparency and enables consumers to comply with data protection standards.
### [About SLSA levels for artifact attestations](https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds#about-slsa-levels-for-artifact-attestations)
The SLSA framework is an industry standard used to evaluate supply chain security. It is organized into levels. Each level represents an increasing degree of security and trustworthiness for a software supply chain. Artifact attestations by itself provides SLSA v1.0 Build Level 2.
This provides a link between your artifact and its build instructions, but you can take this a step further by requiring builds make use of known, vetted build instructions. A great way to do this is to have your build take place in a reusable workflow that many repositories across your organization share. Reusable workflows can provide isolation between the build process and the calling workflow, to meet SLSA v1.0 Build Level 3. For more information, see [Using artifact attestations and reusable workflows to achieve SLSA v1 Build Level 3](https://docs.github.com/en/actions/security-guides/using-artifact-attestations-and-reusable-workflows-to-achieve-slsa-v1-build-level-3).
For more information on SLSA levels, see [SLSA Security Levels](https://slsa.dev/spec/v1.0/levels).
### [About using Sigstore for artifact attestations](https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds#about-using-sigstore-for-artifact-attestations)
To generate artifact attestations, GitHub uses Sigstore, which is an open source project that offers a comprehensive solution for signing and verifying software artifacts via attestations.
**Public repositories** that generate artifact attestations use the [Sigstore Public Good Instance](https://openssf.org/blog/2023/10/03/running-sigstore-as-a-managed-service-a-tour-of-sigstores-public-good-instance/). A copy of the generated Sigstore bundle is stored with GitHub and is also written to an immutable transparency log that is publicly readable on the internet.
**Private repositories** that generate artifact attestations use GitHub's Sigstore instance. GitHub's Sigstore instance uses the same codebase as the Sigstore Public Good Instance, but it does not have a transparency log and only federates with GitHub Actions.
### [What to attest](https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds#what-to-attest)
Generating attestations alone doesn't provide any security benefit, the attestations must be verified for the benefit to be realized. Here are some guidelines for how to think about what to sign and how often:
You should sign:
  * Software you are releasing that you expect people to run `gh attestation verify ...` on.
  * Binaries people will run, packages people will download, or manifests that include hashes of detailed contents.


You should **not** sign:
  * Frequent builds that are just for automated testing.
  * Individual files like source code, documentation files, or embedded images.


### [About verifying artifact attestations](https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds#about-verifying-artifact-attestations)
If you consume software that publishes artifact attestations, you can use the GitHub CLI to verify those attestations. Because the attestations give you information about where and how software was built, you can use that information to create and enforce security policies that elevate your supply chain security. For more information, see [Verifying artifact attestations with the GitHub CLI](https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds#verifying-artifact-attestations-with-the-github-cli).
It is important to remember that artifact attestations are _not_ a guarantee that an artifact is secure. Instead, artifact attestations link you to the source code and the build instructions that produced them. It is up to you to define your policy criteria, evaluate that policy by evaluating the content, and make an informed risk decision when you are consuming software.
## [Generating artifact attestations for your builds](https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds#generating-artifact-attestations-for-your-builds)
You can use GitHub Actions to generate artifact attestations that establish build provenance for artifacts such as binaries and container images.
To generate an artifact attestation, you must:
  * Ensure you have the appropriate permissions configured in your workflow.
  * Include a step in your workflow that uses the [`attest-build-provenance` action](https://github.com/actions/attest-build-provenance).


When you run your updated workflows, they will build your artifacts and generate an artifact attestation that establishes build provenance. You can view attestations in your repository's **Actions** tab. For more information, see the [`attest-build-provenance`](https://github.com/actions/attest-build-provenance) repository.
### [Generating build provenance for binaries](https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds#generating-build-provenance-for-binaries)
  1. In the workflow that builds the binary you would like to attest, add the following permissions.
```
permissions:
  id-token: write
  contents: read
  attestations: write

```

  2. After the step where the binary has been built, add the following step.
```
- name: Generate artifact attestation
  uses: actions/attest-build-provenance@v2
  with:
    subject-path: 'PATH/TO/ARTIFACT'

```

The value of the `subject-path` parameter should be set to the path to the binary you want to attest.


### [Generating build provenance for container images](https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds#generating-build-provenance-for-container-images)
  1. In the workflow that builds the container image you would like to attest, add the following permissions.
```
permissions:
  id-token: write
  contents: read
  attestations: write
  packages: write

```

  2. After the step where the image has been built, add the following step.
```
- name: Generate artifact attestation
  uses: actions/attest-build-provenance@v2
  with:
    subject-name: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
    subject-digest: 'sha256:fedcba0...'
    push-to-registry: true

```

The value of the `subject-name` parameter should specify the fully-qualified image name. For example, `ghcr.io/user/app` or `acme.azurecr.io/user/app`. Do not include a tag as part of the image name.
The value of the `subject-digest` parameter should be set to the SHA256 digest of the subject for the attestation, in the form `sha256:HEX_DIGEST`. If your workflow uses `docker/build-push-action`, you can use the [`digest`](https://github.com/docker/build-push-action?tab=readme-ov-file#outputs) output from that step to supply the value. For more information on using outputs, see [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idoutputs).


## [Generating an attestation for a software bill of materials (SBOM)](https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds#generating-an-attestation-for-a-software-bill-of-materials-sbom)
You can generate signed SBOM attestations for workflow artifacts.
To generate an attestation for an SBOM, you must:
  * Ensure you have the appropriate permissions configured in your workflow.
  * Create an SBOM for your artifact. For more information, see [`anchore-sbom-action`](https://github.com/marketplace/actions/anchore-sbom-action) in the GitHub Marketplace.
  * Include a step in your workflow that uses the [`attest-sbom` action](https://github.com/actions/attest-sbom).


When you run your updated workflows, they will build your artifacts and generate an SBOM attestation. You can view attestations in your repository's **Actions** tab. For more information, see the [`attest-sbom` action](https://github.com/actions/attest-sbom) repository.
### [Generating an SBOM attestation for binaries](https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds#generating-an-sbom-attestation-for-binaries)
  1. In the workflow that builds the binary you would like to attest, add the following permissions.
```
permissions:
  id-token: write
  contents: read
  attestations: write

```

  2. After the step where the binary has been built, add the following step.
```
- name: Generate SBOM attestation
  uses: actions/attest-sbom@v1
  with:
    subject-path: 'PATH/TO/ARTIFACT'
    sbom-path: 'PATH/TO/SBOM'

```

The value of the `subject-path` parameter should be set to the path of the binary the SBOM describes. The value of the `sbom-path` parameter should be set to the path of the SBOM file you generated.


### [Generating an SBOM attestation for container images](https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds#generating-an-sbom-attestation-for-container-images)
  1. In the workflow that builds the container image you would like to attest, add the following permissions.
```
permissions:
  id-token: write
  contents: read
  attestations: write
  packages: write

```

  2. After the step where the image has been built, add the following step.
```
- name: Generate SBOM attestation
  uses: actions/attest-sbom@v1
  with:
    subject-name: ${{ env.REGISTRY }}/PATH/TO/IMAGE
    subject-digest: 'sha256:fedcba0...'
    sbom-path: 'sbom.json'
    push-to-registry: true

```

The value of the `subject-name` parameter should specify the fully-qualified image name. For example, `ghcr.io/user/app` or `acme.azurecr.io/user/app`. Do not include a tag as part of the image name.
The value of the `subject-digest` parameter should be set to the SHA256 digest of the subject for the attestation, in the form `sha256:HEX_DIGEST`. If your workflow uses `docker/build-push-action`, you can use the [`digest`](https://github.com/docker/build-push-action?tab=readme-ov-file#outputs) output from that step to supply the value. For more information on using outputs, see [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idoutputs).
The value of the `sbom-path` parameter should be set to the path to the JSON-formatted SBOM file you want to attest.


## [Verifying artifact attestations with the GitHub CLI](https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds#verifying-artifact-attestations-with-the-github-cli)
You can validate artifact attestations for binaries and container images and validate SBOM attestations using the GitHub CLI. For more information, see the [`attestation`](https://cli.github.com/manual/gh_attestation) section of the GitHub CLI manual.
These commands assume you are in an online environment. If you are in an offline or air-gapped environment, see [Verifying attestations offline](https://docs.github.com/en/actions/security-guides/verifying-attestations-offline).
### [Verifying an artifact attestation for binaries](https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds#verifying-an-artifact-attestation-for-binaries)
To verify artifact attestations for **binaries** , use the following GitHub CLI command.
Bash```
gh attestation verify PATH/TO/YOUR/BUILD/ARTIFACT-BINARY -R ORGANIZATION_NAME/REPOSITORY_NAME

```
```
gh attestation verify PATH/TO/YOUR/BUILD/ARTIFACT-BINARY -R ORGANIZATION_NAME/REPOSITORY_NAME

```

### [Verifying an artifact attestation for container images](https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds#verifying-an-artifact-attestation-for-container-images)
To verify artifact attestations for **container images** , you must provide the image's FQDN prefixed with `oci://` instead of the path to a binary. You can use the following GitHub CLI command.
Bash```
docker login ghcr.io

gh attestation verify oci://ghcr.io/ORGANIZATION_NAME/IMAGE_NAME:test -R ORGANIZATION_NAME/REPOSITORY_NAME

```
```
docker login ghcr.io

gh attestation verify oci://ghcr.io/ORGANIZATION_NAME/IMAGE_NAME:test -R ORGANIZATION_NAME/REPOSITORY_NAME

```

### [Verifying an attestation for SBOMs](https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds#verifying-an-attestation-for-sboms)
To verify SBOM attestations, you have to provide the `--predicate-type` flag to reference a non-default predicate. For more information, see [Vetted predicates](https://github.com/in-toto/attestation/tree/main/spec/predicates#vetted-predicates) in the `in-toto/attestation` repository.
For example, the [`attest-sbom` action](https://github.com/actions/attest-sbom) currently supports either SPDX or CycloneDX SBOM predicates. To verify an SBOM attestation in the SPDX format, you can use the following GitHub CLI command.
Bash```
gh attestation verify PATH/TO/YOUR/BUILD/ARTIFACT-BINARY \
  -R ORGANIZATION_NAME/REPOSITORY_NAME \
  --predicate-type https://spdx.dev/Document/v2.3

```
```
gh attestation verify PATH/TO/YOUR/BUILD/ARTIFACT-BINARY \
  -R ORGANIZATION_NAME/REPOSITORY_NAME \
  --predicate-type https://spdx.dev/Document/v2.3

```

To view more information on the attestation, reference the `--format json` flag. This can be especially helpful when reviewing SBOM attestations.
Bash```
gh attestation verify PATH/TO/YOUR/BUILD/ARTIFACT-BINARY \
  -R ORGANIZATION_NAME/REPOSITORY_NAME \
  --predicate-type https://spdx.dev/Document/v2.3 \
  --format json \
  --jq '.[].verificationResult.statement.predicate'

```
```
gh attestation verify PATH/TO/YOUR/BUILD/ARTIFACT-BINARY \
  -R ORGANIZATION_NAME/REPOSITORY_NAME \
  --predicate-type https://spdx.dev/Document/v2.3 \
  --format json \
  --jq '.[].verificationResult.statement.predicate'

```

