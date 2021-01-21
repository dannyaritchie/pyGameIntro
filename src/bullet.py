import pygame
from decimal import *
import math
from globalvariables import *
from pygame.locals import (
    RLEACCEL,
)

#General class for a bullet
class Bullet(pygame.sprite.Sprite):
    #startPosition: [x,y]: for co-ordinates of center of bullets start position
    #destinationPosition: [x,y]: for coordinates of center of bullets end position
    #damage: number: for damage value bullet will pass on to any object it collides with
    #speed: number: number of pixels bullet moves per update
    #image: string: relative file address of image to be used for bullet
    #special: ["",""]: list of string that bullet passes to object it collides with for special effects
    #size: [width,length]: dimensions of bullet 
    def __init__(self, startPosition, destinationPosition, damage=0,speed=0.5,image="",special=[],size=[60,60]):
        #call parent class (pygame.sprite.Sprite) constructor
        super(Bullet, self).__init__()
        #simple assignment of initialisation arguments to instance variable (class variables that are instance specific)
        self.damage = damage
        self.speed=speed
        self.image=image
        self.special=special
        self.size=size

        #these are to keep track of future bullet position, cant use usual .rect provided py pygame as it rounds to nearest pixel which causes bullets to miss at long distance
        self.floatx=float(startPosition[0])
        self.floaty=float(startPosition[1])

        #assignemt of direction instance variable, involves normalisation (dividing each direction by the total distance of the transformation so directions are always 1 pixel long
        magnitude = math.sqrt((destinationPosition[0]-startPosition[0])**2+(destinationPosition[1]-startPosition[1])**2)/10
        self.direction=[float(i-j)/float(magnitude) for i,j in zip(destinationPosition,startPosition)]

        #create surface of apropriate dimensions
        self.surf=pygame.Surface((self.size[0],self.size[1]))
        #if image provided draw image to a surface and resize and use this as bullet surface
        #else draw rectangle to bullet surface
        if self.image != "":
            tempSurface = pygame.image.load(self.image).convert()
            tempSurface.set_colorkey((255, 255, 255), RLEACCEL)
            self.surf=pygame.transform.scale(tempSurface,(self.size[0],self.size[1]))
        else:
            pygame.draw.rect(self.surf,pygame.Color(0,0,255),(0,0,self.size[0],self.size[1]))

        #roate bullet surface by angle to mouse position 
        angle=180/math.pi*math.atan2(destinationPosition[1]-startPosition[1],destinationPosition[0]-startPosition[0])
        if angle<0:
            angle += 360
        self.surf=pygame.transform.rotate(self.surf,-angle+180)

        #provide bullet surface with rectangle coordinates corresponding to bullet position on screen
        self.rect = self.surf.get_rect(center=(startPosition[0],startPosition[1]))

    #update method for moving bullet, checking for collisions and triggering appropriate collision events 
    #takes otherObjects as argument which is a list of the pygame.sprite.Sprite objects that a bullet can collide with
    def update(self,otherObjects):
        #update bullet position to actual decimal position
        self.floatx+=self.direction[0]*self.speed
        self.floaty+=self.direction[1]*self.speed
        #move bullet to closest screen position
        self.rect = self.surf.get_rect(center=(self.floatx,self.floaty))

        #destroy bullet once its gone off screen 
        if self.rect.left < -self.size[0] - 1:
            self.kill()
        if self.rect.right > SCREEN_WIDTH+self.size[0]+1:
            self.kill()
        if self.rect.top <= 0-self.size[1]-1:
            self.kill()
        if self.rect.bottom >= SCREEN_HEIGHT+self.size[1]+1:
            self.kill()
        
        #get list of objects bullet has collided with
        collidedObjects = pygame.sprite.spritecollide(self,otherObjects,False)
        #call collision function for any objects bullet collided with and pass on damage and special instance variables
        for i in collidedObjects:
            i.hitByBullet(self.damage,self.special)
        #if bullet collided with at least one object destroy bullet
        if len(collidedObjects)>0:
            self.kill()

        


