"""Testing of module sitecustomize."""


def test_import_sitecustomize():
    try:
        import sitecustomize

        assert True
    except ImportError:
        # package sitecustomize-entrypoints is not installed
        assert False


def test_cancel():
    from sitecustomize import cancel

    assert cancel() is None


def test_print_entrypoints():
    # unsure how to properly unit-test this.
    from sitecustomize import print_entrypoints

    assert print_entrypoints() is None
    assert print_entrypoints(filtered=True) is None
    assert print_entrypoints(filtered=False) is None