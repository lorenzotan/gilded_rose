# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items) -> None:
        self.items = items


    def update_quality(self) -> None:
        for item in self.items:
            if item.name == 'Aged Brie':
                self.update_aged_brie(item)
            elif item.name == 'Backstage passes to a TAFKAL80ETC concert':
                self.update_backstage(item)
            elif item.name == 'Conjured Mana Cake':
                self.update_conjured(item)
            elif item.name == 'Sulfuras, Hand of Ragnaros':
                self.update_sulfuras(item)
            else:
                self.update_default(item)


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