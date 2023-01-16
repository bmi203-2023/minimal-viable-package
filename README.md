![BuildStatus](https://github.com/bmi203-2023/minimal-viable-package/actions/workflows/main.yml/badge.svg?event=push)
[![Documentation Status](https://readthedocs.org/projects/minimal-viable-package/badge/?version=latest)](https://minimal-viable-package.readthedocs.io/en/latest/?badge=latest)

# Minimal-Viable-Package
Demonstrate the minimal concepts/training to structure a project, build Python packages, unit testing, GitHub Actions, Read the Docs (RTD), package managers, distributions, containers, and high performance computing (HPC). We intend the README tutorial suggestions to be read and followed linearly.

## Project Structure
A minimal example of a **complete** Python package's working directory, will look like something below. In this README tutorial, we'll review how to build this as hassle free (as we're aware of).

```bash
minimal-viable-package # The working directory
├── README.md
├── data # A data directory for any relevant data used for unit testing your package, training a model, etc.
│   └── the-zen-of-python.txt
├── docs  # This makes the module's ReadTheDocs (RTD).
│   ├── Makefile
│   ├── build
│   ├── make.bat
│   └── source
│       ├── _static
│       ├── _templates
│       ├── conf.py # RTD configuration file
        # The reStructuredText (RST) file format is for textual data used in Python programming for documention.
│       ├── example.rst # The Python package's module and submodule API documentation. The file is named after the module.
│       ├── index.rst
│       └── modules.rst
├── env # The environment directory for sharing and reproducing the Python package or model. 
│   └── mvp_env.yml
├── pyproject.toml # Definition of the build process for the package.
├── src # The src directory contains all of the source material for building the project.
│   └── example # The Python example package directory.
│       ├── __init__.py # This makes the directory a package.
│       └── welcome.py # The example's welcome module.
└── test # The test directory contains all of the unit testing material.
    └── test_greeting.py # A unit test for the example.welcome submodule greeting
```

You might notice a few files are missing, like the ones that start with a period. These are considered hidden folders in Unix-like operating systems, and in this README tutorial, we'll review the directory **.github** and the files **.gitignore** and **.readthedocs.yaml**.

For more references on **project directory** structure/organization for building a Python package, here are a few helpful links:
* [A Practical Guide to Setuptools and Pyproject.toml](https://godatadriven.com/blog/a-practical-guide-to-setuptools-and-pyproject-toml/)

## Building a Python Package

We can automate the majority of building a Python package, however, there are a few starting steps to consider. Here we'll outline the best practices (that again we're aware of) to simplify the process.

In this section of the README tutorial, we're going to review the minimal steps to create this repository from scratch.

**1. Create a repository**

```bash
$ mkdir minimal-viable-package
$ cd minimal-viable-package
$ git init
$ touch README.md
$ echo "# Minimal-Viable-Package" > README.md
$ git add README.md
$ git commit -m "Initial commit with README"
$ git push
```
**2. Install conda**

**3. Create a clean environment and activate it.**

```bash
$ conda create --name mvp_env python=3.9
$ conda activate mvp_env
```

**Note:** The mvp_env is shorthand for our minimal-viable-package environment.

**4. Install the minimal depedencies for unit testing and building our documentation.**

Here's how we would install each dependency individually:

```bash
(mvp_env)$ conda install -c conda-forge flit
(mvp_env)$ conda install -c conda-forge tree
(mvp_env)$ conda install -c anaconda sphinx
(mvp_env)$ conda install -c conda-forge sphinx_rtd_theme
```

Now that we have a minimal environment for our package, let's export the dependencies to a **yml** file, so we don't have to do this again.

```bash
(mvp_env)$ cd minimal-viable-package
(mvp_env)$ mkdir env # Create an (env)ironment directory for our package to help make it more reproducible
(mvp_env)$ cd env
(mvp_env)$ conda env export -n mvp_env > mvp_env.yml
```

For example, if you cloned this repository and had conda installed, here's how you would create the environment.

```bash
$ git clone https://github.com/bmi203-2023/minimal-viable-package.git
$ cd env
$ conda env create -f environment.yml
$ conda activate mvp_env
$ conda deactivate mvp_env # how to deactivate the conda environment
```
**Note**: Keeping the mvp_env activate is not necessary for this tutorial's entire build and test cycle. We will specify when to activate the environment. You can leave the environment activated unless you're installing/testing/developing other Python libraries. Otherwise, we suggest deactivating the environment.

**5. Create a pyproject.toml in the working directory that specifies the package's build system.**

Using the terminal or your favorite IDE, please follow these steps:

```bash
$ touch pyproject.toml
$ vim pyproject.toml 
```

Copy/Paste and update the relevant fields with <**your info**>.

```python
[build-system]
requires = [
	"flit_core >=3.2,<4",
	"python_version >= '3.9'"
	]
build-backend = "flit_core.buildapi"

[project]
name = "<your name>"
authors = [{name = "<name>", email = "<email>"}]
license = {file = "LICENSE"}
classifiers = ["License :: OSI Approved :: MIT License"]
dynamic = ["version", "description"]
dependencies = ["pytest", "numpy", "scipy", "matplotlib", "scikit-learn", "sphinx"]

[tool.coverage.run]
source = ["src"] # parent directory of package

[project.urls]
Home = "https://github.com/<your git handle or organization>/<repository name>"
```

**6. Create a source directory for your package and modules.**

```bash
$ mkdir src
$ cd src
$ mkdir example
$ cd example
$ touch __init__.py
$ touch welcome.py
```

**7. Iteratively develop your package and modules. See this repository's simple example [here](https://github.com/bmi203-2023/Minimal-Example/tree/master/src/example).**

```bash
$ cd minimal-viable-package
$ conda activate mvp_env
(mvp_env)$ flit install -s # builds your package in editable or development mode
$ conda deactivate mvp_env
```

**8. As you iteratively develop each module and submodule, consider your edge cases and design rationally explained unit tests to assess them. We suggest naming your unit tests by their associated module and their test functions as the submodule you're evaluating.**

```bash
$ cd minimal-viable-package
$ mkdir test
$ touch test_greeting.py # name the modules/submodule you're evaluating
```
In the next section, we'll review our unit test suggestions. At this point your working directory should look like this:

```bash
minimal-viable-package # The working directory
├── README.md
├── data # A data directory for any relevant data used for unit testing your package, training a model, etc.
│   └── the-zen-of-python.txt
├── env # The environment directory for sharing and reproducing the Python package or model. 
│   └── mvp_env.yml
├── pyproject.toml # Definition of the build process for the package.
├── src # The src directory contains all of the source material for building the project.
│   └── example # The Python example package directory.
│       ├── __init__.py # This makes the directory a package.
│       └── welcome.py # The example's welcome module.
└── test # The test directory contains all of the unit testing material.
    └── test_greeting.py # A unit test for the example.welcome submodule greeting
```
*Assuming you made and populated the data folder.*

To create a project directory tree as seen above for your README, please follow these commands:

```bash
$ cd minimal-viable-package
$ tree minimal-viable-package -o minimal-viable-package/tree.md
```

For this tutorial, we copied/pasted the contents of tree.md into this README and edited accordingly.

For more references on Python packaging, here are a few helpful links:
* [Setting up a repository](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-init)
* [A pyproject.toml Developer's Cheat Sheet](https://betterprogramming.pub/a-pyproject-toml-developers-cheat-sheet-5782801fb3ed)

## Unit Testing
In our minimal-viable-package unit test submodule example (e.g., the Greeting class in welcome.py or welcome.Greeting()), we evaluate class attributes and methods based on our set parameters and expectations. Please find the unit test [here](https://github.com/bmi203-2023/Minimal-Example/blob/master/test/test_greeting.py).

For more references on **unit testing** using **pytest**, here are a few helpful links:
* [pytest: helps you write better programs](https://docs.pytest.org/en/7.2.x/)

## GitHub Actions
Now that all of our configuration and recipe files have been made, we can automate our build and testing.

**1. Create a .github/workflows directory tree.**

```bash
$ cd minimal-viable-package
$ mkdir .github
$ cd .github
$ mkdir workflows
```

**2. Create a yet another markup language (YAML) file and specify the commands to run whenever your code is pushed to the repository (i.e, unit tests, RTD, etc.).**

```bash
$ cd minimal-viable-project/.github/workflows
$ touch main.yml
$ vim main.yml
```

Copy/Paste and update the relevant fields with <**your info**>.

```yaml
# This is a basic workflow to help you get started with Actions
name: <your package's name>

# Controls when the workflow will run
on:
  # Triggers the workflow on push or pull request events but only for the main branch
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - uses: actions/checkout@v2
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install .
      
      - name: Run unit tests
        run: python -m pytest -v test/*
```

**3. Add a workflow status badge to your README to indicate if you're failing or passing.**

```bash
$ cd minimal-viable-project
$ vim REAMD.md
```
Copy/Paste and update the relevant fields with <**your info**>.

```markdown
![BuildStatus](https://github.com/<your githandle>/<your repository name>/actions/workflows/main.yml/badge.svg?event=push)
```

**4. Push your commits and then check if your workflow badge indicates passing.**

You've now specified the minimal requirements to automate the build and test cycle for your software package. Congrats!

For more references related to **GitHub Actions**, here are a few helpful links:
* [Understanding GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions)
* [Adding a workflow status badge](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge)

## Read the Docs

Read the Docs (RTD) is a software documentation service for automating the building, version control, and hosting of your software's documentation. In this section of the README tutorial, we'll review how we built the RTD for the minimal-viable-package's example module.

**1. Create a RTD account and link your GitHub account.**
* [ReadtheDocs](https://readthedocs.org/)

**2. Create the RTD directory for your Python package.**

Update the relevant fields with <**your info**>.

```bash
$ cd minimal-viable-example
$ conda activate mvp_env
(mvp_env)$ mkdir docs
(mvp_env)$ cd docs
(mvp_env)$ sphinx-quickstart

Welcome to the Sphinx 4.4.0 quickstart utility.

Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets).

Selected root path: .

You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]: y

The project name will occur in several places in the built documentation.
> Project name: <Minimal Viable Project>
> Author name(s): <Andrew Blair>
> Project release []: <0.1.0>

If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
> Project language [en]: 

Creating file (RTD will automate the full path to) minimal-viable-package/docs/source/conf.py.
Creating file (RTD will automate the full path to) minimal-viable-package/docs/source/index.rst.
Creating file (RTD will automate the full path to) minimal-viable-package/docs/Makefile.
Creating file (RTD will automate the full path to) minimal-viable-package/docs/make.bat.

Finished: An initial directory structure has been created.

You should now populate your master file  (RTD will automate the full path to) minimal-viable-package/docs/source/index.rst and create other documentation
source files. Use the Makefile to build the docs, like so:
   make builder
where "builder" is one of the supported builders, e.g. html, latex or linkcheck.
```

Let's review the most important folder/files RTD autogenerated for us in the **docs** directory:

```bash
docs
├── Makefile
├── build
├── make.bat
└── source # The directory where all our .rst files and configuration files will reside.
    ├── _static
    ├── _templates 
    ├── conf.py # The configuration file where all Sphinx settings are specified and ran to extract/build our desired configuration.
    ├── index.rst # The file that tells Sphinx how to render our front index page.
```

Before we build our documentation, we need to update **conf.py**.

**3. Update the theme and autodoc configuration settings in conf.py.**

```bash
$ cd minimal-viable-package/docs/source
$ vim conf.py
```

In **conf.py**, modify the following configuration variable:

```python
html_theme = 'sphinx_rtd_theme'
```

Next, if we want Sphinx to autogenerate our package's documentation from our code using the **autodoc** extension, we need to point Sphinx to the directory our Python package's source code. We'll do this by adding the following lines of code to the top of **conf.py**.

```python
import os
import sys

sys.path.insert(0, os.path.abspath('../../src/example'))
```



For more references related to **Sphinx-RTD-Tutorial**, here are a few helpful links:
* [Read the Docs Tutorial](https://docs.readthedocs.io/en/stable/tutorial/index.html)
* [Sphinx-RTD-Tutorial](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/sphinx-quickstart.html)
* [Sphinx Theme](https://sphinx-rtd-theme.readthedocs.io/en/stable/)
* [Sphinx.ext.autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#module-sphinx.ext.autodoc)
## Package Managers, Distributions, & Containers

* [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
* [Homebrew](https://brew.sh/)
* [Docker](https://www.docker.com/products/docker-desktop/)
* [Singularity](https://sylabs.io/)

## UCSF High Performance Computing (HPC) Resources

