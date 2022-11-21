import json
import pygame
from constantes import *
from level import Level
from manager import *
from character import *




def show_text_on_screen(x,y,text,screen,font_size):
    font = pygame.font.Font(PATH + r"\\font\\alagard.ttf",font_size)
    image_text = font.render(text,True,(255,255,255))
    screen.blit(image_text,(x,y))




def draw_bg(screen):
    screen.fill((0,0,0))

def load_json(path:str)->list:
    with open(path,"r") as file:
        dic_file = json.load(file)

    return dic_file["levels"]

def restart_level(group_spells_player,group_spells_enemies,group_platforms,group_items,level_number):
    group_spells_player.empty()
    group_spells_enemies.empty()
    group_platforms.empty()
    group_items.empty()
    

    level_info = load_json(PATH + r"\\level\\level_info.json")

    level = Level(total_items=level_info[level_number]["number_max_items"],background=level_info[level_number]["background"],
    max_platforms=level_info[level_number]["number_max_platform"],platform_type=level_info[level_number]["platform_type"],
    platform_height=level_info[level_number]["platform_height"],platform_width=level_info[level_number]["platform_width"],
    music=level_info[level_number]["music"])
    
    return level

def restart_enemies(group_enemies,level_number):
    group_enemies.empty()

    level_info = load_json(PATH + r"\\level\\level_info.json")

    enemies = EnemyManager(total_enemies=level_info[level_number]["number_max_enemies"],
    enemy_type=level_info[level_number]["enemy_type"],enemy_timer=level_info[level_number]["enemy_timer"],
    enemy_health=level_info[level_number]["enemy_health"],enemy_scale=level_info[level_number]["enemy_scale"])

    return enemies

def restart_player():
    
    player = Character(char_type="player",x=200,y=200,speed=8,magic=5,health=100)

    return player
    


    
    




