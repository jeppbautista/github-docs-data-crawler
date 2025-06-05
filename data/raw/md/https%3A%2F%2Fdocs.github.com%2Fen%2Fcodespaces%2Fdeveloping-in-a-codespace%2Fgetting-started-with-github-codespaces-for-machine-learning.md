  * [Codespaces](https://docs.github.com/en/codespaces "Codespaces")/
  * [Developing in a codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace "Developing in a codespace")/
  * [Machine learning](https://docs.github.com/en/codespaces/developing-in-a-codespace/getting-started-with-github-codespaces-for-machine-learning "Machine learning")


# Getting started with GitHub Codespaces for machine learning
Learn about working on machine learning projects with GitHub Codespaces and its out-of-the-box tools.
## In this article
  * [Introduction](https://docs.github.com/en/codespaces/developing-in-a-codespace/getting-started-with-github-codespaces-for-machine-learning#introduction)
  * [Building a simple image classifier](https://docs.github.com/en/codespaces/developing-in-a-codespace/getting-started-with-github-codespaces-for-machine-learning#building-a-simple-image-classifier)
  * [Opening your codespace in JupyterLab](https://docs.github.com/en/codespaces/developing-in-a-codespace/getting-started-with-github-codespaces-for-machine-learning#opening-your-codespace-in-jupyterlab)
  * [Configuring NVIDIA CUDA for your codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/getting-started-with-github-codespaces-for-machine-learning#configuring-nvidia-cuda-for-your-codespace)


## [Introduction](https://docs.github.com/en/codespaces/developing-in-a-codespace/getting-started-with-github-codespaces-for-machine-learning#introduction)
This guide introduces you to machine learning with GitHub Codespaces. You’ll build a simple image classifier, learn about some of the tools that come preinstalled in GitHub Codespaces, and find out how to open your codespace in JupyterLab.
## [Building a simple image classifier](https://docs.github.com/en/codespaces/developing-in-a-codespace/getting-started-with-github-codespaces-for-machine-learning#building-a-simple-image-classifier)
We'll use a Jupyter notebook to build a simple image classifier.
Jupyter notebooks are sets of cells that you can execute one after another. The notebook we'll use includes a number of cells that build an image classifier using [PyTorch](https://pytorch.org/). Each cell is a different phase of that process: download a dataset, set up a neural network, train a model, and then test that model.
We'll run all of the cells, in sequence, to perform all phases of building the image classifier. When we do this Jupyter saves the output back into the notebook so that you can examine the results.
### [Creating a codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/getting-started-with-github-codespaces-for-machine-learning#creating-a-codespace)
  1. Go to the [github/codespaces-jupyter](https://github.com/github/codespaces-jupyter) template repository.
  2. Click **Use this template** , then click **Open in a codespace**.
![Screenshot of the "Use this template" button and the dropdown menu expanded to show the "Open in a codespace" option.](https://docs.github.com/assets/cb-76823/images/help/repository/use-this-template-button.png)


A codespace for this template will open in a web-based version of Visual Studio Code.
### [Opening the image classifier notebook](https://docs.github.com/en/codespaces/developing-in-a-codespace/getting-started-with-github-codespaces-for-machine-learning#opening-the-image-classifier-notebook)
The default container image that's used by GitHub Codespaces includes a set of machine learning libraries that are preinstalled in your codespace. For example, Numpy, pandas, SciPy, Matplotlib, seaborn, scikit-learn, Keras, PyTorch, Requests, and Plotly. For more information about the default image, see [Introduction to dev containers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers#using-the-default-dev-container-configuration) and the [devcontainers/images](https://github.com/devcontainers/images/tree/main/src/universal) repository.
  1. In the VS Code editor, close any "Get Started" tabs that are displayed.
  2. Open the `notebooks/image-classifier.ipynb` notebook file.


### [Building the image classifier](https://docs.github.com/en/codespaces/developing-in-a-codespace/getting-started-with-github-codespaces-for-machine-learning#building-the-image-classifier)
The image classifier notebook contains all the code you need to download a dataset, train a neural network, and evaluate its performance.
  1. Click **Run All** to execute all of the notebook’s cells.
![Screenshot of the top of the editor tab for the "image-classifier.ipynb" file. A cursor hovers over a button labeled "Run All."](https://docs.github.com/assets/cb-22183/images/help/codespaces/jupyter-run-all.png)
  2. If you are prompted to choose a kernel source, select **Python Environments** , then select the version of Python at the recommended location.
![Screenshot of the "Select a Python Environment" dropdown. The first option in the list of Python versions is labeled "Recommended."](https://docs.github.com/assets/cb-51563/images/help/codespaces/jupyter-choose-python.png)
  3. Scroll down to view the output of each cell.
![Screenshot of the cell in the editor, with the header "Step 3: Train the network and save model."](https://docs.github.com/assets/cb-120492/images/help/codespaces/jupyter-notebook-step3.png)


## [Opening your codespace in JupyterLab](https://docs.github.com/en/codespaces/developing-in-a-codespace/getting-started-with-github-codespaces-for-machine-learning#opening-your-codespace-in-jupyterlab)
You can open your codespace in JupyterLab from the "Your codespaces" page at [github.com/codespaces](https://github.com/codespaces), or by using GitHub CLI. For more information, see [Opening an existing codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/opening-an-existing-codespace).
The JupyterLab application must be installed in the codespace you are opening. The default dev container image includes JupyterLab, so codespaces created from the default image will always have JupyterLab installed. For more information about the default image, see [Introduction to dev containers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers#using-the-default-dev-container-configuration) and the [`devcontainers/images`](https://github.com/devcontainers/images/tree/main/src/universal) repository. If you're not using the default image in your dev container configuration, you can install JupyterLab by adding the `ghcr.io/devcontainers/features/python` feature to your `devcontainer.json` file. You should include the option `"installJupyterlab": true`. For more information, see the README for the [`python`](https://github.com/devcontainers/features/tree/main/src/python#python-python) feature, in the `devcontainers/features` repository.
## [Configuring NVIDIA CUDA for your codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/getting-started-with-github-codespaces-for-machine-learning#configuring-nvidia-cuda-for-your-codespace)
This section only applies to customers who can create codespaces on machines that use a GPU. The ability to choose a machine type that uses a GPU was offered to selected customers during a trial period. This option is not generally available.
Some software requires you to install NVIDIA CUDA to use your codespace’s GPU. Where this is the case, you can create your own custom configuration, by using a `devcontainer.json` file, and specify that CUDA should be installed. For more information on creating a custom configuration, see [Introduction to dev containers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers#creating-a-custom-dev-container-configuration).
For full details of the script that's run when you add the `nvidia-cuda` feature, see the [devcontainers/features](https://github.com/devcontainers/features/tree/main/src/nvidia-cuda) repository.
  1. Within the codespace, open the `.devcontainer/devcontainer.json` file in the editor.
  2. Add a top-level `features` object with the following contents:
JSON```
  "features": {
    "ghcr.io/devcontainers/features/nvidia-cuda:1": {
      "installCudnn": true
    }
  }

```
```
  "features": {
    "ghcr.io/devcontainers/features/nvidia-cuda:1": {
      "installCudnn": true
    }
  }

```

For more information about the `features` object, see the [development containers specification](https://containers.dev/implementors/features/#devcontainer-json-properties).
If you are using the `devcontainer.json` file from the image classifier repository you created for this tutorial, your `devcontainer.json` file will now look like this:
```
{
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-toolsai.jupyter"
      ]
    }
  },
  "features": {
    "ghcr.io/devcontainers/features/nvidia-cuda:1": {
      "installCudnn": true
    }
  }
}

```

  3. Save the change.
  4. Access the VS Code Command Palette (`Shift`+`Command`+`P` / `Ctrl`+`Shift`+`P`), then start typing "rebuild". Click **Codespaces: Rebuild Container**.
![Screenshot of the Command Palette with a search for "rebuild container" and the "Codespace: Rebuild Container" option highlighted in the dropdown.](https://docs.github.com/assets/cb-22518/images/help/codespaces/codespaces-rebuild.png)
You may occasionally want to perform a full rebuild to clear your cache and rebuild your container with fresh images. For more information, see [Rebuilding the container in a codespace](https://docs.github.com/en/codespaces/developing-in-codespaces/rebuilding-the-container-in-a-codespace#about-rebuilding-a-container). The codespace container will be rebuilt. This will take several minutes. When the rebuild is complete the codespace is automatically reopened.
  5. Publish your change to a repository so that CUDA will be installed in any new codespaces you create from this repository in future. For more information, see [Creating a codespace from a template](https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-from-a-template#publishing-from-vs-code).


