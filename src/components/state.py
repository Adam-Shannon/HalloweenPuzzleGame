from components.generator import generate
import regex as re
import pandas as pd
import random
import pygame as pg

spooky_words = pd.read_csv("src/components/spooks.csv").columns.tolist()
class Levl():
    def __init__(self, index, screen, gd):
        self.index = index
        self.screen = screen
        self.gd = gd
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

    def begin_level(self):
        path = "src/components/images/"+self.gd.images[self.index]
        background = pg.image.load(path)
        self.ask_riddle(self.gd.images[self.index].rstrip(".png"))
        self.screen.blit(background, background.get_rect())
    
    def change_level(self):
        return Levl(self.index+1, self.screen, self.gd)
         
