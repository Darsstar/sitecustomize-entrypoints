"""sitecustomize."""
__version__ = "0.0.0"  # poetry-dynamic-versioning substitutes this

import warnings

from ._vendor.importlib_metadata import entry_points

eps = entry_points(group="sitecustomize")


for ep in eps:

    try:
        fn = ep.load()
    except ModuleNotFoundError:
        fn = None
        warnings.warn(f"Registered entrypoint {ep.name}: Module not found")

    if fn and callable(fn):
        try:
            fn()
        except Exception as exc:
            warnings.warn(f"Error executing registered entrypoint {ep.name}: {exc}")
