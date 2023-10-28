import pygame
from sqlalchemy import false
from components.state import First
import components.game_data as gd
import time

pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
state =  First(screen, gd)
COUNTDOWN_TIME = 120 #seconds

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

t_start = time.perf_counter()

#------------------------ sound stuff ---------------------------
#from . import text_to_speech
from pygame import mixer
mixer.init()
# play atmoshpere soundtrack forever
mixer.Channel(0).play(mixer.Sound("components/sound files/horror-background-atmosphere-156462.wav"), -1)

#sfx
door = mixer.Sound("components/sound files/door-creaking-121673.mp3")
whispers = mixer.Sound("components/sound files/four_voices_whispering-6943.mp3")
heartbeat = mixer.Sound("components/sound files/heartbeat.mp3")
whistle = mixer.Sound("components/sound files/wind-whistle-96776.mp3")
scream = mixer.Sound("components/sound files/demonic-woman-scream-6333.mp3")
#hello = pygame.mixer.Sound(text_to_speech.text_to_speech("hello"))

ran = False
delay = t_start
# ------------------------------------------------------------------------------------



while running:
  
    t_stop = time.perf_counter() 
    if COUNTDOWN_TIME <= (t_stop - t_start):
        running = False
    
    # making a heartbeat sound every 10 seconds, if only 30 seconds left
    time_left = COUNTDOWN_TIME - (t_stop - t_start)
    if int(time_left) <= 30 and int(time_left) %10 == 0:
        if ran == False:
            mixer.Channel(1).play(heartbeat, maxtime=5400) #in ms
            ran = True
            delay = t_stop
    if t_stop - delay > 1:
        ran = False


    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            mixer.Channel(1).play(heartbeat, maxtime=5400) #in ms
            state = state.change_level()

    # Displaying the timer
    text = f"{(int)(COUNTDOWN_TIME - (t_stop - t_start))}"
    font = pygame.font.Font(None, 36)
    label = font.render(text, True, (0, 0, 0))
    text_rect = label.get_rect(center=(SCREEN_WIDTH  - 30, 20))
    pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH - 50, 5, 40, 30))
    screen.blit(label, text_rect)


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()