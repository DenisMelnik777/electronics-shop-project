"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def Item_test():
    return Item("Ноутбук", 20000, 5)


def test_init(Item_test):
    assert Item_test.name == "Ноутбук"
    assert Item_test.price == 20000
    assert Item_test.quantity == 5


def test_calculate_total_price(Item_test):
    assert Item_test.calculate_total_price() == 100000


def test_apply_discount(Item_test):
    Item_test.pay_rate = 1.0
    Item_test.apply_discount()
    assert Item_test.price == 20000
    assert Item_test.calculate_total_price() == 100000.0

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

