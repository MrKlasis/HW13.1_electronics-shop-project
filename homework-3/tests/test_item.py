import pytest
from item import Item


@pytest.fixture
def item():
    return Item("Test Item", 10.0, 5)


def test_str_method(item):
    assert str(item) == "Test Item"


def test_repr_method(item):
    assert repr(item) == "Item('Test Item', 10.0, 5)"
