import pygame

def movement(pressed_keys):
    move = [0, 0]
    if pressed_keys[pygame.K_w]:
        move[1] = -1
    if pressed_keys[pygame.K_s]:
        move[1] = 1
    if pressed_keys[pygame.K_d]:
        move[0] = 1
    if pressed_keys[pygame.K_a]:
        move[0] = -1
    return move
