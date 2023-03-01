# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.name != "Sulfuras, Hand of Ragnaros":
                    item.decrement_quality()
            else:
                item.increment_quality()
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 11:
                        item.increment_quality()
                    if item.sell_in < 6:
                        item.increment_quality()
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.decrement_sell_in()
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.name != "Sulfuras, Hand of Ragnaros":
                            item.decrement_quality()
                    else:
                        item.reset_quality()
                else:
                    item.increment_quality()