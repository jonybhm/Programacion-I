import pygame
from constantes import *
from auxiliar import Auxiliar

class Platform:
    
    def __init__(self,speed,x,y,w,h,type=0):
        self.image = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"platforms\\platforms.png",3,1)[type]
        self.image = pygame.transform.scale(self.image,(w,h))
        self.collition_rect = self.image.get_rect()
        self.collition_rect.x = x
        self.collition_rect.y = y
        self.speed = speed
        

        self.life = 10

        
        self.animation = self.image
        
    def movement(self): 
        pass
        #self.collition_rect.y =  #movimiento !!

    def update(self,delta_ms):
        self.movement()
        

    def draw(self,screen):
        if(MODO_DEBUG):
            pygame.draw.rect(screen,RED,self.collition_rect)

        screen.blit(self.image,self.collition_rect)

        


        