import pytest

from src.item import Item, InstantiateCSVError
from src.phone import Phone
from src.setting import CSV


def test_init():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_add():
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    with pytest.raises(ValueError):
        item1 + 10


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.calculate_total_price() == 200000


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0


def test_instantiate_from_csv():
    Item.instantiate_from_csv(CSV)
    assert len(Item.all) == 5

def test_instantiate_from_csv_file_not_found():
    with pytest.raises(FileNotFoundError) as excinfo:
        Item.instantiate_from_csv("nonexistent_file.csv")
    assert str(excinfo.value) == "Отсутствует файл item.csv"


def test_instantiate_from_csv_file_corrupted():
    with pytest.raises(InstantiateCSVError) as excinfo:
        Item.instantiate_from_csv("corrupted_file.csv")
    assert str(excinfo.value) == "Файл item.csv поврежден"


def test_instantiate_from_csv_valid_file():
    Item.instantiate_from_csv("valid_file.csv")
    assert len(Item.all) == 3
    assert Item.all[0].name == "Item 1"
    assert Item.all[0].price == 10.0
    assert Item.all[0].quantity == 5
    assert Item.all[1].name == "Item 2"
    assert Item.all[1].price == 20.0
    assert Item.all[1].quantity == 10
    assert Item.all[2].name == "Item 3"
    assert Item.all[2].price == 30.0
    assert Item.all[2].quantity == 15

def test_name():
    item = Item('Смартфон', 10000, 5)
    item.name = "СуперСмартфон"
    assert len(item.name) <= 10
    assert item.name == 'СуперСмарт'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
