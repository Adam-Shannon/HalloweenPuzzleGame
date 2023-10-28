class Levl():
    def __init__(self, index, bg, screen):
        self.index = index
        self.bg = bg
        self.screen = screen
        self.begin_level()

    def change_level(self):
        self.screen.fill("black")
    def begin_level(self):
        self.screen.fill(self.bg)
        

class First(Levl):
    def __init__(self, screen):
        super().__init__(1, "red", screen)
    def change_level(self):
        return Second(self.screen)

class Second(Levl):
    def __init__(self, screen):
        super().__init__(2, "blue", screen)
    def change_level(self):
        return First(self.screen)
