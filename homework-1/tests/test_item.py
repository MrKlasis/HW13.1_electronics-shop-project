import pytest

from src.item.parent import Item

def test_init(test_item):
    assert test_item.name == 'One'
    assert test_item.price == 2
    test_item.price = 22
    assert test_item.price == 22
    assert isinstance(test_item.all[0], Item) == True




"""Здесь надо написать тесты с использованием pytest для модуля item."""
