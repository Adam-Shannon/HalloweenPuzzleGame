class item():
    def __init__(self, durability):
        self.name = self.__class__.__name__
        self.durability = durability
    def use(self):
        self.durability = self.durability - 1

class Shovel(item):
    def __init__(self):
        super().__init__(5)

class Lamp(item):
    def __init__(self):
        super().__init__(15)


inventory = [Shovel(), Lamp()]