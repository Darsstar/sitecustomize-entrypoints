"""Config for pytest."""
import pytest

from sitecustomize._vendor.importlib_metadata import EntryPoint


# @pytest.fixture
# def n1_a():
#     return EntryPoint(name="1", value="v-1aa", group="sitecustomize")

# @pytest.fixture
# def n1_b():
#     return EntryPoint(name="1", value="v-1bb", group="sitecustomize")

@pytest.fixture
def n1():
    return EntryPoint(name="1", value="v1", group="sitecustomize")

@pytest.fixture
def n2():
    return EntryPoint(name="2", value="v2", group="sitecustomize")

@pytest.fixture
def n3():
    return EntryPoint(name="3", value="v3", group="sitecustomize")

