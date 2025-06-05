  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Supply chain security](https://docs.github.com/en/code-security/supply-chain-security "Supply chain security")/
  * [End-to-end supply chain](https://docs.github.com/en/code-security/supply-chain-security/end-to-end-supply-chain "End-to-end supply chain")/
  * [Securing builds](https://docs.github.com/en/code-security/supply-chain-security/end-to-end-supply-chain/securing-builds "Securing builds")


# Best practices for securing your build system
Guidance on how to protect the end of your supply chain—the systems you use to build and distribute artifacts.
## In this article
  * [About this guide](https://docs.github.com/en/code-security/supply-chain-security/end-to-end-supply-chain/securing-builds#about-this-guide)
  * [What's the risk?](https://docs.github.com/en/code-security/supply-chain-security/end-to-end-supply-chain/securing-builds#whats-the-risk)
  * [Secure your build system](https://docs.github.com/en/code-security/supply-chain-security/end-to-end-supply-chain/securing-builds#secure-your-build-system)
  * [Generate artifact attestations for your builds](https://docs.github.com/en/code-security/supply-chain-security/end-to-end-supply-chain/securing-builds#generate-artifact-attestations-for-your-builds)
  * [Sign your builds](https://docs.github.com/en/code-security/supply-chain-security/end-to-end-supply-chain/securing-builds#sign-your-builds)
  * [Harden security for GitHub Actions](https://docs.github.com/en/code-security/supply-chain-security/end-to-end-supply-chain/securing-builds#harden-security-for-github-actions)
  * [Next steps](https://docs.github.com/en/code-security/supply-chain-security/end-to-end-supply-chain/securing-builds#next-steps)


## [About this guide](https://docs.github.com/en/code-security/supply-chain-security/end-to-end-supply-chain/securing-builds#about-this-guide)
This guide describes the highest impact changes you can make to improve the security of your build systems. Each section outlines a change you can make to your processes to improve security. The highest impact changes are listed first.
## [What's the risk?](https://docs.github.com/en/code-security/supply-chain-security/end-to-end-supply-chain/securing-builds#whats-the-risk)
Some attacks on software supply chains target the build system directly. If an attacker can modify the build process, they can exploit your system without the effort of compromising personal accounts or code. It's important to make sure that you don't forget to protect the build system as well as personal accounts and code.
## [Secure your build system](https://docs.github.com/en/code-security/supply-chain-security/end-to-end-supply-chain/securing-builds#secure-your-build-system)
There are several security capabilities a build system should have:
  1. The build steps should be clear and repeatable.
  2. You should know exactly what was running during the build process.
  3. Each build should start in a fresh environment, so a compromised build doesn't persist to affect future builds.


GitHub Actions can help you meet these capabilities. Build instructions are stored in your repository, alongside your code. You choose what environment your build runs on, including Windows, Mac, Linux, or runners you host yourself. Each build starts with a fresh runner image, making it difficult for an attack to persist in your build environment.
In addition to the security benefits, GitHub Actions lets you trigger builds manually, periodically, or on git events in your repository for frequent and fast builds.
GitHub Actions is a big topic, but a good place to get started is [Understanding GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions), as well as [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#choosing-github-hosted-runners), and [Triggering a workflow](https://docs.github.com/en/actions/using-workflows/triggering-a-workflow).
## [Generate artifact attestations for your builds](https://docs.github.com/en/code-security/supply-chain-security/end-to-end-supply-chain/securing-builds#generate-artifact-attestations-for-your-builds)
Artifact attestations enable you to create unfalsifiable provenance and integrity guarantees for the software you build. In turn, people who consume your software can verify where and how your software was built.
When you generate artifact attestations with your software, you create cryptographically signed claims that establish your build's provenance and include the following information:
  * A link to the workflow associated with the artifact.
  * The repository, organization, environment, commit SHA, and triggering event for the artifact.
  * Other information from the OIDC token used to establish provenance. For more information, see [About security hardening with OpenID Connect](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect).


You can also generate artifact attestations that include an associated software bill of materials (SBOM). Associating your builds with a list of the open source dependencies used in them provides transparency and enables consumers to comply with data protection standards.
Artifact attestations include a signature over a built artifact, along with links to the source code and build instructions. If you sign your build with artifact attestations, you do not have to manage your own signing key material. GitHub handles this for you with the signing authority we operate.
For more information, see [Using artifact attestations to establish provenance for builds](https://docs.github.com/en/actions/security-guides/using-artifact-attestations-to-establish-provenance-for-builds).
## [Sign your builds](https://docs.github.com/en/code-security/supply-chain-security/end-to-end-supply-chain/securing-builds#sign-your-builds)
After your build process is secure, you want to prevent someone from tampering with the end result of your build process. A great way to do this is to sign your builds. When distributing software publicly, this is often done with a public/private cryptographic key pair. You use the private key to sign the build, and you publish your public key so users of your software can verify the signature on the build before they use it. If the bytes of the build are modified, the signature will not verify.
How exactly you sign your build will depend on what sort of code you're writing, and who your users are. Often it's difficult to know how to securely store the private key. One basic option here is to use GitHub Actions encrypted secrets, although you'll need to be careful to limit who has access to those GitHub Actions workflows. If your private key is stored in another system accessible over the public internet (like Microsoft Azure, or HashiCorp Vault), a more advanced option is to authenticate with OpenID Connect, so you don't have to share secrets across systems. If your private key is only accessible from a private network, another option is to use self-hosted runners for GitHub Actions.
For more information, see [Using secrets in GitHub Actions](https://docs.github.com/en/actions/security-guides/encrypted-secrets), [About security hardening with OpenID Connect](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect), and [About self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners).
## [Harden security for GitHub Actions](https://docs.github.com/en/code-security/supply-chain-security/end-to-end-supply-chain/securing-builds#harden-security-for-github-actions)
There are many further steps you can take to additionally secure GitHub Actions. In particular, be careful when evaluating third-party workflows, and consider using `CODEOWNERS` to limit who can make changes to your workflows.
For more information, see [Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions) and [Using GitHub's security features to secure your use of GitHub Actions](https://docs.github.com/en/actions/security-guides/using-githubs-security-features-to-secure-your-use-of-github-actions).
## [Next steps](https://docs.github.com/en/code-security/supply-chain-security/end-to-end-supply-chain/securing-builds#next-steps)
  * [Securing your end-to-end supply chain](https://docs.github.com/en/code-security/supply-chain-security/end-to-end-supply-chain/end-to-end-supply-chain-overview)
  * [Best practices for securing accounts](https://docs.github.com/en/code-security/supply-chain-security/end-to-end-supply-chain/securing-accounts)
  * [Best practices for securing code in your supply chain](https://docs.github.com/en/code-security/supply-chain-security/end-to-end-supply-chain/securing-code)


