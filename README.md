![BuildStatus](https://github.com/bmi203-2023/Minimal-Example/actions/workflows/main.yml/badge.svg?event=push)
[![Documentation Status](https://readthedocs.org/projects/minimal-example/badge/?version=latest)](https://minimal-example.readthedocs.io/en/latest/?badge=latest)

# Minimal-Viable-Package
Demonstrate the minimal concepts/training to structure a project, build Python packages, unit testing, GitHub Actions, package managers, distributions, containers, and Read the Docs. We intend the README/Tutorial suggestions to be read and followed linearly.

## Project Structure
A minimal example of a **complete** Python package's working directory, will look like something below. In this README tutorial, we'll review how to build this as hassle free (as we're aware of).

```bash
Minimal-Viable-Package # Working Directory
├── README.md
├── data # A data directory for any relevant data used for unit testing, training, etc.
│   └── the-zen-of-python.txt
├── docs # This makes the module's ReadTheDocs.
│   ├── Makefile
│   ├── build
│   ├── make.bat
│   └── source
│       ├── _static
│       ├── _templates
│       ├── conf.py
│       ├── example.rst
│       ├── index.rst
│       └── modules.rst
├── pyproject.toml # Definition of build process of the package.
├── src # The src directory contains all of the source material for building the project.
│   └── example # The Python example package directory.
│       ├── __init__.py # This makes the directory a package.
│       └── welcome.py # The example's welcome module.
└── test # The test directory contains all of the unit testing material.
    └── test_greeting.py
```

You might notice a few files are missing, like the ones that start with a period. These are considered hidden folders in Unix-like operating systems, and in this README tutorial, we'll review the directory **.github** and the files **.gitignore** and **.readthedocs.yaml**.

For more references on **project directory** structure/organization for building a Python package, here are a few helpful links:
* [A Practical Guide to Setuptools and Pyproject.toml](https://godatadriven.com/blog/a-practical-guide-to-setuptools-and-pyproject-toml/)

## Building a Python Package

We can automate the majority of building a Python package, however, there are a few starting steps to consider. Here we'll outline the best practices (that again we're aware of) to simplify the process.

In this section of the tutorial, let's start from

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

Note: The mvp_env is shorthand for our minimal-viable-package environment.

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

```bash
$ git clone https://github.com/bmi203-2023/minimal-viable-package.git
$ cd env
$ conda env create -f environment.yml
```

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
$ flit install -s # builds your package in editable or development mode
```

**8. As you iteratively develop each module and submodule, consider your edge cases and design rationally explained unit tests to assess them. We suggest naming your unit tests by their associated module/submodule naming convention.**

```bash
$ cd minimal-viable-package
$ mkdir test
$ touch test_greeting.py # name the modules/submodule you're evaluating
```
In the next section, we'll review our unit test suggestions. At this point your working directory should look like this:

```bash
minimal-viable-package # Working Directory
├── README.md
├── data # A data directory for any relevant data used for unit testing, training, etc.
│   └── the-zen-of-python.txt
├── pyproject.toml # Definition of build process of the package.
├── src # The src directory contains all of the source material for building the project.
│   └── example # The Python example package directory.
│       ├── __init__.py # This makes the directory a package.
│       └── welcome.py # The example's welcome module.
└── test # The test directory contains all of the unit testing material.
    └── test_greeting.py
```
*Assuming you made and populated the data folder.*

To create a project directory tree as seen above for your README, please follow these commands:

```bash
$ cd minimal-viable-package
$ tree minimal-viable-package -o tree.md
```

For more references on Python packaging, here are a few helpful links:
* [Setting up a repository](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-init)
* [A pyproject.toml Developer's Cheat Sheet](https://betterprogramming.pub/a-pyproject-toml-developers-cheat-sheet-5782801fb3ed)

## Unit Testing
In our Minimal-Example unit test submodule example (e.g., the Greeting class in welcome.py or welcome.Greeting()), we evaluate class attributes and methods based on our set parameters and expectations. Please find the unit test [here](https://github.com/bmi203-2023/Minimal-Example/blob/master/test/test_greeting.py).

For more references on **unit testing** using **pytest**, here are a few helpful links:
* [pytest: helps you write better programs](https://docs.pytest.org/en/7.2.x/)

## GitHub Actions
Now that all of our configuration and recipe files have been made, we can automate our build and testing.

```yaml
# This is a basic workflow to help you get started with Actions
name: Minimal-Viable-Package

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

For more references related to **GitHub Actions**, here are a few helpful links:
* [Adding a workflow status badge](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge)

## Package Managers, Distributions, & Containers
* [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
* [Homebrew](https://brew.sh/)

## Read the Docs

## UCSF High Performance Computing (HPC) Resources
