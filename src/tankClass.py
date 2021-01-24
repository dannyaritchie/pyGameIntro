import pygame
from bullet import Bullet
from pygame.locals import *
SCREENHEIGHT = 500
SCREENWIDTH = 500


class Tank(pygame.sprite.Sprite):
    def __init__(self, speedInput = 0, fireRateInput = 500, damageInput = 20, healthInput = 100, colourInput = 0,
                 position = (SCREENWIDTH / 2, SCREENHEIGHT / 2)):
        super(Tank, self).__init__()
        self.surf = pygame.Surface((50, 50))
        pygame.draw.rect(self.surf, pygame.Color(255, 0, 0), (0, 0, 50, 50))
        self.rect = self.surf.get_rect(center=position)
        self.speed = speedInput
        self.health = healthInput
        self.fireRate = fireRateInput
        self.damage = damageInput
        self.colour = colourInput
        self.shotAvailable = True
        self.startReloadTime = None

    def hitByBullet(self, bulletDamage, special):
        self.health -= bulletDamage
        if self.health <= 0:
            self.kill()

    def update(self, bullet, pressedKeys):
        if not self.shotAvailable:
            if pygame.time.get_ticks()-self.startReloadTime > self.fireRate:
                self.shotAvailable = True
        if pressedKeys[K_SPACE]:
            if self.shotAvailable:
                bullet=Bullet([self.rect.x, self.rect.y], pygame.mouse.get_pos(), image="../gallery/bullet.png",
                              speed=0.1, damage=self.damage, unhittable=self)
                bullets.add(bullet)
                self.shotAvailable = False
                self.startReloadTime = pygame.time.get_ticks()


pygame.init()
screen = pygame.display.set_mode([SCREENWIDTH, SCREENHEIGHT])
redTank = Tank()
blueTank = Tank(position=(0, 0))
tanks = pygame.sprite.Group()
tanks.add(redTank, blueTank)
bullets = pygame.sprite.Group()
collisionObject = pygame.sprite.Group()
collisionObject.add(blueTank, redTank)
running = True


while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    for item in tanks:
        screen.blit(item.surf, item.rect)
    for bulletItem in bullets:
        bulletItem.update(collisionObject)
    pressedKeys = pygame.key.get_pressed()
    for item in tanks:
        item.update(bullets, pressedKeys)
    for bulletItem in bullets:
        screen.blit(bulletItem.surf, bulletItem.rect)
    pygame.display.flip()
