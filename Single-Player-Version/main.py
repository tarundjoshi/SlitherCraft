import pygame
import random
from player import Player
from orbs import orb
from camera import Camera
from segment import Segment
HEIGHT = 1000
WIDTH = 1000
MAXORBS = 30
START_X = 0
START_Y = 0
START_W = 100
START_H= 100
clock = pygame.time.Clock()

class main:
    def __init__(self):
        self.dimensions = (WIDTH, HEIGHT)
        self.window = pygame.display.set_mode(self.dimensions)
        self.run = True
        self.wincolor = (0, 0, 0)
        self.SCORE = 0
        self.food = []
        self.player = Player(START_X, START_Y)
        self.camera = Camera(START_X, START_Y)

    def play(self):
        while self.run:
            clock.tick(60)
            self.update()
            self.render()

    def renderorbs(self,count):
        for i in range(count):
            self.food.append(orb())

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False 
        self.player.update(self.food)
        self.camera.update(self.player.hitbox.x, self.player.hitbox.y)
        
    def render(self):
        self.window.fill(self.wincolor)
        self.player.render(self.window,self.camera)

        #trying to keep number of orbs constant in the space
        self.renderorbs(MAXORBS - len(self.food))
        
        for orb in self.food:
            orb.render(self.window,self.camera)
        pygame.display.update()
