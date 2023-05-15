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
