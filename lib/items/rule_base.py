from abc import ABC, abstractclassmethod
from .item_proxy import ItemProxy

class RuleBase(ABC):
    @abstractclassmethod
    def __str__() -> str:
        pass

    @abstractclassmethod
    def is_match(self, item: ItemProxy) -> bool:
        pass

    @abstractclassmethod
    def update_item(self, item: ItemProxy) -> None:
        pass