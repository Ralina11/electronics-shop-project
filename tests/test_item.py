"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import *

@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)

def test_init(item1):
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20

def test_calculate_total_price():
    item3 = Item("cat", 3000, 10)
    total_price = item3.calculate_total_price()
    assert total_price == 30000

def test_apply_discount():
    item3 = Item("cat", 3000, 10)
    item3.pay_rate = 0.8
    item3.apply_discount()
    assert item3.price == 2400

def test_instantiate_from_csv():
    item = Item("cat", 3000, 10)
    item.instantiate_from_csv()
    assert len(Item.all) == 5

def test_string_to_number():
    item = Item("cat", 3000, 10)
    string_num = "5.0"
    int_num = item.string_to_number(string_num)
    assert int_num == 5

def test_repr(item1):
    assert repr(item1) == "Item('Смартфон', 10000, 20)"

def test_string(item1):
    assert str(item1) == 'Смартфон'
