import pygame


SCREENHEIGHT = 500
SCREENWIDTH = 500


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


pygame.init()
screen = pygame.display.set_mode([SCREENWIDTH, SCREENHEIGHT])
redTank = Tank()
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(redTank.surf, redTank.rect)
    pygame.display.flip()
