__version__ = "0.0.0"  # poetry-dynamic-versioning substitutes this

from ._vendor.importlib_metadata import entry_points

eps = entry_points(group="sitecustomize")

for ep in eps:
    init_func = ep.load()
    if callable(init_func):
        init_func()
