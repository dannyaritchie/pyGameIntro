import pygame
class MapObject:
    def __init__(self,name):
        self.name=name
    
    def draw(screen):
        pygame.draw.circle(screen, (0,0,255), (250,250),75)
    
