import pygame

import config

pygame.init()

window = pygame.display.set_mode((config.WINDOW_INIT_WIDTH, config.WINDOW_INIT_HEIGHT), pygame.RESIZABLE)
font = pygame.font.Font(config.FONT_PATH, config.FONT_SIZE)

pygame.display.set_caption(config.WINDOW_NAME)

player_pos_x = config.PLAYER_INIT_X
player_pos_y = config.PLAYER_INIT_Y

fps = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    window.fill(config.COLOR_BACKGROUND)

    window.blit(font.render(f"fps: {fps}", True, config.COLOR_FONT), (25, 25))

    pygame.draw.rect(window, config.PLAYER_COLOR, (player_pos_x, player_pos_y, config.PLAYER_WIDTH, config.PLAYER_HEIGHT))

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_w]:
        player_pos_y -= (1 / fps) * config.PLAYER_SPEED

    if pressed[pygame.K_s]:
        player_pos_y += (1 / fps) * config.PLAYER_SPEED

    if pressed[pygame.K_d]:
        player_pos_x += (1 / fps) * config.PLAYER_SPEED

    if pressed[pygame.K_a]:
        player_pos_x -= (1 / fps) * config.PLAYER_SPEED

    fps = clock.get_fps()

    clock.tick(config.MAX_FPS)

    pygame.display.update()
