import pytest

@pytest.fixture
def item():
    return Item('Телефон', 10000, 5)

def test_name_property(item):
    assert item.name == 'Телефон'

def test_name_property_setter_valid_length(item):
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

def test_name_property_setter_invalid_length(item):
    with pytest.raises(Exception) as e:
        item.name = 'СуперСмартфон'
    assert str(e.value) == 'Длина наименования товара превышает 10 символов.'

def test_instantiate_from_csv():
    Item.instantiate_from_csv("items.csv")
    assert len(Item.all) == 5

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5