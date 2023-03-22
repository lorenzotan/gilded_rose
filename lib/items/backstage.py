from .rule_base import RuleBase
from .item_proxy import ItemProxy

class Backstage(RuleBase):
    def __str__(self) -> str:
        return 'Backstage passes to a TAFKAL80ETC concert'


    def is_match(self, item: ItemProxy) -> bool:
        return item.name == 'Backstage passes to a TAFKAL80ETC concert'


    def update_item(self, item: ItemProxy) -> None:
        item.increment_quality()

        if item.sell_in < 11:
            item.increment_quality()

        if item.sell_in < 6:
            item.increment_quality()

        item.decrement_sell_in()

        if item.sell_in < 0:
            item.reset_quality()