from matplotlib.rcsetup import validate_int_or_None
import pygame
import math
import random
from constantes import *

class Tarjeta:
    
    def __init__(self,imagen_frente,imagen_reves,id,x,y):
                
        self.imagen_frente = imagen_frente
        self.imagen_reves = imagen_reves
        self.id = id
        self.x = x
        self.y = y
        self.lista = [imagen_frente,imagen_reves,id,x,y]

    def __str__(self):
        return "id:{0}".format(self.id)

    def __len__(self):
        return self.lista
    
    def __getitem__ (self,i):
        self.lista[i]
    
    def __iter__(self):
        for i in range(len(self.lista)):
            yield self.lista[i]






            
    