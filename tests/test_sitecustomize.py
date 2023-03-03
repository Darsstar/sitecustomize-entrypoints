"""Testing of module sitecustomize."""

def test_import_sitecustomize():

    try:
        import sitecustomize
        assert True
    except ImportError:
        # package sitecustomize-entrypoints is not installed
        assert False
