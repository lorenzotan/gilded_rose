import lib.items as items
from inspect import getmembers, isclass, isabstract

class ItemFactory(object):
    gilded_items = {}

    def __init__(self):
        self.load_items()


    def load_items(self):
        classes = getmembers(items,
                             lambda m: isclass(m) and not isabstract(m))

        for name, _type in classes:
            if isclass(_type) and issubclass(_type, items.RuleBase):
                self.gilded_items.update([[_type.__str__(_type), _type]])


    def show_items(self):
        return self.gilded_items


    def create_instance(self, item):
        if item in self.gilded_items:
            return self.gilded_items[item]()
        else:
            return self.gilded_items['Other'](item)
