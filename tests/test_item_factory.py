import pytest
from lib.items.item_proxy import ItemProxy
from lib.item_factory import ItemFactory
# import lib.items
from lib.items import *

# TODO: BEFORE TEST, CREATE ITEM ONCE FOR ALL TESTS
@pytest.mark.parametrize("category, expected_obj",
                         [
('Aged Brie', 'AgedBrie'),
# ('Backstage passes to a TAFKAL80ETC concert', 'Backstage'),
# ('Conjured Mana Cake', 'Conjured'),
# ('Eggs Benny', 'Other'),
# ('Sulfuras, Hand of Ragnaros', 'Sulfuras'),
                         ])
def test_create_aged_brie(category, expected_obj):
    item = [ ItemProxy(category, 5, 10) ]
    factory = ItemFactory()
    # XXX gilded_rose.lib.items.aged_brie.AgedBrie
    # can i check the type dynamically?
    obj = type(AgedBrie())
    # XXX lib.items.aged_brie.AgedBrie
    instance = factory.create_instance(item[0].name)

    assert isinstance(instance, obj)

@pytest.mark.parametrize("category, expected_obj",
                         [
('Backstage passes to a TAFKAL80ETC concert', 'Backstage'),
# ('Conjured Mana Cake', 'Conjured'),
# ('Eggs Benny', 'Other'),
# ('Sulfuras, Hand of Ragnaros', 'Sulfuras'),
                         ])
def test_create_backstage(category, expected_obj):
    item = [ ItemProxy(category, 5, 10) ]
    factory = ItemFactory()
    # XXX gilded_rose.lib.items.aged_brie.AgedBrie
    # can i check the type dynamically?
    obj = type(Backstage())
    # XXX lib.items.aged_brie.AgedBrie
    instance = factory.create_instance(item[0].name)

    assert isinstance(instance, obj)

@pytest.mark.parametrize("category, expected_obj",
                         [
('Conjured Mana Cake', 'Conjured'),
# ('Eggs Benny', 'Other'),
# ('Sulfuras, Hand of Ragnaros', 'Sulfuras'),
                         ])
def test_create_conjured(category, expected_obj):
    item = [ ItemProxy(category, 5, 10) ]
    factory = ItemFactory()
    # XXX gilded_rose.lib.items.aged_brie.AgedBrie
    # can i check the type dynamically?
    obj = type(Conjured())
    # XXX lib.items.aged_brie.AgedBrie
    instance = factory.create_instance(item[0].name)

    assert isinstance(instance, obj)

@pytest.mark.parametrize("category, expected_obj",
                         [
('Eggs Benny', 'Other'),
# ('Sulfuras, Hand of Ragnaros', 'Sulfuras'),
                         ])
def test_create_other(category, expected_obj):
    item = [ ItemProxy(category, 5, 10) ]
    factory = ItemFactory()
    # XXX gilded_rose.lib.items.aged_brie.AgedBrie
    # can i check the type dynamically?
    obj = type(Other())
    # XXX lib.items.aged_brie.AgedBrie
    instance = factory.create_instance(item[0].name)

    assert isinstance(instance, obj)

@pytest.mark.parametrize("category, expected_obj",
                         [
('Sulfuras, Hand of Ragnaros', 'Sulfuras'),
                         ])
def test_create_sulfuras(category, expected_obj):
    item = [ ItemProxy(category, 5, 10) ]
    factory = ItemFactory()
    # XXX gilded_rose.lib.items.aged_brie.AgedBrie
    # can i check the type dynamically?
    obj = type(Sulfuras())
    # XXX lib.items.aged_brie.AgedBrie
    instance = factory.create_instance(item[0].name)

    assert isinstance(instance, obj)
