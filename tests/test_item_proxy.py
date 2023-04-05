import pytest
from lib.items.item_proxy import ItemProxy

def test_increment_quality():
    item = ItemProxy('Item', 5, 10)
    item.increment_quality()

    assert item.quality == 11


def test_decrement_quality():
    item = ItemProxy('Item', 5, 10)
    item.decrement_quality()

    assert item.quality == 9


def test_reset_quality():
    item = ItemProxy('Item', 5, 10)
    item.reset_quality()

    assert item.quality == 0


def test_decrement_sell_in():
    item = ItemProxy('Item', 5, 10)
    item.decrement_sell_in()

    assert item.sell_in == 4