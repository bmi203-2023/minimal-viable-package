![BuildStatus](https://github.com/bmi203-2023/Minimal-Example/actions/workflows/main.yml/badge.svg?event=push)
[![Documentation Status](https://readthedocs.org/projects/minimal-example/badge/?version=latest)](https://minimal-example.readthedocs.io/en/latest/?badge=latest)

# Minimal-Example
Demonstrate the minimal concepts/training to structure a project, build Python packages, unit testing, GitHub Actions, package managers, distributions, containers, and Read the Docs.

## Project Structure
A minimal example of a **complete** Python package's working directory, will look like something below. In this README tutorial, we'll review how to build this as hassle free (as we're aware of).

```bash
Minimal-Example # Working Directory
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
To create a project directory tree as seen above for your README, please follow these commands:

```bash
$ brew install tree
$ tree Minimal-Example -o tree.md
```
For more references on project directory structure/organization, here are a few helpful links:
* [A Practical Guide to Setuptools and Pyproject.toml](https://godatadriven.com/blog/a-practical-guide-to-setuptools-and-pyproject-toml/)

## Building a Python Package

We can automate the majority of building a Python package, however, there are a few starting steps to consider. Here we'll outline the best practices (that again we're aware of) to simplify the process.

**1. Create a repository**

```bash
$ mkdir Minimal-Example
$ cd Minimal-Example
$ git init
$ touch README.md
$ echo "# Minimal-Example" > README.md
$ git add README.md
$ git commit -m "Initial commit with README"
$ git push
```
**2. Install conda**

**3. Create a clean environment and activate it.**

```bash
$ conda create --name minimal_example python=3.9
$ conda activate minimal_example
```

**4. Install the minimal depedency flit for unit testing.**

```bash
(minimal_example)$ conda install -c conda-forge flit
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

**8. As you iteratively develop each module and submodule, consider your edge cases and design rationally explained unit tests to assess them. We suggest naming your unit tests by their associated module/submodule naming convention.**

```bash
$ cd Minimal-Example
$ mkdir test
$ touch test_greeting.py # name the modules/submodule you're evaluating
```
In the next section, we'll review our unit test suggestions.

For more references on Python packaging, here are a few helpful links:
* [Setting up a repository](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-init)
* [A pyproject.toml Developer's Cheat Sheet](https://betterprogramming.pub/a-pyproject-toml-developers-cheat-sheet-5782801fb3ed)

## Unit Testing


## GitHub Actions


## Package Managers, Distributions, & Containers

* [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
* [Homebrew](https://brew.sh/)

## Read the Docs

## UCSF High Performance Computing (HPC) Resources