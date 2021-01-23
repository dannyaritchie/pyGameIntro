from classes import *
from functions import *
from globalVariables import *
import pygame

# initialise the pygame
pygame.init()

# create the screen
gameScreen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

# Title and Icon
pygame.display.set_caption("Rotating Function")
icon = pygame.image.load('space-ship.png')
pygame.display.set_icon(icon)

# Player
playerX = 400
playerY = 300
width = 100
height = 100
space_ship = Tank(playerX, playerY, width, height, speedInput=0.6)
offset = height/4

# Game icon
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RGB - Red Green Blue
    gameScreen.fill((255, 255, 255))

    # register inputs from the player
    cursorPosition = pygame.mouse.get_pos()
    pressed_keys = pygame.key.get_pressed()
    moveDirection = movement(pressed_keys)

    space_ship.update(cursorPosition, moveDirection)
    space_ship.display(gameScreen)

    pygame.display.update()
