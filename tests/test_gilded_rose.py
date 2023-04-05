import pytest
from lib.items.item_proxy import ItemProxy
from lib.gilded_rose import GildedRose


@pytest.mark.parametrize("item, sell_in, expected_sell_in",
    [
        ("Default", 2, 1),
        ("Aged Brie", 2, 1),
        ("Backstage passes to a TAFKAL80ETC concert", 2, 1),
        ("Conjured Mana Cake", 0, -1),
        ("Sulfuras, Hand of Ragnaras", 1, 0)
    ]
)
def test_item_sell_in(item, sell_in, expected_sell_in):
    items = [ItemProxy(item, sell_in=sell_in, quality=0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == expected_sell_in


@pytest.mark.parametrize("item, quality, expected_quality",
    [
        ("Aged Brie", 0, 1),
        ("Backstage passes to a TAFKAL80ETC concert", 20, 23),
        ("Conjured Mana Cake", 3, 1),   # quality drops twice as fast
        ("Default", 1, 0),
        ("Sulfuras, Hand of Ragnaros", 79, 79)
    ]
)
def test_item_quality(item, quality, expected_quality):
    items = [ItemProxy(item, sell_in=1, quality=quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == expected_quality


@pytest.mark.parametrize("item, sell_in, quality, expected_quality, days",
    [
        ("Aged Brie", 5, 45, 50, 10),
        ("Aged Brie", 3, 20, 37, 10),
        ("Aged Brie", 10, 20, 25, 5),
        ("Backstage passes to a TAFKAL80ETC concert", 11, 20, 25, 3),
        ("Backstage passes to a TAFKAL80ETC concert", 7, 20, 30, 4),
        ("Backstage passes to a TAFKAL80ETC concert", 3, 20, 0, 4),
        ("Default", 5, 23, 8, 10),
    ]
)
def test_item_quality_over_time(item, sell_in, quality, expected_quality, days):
    items = [ItemProxy(item, sell_in=sell_in, quality=quality)]
    gilded_rose = GildedRose(items)
    for day in (range(days)):
        gilded_rose.update_quality()

    assert items[0].quality == expected_quality

def test_foo():
    items = [ItemProxy("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == 'foo'