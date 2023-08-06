import pytest

from src.item.parent import Item


def test_init():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20


def test_name():
    item = Item('Смартфон', 10000, 5)
    item.name = "СуперСмартфон"
    assert len(item.name) <= 10
    assert item.name == 'СуперСмарт'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
