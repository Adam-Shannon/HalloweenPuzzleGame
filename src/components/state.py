from components.generator import generate
import regex as re
import pandas as pd
import random
import pygame as pg
from PIL import Image

spooky_words = pd.read_csv("src/components/spooks.csv").columns.tolist()
class Levl():
    def __init__(self, index, screen, gd):
        self.index = index
        self.screen = screen
        self.gd = gd
        self.answer = None
        self.riddle = None
        self.begin_level()

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
            extractor = f"(\s*){answer}(\w*)(\s*)"
            extractor = re.compile(extractor,flags=re.IGNORECASE)
            riddle = re.sub(extractor,"___",riddle)
            self.riddle = riddle
            self.answer = answer

    def begin_level(self):
        choice = random.randint(0,len(self.gd.images)-1)
        path = "src/components/images/"+self.gd.images[choice]
        image = Image.open(path)
        new_image = image.resize((1280, 720))
        new_image.save('resized.png')
        background = pg.image.load('resized.png')
        #background = pg.image.load(path)
        self.ask_riddle(self.gd.images[choice].rstrip(".png"))
        self.screen.blit(background, background.get_rect())
        self.RiddlePurveyeor()
    
    def change_level(self):
        return Levl(self.index+1, self.screen, self.gd)
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
         
