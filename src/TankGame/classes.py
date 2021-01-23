import pygame
from math import *


class Tank(pygame.sprite.Sprite):
    def __init__(self, x_position, y_position, width, height, speedInput=0, fireRateInput=0, damageInput=0,
                 healthInput=0, colourInput=0):
        super(Tank, self).__init__()
        self.baseSurf = pygame.transform.scale(pygame.image.load("base.png"), (width, height))
        self.turretSurf = pygame.transform.scale(pygame.image.load("turret.png"), (int(width / 1.5), height))
        self.rotatedBaseSurf = self.baseSurf
        self.rotatedTurretSurf = self.turretSurf
        self.speed = speedInput
        self.health = healthInput
        self.fireRate = fireRateInput
        self.damage = damageInput
        self.colour = colourInput
        self.x = x_position
        self.y = y_position
        self.offset = height / 3
        self.baseCenter = (self.x - width / 2, self.y - height / 2)
        self.turretCenter = (self.x - width / 2, self.y - height / 2)

    def update(self, bullet, pressedKeys):
        if not self.shotAvailable:
            if pygame.time.get_ticks()-self.startReloadTime > self.fireRate:
                self.shotAvailable = True
        if pressedKeys[K_SPACE]:
            if self.shotAvailable:
                bullet=Bullet([self.rect.x, self.rect.y], pygame.mouse.get_pos(), image="../gallery/bullet.png", speed=0.1)
                bullets.add(bullet)
                self.shotAvailable = False
                self.startReloadTime = pygame.time.get_ticks()

    def move(self, directions):
        if directions[0] == 0 | directions[1] == 0:
            coeff = 1
        else:
            coeff = 0.7071067
        self.x += directions[0] * self.speed * coeff
        self.y += directions[1] * self.speed * coeff

    def rotate_base(self, directions):
        angle = atan2(directions[0], directions[1]) * (180 / pi)
        self.rotatedBaseSurf = pygame.transform.rotate(self.baseSurf, angle)
        self.baseCenter = (self.x - self.rotatedBaseSurf.get_width() / 2,
                            self.y - self.rotatedBaseSurf.get_height() / 2)

    def rotate_turret(self, cursorPosition):
        dx, dy = cursorPosition[0] - self.x, cursorPosition[1] - self.y
        angle = -90 - atan2(dy, dx) * (180 / pi)
        self.rotatedTurretSurf = pygame.transform.rotate(self.turretSurf, angle)
        self.turretCenter = (self.x - self.rotatedTurretSurf.get_width() / 2 - self.offset * sin(angle * (pi / 180)),
                             self.y - self.rotatedTurretSurf.get_height() / 2 - self.offset * cos(angle * (pi / 180)))

    def update(self, cursor, moveDirections):
        self.move(moveDirections)
        self.rotate_turret(cursor)
        self.rotate_base(moveDirections)

    def display(self, screen):
        screen.blit(self.rotatedBaseSurf, self.baseCenter)
        screen.blit(self.rotatedTurretSurf, self.turretCenter)