![BuildStatus](https://github.com/bmi203-2023/Minimal-Example/actions/workflows/main.yml/badge.svg?event=push)
[![Documentation Status](https://readthedocs.org/projects/minimal-example/badge/?version=latest)](https://minimal-example.readthedocs.io/en/latest/?badge=latest)

# Minimal-Example
Demonstrate how to structure a project, build Python packages, unit testing, GitHub Actions, distributions & containers, and Read the Docs.

## Project Structure


```bash
Minimal-Example # Working Directory
├── README.md
├── data
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

Brew is a package manager for macOS. Please see the

## Building a Python Package

## Unit Testing

## GitHub Actions

## Package Managers, Distributions, & Containers

* [Homebrew](https://brew.sh/)

## Read the Docs

## UCSF High Performance Computing (HPC) Resources