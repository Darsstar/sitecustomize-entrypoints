[![Testing](https://img.shields.io/github/actions/workflow/status/Darsstar/sitecustomize-entrypoints/testing.yaml?branch=main&longCache=true&style=flat-square&label=tests&logo=GitHub%20Actions&logoColor=fff")](https://github.com/Darsstar/sitecustomize-entrypoints/actions/workflows/testing.yaml)
[![Linting](https://img.shields.io/github/actions/workflow/status/Darsstar/sitecustomize-entrypoints/linting.yaml?branch=main&longCache=true&style=flat-square&label=Linting&logo=GitHub%20Actions&logoColor=fff")](https://github.com/Darsstar/sitecustomize-entrypoints/actions/workflows/linting.yaml)
[![Read the Docs](https://readthedocs.org/projects/sitecustomize-entrypoints/badge/?version=latest)](https://sitecustomize-entrypoints.readthedocs.io/en/latest/)
[![PyPi Package](https://img.shields.io/pypi/v/sitecustomize-entrypoints?color=%2334D058&label=pypi%20package)](https://pypi.org/project/sitecustomize-entrypoints/)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/Darsstar/sitecustomize-entrypoints/blob/main/license.md)

# sitecustomize-entrypoints

A very simple library that makes a python module called `sitecustomize`
available. Python's [site](https://docs.python.org/3/library/site.html)
module gives it, and `usercustomize`, special treatment by importing it after
it is done looking for and processing .pth files.

What this package does is that is finds all `sitecustomize` entry points and,
if they are callable, calls them.