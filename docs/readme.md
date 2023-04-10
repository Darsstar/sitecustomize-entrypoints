[![Testing](https://img.shields.io/github/actions/workflow/status/Darsstar/sitecustomize-entrypoints/testing.yaml?branch=main&longCache=true&style=flat-square&label=tests&logo=GitHub%20Actions&logoColor=fff")](https://github.com/Darsstar/sitecustomize-entrypoints/actions/workflows/testing.yaml)
[![Linting](https://img.shields.io/github/actions/workflow/status/Darsstar/sitecustomize-entrypoints/linting.yaml?branch=main&longCache=true&style=flat-square&label=Linting&logo=GitHub%20Actions&logoColor=fff")](https://github.com/Darsstar/sitecustomize-entrypoints/actions/workflows/linting.yaml)
[![Read the Docs](https://readthedocs.org/projects/sitecustomize-entrypoints/badge/?version=latest)](https://sitecustomize-entrypoints.readthedocs.io/en/latest/)
[![PyPi Package](https://img.shields.io/pypi/v/sitecustomize-entrypoints?color=%2334D058&label=pypi%20package)](https://pypi.org/project/sitecustomize-entrypoints/)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/Darsstar/sitecustomize-entrypoints/blob/main/license.md)

# sitecustomize-entrypoints

## Overview

`sitecustomize-entrypoints` is a library that installs a python-module called `sitecustomize`,
and allows you to define and register any callable as a `sitecustomize`-entrypoint in your project's `setup.py` or `pyproject.toml`.

These callables will be then executed automatically whenever `sitecustomize` is imported during python-startup.
This provides a simple & modular way to patch or extend the functionality of any python-code installed in your environment without modifying its source code.

`sitecustomize` is a special python-module that can be used to customize the python environment at startup.
When the python-interpreter starts, it looks for a `sitecustomize.py`-file in the site-packages directory or any other directory specified in the `PYTHONPATH`.
The `sitecustomize.py`-file is executed before any other Python code, allowing you to make customizations that will be applied to the entire python environment.
For more information, check the official [site.py](https://docs.python.org/3/library/site.html)-documentation.



## Installation

You can install `sitecustomize-entrypoints` using pip:

```bash
> bin/pip install sitecustomize-entrypoints
```

Or add it to your poetry-based project:

```bash
> poetry add sitecustomize-entrypoints
```


## Usage

To use `sitecustomize-entrypoints`, you need to define and register one or more entrypoints
in your project's `setup.py` or `pyproject.toml` file. Here's an example:

```toml
[tool.poetry.plugins."sitecustomize"]
"my-action" = "my_project.action:my_action"
```

In this example, we're registering an entrypoint called `my-action` in the `sitecustomize`-group.
This entrypoint points to the `my_action`-function in the `my_project.actions`-module.

Once you've registered your entrypoints, they will be executed **automatically**
when the `sitecustomize`-module is imported.


```python

import sitecustomize
```


## Ordering

**Entrypoints are sorted by name.**

The ordering in which the entrypoints are defined in your `setup.py` or `pyproject.toml`
are unfortunately not the order in which they are registered internally.

The entrypoints are first ordered alphanumerically by name.

So defined entrypoints are re-ordered from
```toml
[tool.poetry.plugins."sitecustomize"]
foo = "my_project.action:action_foo"
bar = "my_project.action:action_bar"
```

into

```toml
[tool.poetry.plugins."sitecustomize"]
bar = "my_project.action:action_bar"
foo = "my_project.action:action_foo"
```

This can cause issues when there are dependencies between your entrypoints.

TIP: You can use integer-prefixes to the name to enforce the ordering in which you define your entrypoints.:

```toml
[tool.poetry.plugins."sitecustomize"]
10-foo = "my_project.action:action_foo"
20-bar = "my_project.action:action_bar"
```


## Cancel entrypoints registered by third-party packages

Imagine a third-party package has registered an entrypoint as follows:

```toml
[tool.poetry.plugins."sitecustomize"]
their-action = "external_module:their_action"
```

But it does not match the ordering you'd like.

You can cancel the execution of this plugin, by registering an entrypoint with the same name in your own `setup.py` or `pyproject.toml` file,
and pointing to the no-action `sitecustomize.cancel`-function.

```toml
[tool.poetry.plugins."sitecustomize"]
 their-action = "sitecustomize:cancel"
```

By registering an entrypoint with the **same name** it overrides the previous registered action.
Subsequently you can re-register this entrypoint by a different name to change the order of execution.


## Overriding and re-ordering entrypoints
You can override and re-order registered entrypoints by defining your own entrypoints with the same name in your setup.py or pyproject.toml file.
When `sitecustomize` executes registered entrypoints, it uses a FIFO-approach (first in, first out):
Only the last registered entrypoint with a given name is executed. Any prior entrypoints with the same name are filtered out (overriden by the last).

To re-order entrypoints, you can use the `cancel`-function provided by `sitecustomize-entrypoints`.
The `cancel`-function allows you to cancel out a previously registered entrypoint, so you can re-register it in a different order.

Here's an example to enforce a specific order of execution:


```toml
[tool.poetry.plugins."sitecustomize"]
"their-action = external_module:their_action"
```

```toml
[tool.poetry.plugins."sitecustomize"]
"their-action = sitecustomize:cancel"
"10-my-action = my_project.action:my_action"
"20-their-action = external_module:their_action"
```

In this example, we're re-ordering an entrypoint registered by a third-party module to be executed after our own.
First we re-register it with the same name to override and cancel its action, and subsequently we re-register it under a different name to ensure
it get executed after our own entrypoints, even if all entrypoints are sorted alphabetically



## Display all registered entrypoint in order of execution
The `sitecustomize.print_entrypoints`-function provided by `sitecustomize-entrypoints` allows you to display a list of all registered entrypoints.
By default, it will display all registered entrypoints in the `sitecustomize`-group in order of execution.
You can optionally pass a different entrypoint group name as an argument.
If you pass `filtered=True` as an argument, the function will also filter out any duplicate entrypoints and display only the last instance of each entrypoint. Here's an example usage:


```python

import sitecustomize

# Display all registered entrypoints in the sitecustomize group
sitecustomize.print_entrypoints()

# More explicit equivalent
sitecustomize.print_entrypoints(group_name="sitecustomize")

# Display only the first instance of each registered entrypoint in the sitecustomize group
sitecustomize.print_entrypoints(filtered=True)
```