# Changelog

All notable changes to this project will be documented in this file.


## Unreleased (YYYY-MM-DD)

- Add colorful badges to readme. [WouterVH]

- Add ``ruff`` as dev-dependency. [WouterVH]

- Add github-action for [testing](https://github.com/Darsstar/sitecustomize-entrypoints/actions/workflows/testing.yaml). [WouterVH]

- Add github-action for [linting](https://github.com/Darsstar/sitecustomize-entrypoints/actions/workflows/linting.yaml). [WouterVH]

- Use a constant ``ENTRYPOINT_GROUPNAME``. [WouterVH]

- Add ``print_entrypoints``-function to easily output a list an registered entrypoints. [WouterVH]

- Add ``cancel``-function that you can use in your own ``pyproject.toml`` to
  override pre-existing entrypoints so you can re-order them. [WouterVH]

- Avoid executing a registered entrypoint more than once,
  even when it was registered multiple times. [WouterVH]

- Allow to set the order in your own ``pyproject.toml``, in which any registered entrypoint executed. [WouterVH]

- Display warnings in a simplified format. [WouterVH]

- Add changelog. [WouterVH]

- Add license. [WouterVH]

- Complete project-metadata in ``pyproject.toml``. [WouterVH]

- Avoid breaking when a registered entrypoint throws an ``AttributeError``. [WouterVH]


## 1.0.0 (2023-03-10)

- Avoid breaking when a registered entrypoint throws an error when executed [WouterVH]

- Avoid breaking when a registered entrypoint cannot be found,  e.g. renamed function. [WouterVH]


## 0.1.0 (2022-04-19)

- Package created by [Dos Moonen <d.moonen@nki.nl>]
