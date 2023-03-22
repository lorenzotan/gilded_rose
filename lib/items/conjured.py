from .rule_base import RuleBase
from .item_proxy import ItemProxy

class Conjured(RuleBase):
    def __str__(self) -> str:
        return 'Conjured Mana Cake'


    def is_match(self, item: ItemProxy) -> bool:
        return item.name == 'Conjured Mana Cake'


    def update_item(self, item: ItemProxy) -> None:
        item.decrement_quality()
        item.decrement_quality()

        item.decrement_sell_in()

        if item.sell_in < 0:
            item.decrement_quality()
            item.decrement_quality()