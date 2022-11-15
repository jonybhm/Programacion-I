import pygame
from constantes import *
from auxiliar import *

class Items(pygame.sprite.Sprite):
    def __init__(self,type,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.type = type #dada la cuadricula: health:1 , money:7 , magic:10
        self.image = Auxiliar.getAnimationListFromSpriteSheet(PATH + r"\\items\\items.png",3,4,scale=0.5)[type]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    

    def update(self,player):
        #verificar si el jugador colisiona con el item
        if (pygame.sprite.collide_rect(self,player)):
            #verificar el tipo de item
            if (self.type == 1): #type health
                player.health += 10
                if (player.health > player.max_health):
                    player.health = player.max_health
            elif (self.type == 7): #type money
                player.money += 10
            elif (self.type == 10): #type magic
                player.magic += 1    
            self.kill()#borra el sprite del grupo

