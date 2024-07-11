import pygame
class Camera:
    def __init__(self,x,y):
      self.x = x
      self.y = y
    def update(self,player_x,player_y):
       self.x = player_x
       self.y = player_y
       
    #shifting of origin
    def translate(self,x,y):
       return (x - self.x + 475, y - self.y + 475)
       
    
