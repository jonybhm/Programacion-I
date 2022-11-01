import pygame
import math
import random
from  tarjeta import * 
from constantes import *

class Tablero:

    def __init__ (self,cantidad_tarjetas,lista_tarjetas,temporizador):
        
        self.cantidad_tarjetas = cantidad_tarjetas
        self.lista_tarjetas = lista_tarjetas
        self.temporizador = temporizador
    
    def __str__(self):
        return "cantidad de tarjetas:{0}".format(self.cantidad_tarjetas)

    def __len__(self):
        return self.lista_tarjetas
    
    def __getitem__ (self,i):
        self.lista_tarjetas[i]

    def __setitem__ (self,i,valor): 
        self.lista_tarjetas[i] = valor

    def __iter__(self):
        for i in range(len(self.lista_tarjetas)):
            yield self.lista_tarjetas[i]


superficie_reves = pygame.transform.scale(pygame.image.load(PATH_RECURSOS+"00.png"), (ANCHO_TARJETA,ALTO_TARJETA))

lista_tarjetas_prueba = []
i = 1
for x in range(0,CANTIDAD_TARJETAS_H*ANCHO_TARJETA,ANCHO_TARJETA):
    for y in range(0,CANTIDAD_TARJETAS_V*ALTO_TARJETA,ALTO_TARJETA):
        if(i > CANTIDAD_TARJETAS_UNICAS):
            tarjeta_test = Tarjeta("0{0}.png".format(i-CANTIDAD_TARJETAS_UNICAS)
            ,r"00.png",x,y,False,False,
            pygame.transform.scale(pygame.image.load(PATH_RECURSOS+"0{0}.png".format(i-CANTIDAD_TARJETAS_UNICAS)), (ANCHO_TARJETA,ALTO_TARJETA)),
            superficie_reves,
            (pygame.transform.scale(pygame.image.load(PATH_RECURSOS+"0{0}.png".format(i-CANTIDAD_TARJETAS_UNICAS)), (ANCHO_TARJETA,ALTO_TARJETA)).get_rect()))
        else:
            tarjeta_test = Tarjeta("0{0}.png".format(i)
            ,r"00.png",x,y,False,False,
            pygame.transform.scale(pygame.image.load(PATH_RECURSOS+"0{0}.png".format(i)), (ANCHO_TARJETA,ALTO_TARJETA)),
            superficie_reves,
            (pygame.transform.scale(pygame.image.load(PATH_RECURSOS+"0{0}.png".format(i)), (ANCHO_TARJETA,ALTO_TARJETA)).get_rect()))
            
        lista_tarjetas_prueba.append(tarjeta_test)
        i = i + 1

tablero_prueba = Tablero(10,lista_tarjetas_prueba,0)

def colicion(tablero_prueba,pos_xy):
    '''
    verifica si existe una colicion alguna tarjetas del tablero y la coordenada recivida como parametro
    Recibe como parametro el tablero y una tupla (X,Y)
    Retorna el indice de la tarjeta que colisiono con la coordenada
    '''
    lista_tarjetas = tablero_prueba.lista_tarjetas
    if(cantidad_tarjetas_visibles_no_descubiertas(lista_tarjetas) < 2):
        for aux_tarjeta in lista_tarjetas:
            if(aux_tarjeta.rectangulo.collidepoint(pos_xy)):
                aux_tarjeta.estado_visibile=True
                tablero_prueba.temporizador = pygame.time.get_ticks()

def update(tablero_prueba):
    '''
    verifica si es necesario actualizar el estado de alguna tarjeta, en funcion de su propio estado y el de las otras
    Recibe como parametro el tablero y el tiempo transcurrido desde el ultimo llamado
    '''
    tiempo_actual = pygame.time.get_ticks()
    if(tiempo_actual - tablero_prueba.temporizador > 3000 and tablero_prueba.temporizador > 0):
        tablero_prueba.temporizador = 0
        lista_tarjetas = tablero_prueba.lista_tarjetas
        for aux_tarjeta in lista_tarjetas:
            if(aux_tarjeta.estado_descubierto==False):
                aux_tarjeta.estado_visibile=False
    
    if(tablero_prueba.temporizador > 0):
        if(match(tablero_prueba.lista_tarjetas)):
             tablero_prueba.temporizador = 0


def render(tablero_prueba,pantalla_juego):
    '''
    Dibuja todos los elementos del tablero en la superficie recibida como parametro
    Recibe como parametro el tablero
    '''
    lista_tarjetas = tablero_prueba.lista_tarjetas
    for tarjeta in lista_tarjetas:
        if(tarjeta.estado_visible):
            pantalla_juego.blit(tarjeta.superficie_frente,tarjeta.rectangulo)
        else:
            pantalla_juego.blit(tarjeta.superficie_reves,tarjeta.rectangulo)
     