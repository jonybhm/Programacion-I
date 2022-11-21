import pygame
import json
from constantes import *
from character import *
from auxiliares import *
from spell import *
from items import *
from plataforma import *
from level import *
from manager import *
from button import *

pygame.init()

#pantalla y nombre de ventana
main_screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Shade Knigth")

#player
player = Character(char_type="player",x=200,y=200,speed=8,magic=5)
spell_group_player = pygame.sprite.Group()

#informacion del nivel
game_start = False
game_pause = False
menu_selected = "main"
level_number = 0
level_info = load_json(PATH + r"\\level\\level_info.json")

level = Level(total_items=level_info[level_number]["number_max_items"],background=level_info[level_number]["background"],
max_platforms=level_info[level_number]["number_max_platform"],platform_type=level_info[level_number]["platform_type"],
platform_height=level_info[level_number]["platform_height"],platform_width=level_info[level_number]["platform_width"],
music=level_info[level_number]["music"])
#background
imagen_scroll = level.generate_background()
#items
health=level.generate_health_update()
magic=level.generate_magic_update()
money=level.generate_money_update()
items_group = level.items_group
#platforms
level.generate_platforms()
platform_group = level.platform_group
#enemies
enemies = EnemyManager(total_enemies=level_info[level_number]["number_max_enemies"],
enemy_type=level_info[level_number]["enemy_type"],enemy_timer=level_info[level_number]["enemy_timer"],
enemy_health=level_info[level_number]["enemy_health"],enemy_scale=level_info[level_number]["enemy_scale"])
enemies.manage_enemies_update(player)
enemy_group = enemies.managed_enemy_group
spell_group_enemy = level.spell_group_enemy

#musica menu ppal
if(game_start == False):    
    #musica menu ppal
    pygame.mixer.music.load(PATH + r"\\music\\main_menu.wav")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1,0.0,7000)

#setear framerate 
clock = pygame.time.Clock()

scroll = 0 #variable scrolling
tiles = math.ceil(SCREEN_WIDTH /imagen_scroll.get_width()) + 1 #eliminar buffering



run = True

while (run):

    clock.tick(FPS) 
         

    if (game_start == False): 
        
        if (menu_selected == "main"):#menu principal
            
            #FONDO menu ppal
            imagen_menu = pygame.image.load(PATH + r"\\menu\\menu_widget.png").convert_alpha()
            imagen_menu = pygame.transform.scale(imagen_menu,(SCREEN_WIDTH,SCREEN_HEIGHT))
            main_screen.blit(imagen_menu,(0,0))
            
            #BOTONES instancio y dibujo en pantalla que toma la imagen del menu
            menu_ppal_subtitle = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-200,text="MENU PRINCIPAL",screen=main_screen,font_size=50)
            menu_ppal_title = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-300,text="SHADE KNIGHT",screen=main_screen,font_size=75)
            button_start = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-100,text="COMENZAR",screen=main_screen)
            button_level_select = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2,text="SELECCIONAR NIVEL",screen=main_screen)
            button_options = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+100,text="OPCIONES",screen=main_screen)
            button_exit = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+200,text="SALIR",screen=main_screen)
            menu_ppal_title.draw()
            menu_ppal_subtitle.draw()
            button_start.draw()
            button_exit.draw()
            button_level_select.draw()
            button_options.draw()
            #ACCIONES DE BOTONES
            if(button_start.button_pressed()):
                game_start = True
                pygame.mixer.music.stop()
                level.generate_music()
            if(button_level_select.button_pressed()):
                menu_selected = "levels"
            if(button_options.button_pressed()):
                menu_selected = "options"
            if(button_exit.button_pressed()):
                run = False
        if (menu_selected == "options"):#menu principal
            #FONDO menu opciones
            imagen_menu = pygame.image.load(PATH + r"\\menu\\menu_widget.png").convert_alpha()
            imagen_menu = pygame.transform.scale(imagen_menu,(SCREEN_WIDTH,SCREEN_HEIGHT))
            main_screen.blit(imagen_menu,(0,0))
            
            #BOTONES instancio y dibujo en pantalla que toma la imagen del menu
            options_subtitle = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-200,text="OPCIONES",screen=main_screen,font_size=50)
            options_title = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-300,text="SHADE KNIGHT",screen=main_screen,font_size=75)
            button_music_on = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-100,text="MUSIC ON",screen=main_screen)
            button_music_off = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2,text="MUSIC OFF",screen=main_screen)
            button_full_screen = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+100,text="PANTALLA COMPLETA",screen=main_screen)
            button_back = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+200,text="VOLVER",screen=main_screen)
            options_title.draw()
            options_subtitle.draw()
            button_music_on.draw()
            button_back.draw()
            button_music_off.draw()
            button_full_screen.draw()
            #ACCIONES DE BOTONES
            if(button_music_on.button_pressed()):
                pygame.mixer.music.unpause()
            if(button_music_off.button_pressed()):
                pygame.mixer.music.pause()
            if(button_full_screen.button_pressed()):
               pass
            if(button_back.button_pressed()):
                menu_selected = "main"
                
        if (menu_selected == "levels"):#menu principal
            #FONDO menu opciones
            imagen_menu = pygame.image.load(PATH + r"\\menu\\menu_widget.png").convert_alpha()
            imagen_menu = pygame.transform.scale(imagen_menu,(SCREEN_WIDTH,SCREEN_HEIGHT))
            main_screen.blit(imagen_menu,(0,0))
            
            #BOTONES instancio y dibujo en pantalla que toma la imagen del menu
            levels_subtitle = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-200,text="ELEGIR NIVEL",screen=main_screen,font_size=50)
            levels_title = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-300,text="SHADE KNIGHT",screen=main_screen,font_size=75)
            button_level_1 = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-100,text="NIVEL 1",screen=main_screen)
            button_level_2 = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2,text="NIVEL 2",screen=main_screen)
            button_level_3 = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+100,text="NIVEL 3",screen=main_screen)
            button_back = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+200,text="VOLVER",screen=main_screen)
            levels_title.draw()
            levels_subtitle.draw()
            button_level_1.draw()
            button_back.draw()
            button_level_2.draw()
            button_level_3.draw()
            #ACCIONES DE BOTONES
            if(button_level_1.button_pressed()):
                level_number = 0
                game_start = True
            if(button_level_2.button_pressed()):
                level_number = 1
                game_start = True
            if(button_level_3.button_pressed()):
                level_number = 2
                game_start = True
            if(button_back.button_pressed()):
                menu_selected = "main"
    
    elif (game_pause == True): #menu pausa        
        
        #BOTONES instancio y dibujo en pantalla nueva que corresponde al nivel
        menu_pause_subtitle = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-200,text="PAUSA",screen=main_screen,font_size=50)
        menu_pause_title = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-300,text="SHADE KNIGHT",screen=main_screen,font_size=75)
        button_resume = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-100,text="VOLVER AL NIVEL",screen=main_screen)
        button_level_restart = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2,text="REINICIAR NIVEL",screen=main_screen)
        button_options = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+100,text="MUSICA: ON/OFF",screen=main_screen)
        button_return_main_menu = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+200,text="VOLVER AL MENU",screen=main_screen)
        menu_pause_title.draw()
        menu_pause_subtitle.draw()
        button_resume.draw()
        button_return_main_menu.draw()
        button_level_restart.draw()
        button_options.draw()
        #ACCIONES DE BOTONES
        if(button_resume.button_pressed()):
            game_pause = False
        if(button_level_restart.button_pressed()):
            '''restart_level(spell_group_player,spell_group_enemy,platform_group,items_group,level_number)
            #background
            imagen_scroll = level.generate_background()
            #items
            health=level.generate_health_update()
            magic=level.generate_magic_update()
            money=level.generate_money_update()
            items_group = level.items_group
            #platforms
            level.generate_platforms()
            platform_group = level.platform_group
            
            restart_enemies(enemy_group,level_number)
            #enemies
            enemies.manage_enemies_update(player)
            enemy_group = enemies.managed_enemy_group
            spell_group_enemy = level.spell_group_enemy
'''            
            pass
        if(button_return_main_menu.button_pressed()):
            game_start = False
            menu_selected = "main"

    else:
         

        #pantalla scrolling en el fondo
        i = 0
        while(i < tiles):
            main_screen.blit(imagen_scroll, (imagen_scroll.get_width()*i+ scroll, 0)) #appendea la imagen de fondo al final de la misma imagen
            i += 1
        scroll -= 6  #frame para el scrolling
        if abs(scroll) > imagen_scroll.get_width():
            scroll = 0 #resetear el frame de scroll

        #draw y upadte de player
        player.draw(screen=main_screen)
        player.update(platform_group)

        #metodos draw y update de grupos
        
        for enemy in enemy_group:
            enemy.draw(screen=main_screen)
            enemy.update()
            enemy.enemy_actions(player,spell_group_enemy)

        for platform in platform_group:
            platform.draw(main_screen)
            platform.update(spell_group_enemy,platform_group)
                    
        spell_group_player.update(player,spell_group_player,spell_group_enemy,enemy_group)
        spell_group_player.draw(main_screen)

        spell_group_enemy.update(player,spell_group_player,spell_group_enemy,enemy_group)
        spell_group_enemy.draw(main_screen)

        items_group.update(player)
        items_group.draw(main_screen)
        #actualiza timer de items
        level.update() 
        #update timer enemigos
        enemies.update(player)

        #mostrar info en pantalla / MODO DEBUG
        if (DEBUG_MODE): 
            show_text_on_screen(0,SCREEN_HEIGHT-175,"SMALL SPELL COOLDOWN: {0}".format(player.spell_small_cooldown),main_screen,font_size=25)
            show_text_on_screen(0,SCREEN_HEIGHT-150,"SPELL COOLDOWN: {0}".format(player.spell_cooldown),main_screen,font_size=25)
            show_text_on_screen(0,SCREEN_HEIGHT-25,"SCORE: {0}".format(player.score),main_screen,font_size=25)
            show_text_on_screen(0,SCREEN_HEIGHT-50,"ENEMY TIMER: {0}".format(enemies.timer),main_screen,font_size=25)
            show_text_on_screen(0,SCREEN_HEIGHT-75,"MONEY TIMER: {0}".format(level.timer_money),main_screen,font_size=25)
            show_text_on_screen(0,SCREEN_HEIGHT-100,"HEALTH TIMER: {0}".format(level.timer_health),main_screen,font_size=25)
            show_text_on_screen(0,SCREEN_HEIGHT-125,"MAGIC TIMER: {0}".format(level.timer_magic),main_screen,font_size=25)

            
        #mostrar salud, dinero y magia en pantalla, texto e imagenes
        
        show_text_on_screen(25,0,"SALUD: {0}%".format(player.health),main_screen,font_size=25)
        health_image = pygame.image.load(PATH + r"\\items\\health_icon.png")
        health_image = pygame.transform.scale(health_image,(25,25)).convert_alpha()
        main_screen.blit(health_image,(0,0))
        show_text_on_screen(25,25,"MAGIA: X{0}".format(player.magic),main_screen,font_size=25)
        magic_image = pygame.image.load(PATH + r"\\items\\magic_icon.png")
        magic_image = pygame.transform.scale(magic_image,(25,25)).convert_alpha()
        main_screen.blit(magic_image,(0,25))
        show_text_on_screen(25,50,"DINERO: X{0}".format(player.money),main_screen,font_size=25)
        money_image = pygame.image.load(PATH + r"\\items\\money_icon.png")
        money_image = pygame.transform.scale(money_image,(25,25)).convert_alpha()
        main_screen.blit(money_image,(0,50))

        #actualizar las acciones del personaje
        if (player.is_alive):
            if (player.is_shoot_spell):
                player.shooting_spell(spell_group_player)
            if (player.is_shoot_spell_small):
                player.shooting_spell_small(spell_group_player)
                
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
            if (event.key == pygame.K_LSHIFT):
                player.is_shoot_spell_small = True
            if (event.key == pygame.K_ESCAPE):
                game_pause = True
                
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
            if (event.key == pygame.K_LSHIFT):
                player.is_shoot_spell_small = False

    pygame.display.update()



pygame.quit()
