"""Здесь надо написать тесты с использованием pytest для модуля item."""

item1 = Item("Товар 1", 10.0, 5)
item2 = Item("Товар 2", 20.0, 3)

# Тест для метода __repr__
assert repr(item1) == "Item(name=Товар 1, price=10.0, quantity=5)"
assert repr(item2) == "Item(name=Товар 2, price=20.0, quantity=3)"

# Тест для метода __str__
assert str(item1) == "Item: Товар 1, Price: 10.0, Quantity: 5"
assert str(item2) == "Item: Товар 2, Price: 20.0, Quantity: 3"
