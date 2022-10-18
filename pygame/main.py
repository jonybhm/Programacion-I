import pygame #importa la bibioleta
import colores
import elementos
import personaje

pygame.init() #inicializa la bibioleta

#---------CONSTANTES-------------
ANCHO_VENTANA = 500
ALTO_VENTANA = 500


ventana_ppal = pygame.display.set_mode([ANCHO_VENTANA,ALTO_VENTANA]) #inicializa la pantalla con tamaño 500x500


#type de ventana_ppal de "pygame.SURFACE" , casi todo lo que se muestra en pantalla es de este tipo
#SURFACE es un buffer de pixeles

pygame.display.setcaption("PYGAME TEST") #nombre de la ventana

flag_run = True #flag para mantener corriendo el juego

timer_segundo = pygame.USEREVENT #setear un eventod de usuario, USEREVENT es un entero
pygame.time.set_timer(timer_segundo,1000) #cadencia en milisegundos

timer_2_segundo = pygame.USEREVENT + 1
pygame.time.set_timer(timer_segundo,2000) 

elemento_player = personaje.crear_personaje("imagen_uno.png",ANCHO_VENTANA/2,ALTO_VENTANA/2,50,50) #crear personaje

lista_elementos_dos = elementos.crear_lista_elementos("imagen_dos.png",0,0,50,50) #crear elemento

fuente = pygame.font.SysFont("Arial",30) #importo fuente
texto = fuente.render("HOLA",True,colores.COLOR_BLANCO) #renderiza un texto como superficie 
flag_mostrar_imagen_texto = False 

while flag_run:

    lista_eventos = pygame.event.get() #lista de eventos de pygame(mover mouse, presionar tecla, etc)son tipo "EVENT"
    for evento in lista_eventos:
        #los eventos se analizan en simultaneo, porlo que siempre entra con un if
        if evento.type == pygame.QUIT: #si el evento es QUIT el flag pasa a falso
            flag_run = False
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos) #muestra la posicion en (x,y)
            posicion_mouse = list(evento.pos) #asigno coordenadas a la posicion del circulo (tupla)
        
        if evento.type == pygame.USEREVENT: #evento de tiempo
            if evento.type == timer_segundo:
                elementos.mover_elemento()
            if evento.type == timer_2_segundo:
                flag_mostrar_imagen_texto = True

        if evento.type == pygame.KEYDOWN:#detecta cuando se presiona la tecla
            if evento.key == pygame.K_DOWN:#detecta tecla flecha abajo
                posicion_mouse[1] = posicion_mouse[1] + 10

    lista_teclas = pygame.key.get_pressed() #tira una lista de teclas que estan presionadas, NO es un evento                
    if lista_teclas[pygame.K_LEFT]: #pregunta si es True
        posicion_mouse[0] = posicion_mouse[0] + 10
    
    ventana_ppal.fill ([colores.COLOR_VERDE]) #le da un color         
    pygame.draw.rect(ventana_ppal,colores.COLOR_BLANCO,(30,60,100,200)) #dibujar rectangulo con coordenadas (x,y,ancho,alto)
    pygame.draw.circle(ventana_ppal,colores.COLOR_BLANCO,(posicion_mouse),80) #dibujar circulo con coordenadas (x,y,)diametro)
    
    #------------FUNDIR IMAGEN CON FONDO-------------------
    elementos.actualizar_pantalla(elemento_player,ventana_ppal)
    elementos.actualizar_pantalla(lista_elementos_dos,ventana_ppal)
   
   
   
    if flag_mostrar_imagen_texto:
        ventana_ppal.blit(texto,(50,50))#fundir texto con la pantalla

    pygame.display.flip() #muestra cambios al usuario, es la ultima linea del codigo

pygame.quit() #fin
