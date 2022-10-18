import pygame
import colores
from pygame.main import ANCHO_VENTANA

def crear_elemento_uno(ruta_imagen:str,x:int,y:int,ancho,alto):
    image_dos = pygame.image.load(ruta_imagen)
    image_dos = pygame.transform.scale(image_dos,(ancho,alto)) #modificar tamaño imagen
    rect_image_dos = image_dos.get_rect()#obtiene un "rectangulo" en base al tamaño de la dona
    rect_image_dos.x = x #posiciones del rectangulo
    rect_image_dos.y = y
    dict_elemento = {}
    dict_elemento["surface"] = image_dos
    dict_elemento["rect"] = rect_image_dos
    return dict_elemento

def actualizar_pantalla(lista_elementos,pantalla,personaje):
    for elemento in lista_elementos:
        if personaje["rect"].colliderect(elemento["rect"]): #detecta si hay una colision
            pass

        pygame.draw.rect(pantalla,colores.COLOR_BLANCO,elemento["rect"]) #creo rectangulo que me compare el "rectangulo" hitbox
        pantalla.blit(elemento["surface"],elemento["rect"])#fundir la imagen con la pantalla
    

def crear_lista_elementos(ruta_imagen:str,x:int,y:int,ancho,alto):
    lista_elementos = []
    for i in range(10):
        lista_elementos.append(elemento_dos = crear_elemento_uno(ruta_imagen,x+10,y,ancho,alto))#utiliza la funcion para crear elementos
    
    return lista_elementos



def mover_elemento():
    pass