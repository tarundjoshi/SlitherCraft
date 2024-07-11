import pygame 

class Segment:
    def __init__(self,coords):
        image = pygame.image.load('circlered.png')
        self.hitbox = pygame.Rect(coords[0],coords[1],50,50)
        self.image = pygame.transform.scale(image,(50,50))
    def update(self,target,speed):

        #the unit dist vector in direction of nect segment
        disVec = [target[0] - self.hitbox.x, target[1] - self.hitbox.y]
        dis = (disVec[0]**2 + disVec[1]**2)**0.5 + 0.00001
        disVec = [disVec[0]/dis, disVec[1]/dis]

        #prevent shrinkage
        if(dis < 20):
            return 
        
        #new pos of segment
        self.hitbox.x += disVec[0]*speed
        self.hitbox.y += disVec[1]*speed


    def draw(self,win,camera):
        win.blit(self.image,camera.translate(self.hitbox.x,self.hitbox.y))