# 초기화 & 양 옆 넓이랑 높이 맞추기

from turtle import width
import pygame
from torch import true_divide

pygame.init()

width_screen = 640
height_screen = 480

# display.set_caption, display.set_mode가 존재

screen = pygame.display.set_mode((width_screen, height_screen))

pygame.display.set_caption("jongho_game_1")

# image.load

bg = pygame.image.load("C:/workspace2/bg.png")

ch = pygame.image.load("C:/workspace2/pig.png")

ch_size = ch.get_rect().size

ch_width = ch_size[0]
ch_height = ch_size[1]
ch_x_pos = (width_screen / 2) - (ch_width / 2)
ch_y_pos = (height_screen / 2) - (ch_height / 2)

# event.get() 이 존재, event의 타입이 QUIT이면 종료하겠다.

# pygame.display.set_mode 에 blit가 존재

to_x = 0
to_y = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5
            elif event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    ch_x_pos += to_x
    ch_y_pos += to_y

    if ch_x_pos < 0:
        ch_x_pos = 0
    elif ch_x_pos > width_screen - ch_width:
        ch_x_pos = width_screen - ch_width
    if ch_y_pos < 0:
        ch_y_pos = 0
    elif ch_y_pos > height_screen - ch_height:
        ch_y_pos = height_screen - ch_height

    screen.blit(bg, (0,0))
    screen.blit(ch, (ch_x_pos, ch_y_pos))
    pygame.display.update()

    
pygame.quit()