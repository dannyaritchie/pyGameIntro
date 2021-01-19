# Simple pygame program
# Import and initialize the pygame library
import pygame
import random
import math
from objects.mapObject import MapObject
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
def consumeCollision(collider,collidees):
    collidedSprites = pygame.sprite.spritecollide(collider,collidees,True)
def distanceBetweenRects(recta,rectb):
    #function to get squared euclidian distance between two rectangle (i think x,y are top left corner but am not sure)
    return (recta.x-rectb.x)**2+(recta.y-rectb.y)**2
def moveRectaTowardsRectb(recta,rectb,units):
    #gives x,y translation for recta to move towards rectb by units amount
    distance=distanceBetweenRects(recta,rectb)
    xjump = units*(rectb.x-recta.x)/math.sqrt(distance+1)
    yjump = units*(rectb.y-recta.y)/math.sqrt(distance+1)
    return (xjump,yjump)

class gPlayer(pygame.sprite.Sprite):
    def __init__(self):
        super(gPlayer, self).__init__()
    mass = 50
    def eatFood(self,foodMass):
       self.mass += foodMass
    def update(self):
        self.surf=pygame.transform.scale(self.surf,(self.mass,self.mass))
        self.rect.w=self.mass
        self.rect.h=self.mass
    # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
    def goToNearestFood(self,foods):
        minDist=999999
        for food in foods:
            print(distanceBetweenRects(self.rect,food.rect))
            if distanceBetweenRects(self.rect,food.rect) < minDist:
                nearestFood = food
                minDist=distanceBetweenRects(self.rect,food.rect)
        if minDist < 999999:
            translation=moveRectaTowardsRectb(self.rect,nearestFood.rect,2)
            self.rect.move_ip(translation)
class aiAPlayer(gPlayer):
    #ai player that runs from other team if they are close and runs towards food if not
    def __init__(self):
        super(aiAPlayer, self).__init__()
        self.surf=pygame.Surface((50,50))
        pygame.draw.rect(self.surf,pygame.Color(255,0,0),(0,0,50,50))
        self.rect = self.surf.get_rect(
                center=(
                    random.randint(0, SCREEN_WIDTH),
                    random.randint(0, SCREEN_HEIGHT),
                ))

    def update(self, enemies,foods):
        #find closest food
        super().update()
        minDist=999999
        nearestFood=0
        print(len(foods))
        nearestEnemyDist=999999
        nearestEnemy=0
        for enemy in enemies:
            if distanceBetweenRects(self.rect,enemy.rect)<nearestEnemyDist:
                if enemy.mass>self.mass:
                    nearestEnemy=enemy
                    nearestEnemyDist=distanceBetweenRects(self.rect,enemy.rect)
        if nearestEnemyDist<20:
            translation=moveRectaTowardsRectb(nearestEnemy.rect,self.rect,2)
            self.rect.move_ip(translation)
        else:
            super().goToNearestFood(foods)
class aiBPlayer(gPlayer):
    #ai player that eats smaller enemies otherwise gets food
    def __init__(self):
        super(aiBPlayer, self).__init__()
        self.surf=pygame.Surface((50,50))
        pygame.draw.rect(self.surf,pygame.Color(0,255,0),(0,0,50,50))
        self.rect = self.surf.get_rect(center=(random.randint(0, SCREEN_WIDTH),random.randint(0, SCREEN_HEIGHT),))
    def update(self,enemies,food):
        super().update()
        nearestEnemyDist=999999
        nearestEnemy=0
        for enemy in enemies:
            if enemy.mass<self.mass:
                    nearestEnemy=enemy
                    nearestEnemyDist=distanceBetweenRects(self.rect,enemy.rect)
        if nearestEnemyDist<999999:
            translation=moveRectaTowardsRectb(self.rect,nearestEnemy.rect,2)
            self.rect.move_ip(translation)
        else:
            super().goToNearestFood(foods)






class Player(gPlayer):
    def __init__(self):
        super(Player, self).__init__()
        tempSurface = pygame.image.load("../gallery/james.png").convert()
        tempSurface.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf=pygame.transform.scale(tempSurface,(self.mass,self.mass))
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        super().update()
        if pressed_keys[K_UP]:
           # self.rect.inflate_ip(0.01,0.01)
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        tempSurface = pygame.image.load("../gallery/carrot.jpg").convert()
        tempSurface.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf=tempSurface
        self.surf=pygame.transform.scale(tempSurface,(200,20))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(1, 5)
    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class Food(pygame.sprite.Sprite):
    def __init__(self):
        super(Food, self).__init__()
        self.surf=pygame.Surface((10,10))
        pygame.draw.rect(self.surf,pygame.Color(255,140,0),(0,0,10,10))
        self.rect = self.surf.get_rect(
                center=(
                    random.randint(0, SCREEN_WIDTH),
                    random.randint(0, SCREEN_HEIGHT),
                ))
        ''' pygame.draw.circle(self.surf,(50,50,50),(10,10),50)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0, SCREEN_WIDTH),
                random.randint(0, SCREEN_HEIGHT),
            )
        )'''


pygame.init()


# Define constants for the screen width and height
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800

# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 1150)

# Create new event for adding foo
ADDFOOD = pygame.USEREVENT+2
pygame.time.set_timer(ADDFOOD,1000)
#Instantiate player
player=Player()
aiAPlayer=aiAPlayer()
aiBPlayer=aiBPlayer()
# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
foods = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player,aiAPlayer,aiBPlayer)


# Run until the user asks to quit
running = True
# Main loop

while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
        # Add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        elif event.type==ADDFOOD:
            new_food = Food()
            foods.add(new_food)
            all_sprites.add(new_food)
    # Fill the screen with black
    screen.fill((0, 0, 0))
    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        # If so, then remove the player and stop the loop
        player.kill()
        running = False
   # if pygame.sprite.spritecollideany(player, foods):
   #     print("H")
   #     player.kill()
   #     running = False
    collidedSprites = pygame.sprite.spritecollide(player,foods,True)
    player.eatFood(10*len(collidedSprites))
    aiAcollidedSprites = pygame.sprite.spritecollide(aiAPlayer,foods,True)
    aiAPlayer.eatFood(10*len(aiAcollidedSprites))
    aiBcollidedSprites = pygame.sprite.spritecollide(aiBPlayer,foods,True)
    aiBPlayer.eatFood(10*len(aiBcollidedSprites))
    print(player.mass)

    #player.mutualAnnihilation(foods)
    #get keys pressed
    pressed_keys = pygame.key.get_pressed()
    #update player
    player.update(pressed_keys)
    # Update enemy position
    enemies.update()
    aiAPlayer.update([aiBPlayer],foods)
    aiBPlayer.update([aiAPlayer],foods)
    #draw player
    screen.blit(player.surf, player.rect)
    #update screen
    pygame.display.flip()


pygame.quit()
