"""sitecustomize."""

# poetry-dynamic-versioning substitutes this
__version__ = "0.0.0"
__version_tuple__ = (0, 0, 0)

import warnings

from sitecustomize._utils import SimpleWarning, fifo_filter
from sitecustomize._vendor.importlib_metadata import entry_points

ENTRYPOINT_GROUPNAME = "sitecustomize"

with SimpleWarning():
    eps = entry_points(group=ENTRYPOINT_GROUPNAME)

    for ep in fifo_filter(eps):
        try:
            fn = ep.load()
        except ModuleNotFoundError:
            warnings.warn(
                f"Registered entrypoint {ep.name}: Module {ep.module} not found."
            )
            continue
        except AttributeError:
            warnings.warn(
                f"Registered entrypoint {ep.name}: Attribute {ep.name} not found."
            )
            continue

        if not callable(fn):
            warnings.warn(f"Registered entrypoint {ep.name} not executable.")
            continue

        try:
            fn()
        except Exception as exc:
            warnings.warn(f"Error executing registered entrypoint {ep.name}: {exc}")


def cancel() -> None:
    """No-op function to cancel registered entrypoints.

    Imagine your project depends on a package that registers a sitecustomize-entrypoint:

    In third third-party package:
        [tool.poetry.plugins."sitecustomize"]
        foo = "package_foo:foo"

    And you register a sitecustomize-entrypoint in your own project:
        [tool.poetry.plugins."sitecustomize"]
        bar = "package_bar:bar"

    You can guarantee the ordering, bv canceling the registered entrypoints
    and re-registering them in the order you want:

    in our own pyproject.toml:

        [tool.poetry.plugins."sitecustomize"]
        foo = "sitecustomize:cancel"
        bar = "sitecustomize:cancel"

        1_bar = "package_bar:bar"
        2_foo = "package_foo:foo"

    But please becautioned that the ordering in your pyproject.toml is irrelevant
    and that after parsing the names of entrypoints will be sorted alpanumerically.
    Therefore we advice to use integer-prefixes.
    """


def print_entrypoints(group_name: str = ENTRYPOINT_GROUPNAME, filtered: bool = False):
    """print registered entrypoints."""
    eps = entry_points(group=group_name)

    if filtered:
        eps = fifo_filter(eps)

    for ep in eps:
        print(f"{ep.name}: {ep.value}")
