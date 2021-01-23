import pygame
class power_up_object:
    def __init__(self, x, y, r, colour=[255,0,0], time_limit=10, speed_stat):
        self.x = x
        self.y = y
        self.r = r
        self.colour = colour
        self.timer =                        # pygame.clock
        self.time_limit = time_limit
        self.speed_stat = speed_stat + 0.2


