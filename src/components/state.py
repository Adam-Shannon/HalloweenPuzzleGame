from components.generator import generate
import regex as re
import pandas as pd
import random
import pygame as pg
from PIL import Image
import time

spooky_words = pd.read_csv("src/components/spooks.csv").columns.tolist()
class Levl():
    def __init__(self, index, screen, gd, t_loading_start):
        self.index = index
        self.screen = screen
        self.gd = gd
        self.answer = None
        self.riddle = None
        self.begin_level(t_loading_start)

    def ask_riddle(self, villain):
        with open("src/components/prompt.txt") as f:
            text = f.readline()
            text = text.replace("villain_name", villain)
            #text = text.replace("prev_answers", ",".join(self.gd.previous_answers))
            answer = random.choice(spooky_words)
            spooky_words.remove(answer)
            text = text.replace("riddle_answer", answer)
            print(text)
            riddle = generate(text)
            extractor = re.compile(f"\s({answer})(\w+)\s",flags=re.IGNORECASE)
            riddle = extractor.sub("___",riddle)
            self.riddle = riddle
            self.answer = answer

    def begin_level(self, t_loading_start):
        print(self.index)
        path = "src/components/images/"+self.gd.images[self.index]
        image = Image.open(path)
        new_image = image.resize((1280, 720))
        new_image.save('resized.png')
        background = pg.image.load('resized.png')
        #background = pg.image.load(path)
        self.ask_riddle(self.gd.images[self.index].rstrip(".png"))
        self.screen.blit(background, background.get_rect())
        self.RiddlePurveyeor()
        self.t_loading_diff = time.perf_counter() - t_loading_start
        print(self.t_loading_diff)
    
    def change_level(self, t_loading_start):
        t_loading = time.perf_counter()
        return Levl(self.index+1, self.screen, self.gd, t_loading_start)
    def RiddlePurveyeor(self):
        font = pg.font.SysFont(None, 30)
        riddle_lines = self.riddle.splitlines()
        line_height = 0 
        for line in riddle_lines:
            text_surface = font.render(line, True, (255,0,0))
            self.screen.blit(text_surface, (0, line_height))
            line_height += 30 +2
    def isAnswer(self,user_answer):
        return user_answer.lower().replace(" ", "") == self.answer.lower().replace(" ", "")
         
