from components.generator import generate
import regex as re
class Levl():
    def __init__(self, index, bg, screen, gd):
        self.index = index
        self.bg = bg
        self.screen = screen
        self.gd = gd
        self.prompt = "generate a riddle"
        self.begin_level()

    def ask_riddle(self, villain):
        with open("src/components/prompt.txt") as f:
            text = f.readline()
            text = text.replace("villain_name", villain)
            text = text.replace("prev_answers", ",".join(self.gd.previous_answers))
            print(text)
            (riddle,answer) = generate(text)
            print(riddle)
            print(answer)

    def change_level(self):
        self.screen.fill("black")
        

class First(Levl):
    def __init__(self, screen, gd):
        super().__init__(1, "red", screen, gd)
    def change_level(self):
        return Second(self.screen, self.gd)
    def begin_level(self):
        self.ask_riddle("ogre")
        self.screen.fill(self.bg)

class Second(Levl):
    def __init__(self, screen, gd):
        super().__init__(2, "blue", screen, gd)
    def change_level(self):
        return First(self.screen, self.gd)
    def begin_level(self):
        self.ask_riddle("evil jester")
        self.screen.fill(self.bg)   
