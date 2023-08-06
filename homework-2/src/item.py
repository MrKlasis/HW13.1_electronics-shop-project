import csv
import inspect
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        list_values =list()
        for value in self.__dict__.values():
            list_values.append(str(value))
        return f"{self.__class__.__name__}({', '.join(list_values)})"

    def __str__(self):
        return f"{self.name}"

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise TypeError("Складывать можно только объекты классов с родительским классом Item")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception("Длина наименования товара больше 10 симвовов")

    @classmethod
    def instantiate_from_csv(cls):
        class_file = inspect.getfile(cls)  # узнаем название файла содержащего класс
        path_to_dir = os.path.dirname(class_file)  # ищем абсолютный путь до файла
        try:
            with open(f'{path_to_dir}/items.csv', encoding='pt154') as csvfile:
                reader = csv.DictReader(csvfile)
                for ex in reader:
                    cls(name=ex['name'], price=float(ex['price']), quantity=int(ex['quantity']))
        except FileNotFoundError:
            print("Отсутствует файл item.csv")


    @staticmethod
    def string_to_number(string_number: str):
        """
        Переводит число-строку в число
        :param string_number: число-строка.
        :return: число.
        """
        return int(string_number.split('.')[0])