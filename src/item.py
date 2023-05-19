import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    file_name = 'items.csv'

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


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_):
        if len(name_) <= 10:
            self.__name = name_
        else:
            raise ValueError('Длина наименования товара больше 10 символов')


    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        try:
            with open(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')), 'src',
                                   'items.csv')) as f:
                reader = csv.DictReader(f)
                for row in reader:
                    cls.all.append(cls(row['name'], row['price'], row['quantity']))
        except FileNotFoundError:
            raise FileNotFoundError(f'Отсутствует файл {cls.file_name}')
        except PermissionError:
            print(f'Невозможно создать файл {cls.file_name}')


    @staticmethod
    def string_to_number(number):
        return int(float(number))


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
