"""sitecustomize._utils."""
import typing as tp
import warnings


if tp.TYPE_CHECKING:

    class NamedObject(tp.Protocol):
        name: str


def fifo_filter(ordered_list: tp.List["NamedObject"]) -> tp.List["NamedObject"]:
    """Remove duplicate entries from an ordered list,
    preserving initial ordering but removing previously seen entries.

    Example:

        >>> fifo_filter([1, 2, 3, 1])
          [2, 3, 1]

    This allows you to override the ordering of a registered entrypoint
    in your own pyproject.toml.
    """
    fifo_dict: tp.Dict[str, "NamedObject"] = {}  # dict is ordered since python3.6

    for ep in ordered_list:
        # remove pre-existing entry
        if ep.name in fifo_dict:
            del fifo_dict[ep.name]

        # append new entry at the end
        fifo_dict[ep.name] = ep

    return list(fifo_dict.values())


class SimpleWarning:
    def __enter__(self):
        self.old_format = warnings.formatwarning
        warnings.formatwarning = self.simple_warning_format
        return self

    def __exit__(self, *args):
        warnings.formatwarning = self.old_format

    @staticmethod
    # def simple_warning_format(msg, *args, **kwargs):
    def simple_warning_format(msg, category, filename, lineno, file=None, line=None):
        """Simple warning-formatting."""
        # return f"Warning from sitecustomize.py: {msg}\n"
        return f"{category}: Warning from sitecustomize.py: {msg}\n"
