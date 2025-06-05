  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Security advisories](https://docs.github.com/en/code-security/security-advisories "Security advisories")/
  * [Repository security advisories](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories "Repository security advisories")/
  * [Edit repository advisories](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/editing-a-repository-security-advisory "Edit repository advisories")


# Editing a repository security advisory
You can edit the metadata and description for a repository security advisory if you need to update details or correct errors.
## Who can use this feature?
Repository owners, organization owners, security managers, and users with the **admin** role
## In this article
  * [Editing a security advisory](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/editing-a-repository-security-advisory#editing-a-security-advisory)
  * [Further reading](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/editing-a-repository-security-advisory#further-reading)


This article applies to editing repository-level advisories as an owner of a public repository.
Users who are not repository owners can contribute to global security advisories in the GitHub Advisory Database at [github.com/advisories](https://github.com/advisories). Edits to global advisories will not change or affect how the advisory appears on the repository. For more information, see [Editing security advisories in the GitHub Advisory Database](https://docs.github.com/en/code-security/security-advisories/working-with-global-security-advisories-from-the-github-advisory-database/editing-security-advisories-in-the-github-advisory-database).
## [Editing a security advisory](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/editing-a-repository-security-advisory#editing-a-security-advisory)
You can also use the REST API to edit repository security advisories. For more information, see [REST API endpoints for repository security advisories](https://docs.github.com/en/rest/security-advisories/repository-advisories).
  1. On GitHub, navigate to the main page of the repository.
  2. Under the repository name, click **Security**. 
![Screenshot of a repository header showing the tabs. The "Security" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-17801/images/help/repository/security-tab.png)
  3. In the left sidebar, under "Reporting", click 
  4. In the "Security Advisories" list, click the name of the security advisory you'd like to edit.
  5. In the upper-right corner of the details for the security advisory, click **Edit advisory**. This will open the security advisory form in edit mode.
  6. Use the **CVE identifier** dropdown menu to specify whether you already have a CVE identifier or plan to request one from GitHub later. If you have an existing CVE identifier, select **I have an existing CVE identifier** to display an **Existing CVE** field, and type the CVE identifier in the field. For more information, see [About repository security advisories](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/about-repository-security-advisories#cve-identification-numbers).
  7. In the **Description** field, type a description of the security vulnerability including its impact, any patches or workarounds available, and any references.
  8. Under "Affected products", define the ecosystem, package name, affected/patched versions, and vulnerable functions for the security vulnerability that this security advisory describes. If applicable, you can add multiple affected products to the same advisory by clicking **Add another affected product**.
For information about how to specify information on the form, including affected versions, see [Best practices for writing repository security advisories](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/best-practices-for-writing-repository-security-advisories).
  9. Define the severity of the security vulnerability using the **Severity** dropdown menu. If you want to calculate a CVSS score, select **Assess severity using CVSS** and then select the appropriate values in the **Calculator**. GitHub calculates the score according to the [Common Vulnerability Scoring System Calculator](https://www.first.org/cvss/calculator).
  10. Under "Weaknesses", in the **Common weakness enumerator** field, type common weakness enumerators (CWEs) that describe the kinds of security weaknesses that this security advisory reports. For a full list of CWEs, see the [Common Weakness Enumeration](https://cwe.mitre.org/index.html) from MITRE.
  11. Optionally, under "Credits", remove existing credits, or use the search box to find additional people you want to credit on the security advisory, then click their username to add them.
     * Use the dropdown menu next to the name of the person you're crediting to assign a credit type. For more information about credit types, see [Creating a repository security advisory](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/creating-a-repository-security-advisory#about-credits-for-repository-security-advisories).
![Screenshot of a draft security advisory. A dropdown menu, labeled "Choose a credit type," is highlighted with an orange outline.](https://docs.github.com/assets/cb-21132/images/help/security/security-advisories-choose-credit-type.png)
     * Optionally, to remove someone, click the 
  12. Click **Update security advisory**.


The people listed in the "Credits" section will receive an email or web notification inviting them to accept credit. If a person accepts, their username will be publicly visible once the security advisory is published.
## [Further reading](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/editing-a-repository-security-advisory#further-reading)
  * [Deleting a repository security advisory](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/deleting-a-repository-security-advisory)


