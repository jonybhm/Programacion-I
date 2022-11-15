import pygame
import random
from auxiliar import *
from constantes import *
from spell import *


class Character(pygame.sprite.Sprite):
    def __init__(self,type,x,y,speed,magic,health=100):
        pygame.sprite.Sprite.__init__(self)
        self.is_alive = True
                
        self.health = health
        self.max_health = health

        self.magic = magic
        self.start_magic = magic
        self.spell_cooldown = 0

        self.money = 0

        self.type = type #tipo de personaje player/enemigo/boss
        self.speed = speed #cantidad de pixeles que el personaje se va a mover
        self.x = x
        self.y = y
        
        self.animation_list = []
        self.frame_index = 0
        self.character_action_index = 0
        self.time_update = pygame.time.get_ticks()
        
        if(self.type=="player"):
            #diccionario con nombre de carpeta y cantidad de frames segun accion
            animation_folders_dic = {"idle":16,"death":6,"move":15} 
            #"meele":8,
            for type_folder in animation_folders_dic:
                buffer_list = []     
            
                buffer_list =  Auxiliar.getAnimationListFromSpriteSheet(
                PATH + r"\\{}\\{}.png".format(type,type_folder),
                animation_folders_dic.get(type_folder),1)

                self.animation_list.append(buffer_list)
        elif(self.type=="enemy"):
            #diccionario con nombre de carpeta y cantidad de frames segun accion
            animation_folders_dic = {"idle":6,"death":6} 
            for type_folder in animation_folders_dic:
                buffer_list = []     
            
                buffer_list =  Auxiliar.getAnimationListFromSpriteSheet(
                PATH + r"\\{}\\{}.png".format(type,type_folder),
                animation_folders_dic.get(type_folder),1,False,1,0.75)

                self.animation_list.append(buffer_list)

        elif(self.type=="boss"):
            #diccionario con nombre de carpeta y cantidad de frames segun accion
            animation_folders_dic = {"mid":8,"death":6,"final":8} 
            for type_folder in animation_folders_dic:
                buffer_list = []     
            
                buffer_list =  Auxiliar.getAnimationListFromSpriteSheet(
                PATH + r"\\{}\\{}.png".format(type,type_folder),
                animation_folders_dic.get(type_folder),1,False,1,1)

                self.animation_list.append(buffer_list)
                
        self.image = self.animation_list[self.character_action_index][self.frame_index] 
        
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

        #acciones del jugador
        self.is_move_left = False
        self.is_move_right = False
        self.is_move_up = False
        self.is_move_down = False
        self.is_shoot_spell = False

        #propiedades de los enemigos
        self.direction = 1 #"viendo" hacia arriba
        self.enemy_move_limit = 0 #contador de cuanto se mueve hacia un lado
        self.stop_move = False
        self.stop_move_limit = 0 #contador de cuanto se queda quieto

    
    def move_update (self):
        #reiniciar variables de movimiento
        delta_x = 0
        delta_y = 0  

        #variables de movimiento
        if (self.is_move_left):
            delta_x = -self.speed
              
        if (self.is_move_right):
            delta_x = self.speed

        if (self.is_move_up):
            delta_y = -self.speed

        if (self.is_move_down):
            delta_y = self.speed

        #actualizar posicion del rectangulo
        self.rect.x += delta_x
        self.rect.y += delta_y

    def shooting_spell(self,spell_group):
        if (self.spell_cooldown == 0 and self.magic > 0 and self.is_shoot_spell):
            self.spell_cooldown = 100 #disparo una vez y hay que esperar hasta el siguiente    
            spell = Spell(self.rect.centerx + (self.rect.size[0]),self.rect.centery,speed=10)
            spell_group.add(spell)
            self.magic -= 1 #reduce la cantidad de hechizos en 1
            
    def enemy_actions(self,player):
        if (self.is_alive and player.is_alive):
            if(random.randint(1,300) == 1): #probabilidad de 1/500
                self.stop_move = True
                self.stop_move_limit = 30 
                        
            if (self.stop_move == False):
                if(self.direction==-1):
                    self.is_move_up = False
                    self.is_move_down = True
                elif (self.direction==1):
                    self.is_move_down = False
                    self.is_move_up = True 
                
                self.move_update()    
                self.enemy_move_limit += 1 

                if (self.enemy_move_limit > 20):
                    self.direction *= -1
                    self.enemy_move_limit *= -1
            
            elif(self.stop_move == True):
                self.stop_move_limit -=1 
                if(self.stop_move_limit <= 0):
                    self.stop_move = False


    def cooldown_update(self):
        if (self.spell_cooldown > 0):
            self.spell_cooldown -= 1

    def verify_is_alive_update(self):
        if (self.health <= 0):
            self.health = 0
            self.speed = 0
            self.is_alive = False
            self.action_update(1)
        
    def animation_update(self):
        #avanzar el frame en la animacion
        self.image = self.animation_list[self.character_action_index][self.frame_index]
        #verificar si el tiempo que paso desde la ultima update es maor a la cte ANIMATION_COOLDOWN
        if (pygame.time.get_ticks() - self.time_update > ANIMATION_COOLDOWN):
            self.time_update =  pygame.time.get_ticks()
            self.frame_index += 1
        #loopear la lista de frames
        if (self.frame_index >= len(self.animation_list[self.character_action_index])):
            if (self.character_action_index == 1): #en caso de morir
                self.frame_index = len (self.animation_list[self.character_action_index]) - 1
            else:    
                self.frame_index = 0
        
    def action_update(self,new_ation):
        #verificar accion nueva es disntina a la anterior
        if (new_ation != self.character_action_index):
            self.character_action_index = new_ation
            self.frame_index = 0 #iniciar nueva accion en el frame 0
            self.time_update = pygame.time.get_ticks()

    def global_update(self,group):
        self.animation_update()
        self.cooldown_update()
        self.move_update()
        self.verify_is_alive_update()
        self.shooting_spell(group)
        
        
        

    def draw (self,screen):
        if (DEBUG_MODE):
            pygame.draw.rect(screen,RED,self.rect,1)
        screen.blit(self.image,self.rect)



