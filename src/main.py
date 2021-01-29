import math
import threading

import pygame

pygame.init()

window = pygame.display.set_mode((800, 750), pygame.RESIZABLE, vsync=False)
font = pygame.font.Font("font/SourceSansPro-SemiBoldItalic.ttf", 20)

pygame.display.set_caption("Python Performance Demo")

player_pos_x = 0
player_pos_y = 0

clock = pygame.time.Clock()
clock2 = pygame.time.Clock()

fps = 0
time = 0

speed = 450
tick = 1500

act_fps = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    window.fill((0, 0, 0))

    window.blit(font.render(f"fps: {fps}", True, (255, 255, 255)), (25, 25))

    pygame.draw.rect(window, (255, 255, 255), (player_pos_x, player_pos_y, 50, 50))

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_w]:
        player_pos_y -= (1 / clock.get_fps()) * speed

    if pressed[pygame.K_s]:
        player_pos_y += (1 / clock.get_fps()) * speed

    if pressed[pygame.K_d]:
        player_pos_x += (1 / clock.get_fps()) * speed

    if pressed[pygame.K_a]:
        player_pos_x -= (1 / clock.get_fps()) * speed

    fps = clock.get_fps()

    clock.tick(tick)

    pygame.display.update()
