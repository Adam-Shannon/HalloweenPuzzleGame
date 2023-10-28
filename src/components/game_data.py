class item():
    def __init__(self, durability):
        self.name = self.__class__.__name__
        self.durability = durability

class Shovel(item):
    def __init__(self):
        super().__init__(1)


inventory = [Shovel()]