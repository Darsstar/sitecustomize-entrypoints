Changelog
=========
.. _changes:


Unreleased
----------
- Avoid executing a registered entrypoint more than once,
  even when it was registered multiple times. [WouterVH]

- Allow to set the order in your own ``pyproject.toml``, in which any registered entrypoint executed. [WouterVH]


1.0.0 (2023-03-10)
------------------

- Avoid breaking when a registered entrypoint throws an error when executed [WouterVH]

- Avoid breaking when a registered entrypoint cannot be found,  e.g. renamed function. [WouterVH]

0.1.0 (2022-04-19)
------------------

- Package created by [Dos Moonen <d.moonen@nki.nl>]