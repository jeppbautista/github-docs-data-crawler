  * [Secure coding](https://docs.github.com/en/code-security "Secure coding")/
  * [Security advisories](https://docs.github.com/en/code-security/security-advisories "Security advisories")/
  * [Global security advisories](https://docs.github.com/en/code-security/security-advisories/working-with-global-security-advisories-from-the-github-advisory-database "Global security advisories")/
  * [About the GitHub Advisory database](https://docs.github.com/en/code-security/security-advisories/working-with-global-security-advisories-from-the-github-advisory-database/about-the-github-advisory-database "About the GitHub Advisory database")


# About the GitHub Advisory database
The GitHub Advisory Database contains a list of known security vulnerabilities and malware, grouped in three categories: GitHub-reviewed advisories, unreviewed advisories, and malware advisories.
## In this article
  * [About the GitHub Advisory Database](https://docs.github.com/en/code-security/security-advisories/working-with-global-security-advisories-from-the-github-advisory-database/about-the-github-advisory-database#about-the-github-advisory-database)
  * [About types of security advisories](https://docs.github.com/en/code-security/security-advisories/working-with-global-security-advisories-from-the-github-advisory-database/about-the-github-advisory-database#about-types-of-security-advisories)
  * [About information in security advisories](https://docs.github.com/en/code-security/security-advisories/working-with-global-security-advisories-from-the-github-advisory-database/about-the-github-advisory-database#about-information-in-security-advisories)
  * [Further reading](https://docs.github.com/en/code-security/security-advisories/working-with-global-security-advisories-from-the-github-advisory-database/about-the-github-advisory-database#further-reading)


## [About the GitHub Advisory Database](https://docs.github.com/en/code-security/security-advisories/working-with-global-security-advisories-from-the-github-advisory-database/about-the-github-advisory-database#about-the-github-advisory-database)
We add advisories to the GitHub Advisory Database from the following sources:
  * Security advisories reported on GitHub
  * The [National Vulnerability database](https://nvd.nist.gov/)
  * The [npm Security advisories database](https://github.com/advisories?query=type%3Areviewed+ecosystem%3Anpm)
  * The [FriendsOfPHP database](https://github.com/FriendsOfPHP/security-advisories)
  * The [Go Vulncheck database](https://pkg.go.dev/vuln/)
  * The [Python Packaging Advisory database](https://github.com/pypa/advisory-database)
  * The [Ruby Advisory database](https://rubysec.com/)
  * The [RustSec Advisory database](https://rustsec.org/)
  * Community contributions. For more information, see <https://github.com/github/advisory-database/pulls>.


If you know of another database we should be importing advisories from, tell us about it by opening an issue in <https://github.com/github/advisory-database>.
Security advisories are published as JSON files in the Open Source Vulnerability (OSV) format. For more information about the OSV format, see [Open Source Vulnerability format](https://ossf.github.io/osv-schema/).
## [About types of security advisories](https://docs.github.com/en/code-security/security-advisories/working-with-global-security-advisories-from-the-github-advisory-database/about-the-github-advisory-database#about-types-of-security-advisories)
Each advisory in the GitHub Advisory Database is for a vulnerability in open source projects or for malicious open source software.
A vulnerability is a problem in a project's code that could be exploited to damage the confidentiality, integrity, or availability of the project or other projects that use its code. Vulnerabilities vary in type, severity, and method of attack. Vulnerabilities in code are usually introduced by accident and fixed soon after they are discovered. You should update your code to use the fixed version of the dependency as soon as it is available.
In contrast, malicious software, or malware, is code that is intentionally designed to perform unwanted or harmful functions. The malware may target hardware, software, confidential data, or users of any application that uses the malware. You need to remove the malware from your project and find an alternative, more secure replacement for the dependency.
### [GitHub-reviewed advisories](https://docs.github.com/en/code-security/security-advisories/working-with-global-security-advisories-from-the-github-advisory-database/about-the-github-advisory-database#github-reviewed-advisories)
GitHub-reviewed advisories are security vulnerabilities that have been mapped to packages in ecosystems we support. We carefully review each advisory for validity and ensure that they have a full description, and contain both ecosystem and package information.
Generally, we name our supported ecosystems after the software programming language's associated package registry. We review advisories if they are for a vulnerability in a package that comes from a supported registry.
  * Composer (registry: <https://packagist.org/>)
  * Erlang (registry: <https://hex.pm/>)
  * Go (registry: <https://pkg.go.dev/>)
  * GitHub Actions (<https://github.com/marketplace?type=actions/>)
  * Maven (registry: <https://repo.maven.apache.org/maven2>)
  * Npm (registry: <https://www.npmjs.com/>)
  * NuGet (registry: <https://www.nuget.org/>)
  * Pip (registry: <https://pypi.org/>)
  * Pub (registry: <https://pub.dev/packages/registry>)
  * RubyGems (registry: <https://rubygems.org/>)
  * Rust (registry: <https://crates.io/>)
  * Swift (registry: N/A)


If you have a suggestion for a new ecosystem we should support, please open an [issue](https://github.com/github/advisory-database/issues) for discussion.
If you enable Dependabot alerts for your repositories, you are automatically notified when a new GitHub-reviewed advisory reports a vulnerability for a package you depend on. For more information, see [About Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts).
### [Unreviewed advisories](https://docs.github.com/en/code-security/security-advisories/working-with-global-security-advisories-from-the-github-advisory-database/about-the-github-advisory-database#unreviewed-advisories)
Unreviewed advisories are security vulnerabilities that we publish automatically into the GitHub Advisory Database, directly from the National Vulnerability Database feed.
Dependabot doesn't create Dependabot alerts for unreviewed advisories as this type of advisory isn't checked for validity or completion.
### [Malware advisories](https://docs.github.com/en/code-security/security-advisories/working-with-global-security-advisories-from-the-github-advisory-database/about-the-github-advisory-database#malware-advisories)
Malware advisories relate to vulnerabilities caused by malware, and are security advisories that GitHub publishes automatically into the GitHub Advisory Database, directly from information provided by the npm security team. Malware advisories are exclusive to the npm ecosystem. GitHub doesn't edit or accept community contributions on these advisories.
Dependabot doesn't generate alerts when malware is detected as most of the vulnerabilities cannot be resolved by downstream users. You can view malware advisories by searching for `type:malware` in the GitHub Advisory Database.
Our malware advisories are mostly about substitution attacks. During this type of attack, an attacker publishes a package to the public registry with the same name as a dependency that users rely on from a third party or private registry, with the hope that the malicious version is consumed. Dependabot doesn’t look at project configurations to determine if the packages are coming from a private registry, so we aren't sure if you're using the malicious version or a non-malicious version. Users who have their dependencies appropriately scoped should not be affected by malware.
## [About information in security advisories](https://docs.github.com/en/code-security/security-advisories/working-with-global-security-advisories-from-the-github-advisory-database/about-the-github-advisory-database#about-information-in-security-advisories)
In this section, you can find more detailed information about specific data attributes of the GitHub Advisory Database.
### [About GHSA IDs](https://docs.github.com/en/code-security/security-advisories/working-with-global-security-advisories-from-the-github-advisory-database/about-the-github-advisory-database#about-ghsa-ids)
Each security advisory, regardless of its type, has a unique identifier referred to as a GHSA ID. A `GHSA-ID` qualifier is assigned when a new advisory is created on GitHub or added to the GitHub Advisory Database from any of the supported sources.
The syntax of GHSA IDs follows this format: `GHSA-xxxx-xxxx-xxxx` where:
  * `x` is a letter or a number from the following set: `23456789cfghjmpqrvwx`.
  * Outside the `GHSA` portion of the name: 
    * The numbers and letters are randomly assigned.
    * All letters are lowercase.


You can validate a GHSA ID using a regular expression.
Bash```
/GHSA(-[23456789cfghjmpqrvwx]{4}){3}/

```
```
/GHSA(-[23456789cfghjmpqrvwx]{4}){3}/

```

### [About CVSS levels](https://docs.github.com/en/code-security/security-advisories/working-with-global-security-advisories-from-the-github-advisory-database/about-the-github-advisory-database#about-cvss-levels)
The GitHub Advisory Database supports both CVSS version 3.1 and CVSS version 4.0.
Each security advisory contains information about the vulnerability or malware, which may include the description, severity, affected package, package ecosystem, affected versions and patched versions, impact, and optional information such as references, workarounds, and credits. In addition, advisories from the National Vulnerability Database list contain a link to the CVE record, where you can read more details about the vulnerability, its CVSS scores, and its qualitative severity level. For more information, see the [National Vulnerability Database](https://nvd.nist.gov/) from the National Institute of Standards and Technology.
The severity level is one of four possible levels defined in the [Common Vulnerability Scoring System (CVSS), Section 5](https://www.first.org/cvss/specification-document).
  * Low
  * Medium/Moderate
  * High
  * Critical


The GitHub Advisory Database uses the CVSS levels described above. If GitHub obtains a CVE, the GitHub Advisory Database uses the CVSS version assigned by the maintainer, which can be version 3.1 or 4.0. If the CVE is imported, the GitHub Advisory Database supports CVSS versions 4.0, 3.1 and 3.0.
You can also join [GitHub Security Lab](https://securitylab.github.com/) to browse security-related topics and contribute to security tools and projects.
### [About EPSS scores](https://docs.github.com/en/code-security/security-advisories/working-with-global-security-advisories-from-the-github-advisory-database/about-the-github-advisory-database#about-epss-scores)
The Exploit Prediction Scoring System, or EPSS, is a system devised by the global Forum of Incident Response and Security Teams (FIRST) for quantifying the likelihood of vulnerability exploit. The model produces a probability score between 0 and 1 (0 and 100%), where the higher the score, the greater the probability that a vulnerability will be exploited. For more information about FIRST, see <https://www.first.org/>.
The GitHub Advisory Database includes EPSS scores from FIRST for advisories containing CVEs with corresponding EPSS data. GitHub also displays the EPSS score percentile, which is the proportion of all scored vulnerabilities with the same or a lower EPSS score.
For example, if an advisory had an EPSS score that had a percentage of 90.534% at the 95th percentile, according to the [EPSS model](https://www.first.org/epss/model), this means that:
  * There is a 90.534% chance of this vulnerability being exploited in the wild in the next 30 days.
  * 95% of the total modeled vulnerabilities are considered less likely to be exploited in the next 30 days than this vulnerability.


Extended information about how to interpret this data can be found in FIRST's EPSS User Guide. This information helps you understand how both percentage and percentile can be used to interpret the likelihood that a vulnerability could be exploited in the wild according to FIRST's model. For more information, see the [FIRST's EPSS User Guide](https://www.first.org/epss/user-guide) on the FIRST website.
FIRST also provides additional information around the distribution of their EPSS data. For more information, see [EPSS data and statistics documentation](https://www.first.org/epss/data_stats) on the FIRST website.
GitHub keeps EPSS data up to date with a daily synchronization action. While EPSS score percentages will always be fully synchronized, score percentiles will only be updated when significantly different.
At GitHub, we do not author this data, but rather source it from FIRST, which means that this data is not editable in community contributions. For more information about community contributions, see [Editing security advisories in the GitHub Advisory Database](https://docs.github.com/en/code-security/security-advisories/working-with-global-security-advisories-from-the-github-advisory-database/editing-security-advisories-in-the-github-advisory-database).
## [Further reading](https://docs.github.com/en/code-security/security-advisories/working-with-global-security-advisories-from-the-github-advisory-database/about-the-github-advisory-database#further-reading)
  * [About Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts)
  * The CVE Program's [definition of "vulnerability"](https://www.cve.org/ResourcesSupport/Glossary#glossaryVulnerability)


