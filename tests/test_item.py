"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item, InstantiateCSVError


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert repr(item2) == "Item('Ноутбук', 20000, 5)"


def test_str():
    item1 = Item("Смартфон", 10000, 50)
    item2 = Item("Ноутбук", 20000, 15)
    assert str(item1) == 'Смартфон'
    assert str(item2) == 'Ноутбук'


def test_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.total_price() == 200000
    assert item2.total_price() == 100000


def test_apply_pay_rate():
    Item.discount = 0.9  # установка скидки на все товары
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.price == 10000  # ожидаемая цена со ставкой оплаты
    assert item2.price == 20000  # ожидаемая цена со ставкой оплаты


def test_apply_pay_rate_negative_pay_rate():
    Item.discount = -0.1  # отрицательная скидка
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    item1.apply_pay_rate(0.1)
    assert item1.price == 9000
    assert item2.price == 20000


def test_apply_pay_rate_positive_pay_rate():
    Item.pay_rate = 0.5  # положительный коэффициент оплаты
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    item1.apply_pay_rate(Item.pay_rate)  # передать pay_rate как аргумент
    assert item1.price == 5000 and item2.price == 20000


def test_name_setter():
    item = Item('СуперСмартфон', 10000, 1)
    item.name = 'Ноутбук'
    assert item.name == 'Ноутбук'


def test_instantiate_from_csv():
    item1 = Item('Смартфон', 10000, 1)
    item1.instantiate_from_csv()
    assert len(Item.all) == 10
    assert Item.all[0].name == 'Смартфон'


def test_string_to_number():
    item = Item('Смартфон', 10000, 1)
    assert isinstance(item.string_to_number(item.quantity), int)


def test_exception_instantiate_from_csv():
    Item.file_name = '123'
    with pytest.raises(FileNotFoundError) as e:
        Item.instantiate_from_csv()
    assert str(e.value) == f'Отсутствует файл {Item.file_name}'

    Item.file_name = 'items_test.csv'
    with pytest.raises(InstantiateCSVError) as e:
        Item.instantiate_from_csv()
    assert str(e.value) == f'Файл {Item.file_name} поврежден'