class Levl():
    def __init__(self, index, bg):
        self.index = index
        self.bg = bg
    def change_level(self):
        pass

class First(Levl):
    def __init__(self):
        super().__init__(1, "red")
    def change_level(self):
        return Second()

class Second(Levl):
    def __init__(self):
        super().__init__(2, "blue")
    def change_level(self):
        return First()
