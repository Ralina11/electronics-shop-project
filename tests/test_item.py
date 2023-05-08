"""Здесь надо написать тесты с использованием pytest для модуля item."""
import contextlib, io
import pytest
from src.item import *
from src.phone import Phone
from src.keyboard import KeyBoard


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


@pytest.fixture()
def item2():
    return Phone("Смартфон", 10000, 20, 2)


def test_init(item2):
    assert item2.name == "Смартфон"
    assert item2.price == 10000
    assert item2.quantity == 20
    assert item2.number_of_sim == 2


def test_repr(item2):
    assert repr(item2) == "Phone('Смартфон', 10000, 20, 2)"


def test_add(item2):
    test_1 = Item("Melon", 100, 50)
    assert (item2 + test_1)


@pytest.fixture()
def item3():
    return KeyBoard('Dark Project KD87A', 9600, 5)


def test_change_lang(item3):
    assert str(item3.language) == "EN"
    item3.change_lang()
    assert str(item3.language) == "RU"


def test_str(item3):
    assert str(item3) == "Dark Project KD87A"


def test_instantiate_from_csv(item2):
    s = io.StringIO()
    with contextlib.redirect_stdout(s):
        item2.instantiate_from_csv(path="../src/itemms.csv")
    assert s.getvalue() == f'Item not found\n'



