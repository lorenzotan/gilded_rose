from lib.item_factory import ItemFactory
# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items) -> None:
        self.items = items


    def update_quality(self) -> None:
        factory = ItemFactory()
        for item in self.items:
            gr_item = factory.create_instance(item.name)
            gr_item.update_item(item)
