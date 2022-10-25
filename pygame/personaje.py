import pygame
import colores

def crear_personaje(ruta_imagen:str,x:int,y:int,ancho,alto):
    image_dos = pygame.image.load(ruta_imagen)
    image_dos = pygame.transform.scale(image_dos,(ancho,alto)) #modificar tamaño imagen
    rect_image_dos = image_dos.get_rect()#obtiene un "rectangulo" en base al tamaño del elemento
    rect_image_dos.centerx = x #posiciones del rectangulo con referencia al centro
    rect_image_dos.centery = y
    dict_elemento = {}
    dict_elemento["surface"] = image_dos
    dict_elemento["rect"] = rect_image_dos
    return dict_elemento

def actualizar_pantalla(elemento,pantalla):
    pygame.draw.rect(pantalla,colores.COLOR_BLANCO,elemento["rect"]) #creo rectangulo que me compare el "rectangulo" hitbox
    pantalla.blit(elemento["surface"],elemento["rect"])#fundir la imagen con la pantalla
    
