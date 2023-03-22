from .rule_base import RuleBase
from .item_proxy import ItemProxy

class Other(RuleBase):
    def __init__(self, name='Other'):
        self.name = name


    def __str__(self) -> str:
        return getattr(self, 'name', 'Other')


    def is_match(self, item: ItemProxy) -> bool:
        True


    def update_item(self, item: ItemProxy) -> None:
        item.decrement_quality()

        item.decrement_sell_in()

        if item.sell_in < 0:
            item.decrement_quality()