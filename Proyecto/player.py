from doctest import FAIL_FAST
import pygame
from constantes import *
from auxiliar import Auxiliar

class Player:
    def __init__(self,x,y,speed_move,frame_rate_ms,move_rate_ms) -> None:
        self.float_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"player\\float.png",15,1)
        self.float_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"player\\float.png",15,1,True)
        self.float_u = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"player\\float.png",15,1)
        self.float_d = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"player\\float.png",15,1,True)
        self.idle_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"player\\shadow_idle.png",16,1)
        self.idle_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"player\\shadow_idle.png",16,1,True)
        self.meele_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"player\\player_meele.png",8,1)
        self.meele_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"player\\player_meele.png",8,1,True)
        self.meele_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"player\\player_spell.png",8,1)
        self.spell_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"player\\player_spell.png",8,1,True)
        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_move =  speed_move
                    
        self.animation = self.idle_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_meele = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms #se utiliza con delta_ms para determinar en do_animation 
        self.tiempo_transcurrido_move = 0 
        self.move_rate_ms = move_rate_ms #se utiliza con delta_ms para determinar en do_move 

        self.collition_rect = pygame.Rect(self.rect.x+self.rect.w/4
        , self.rect.y +50 , COLLITION_RECT , COLLITION_RECT)

        

    def float(self,direction):
        if(self.direction != direction or (self.animation != self.float_r and self.animation != self.float_l
        and self.animation != self.float_u and self.animation != self.float_d)):

            self.frame = 0 #inicia en el frame 0 de animacion
            self.direction = direction 
            if(direction == DIRECTION_R):
                self.move_x = self.speed_move
                self.animation = self.float_r
            elif(direction == DIRECTION_L):
                self.move_x = -self.speed_move
                self.animation = self.float_l
            elif(direction == DIRECTION_U):
                self.move_y = -self.speed_move
                self.animation = self.float_u
            elif(direction == DIRECTION_D):
                self.move_y = self.speed_move
                self.animation = self.float_d
        

    def idle(self):
        if(self.animation != self.idle_r and self.animation != self.idle_l):
            if(self.direction == DIRECTION_R):
                self.animation = self.idle_r
            else:
                self.animation = self.idle_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def do_movement(self,delta_ms):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            

            self.tiempo_transcurrido_move = 0
            self.add_x(self.rect.x)
            self.add_y(self.rect.y)

            self.collition_rect

    #RECTANGULOS DEL PLAYER
   
    def add_x(self,delta_x):
        self.rect.x += self.move_x
        self.collition_rect.x += self.move_x


    def add_y(self,delta_y):
        self.rect.y += self.move_y
        self.collition_rect.y += self.move_y


            
            
                

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms #mide el tiempo desde que empezo el juego 
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms): 
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0



    def update(self,delta_ms):
        self.do_movement(delta_ms)
        self.do_animation(delta_ms)
        
    
    def draw(self,screen):
        if (MODO_DEBUG):
            pygame.draw.rect(screen,RED,self.rect)
            pygame.draw.rect(screen,GREEN,self.collition_rect)

        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        

    def events(self,delta_ms,keys):
        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
            self.float(DIRECTION_L)
        if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
            self.float(DIRECTION_R)
        if(keys[pygame.K_DOWN] and not keys[pygame.K_UP]):
            self.float(DIRECTION_D)
        if(not keys[pygame.K_DOWN] and keys[pygame.K_UP]):
            self.float(DIRECTION_U)
        if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
            self.idle()
        
        
        if(keys[pygame.K_SPACE]):
            self.is_meele(True)