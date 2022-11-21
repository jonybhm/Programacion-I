import pygame
import random
from constantes import *
from auxiliar3 import MetodoAuxiliar



class Platform(pygame.sprite.Sprite):
    
    def __init__(self,speed,w,h,type):
        pygame.sprite.Sprite.__init__(self)
        self.image = MetodoAuxiliar.getSurfaceFromSpriteSheet(PATH + r"\\platforms\\platforms.png",3,1)[type]
        self.image = pygame.transform.scale(self.image,(w,h))
        
        self.rect = self.image.get_rect()
        self.x=random.randrange(0 + (self.rect.size[0]),SCREEN_WIDTH//2,(self.rect.size[0])*2)
        self.y=random.randrange(0 + (self.rect.size[0]),SCREEN_HEIGHT - (self.rect.size[0]),(self.rect.size[0])*2)
        self.rect.center = (self.x,self.y)

        self.speed = speed
        self.direction = 1
        self.platform_move_limit = 0

        
    def move_update (self):
        #reiniciar variables de movimiento
        delta_x = 0
        delta_y = 0  

        #variables de movimiento
        if (self.is_move_up):
            delta_y = -self.speed

        if (self.is_move_down):
            delta_y = self.speed

        #actualizar posicion del rectangulo
        self.rect.x += delta_x
        self.rect.y += delta_y

    def platform_wave(self):

        if (self.direction==-1):
            self.is_move_up = False
            self.is_move_down = True
        elif (self.direction==1):
            self.is_move_down = False
            self.is_move_up = True 
                            
        self.move_update()    
        self.platform_move_limit += 1 

        if (self.platform_move_limit > 25):
            self.direction *= -1
            self.platform_move_limit *= -1
            


    #colisiones con plataformas
    def collide_update (self,spell_group,platform_group):
        for spell in spell_group:
            if (pygame.sprite.spritecollide(spell,platform_group,False)):
                spell.kill()   
    

    def draw(self,screen):
        if(DEBUG_MODE):
            pygame.draw.rect(screen,RED,self.rect,1)

        screen.blit(self.image,self.rect)

    def update(self,spell_group,platform_group):
        self.platform_wave()
        self.collide_update(spell_group,platform_group)


        


        