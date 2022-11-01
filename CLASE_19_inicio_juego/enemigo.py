from doctest import FAIL_FAST
import pygame
from constantes import *
from auxiliar import Auxiliar

class Enemy:
    def __init__(self,x,y,speed_walk,gravity) -> None:
        self.walk = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"inhabitants\\dust\\walk_right.png",9,1,True)
        self.idle = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"inhabitants\\dust\\idle.png",9,20)
        
        self.frame = 0
        
        self.move_x = -x
        self.move_y = y
        self.speed_walk =  speed_walk
        self.gravity = gravity
        
        self.animation = self.idle
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()

    


    def update(self):
        if(self.frame < len(self.animation) - 1):
            self.frame += 1 
        else: 
            self.frame = 0
            
        
        self.rect.x += self.move_x
        #self.rect.y += self.move_y
        
        if(self.rect.y < 550):
            self.rect.y += self.gravity
            self.move_x = self.speed_walk
            self.animation = self.walk
            #self.frame = 0
    
    def draw(self,screen):
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        


