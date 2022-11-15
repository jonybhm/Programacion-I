import pygame
from constantes import *
from auxiliar import *


class Spell(pygame.sprite.Sprite):
    def __init__(self,x,y,speed):
        pygame.sprite.Sprite.__init__(self)

        self.speed = speed #cantidad de pixeles que el personaje se va a mover
        self.x = x
        self.y = y
        self.time_update = pygame.time.get_ticks()

        self.animation_list = []
        self.frame_index = 0
        self.animation_list = Auxiliar.getAnimationListFromSpriteSheet(
        PATH + r"\\spells\\spell_player.png",6,1)

        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

        self.direction = 1
    
    def animation_update(self):
        #avanzar el frame en la animacion
        self.image = self.animation_list[self.frame_index]
        #verificar si el tiempo que paso desde la ultima update es maor a la cte ANIMATION_COOLDOWN
        if (pygame.time.get_ticks() - self.time_update > ANIMATION_COOLDOWN):
            self.time_update =  pygame.time.get_ticks()
            self.frame_index += 1
        #loopear la lista de frames
        if (self.frame_index >= len(self.animation_list)):
            self.frame_index = 0

    def update(self,player,enemy,group_player,group_enemy):
        #animacion de los hechizos
        self.animation_update()
        #movimiento de los hechizos
        self.rect.x += self.speed
        
        #verificar si los hechizos estan fuera de la pantalla
        if (self.rect.left > SCREEN_WIDTH):
            self.kill() #elimina sprite del grupo

        #verificar si los hechizos colisionan con enemigos/player
        if (pygame.sprite.spritecollide(player,group_enemy,False)):
            if (player.is_alive):
                player.health -= 10
                self.kill()
                group_enemy.remove(enemy)

        if (pygame.sprite.spritecollide(enemy,group_player,False)):
            if (enemy.is_alive):
                enemy.health -= 100
                self.kill()



        
