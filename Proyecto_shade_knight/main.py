import pygame
from constantes import *
from character import *
from auxiliar import *
from spell import *
from items import *


pygame.init()

#pantalla y nombre de ventana
main_screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Shade Knigth")

#setear framerate 
clock = pygame.time.Clock()

#grupos de sprites
spell_group_player = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
spell_group_enemy = pygame.sprite.Group()
items_group = pygame.sprite.Group()

#TEMPORAL
money = Items(type=7,x=100,y=300)
items_group.add(money)
magic = Items(type=10,x=300,y=300)
items_group.add(magic)
health = Items(type=1,x=500,y=300)
items_group.add(health)

player = Character(type="player",x=200,y=200,speed=8,magic=5)

enemy_1 = Character(type="enemy",x=SCREEN_WIDTH,y=200,speed=5,magic=5)
enemy_2 = Character(type="enemy",x=SCREEN_WIDTH,y=500,speed=5,magic=5)
boss_mid = Character(type="boss",x=SCREEN_WIDTH,y=300,speed=3,magic=5)
enemy_group.add(enemy_1)
enemy_group.add(enemy_2)
enemy_group.add(boss_mid)



run = True
while (run):

    clock.tick(FPS)

    draw_bg(screen=main_screen)

    #mostrar salud, dinero y magia en pantalla, texto e imagenes
    show_text_on_screen(0,SCREEN_HEIGHT-20,"SALUD: {0}%".format(player.health),main_screen)
    for i in range(player.health//20):
        health_image = pygame.transform.scale(health.image,(50,50)).convert_alpha()
        main_screen.blit(health_image,((i*20),SCREEN_HEIGHT-70))
    show_text_on_screen(0,0,"MAGIA: X{0}".format(player.magic),main_screen)
    for i in range(player.magic):
        magic_image = pygame.transform.scale(magic.image,(50,50)).convert_alpha()
        main_screen.blit(magic_image,((i*20),20))
    show_text_on_screen(150,0,"DINERO: X{0}".format(player.money),main_screen)
    money_image = pygame.transform.scale(money.image,(50,50)).convert_alpha()
    main_screen.blit(money_image,(150,20))
    
    #draw y upadte de player
    player.draw(screen=main_screen)
    player.global_update(spell_group_player)
   
   
    #metodos draw y update de grupos
   
    for enemy in enemy_group:
        enemy.draw(screen=main_screen)
        enemy.global_update(spell_group_player)
        enemy.enemy_actions(player)
        
        spell_group_player.update(player=player,enemy=enemy,
        group_player=spell_group_player,group_enemy=spell_group_enemy)
        spell_group_player.draw(main_screen)

    items_group.update(player)
    items_group.draw(main_screen)

    #actualizar las acciones del personaje
    if (player.is_alive):
        if (player.is_shoot_spell):
            player.shooting_spell(spell_group_player)
            
        if (player.is_move_left or player.is_move_right or
        player.is_move_up or player.is_move_down):
            player.action_update(2)#actualiza la accion a "2" = "move"
        else:
            player.action_update(0)#actualiza la accion a "0" = "idle"


    event_list = pygame.event.get()
    for event in event_list:
        #salir del juego
        if (event.type == pygame.QUIT):
            run = False
        #eventos de teclado presionado
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_a):
                player.is_move_left = True
            if (event.key == pygame.K_d):
                player.is_move_right = True
            if (event.key == pygame.K_w):
                player.is_move_up = True
            if (event.key == pygame.K_s):
                player.is_move_down = True
            if (event.key == pygame.K_SPACE):
                player.is_shoot_spell = True
                
        #eventos de teclado al soltar  
        if (event.type == pygame.KEYUP):
            if (event.key == pygame.K_a):
                player.is_move_left = False
            if (event.key == pygame.K_d):
                player.is_move_right = False              
            if (event.key == pygame.K_w):
                player.is_move_up = False
            if (event.key == pygame.K_s):
                player.is_move_down = False
            if (event.key == pygame.K_SPACE):
                player.is_shoot_spell = False

    pygame.display.update()



pygame.quit()
