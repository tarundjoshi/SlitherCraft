import pygame
import random 
from camera import Camera
COLORS = [(255,0,0),(0,255,0),(0,0,255),(255,255,0),(255,0,255),(0,255,255)]
def random_color():
    return random.choice(COLORS)

class orb:
    def __init__(self):
        self.ORB_SIZE = random.randint(1,20)
        self.x = random.randint(-1*1000, 1*1000)
        self.y = random.randint(-1*1000, 1*1000)
        self.color = random_color()
        self.hitbox = pygame.Rect(self.x - self.ORB_SIZE, self.y - self.ORB_SIZE, self.ORB_SIZE*2, self.ORB_SIZE*2)
    def update(self):
        pass
    def render(self, window,camera):
        pygame.draw.circle(window, self.color, camera.translate(self.x,self.y), self.ORB_SIZE)
