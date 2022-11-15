import pygame
from constantes import *
from auxiliar import Auxiliar

class Enemy:
    
    def __init__(self,path,frame_rate_ms,move_rate_ms,x,y,speed_x=10,speed_y=0):
        self.spell = path
        self.animation = self.spell
        self.frame = 0
        self.image = self.animation[self.frame]

        self.speed_x = speed_x
        self.speed_y = speed_y
        
        self.rect = self.image.get_rect()
               
        self.rect.x = x
        self.rect.y = y
        
        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms
        self.tiempo_transcurrido_move = 0 
        self.move_rate_ms = move_rate_ms

        self.damage = 10
    

    def do_movement(self,delta_ms,lista_platforms):
        if(not self.collides_platform(lista_platforms)):
            self.tiempo_transcurrido_move += delta_ms
            if(self.tiempo_transcurrido_move >= self.move_rate_ms):
                self.rect.x += self.speed_x
                self.rect.y += self.speed_y

    def collides_platform(self,lista_platforms):
        retorno = False
        for plataforma in lista_platforms:
            if(plataforma.collition_rect.colliderect(self.rect)):
                retorno=True
                
                break

        return retorno    

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms 
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms): 
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0


    def update(self,delta_ms,lista_platforms):
        self.do_movement(delta_ms,lista_platforms)
        self.do_animation(delta_ms)


    def draw(self,screen):
        if (MODO_DEBUG):
            pygame.draw.rect(screen,GREEN,self.rect)

        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)

   