# 초기화 & 양 옆 넓이랑 높이 맞추기

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

# event.get() 이 존재, event의 타입이 QUIT이면 종료하겠다.

# pygame.display.set_mode 에 blit이라는 게 존재

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg, (0,0))
    pygame.display.update()

    
pygame.quit()