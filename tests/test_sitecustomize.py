"""Testing of module sitecustomize."""


def test_import_sitecustomize():
    try:
        import sitecustomize

        assert True
    except ImportError:
        # package sitecustomize-entrypoints is not installed
        assert False


def most_recent_unique_entries():
    from sitecustomize import most_recent_unique_entries

    assert most_recent_unique_entries([]) == []
    assert most_recent_unique_entries([1]) == [1]
    assert most_recent_unique_entries([1, 1, 1]) == [1]

    assert most_recent_unique_entries([1, 2]) == [1, 2]
    assert most_recent_unique_entries([1, 2, 1]) == [2, 1]
    assert most_recent_unique_entries([1, 2, 2, 1]) == [2, 1]
    assert most_recent_unique_entries([1, 2, 3, 3, 2, 1]) == [3, 2, 1]
