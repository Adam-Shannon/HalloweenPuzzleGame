import pygame
from components.state import First
import components.game_data as gd

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
state =  First(screen, gd)

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

def play_sound(sound):
 mixer.Channel(1).play(sound)
 mixer.music.stop()

# ------------------------------------------------------------------------------------



while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            play_sound(whistle)
            state = state.change_level()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()