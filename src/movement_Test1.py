import pygame
import sys
import os

SCREENHEIGHT = 500
SCREENWIDTH = 500
fps = 40

class Tank(pygame.sprite.Sprite):
    def __init__(self, speedInput = 0, fireRateInput = 0, damageInput = 0, healthInput = 0, colourInput = 0):
        super(Tank, self).__init__()
        self.surf = pygame.Surface((50, 50))
        pygame.draw.rect(self.surf, pygame.Color(255, 0, 0), (0, 0, 50, 50))
        self.rect = self.surf.get_rect(center=(SCREENWIDTH / 2, SCREENHEIGHT / 2))
        self.speed = speedInput
        self.health = healthInput
        self.fireRate = fireRateInput
        self.damage = damageInput
        self.colour = colourInput
        self.movex = 0
        self.movey = 0

    def control(self, x, y):
        """
        control player movement
        """
        self.movex += x
        self.movey += y

    def update(self):
        """
        Update sprite position
        """

        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode([SCREENWIDTH, SCREENHEIGHT])
redTank = Tank()
running = True
#while running:
    #screen.fill((0, 0, 0))
    #screen.blit(redTank.surf, redTank.rect)
    #pygame.display.flip()
player = Tank()  # spawn player
player.rect.x = 0  # go to x
player.rect.y = 0  # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 2

'''
Main Loop
'''

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    main = False
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps, 0)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0,steps)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0,-steps)


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps, 0)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0, -steps)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0, steps)
    screen.fill((0, 0, 0))
    player.update()
    screen.blit(player.surf, player.rect)
    pygame.display.flip()
    clock.tick(fps)