"""Testing of module sitecustomize._utils."""


def test_fifo_filter(n1, n2, n3):
    from sitecustomize._utils import fifo_filter

    assert fifo_filter([]) == []
    assert fifo_filter([n1]) == [n1]
    assert fifo_filter([n1, n1]) == [n1]

    assert fifo_filter([n1, n2]) == [n1, n2]
    assert fifo_filter([n1, n2, n1]) == [n2, n1]
    assert fifo_filter([n1, n2, n3, n2, n1]) == [n3, n2, n1]