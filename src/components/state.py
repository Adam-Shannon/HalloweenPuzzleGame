import pygame

class Levl():    
    def __init__(self, index, bg, screen, gd):
        self.index = index
        self.bg = bg
        self.screen = screen
        self.gd = gd
        self.begin_level()
        self.loading(screen)
    
    def loading(self, screen):
        while True:
            # loading = pygame.image.load("src/components/img/Loading.png").convert()
            # screen.blit(loading, (0, 0))
            pass


    def change_level(self):
        self.screen.fill("black")
    def begin_level(self):
        self.screen.fill(self.bg)

class First(Levl):
    def __init__(self, screen, gd):
        super().__init__(1, "red", screen, gd)
    def change_level(self):
        print([i.name for i in self.gd.inventory] )
        return Second(self.screen, self.gd)

class Second(Levl):
    def __init__(self, screen, gd):
        super().__init__(2, "blue", screen, gd)
    def change_level(self):
        print([i.name for i in self.gd.inventory])
        return First(self.screen, self.gd)
