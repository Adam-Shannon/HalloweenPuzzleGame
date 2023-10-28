from components.generator import generate
import regex as re
import pandas as pd
import random

spooky_words = pd.read_csv("src/components/spooks.csv").columns.tolist()
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
            #text = text.replace("prev_answers", ",".join(self.gd.previous_answers))
            answer = random.choice(spooky_words)
            spooky_words.remove(answer)
            text = text.replace("riddle_answer", answer)
            riddle = generate(text)
            extractor = re.compile(f"\s({answer})(\w+)\s",flags=re.IGNORECASE)
            riddle = extractor.sub("___",riddle)
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
