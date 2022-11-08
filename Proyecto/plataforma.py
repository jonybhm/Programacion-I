import pygame
from constantes import *
from auxiliar import Auxiliar




class Platform:
    
    def __init__(self,x,y,w,h,type=0):
        self.image = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"platforms\platforms.png",3,1)[type]
        self.image = pygame.transform.scale(self.image,(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        

    def draw(self,screen):
        if(MODO_DEBUG):
            pygame.draw.rect(screen,RED,self.rect)

        screen.blit(self.image,self.rect)

        