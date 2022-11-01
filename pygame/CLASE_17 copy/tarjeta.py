from re import X
import pygame
import math
import random
from constantes import *
from tablero import *

class Tarjeta:
    def __init__(self,path_imagen,path_imagen_hide,x,y,l_tarjetas)->None:
        
        
        self.visible = False
        self.descubierto = False
        self.path_imagen = path_imagen
        self.path_imagen_hide = path_imagen_hide
        self.surface = pygame.transform.scale(pygame.image.load(self.path_imagen), (ANCHO_TARJETA,ALTO_TARJETA))
        self.surface_hide = pygame.transform.scale(pygame.image.load(self.path_imagen_hide), (ANCHO_TARJETA,ALTO_TARJETA))
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y
            


    def cantidad_tarjetas_descubiertas(self,lista_tarjetas):
        cantidad = 0
        for aux_tarjeta in lista_tarjetas:
            if(aux_tarjeta.descubierto):
                cantidad += 1
        return cantidad
        

    def cantidad_tarjetas_visibles_no_descubiertas(self,lista_tarjetas):
        cantidad = 0
        for aux_tarjeta in lista_tarjetas:
            if(aux_tarjeta.visible and not aux_tarjeta.descubierto):
                cantidad += 1
        return cantidad
        
    def match(self,lista_tarjetas):
        for index_p in range(len(lista_tarjetas)):
            if(lista_tarjetas[index_p].visible and not lista_tarjetas[index_p].descubierto):
                aux_primer_tarjeta = lista_tarjetas[index_p]
                for index_s in range(index_p+1,len(lista_tarjetas)):
                    if(lista_tarjetas[index_s].visible and not lista_tarjetas[index_s].descubierto ):
                        aux_segunda_tarjeta = lista_tarjetas[index_s]
                        if(aux_primer_tarjeta.path_imagen == aux_segunda_tarjeta.path_imagen):
                            aux_primer_tarjeta.descubierto=True
                            aux_segunda_tarjeta.descubierto=True
                            return True
        return False
