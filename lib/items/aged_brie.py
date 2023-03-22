import sys
from .rule_base import RuleBase
from .item_proxy import ItemProxy

class AgedBrie(RuleBase):
    def __str__(self) -> str:
        return 'Aged Brie'


    def is_match(self, item: ItemProxy) -> bool:
        return item.name == 'Aged Brie'


    def update_item(self, item: ItemProxy) -> None:
        item.increment_quality()

        item.decrement_sell_in()

        if item.sell_in < 0:
            item.increment_quality()