import pygame

class Auxiliar:
    @staticmethod
    def getSurfaceFromSpriteSheet(path,columnas,filas,flip=False, step = 1):
        lista = []
        surface_imagen = pygame.image.load(path)
        fotograma_ancho = int(surface_imagen.get_width()/columnas)
        fotograma_alto = int(surface_imagen.get_height()/filas)
        x = 0
        
        for fila in range(filas):
            for columna in range(0,columnas,step):
                x = columna * fotograma_ancho
                y = fila * fotograma_alto
                surface_fotograma = surface_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto)
                if(flip):
                    surface_fotograma = pygame.transform.flip(surface_fotograma,True,False)
                lista.append(surface_fotograma)
        return lista

class Auxiliar_2:
    @staticmethod
    def scrollingScreen(clock,scroll_speed,screen,bg,tiles,scroll):

        # THIS WILL MANAGE THE SPEED OF
        # THE SCROLLING IN PYGAME
        clock.tick(scroll_speed)
    
        # APPENDING THE IMAGE TO THE BACK
        # OF THE SAME IMAGE
        i = 0
        while(i < tiles):
            screen.blit(bg, (bg.get_width()*i+ scroll, 0))
            i += 1
        # FRAME FOR SCROLLING
        scroll -= 6
    
        # RESET THE SCROLL FRAME
        if abs(scroll) > bg.get_width():
            scroll = 0
        # CLOSINF THE FRAME OF SCROLLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
  
        pygame.display.update()


        
