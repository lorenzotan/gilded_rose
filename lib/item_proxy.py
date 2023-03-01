from .item import Item

'''
The rules state that we cannot alter the Item class.
So we want to create an Item Proxy that will have access to
the attributes so that we can manipulate them without 
touching the Item class itself.
'''        
class ItemProxy(Item):
    def __init__(self, name: str, sell_in: int, quality: int) -> None:
        Item.__init__(self, name, sell_in, quality)

    def increment_quality(self) -> None:
        if self.quality < 50:
            self.quality = self.quality + 1

    def decrement_quality(self) -> None:
        if self.quality > 0:
            self.quality = self.quality - 1

    def reset_quality(self) -> None:
        self.quality = 0

    def decrement_sell_in(self) -> None:
        self.sell_in = self.sell_in - 1