from matplotlib.rcsetup import validate_int_or_None
import pygame
import math
import random
from constantes import *

class Tarjeta:
    
    def __init__(self,imagen_frente,imagen_reves,x,y,
    estado_descubierto,estado_visible,superficie_frente,
    superficie_reves,rectangulo):

        self.imagen_frente = imagen_frente
        self.imagen_reves = imagen_reves
        self.x = x
        self.y = y
        self.estado_descubierto = estado_descubierto
        self.estado_visible = estado_visible
        self.superficie_frente = superficie_frente
        self.superficie_reves = superficie_reves
        self.rectangulo = rectangulo
        self.lista = [imagen_frente,imagen_reves,x,y]

    def __str__(self):
        return "descubierto:{0}".format(self.estado_descubierto)

    def __len__(self):
        return self.lista
    
    def __getitem__ (self,i):
        self.lista[i]

    def __setitem__ (self,i,valor): 
        self.lista[i] = valor

    def __iter__(self):
        for i in range(len(self.lista)):
            yield self.lista[i]


def cantidad_tarjetas_descubiertas(lista_tarjetas):
    cantidad = 0
    for tarjeta in lista_tarjetas:
        if(tarjeta.estado_descubierto):
            cantidad += 1
    return cantidad
     

def cantidad_tarjetas_visibles_no_descubiertas(lista_tarjetas):
    cantidad = 0
    for tarjeta in lista_tarjetas:
        if(tarjeta.estado_visible and not tarjeta.estado_descubierto):
            cantidad += 1
    return cantidad
     
def match(lista_tarjetas):
    for index_p in range(len(lista_tarjetas)):
        if(lista_tarjetas[index_p].estado_visible and not lista_tarjetas[index_p].estado_descubierto):
            aux_primer_tarjeta = lista_tarjetas[index_p]
            for index_s in range(index_p+1,len(lista_tarjetas)):
                if(lista_tarjetas[index_s].estado_visible and not lista_tarjetas[index_s].estado_descubierto ):
                    aux_segunda_tarjeta = lista_tarjetas[index_s]
                    if(aux_primer_tarjeta.imagen_frente == aux_segunda_tarjeta.imagen_frente):
                        aux_primer_tarjeta.estado_descubierto=True
                        aux_segunda_tarjeta.estado_descubierto=True
                        return True
    return False







            
    