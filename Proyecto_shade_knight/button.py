import pygame
from auxiliar import *
from constantes import *



class FormMainMenu():
    def __init__(self,main_screen):
        
        self.is_active = False
        #FONDO menu ppal
        self.imagen_menu = pygame.image.load(PATH + r"\\menu\\menu_widget.png").convert_alpha()
        self.imagen_menu = pygame.transform.scale(self.imagen_menu,(SCREEN_WIDTH,SCREEN_HEIGHT))
        main_screen.blit(self.imagen_menu,(0,0))
        
        #BOTONES instancio y dibujo en pantalla que toma la imagen del menu
        self.menu_ppal_subtitle = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-200,text="MENU PRINCIPAL",screen=main_screen,font_size=50)
        self.menu_ppal_title = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-300,text="SHADE KNIGHT",screen=main_screen,font_size=75)
        self.button_start = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-100,text="COMENZAR",screen=main_screen)
        self.button_level_select = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2,text="SELECCIONAR NIVEL",screen=main_screen)
        self.button_options = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+100,text="OPCIONES",screen=main_screen)
        self.button_exit = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+200,text="SALIR",screen=main_screen)
    
    def draw(self):
        self.menu_ppal_title.draw()
        self.menu_ppal_subtitle.draw()
        self.button_start.draw()
        self.button_exit.draw()
        self.button_level_select.draw()
        self.button_options.draw()
        
        #ACCIONES DE BOTONES
        
    def event_start(self,level):  
        if(self.button_start.button_pressed()):
            game_start = True
            pygame.mixer.music.stop()
            level.generate_music()
            return game_start

    def event_level_select_options(self): 
        if(self.button_level_select.button_pressed()):
            menu_selected = "levels"
            return menu_selected

        if(self.button_options.button_pressed()):
            menu_selected = "options"
            return menu_selected

    def event_exit(self): 
        if(self.button_exit.button_pressed()):
            run = False
            return run
    
    def update(self):
        self.draw()
        '''self.event_start(level)
        self.event_exit()
        self.event_level_select_options()'''
        

class FormOptions():
    def __init__(self,main_screen):
        
        self.is_active = False

        #FONDO menu opciones
        self.imagen_menu = pygame.image.load(PATH + r"\\menu\\menu_widget.png").convert_alpha()
        self.imagen_menu = pygame.transform.scale(self.imagen_menu,(SCREEN_WIDTH,SCREEN_HEIGHT))
        main_screen.blit(self.imagen_menu,(0,0))
        
        #BOTONES instancio y dibujo en pantalla que toma la imagen del menu
        self.options_subtitle = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-200,text="OPCIONES",screen=main_screen,font_size=50)
        self.options_title = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-300,text="SHADE KNIGHT",screen=main_screen,font_size=75)
        self.button_music_on = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-100,text="MUSIC ON",screen=main_screen)
        self.button_music_off = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2,text="MUSIC OFF",screen=main_screen)
        self.button_full_screen = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+100,text="PANTALLA COMPLETA",screen=main_screen)
        self.button_back = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+200,text="VOLVER",screen=main_screen)
        
    def draw(self):        
        self.options_title.draw()
        self.options_subtitle.draw()
        self.button_music_on.draw()
        self.button_back.draw()
        self.button_music_off.draw()
        self.button_full_screen.draw()
    
    def events(self):
        #ACCIONES DE BOTONES
        if(self.button_music_on.button_pressed()):
            pygame.mixer.music.unpause()
        if(self.button_music_off.button_pressed()):
            pygame.mixer.music.pause()
        if(self.button_full_screen.button_pressed()):
            pass
        if(self.button_back.button_pressed()):
            menu_selected = "main"
            return menu_selected
            
    def update(self):
        self.draw()
        self.events()

class FormLevelSelect():
    def __init__(self,main_screen):
        
        self.is_active = False

        #FONDO menu opciones
        self.imagen_menu = pygame.image.load(PATH + r"\\menu\\menu_widget.png").convert_alpha()
        self.imagen_menu = pygame.transform.scale(self.imagen_menu,(SCREEN_WIDTH,SCREEN_HEIGHT))
        main_screen.blit(self.imagen_menu,(0,0))
        
        #BOTONES instancio y dibujo en pantalla que toma la imagen del menu
        self.levels_subtitle = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-200,text="ELEGIR NIVEL",screen=main_screen,font_size=50)
        self.levels_title = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-300,text="SHADE KNIGHT",screen=main_screen,font_size=75)
        self.button_level_1 = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-100,text="NIVEL 1",screen=main_screen)
        self.button_level_2 = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2,text="NIVEL 2",screen=main_screen)
        self.button_level_3 = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+100,text="NIVEL 3",screen=main_screen)
        self.button_back = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+200,text="VOLVER",screen=main_screen)
    
    def draw(self):
        self.levels_title.draw()
        self.levels_subtitle.draw()
        self.button_level_1.draw()
        self.button_back.draw()
        self.button_level_2.draw()
        self.button_level_3.draw()
    
    def events(self,spell_group_player):
        #ACCIONES DE BOTONES
        if(self.button_level_1.button_pressed()):
            player = restart_player()
            level = restart_level(spell_group_player,spell_group_enemy,platform_group,items_group,level_number=0)
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
            
            enemies = restart_enemies(enemy_group,level_number=0)
            #enemies
            enemies.manage_enemies_update(player)
            enemy_group = enemies.managed_enemy_group
            spell_group_enemy = level.spell_group_enemy
            level_number=0
            game_start = True
            pygame.mixer.music.stop()
            level.generate_music()
        if(self.button_level_2.button_pressed()):
            player = restart_player()
            level = restart_level(spell_group_player,spell_group_enemy,platform_group,items_group,level_number=1)
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
            
            enemies = restart_enemies(enemy_group,level_number=1)
            #enemies
            enemies.manage_enemies_update(player)
            enemy_group = enemies.managed_enemy_group
            spell_group_enemy = level.spell_group_enemy
            level_number=1
            game_start = True
            pygame.mixer.music.stop()
            level.generate_music()
        if(self.button_level_3.button_pressed()):
            player = restart_player()
            level = restart_level(spell_group_player,spell_group_enemy,platform_group,items_group,level_number=2)
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
            
            enemies = restart_enemies(enemy_group,level_number=2)
            #enemies
            enemies.manage_enemies_update(player)
            enemy_group = enemies.managed_enemy_group
            spell_group_enemy = level.spell_group_enemy
            level_number=2
            game_start = True
            pygame.mixer.music.stop()
            level.generate_music()
        if(self.button_back.button_pressed()):
            menu_selected = "main"

class FormPause():
    def __init__(self,main_screen):
        
        self.is_active = False

        #BOTONES instancio y dibujo en pantalla nueva que corresponde al nivel
        self.menu_pause_subtitle = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-200,text="PAUSA",screen=main_screen,font_size=50)
        self.menu_pause_title = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-300,text="SHADE KNIGHT",screen=main_screen,font_size=75)
        self.button_resume = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2-100,text="VOLVER AL NIVEL",screen=main_screen)
        self.button_level_restart = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2,text="REINICIAR NIVEL",screen=main_screen)
        self.button_options = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+100,text="MUSICA: ON/OFF",screen=main_screen)
        self.button_return_main_menu = Button(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2+200,text="VOLVER AL MENU",screen=main_screen)

    def draw(self):        
        self.menu_pause_title.draw()
        self.menu_pause_subtitle.draw()
        self.button_resume.draw()
        self.button_return_main_menu.draw()
        self.button_level_restart.draw()
        self.button_options.draw()

    def events(self,spell_group_player,level_number):
        #ACCIONES DE BOTONES
        if(self.button_resume.button_pressed()):
            game_pause = False
        if(self.button_level_restart.button_pressed()):
            player = restart_player()
            level = restart_level(spell_group_player,spell_group_enemy,platform_group,items_group,level_number)
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
            enemies = restart_enemies(enemy_group,level_number)
            enemies.manage_enemies_update(player)
            enemy_group = enemies.managed_enemy_group
            spell_group_enemy = level.spell_group_enemy
            
            game_pause = False
            pygame.mixer.music.stop()
            level.generate_music()
            
        if(self.button_return_main_menu.button_pressed()):
            game_start = False
            menu_selected = "main"
            pygame.mixer.music.stop()
            pygame.mixer.music.load(PATH + r"\\music\\main_menu.wav")
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(-1,0.0,7000)
    
    def update(self,spell_group_player,level_number):
        self.draw()
        self.events(spell_group_player,level_number)


class Widget:
    def __init__ (self):
        
        pass

   

class Button(Widget):
    def __init__ (self,x,y,text,screen,font_size=25):
        Widget.__init__(self)
        self.font_size = font_size
        self.font = pygame.font.Font(PATH + r"\\font\\alagard.ttf",self.font_size)
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        self.image_text = self.font.render(self.text,True,(255,255,255))
        self.rect = self.image_text.get_rect()
        self.rect.center = (x,y)
        self.click = False
        self.click_option_sfx = pygame.mixer.Sound(PATH +r"\\sfx\\menu_select.wav")

    def draw(self):
        
        #mostrar texto en pantalla
        self.screen.blit(self.image_text,(self.rect.x,self.rect.y))

    def button_pressed(self):
        action = False
        #posicion del mouse
        pos = pygame.mouse.get_pos()

        #colision mouse/boton
        if (self.rect.collidepoint(pos)):
            if (pygame.mouse.get_pressed()[0] == 1 and self.click == False):
                action = True
                self.click = True
                self.click_option_sfx.set_volume(0.2)
                self.click_option_sfx.play()
            if (pygame.mouse.get_pressed()[0] == 0):
                action = False
        
        return action

    def update(self):
        self.draw()
        self.button_pressed()
        




