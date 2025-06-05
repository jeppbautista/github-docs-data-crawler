  * [Organizations](https://docs.github.com/en/organizations "Organizations")/
  * [Manage organization settings](https://docs.github.com/en/organizations/managing-organization-settings "Manage organization settings")/
  * [Manage Pages site publication](https://docs.github.com/en/organizations/managing-organization-settings/managing-the-publication-of-github-pages-sites-for-your-organization "Manage Pages site publication")


# Managing the publication of GitHub Pages sites for your organization
You can control whether organization members can publish GitHub Pages sites from repositories in the organization.
## Who can use this feature?
Organization owners can manage the publication of GitHub Pages sites from repositories in the organization.
GitHub Pages is available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub’s plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans).
GitHub Pages now uses GitHub Actions to execute the Jekyll build. When using a branch as the source of your build, GitHub Actions must be enabled in your repository if you want to use the built-in Jekyll workflow. Alternatively, if GitHub Actions is unavailable or disabled, adding a `.nojekyll` file to the root of your source branch will bypass the Jekyll build process and deploy the content directly. For more information on enabling GitHub Actions, see [Managing GitHub Actions settings for a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository).
You can choose to allow or disallow organization members from publishing GitHub Pages sites. Organizations that use GitHub Enterprise Cloud can also choose to allow publicly published sites, privately published sites, both, or neither. For more information, see [the GitHub Enterprise Cloud documentation](https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/managing-the-publication-of-github-pages-sites-for-your-organization).
If you disallow publication of GitHub Pages sites, any sites that are already published will remain published. You can manually unpublish the site. For more information, see [Unpublishing a GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/unpublishing-a-github-pages-site).
  1. In the upper-right corner of GitHub, select your profile photo, then click 
  2. Next to the organization, click **Settings**.
  3. In the "Access" section of the sidebar, click 
  4. Under "Pages creation, select or deselect **Public**.
To publish a GitHub Pages site privately, your organization must use GitHub Enterprise Cloud. For more information about how you can try GitHub Enterprise Cloud for free, see [Setting up a trial of GitHub Enterprise Cloud](https://docs.github.com/en/enterprise-cloud@latest/admin/overview/setting-up-a-trial-of-github-enterprise-cloud).
  5. Click **Save**.


## [Further reading](https://docs.github.com/en/organizations/managing-organization-settings/managing-the-publication-of-github-pages-sites-for-your-organization#further-reading)
  * [What is GitHub Pages?](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages)


