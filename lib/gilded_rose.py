from .item_factory import ItemFactory
# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items) -> None:
        self.items = items


    def update_quality(self) -> None:
        factory = ItemFactory()
        for item in self.items:
            gr_item = factory.create_instance(item.name)
            gr_item.update_item(item)


    def update_aged_brie(self, item) -> None:
        item.increment_quality()

        item.decrement_sell_in()

        if item.sell_in < 0:
            item.increment_quality()


    def update_backstage(self, item) -> None:
        item.increment_quality()

        if item.sell_in < 11:
            item.increment_quality()

        if item.sell_in < 6:
            item.increment_quality()

        item.decrement_sell_in()

        if item.sell_in < 0:
            item.reset_quality()


    def update_conjured(self, item) -> None:
        item.decrement_quality()
        item.decrement_quality()

        item.decrement_sell_in()

        if item.sell_in < 0:
            item.decrement_quality()
            item.decrement_quality()


    def update_default(self, item) -> None:
        item.decrement_quality()

        item.decrement_sell_in()

        if item.sell_in < 0:
            item.decrement_quality()


    def update_sulfuras(self, item) -> None:
        pass