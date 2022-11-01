import pygame
import sys
from constantes import *
from player import *
from enemigo import *


screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()

imagen_fondo = pygame.image.load(PATH_IMAGE + r"locations\\forest\\all.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
player_1 = Player(x=0,y=0,speed_walk=4,speed_run=8,gravity=8,jump=16)

enemy_1 = Enemy(10,0,1,9)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_1.walk(DIRECCION_L)
            if event.key == pygame.K_RIGHT:
                player_1.walk(DIRECCION_R)
            if event.key == pygame.K_SPACE:
                player_1.jump(DIRECCION_R)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_SPACE:
                player_1.walk()

    screen.blit(imagen_fondo,imagen_fondo.get_rect())
   
    player_1.update()
    player_1.draw(screen)
    enemy_1.update()
    enemy_1.draw(screen)
    
    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel

    pygame.display.flip()
    
    delta_ms = clock.tick(FPS) #1000/FPS es la cantidad de veces que quiere entrar por segundo



    






