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
        self.price = self.price * self.pay_rate

    @property
    def name(self) -> str:
        """Возвращает имя товара"""
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """Проверяет, что длина наименования товара не больше 10 симвовов"""
        if len(value) > 10:
            raise ValueError("The name is below eligibility criteria ")
        else:
            self.__name = value

    @classmethod
    def instantiate_from_csv(cls):
        cls.all.clear()
        """инициализирующий экземпляры класса `Item` данными из файла _src/items.csv"""
        with open('../items.csv', encoding="windows-1251") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=",")
            for i in reader:
                item = Item(i["name"], i["price"], i["quantity"])
    @staticmethod
    def string_to_number(string_number: str) -> int:
        try:
            return int(string_number)
        except ValueError:
            return int(string_number[0:string_number.find(".")])

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"