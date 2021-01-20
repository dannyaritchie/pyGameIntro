import pygame
import math


class Player:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.center = (x+w/2, y+h/2)
        self.surface = pygame.transform.scale(pygame.image.load("turret.png"), (w, h))
        self.rotated_surface = self.surface.copy()
        self.rect = self.surface.get_rect()

    def rotate(self, X, Y, R):
        dx, dy = X - self.x, Y - self.y
        angle = -90 - math.atan2(dy, dx) * (180/math.pi)
        self.rotated_surface = pygame.transform.rotate(self.surface, angle)
        self.center = (self.x - self.rotated_surface.get_width() / 2 - R*math.sin(angle*(math.pi/180)),
                       self.y - self.rotated_surface.get_height() / 2 - R*math.cos(angle*(math.pi/180)))

    def display(self, screen, xPosition, yPosition, R):
        self.rotate(xPosition, yPosition, R)
        screen.blit(self.rotated_surface, self.center)


# initialise the pygame
pygame.init()

# create the screen
gameScreen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Rotating Function")
icon = pygame.image.load('space-ship.png')
pygame.display.set_icon(icon)

# Player
playerX = 400
playerY = 300
width = 30
height = 70
space_ship = Player(playerX, playerY, width, height)
offset = height/4

# Game icon
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RGB - Red Green Blue
    gameScreen.fill((255,255,255))
    cursorX, cursorY = pygame.mouse.get_pos()
    space_ship.display(gameScreen, cursorX, cursorY, offset)

    pygame.display.update()
