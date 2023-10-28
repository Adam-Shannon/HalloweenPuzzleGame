import pygame
from components.state import First
import components.game_data as gd
import time

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
state =  First(screen, gd)
COUNTDOWN_TIME = 120

t_start = time.perf_counter()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    t_stop = time.perf_counter()
    
    if COUNTDOWN_TIME <= (t_stop - t_start):
        running = False
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            state = state.change_level()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()