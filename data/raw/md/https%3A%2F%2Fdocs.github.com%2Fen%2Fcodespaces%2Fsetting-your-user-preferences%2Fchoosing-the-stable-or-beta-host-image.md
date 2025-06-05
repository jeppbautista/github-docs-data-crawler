  * [Codespaces](https://docs.github.com/en/codespaces "Codespaces")/
  * [Setting your user preferences](https://docs.github.com/en/codespaces/setting-your-user-preferences "Setting your user preferences")/
  * [Choose the host image](https://docs.github.com/en/codespaces/setting-your-user-preferences/choosing-the-stable-or-beta-host-image "Choose the host image")


# Choosing the stable or beta host image
You can choose to build codespaces using either the stable or beta version of the host image for the underlying virtual machine.
## In this article
  * [About the virtual machine host image](https://docs.github.com/en/codespaces/setting-your-user-preferences/choosing-the-stable-or-beta-host-image#about-the-virtual-machine-host-image)
  * [Choosing the host image](https://docs.github.com/en/codespaces/setting-your-user-preferences/choosing-the-stable-or-beta-host-image#choosing-the-host-image)
  * [Further reading](https://docs.github.com/en/codespaces/setting-your-user-preferences/choosing-the-stable-or-beta-host-image#further-reading)


## [About the virtual machine host image](https://docs.github.com/en/codespaces/setting-your-user-preferences/choosing-the-stable-or-beta-host-image#about-the-virtual-machine-host-image)
A GitHub codespace is a development environment provided by a Docker container that runs on a virtual machine (VM). For more information about the relationship of the development container and the VM, see [Quickstart for GitHub Codespaces](https://docs.github.com/en/codespaces/quickstart#introduction).
The VM for a codespace is built using a host image that defines the operating system of the VM. The image is periodically upgraded to improve security, functionality, and performance. The upgraded host image is initially made available as a beta release and subsequently becomes the stable release after a period of testing. You can choose, in your personal settings, to use either the stable or beta version of the host image. Any codespace you create or resume after changing this setting will run on a VM built from the specified host image.
The stable image is the default selected setting. Changing the setting to the beta host image gives you early access to improvements and new features on the host VM, but may also introduce incompatibilities with your current dev container configuration. This gives you the opportunity to alter your dev container configuration to avoid problems before the beta image is promoted to the stable image. If you do encounter problems with the beta host image, you can switch back to the stable host image at any time.
  * It's unlikely you will encounter problems using the beta host image unless your dev container configuration has dependencies on components of the VM host kernel.
  * The virtual machine host image should not be confused with the dev container image, which provides the environment of your codespace. For more information, see [Restricting the base image for codespaces](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-base-image-for-codespaces#overview).


If you choose to use the beta host image but no beta image is currently available, your codespaces will be built using the stable host image.
For information about the current host image versions, including the date on which the current stable image will be replaced by the current beta image, see [the `github/codespaces-host-images` repository](https://github.com/github/codespaces-host-images/blob/main/README.md).
## [Choosing the host image](https://docs.github.com/en/codespaces/setting-your-user-preferences/choosing-the-stable-or-beta-host-image#choosing-the-host-image)
  1. In the upper-right corner of any page on GitHub, click your profile photo, then click 
  2. In the "Code, planning, and automation" section of the sidebar, click 
  3. Under "Host image version preference", select either **Stable** or **Beta**.
![Screenshot of the "Host image version preference" options, with "Stable" selected.](https://docs.github.com/assets/cb-64684/images/help/codespaces/host-image-choice.png)


## [Further reading](https://docs.github.com/en/codespaces/setting-your-user-preferences/choosing-the-stable-or-beta-host-image#further-reading)
  * [Customizing your codespace](https://docs.github.com/en/codespaces/customizing-your-codespace)
  * [Managing your codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces)


