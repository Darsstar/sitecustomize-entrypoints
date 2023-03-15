"""sitecustomize."""
__version__ = "1.0.0"  # poetry-dynamic-versioning substitutes this
import warnings

from sitecustomize._utils import SimpleWarnings, most_recent_unique_entries
from sitecustomize._vendor.importlib_metadata import entry_points


with SimpleWarnings():
    eps = entry_points(group="sitecustomize")

    for ep in most_recent_unique_entries(eps):
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
