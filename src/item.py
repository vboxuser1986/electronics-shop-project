import csv


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
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        """Возвращает данные объекта"""
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Возвращает название"""
        return f"{self.name}"

    def __add__(self, other):
        """Определение сложения товаров"""
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("Unsupported class.")

    @property
    def name(self) -> str:
        """Геттер названия"""
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        """Сеттер названия"""
        if len(new_name) >= 10:
            raise ValueError('More than 10 letters in the name')
        else:
            self.__name = new_name

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
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv"""
        cls.all = []

        try:
            with open("src/items.csv", newline='', encoding='CP1251') as file:
                data = csv.DictReader(file)
                for item in data:
                    cls(item['name'], float(item['price']), Item.string_to_number(item['quantity']))
        except Exception as Error:
            print(Error)

    @staticmethod
    def string_to_number(str_number: str) -> int:
        """
        Статический метод, возвращающий число из числа-строки
        """
        return int(float(str_number))
