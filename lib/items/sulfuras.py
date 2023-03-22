from .rule_base import RuleBase
from .item_proxy import ItemProxy

class Sulfuras(RuleBase):
    def __str__(self) -> str:
        return 'Sulfuras, Hand of Ragnaros'


    def is_match(self, item: ItemProxy) -> bool:
        return item.name == 'Sulfuras, Hand of Ragnaros'


    def update_item(self, item: ItemProxy) -> None:
        return