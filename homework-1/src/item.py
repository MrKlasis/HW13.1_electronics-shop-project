class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: int, quantity: float):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """

    def apply_discount(self):
        self.price *= self.pay_rate
    """
    Применяет установленную скидку для конкретного товара.
    """