import pytest
from item import Item

@pytest.fixture
def item():
    return Item("Test Item", 10.0, 5)

def test_calculate_total_price(item):
    assert item.calculate_total_price() == 50.0

def test_apply_discount(item):
    item.apply_discount()
    assert item.price == 10.0

def test_name_property(item):
    assert item.name == "Test Item"

def test_name_setter(item):
    item.name = "New Test Item Name"
    assert item.name == "New Test Ite"

def test_instantiate_from_csv():
    Item.instantiate_from_csv("test_items.csv")
    assert len(Item.all) == 2
    assert Item.all[0].name == "Item 1"
    assert Item.all[0].price == 10.0
    assert Item.all[0].quantity == 5
    assert Item.all[1].name == "Item 2"
    assert Item.all[1].price == 20.0
    assert Item.all[1].quantity == 3

def test_string_to_number():
    assert Item.string_to_number("10.0") == 10
    assert Item.string_to_number("5.5") == 5
    assert Item.string_to_number("3.14") == 3
