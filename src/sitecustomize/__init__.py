"""sitecustomize."""
__version__ = "1.0.0"  # poetry-dynamic-versioning substitutes this
import typing as tp
import warnings

from ._vendor.importlib_metadata import entry_points, EntryPoints


# -> Union[EntryPoints, SelectableGroups]


def most_recent_unique_entries(
    ordered_list: tp.List[EntryPoints],
) -> tp.List[EntryPoints]:
    """Remove duplicate entries from an ordered list,
    preserving initial ordering but removing previously seen entries.

    Example:

        >>> most_recent_unique_entries([1, 2, 3, 1])
          [2, 3, 1]

    This allows you to override the ordering of a registered entrypoint in your own pyproject.toml.
    """
    return {ep.name: ep for ep in ordered_list}.values()


class SimpleWarnings:
    def __enter__(self):
        self.old_format = warnings.formatwarning
        warnings.formatwarning = self.simple_warning_format
        return self

    def __exit__(self, *args):
        warnings.formatwarning = self.old_format

    @staticmethod
    def simple_warning_format(msg, *args, **kwargs):
        return f"Warning from sitecustomize.py: {msg}\n"


with SimpleWarnings():

    eps = entry_points(group="sitecustomize")

    for ep in most_recent_unique_entries(eps):

        try:
            fn = ep.load()

        except ModuleNotFoundError:
            warnings.warn(
                f"Registered entrypoint {ep.name}: Module {ep.module} not found"
            )
            continue

        except AttributeError:
            warnings.warn(
                f"Registered entrypoint {ep.name}: Attribute {ep.name} not found"
            )
            continue

        if not callable(fn):
            warnings.warn(f"Error executing registered entrypoint {ep.name} not callable")
            continue

        try:
            fn()
        except Exception as exc:
            warnings.warn(f"Error executing registered entrypoint {ep.name}: {exc}")
