import pygame
from components.state import First
import components.game_data as gd

pygame.init()
width = 1280
height = 720
font_size = 30
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
state =  First(screen, gd)
input_text = ''
rid_rect = pygame.Rect(0,0,width,30)
input_rect = pygame.Rect(0, height*0.8, width, 30) 
font = pygame.font.SysFont(None, 60)
answering = False
while running:
    # poll for events
    riddle = 'Test Riddle \n I am nowhere \n But i am here \n I am alone \n but i am in company \n What am i?'
    riddle_lines = riddle.splitlines()
    line_height = rid_rect.top
    for line in riddle_lines:
        text_surface = font.render(line, True, (255,255,255))
        screen.blit(text_surface, (rid_rect.left, line_height))
        line_height += font_size + 2
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # elif event.type == pygame.KEYUP:
        #     state = state.change_level()
        elif event.type == pygame.KEYDOWN:
         if event.key == pygame.K_BACKSPACE:
            input_text =  input_text[:-1]
         elif event.key==pygame.K_RETURN:
            #Should do something with answer here
            continue
         else:
            input_text += event.unicode
    
    
    pygame.draw.rect(screen, pygame.Color('purple'), input_rect) 
    text_surface = font.render(input_text, True, (255, 255, 255)) 
    screen.blit(text_surface, (input_rect.x, input_rect.y)) 

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()