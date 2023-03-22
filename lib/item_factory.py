import lib.items as items
from inspect import getmembers, isclass, isabstract

# NOTE: why pass 'object'
class ItemFactory(object):
    gilded_items = {}

    def __init__(self):
        self.load_items()

    def load_items(self):
        classes = getmembers(items,
                             lambda m: isclass(m) and not isabstract(m))

        for name, _type in classes:
            if isclass(_type) and issubclass(_type, items.RuleBase):
                print(f"Full Name:  {_type.__str__(_type)}")
                print(f"Class Name: {name}\nClass Type: {_type}")
                self.gilded_items.update([[_type.__str__(_type), _type]])
            else:
                print(f"Excluding: {name}")

    def show_items(self):
        return self.gilded_items

    def create_instance(self, item):
        if item in self.gilded_items:
            return self.gilded_items[item]()
        else:
            return self.gilded_items['Other'](item)




if __name__ == '__main__':
    factory = ItemFactory()
    print()
    print("Init")
    print(factory)
    print()
    print("Show Items")
    print(factory.show_items())
    i = factory.create_instance('Aged Brie')
    print()
    print("Instance")
    print(i)

    d = factory.create_instance('Dog')
    print()
    print("Instance")
    print(d)