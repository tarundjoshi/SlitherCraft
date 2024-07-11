
import pygame
from segment import Segment

SPEED = 5
ORB_SIZE = 20 #size of player orb
class Player:
    def __init__(self,x,y):
        # image = pygame.image.load('circlered.png')
        self.ORB_SIZE = ORB_SIZE
        self.hitbox = pygame.Rect(x, y, self.ORB_SIZE*2, self.ORB_SIZE*2)
        # self.image = pygame.transform.scale(image,(50,50))
        self.score = 0
        self.segments = [Segment((x,y))]
    def update(self,orbs):
        mousepos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()

        #worldpos is the pos of the head in the realworld
        worldpos = (mousepos[0] - 500 + self.hitbox.x, mousepos[1] - 500 + self.hitbox.y)
        print(worldpos)

        #unit vector in dirn towards mouse from head
        distVec = [worldpos[0] - self.hitbox.x, worldpos[1] - self.hitbox.y]
        dist = (distVec[0]**2 + distVec[1]**2)**0.5 + 0.00001
        self.distVec = [distVec[0]/dist, distVec[1]/dist]

        #boost effect 
        if keys[pygame.K_LSHIFT] and len(self.segments) > 1:
            SPEED = 10
            self.score -= 0.5
            if(self.score < -20):
                self.segments.pop()
                self.score = 0
        else:
            SPEED = 5

        self.hitbox.x += self.distVec[0]*SPEED
        self.hitbox.y += self.distVec[1]*SPEED

        self.segments[0].hitbox.x = self.hitbox.x
        self.segments[0].hitbox.y = self.hitbox.y

        #collision detection
        for orb in orbs:
            if(self.hitbox.colliderect(orb.hitbox)):
                orbs.remove(orb)
                self.score += 5
            #extending snake
            if(self.score >= 20):
                self.score -= 20
                self.addseg()

        #updating the next location of segments in the list
        for i in range(1,len(self.segments)):
            if(i == 0): 
                self.segments[i].update((self.hitbox.x,self.hitbox.y),SPEED)
            else:
                self.segments[i].update((self.segments[i-1].hitbox.x,self.segments[i-1].hitbox.y),SPEED)
    

    def render(self,window,camera):
        # window.blit(self.image, camera.translate(self.hitbox.x,self.hitbox.y))
        pygame.draw.circle(window,(255,0,0),camera.translate(self.hitbox.x + ORB_SIZE,self.hitbox.y + ORB_SIZE),ORB_SIZE)
        pygame.draw.rect(window,(0,255,0),(camera.translate(self.hitbox.x,self.hitbox.y), (40,40)),1)
        for seg in self.segments:
            seg.draw(window,camera)
    
    def addseg(self):
        if(len(self.segments) == 0):
            startx = self.distVec[0]*-1*20 + self.hitbox.x
            starty = self.distVec[1]*-1*20 + self.hitbox.y
            self.segments.append(Segment((startx,starty)))
        else:
            #adding the segment at a distance of approx half radius of the last segment
            startx = self.distVec[0]*-1*20+ self.segments[-1].hitbox.x
            starty = self.distVec[1]*-1*20 + self.segments[-1].hitbox.y
            self.segments.append(Segment((startx,starty)))