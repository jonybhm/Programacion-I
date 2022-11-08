import math
import pygame
import sys
from constantes import *
from player import Player
from auxiliar import *
from plataforma import *


screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Hollow Shadow")

imagen_scroll = pygame.image.load(PATH_IMAGE + r"level\\nivel0.png")
imagen_scroll = pygame.transform.scale(imagen_scroll,(ANCHO_VENTANA,ALTO_VENTANA))

scroll = 0 #variable scrolling
tiles = math.ceil(ANCHO_VENTANA /imagen_scroll.get_width()) + 1 #eliminar buffering


player_1 = Player(x=0,y=400,speed_move=15,frame_rate_ms=80,move_rate_ms=40)
lista_plataformas = []
lista_plataformas.append(Platform(x=400,y=500,w=150,h=90,type=0))
lista_plataformas.append(Platform(x=600,y=200,w=150,h=90,type=0))
lista_plataformas.append(Platform(x=900,y=400,w=150,h=90,type=0))


while True:

      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()


    delta_ms = clock.tick(FPS)
   

    clock.tick(90) #velocidad del scroll
  
    i = 0
    while(i < tiles):
        screen.blit(imagen_scroll, (imagen_scroll.get_width()*i+ scroll, 0)) #appendea la imagen de fondo al final de la misma imagen
        i += 1

        for plataforma in lista_plataformas:
            plataforma.draw(screen)

        player_1.events(delta_ms,keys)
        player_1.update(delta_ms)
        player_1.draw(screen)
   
    scroll -= 6  #frame para el scrolling
  
    
    if abs(scroll) > imagen_scroll.get_width():
        scroll = 0 #resetear el frame de scroll
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

  
    pygame.display.update()
    
    
    pygame.display.flip()
    



    


